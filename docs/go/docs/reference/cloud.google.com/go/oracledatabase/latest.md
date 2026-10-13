---
url: https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/
title: Oracle Database@Google Cloud API v1 - Package cloud.google.com/go/oracledatabase/apiv1 (v1.6.0) \u00a0|\u00a0 Go client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:08:39.861592+00:00
---

# Oracle Database@Google Cloud API v1 - Package cloud.google.com/go/oracledatabase/apiv1 (v1.6.0)  |  Go client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Go ](https://docs.cloud.google.com/go/docs)
  * [ Client libraries ](https://docs.cloud.google.com/go/docs/reference)



Send feedback 

#  Oracle Database@Google Cloud API v1 - Package cloud.google.com/go/oracledatabase/apiv1 (v1.6.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.6.0 (latest)  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.1  0.4.1  0.3.1  0.2.1  0.1.3 

**Note:** To get more information about this package, such as access to older versions, view [this package on pkg.go.dev](https://pkg.go.dev/cloud.google.com/go/oracledatabase/apiv1). 

Package oracledatabase is an auto-generated package for the Oracle Database@Google Cloud API. 

The Oracle Database@Google Cloud API provides a set of APIs to manage Oracle database services, such as Exadata and Autonomous Databases. 

## General documentation

For information that is relevant for all client libraries please reference <https://pkg.go.dev/cloud.google.com/go#pkg-overview>. Some information on this page includes: 

  * [Authentication and Authorization](https://pkg.go.dev/cloud.google.com/go#hdr-Authentication_and_Authorization)
  * [Timeouts and Cancellation](https://pkg.go.dev/cloud.google.com/go#hdr-Timeouts_and_Cancellation)
  * [Testing against Client Libraries](https://pkg.go.dev/cloud.google.com/go#hdr-Testing)
  * [Debugging Client Libraries](https://pkg.go.dev/cloud.google.com/go#hdr-Debugging)
  * [Inspecting errors](https://pkg.go.dev/cloud.google.com/go#hdr-Inspecting_errors)



## Example usage

To get started with this package, create a client.
    
    
    // go get cloud.google.com/go/oracledatabase/apiv1@latest
    ctx := context.Background()
    // This snippet has been automatically generated and should be regarded as a code template only.
    // It will require modifications to work:
    // - It may require correct/in-range values for request initialization.
    // - It may require specifying regional endpoints when creating the service client as shown in:
    //   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    c, err := oracledatabase.NewClient(ctx)
    if err != nil {
        // TODO: Handle error.
    }
    defer c.Close()

The client will use your default application credentials. Clients should be reused instead of created as needed. The methods of Client are safe for concurrent use by multiple goroutines. The returned client must be Closed when it is done being used. 

## Using the Client

The following is an example of making an API call with the newly created client, mentioned above.
    
    
    req := &oracledatabasepb.ConfigureExascaleCloudExadataInfrastructureRequest{
        // TODO: Fill request struct fields.
        // See https://pkg.go.dev/cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb#ConfigureExascaleCloudExadataInfrastructureRequest.
    }
    op, err := c.ConfigureExascaleCloudExadataInfrastructure(ctx, req)
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

The ctx passed to NewClient is used for authentication requests and for creating the underlying connection, but is not used for subsequent calls. Individual methods on the client use the ctx given to them. 

To close the open connection, use the Close() method.

## Functions 

### func DefaultAuthScopes 
    
    
    func DefaultAuthScopes() [][string](https://pkg.go.dev/builtin#string)

DefaultAuthScopes reports the default set of authentication scopes to use with this package.

## AutonomousDatabaseBackupIterator
    
    
    type AutonomousDatabaseBackupIterator struct {
    
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
    	InternalFetch func(pageSize [int](https://pkg.go.dev/builtin#int), pageToken [string](https://pkg.go.dev/builtin#string)) (results []*oracledatabasepb.AutonomousDatabaseBackup, nextPageToken [string](https://pkg.go.dev/builtin#string), err [error](https://pkg.go.dev/builtin#error))
    	// contains filtered or unexported fields
    }

AutonomousDatabaseBackupIterator manages a stream of *oracledatabasepb.AutonomousDatabaseBackup.

### func (*AutonomousDatabaseBackupIterator) All 
    
    
    func (it *AutonomousDatabaseBackupIterator) All() iter.Seq2[*oracledatabasepb.AutonomousDatabaseBackup, error]

All returns an iterator. If an error is returned by the iterator, the iterator will stop after that iteration.

### func (*AutonomousDatabaseBackupIterator) Next 
    
    
    func (it *AutonomousDatabaseBackupIterator) Next() (*[oracledatabasepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb).[AutonomousDatabaseBackup](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb#cloud_google_com_go_oracledatabase_apiv1_oracledatabasepb_AutonomousDatabaseBackup), [error](https://pkg.go.dev/builtin#error))

Next returns the next result. Its second return value is iterator.Done if there are no more results. Once Next returns Done, all subsequent calls will return Done.

### func (*AutonomousDatabaseBackupIterator) PageInfo 
    
    
    func (it *AutonomousDatabaseBackupIterator) PageInfo() *iterator.PageInfo

PageInfo supports pagination. See the [google.golang.org/api/iterator] package for details.

## AutonomousDatabaseCharacterSetIterator
    
    
    type AutonomousDatabaseCharacterSetIterator struct {
    
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
    	InternalFetch func(pageSize [int](https://pkg.go.dev/builtin#int), pageToken [string](https://pkg.go.dev/builtin#string)) (results []*oracledatabasepb.AutonomousDatabaseCharacterSet, nextPageToken [string](https://pkg.go.dev/builtin#string), err [error](https://pkg.go.dev/builtin#error))
    	// contains filtered or unexported fields
    }

AutonomousDatabaseCharacterSetIterator manages a stream of *oracledatabasepb.AutonomousDatabaseCharacterSet.

### func (*AutonomousDatabaseCharacterSetIterator) All 
    
    
    func (it *AutonomousDatabaseCharacterSetIterator) All() iter.Seq2[*oracledatabasepb.AutonomousDatabaseCharacterSet, error]

All returns an iterator. If an error is returned by the iterator, the iterator will stop after that iteration.

### func (*AutonomousDatabaseCharacterSetIterator) Next 
    
    
    func (it *AutonomousDatabaseCharacterSetIterator) Next() (*[oracledatabasepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb).[AutonomousDatabaseCharacterSet](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb#cloud_google_com_go_oracledatabase_apiv1_oracledatabasepb_AutonomousDatabaseCharacterSet), [error](https://pkg.go.dev/builtin#error))

Next returns the next result. Its second return value is iterator.Done if there are no more results. Once Next returns Done, all subsequent calls will return Done.

### func (*AutonomousDatabaseCharacterSetIterator) PageInfo 
    
    
    func (it *AutonomousDatabaseCharacterSetIterator) PageInfo() *iterator.PageInfo

PageInfo supports pagination. See the [google.golang.org/api/iterator] package for details.

## AutonomousDatabaseIterator
    
    
    type AutonomousDatabaseIterator struct {
    
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
    	InternalFetch func(pageSize [int](https://pkg.go.dev/builtin#int), pageToken [string](https://pkg.go.dev/builtin#string)) (results []*oracledatabasepb.AutonomousDatabase, nextPageToken [string](https://pkg.go.dev/builtin#string), err [error](https://pkg.go.dev/builtin#error))
    	// contains filtered or unexported fields
    }

AutonomousDatabaseIterator manages a stream of *oracledatabasepb.AutonomousDatabase.

### func (*AutonomousDatabaseIterator) All 
    
    
    func (it *AutonomousDatabaseIterator) All() iter.Seq2[*oracledatabasepb.AutonomousDatabase, error]

All returns an iterator. If an error is returned by the iterator, the iterator will stop after that iteration.

### func (*AutonomousDatabaseIterator) Next 
    
    
    func (it *AutonomousDatabaseIterator) Next() (*[oracledatabasepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb).[AutonomousDatabase](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb#cloud_google_com_go_oracledatabase_apiv1_oracledatabasepb_AutonomousDatabase), [error](https://pkg.go.dev/builtin#error))

Next returns the next result. Its second return value is iterator.Done if there are no more results. Once Next returns Done, all subsequent calls will return Done.

### func (*AutonomousDatabaseIterator) PageInfo 
    
    
    func (it *AutonomousDatabaseIterator) PageInfo() *iterator.PageInfo

PageInfo supports pagination. See the [google.golang.org/api/iterator] package for details.

## AutonomousDbVersionIterator
    
    
    type AutonomousDbVersionIterator struct {
    
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
    	InternalFetch func(pageSize [int](https://pkg.go.dev/builtin#int), pageToken [string](https://pkg.go.dev/builtin#string)) (results []*oracledatabasepb.AutonomousDbVersion, nextPageToken [string](https://pkg.go.dev/builtin#string), err [error](https://pkg.go.dev/builtin#error))
    	// contains filtered or unexported fields
    }

AutonomousDbVersionIterator manages a stream of *oracledatabasepb.AutonomousDbVersion.

### func (*AutonomousDbVersionIterator) All 
    
    
    func (it *AutonomousDbVersionIterator) All() iter.Seq2[*oracledatabasepb.AutonomousDbVersion, error]

All returns an iterator. If an error is returned by the iterator, the iterator will stop after that iteration.

### func (*AutonomousDbVersionIterator) Next 
    
    
    func (it *AutonomousDbVersionIterator) Next() (*[oracledatabasepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb).[AutonomousDbVersion](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb#cloud_google_com_go_oracledatabase_apiv1_oracledatabasepb_AutonomousDbVersion), [error](https://pkg.go.dev/builtin#error))

Next returns the next result. Its second return value is iterator.Done if there are no more results. Once Next returns Done, all subsequent calls will return Done.

### func (*AutonomousDbVersionIterator) PageInfo 
    
    
    func (it *AutonomousDbVersionIterator) PageInfo() *iterator.PageInfo

PageInfo supports pagination. See the [google.golang.org/api/iterator] package for details.

## CallOptions
    
    
    type CallOptions struct {
    	ListCloudExadataInfrastructures             []gax.CallOption
    	GetCloudExadataInfrastructure               []gax.CallOption
    	CreateCloudExadataInfrastructure            []gax.CallOption
    	DeleteCloudExadataInfrastructure            []gax.CallOption
    	ConfigureExascaleCloudExadataInfrastructure []gax.CallOption
    	ListCloudVmClusters                         []gax.CallOption
    	GetCloudVmCluster                           []gax.CallOption
    	CreateCloudVmCluster                        []gax.CallOption
    	DeleteCloudVmCluster                        []gax.CallOption
    	ListEntitlements                            []gax.CallOption
    	ListDbServers                               []gax.CallOption
    	ListDbNodes                                 []gax.CallOption
    	ListGiVersions                              []gax.CallOption
    	ListMinorVersions                           []gax.CallOption
    	ListDbSystemShapes                          []gax.CallOption
    	ListAutonomousDatabases                     []gax.CallOption
    	GetAutonomousDatabase                       []gax.CallOption
    	CreateAutonomousDatabase                    []gax.CallOption
    	UpdateAutonomousDatabase                    []gax.CallOption
    	DeleteAutonomousDatabase                    []gax.CallOption
    	RestoreAutonomousDatabase                   []gax.CallOption
    	GenerateAutonomousDatabaseWallet            []gax.CallOption
    	ListAutonomousDbVersions                    []gax.CallOption
    	ListAutonomousDatabaseCharacterSets         []gax.CallOption
    	ListAutonomousDatabaseBackups               []gax.CallOption
    	StopAutonomousDatabase                      []gax.CallOption
    	StartAutonomousDatabase                     []gax.CallOption
    	RestartAutonomousDatabase                   []gax.CallOption
    	SwitchoverAutonomousDatabase                []gax.CallOption
    	FailoverAutonomousDatabase                  []gax.CallOption
    	RefreshAutonomousDatabase                   []gax.CallOption
    	GetAutonomousDatabaseRefreshableClones      []gax.CallOption
    	ListOdbNetworks                             []gax.CallOption
    	GetOdbNetwork                               []gax.CallOption
    	CreateOdbNetwork                            []gax.CallOption
    	DeleteOdbNetwork                            []gax.CallOption
    	ListOdbSubnets                              []gax.CallOption
    	GetOdbSubnet                                []gax.CallOption
    	CreateOdbSubnet                             []gax.CallOption
    	DeleteOdbSubnet                             []gax.CallOption
    	ListExadbVmClusters                         []gax.CallOption
    	GetExadbVmCluster                           []gax.CallOption
    	CreateExadbVmCluster                        []gax.CallOption
    	DeleteExadbVmCluster                        []gax.CallOption
    	UpdateExadbVmCluster                        []gax.CallOption
    	RemoveVirtualMachineExadbVmCluster          []gax.CallOption
    	ListExascaleDbStorageVaults                 []gax.CallOption
    	GetExascaleDbStorageVault                   []gax.CallOption
    	CreateExascaleDbStorageVault                []gax.CallOption
    	DeleteExascaleDbStorageVault                []gax.CallOption
    	ListDbSystemInitialStorageSizes             []gax.CallOption
    	ListDatabases                               []gax.CallOption
    	GetDatabase                                 []gax.CallOption
    	ListPluggableDatabases                      []gax.CallOption
    	GetPluggableDatabase                        []gax.CallOption
    	ListDbSystems                               []gax.CallOption
    	GetDbSystem                                 []gax.CallOption
    	CreateDbSystem                              []gax.CallOption
    	DeleteDbSystem                              []gax.CallOption
    	ListGoldengateDeployments                   []gax.CallOption
    	GetGoldengateDeployment                     []gax.CallOption
    	CreateGoldengateDeployment                  []gax.CallOption
    	DeleteGoldengateDeployment                  []gax.CallOption
    	StopGoldengateDeployment                    []gax.CallOption
    	StartGoldengateDeployment                   []gax.CallOption
    	ListGoldengateConnections                   []gax.CallOption
    	GetGoldengateConnection                     []gax.CallOption
    	CreateGoldengateConnection                  []gax.CallOption
    	DeleteGoldengateConnection                  []gax.CallOption
    	ListGoldengateDeploymentVersions            []gax.CallOption
    	ListGoldengateDeploymentTypes               []gax.CallOption
    	ListGoldengateDeploymentEnvironments        []gax.CallOption
    	ListGoldengateConnectionTypes               []gax.CallOption
    	ListDbVersions                              []gax.CallOption
    	ListDatabaseCharacterSets                   []gax.CallOption
    	ListGoldengateConnectionAssignments         []gax.CallOption
    	GetGoldengateConnectionAssignment           []gax.CallOption
    	CreateGoldengateConnectionAssignment        []gax.CallOption
    	DeleteGoldengateConnectionAssignment        []gax.CallOption
    	TestGoldengateConnectionAssignment          []gax.CallOption
    	GetLocation                                 []gax.CallOption
    	ListLocations                               []gax.CallOption
    	CancelOperation                             []gax.CallOption
    	DeleteOperation                             []gax.CallOption
    	GetOperation                                []gax.CallOption
    	ListOperations                              []gax.CallOption
    }

CallOptions contains the retry settings for each method of Client.

## Client
    
    
    type Client struct {
    
    	// The call options for this service.
    	CallOptions *CallOptions
    
    	// LROClient is used internally to handle long-running operations.
    	// It is exposed so that its CallOptions can be modified if required.
    	// Users should not Close this client.
    	LROClient *lroauto.OperationsClient
    	// contains filtered or unexported fields
    }

Client is a client for interacting with Oracle Database@Google Cloud API. Methods, except Close, may be called concurrently. However, fields must not be modified concurrently with method calls.

Service describing handlers for resources

### func NewClient 
    
    
    func NewClient(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...option.ClientOption) (*Client, [error](https://pkg.go.dev/builtin#error))

NewClient creates a new oracle database client based on gRPC. The returned client must be Closed when it is done being used to clean up its underlying connections.

Service describing handlers for resources

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	oracledatabase "cloud.google.com/go/oracledatabase/apiv1"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := oracledatabase.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_Close)()
    
    	// TODO: Use client.
    	_ = c
    }
    

### func NewRESTClient 
    
    
    func NewRESTClient(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...option.ClientOption) (*Client, [error](https://pkg.go.dev/builtin#error))

NewRESTClient creates a new oracle database rest client.

Service describing handlers for resources

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	oracledatabase "cloud.google.com/go/oracledatabase/apiv1"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := oracledatabase.[NewRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_NewRESTClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_Close)()
    
    	// TODO: Use client.
    	_ = c
    }
    

### func (*Client) CancelOperation 
    
    
    func (c *Client) CancelOperation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[CancelOperationRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#CancelOperationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

CancelOperation is a utility method from google.longrunning.Operations.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    	oracledatabase "cloud.google.com/go/oracledatabase/apiv1"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := oracledatabase.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_Close)()
    
    	req := &longrunningpb.[CancelOperationRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_CancelOperationRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#CancelOperationRequest.
    	}
    	err = c.CancelOperation(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    }
    

### func (*Client) Close 
    
    
    func (c *Client) Close() [error](https://pkg.go.dev/builtin#error)

Close closes the connection to the API service. **Always** call Close() when the client is no longer required.

### func (*Client) ConfigureExascaleCloudExadataInfrastructure 
    
    
    func (c *Client) ConfigureExascaleCloudExadataInfrastructure(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[oracledatabasepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb).[ConfigureExascaleCloudExadataInfrastructureRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb#cloud_google_com_go_oracledatabase_apiv1_oracledatabasepb_ConfigureExascaleCloudExadataInfrastructureRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*ConfigureExascaleCloudExadataInfrastructureOperation, [error](https://pkg.go.dev/builtin#error))

ConfigureExascaleCloudExadataInfrastructure configures Exascale for a single Exadata Infrastructure.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	oracledatabase "cloud.google.com/go/oracledatabase/apiv1"
    
    	oracledatabasepb "cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := oracledatabase.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_Close)()
    
    	req := &oracledatabasepb.ConfigureExascaleCloudExadataInfrastructureRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb#ConfigureExascaleCloudExadataInfrastructureRequest.
    	}
    	op, err := c.ConfigureExascaleCloudExadataInfrastructure(ctx, req)
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
    

### func (*Client) ConfigureExascaleCloudExadataInfrastructureOperation 
    
    
    func (c *Client) ConfigureExascaleCloudExadataInfrastructureOperation(name [string](https://pkg.go.dev/builtin#string)) *ConfigureExascaleCloudExadataInfrastructureOperation

ConfigureExascaleCloudExadataInfrastructureOperation returns a new ConfigureExascaleCloudExadataInfrastructureOperation from a given name. The name must be that of a previously created ConfigureExascaleCloudExadataInfrastructureOperation, possibly from a different process.

### func (*Client) Connection (deprecated)
    
    
    func (c *Client) Connection() *grpc.ClientConn

Connection returns a connection to the API service.

Deprecated: Connections are now pooled so this method does not always return the same resource.

### func (*Client) CreateAutonomousDatabase 
    
    
    func (c *Client) CreateAutonomousDatabase(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[oracledatabasepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb).[CreateAutonomousDatabaseRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb#cloud_google_com_go_oracledatabase_apiv1_oracledatabasepb_CreateAutonomousDatabaseRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*CreateAutonomousDatabaseOperation, [error](https://pkg.go.dev/builtin#error))

CreateAutonomousDatabase creates a new Autonomous Database in a given project and location.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	oracledatabase "cloud.google.com/go/oracledatabase/apiv1"
    
    	oracledatabasepb "cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := oracledatabase.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_Close)()
    
    	req := &oracledatabasepb.CreateAutonomousDatabaseRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb#CreateAutonomousDatabaseRequest.
    	}
    	op, err := c.CreateAutonomousDatabase(ctx, req)
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
    

### func (*Client) CreateAutonomousDatabaseOperation 
    
    
    func (c *Client) CreateAutonomousDatabaseOperation(name [string](https://pkg.go.dev/builtin#string)) *CreateAutonomousDatabaseOperation

CreateAutonomousDatabaseOperation returns a new CreateAutonomousDatabaseOperation from a given name. The name must be that of a previously created CreateAutonomousDatabaseOperation, possibly from a different process.

### func (*Client) CreateCloudExadataInfrastructure 
    
    
    func (c *Client) CreateCloudExadataInfrastructure(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[oracledatabasepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb).[CreateCloudExadataInfrastructureRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb#cloud_google_com_go_oracledatabase_apiv1_oracledatabasepb_CreateCloudExadataInfrastructureRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*CreateCloudExadataInfrastructureOperation, [error](https://pkg.go.dev/builtin#error))

CreateCloudExadataInfrastructure creates a new Exadata Infrastructure in a given project and location.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	oracledatabase "cloud.google.com/go/oracledatabase/apiv1"
    
    	oracledatabasepb "cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := oracledatabase.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_Close)()
    
    	req := &oracledatabasepb.CreateCloudExadataInfrastructureRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb#CreateCloudExadataInfrastructureRequest.
    	}
    	op, err := c.CreateCloudExadataInfrastructure(ctx, req)
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
    

### func (*Client) CreateCloudExadataInfrastructureOperation 
    
    
    func (c *Client) CreateCloudExadataInfrastructureOperation(name [string](https://pkg.go.dev/builtin#string)) *CreateCloudExadataInfrastructureOperation

CreateCloudExadataInfrastructureOperation returns a new CreateCloudExadataInfrastructureOperation from a given name. The name must be that of a previously created CreateCloudExadataInfrastructureOperation, possibly from a different process.

### func (*Client) CreateCloudVmCluster 
    
    
    func (c *Client) CreateCloudVmCluster(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[oracledatabasepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb).[CreateCloudVmClusterRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb#cloud_google_com_go_oracledatabase_apiv1_oracledatabasepb_CreateCloudVmClusterRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*CreateCloudVmClusterOperation, [error](https://pkg.go.dev/builtin#error))

CreateCloudVmCluster creates a new VM Cluster in a given project and location.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	oracledatabase "cloud.google.com/go/oracledatabase/apiv1"
    
    	oracledatabasepb "cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := oracledatabase.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_Close)()
    
    	req := &oracledatabasepb.CreateCloudVmClusterRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb#CreateCloudVmClusterRequest.
    	}
    	op, err := c.CreateCloudVmCluster(ctx, req)
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
    

### func (*Client) CreateCloudVmClusterOperation 
    
    
    func (c *Client) CreateCloudVmClusterOperation(name [string](https://pkg.go.dev/builtin#string)) *CreateCloudVmClusterOperation

CreateCloudVmClusterOperation returns a new CreateCloudVmClusterOperation from a given name. The name must be that of a previously created CreateCloudVmClusterOperation, possibly from a different process.

### func (*Client) CreateDbSystem 
    
    
    func (c *Client) CreateDbSystem(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[oracledatabasepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb).[CreateDbSystemRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb#cloud_google_com_go_oracledatabase_apiv1_oracledatabasepb_CreateDbSystemRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*CreateDbSystemOperation, [error](https://pkg.go.dev/builtin#error))

CreateDbSystem creates a new DbSystem in a given project and location.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	oracledatabase "cloud.google.com/go/oracledatabase/apiv1"
    
    	oracledatabasepb "cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := oracledatabase.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_Close)()
    
    	req := &oracledatabasepb.CreateDbSystemRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb#CreateDbSystemRequest.
    	}
    	op, err := c.CreateDbSystem(ctx, req)
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
    

### func (*Client) CreateDbSystemOperation 
    
    
    func (c *Client) CreateDbSystemOperation(name [string](https://pkg.go.dev/builtin#string)) *CreateDbSystemOperation

CreateDbSystemOperation returns a new CreateDbSystemOperation from a given name. The name must be that of a previously created CreateDbSystemOperation, possibly from a different process.

### func (*Client) CreateExadbVmCluster 
    
    
    func (c *Client) CreateExadbVmCluster(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[oracledatabasepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb).[CreateExadbVmClusterRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb#cloud_google_com_go_oracledatabase_apiv1_oracledatabasepb_CreateExadbVmClusterRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*CreateExadbVmClusterOperation, [error](https://pkg.go.dev/builtin#error))

CreateExadbVmCluster creates a new Exadb (Exascale) VM Cluster resource.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	oracledatabase "cloud.google.com/go/oracledatabase/apiv1"
    
    	oracledatabasepb "cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := oracledatabase.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_Close)()
    
    	req := &oracledatabasepb.CreateExadbVmClusterRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb#CreateExadbVmClusterRequest.
    	}
    	op, err := c.CreateExadbVmCluster(ctx, req)
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
    

### func (*Client) CreateExadbVmClusterOperation 
    
    
    func (c *Client) CreateExadbVmClusterOperation(name [string](https://pkg.go.dev/builtin#string)) *CreateExadbVmClusterOperation

CreateExadbVmClusterOperation returns a new CreateExadbVmClusterOperation from a given name. The name must be that of a previously created CreateExadbVmClusterOperation, possibly from a different process.

### func (*Client) CreateExascaleDbStorageVault 
    
    
    func (c *Client) CreateExascaleDbStorageVault(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[oracledatabasepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb).[CreateExascaleDbStorageVaultRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb#cloud_google_com_go_oracledatabase_apiv1_oracledatabasepb_CreateExascaleDbStorageVaultRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*CreateExascaleDbStorageVaultOperation, [error](https://pkg.go.dev/builtin#error))

CreateExascaleDbStorageVault creates a new ExascaleDB Storage Vault resource.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	oracledatabase "cloud.google.com/go/oracledatabase/apiv1"
    
    	oracledatabasepb "cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := oracledatabase.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_Close)()
    
    	req := &oracledatabasepb.CreateExascaleDbStorageVaultRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb#CreateExascaleDbStorageVaultRequest.
    	}
    	op, err := c.CreateExascaleDbStorageVault(ctx, req)
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
    

### func (*Client) CreateExascaleDbStorageVaultOperation 
    
    
    func (c *Client) CreateExascaleDbStorageVaultOperation(name [string](https://pkg.go.dev/builtin#string)) *CreateExascaleDbStorageVaultOperation

CreateExascaleDbStorageVaultOperation returns a new CreateExascaleDbStorageVaultOperation from a given name. The name must be that of a previously created CreateExascaleDbStorageVaultOperation, possibly from a different process.

### func (*Client) CreateGoldengateConnection 
    
    
    func (c *Client) CreateGoldengateConnection(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[oracledatabasepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb).[CreateGoldengateConnectionRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb#cloud_google_com_go_oracledatabase_apiv1_oracledatabasepb_CreateGoldengateConnectionRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*CreateGoldengateConnectionOperation, [error](https://pkg.go.dev/builtin#error))

CreateGoldengateConnection creates a new GoldengateConnection in a given project and location.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	oracledatabase "cloud.google.com/go/oracledatabase/apiv1"
    
    	oracledatabasepb "cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := oracledatabase.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_Close)()
    
    	req := &oracledatabasepb.CreateGoldengateConnectionRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb#CreateGoldengateConnectionRequest.
    	}
    	op, err := c.CreateGoldengateConnection(ctx, req)
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
    

### func (*Client) CreateGoldengateConnectionAssignment 
    
    
    func (c *Client) CreateGoldengateConnectionAssignment(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[oracledatabasepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb).[CreateGoldengateConnectionAssignmentRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb#cloud_google_com_go_oracledatabase_apiv1_oracledatabasepb_CreateGoldengateConnectionAssignmentRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*CreateGoldengateConnectionAssignmentOperation, [error](https://pkg.go.dev/builtin#error))

CreateGoldengateConnectionAssignment creates a new GoldengateConnectionAssignment in a given project and location.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	oracledatabase "cloud.google.com/go/oracledatabase/apiv1"
    
    	oracledatabasepb "cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := oracledatabase.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_Close)()
    
    	req := &oracledatabasepb.CreateGoldengateConnectionAssignmentRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb#CreateGoldengateConnectionAssignmentRequest.
    	}
    	op, err := c.CreateGoldengateConnectionAssignment(ctx, req)
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
    

### func (*Client) CreateGoldengateConnectionAssignmentOperation 
    
    
    func (c *Client) CreateGoldengateConnectionAssignmentOperation(name [string](https://pkg.go.dev/builtin#string)) *CreateGoldengateConnectionAssignmentOperation

CreateGoldengateConnectionAssignmentOperation returns a new CreateGoldengateConnectionAssignmentOperation from a given name. The name must be that of a previously created CreateGoldengateConnectionAssignmentOperation, possibly from a different process.

### func (*Client) CreateGoldengateConnectionOperation 
    
    
    func (c *Client) CreateGoldengateConnectionOperation(name [string](https://pkg.go.dev/builtin#string)) *CreateGoldengateConnectionOperation

CreateGoldengateConnectionOperation returns a new CreateGoldengateConnectionOperation from a given name. The name must be that of a previously created CreateGoldengateConnectionOperation, possibly from a different process.

### func (*Client) CreateGoldengateDeployment 
    
    
    func (c *Client) CreateGoldengateDeployment(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[oracledatabasepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb).[CreateGoldengateDeploymentRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb#cloud_google_com_go_oracledatabase_apiv1_oracledatabasepb_CreateGoldengateDeploymentRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*CreateGoldengateDeploymentOperation, [error](https://pkg.go.dev/builtin#error))

CreateGoldengateDeployment creates a new GoldengateDeployment in a given project and location.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	oracledatabase "cloud.google.com/go/oracledatabase/apiv1"
    
    	oracledatabasepb "cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := oracledatabase.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_Close)()
    
    	req := &oracledatabasepb.CreateGoldengateDeploymentRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb#CreateGoldengateDeploymentRequest.
    	}
    	op, err := c.CreateGoldengateDeployment(ctx, req)
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
    

### func (*Client) CreateGoldengateDeploymentOperation 
    
    
    func (c *Client) CreateGoldengateDeploymentOperation(name [string](https://pkg.go.dev/builtin#string)) *CreateGoldengateDeploymentOperation

CreateGoldengateDeploymentOperation returns a new CreateGoldengateDeploymentOperation from a given name. The name must be that of a previously created CreateGoldengateDeploymentOperation, possibly from a different process.

### func (*Client) CreateOdbNetwork 
    
    
    func (c *Client) CreateOdbNetwork(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[oracledatabasepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb).[CreateOdbNetworkRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb#cloud_google_com_go_oracledatabase_apiv1_oracledatabasepb_CreateOdbNetworkRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*CreateOdbNetworkOperation, [error](https://pkg.go.dev/builtin#error))

CreateOdbNetwork creates a new ODB Network in a given project and location.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	oracledatabase "cloud.google.com/go/oracledatabase/apiv1"
    
    	oracledatabasepb "cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := oracledatabase.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_Close)()
    
    	req := &oracledatabasepb.CreateOdbNetworkRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb#CreateOdbNetworkRequest.
    	}
    	op, err := c.CreateOdbNetwork(ctx, req)
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
    

### func (*Client) CreateOdbNetworkOperation 
    
    
    func (c *Client) CreateOdbNetworkOperation(name [string](https://pkg.go.dev/builtin#string)) *CreateOdbNetworkOperation

CreateOdbNetworkOperation returns a new CreateOdbNetworkOperation from a given name. The name must be that of a previously created CreateOdbNetworkOperation, possibly from a different process.

### func (*Client) CreateOdbSubnet 
    
    
    func (c *Client) CreateOdbSubnet(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[oracledatabasepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb).[CreateOdbSubnetRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb#cloud_google_com_go_oracledatabase_apiv1_oracledatabasepb_CreateOdbSubnetRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*CreateOdbSubnetOperation, [error](https://pkg.go.dev/builtin#error))

CreateOdbSubnet creates a new ODB Subnet in a given ODB Network.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	oracledatabase "cloud.google.com/go/oracledatabase/apiv1"
    
    	oracledatabasepb "cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := oracledatabase.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_Close)()
    
    	req := &oracledatabasepb.CreateOdbSubnetRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb#CreateOdbSubnetRequest.
    	}
    	op, err := c.CreateOdbSubnet(ctx, req)
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
    

### func (*Client) CreateOdbSubnetOperation 
    
    
    func (c *Client) CreateOdbSubnetOperation(name [string](https://pkg.go.dev/builtin#string)) *CreateOdbSubnetOperation

CreateOdbSubnetOperation returns a new CreateOdbSubnetOperation from a given name. The name must be that of a previously created CreateOdbSubnetOperation, possibly from a different process.

### func (*Client) DeleteAutonomousDatabase 
    
    
    func (c *Client) DeleteAutonomousDatabase(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[oracledatabasepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb).[DeleteAutonomousDatabaseRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb#cloud_google_com_go_oracledatabase_apiv1_oracledatabasepb_DeleteAutonomousDatabaseRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*DeleteAutonomousDatabaseOperation, [error](https://pkg.go.dev/builtin#error))

DeleteAutonomousDatabase deletes a single Autonomous Database.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	oracledatabase "cloud.google.com/go/oracledatabase/apiv1"
    
    	oracledatabasepb "cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := oracledatabase.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_Close)()
    
    	req := &oracledatabasepb.DeleteAutonomousDatabaseRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb#DeleteAutonomousDatabaseRequest.
    	}
    	op, err := c.DeleteAutonomousDatabase(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    
    	err = op.Wait(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    }
    

### func (*Client) DeleteAutonomousDatabaseOperation 
    
    
    func (c *Client) DeleteAutonomousDatabaseOperation(name [string](https://pkg.go.dev/builtin#string)) *DeleteAutonomousDatabaseOperation

DeleteAutonomousDatabaseOperation returns a new DeleteAutonomousDatabaseOperation from a given name. The name must be that of a previously created DeleteAutonomousDatabaseOperation, possibly from a different process.

### func (*Client) DeleteCloudExadataInfrastructure 
    
    
    func (c *Client) DeleteCloudExadataInfrastructure(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[oracledatabasepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb).[DeleteCloudExadataInfrastructureRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb#cloud_google_com_go_oracledatabase_apiv1_oracledatabasepb_DeleteCloudExadataInfrastructureRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*DeleteCloudExadataInfrastructureOperation, [error](https://pkg.go.dev/builtin#error))

DeleteCloudExadataInfrastructure deletes a single Exadata Infrastructure.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	oracledatabase "cloud.google.com/go/oracledatabase/apiv1"
    
    	oracledatabasepb "cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := oracledatabase.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_Close)()
    
    	req := &oracledatabasepb.DeleteCloudExadataInfrastructureRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb#DeleteCloudExadataInfrastructureRequest.
    	}
    	op, err := c.DeleteCloudExadataInfrastructure(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    
    	err = op.Wait(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    }
    

### func (*Client) DeleteCloudExadataInfrastructureOperation 
    
    
    func (c *Client) DeleteCloudExadataInfrastructureOperation(name [string](https://pkg.go.dev/builtin#string)) *DeleteCloudExadataInfrastructureOperation

DeleteCloudExadataInfrastructureOperation returns a new DeleteCloudExadataInfrastructureOperation from a given name. The name must be that of a previously created DeleteCloudExadataInfrastructureOperation, possibly from a different process.

### func (*Client) DeleteCloudVmCluster 
    
    
    func (c *Client) DeleteCloudVmCluster(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[oracledatabasepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb).[DeleteCloudVmClusterRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb#cloud_google_com_go_oracledatabase_apiv1_oracledatabasepb_DeleteCloudVmClusterRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*DeleteCloudVmClusterOperation, [error](https://pkg.go.dev/builtin#error))

DeleteCloudVmCluster deletes a single VM Cluster.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	oracledatabase "cloud.google.com/go/oracledatabase/apiv1"
    
    	oracledatabasepb "cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := oracledatabase.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_Close)()
    
    	req := &oracledatabasepb.DeleteCloudVmClusterRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb#DeleteCloudVmClusterRequest.
    	}
    	op, err := c.DeleteCloudVmCluster(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    
    	err = op.Wait(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    }
    

### func (*Client) DeleteCloudVmClusterOperation 
    
    
    func (c *Client) DeleteCloudVmClusterOperation(name [string](https://pkg.go.dev/builtin#string)) *DeleteCloudVmClusterOperation

DeleteCloudVmClusterOperation returns a new DeleteCloudVmClusterOperation from a given name. The name must be that of a previously created DeleteCloudVmClusterOperation, possibly from a different process.

### func (*Client) DeleteDbSystem 
    
    
    func (c *Client) DeleteDbSystem(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[oracledatabasepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb).[DeleteDbSystemRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb#cloud_google_com_go_oracledatabase_apiv1_oracledatabasepb_DeleteDbSystemRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*DeleteDbSystemOperation, [error](https://pkg.go.dev/builtin#error))

DeleteDbSystem deletes a single DbSystem.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	oracledatabase "cloud.google.com/go/oracledatabase/apiv1"
    
    	oracledatabasepb "cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := oracledatabase.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_Close)()
    
    	req := &oracledatabasepb.DeleteDbSystemRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb#DeleteDbSystemRequest.
    	}
    	op, err := c.DeleteDbSystem(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    
    	err = op.Wait(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    }
    

### func (*Client) DeleteDbSystemOperation 
    
    
    func (c *Client) DeleteDbSystemOperation(name [string](https://pkg.go.dev/builtin#string)) *DeleteDbSystemOperation

DeleteDbSystemOperation returns a new DeleteDbSystemOperation from a given name. The name must be that of a previously created DeleteDbSystemOperation, possibly from a different process.

### func (*Client) DeleteExadbVmCluster 
    
    
    func (c *Client) DeleteExadbVmCluster(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[oracledatabasepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb).[DeleteExadbVmClusterRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb#cloud_google_com_go_oracledatabase_apiv1_oracledatabasepb_DeleteExadbVmClusterRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*DeleteExadbVmClusterOperation, [error](https://pkg.go.dev/builtin#error))

DeleteExadbVmCluster deletes a single Exadb (Exascale) VM Cluster.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	oracledatabase "cloud.google.com/go/oracledatabase/apiv1"
    
    	oracledatabasepb "cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := oracledatabase.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_Close)()
    
    	req := &oracledatabasepb.DeleteExadbVmClusterRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb#DeleteExadbVmClusterRequest.
    	}
    	op, err := c.DeleteExadbVmCluster(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    
    	err = op.Wait(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    }
    

### func (*Client) DeleteExadbVmClusterOperation 
    
    
    func (c *Client) DeleteExadbVmClusterOperation(name [string](https://pkg.go.dev/builtin#string)) *DeleteExadbVmClusterOperation

DeleteExadbVmClusterOperation returns a new DeleteExadbVmClusterOperation from a given name. The name must be that of a previously created DeleteExadbVmClusterOperation, possibly from a different process.

### func (*Client) DeleteExascaleDbStorageVault 
    
    
    func (c *Client) DeleteExascaleDbStorageVault(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[oracledatabasepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb).[DeleteExascaleDbStorageVaultRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb#cloud_google_com_go_oracledatabase_apiv1_oracledatabasepb_DeleteExascaleDbStorageVaultRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*DeleteExascaleDbStorageVaultOperation, [error](https://pkg.go.dev/builtin#error))

DeleteExascaleDbStorageVault deletes a single ExascaleDB Storage Vault.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	oracledatabase "cloud.google.com/go/oracledatabase/apiv1"
    
    	oracledatabasepb "cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := oracledatabase.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_Close)()
    
    	req := &oracledatabasepb.DeleteExascaleDbStorageVaultRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb#DeleteExascaleDbStorageVaultRequest.
    	}
    	op, err := c.DeleteExascaleDbStorageVault(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    
    	err = op.Wait(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    }
    

### func (*Client) DeleteExascaleDbStorageVaultOperation 
    
    
    func (c *Client) DeleteExascaleDbStorageVaultOperation(name [string](https://pkg.go.dev/builtin#string)) *DeleteExascaleDbStorageVaultOperation

DeleteExascaleDbStorageVaultOperation returns a new DeleteExascaleDbStorageVaultOperation from a given name. The name must be that of a previously created DeleteExascaleDbStorageVaultOperation, possibly from a different process.

### func (*Client) DeleteGoldengateConnection 
    
    
    func (c *Client) DeleteGoldengateConnection(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[oracledatabasepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb).[DeleteGoldengateConnectionRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb#cloud_google_com_go_oracledatabase_apiv1_oracledatabasepb_DeleteGoldengateConnectionRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*DeleteGoldengateConnectionOperation, [error](https://pkg.go.dev/builtin#error))

DeleteGoldengateConnection deletes a single GoldengateConnection.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	oracledatabase "cloud.google.com/go/oracledatabase/apiv1"
    
    	oracledatabasepb "cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := oracledatabase.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_Close)()
    
    	req := &oracledatabasepb.DeleteGoldengateConnectionRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb#DeleteGoldengateConnectionRequest.
    	}
    	op, err := c.DeleteGoldengateConnection(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    
    	err = op.Wait(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    }
    

### func (*Client) DeleteGoldengateConnectionAssignment 
    
    
    func (c *Client) DeleteGoldengateConnectionAssignment(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[oracledatabasepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb).[DeleteGoldengateConnectionAssignmentRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb#cloud_google_com_go_oracledatabase_apiv1_oracledatabasepb_DeleteGoldengateConnectionAssignmentRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*DeleteGoldengateConnectionAssignmentOperation, [error](https://pkg.go.dev/builtin#error))

DeleteGoldengateConnectionAssignment deletes a single GoldengateConnectionAssignment.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	oracledatabase "cloud.google.com/go/oracledatabase/apiv1"
    
    	oracledatabasepb "cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := oracledatabase.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_Close)()
    
    	req := &oracledatabasepb.DeleteGoldengateConnectionAssignmentRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb#DeleteGoldengateConnectionAssignmentRequest.
    	}
    	op, err := c.DeleteGoldengateConnectionAssignment(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    
    	err = op.Wait(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    }
    

### func (*Client) DeleteGoldengateConnectionAssignmentOperation 
    
    
    func (c *Client) DeleteGoldengateConnectionAssignmentOperation(name [string](https://pkg.go.dev/builtin#string)) *DeleteGoldengateConnectionAssignmentOperation

DeleteGoldengateConnectionAssignmentOperation returns a new DeleteGoldengateConnectionAssignmentOperation from a given name. The name must be that of a previously created DeleteGoldengateConnectionAssignmentOperation, possibly from a different process.

### func (*Client) DeleteGoldengateConnectionOperation 
    
    
    func (c *Client) DeleteGoldengateConnectionOperation(name [string](https://pkg.go.dev/builtin#string)) *DeleteGoldengateConnectionOperation

DeleteGoldengateConnectionOperation returns a new DeleteGoldengateConnectionOperation from a given name. The name must be that of a previously created DeleteGoldengateConnectionOperation, possibly from a different process.

### func (*Client) DeleteGoldengateDeployment 
    
    
    func (c *Client) DeleteGoldengateDeployment(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[oracledatabasepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb).[DeleteGoldengateDeploymentRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb#cloud_google_com_go_oracledatabase_apiv1_oracledatabasepb_DeleteGoldengateDeploymentRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*DeleteGoldengateDeploymentOperation, [error](https://pkg.go.dev/builtin#error))

DeleteGoldengateDeployment deletes a single GoldengateDeployment.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	oracledatabase "cloud.google.com/go/oracledatabase/apiv1"
    
    	oracledatabasepb "cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := oracledatabase.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_Close)()
    
    	req := &oracledatabasepb.DeleteGoldengateDeploymentRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb#DeleteGoldengateDeploymentRequest.
    	}
    	op, err := c.DeleteGoldengateDeployment(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    
    	err = op.Wait(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    }
    

### func (*Client) DeleteGoldengateDeploymentOperation 
    
    
    func (c *Client) DeleteGoldengateDeploymentOperation(name [string](https://pkg.go.dev/builtin#string)) *DeleteGoldengateDeploymentOperation

DeleteGoldengateDeploymentOperation returns a new DeleteGoldengateDeploymentOperation from a given name. The name must be that of a previously created DeleteGoldengateDeploymentOperation, possibly from a different process.

### func (*Client) DeleteOdbNetwork 
    
    
    func (c *Client) DeleteOdbNetwork(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[oracledatabasepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb).[DeleteOdbNetworkRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb#cloud_google_com_go_oracledatabase_apiv1_oracledatabasepb_DeleteOdbNetworkRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*DeleteOdbNetworkOperation, [error](https://pkg.go.dev/builtin#error))

DeleteOdbNetwork deletes a single ODB Network.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	oracledatabase "cloud.google.com/go/oracledatabase/apiv1"
    
    	oracledatabasepb "cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := oracledatabase.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_Close)()
    
    	req := &oracledatabasepb.DeleteOdbNetworkRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb#DeleteOdbNetworkRequest.
    	}
    	op, err := c.DeleteOdbNetwork(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    
    	err = op.Wait(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    }
    

### func (*Client) DeleteOdbNetworkOperation 
    
    
    func (c *Client) DeleteOdbNetworkOperation(name [string](https://pkg.go.dev/builtin#string)) *DeleteOdbNetworkOperation

DeleteOdbNetworkOperation returns a new DeleteOdbNetworkOperation from a given name. The name must be that of a previously created DeleteOdbNetworkOperation, possibly from a different process.

### func (*Client) DeleteOdbSubnet 
    
    
    func (c *Client) DeleteOdbSubnet(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[oracledatabasepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb).[DeleteOdbSubnetRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb#cloud_google_com_go_oracledatabase_apiv1_oracledatabasepb_DeleteOdbSubnetRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*DeleteOdbSubnetOperation, [error](https://pkg.go.dev/builtin#error))

DeleteOdbSubnet deletes a single ODB Subnet.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	oracledatabase "cloud.google.com/go/oracledatabase/apiv1"
    
    	oracledatabasepb "cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := oracledatabase.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_Close)()
    
    	req := &oracledatabasepb.DeleteOdbSubnetRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb#DeleteOdbSubnetRequest.
    	}
    	op, err := c.DeleteOdbSubnet(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    
    	err = op.Wait(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    }
    

### func (*Client) DeleteOdbSubnetOperation 
    
    
    func (c *Client) DeleteOdbSubnetOperation(name [string](https://pkg.go.dev/builtin#string)) *DeleteOdbSubnetOperation

DeleteOdbSubnetOperation returns a new DeleteOdbSubnetOperation from a given name. The name must be that of a previously created DeleteOdbSubnetOperation, possibly from a different process.

### func (*Client) DeleteOperation 
    
    
    func (c *Client) DeleteOperation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[DeleteOperationRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#DeleteOperationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

DeleteOperation is a utility method from google.longrunning.Operations.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    	oracledatabase "cloud.google.com/go/oracledatabase/apiv1"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := oracledatabase.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_Close)()
    
    	req := &longrunningpb.[DeleteOperationRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_DeleteOperationRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#DeleteOperationRequest.
    	}
    	err = c.DeleteOperation(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    }
    

### func (*Client) FailoverAutonomousDatabase 
    
    
    func (c *Client) FailoverAutonomousDatabase(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[oracledatabasepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb).[FailoverAutonomousDatabaseRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb#cloud_google_com_go_oracledatabase_apiv1_oracledatabasepb_FailoverAutonomousDatabaseRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*FailoverAutonomousDatabaseOperation, [error](https://pkg.go.dev/builtin#error))

FailoverAutonomousDatabase initiates a failover to target autonomous database from the associated primary database.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	oracledatabase "cloud.google.com/go/oracledatabase/apiv1"
    
    	oracledatabasepb "cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := oracledatabase.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_Close)()
    
    	req := &oracledatabasepb.FailoverAutonomousDatabaseRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb#FailoverAutonomousDatabaseRequest.
    	}
    	op, err := c.FailoverAutonomousDatabase(ctx, req)
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
    

### func (*Client) FailoverAutonomousDatabaseOperation 
    
    
    func (c *Client) FailoverAutonomousDatabaseOperation(name [string](https://pkg.go.dev/builtin#string)) *FailoverAutonomousDatabaseOperation

FailoverAutonomousDatabaseOperation returns a new FailoverAutonomousDatabaseOperation from a given name. The name must be that of a previously created FailoverAutonomousDatabaseOperation, possibly from a different process.

### func (*Client) GenerateAutonomousDatabaseWallet 
    
    
    func (c *Client) GenerateAutonomousDatabaseWallet(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[oracledatabasepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb).[GenerateAutonomousDatabaseWalletRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb#cloud_google_com_go_oracledatabase_apiv1_oracledatabasepb_GenerateAutonomousDatabaseWalletRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[oracledatabasepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb).[GenerateAutonomousDatabaseWalletResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb#cloud_google_com_go_oracledatabase_apiv1_oracledatabasepb_GenerateAutonomousDatabaseWalletResponse), [error](https://pkg.go.dev/builtin#error))

GenerateAutonomousDatabaseWallet generates a wallet for an Autonomous Database.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	oracledatabase "cloud.google.com/go/oracledatabase/apiv1"
    
    	oracledatabasepb "cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := oracledatabase.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_Close)()
    
    	req := &oracledatabasepb.GenerateAutonomousDatabaseWalletRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb#GenerateAutonomousDatabaseWalletRequest.
    	}
    	resp, err := c.GenerateAutonomousDatabaseWallet(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*Client) GetAutonomousDatabase 
    
    
    func (c *Client) GetAutonomousDatabase(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[oracledatabasepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb).[GetAutonomousDatabaseRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb#cloud_google_com_go_oracledatabase_apiv1_oracledatabasepb_GetAutonomousDatabaseRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[oracledatabasepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb).[AutonomousDatabase](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb#cloud_google_com_go_oracledatabase_apiv1_oracledatabasepb_AutonomousDatabase), [error](https://pkg.go.dev/builtin#error))

GetAutonomousDatabase gets the details of a single Autonomous Database.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	oracledatabase "cloud.google.com/go/oracledatabase/apiv1"
    
    	oracledatabasepb "cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := oracledatabase.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_Close)()
    
    	req := &oracledatabasepb.GetAutonomousDatabaseRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb#GetAutonomousDatabaseRequest.
    	}
    	resp, err := c.GetAutonomousDatabase(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*Client) GetAutonomousDatabaseRefreshableClones 
    
    
    func (c *Client) GetAutonomousDatabaseRefreshableClones(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[oracledatabasepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb).[GetAutonomousDatabaseRefreshableClonesRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb#cloud_google_com_go_oracledatabase_apiv1_oracledatabasepb_GetAutonomousDatabaseRefreshableClonesRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[oracledatabasepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb).[AutonomousDatabaseRefreshableClones](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb#cloud_google_com_go_oracledatabase_apiv1_oracledatabasepb_AutonomousDatabaseRefreshableClones), [error](https://pkg.go.dev/builtin#error))

GetAutonomousDatabaseRefreshableClones gets the refreshable clones for a given Autonomous Database.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	oracledatabase "cloud.google.com/go/oracledatabase/apiv1"
    
    	oracledatabasepb "cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := oracledatabase.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_Close)()
    
    	req := &oracledatabasepb.GetAutonomousDatabaseRefreshableClonesRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb#GetAutonomousDatabaseRefreshableClonesRequest.
    	}
    	resp, err := c.GetAutonomousDatabaseRefreshableClones(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*Client) GetCloudExadataInfrastructure 
    
    
    func (c *Client) GetCloudExadataInfrastructure(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[oracledatabasepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb).[GetCloudExadataInfrastructureRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb#cloud_google_com_go_oracledatabase_apiv1_oracledatabasepb_GetCloudExadataInfrastructureRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[oracledatabasepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb).[CloudExadataInfrastructure](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb#cloud_google_com_go_oracledatabase_apiv1_oracledatabasepb_CloudExadataInfrastructure), [error](https://pkg.go.dev/builtin#error))

GetCloudExadataInfrastructure gets details of a single Exadata Infrastructure.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	oracledatabase "cloud.google.com/go/oracledatabase/apiv1"
    
    	oracledatabasepb "cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := oracledatabase.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_Close)()
    
    	req := &oracledatabasepb.GetCloudExadataInfrastructureRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb#GetCloudExadataInfrastructureRequest.
    	}
    	resp, err := c.GetCloudExadataInfrastructure(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*Client) GetCloudVmCluster 
    
    
    func (c *Client) GetCloudVmCluster(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[oracledatabasepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb).[GetCloudVmClusterRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb#cloud_google_com_go_oracledatabase_apiv1_oracledatabasepb_GetCloudVmClusterRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[oracledatabasepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb).[CloudVmCluster](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb#cloud_google_com_go_oracledatabase_apiv1_oracledatabasepb_CloudVmCluster), [error](https://pkg.go.dev/builtin#error))

GetCloudVmCluster gets details of a single VM Cluster.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	oracledatabase "cloud.google.com/go/oracledatabase/apiv1"
    
    	oracledatabasepb "cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := oracledatabase.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_Close)()
    
    	req := &oracledatabasepb.GetCloudVmClusterRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb#GetCloudVmClusterRequest.
    	}
    	resp, err := c.GetCloudVmCluster(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*Client) GetDatabase 
    
    
    func (c *Client) GetDatabase(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[oracledatabasepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb).[GetDatabaseRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb#cloud_google_com_go_oracledatabase_apiv1_oracledatabasepb_GetDatabaseRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[oracledatabasepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb).[Database](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb#cloud_google_com_go_oracledatabase_apiv1_oracledatabasepb_Database), [error](https://pkg.go.dev/builtin#error))

GetDatabase gets details of a single Database.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	oracledatabase "cloud.google.com/go/oracledatabase/apiv1"
    
    	oracledatabasepb "cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := oracledatabase.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_Close)()
    
    	req := &oracledatabasepb.GetDatabaseRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb#GetDatabaseRequest.
    	}
    	resp, err := c.GetDatabase(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*Client) GetDbSystem 
    
    
    func (c *Client) GetDbSystem(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[oracledatabasepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb).[GetDbSystemRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb#cloud_google_com_go_oracledatabase_apiv1_oracledatabasepb_GetDbSystemRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[oracledatabasepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb).[DbSystem](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb#cloud_google_com_go_oracledatabase_apiv1_oracledatabasepb_DbSystem), [error](https://pkg.go.dev/builtin#error))

GetDbSystem gets details of a single DbSystem.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	oracledatabase "cloud.google.com/go/oracledatabase/apiv1"
    
    	oracledatabasepb "cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := oracledatabase.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_Close)()
    
    	req := &oracledatabasepb.GetDbSystemRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb#GetDbSystemRequest.
    	}
    	resp, err := c.GetDbSystem(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*Client) GetExadbVmCluster 
    
    
    func (c *Client) GetExadbVmCluster(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[oracledatabasepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb).[GetExadbVmClusterRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb#cloud_google_com_go_oracledatabase_apiv1_oracledatabasepb_GetExadbVmClusterRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[oracledatabasepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb).[ExadbVmCluster](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb#cloud_google_com_go_oracledatabase_apiv1_oracledatabasepb_ExadbVmCluster), [error](https://pkg.go.dev/builtin#error))

GetExadbVmCluster gets details of a single Exadb (Exascale) VM Cluster.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	oracledatabase "cloud.google.com/go/oracledatabase/apiv1"
    
    	oracledatabasepb "cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := oracledatabase.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_Close)()
    
    	req := &oracledatabasepb.GetExadbVmClusterRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb#GetExadbVmClusterRequest.
    	}
    	resp, err := c.GetExadbVmCluster(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*Client) GetExascaleDbStorageVault 
    
    
    func (c *Client) GetExascaleDbStorageVault(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[oracledatabasepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb).[GetExascaleDbStorageVaultRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb#cloud_google_com_go_oracledatabase_apiv1_oracledatabasepb_GetExascaleDbStorageVaultRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[oracledatabasepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb).[ExascaleDbStorageVault](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb#cloud_google_com_go_oracledatabase_apiv1_oracledatabasepb_ExascaleDbStorageVault), [error](https://pkg.go.dev/builtin#error))

GetExascaleDbStorageVault gets details of a single ExascaleDB Storage Vault.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	oracledatabase "cloud.google.com/go/oracledatabase/apiv1"
    
    	oracledatabasepb "cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := oracledatabase.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_Close)()
    
    	req := &oracledatabasepb.GetExascaleDbStorageVaultRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb#GetExascaleDbStorageVaultRequest.
    	}
    	resp, err := c.GetExascaleDbStorageVault(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*Client) GetGoldengateConnection 
    
    
    func (c *Client) GetGoldengateConnection(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[oracledatabasepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb).[GetGoldengateConnectionRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb#cloud_google_com_go_oracledatabase_apiv1_oracledatabasepb_GetGoldengateConnectionRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[oracledatabasepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb).[GoldengateConnection](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb#cloud_google_com_go_oracledatabase_apiv1_oracledatabasepb_GoldengateConnection), [error](https://pkg.go.dev/builtin#error))

GetGoldengateConnection gets details of a single GoldengateConnection.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	oracledatabase "cloud.google.com/go/oracledatabase/apiv1"
    
    	oracledatabasepb "cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := oracledatabase.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_Close)()
    
    	req := &oracledatabasepb.GetGoldengateConnectionRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb#GetGoldengateConnectionRequest.
    	}
    	resp, err := c.GetGoldengateConnection(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*Client) GetGoldengateConnectionAssignment 
    
    
    func (c *Client) GetGoldengateConnectionAssignment(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[oracledatabasepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb).[GetGoldengateConnectionAssignmentRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb#cloud_google_com_go_oracledatabase_apiv1_oracledatabasepb_GetGoldengateConnectionAssignmentRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[oracledatabasepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb).[GoldengateConnectionAssignment](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb#cloud_google_com_go_oracledatabase_apiv1_oracledatabasepb_GoldengateConnectionAssignment), [error](https://pkg.go.dev/builtin#error))

GetGoldengateConnectionAssignment gets details of a single GoldengateConnectionAssignment.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	oracledatabase "cloud.google.com/go/oracledatabase/apiv1"
    
    	oracledatabasepb "cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := oracledatabase.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_Close)()
    
    	req := &oracledatabasepb.GetGoldengateConnectionAssignmentRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb#GetGoldengateConnectionAssignmentRequest.
    	}
    	resp, err := c.GetGoldengateConnectionAssignment(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*Client) GetGoldengateDeployment 
    
    
    func (c *Client) GetGoldengateDeployment(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[oracledatabasepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb).[GetGoldengateDeploymentRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb#cloud_google_com_go_oracledatabase_apiv1_oracledatabasepb_GetGoldengateDeploymentRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[oracledatabasepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb).[GoldengateDeployment](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb#cloud_google_com_go_oracledatabase_apiv1_oracledatabasepb_GoldengateDeployment), [error](https://pkg.go.dev/builtin#error))

GetGoldengateDeployment gets details of a single GoldengateDeployment.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	oracledatabase "cloud.google.com/go/oracledatabase/apiv1"
    
    	oracledatabasepb "cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := oracledatabase.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_Close)()
    
    	req := &oracledatabasepb.GetGoldengateDeploymentRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb#GetGoldengateDeploymentRequest.
    	}
    	resp, err := c.GetGoldengateDeployment(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*Client) GetLocation 
    
    
    func (c *Client) GetLocation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[locationpb](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location).[GetLocationRequest](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#GetLocationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[locationpb](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location).[Location](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#Location), [error](https://pkg.go.dev/builtin#error))

GetLocation gets information about a location.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	oracledatabase "cloud.google.com/go/oracledatabase/apiv1"
    
    	locationpb "google.golang.org/genproto/googleapis/cloud/location"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := oracledatabase.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_Close)()
    
    	req := &locationpb.GetLocationRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#GetLocationRequest.
    	}
    	resp, err := c.[GetLocation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_GetLocation)(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*Client) GetOdbNetwork 
    
    
    func (c *Client) GetOdbNetwork(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[oracledatabasepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb).[GetOdbNetworkRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb#cloud_google_com_go_oracledatabase_apiv1_oracledatabasepb_GetOdbNetworkRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[oracledatabasepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb).[OdbNetwork](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb#cloud_google_com_go_oracledatabase_apiv1_oracledatabasepb_OdbNetwork), [error](https://pkg.go.dev/builtin#error))

GetOdbNetwork gets details of a single ODB Network.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	oracledatabase "cloud.google.com/go/oracledatabase/apiv1"
    
    	oracledatabasepb "cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := oracledatabase.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_Close)()
    
    	req := &oracledatabasepb.GetOdbNetworkRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb#GetOdbNetworkRequest.
    	}
    	resp, err := c.GetOdbNetwork(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*Client) GetOdbSubnet 
    
    
    func (c *Client) GetOdbSubnet(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[oracledatabasepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb).[GetOdbSubnetRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb#cloud_google_com_go_oracledatabase_apiv1_oracledatabasepb_GetOdbSubnetRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[oracledatabasepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb).[OdbSubnet](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb#cloud_google_com_go_oracledatabase_apiv1_oracledatabasepb_OdbSubnet), [error](https://pkg.go.dev/builtin#error))

GetOdbSubnet gets details of a single ODB Subnet.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	oracledatabase "cloud.google.com/go/oracledatabase/apiv1"
    
    	oracledatabasepb "cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := oracledatabase.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_Close)()
    
    	req := &oracledatabasepb.GetOdbSubnetRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb#GetOdbSubnetRequest.
    	}
    	resp, err := c.GetOdbSubnet(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*Client) GetOperation 
    
    
    func (c *Client) GetOperation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[GetOperationRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#GetOperationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[Operation](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#Operation), [error](https://pkg.go.dev/builtin#error))

GetOperation is a utility method from google.longrunning.Operations.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    	oracledatabase "cloud.google.com/go/oracledatabase/apiv1"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := oracledatabase.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_Close)()
    
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
    

### func (*Client) GetPluggableDatabase 
    
    
    func (c *Client) GetPluggableDatabase(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[oracledatabasepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb).[GetPluggableDatabaseRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb#cloud_google_com_go_oracledatabase_apiv1_oracledatabasepb_GetPluggableDatabaseRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[oracledatabasepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb).[PluggableDatabase](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb#cloud_google_com_go_oracledatabase_apiv1_oracledatabasepb_PluggableDatabase), [error](https://pkg.go.dev/builtin#error))

GetPluggableDatabase gets details of a single PluggableDatabase.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	oracledatabase "cloud.google.com/go/oracledatabase/apiv1"
    
    	oracledatabasepb "cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := oracledatabase.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_Close)()
    
    	req := &oracledatabasepb.GetPluggableDatabaseRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb#GetPluggableDatabaseRequest.
    	}
    	resp, err := c.GetPluggableDatabase(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*Client) ListAutonomousDatabaseBackups 
    
    
    func (c *Client) ListAutonomousDatabaseBackups(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[oracledatabasepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb).[ListAutonomousDatabaseBackupsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb#cloud_google_com_go_oracledatabase_apiv1_oracledatabasepb_ListAutonomousDatabaseBackupsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *AutonomousDatabaseBackupIterator

ListAutonomousDatabaseBackups lists the long-term and automatic backups of an Autonomous Database.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	oracledatabase "cloud.google.com/go/oracledatabase/apiv1"
    
    	oracledatabasepb "cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := oracledatabase.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_Close)()
    
    	req := &oracledatabasepb.ListAutonomousDatabaseBackupsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb#ListAutonomousDatabaseBackupsRequest.
    	}
    	it := c.ListAutonomousDatabaseBackups(ctx, req)
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
    		_ = it.Response.(*oracledatabasepb.ListAutonomousDatabaseBackupsResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	oracledatabase "cloud.google.com/go/oracledatabase/apiv1"
    
    	oracledatabasepb "cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := oracledatabase.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_Close)()
    
    	req := &oracledatabasepb.ListAutonomousDatabaseBackupsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb#ListAutonomousDatabaseBackupsRequest.
    	}
    	for resp, err := range c.ListAutonomousDatabaseBackups(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*Client) ListAutonomousDatabaseCharacterSets 
    
    
    func (c *Client) ListAutonomousDatabaseCharacterSets(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[oracledatabasepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb).[ListAutonomousDatabaseCharacterSetsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb#cloud_google_com_go_oracledatabase_apiv1_oracledatabasepb_ListAutonomousDatabaseCharacterSetsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *AutonomousDatabaseCharacterSetIterator

ListAutonomousDatabaseCharacterSets lists Autonomous Database Character Sets in a given project and location.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	oracledatabase "cloud.google.com/go/oracledatabase/apiv1"
    
    	oracledatabasepb "cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := oracledatabase.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_Close)()
    
    	req := &oracledatabasepb.ListAutonomousDatabaseCharacterSetsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb#ListAutonomousDatabaseCharacterSetsRequest.
    	}
    	it := c.ListAutonomousDatabaseCharacterSets(ctx, req)
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
    		_ = it.Response.(*oracledatabasepb.ListAutonomousDatabaseCharacterSetsResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	oracledatabase "cloud.google.com/go/oracledatabase/apiv1"
    
    	oracledatabasepb "cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := oracledatabase.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_Close)()
    
    	req := &oracledatabasepb.ListAutonomousDatabaseCharacterSetsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb#ListAutonomousDatabaseCharacterSetsRequest.
    	}
    	for resp, err := range c.ListAutonomousDatabaseCharacterSets(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*Client) ListAutonomousDatabases 
    
    
    func (c *Client) ListAutonomousDatabases(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[oracledatabasepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb).[ListAutonomousDatabasesRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb#cloud_google_com_go_oracledatabase_apiv1_oracledatabasepb_ListAutonomousDatabasesRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *AutonomousDatabaseIterator

ListAutonomousDatabases lists the Autonomous Databases in a given project and location.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	oracledatabase "cloud.google.com/go/oracledatabase/apiv1"
    
    	oracledatabasepb "cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := oracledatabase.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_Close)()
    
    	req := &oracledatabasepb.ListAutonomousDatabasesRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb#ListAutonomousDatabasesRequest.
    	}
    	it := c.ListAutonomousDatabases(ctx, req)
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
    		_ = it.Response.(*oracledatabasepb.ListAutonomousDatabasesResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	oracledatabase "cloud.google.com/go/oracledatabase/apiv1"
    
    	oracledatabasepb "cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := oracledatabase.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_Close)()
    
    	req := &oracledatabasepb.ListAutonomousDatabasesRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb#ListAutonomousDatabasesRequest.
    	}
    	for resp, err := range c.ListAutonomousDatabases(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*Client) ListAutonomousDbVersions 
    
    
    func (c *Client) ListAutonomousDbVersions(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[oracledatabasepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb).[ListAutonomousDbVersionsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb#cloud_google_com_go_oracledatabase_apiv1_oracledatabasepb_ListAutonomousDbVersionsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *AutonomousDbVersionIterator

ListAutonomousDbVersions lists all the available Autonomous Database versions for a project and location.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	oracledatabase "cloud.google.com/go/oracledatabase/apiv1"
    
    	oracledatabasepb "cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := oracledatabase.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_Close)()
    
    	req := &oracledatabasepb.ListAutonomousDbVersionsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb#ListAutonomousDbVersionsRequest.
    	}
    	it := c.ListAutonomousDbVersions(ctx, req)
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
    		_ = it.Response.(*oracledatabasepb.ListAutonomousDbVersionsResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	oracledatabase "cloud.google.com/go/oracledatabase/apiv1"
    
    	oracledatabasepb "cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := oracledatabase.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_Close)()
    
    	req := &oracledatabasepb.ListAutonomousDbVersionsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb#ListAutonomousDbVersionsRequest.
    	}
    	for resp, err := range c.ListAutonomousDbVersions(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*Client) ListCloudExadataInfrastructures 
    
    
    func (c *Client) ListCloudExadataInfrastructures(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[oracledatabasepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb).[ListCloudExadataInfrastructuresRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb#cloud_google_com_go_oracledatabase_apiv1_oracledatabasepb_ListCloudExadataInfrastructuresRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *CloudExadataInfrastructureIterator

ListCloudExadataInfrastructures lists Exadata Infrastructures in a given project and location.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	oracledatabase "cloud.google.com/go/oracledatabase/apiv1"
    
    	oracledatabasepb "cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := oracledatabase.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_Close)()
    
    	req := &oracledatabasepb.ListCloudExadataInfrastructuresRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb#ListCloudExadataInfrastructuresRequest.
    	}
    	it := c.ListCloudExadataInfrastructures(ctx, req)
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
    		_ = it.Response.(*oracledatabasepb.ListCloudExadataInfrastructuresResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	oracledatabase "cloud.google.com/go/oracledatabase/apiv1"
    
    	oracledatabasepb "cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := oracledatabase.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_Close)()
    
    	req := &oracledatabasepb.ListCloudExadataInfrastructuresRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb#ListCloudExadataInfrastructuresRequest.
    	}
    	for resp, err := range c.ListCloudExadataInfrastructures(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*Client) ListCloudVmClusters 
    
    
    func (c *Client) ListCloudVmClusters(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[oracledatabasepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb).[ListCloudVmClustersRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb#cloud_google_com_go_oracledatabase_apiv1_oracledatabasepb_ListCloudVmClustersRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *CloudVmClusterIterator

ListCloudVmClusters lists the VM Clusters in a given project and location.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	oracledatabase "cloud.google.com/go/oracledatabase/apiv1"
    
    	oracledatabasepb "cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := oracledatabase.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_Close)()
    
    	req := &oracledatabasepb.ListCloudVmClustersRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb#ListCloudVmClustersRequest.
    	}
    	it := c.ListCloudVmClusters(ctx, req)
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
    		_ = it.Response.(*oracledatabasepb.ListCloudVmClustersResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	oracledatabase "cloud.google.com/go/oracledatabase/apiv1"
    
    	oracledatabasepb "cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := oracledatabase.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_Close)()
    
    	req := &oracledatabasepb.ListCloudVmClustersRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb#ListCloudVmClustersRequest.
    	}
    	for resp, err := range c.ListCloudVmClusters(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*Client) ListDatabaseCharacterSets 
    
    
    func (c *Client) ListDatabaseCharacterSets(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[oracledatabasepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb).[ListDatabaseCharacterSetsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb#cloud_google_com_go_oracledatabase_apiv1_oracledatabasepb_ListDatabaseCharacterSetsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *DatabaseCharacterSetIterator

ListDatabaseCharacterSets list DatabaseCharacterSets for the given project and location.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	oracledatabase "cloud.google.com/go/oracledatabase/apiv1"
    
    	oracledatabasepb "cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := oracledatabase.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_Close)()
    
    	req := &oracledatabasepb.ListDatabaseCharacterSetsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb#ListDatabaseCharacterSetsRequest.
    	}
    	it := c.ListDatabaseCharacterSets(ctx, req)
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
    		_ = it.Response.(*oracledatabasepb.ListDatabaseCharacterSetsResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	oracledatabase "cloud.google.com/go/oracledatabase/apiv1"
    
    	oracledatabasepb "cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := oracledatabase.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_Close)()
    
    	req := &oracledatabasepb.ListDatabaseCharacterSetsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb#ListDatabaseCharacterSetsRequest.
    	}
    	for resp, err := range c.ListDatabaseCharacterSets(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*Client) ListDatabases 
    
    
    func (c *Client) ListDatabases(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[oracledatabasepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb).[ListDatabasesRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb#cloud_google_com_go_oracledatabase_apiv1_oracledatabasepb_ListDatabasesRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *DatabaseIterator

ListDatabases lists all the Databases for the given project, location and DbSystem.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	oracledatabase "cloud.google.com/go/oracledatabase/apiv1"
    
    	oracledatabasepb "cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := oracledatabase.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_Close)()
    
    	req := &oracledatabasepb.ListDatabasesRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb#ListDatabasesRequest.
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
    		_ = it.Response.(*oracledatabasepb.ListDatabasesResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	oracledatabase "cloud.google.com/go/oracledatabase/apiv1"
    
    	oracledatabasepb "cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := oracledatabase.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_Close)()
    
    	req := &oracledatabasepb.ListDatabasesRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb#ListDatabasesRequest.
    	}
    	for resp, err := range c.ListDatabases(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*Client) ListDbNodes 
    
    
    func (c *Client) ListDbNodes(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[oracledatabasepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb).[ListDbNodesRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb#cloud_google_com_go_oracledatabase_apiv1_oracledatabasepb_ListDbNodesRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *DbNodeIterator

ListDbNodes lists the database nodes of a VM Cluster.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	oracledatabase "cloud.google.com/go/oracledatabase/apiv1"
    
    	oracledatabasepb "cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := oracledatabase.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_Close)()
    
    	req := &oracledatabasepb.ListDbNodesRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb#ListDbNodesRequest.
    	}
    	it := c.ListDbNodes(ctx, req)
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
    		_ = it.Response.(*oracledatabasepb.ListDbNodesResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	oracledatabase "cloud.google.com/go/oracledatabase/apiv1"
    
    	oracledatabasepb "cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := oracledatabase.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_Close)()
    
    	req := &oracledatabasepb.ListDbNodesRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb#ListDbNodesRequest.
    	}
    	for resp, err := range c.ListDbNodes(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*Client) ListDbServers 
    
    
    func (c *Client) ListDbServers(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[oracledatabasepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb).[ListDbServersRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb#cloud_google_com_go_oracledatabase_apiv1_oracledatabasepb_ListDbServersRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *DbServerIterator

ListDbServers lists the database servers of an Exadata Infrastructure instance.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	oracledatabase "cloud.google.com/go/oracledatabase/apiv1"
    
    	oracledatabasepb "cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := oracledatabase.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_Close)()
    
    	req := &oracledatabasepb.ListDbServersRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb#ListDbServersRequest.
    	}
    	it := c.ListDbServers(ctx, req)
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
    		_ = it.Response.(*oracledatabasepb.ListDbServersResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	oracledatabase "cloud.google.com/go/oracledatabase/apiv1"
    
    	oracledatabasepb "cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := oracledatabase.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_Close)()
    
    	req := &oracledatabasepb.ListDbServersRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb#ListDbServersRequest.
    	}
    	for resp, err := range c.ListDbServers(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*Client) ListDbSystemInitialStorageSizes 
    
    
    func (c *Client) ListDbSystemInitialStorageSizes(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[oracledatabasepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb).[ListDbSystemInitialStorageSizesRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb#cloud_google_com_go_oracledatabase_apiv1_oracledatabasepb_ListDbSystemInitialStorageSizesRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *DbSystemInitialStorageSizeIterator

ListDbSystemInitialStorageSizes lists all the DbSystemInitialStorageSizes for the given project and location.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	oracledatabase "cloud.google.com/go/oracledatabase/apiv1"
    
    	oracledatabasepb "cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := oracledatabase.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_Close)()
    
    	req := &oracledatabasepb.ListDbSystemInitialStorageSizesRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb#ListDbSystemInitialStorageSizesRequest.
    	}
    	it := c.ListDbSystemInitialStorageSizes(ctx, req)
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
    		_ = it.Response.(*oracledatabasepb.ListDbSystemInitialStorageSizesResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	oracledatabase "cloud.google.com/go/oracledatabase/apiv1"
    
    	oracledatabasepb "cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := oracledatabase.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_Close)()
    
    	req := &oracledatabasepb.ListDbSystemInitialStorageSizesRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb#ListDbSystemInitialStorageSizesRequest.
    	}
    	for resp, err := range c.ListDbSystemInitialStorageSizes(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*Client) ListDbSystemShapes 
    
    
    func (c *Client) ListDbSystemShapes(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[oracledatabasepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb).[ListDbSystemShapesRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb#cloud_google_com_go_oracledatabase_apiv1_oracledatabasepb_ListDbSystemShapesRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *DbSystemShapeIterator

ListDbSystemShapes lists the database system shapes available for the project and location.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	oracledatabase "cloud.google.com/go/oracledatabase/apiv1"
    
    	oracledatabasepb "cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := oracledatabase.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_Close)()
    
    	req := &oracledatabasepb.ListDbSystemShapesRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb#ListDbSystemShapesRequest.
    	}
    	it := c.ListDbSystemShapes(ctx, req)
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
    		_ = it.Response.(*oracledatabasepb.ListDbSystemShapesResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	oracledatabase "cloud.google.com/go/oracledatabase/apiv1"
    
    	oracledatabasepb "cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := oracledatabase.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_Close)()
    
    	req := &oracledatabasepb.ListDbSystemShapesRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb#ListDbSystemShapesRequest.
    	}
    	for resp, err := range c.ListDbSystemShapes(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*Client) ListDbSystems 
    
    
    func (c *Client) ListDbSystems(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[oracledatabasepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb).[ListDbSystemsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb#cloud_google_com_go_oracledatabase_apiv1_oracledatabasepb_ListDbSystemsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *DbSystemIterator

ListDbSystems lists all the DbSystems for the given project and location.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	oracledatabase "cloud.google.com/go/oracledatabase/apiv1"
    
    	oracledatabasepb "cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := oracledatabase.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_Close)()
    
    	req := &oracledatabasepb.ListDbSystemsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb#ListDbSystemsRequest.
    	}
    	it := c.ListDbSystems(ctx, req)
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
    		_ = it.Response.(*oracledatabasepb.ListDbSystemsResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	oracledatabase "cloud.google.com/go/oracledatabase/apiv1"
    
    	oracledatabasepb "cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := oracledatabase.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_Close)()
    
    	req := &oracledatabasepb.ListDbSystemsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb#ListDbSystemsRequest.
    	}
    	for resp, err := range c.ListDbSystems(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*Client) ListDbVersions 
    
    
    func (c *Client) ListDbVersions(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[oracledatabasepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb).[ListDbVersionsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb#cloud_google_com_go_oracledatabase_apiv1_oracledatabasepb_ListDbVersionsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *DbVersionIterator

ListDbVersions list DbVersions for the given project and location.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	oracledatabase "cloud.google.com/go/oracledatabase/apiv1"
    
    	oracledatabasepb "cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := oracledatabase.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_Close)()
    
    	req := &oracledatabasepb.ListDbVersionsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb#ListDbVersionsRequest.
    	}
    	it := c.ListDbVersions(ctx, req)
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
    		_ = it.Response.(*oracledatabasepb.ListDbVersionsResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	oracledatabase "cloud.google.com/go/oracledatabase/apiv1"
    
    	oracledatabasepb "cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := oracledatabase.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_Close)()
    
    	req := &oracledatabasepb.ListDbVersionsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb#ListDbVersionsRequest.
    	}
    	for resp, err := range c.ListDbVersions(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*Client) ListEntitlements 
    
    
    func (c *Client) ListEntitlements(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[oracledatabasepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb).[ListEntitlementsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb#cloud_google_com_go_oracledatabase_apiv1_oracledatabasepb_ListEntitlementsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *EntitlementIterator

ListEntitlements lists the entitlements in a given project.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	oracledatabase "cloud.google.com/go/oracledatabase/apiv1"
    
    	oracledatabasepb "cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := oracledatabase.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_Close)()
    
    	req := &oracledatabasepb.ListEntitlementsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb#ListEntitlementsRequest.
    	}
    	it := c.ListEntitlements(ctx, req)
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
    		_ = it.Response.(*oracledatabasepb.ListEntitlementsResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	oracledatabase "cloud.google.com/go/oracledatabase/apiv1"
    
    	oracledatabasepb "cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := oracledatabase.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_Close)()
    
    	req := &oracledatabasepb.ListEntitlementsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb#ListEntitlementsRequest.
    	}
    	for resp, err := range c.ListEntitlements(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*Client) ListExadbVmClusters 
    
    
    func (c *Client) ListExadbVmClusters(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[oracledatabasepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb).[ListExadbVmClustersRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb#cloud_google_com_go_oracledatabase_apiv1_oracledatabasepb_ListExadbVmClustersRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *ExadbVmClusterIterator

ListExadbVmClusters lists all the Exadb (Exascale) VM Clusters for the given project and location.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	oracledatabase "cloud.google.com/go/oracledatabase/apiv1"
    
    	oracledatabasepb "cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := oracledatabase.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_Close)()
    
    	req := &oracledatabasepb.ListExadbVmClustersRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb#ListExadbVmClustersRequest.
    	}
    	it := c.ListExadbVmClusters(ctx, req)
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
    		_ = it.Response.(*oracledatabasepb.ListExadbVmClustersResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	oracledatabase "cloud.google.com/go/oracledatabase/apiv1"
    
    	oracledatabasepb "cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := oracledatabase.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_Close)()
    
    	req := &oracledatabasepb.ListExadbVmClustersRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb#ListExadbVmClustersRequest.
    	}
    	for resp, err := range c.ListExadbVmClusters(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*Client) ListExascaleDbStorageVaults 
    
    
    func (c *Client) ListExascaleDbStorageVaults(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[oracledatabasepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb).[ListExascaleDbStorageVaultsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb#cloud_google_com_go_oracledatabase_apiv1_oracledatabasepb_ListExascaleDbStorageVaultsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *ExascaleDbStorageVaultIterator

ListExascaleDbStorageVaults lists all the ExascaleDB Storage Vaults for the given project and location.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	oracledatabase "cloud.google.com/go/oracledatabase/apiv1"
    
    	oracledatabasepb "cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := oracledatabase.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_Close)()
    
    	req := &oracledatabasepb.ListExascaleDbStorageVaultsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb#ListExascaleDbStorageVaultsRequest.
    	}
    	it := c.ListExascaleDbStorageVaults(ctx, req)
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
    		_ = it.Response.(*oracledatabasepb.ListExascaleDbStorageVaultsResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	oracledatabase "cloud.google.com/go/oracledatabase/apiv1"
    
    	oracledatabasepb "cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := oracledatabase.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_Close)()
    
    	req := &oracledatabasepb.ListExascaleDbStorageVaultsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb#ListExascaleDbStorageVaultsRequest.
    	}
    	for resp, err := range c.ListExascaleDbStorageVaults(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*Client) ListGiVersions 
    
    
    func (c *Client) ListGiVersions(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[oracledatabasepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb).[ListGiVersionsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb#cloud_google_com_go_oracledatabase_apiv1_oracledatabasepb_ListGiVersionsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *GiVersionIterator

ListGiVersions lists all the valid Oracle Grid Infrastructure (GI) versions for the given project and location.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	oracledatabase "cloud.google.com/go/oracledatabase/apiv1"
    
    	oracledatabasepb "cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := oracledatabase.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_Close)()
    
    	req := &oracledatabasepb.ListGiVersionsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb#ListGiVersionsRequest.
    	}
    	it := c.ListGiVersions(ctx, req)
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
    		_ = it.Response.(*oracledatabasepb.ListGiVersionsResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	oracledatabase "cloud.google.com/go/oracledatabase/apiv1"
    
    	oracledatabasepb "cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := oracledatabase.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_Close)()
    
    	req := &oracledatabasepb.ListGiVersionsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb#ListGiVersionsRequest.
    	}
    	for resp, err := range c.ListGiVersions(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*Client) ListGoldengateConnectionAssignments 
    
    
    func (c *Client) ListGoldengateConnectionAssignments(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[oracledatabasepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb).[ListGoldengateConnectionAssignmentsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb#cloud_google_com_go_oracledatabase_apiv1_oracledatabasepb_ListGoldengateConnectionAssignmentsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *GoldengateConnectionAssignmentIterator

ListGoldengateConnectionAssignments lists GoldengateConnectionAssignments in a given project and location.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	oracledatabase "cloud.google.com/go/oracledatabase/apiv1"
    
    	oracledatabasepb "cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := oracledatabase.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_Close)()
    
    	req := &oracledatabasepb.ListGoldengateConnectionAssignmentsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb#ListGoldengateConnectionAssignmentsRequest.
    	}
    	it := c.ListGoldengateConnectionAssignments(ctx, req)
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
    		_ = it.Response.(*oracledatabasepb.ListGoldengateConnectionAssignmentsResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	oracledatabase "cloud.google.com/go/oracledatabase/apiv1"
    
    	oracledatabasepb "cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := oracledatabase.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_Close)()
    
    	req := &oracledatabasepb.ListGoldengateConnectionAssignmentsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb#ListGoldengateConnectionAssignmentsRequest.
    	}
    	for resp, err := range c.ListGoldengateConnectionAssignments(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*Client) ListGoldengateConnectionTypes 
    
    
    func (c *Client) ListGoldengateConnectionTypes(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[oracledatabasepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb).[ListGoldengateConnectionTypesRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb#cloud_google_com_go_oracledatabase_apiv1_oracledatabasepb_ListGoldengateConnectionTypesRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *GoldengateConnectionTypeIterator

ListGoldengateConnectionTypes lists GoldengateConnectionTypes in a given project and location.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	oracledatabase "cloud.google.com/go/oracledatabase/apiv1"
    
    	oracledatabasepb "cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := oracledatabase.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_Close)()
    
    	req := &oracledatabasepb.ListGoldengateConnectionTypesRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb#ListGoldengateConnectionTypesRequest.
    	}
    	it := c.ListGoldengateConnectionTypes(ctx, req)
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
    		_ = it.Response.(*oracledatabasepb.ListGoldengateConnectionTypesResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	oracledatabase "cloud.google.com/go/oracledatabase/apiv1"
    
    	oracledatabasepb "cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := oracledatabase.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_Close)()
    
    	req := &oracledatabasepb.ListGoldengateConnectionTypesRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb#ListGoldengateConnectionTypesRequest.
    	}
    	for resp, err := range c.ListGoldengateConnectionTypes(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*Client) ListGoldengateConnections 
    
    
    func (c *Client) ListGoldengateConnections(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[oracledatabasepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb).[ListGoldengateConnectionsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb#cloud_google_com_go_oracledatabase_apiv1_oracledatabasepb_ListGoldengateConnectionsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *GoldengateConnectionIterator

ListGoldengateConnections lists all the GoldengateConnections for the given project and location.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	oracledatabase "cloud.google.com/go/oracledatabase/apiv1"
    
    	oracledatabasepb "cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := oracledatabase.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_Close)()
    
    	req := &oracledatabasepb.ListGoldengateConnectionsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb#ListGoldengateConnectionsRequest.
    	}
    	it := c.ListGoldengateConnections(ctx, req)
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
    		_ = it.Response.(*oracledatabasepb.ListGoldengateConnectionsResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	oracledatabase "cloud.google.com/go/oracledatabase/apiv1"
    
    	oracledatabasepb "cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := oracledatabase.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_Close)()
    
    	req := &oracledatabasepb.ListGoldengateConnectionsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb#ListGoldengateConnectionsRequest.
    	}
    	for resp, err := range c.ListGoldengateConnections(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*Client) ListGoldengateDeploymentEnvironments 
    
    
    func (c *Client) ListGoldengateDeploymentEnvironments(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[oracledatabasepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb).[ListGoldengateDeploymentEnvironmentsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb#cloud_google_com_go_oracledatabase_apiv1_oracledatabasepb_ListGoldengateDeploymentEnvironmentsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *GoldengateDeploymentEnvironmentIterator

ListGoldengateDeploymentEnvironments lists GoldengateDeploymentEnvironments in a given project and location.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	oracledatabase "cloud.google.com/go/oracledatabase/apiv1"
    
    	oracledatabasepb "cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := oracledatabase.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_Close)()
    
    	req := &oracledatabasepb.ListGoldengateDeploymentEnvironmentsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb#ListGoldengateDeploymentEnvironmentsRequest.
    	}
    	it := c.ListGoldengateDeploymentEnvironments(ctx, req)
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
    		_ = it.Response.(*oracledatabasepb.ListGoldengateDeploymentEnvironmentsResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	oracledatabase "cloud.google.com/go/oracledatabase/apiv1"
    
    	oracledatabasepb "cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := oracledatabase.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_Close)()
    
    	req := &oracledatabasepb.ListGoldengateDeploymentEnvironmentsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb#ListGoldengateDeploymentEnvironmentsRequest.
    	}
    	for resp, err := range c.ListGoldengateDeploymentEnvironments(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*Client) ListGoldengateDeploymentTypes 
    
    
    func (c *Client) ListGoldengateDeploymentTypes(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[oracledatabasepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb).[ListGoldengateDeploymentTypesRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb#cloud_google_com_go_oracledatabase_apiv1_oracledatabasepb_ListGoldengateDeploymentTypesRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *GoldengateDeploymentTypeIterator

ListGoldengateDeploymentTypes lists GoldenGateDeploymentTypes in a given project and location.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	oracledatabase "cloud.google.com/go/oracledatabase/apiv1"
    
    	oracledatabasepb "cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := oracledatabase.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_Close)()
    
    	req := &oracledatabasepb.ListGoldengateDeploymentTypesRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb#ListGoldengateDeploymentTypesRequest.
    	}
    	it := c.ListGoldengateDeploymentTypes(ctx, req)
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
    		_ = it.Response.(*oracledatabasepb.ListGoldengateDeploymentTypesResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	oracledatabase "cloud.google.com/go/oracledatabase/apiv1"
    
    	oracledatabasepb "cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := oracledatabase.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_Close)()
    
    	req := &oracledatabasepb.ListGoldengateDeploymentTypesRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb#ListGoldengateDeploymentTypesRequest.
    	}
    	for resp, err := range c.ListGoldengateDeploymentTypes(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*Client) ListGoldengateDeploymentVersions 
    
    
    func (c *Client) ListGoldengateDeploymentVersions(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[oracledatabasepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb).[ListGoldengateDeploymentVersionsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb#cloud_google_com_go_oracledatabase_apiv1_oracledatabasepb_ListGoldengateDeploymentVersionsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *GoldengateDeploymentVersionIterator

ListGoldengateDeploymentVersions lists GoldengateDeploymentVersions in a given project and location.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	oracledatabase "cloud.google.com/go/oracledatabase/apiv1"
    
    	oracledatabasepb "cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := oracledatabase.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_Close)()
    
    	req := &oracledatabasepb.ListGoldengateDeploymentVersionsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb#ListGoldengateDeploymentVersionsRequest.
    	}
    	it := c.ListGoldengateDeploymentVersions(ctx, req)
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
    		_ = it.Response.(*oracledatabasepb.ListGoldengateDeploymentVersionsResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	oracledatabase "cloud.google.com/go/oracledatabase/apiv1"
    
    	oracledatabasepb "cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := oracledatabase.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_Close)()
    
    	req := &oracledatabasepb.ListGoldengateDeploymentVersionsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb#ListGoldengateDeploymentVersionsRequest.
    	}
    	for resp, err := range c.ListGoldengateDeploymentVersions(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*Client) ListGoldengateDeployments 
    
    
    func (c *Client) ListGoldengateDeployments(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[oracledatabasepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb).[ListGoldengateDeploymentsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb#cloud_google_com_go_oracledatabase_apiv1_oracledatabasepb_ListGoldengateDeploymentsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *GoldengateDeploymentIterator

ListGoldengateDeployments lists all the GoldengateDeployments for the given project and location.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	oracledatabase "cloud.google.com/go/oracledatabase/apiv1"
    
    	oracledatabasepb "cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := oracledatabase.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_Close)()
    
    	req := &oracledatabasepb.ListGoldengateDeploymentsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb#ListGoldengateDeploymentsRequest.
    	}
    	it := c.ListGoldengateDeployments(ctx, req)
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
    		_ = it.Response.(*oracledatabasepb.ListGoldengateDeploymentsResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	oracledatabase "cloud.google.com/go/oracledatabase/apiv1"
    
    	oracledatabasepb "cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := oracledatabase.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_Close)()
    
    	req := &oracledatabasepb.ListGoldengateDeploymentsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb#ListGoldengateDeploymentsRequest.
    	}
    	for resp, err := range c.ListGoldengateDeployments(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*Client) ListLocations 
    
    
    func (c *Client) ListLocations(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[locationpb](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location).[ListLocationsRequest](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#ListLocationsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *LocationIterator

ListLocations lists information about the supported locations for this service.

This method lists locations based on the resource scope provided in the [ListLocationsRequest.name (at http://ListLocationsRequest.name)][google.cloud.location.ListLocationsRequest.name (at <http://google.cloud.location.ListLocationsRequest.name>)] field: * Global locations: If name is empty, the method lists the public locations available to all projects. * Project-specific locations: If name follows the format projects/{project}, the method lists locations visible to that specific project. This includes public, private, or other project-specific locations enabled for the project.

For gRPC and client library implementations, the resource name is passed as the name field. For direct service calls, the resource name is incorporated into the request path based on the specific service implementation and version.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	oracledatabase "cloud.google.com/go/oracledatabase/apiv1"
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
    	c, err := oracledatabase.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_Close)()
    
    	req := &locationpb.ListLocationsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#ListLocationsRequest.
    	}
    	it := c.[ListLocations](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_ListLocations)(ctx, req)
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
    
    	oracledatabase "cloud.google.com/go/oracledatabase/apiv1"
    
    	locationpb "google.golang.org/genproto/googleapis/cloud/location"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := oracledatabase.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_Close)()
    
    	req := &locationpb.ListLocationsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#ListLocationsRequest.
    	}
    	for resp, err := range c.[ListLocations](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_ListLocations)(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*Client) ListMinorVersions 
    
    
    func (c *Client) ListMinorVersions(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[oracledatabasepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb).[ListMinorVersionsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb#cloud_google_com_go_oracledatabase_apiv1_oracledatabasepb_ListMinorVersionsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *MinorVersionIterator

ListMinorVersions lists all the valid minor versions for the given project, location, gi version and shape family.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	oracledatabase "cloud.google.com/go/oracledatabase/apiv1"
    
    	oracledatabasepb "cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := oracledatabase.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_Close)()
    
    	req := &oracledatabasepb.ListMinorVersionsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb#ListMinorVersionsRequest.
    	}
    	it := c.ListMinorVersions(ctx, req)
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
    		_ = it.Response.(*oracledatabasepb.ListMinorVersionsResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	oracledatabase "cloud.google.com/go/oracledatabase/apiv1"
    
    	oracledatabasepb "cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := oracledatabase.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_Close)()
    
    	req := &oracledatabasepb.ListMinorVersionsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb#ListMinorVersionsRequest.
    	}
    	for resp, err := range c.ListMinorVersions(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*Client) ListOdbNetworks 
    
    
    func (c *Client) ListOdbNetworks(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[oracledatabasepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb).[ListOdbNetworksRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb#cloud_google_com_go_oracledatabase_apiv1_oracledatabasepb_ListOdbNetworksRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *OdbNetworkIterator

ListOdbNetworks lists the ODB Networks in a given project and location.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	oracledatabase "cloud.google.com/go/oracledatabase/apiv1"
    
    	oracledatabasepb "cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := oracledatabase.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_Close)()
    
    	req := &oracledatabasepb.ListOdbNetworksRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb#ListOdbNetworksRequest.
    	}
    	it := c.ListOdbNetworks(ctx, req)
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
    		_ = it.Response.(*oracledatabasepb.ListOdbNetworksResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	oracledatabase "cloud.google.com/go/oracledatabase/apiv1"
    
    	oracledatabasepb "cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := oracledatabase.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_Close)()
    
    	req := &oracledatabasepb.ListOdbNetworksRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb#ListOdbNetworksRequest.
    	}
    	for resp, err := range c.ListOdbNetworks(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*Client) ListOdbSubnets 
    
    
    func (c *Client) ListOdbSubnets(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[oracledatabasepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb).[ListOdbSubnetsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb#cloud_google_com_go_oracledatabase_apiv1_oracledatabasepb_ListOdbSubnetsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *OdbSubnetIterator

ListOdbSubnets lists all the ODB Subnets in a given ODB Network.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	oracledatabase "cloud.google.com/go/oracledatabase/apiv1"
    
    	oracledatabasepb "cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := oracledatabase.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_Close)()
    
    	req := &oracledatabasepb.ListOdbSubnetsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb#ListOdbSubnetsRequest.
    	}
    	it := c.ListOdbSubnets(ctx, req)
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
    		_ = it.Response.(*oracledatabasepb.ListOdbSubnetsResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	oracledatabase "cloud.google.com/go/oracledatabase/apiv1"
    
    	oracledatabasepb "cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := oracledatabase.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_Close)()
    
    	req := &oracledatabasepb.ListOdbSubnetsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb#ListOdbSubnetsRequest.
    	}
    	for resp, err := range c.ListOdbSubnets(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*Client) ListOperations 
    
    
    func (c *Client) ListOperations(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[ListOperationsRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#ListOperationsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *OperationIterator

ListOperations is a utility method from google.longrunning.Operations.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    	oracledatabase "cloud.google.com/go/oracledatabase/apiv1"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := oracledatabase.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_Close)()
    
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
    	oracledatabase "cloud.google.com/go/oracledatabase/apiv1"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := oracledatabase.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_Close)()
    
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
    

### func (*Client) ListPluggableDatabases 
    
    
    func (c *Client) ListPluggableDatabases(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[oracledatabasepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb).[ListPluggableDatabasesRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb#cloud_google_com_go_oracledatabase_apiv1_oracledatabasepb_ListPluggableDatabasesRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *PluggableDatabaseIterator

ListPluggableDatabases lists all the PluggableDatabases for the given project, location and Container Database.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	oracledatabase "cloud.google.com/go/oracledatabase/apiv1"
    
    	oracledatabasepb "cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := oracledatabase.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_Close)()
    
    	req := &oracledatabasepb.ListPluggableDatabasesRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb#ListPluggableDatabasesRequest.
    	}
    	it := c.ListPluggableDatabases(ctx, req)
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
    		_ = it.Response.(*oracledatabasepb.ListPluggableDatabasesResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	oracledatabase "cloud.google.com/go/oracledatabase/apiv1"
    
    	oracledatabasepb "cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := oracledatabase.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_Close)()
    
    	req := &oracledatabasepb.ListPluggableDatabasesRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb#ListPluggableDatabasesRequest.
    	}
    	for resp, err := range c.ListPluggableDatabases(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*Client) RefreshAutonomousDatabase 
    
    
    func (c *Client) RefreshAutonomousDatabase(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[oracledatabasepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb).[RefreshAutonomousDatabaseRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb#cloud_google_com_go_oracledatabase_apiv1_oracledatabasepb_RefreshAutonomousDatabaseRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*RefreshAutonomousDatabaseOperation, [error](https://pkg.go.dev/builtin#error))

RefreshAutonomousDatabase refreshes the refreshable clone of an Autonomous Database.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	oracledatabase "cloud.google.com/go/oracledatabase/apiv1"
    
    	oracledatabasepb "cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := oracledatabase.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_Close)()
    
    	req := &oracledatabasepb.RefreshAutonomousDatabaseRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb#RefreshAutonomousDatabaseRequest.
    	}
    	op, err := c.RefreshAutonomousDatabase(ctx, req)
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
    

### func (*Client) RefreshAutonomousDatabaseOperation 
    
    
    func (c *Client) RefreshAutonomousDatabaseOperation(name [string](https://pkg.go.dev/builtin#string)) *RefreshAutonomousDatabaseOperation

RefreshAutonomousDatabaseOperation returns a new RefreshAutonomousDatabaseOperation from a given name. The name must be that of a previously created RefreshAutonomousDatabaseOperation, possibly from a different process.

### func (*Client) RemoveVirtualMachineExadbVmCluster 
    
    
    func (c *Client) RemoveVirtualMachineExadbVmCluster(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[oracledatabasepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb).[RemoveVirtualMachineExadbVmClusterRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb#cloud_google_com_go_oracledatabase_apiv1_oracledatabasepb_RemoveVirtualMachineExadbVmClusterRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*RemoveVirtualMachineExadbVmClusterOperation, [error](https://pkg.go.dev/builtin#error))

RemoveVirtualMachineExadbVmCluster removes virtual machines from an existing exadb vm cluster.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	oracledatabase "cloud.google.com/go/oracledatabase/apiv1"
    
    	oracledatabasepb "cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := oracledatabase.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_Close)()
    
    	req := &oracledatabasepb.RemoveVirtualMachineExadbVmClusterRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb#RemoveVirtualMachineExadbVmClusterRequest.
    	}
    	op, err := c.RemoveVirtualMachineExadbVmCluster(ctx, req)
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
    

### func (*Client) RemoveVirtualMachineExadbVmClusterOperation 
    
    
    func (c *Client) RemoveVirtualMachineExadbVmClusterOperation(name [string](https://pkg.go.dev/builtin#string)) *RemoveVirtualMachineExadbVmClusterOperation

RemoveVirtualMachineExadbVmClusterOperation returns a new RemoveVirtualMachineExadbVmClusterOperation from a given name. The name must be that of a previously created RemoveVirtualMachineExadbVmClusterOperation, possibly from a different process.

### func (*Client) RestartAutonomousDatabase 
    
    
    func (c *Client) RestartAutonomousDatabase(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[oracledatabasepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb).[RestartAutonomousDatabaseRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb#cloud_google_com_go_oracledatabase_apiv1_oracledatabasepb_RestartAutonomousDatabaseRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*RestartAutonomousDatabaseOperation, [error](https://pkg.go.dev/builtin#error))

RestartAutonomousDatabase restarts an Autonomous Database.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	oracledatabase "cloud.google.com/go/oracledatabase/apiv1"
    
    	oracledatabasepb "cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := oracledatabase.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_Close)()
    
    	req := &oracledatabasepb.RestartAutonomousDatabaseRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb#RestartAutonomousDatabaseRequest.
    	}
    	op, err := c.RestartAutonomousDatabase(ctx, req)
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
    

### func (*Client) RestartAutonomousDatabaseOperation 
    
    
    func (c *Client) RestartAutonomousDatabaseOperation(name [string](https://pkg.go.dev/builtin#string)) *RestartAutonomousDatabaseOperation

RestartAutonomousDatabaseOperation returns a new RestartAutonomousDatabaseOperation from a given name. The name must be that of a previously created RestartAutonomousDatabaseOperation, possibly from a different process.

### func (*Client) RestoreAutonomousDatabase 
    
    
    func (c *Client) RestoreAutonomousDatabase(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[oracledatabasepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb).[RestoreAutonomousDatabaseRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb#cloud_google_com_go_oracledatabase_apiv1_oracledatabasepb_RestoreAutonomousDatabaseRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*RestoreAutonomousDatabaseOperation, [error](https://pkg.go.dev/builtin#error))

RestoreAutonomousDatabase restores a single Autonomous Database.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	oracledatabase "cloud.google.com/go/oracledatabase/apiv1"
    
    	oracledatabasepb "cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := oracledatabase.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_Close)()
    
    	req := &oracledatabasepb.RestoreAutonomousDatabaseRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb#RestoreAutonomousDatabaseRequest.
    	}
    	op, err := c.RestoreAutonomousDatabase(ctx, req)
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
    

### func (*Client) RestoreAutonomousDatabaseOperation 
    
    
    func (c *Client) RestoreAutonomousDatabaseOperation(name [string](https://pkg.go.dev/builtin#string)) *RestoreAutonomousDatabaseOperation

RestoreAutonomousDatabaseOperation returns a new RestoreAutonomousDatabaseOperation from a given name. The name must be that of a previously created RestoreAutonomousDatabaseOperation, possibly from a different process.

### func (*Client) StartAutonomousDatabase 
    
    
    func (c *Client) StartAutonomousDatabase(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[oracledatabasepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb).[StartAutonomousDatabaseRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb#cloud_google_com_go_oracledatabase_apiv1_oracledatabasepb_StartAutonomousDatabaseRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*StartAutonomousDatabaseOperation, [error](https://pkg.go.dev/builtin#error))

StartAutonomousDatabase starts an Autonomous Database.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	oracledatabase "cloud.google.com/go/oracledatabase/apiv1"
    
    	oracledatabasepb "cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := oracledatabase.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_Close)()
    
    	req := &oracledatabasepb.StartAutonomousDatabaseRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb#StartAutonomousDatabaseRequest.
    	}
    	op, err := c.StartAutonomousDatabase(ctx, req)
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
    

### func (*Client) StartAutonomousDatabaseOperation 
    
    
    func (c *Client) StartAutonomousDatabaseOperation(name [string](https://pkg.go.dev/builtin#string)) *StartAutonomousDatabaseOperation

StartAutonomousDatabaseOperation returns a new StartAutonomousDatabaseOperation from a given name. The name must be that of a previously created StartAutonomousDatabaseOperation, possibly from a different process.

### func (*Client) StartGoldengateDeployment 
    
    
    func (c *Client) StartGoldengateDeployment(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[oracledatabasepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb).[StartGoldengateDeploymentRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb#cloud_google_com_go_oracledatabase_apiv1_oracledatabasepb_StartGoldengateDeploymentRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*StartGoldengateDeploymentOperation, [error](https://pkg.go.dev/builtin#error))

StartGoldengateDeployment starts a single GoldengateDeployment.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	oracledatabase "cloud.google.com/go/oracledatabase/apiv1"
    
    	oracledatabasepb "cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := oracledatabase.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_Close)()
    
    	req := &oracledatabasepb.StartGoldengateDeploymentRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb#StartGoldengateDeploymentRequest.
    	}
    	op, err := c.StartGoldengateDeployment(ctx, req)
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
    

### func (*Client) StartGoldengateDeploymentOperation 
    
    
    func (c *Client) StartGoldengateDeploymentOperation(name [string](https://pkg.go.dev/builtin#string)) *StartGoldengateDeploymentOperation

StartGoldengateDeploymentOperation returns a new StartGoldengateDeploymentOperation from a given name. The name must be that of a previously created StartGoldengateDeploymentOperation, possibly from a different process.

### func (*Client) StopAutonomousDatabase 
    
    
    func (c *Client) StopAutonomousDatabase(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[oracledatabasepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb).[StopAutonomousDatabaseRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb#cloud_google_com_go_oracledatabase_apiv1_oracledatabasepb_StopAutonomousDatabaseRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*StopAutonomousDatabaseOperation, [error](https://pkg.go.dev/builtin#error))

StopAutonomousDatabase stops an Autonomous Database.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	oracledatabase "cloud.google.com/go/oracledatabase/apiv1"
    
    	oracledatabasepb "cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := oracledatabase.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_Close)()
    
    	req := &oracledatabasepb.StopAutonomousDatabaseRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb#StopAutonomousDatabaseRequest.
    	}
    	op, err := c.StopAutonomousDatabase(ctx, req)
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
    

### func (*Client) StopAutonomousDatabaseOperation 
    
    
    func (c *Client) StopAutonomousDatabaseOperation(name [string](https://pkg.go.dev/builtin#string)) *StopAutonomousDatabaseOperation

StopAutonomousDatabaseOperation returns a new StopAutonomousDatabaseOperation from a given name. The name must be that of a previously created StopAutonomousDatabaseOperation, possibly from a different process.

### func (*Client) StopGoldengateDeployment 
    
    
    func (c *Client) StopGoldengateDeployment(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[oracledatabasepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb).[StopGoldengateDeploymentRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb#cloud_google_com_go_oracledatabase_apiv1_oracledatabasepb_StopGoldengateDeploymentRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*StopGoldengateDeploymentOperation, [error](https://pkg.go.dev/builtin#error))

StopGoldengateDeployment stops a single GoldengateDeployment.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	oracledatabase "cloud.google.com/go/oracledatabase/apiv1"
    
    	oracledatabasepb "cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := oracledatabase.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_Close)()
    
    	req := &oracledatabasepb.StopGoldengateDeploymentRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb#StopGoldengateDeploymentRequest.
    	}
    	op, err := c.StopGoldengateDeployment(ctx, req)
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
    

### func (*Client) StopGoldengateDeploymentOperation 
    
    
    func (c *Client) StopGoldengateDeploymentOperation(name [string](https://pkg.go.dev/builtin#string)) *StopGoldengateDeploymentOperation

StopGoldengateDeploymentOperation returns a new StopGoldengateDeploymentOperation from a given name. The name must be that of a previously created StopGoldengateDeploymentOperation, possibly from a different process.

### func (*Client) SwitchoverAutonomousDatabase 
    
    
    func (c *Client) SwitchoverAutonomousDatabase(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[oracledatabasepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb).[SwitchoverAutonomousDatabaseRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb#cloud_google_com_go_oracledatabase_apiv1_oracledatabasepb_SwitchoverAutonomousDatabaseRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*SwitchoverAutonomousDatabaseOperation, [error](https://pkg.go.dev/builtin#error))

SwitchoverAutonomousDatabase initiates a switchover of specified autonomous database to the associated peer database.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	oracledatabase "cloud.google.com/go/oracledatabase/apiv1"
    
    	oracledatabasepb "cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := oracledatabase.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_Close)()
    
    	req := &oracledatabasepb.SwitchoverAutonomousDatabaseRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb#SwitchoverAutonomousDatabaseRequest.
    	}
    	op, err := c.SwitchoverAutonomousDatabase(ctx, req)
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
    

### func (*Client) SwitchoverAutonomousDatabaseOperation 
    
    
    func (c *Client) SwitchoverAutonomousDatabaseOperation(name [string](https://pkg.go.dev/builtin#string)) *SwitchoverAutonomousDatabaseOperation

SwitchoverAutonomousDatabaseOperation returns a new SwitchoverAutonomousDatabaseOperation from a given name. The name must be that of a previously created SwitchoverAutonomousDatabaseOperation, possibly from a different process.

### func (*Client) TestGoldengateConnectionAssignment 
    
    
    func (c *Client) TestGoldengateConnectionAssignment(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[oracledatabasepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb).[TestGoldengateConnectionAssignmentRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb#cloud_google_com_go_oracledatabase_apiv1_oracledatabasepb_TestGoldengateConnectionAssignmentRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[oracledatabasepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb).[TestGoldengateConnectionAssignmentResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb#cloud_google_com_go_oracledatabase_apiv1_oracledatabasepb_TestGoldengateConnectionAssignmentResponse), [error](https://pkg.go.dev/builtin#error))

TestGoldengateConnectionAssignment tests a single GoldengateConnectionAssignment.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	oracledatabase "cloud.google.com/go/oracledatabase/apiv1"
    
    	oracledatabasepb "cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := oracledatabase.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_Close)()
    
    	req := &oracledatabasepb.TestGoldengateConnectionAssignmentRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb#TestGoldengateConnectionAssignmentRequest.
    	}
    	resp, err := c.TestGoldengateConnectionAssignment(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*Client) UpdateAutonomousDatabase 
    
    
    func (c *Client) UpdateAutonomousDatabase(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[oracledatabasepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb).[UpdateAutonomousDatabaseRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb#cloud_google_com_go_oracledatabase_apiv1_oracledatabasepb_UpdateAutonomousDatabaseRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*UpdateAutonomousDatabaseOperation, [error](https://pkg.go.dev/builtin#error))

UpdateAutonomousDatabase updates the parameters of a single Autonomous Database.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	oracledatabase "cloud.google.com/go/oracledatabase/apiv1"
    
    	oracledatabasepb "cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := oracledatabase.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_Close)()
    
    	req := &oracledatabasepb.UpdateAutonomousDatabaseRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb#UpdateAutonomousDatabaseRequest.
    	}
    	op, err := c.UpdateAutonomousDatabase(ctx, req)
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
    

### func (*Client) UpdateAutonomousDatabaseOperation 
    
    
    func (c *Client) UpdateAutonomousDatabaseOperation(name [string](https://pkg.go.dev/builtin#string)) *UpdateAutonomousDatabaseOperation

UpdateAutonomousDatabaseOperation returns a new UpdateAutonomousDatabaseOperation from a given name. The name must be that of a previously created UpdateAutonomousDatabaseOperation, possibly from a different process.

### func (*Client) UpdateExadbVmCluster 
    
    
    func (c *Client) UpdateExadbVmCluster(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[oracledatabasepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb).[UpdateExadbVmClusterRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb#cloud_google_com_go_oracledatabase_apiv1_oracledatabasepb_UpdateExadbVmClusterRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*UpdateExadbVmClusterOperation, [error](https://pkg.go.dev/builtin#error))

UpdateExadbVmCluster updates a single Exadb (Exascale) VM Cluster. To add virtual machines to existing exadb vm cluster, only pass the node count.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	oracledatabase "cloud.google.com/go/oracledatabase/apiv1"
    
    	oracledatabasepb "cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := oracledatabase.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1.html#cloud_google_com_go_oracledatabase_apiv1_Client_Close)()
    
    	req := &oracledatabasepb.UpdateExadbVmClusterRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/oracledatabase/apiv1/oracledatabasepb#UpdateExadbVmClusterRequest.
    	}
    	op, err := c.UpdateExadbVmCluster(ctx, req)
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
    

### func (*Client) UpdateExadbVmClusterOperation 
    
    
    func (c *Client) UpdateExadbVmClusterOperation(name [string](https://pkg.go.dev/builtin#string)) *UpdateExadbVmClusterOperation

UpdateExadbVmClusterOperation returns a new UpdateExadbVmClusterOperation from a given name. The name must be that of a previously created UpdateExadbVmClusterOperation, possibly from a different process.

## CloudExadataInfrastructureIterator
    
    
    type CloudExadataInfrastructureIterator struct {
    
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
    	InternalFetch func(pageSize [int](https://pkg.go.dev/builtin#int), pageToken [string](https://pkg.go.dev/builtin#string)) (results []*oracledatabasepb.CloudExadataInfrastructure, nextPageToken [string](https://pkg.go.dev/builtin#string), err [error](https://pkg.go.dev/builtin#error))
    	// contains filtered or unexported fields
    }

CloudExadataInfrastructureIterator manages a stream of *oracledatabasepb.CloudExadataInfrastructure.

### func (*CloudExadataInfrastructureIterator) All 
    
    
    func (it *CloudExadataInfrastructureIterator) All() iter.Seq2[*oracledatabasepb.CloudExadataInfrastructure, error]

All returns an iterator. If an error is returned by the iterator, the iterator will stop after that iteration.

### func (*CloudExadataInfrastructureIterator) Next 
    
    
    func (it *CloudExadataInfrastructureIterator) Next() (*[oracledatabasepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb).[CloudExadataInfrastructure](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb#cloud_google_com_go_oracledatabase_apiv1_oracledatabasepb_CloudExadataInfrastructure), [error](https://pkg.go.dev/builtin#error))

Next returns the next result. Its second return value is iterator.Done if there are no more results. Once Next returns Done, all subsequent calls will return Done.

### func (*CloudExadataInfrastructureIterator) PageInfo 
    
    
    func (it *CloudExadataInfrastructureIterator) PageInfo() *iterator.PageInfo

PageInfo supports pagination. See the [google.golang.org/api/iterator] package for details.

## CloudVmClusterIterator
    
    
    type CloudVmClusterIterator struct {
    
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
    	InternalFetch func(pageSize [int](https://pkg.go.dev/builtin#int), pageToken [string](https://pkg.go.dev/builtin#string)) (results []*oracledatabasepb.CloudVmCluster, nextPageToken [string](https://pkg.go.dev/builtin#string), err [error](https://pkg.go.dev/builtin#error))
    	// contains filtered or unexported fields
    }

CloudVmClusterIterator manages a stream of *oracledatabasepb.CloudVmCluster.

### func (*CloudVmClusterIterator) All 
    
    
    func (it *CloudVmClusterIterator) All() iter.Seq2[*oracledatabasepb.CloudVmCluster, error]

All returns an iterator. If an error is returned by the iterator, the iterator will stop after that iteration.

### func (*CloudVmClusterIterator) Next 
    
    
    func (it *CloudVmClusterIterator) Next() (*[oracledatabasepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb).[CloudVmCluster](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb#cloud_google_com_go_oracledatabase_apiv1_oracledatabasepb_CloudVmCluster), [error](https://pkg.go.dev/builtin#error))

Next returns the next result. Its second return value is iterator.Done if there are no more results. Once Next returns Done, all subsequent calls will return Done.

### func (*CloudVmClusterIterator) PageInfo 
    
    
    func (it *CloudVmClusterIterator) PageInfo() *iterator.PageInfo

PageInfo supports pagination. See the [google.golang.org/api/iterator] package for details.

## ConfigureExascaleCloudExadataInfrastructureOperation
    
    
    type ConfigureExascaleCloudExadataInfrastructureOperation struct {
    	// contains filtered or unexported fields
    }

ConfigureExascaleCloudExadataInfrastructureOperation manages a long-running operation from ConfigureExascaleCloudExadataInfrastructure.

### func (*ConfigureExascaleCloudExadataInfrastructureOperation) Done 
    
    
    func (op *ConfigureExascaleCloudExadataInfrastructureOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*ConfigureExascaleCloudExadataInfrastructureOperation) Metadata 
    
    
    func (op *ConfigureExascaleCloudExadataInfrastructureOperation) Metadata() (*[oracledatabasepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb).[OperationMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb#cloud_google_com_go_oracledatabase_apiv1_oracledatabasepb_OperationMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*ConfigureExascaleCloudExadataInfrastructureOperation) Name 
    
    
    func (op *ConfigureExascaleCloudExadataInfrastructureOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*ConfigureExascaleCloudExadataInfrastructureOperation) Poll 
    
    
    func (op *ConfigureExascaleCloudExadataInfrastructureOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[oracledatabasepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb).[CloudExadataInfrastructure](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb#cloud_google_com_go_oracledatabase_apiv1_oracledatabasepb_CloudExadataInfrastructure), [error](https://pkg.go.dev/builtin#error))

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*ConfigureExascaleCloudExadataInfrastructureOperation) Wait 
    
    
    func (op *ConfigureExascaleCloudExadataInfrastructureOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[oracledatabasepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb).[CloudExadataInfrastructure](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb#cloud_google_com_go_oracledatabase_apiv1_oracledatabasepb_CloudExadataInfrastructure), [error](https://pkg.go.dev/builtin#error))

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## CreateAutonomousDatabaseOperation
    
    
    type CreateAutonomousDatabaseOperation struct {
    	// contains filtered or unexported fields
    }

CreateAutonomousDatabaseOperation manages a long-running operation from CreateAutonomousDatabase.

### func (*CreateAutonomousDatabaseOperation) Done 
    
    
    func (op *CreateAutonomousDatabaseOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*CreateAutonomousDatabaseOperation) Metadata 
    
    
    func (op *CreateAutonomousDatabaseOperation) Metadata() (*[oracledatabasepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb).[OperationMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb#cloud_google_com_go_oracledatabase_apiv1_oracledatabasepb_OperationMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*CreateAutonomousDatabaseOperation) Name 
    
    
    func (op *CreateAutonomousDatabaseOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*CreateAutonomousDatabaseOperation) Poll 
    
    
    func (op *CreateAutonomousDatabaseOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[oracledatabasepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb).[AutonomousDatabase](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb#cloud_google_com_go_oracledatabase_apiv1_oracledatabasepb_AutonomousDatabase), [error](https://pkg.go.dev/builtin#error))

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*CreateAutonomousDatabaseOperation) Wait 
    
    
    func (op *CreateAutonomousDatabaseOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[oracledatabasepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb).[AutonomousDatabase](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb#cloud_google_com_go_oracledatabase_apiv1_oracledatabasepb_AutonomousDatabase), [error](https://pkg.go.dev/builtin#error))

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## CreateCloudExadataInfrastructureOperation
    
    
    type CreateCloudExadataInfrastructureOperation struct {
    	// contains filtered or unexported fields
    }

CreateCloudExadataInfrastructureOperation manages a long-running operation from CreateCloudExadataInfrastructure.

### func (*CreateCloudExadataInfrastructureOperation) Done 
    
    
    func (op *CreateCloudExadataInfrastructureOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*CreateCloudExadataInfrastructureOperation) Metadata 
    
    
    func (op *CreateCloudExadataInfrastructureOperation) Metadata() (*[oracledatabasepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb).[OperationMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb#cloud_google_com_go_oracledatabase_apiv1_oracledatabasepb_OperationMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*CreateCloudExadataInfrastructureOperation) Name 
    
    
    func (op *CreateCloudExadataInfrastructureOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*CreateCloudExadataInfrastructureOperation) Poll 
    
    
    func (op *CreateCloudExadataInfrastructureOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[oracledatabasepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb).[CloudExadataInfrastructure](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb#cloud_google_com_go_oracledatabase_apiv1_oracledatabasepb_CloudExadataInfrastructure), [error](https://pkg.go.dev/builtin#error))

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*CreateCloudExadataInfrastructureOperation) Wait 
    
    
    func (op *CreateCloudExadataInfrastructureOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[oracledatabasepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb).[CloudExadataInfrastructure](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb#cloud_google_com_go_oracledatabase_apiv1_oracledatabasepb_CloudExadataInfrastructure), [error](https://pkg.go.dev/builtin#error))

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## CreateCloudVmClusterOperation
    
    
    type CreateCloudVmClusterOperation struct {
    	// contains filtered or unexported fields
    }

CreateCloudVmClusterOperation manages a long-running operation from CreateCloudVmCluster.

### func (*CreateCloudVmClusterOperation) Done 
    
    
    func (op *CreateCloudVmClusterOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*CreateCloudVmClusterOperation) Metadata 
    
    
    func (op *CreateCloudVmClusterOperation) Metadata() (*[oracledatabasepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb).[OperationMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb#cloud_google_com_go_oracledatabase_apiv1_oracledatabasepb_OperationMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*CreateCloudVmClusterOperation) Name 
    
    
    func (op *CreateCloudVmClusterOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*CreateCloudVmClusterOperation) Poll 
    
    
    func (op *CreateCloudVmClusterOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[oracledatabasepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb).[CloudVmCluster](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb#cloud_google_com_go_oracledatabase_apiv1_oracledatabasepb_CloudVmCluster), [error](https://pkg.go.dev/builtin#error))

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*CreateCloudVmClusterOperation) Wait 
    
    
    func (op *CreateCloudVmClusterOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[oracledatabasepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb).[CloudVmCluster](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb#cloud_google_com_go_oracledatabase_apiv1_oracledatabasepb_CloudVmCluster), [error](https://pkg.go.dev/builtin#error))

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## CreateDbSystemOperation
    
    
    type CreateDbSystemOperation struct {
    	// contains filtered or unexported fields
    }

CreateDbSystemOperation manages a long-running operation from CreateDbSystem.

### func (*CreateDbSystemOperation) Done 
    
    
    func (op *CreateDbSystemOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*CreateDbSystemOperation) Metadata 
    
    
    func (op *CreateDbSystemOperation) Metadata() (*[oracledatabasepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb).[OperationMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb#cloud_google_com_go_oracledatabase_apiv1_oracledatabasepb_OperationMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*CreateDbSystemOperation) Name 
    
    
    func (op *CreateDbSystemOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*CreateDbSystemOperation) Poll 
    
    
    func (op *CreateDbSystemOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[oracledatabasepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb).[DbSystem](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb#cloud_google_com_go_oracledatabase_apiv1_oracledatabasepb_DbSystem), [error](https://pkg.go.dev/builtin#error))

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*CreateDbSystemOperation) Wait 
    
    
    func (op *CreateDbSystemOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[oracledatabasepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb).[DbSystem](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb#cloud_google_com_go_oracledatabase_apiv1_oracledatabasepb_DbSystem), [error](https://pkg.go.dev/builtin#error))

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## CreateExadbVmClusterOperation
    
    
    type CreateExadbVmClusterOperation struct {
    	// contains filtered or unexported fields
    }

CreateExadbVmClusterOperation manages a long-running operation from CreateExadbVmCluster.

### func (*CreateExadbVmClusterOperation) Done 
    
    
    func (op *CreateExadbVmClusterOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*CreateExadbVmClusterOperation) Metadata 
    
    
    func (op *CreateExadbVmClusterOperation) Metadata() (*[oracledatabasepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb).[OperationMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb#cloud_google_com_go_oracledatabase_apiv1_oracledatabasepb_OperationMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*CreateExadbVmClusterOperation) Name 
    
    
    func (op *CreateExadbVmClusterOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*CreateExadbVmClusterOperation) Poll 
    
    
    func (op *CreateExadbVmClusterOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[oracledatabasepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb).[ExadbVmCluster](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb#cloud_google_com_go_oracledatabase_apiv1_oracledatabasepb_ExadbVmCluster), [error](https://pkg.go.dev/builtin#error))

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*CreateExadbVmClusterOperation) Wait 
    
    
    func (op *CreateExadbVmClusterOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[oracledatabasepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb).[ExadbVmCluster](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb#cloud_google_com_go_oracledatabase_apiv1_oracledatabasepb_ExadbVmCluster), [error](https://pkg.go.dev/builtin#error))

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## CreateExascaleDbStorageVaultOperation
    
    
    type CreateExascaleDbStorageVaultOperation struct {
    	// contains filtered or unexported fields
    }

CreateExascaleDbStorageVaultOperation manages a long-running operation from CreateExascaleDbStorageVault.

### func (*CreateExascaleDbStorageVaultOperation) Done 
    
    
    func (op *CreateExascaleDbStorageVaultOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*CreateExascaleDbStorageVaultOperation) Metadata 
    
    
    func (op *CreateExascaleDbStorageVaultOperation) Metadata() (*[oracledatabasepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb).[OperationMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb#cloud_google_com_go_oracledatabase_apiv1_oracledatabasepb_OperationMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*CreateExascaleDbStorageVaultOperation) Name 
    
    
    func (op *CreateExascaleDbStorageVaultOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*CreateExascaleDbStorageVaultOperation) Poll 
    
    
    func (op *CreateExascaleDbStorageVaultOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[oracledatabasepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb).[ExascaleDbStorageVault](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb#cloud_google_com_go_oracledatabase_apiv1_oracledatabasepb_ExascaleDbStorageVault), [error](https://pkg.go.dev/builtin#error))

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*CreateExascaleDbStorageVaultOperation) Wait 
    
    
    func (op *CreateExascaleDbStorageVaultOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[oracledatabasepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb).[ExascaleDbStorageVault](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb#cloud_google_com_go_oracledatabase_apiv1_oracledatabasepb_ExascaleDbStorageVault), [error](https://pkg.go.dev/builtin#error))

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## CreateGoldengateConnectionAssignmentOperation
    
    
    type CreateGoldengateConnectionAssignmentOperation struct {
    	// contains filtered or unexported fields
    }

CreateGoldengateConnectionAssignmentOperation manages a long-running operation from CreateGoldengateConnectionAssignment.

### func (*CreateGoldengateConnectionAssignmentOperation) Done 
    
    
    func (op *CreateGoldengateConnectionAssignmentOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*CreateGoldengateConnectionAssignmentOperation) Metadata 
    
    
    func (op *CreateGoldengateConnectionAssignmentOperation) Metadata() (*[oracledatabasepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb).[OperationMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb#cloud_google_com_go_oracledatabase_apiv1_oracledatabasepb_OperationMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*CreateGoldengateConnectionAssignmentOperation) Name 
    
    
    func (op *CreateGoldengateConnectionAssignmentOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*CreateGoldengateConnectionAssignmentOperation) Poll 
    
    
    func (op *CreateGoldengateConnectionAssignmentOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[oracledatabasepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb).[GoldengateConnectionAssignment](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb#cloud_google_com_go_oracledatabase_apiv1_oracledatabasepb_GoldengateConnectionAssignment), [error](https://pkg.go.dev/builtin#error))

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*CreateGoldengateConnectionAssignmentOperation) Wait 
    
    
    func (op *CreateGoldengateConnectionAssignmentOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[oracledatabasepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb).[GoldengateConnectionAssignment](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb#cloud_google_com_go_oracledatabase_apiv1_oracledatabasepb_GoldengateConnectionAssignment), [error](https://pkg.go.dev/builtin#error))

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## CreateGoldengateConnectionOperation
    
    
    type CreateGoldengateConnectionOperation struct {
    	// contains filtered or unexported fields
    }

CreateGoldengateConnectionOperation manages a long-running operation from CreateGoldengateConnection.

### func (*CreateGoldengateConnectionOperation) Done 
    
    
    func (op *CreateGoldengateConnectionOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*CreateGoldengateConnectionOperation) Metadata 
    
    
    func (op *CreateGoldengateConnectionOperation) Metadata() (*[oracledatabasepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb).[OperationMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb#cloud_google_com_go_oracledatabase_apiv1_oracledatabasepb_OperationMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*CreateGoldengateConnectionOperation) Name 
    
    
    func (op *CreateGoldengateConnectionOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*CreateGoldengateConnectionOperation) Poll 
    
    
    func (op *CreateGoldengateConnectionOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[oracledatabasepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb).[GoldengateConnection](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb#cloud_google_com_go_oracledatabase_apiv1_oracledatabasepb_GoldengateConnection), [error](https://pkg.go.dev/builtin#error))

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*CreateGoldengateConnectionOperation) Wait 
    
    
    func (op *CreateGoldengateConnectionOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[oracledatabasepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb).[GoldengateConnection](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb#cloud_google_com_go_oracledatabase_apiv1_oracledatabasepb_GoldengateConnection), [error](https://pkg.go.dev/builtin#error))

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## CreateGoldengateDeploymentOperation
    
    
    type CreateGoldengateDeploymentOperation struct {
    	// contains filtered or unexported fields
    }

CreateGoldengateDeploymentOperation manages a long-running operation from CreateGoldengateDeployment.

### func (*CreateGoldengateDeploymentOperation) Done 
    
    
    func (op *CreateGoldengateDeploymentOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*CreateGoldengateDeploymentOperation) Metadata 
    
    
    func (op *CreateGoldengateDeploymentOperation) Metadata() (*[oracledatabasepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb).[OperationMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb#cloud_google_com_go_oracledatabase_apiv1_oracledatabasepb_OperationMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*CreateGoldengateDeploymentOperation) Name 
    
    
    func (op *CreateGoldengateDeploymentOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*CreateGoldengateDeploymentOperation) Poll 
    
    
    func (op *CreateGoldengateDeploymentOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[oracledatabasepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb).[GoldengateDeployment](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb#cloud_google_com_go_oracledatabase_apiv1_oracledatabasepb_GoldengateDeployment), [error](https://pkg.go.dev/builtin#error))

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*CreateGoldengateDeploymentOperation) Wait 
    
    
    func (op *CreateGoldengateDeploymentOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[oracledatabasepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb).[GoldengateDeployment](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb#cloud_google_com_go_oracledatabase_apiv1_oracledatabasepb_GoldengateDeployment), [error](https://pkg.go.dev/builtin#error))

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## CreateOdbNetworkOperation
    
    
    type CreateOdbNetworkOperation struct {
    	// contains filtered or unexported fields
    }

CreateOdbNetworkOperation manages a long-running operation from CreateOdbNetwork.

### func (*CreateOdbNetworkOperation) Done 
    
    
    func (op *CreateOdbNetworkOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*CreateOdbNetworkOperation) Metadata 
    
    
    func (op *CreateOdbNetworkOperation) Metadata() (*[oracledatabasepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb).[OperationMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb#cloud_google_com_go_oracledatabase_apiv1_oracledatabasepb_OperationMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*CreateOdbNetworkOperation) Name 
    
    
    func (op *CreateOdbNetworkOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*CreateOdbNetworkOperation) Poll 
    
    
    func (op *CreateOdbNetworkOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[oracledatabasepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb).[OdbNetwork](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb#cloud_google_com_go_oracledatabase_apiv1_oracledatabasepb_OdbNetwork), [error](https://pkg.go.dev/builtin#error))

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*CreateOdbNetworkOperation) Wait 
    
    
    func (op *CreateOdbNetworkOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[oracledatabasepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb).[OdbNetwork](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb#cloud_google_com_go_oracledatabase_apiv1_oracledatabasepb_OdbNetwork), [error](https://pkg.go.dev/builtin#error))

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## CreateOdbSubnetOperation
    
    
    type CreateOdbSubnetOperation struct {
    	// contains filtered or unexported fields
    }

CreateOdbSubnetOperation manages a long-running operation from CreateOdbSubnet.

### func (*CreateOdbSubnetOperation) Done 
    
    
    func (op *CreateOdbSubnetOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*CreateOdbSubnetOperation) Metadata 
    
    
    func (op *CreateOdbSubnetOperation) Metadata() (*[oracledatabasepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb).[OperationMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb#cloud_google_com_go_oracledatabase_apiv1_oracledatabasepb_OperationMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*CreateOdbSubnetOperation) Name 
    
    
    func (op *CreateOdbSubnetOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*CreateOdbSubnetOperation) Poll 
    
    
    func (op *CreateOdbSubnetOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[oracledatabasepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb).[OdbSubnet](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb#cloud_google_com_go_oracledatabase_apiv1_oracledatabasepb_OdbSubnet), [error](https://pkg.go.dev/builtin#error))

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*CreateOdbSubnetOperation) Wait 
    
    
    func (op *CreateOdbSubnetOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[oracledatabasepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb).[OdbSubnet](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb#cloud_google_com_go_oracledatabase_apiv1_oracledatabasepb_OdbSubnet), [error](https://pkg.go.dev/builtin#error))

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## DatabaseCharacterSetIterator
    
    
    type DatabaseCharacterSetIterator struct {
    
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
    	InternalFetch func(pageSize [int](https://pkg.go.dev/builtin#int), pageToken [string](https://pkg.go.dev/builtin#string)) (results []*oracledatabasepb.DatabaseCharacterSet, nextPageToken [string](https://pkg.go.dev/builtin#string), err [error](https://pkg.go.dev/builtin#error))
    	// contains filtered or unexported fields
    }

DatabaseCharacterSetIterator manages a stream of *oracledatabasepb.DatabaseCharacterSet.

### func (*DatabaseCharacterSetIterator) All 
    
    
    func (it *DatabaseCharacterSetIterator) All() iter.Seq2[*oracledatabasepb.DatabaseCharacterSet, error]

All returns an iterator. If an error is returned by the iterator, the iterator will stop after that iteration.

### func (*DatabaseCharacterSetIterator) Next 
    
    
    func (it *DatabaseCharacterSetIterator) Next() (*[oracledatabasepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb).[DatabaseCharacterSet](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb#cloud_google_com_go_oracledatabase_apiv1_oracledatabasepb_DatabaseCharacterSet), [error](https://pkg.go.dev/builtin#error))

Next returns the next result. Its second return value is iterator.Done if there are no more results. Once Next returns Done, all subsequent calls will return Done.

### func (*DatabaseCharacterSetIterator) PageInfo 
    
    
    func (it *DatabaseCharacterSetIterator) PageInfo() *iterator.PageInfo

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
    	InternalFetch func(pageSize [int](https://pkg.go.dev/builtin#int), pageToken [string](https://pkg.go.dev/builtin#string)) (results []*oracledatabasepb.Database, nextPageToken [string](https://pkg.go.dev/builtin#string), err [error](https://pkg.go.dev/builtin#error))
    	// contains filtered or unexported fields
    }

DatabaseIterator manages a stream of *oracledatabasepb.Database.

### func (*DatabaseIterator) All 
    
    
    func (it *DatabaseIterator) All() iter.Seq2[*oracledatabasepb.Database, error]

All returns an iterator. If an error is returned by the iterator, the iterator will stop after that iteration.

### func (*DatabaseIterator) Next 
    
    
    func (it *DatabaseIterator) Next() (*[oracledatabasepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb).[Database](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb#cloud_google_com_go_oracledatabase_apiv1_oracledatabasepb_Database), [error](https://pkg.go.dev/builtin#error))

Next returns the next result. Its second return value is iterator.Done if there are no more results. Once Next returns Done, all subsequent calls will return Done.

### func (*DatabaseIterator) PageInfo 
    
    
    func (it *DatabaseIterator) PageInfo() *iterator.PageInfo

PageInfo supports pagination. See the [google.golang.org/api/iterator] package for details.

## DbNodeIterator
    
    
    type DbNodeIterator struct {
    
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
    	InternalFetch func(pageSize [int](https://pkg.go.dev/builtin#int), pageToken [string](https://pkg.go.dev/builtin#string)) (results []*oracledatabasepb.DbNode, nextPageToken [string](https://pkg.go.dev/builtin#string), err [error](https://pkg.go.dev/builtin#error))
    	// contains filtered or unexported fields
    }

DbNodeIterator manages a stream of *oracledatabasepb.DbNode.

### func (*DbNodeIterator) All 
    
    
    func (it *DbNodeIterator) All() iter.Seq2[*oracledatabasepb.DbNode, error]

All returns an iterator. If an error is returned by the iterator, the iterator will stop after that iteration.

### func (*DbNodeIterator) Next 
    
    
    func (it *DbNodeIterator) Next() (*[oracledatabasepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb).[DbNode](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb#cloud_google_com_go_oracledatabase_apiv1_oracledatabasepb_DbNode), [error](https://pkg.go.dev/builtin#error))

Next returns the next result. Its second return value is iterator.Done if there are no more results. Once Next returns Done, all subsequent calls will return Done.

### func (*DbNodeIterator) PageInfo 
    
    
    func (it *DbNodeIterator) PageInfo() *iterator.PageInfo

PageInfo supports pagination. See the [google.golang.org/api/iterator] package for details.

## DbServerIterator
    
    
    type DbServerIterator struct {
    
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
    	InternalFetch func(pageSize [int](https://pkg.go.dev/builtin#int), pageToken [string](https://pkg.go.dev/builtin#string)) (results []*oracledatabasepb.DbServer, nextPageToken [string](https://pkg.go.dev/builtin#string), err [error](https://pkg.go.dev/builtin#error))
    	// contains filtered or unexported fields
    }

DbServerIterator manages a stream of *oracledatabasepb.DbServer.

### func (*DbServerIterator) All 
    
    
    func (it *DbServerIterator) All() iter.Seq2[*oracledatabasepb.DbServer, error]

All returns an iterator. If an error is returned by the iterator, the iterator will stop after that iteration.

### func (*DbServerIterator) Next 
    
    
    func (it *DbServerIterator) Next() (*[oracledatabasepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb).[DbServer](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb#cloud_google_com_go_oracledatabase_apiv1_oracledatabasepb_DbServer), [error](https://pkg.go.dev/builtin#error))

Next returns the next result. Its second return value is iterator.Done if there are no more results. Once Next returns Done, all subsequent calls will return Done.

### func (*DbServerIterator) PageInfo 
    
    
    func (it *DbServerIterator) PageInfo() *iterator.PageInfo

PageInfo supports pagination. See the [google.golang.org/api/iterator] package for details.

## DbSystemInitialStorageSizeIterator
    
    
    type DbSystemInitialStorageSizeIterator struct {
    
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
    	InternalFetch func(pageSize [int](https://pkg.go.dev/builtin#int), pageToken [string](https://pkg.go.dev/builtin#string)) (results []*oracledatabasepb.DbSystemInitialStorageSize, nextPageToken [string](https://pkg.go.dev/builtin#string), err [error](https://pkg.go.dev/builtin#error))
    	// contains filtered or unexported fields
    }

DbSystemInitialStorageSizeIterator manages a stream of *oracledatabasepb.DbSystemInitialStorageSize.

### func (*DbSystemInitialStorageSizeIterator) All 
    
    
    func (it *DbSystemInitialStorageSizeIterator) All() iter.Seq2[*oracledatabasepb.DbSystemInitialStorageSize, error]

All returns an iterator. If an error is returned by the iterator, the iterator will stop after that iteration.

### func (*DbSystemInitialStorageSizeIterator) Next 
    
    
    func (it *DbSystemInitialStorageSizeIterator) Next() (*[oracledatabasepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb).[DbSystemInitialStorageSize](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb#cloud_google_com_go_oracledatabase_apiv1_oracledatabasepb_DbSystemInitialStorageSize), [error](https://pkg.go.dev/builtin#error))

Next returns the next result. Its second return value is iterator.Done if there are no more results. Once Next returns Done, all subsequent calls will return Done.

### func (*DbSystemInitialStorageSizeIterator) PageInfo 
    
    
    func (it *DbSystemInitialStorageSizeIterator) PageInfo() *iterator.PageInfo

PageInfo supports pagination. See the [google.golang.org/api/iterator] package for details.

## DbSystemIterator
    
    
    type DbSystemIterator struct {
    
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
    	InternalFetch func(pageSize [int](https://pkg.go.dev/builtin#int), pageToken [string](https://pkg.go.dev/builtin#string)) (results []*oracledatabasepb.DbSystem, nextPageToken [string](https://pkg.go.dev/builtin#string), err [error](https://pkg.go.dev/builtin#error))
    	// contains filtered or unexported fields
    }

DbSystemIterator manages a stream of *oracledatabasepb.DbSystem.

### func (*DbSystemIterator) All 
    
    
    func (it *DbSystemIterator) All() iter.Seq2[*oracledatabasepb.DbSystem, error]

All returns an iterator. If an error is returned by the iterator, the iterator will stop after that iteration.

### func (*DbSystemIterator) Next 
    
    
    func (it *DbSystemIterator) Next() (*[oracledatabasepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb).[DbSystem](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb#cloud_google_com_go_oracledatabase_apiv1_oracledatabasepb_DbSystem), [error](https://pkg.go.dev/builtin#error))

Next returns the next result. Its second return value is iterator.Done if there are no more results. Once Next returns Done, all subsequent calls will return Done.

### func (*DbSystemIterator) PageInfo 
    
    
    func (it *DbSystemIterator) PageInfo() *iterator.PageInfo

PageInfo supports pagination. See the [google.golang.org/api/iterator] package for details.

## DbSystemShapeIterator
    
    
    type DbSystemShapeIterator struct {
    
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
    	InternalFetch func(pageSize [int](https://pkg.go.dev/builtin#int), pageToken [string](https://pkg.go.dev/builtin#string)) (results []*oracledatabasepb.DbSystemShape, nextPageToken [string](https://pkg.go.dev/builtin#string), err [error](https://pkg.go.dev/builtin#error))
    	// contains filtered or unexported fields
    }

DbSystemShapeIterator manages a stream of *oracledatabasepb.DbSystemShape.

### func (*DbSystemShapeIterator) All 
    
    
    func (it *DbSystemShapeIterator) All() iter.Seq2[*oracledatabasepb.DbSystemShape, error]

All returns an iterator. If an error is returned by the iterator, the iterator will stop after that iteration.

### func (*DbSystemShapeIterator) Next 
    
    
    func (it *DbSystemShapeIterator) Next() (*[oracledatabasepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb).[DbSystemShape](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb#cloud_google_com_go_oracledatabase_apiv1_oracledatabasepb_DbSystemShape), [error](https://pkg.go.dev/builtin#error))

Next returns the next result. Its second return value is iterator.Done if there are no more results. Once Next returns Done, all subsequent calls will return Done.

### func (*DbSystemShapeIterator) PageInfo 
    
    
    func (it *DbSystemShapeIterator) PageInfo() *iterator.PageInfo

PageInfo supports pagination. See the [google.golang.org/api/iterator] package for details.

## DbVersionIterator
    
    
    type DbVersionIterator struct {
    
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
    	InternalFetch func(pageSize [int](https://pkg.go.dev/builtin#int), pageToken [string](https://pkg.go.dev/builtin#string)) (results []*oracledatabasepb.DbVersion, nextPageToken [string](https://pkg.go.dev/builtin#string), err [error](https://pkg.go.dev/builtin#error))
    	// contains filtered or unexported fields
    }

DbVersionIterator manages a stream of *oracledatabasepb.DbVersion.

### func (*DbVersionIterator) All 
    
    
    func (it *DbVersionIterator) All() iter.Seq2[*oracledatabasepb.DbVersion, error]

All returns an iterator. If an error is returned by the iterator, the iterator will stop after that iteration.

### func (*DbVersionIterator) Next 
    
    
    func (it *DbVersionIterator) Next() (*[oracledatabasepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb).[DbVersion](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb#cloud_google_com_go_oracledatabase_apiv1_oracledatabasepb_DbVersion), [error](https://pkg.go.dev/builtin#error))

Next returns the next result. Its second return value is iterator.Done if there are no more results. Once Next returns Done, all subsequent calls will return Done.

### func (*DbVersionIterator) PageInfo 
    
    
    func (it *DbVersionIterator) PageInfo() *iterator.PageInfo

PageInfo supports pagination. See the [google.golang.org/api/iterator] package for details.

## DeleteAutonomousDatabaseOperation
    
    
    type DeleteAutonomousDatabaseOperation struct {
    	// contains filtered or unexported fields
    }

DeleteAutonomousDatabaseOperation manages a long-running operation from DeleteAutonomousDatabase.

### func (*DeleteAutonomousDatabaseOperation) Done 
    
    
    func (op *DeleteAutonomousDatabaseOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*DeleteAutonomousDatabaseOperation) Metadata 
    
    
    func (op *DeleteAutonomousDatabaseOperation) Metadata() (*[oracledatabasepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb).[OperationMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb#cloud_google_com_go_oracledatabase_apiv1_oracledatabasepb_OperationMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*DeleteAutonomousDatabaseOperation) Name 
    
    
    func (op *DeleteAutonomousDatabaseOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*DeleteAutonomousDatabaseOperation) Poll 
    
    
    func (op *DeleteAutonomousDatabaseOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*DeleteAutonomousDatabaseOperation) Wait 
    
    
    func (op *DeleteAutonomousDatabaseOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## DeleteCloudExadataInfrastructureOperation
    
    
    type DeleteCloudExadataInfrastructureOperation struct {
    	// contains filtered or unexported fields
    }

DeleteCloudExadataInfrastructureOperation manages a long-running operation from DeleteCloudExadataInfrastructure.

### func (*DeleteCloudExadataInfrastructureOperation) Done 
    
    
    func (op *DeleteCloudExadataInfrastructureOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*DeleteCloudExadataInfrastructureOperation) Metadata 
    
    
    func (op *DeleteCloudExadataInfrastructureOperation) Metadata() (*[oracledatabasepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb).[OperationMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb#cloud_google_com_go_oracledatabase_apiv1_oracledatabasepb_OperationMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*DeleteCloudExadataInfrastructureOperation) Name 
    
    
    func (op *DeleteCloudExadataInfrastructureOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*DeleteCloudExadataInfrastructureOperation) Poll 
    
    
    func (op *DeleteCloudExadataInfrastructureOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*DeleteCloudExadataInfrastructureOperation) Wait 
    
    
    func (op *DeleteCloudExadataInfrastructureOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## DeleteCloudVmClusterOperation
    
    
    type DeleteCloudVmClusterOperation struct {
    	// contains filtered or unexported fields
    }

DeleteCloudVmClusterOperation manages a long-running operation from DeleteCloudVmCluster.

### func (*DeleteCloudVmClusterOperation) Done 
    
    
    func (op *DeleteCloudVmClusterOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*DeleteCloudVmClusterOperation) Metadata 
    
    
    func (op *DeleteCloudVmClusterOperation) Metadata() (*[oracledatabasepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb).[OperationMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb#cloud_google_com_go_oracledatabase_apiv1_oracledatabasepb_OperationMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*DeleteCloudVmClusterOperation) Name 
    
    
    func (op *DeleteCloudVmClusterOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*DeleteCloudVmClusterOperation) Poll 
    
    
    func (op *DeleteCloudVmClusterOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*DeleteCloudVmClusterOperation) Wait 
    
    
    func (op *DeleteCloudVmClusterOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## DeleteDbSystemOperation
    
    
    type DeleteDbSystemOperation struct {
    	// contains filtered or unexported fields
    }

DeleteDbSystemOperation manages a long-running operation from DeleteDbSystem.

### func (*DeleteDbSystemOperation) Done 
    
    
    func (op *DeleteDbSystemOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*DeleteDbSystemOperation) Metadata 
    
    
    func (op *DeleteDbSystemOperation) Metadata() (*[oracledatabasepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb).[OperationMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb#cloud_google_com_go_oracledatabase_apiv1_oracledatabasepb_OperationMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*DeleteDbSystemOperation) Name 
    
    
    func (op *DeleteDbSystemOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*DeleteDbSystemOperation) Poll 
    
    
    func (op *DeleteDbSystemOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*DeleteDbSystemOperation) Wait 
    
    
    func (op *DeleteDbSystemOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## DeleteExadbVmClusterOperation
    
    
    type DeleteExadbVmClusterOperation struct {
    	// contains filtered or unexported fields
    }

DeleteExadbVmClusterOperation manages a long-running operation from DeleteExadbVmCluster.

### func (*DeleteExadbVmClusterOperation) Done 
    
    
    func (op *DeleteExadbVmClusterOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*DeleteExadbVmClusterOperation) Metadata 
    
    
    func (op *DeleteExadbVmClusterOperation) Metadata() (*[oracledatabasepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb).[OperationMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb#cloud_google_com_go_oracledatabase_apiv1_oracledatabasepb_OperationMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*DeleteExadbVmClusterOperation) Name 
    
    
    func (op *DeleteExadbVmClusterOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*DeleteExadbVmClusterOperation) Poll 
    
    
    func (op *DeleteExadbVmClusterOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*DeleteExadbVmClusterOperation) Wait 
    
    
    func (op *DeleteExadbVmClusterOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## DeleteExascaleDbStorageVaultOperation
    
    
    type DeleteExascaleDbStorageVaultOperation struct {
    	// contains filtered or unexported fields
    }

DeleteExascaleDbStorageVaultOperation manages a long-running operation from DeleteExascaleDbStorageVault.

### func (*DeleteExascaleDbStorageVaultOperation) Done 
    
    
    func (op *DeleteExascaleDbStorageVaultOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*DeleteExascaleDbStorageVaultOperation) Metadata 
    
    
    func (op *DeleteExascaleDbStorageVaultOperation) Metadata() (*[oracledatabasepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb).[OperationMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb#cloud_google_com_go_oracledatabase_apiv1_oracledatabasepb_OperationMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*DeleteExascaleDbStorageVaultOperation) Name 
    
    
    func (op *DeleteExascaleDbStorageVaultOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*DeleteExascaleDbStorageVaultOperation) Poll 
    
    
    func (op *DeleteExascaleDbStorageVaultOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*DeleteExascaleDbStorageVaultOperation) Wait 
    
    
    func (op *DeleteExascaleDbStorageVaultOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## DeleteGoldengateConnectionAssignmentOperation
    
    
    type DeleteGoldengateConnectionAssignmentOperation struct {
    	// contains filtered or unexported fields
    }

DeleteGoldengateConnectionAssignmentOperation manages a long-running operation from DeleteGoldengateConnectionAssignment.

### func (*DeleteGoldengateConnectionAssignmentOperation) Done 
    
    
    func (op *DeleteGoldengateConnectionAssignmentOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*DeleteGoldengateConnectionAssignmentOperation) Metadata 
    
    
    func (op *DeleteGoldengateConnectionAssignmentOperation) Metadata() (*[oracledatabasepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb).[OperationMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb#cloud_google_com_go_oracledatabase_apiv1_oracledatabasepb_OperationMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*DeleteGoldengateConnectionAssignmentOperation) Name 
    
    
    func (op *DeleteGoldengateConnectionAssignmentOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*DeleteGoldengateConnectionAssignmentOperation) Poll 
    
    
    func (op *DeleteGoldengateConnectionAssignmentOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*DeleteGoldengateConnectionAssignmentOperation) Wait 
    
    
    func (op *DeleteGoldengateConnectionAssignmentOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## DeleteGoldengateConnectionOperation
    
    
    type DeleteGoldengateConnectionOperation struct {
    	// contains filtered or unexported fields
    }

DeleteGoldengateConnectionOperation manages a long-running operation from DeleteGoldengateConnection.

### func (*DeleteGoldengateConnectionOperation) Done 
    
    
    func (op *DeleteGoldengateConnectionOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*DeleteGoldengateConnectionOperation) Metadata 
    
    
    func (op *DeleteGoldengateConnectionOperation) Metadata() (*[oracledatabasepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb).[OperationMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb#cloud_google_com_go_oracledatabase_apiv1_oracledatabasepb_OperationMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*DeleteGoldengateConnectionOperation) Name 
    
    
    func (op *DeleteGoldengateConnectionOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*DeleteGoldengateConnectionOperation) Poll 
    
    
    func (op *DeleteGoldengateConnectionOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*DeleteGoldengateConnectionOperation) Wait 
    
    
    func (op *DeleteGoldengateConnectionOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## DeleteGoldengateDeploymentOperation
    
    
    type DeleteGoldengateDeploymentOperation struct {
    	// contains filtered or unexported fields
    }

DeleteGoldengateDeploymentOperation manages a long-running operation from DeleteGoldengateDeployment.

### func (*DeleteGoldengateDeploymentOperation) Done 
    
    
    func (op *DeleteGoldengateDeploymentOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*DeleteGoldengateDeploymentOperation) Metadata 
    
    
    func (op *DeleteGoldengateDeploymentOperation) Metadata() (*[oracledatabasepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb).[OperationMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb#cloud_google_com_go_oracledatabase_apiv1_oracledatabasepb_OperationMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*DeleteGoldengateDeploymentOperation) Name 
    
    
    func (op *DeleteGoldengateDeploymentOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*DeleteGoldengateDeploymentOperation) Poll 
    
    
    func (op *DeleteGoldengateDeploymentOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*DeleteGoldengateDeploymentOperation) Wait 
    
    
    func (op *DeleteGoldengateDeploymentOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## DeleteOdbNetworkOperation
    
    
    type DeleteOdbNetworkOperation struct {
    	// contains filtered or unexported fields
    }

DeleteOdbNetworkOperation manages a long-running operation from DeleteOdbNetwork.

### func (*DeleteOdbNetworkOperation) Done 
    
    
    func (op *DeleteOdbNetworkOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*DeleteOdbNetworkOperation) Metadata 
    
    
    func (op *DeleteOdbNetworkOperation) Metadata() (*[oracledatabasepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb).[OperationMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb#cloud_google_com_go_oracledatabase_apiv1_oracledatabasepb_OperationMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*DeleteOdbNetworkOperation) Name 
    
    
    func (op *DeleteOdbNetworkOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*DeleteOdbNetworkOperation) Poll 
    
    
    func (op *DeleteOdbNetworkOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*DeleteOdbNetworkOperation) Wait 
    
    
    func (op *DeleteOdbNetworkOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## DeleteOdbSubnetOperation
    
    
    type DeleteOdbSubnetOperation struct {
    	// contains filtered or unexported fields
    }

DeleteOdbSubnetOperation manages a long-running operation from DeleteOdbSubnet.

### func (*DeleteOdbSubnetOperation) Done 
    
    
    func (op *DeleteOdbSubnetOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*DeleteOdbSubnetOperation) Metadata 
    
    
    func (op *DeleteOdbSubnetOperation) Metadata() (*[oracledatabasepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb).[OperationMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb#cloud_google_com_go_oracledatabase_apiv1_oracledatabasepb_OperationMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*DeleteOdbSubnetOperation) Name 
    
    
    func (op *DeleteOdbSubnetOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*DeleteOdbSubnetOperation) Poll 
    
    
    func (op *DeleteOdbSubnetOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*DeleteOdbSubnetOperation) Wait 
    
    
    func (op *DeleteOdbSubnetOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## EntitlementIterator
    
    
    type EntitlementIterator struct {
    
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
    	InternalFetch func(pageSize [int](https://pkg.go.dev/builtin#int), pageToken [string](https://pkg.go.dev/builtin#string)) (results []*oracledatabasepb.Entitlement, nextPageToken [string](https://pkg.go.dev/builtin#string), err [error](https://pkg.go.dev/builtin#error))
    	// contains filtered or unexported fields
    }

EntitlementIterator manages a stream of *oracledatabasepb.Entitlement.

### func (*EntitlementIterator) All 
    
    
    func (it *EntitlementIterator) All() iter.Seq2[*oracledatabasepb.Entitlement, error]

All returns an iterator. If an error is returned by the iterator, the iterator will stop after that iteration.

### func (*EntitlementIterator) Next 
    
    
    func (it *EntitlementIterator) Next() (*[oracledatabasepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb).[Entitlement](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb#cloud_google_com_go_oracledatabase_apiv1_oracledatabasepb_Entitlement), [error](https://pkg.go.dev/builtin#error))

Next returns the next result. Its second return value is iterator.Done if there are no more results. Once Next returns Done, all subsequent calls will return Done.

### func (*EntitlementIterator) PageInfo 
    
    
    func (it *EntitlementIterator) PageInfo() *iterator.PageInfo

PageInfo supports pagination. See the [google.golang.org/api/iterator] package for details.

## ExadbVmClusterIterator
    
    
    type ExadbVmClusterIterator struct {
    
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
    	InternalFetch func(pageSize [int](https://pkg.go.dev/builtin#int), pageToken [string](https://pkg.go.dev/builtin#string)) (results []*oracledatabasepb.ExadbVmCluster, nextPageToken [string](https://pkg.go.dev/builtin#string), err [error](https://pkg.go.dev/builtin#error))
    	// contains filtered or unexported fields
    }

ExadbVmClusterIterator manages a stream of *oracledatabasepb.ExadbVmCluster.

### func (*ExadbVmClusterIterator) All 
    
    
    func (it *ExadbVmClusterIterator) All() iter.Seq2[*oracledatabasepb.ExadbVmCluster, error]

All returns an iterator. If an error is returned by the iterator, the iterator will stop after that iteration.

### func (*ExadbVmClusterIterator) Next 
    
    
    func (it *ExadbVmClusterIterator) Next() (*[oracledatabasepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb).[ExadbVmCluster](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb#cloud_google_com_go_oracledatabase_apiv1_oracledatabasepb_ExadbVmCluster), [error](https://pkg.go.dev/builtin#error))

Next returns the next result. Its second return value is iterator.Done if there are no more results. Once Next returns Done, all subsequent calls will return Done.

### func (*ExadbVmClusterIterator) PageInfo 
    
    
    func (it *ExadbVmClusterIterator) PageInfo() *iterator.PageInfo

PageInfo supports pagination. See the [google.golang.org/api/iterator] package for details.

## ExascaleDbStorageVaultIterator
    
    
    type ExascaleDbStorageVaultIterator struct {
    
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
    	InternalFetch func(pageSize [int](https://pkg.go.dev/builtin#int), pageToken [string](https://pkg.go.dev/builtin#string)) (results []*oracledatabasepb.ExascaleDbStorageVault, nextPageToken [string](https://pkg.go.dev/builtin#string), err [error](https://pkg.go.dev/builtin#error))
    	// contains filtered or unexported fields
    }

ExascaleDbStorageVaultIterator manages a stream of *oracledatabasepb.ExascaleDbStorageVault.

### func (*ExascaleDbStorageVaultIterator) All 
    
    
    func (it *ExascaleDbStorageVaultIterator) All() iter.Seq2[*oracledatabasepb.ExascaleDbStorageVault, error]

All returns an iterator. If an error is returned by the iterator, the iterator will stop after that iteration.

### func (*ExascaleDbStorageVaultIterator) Next 
    
    
    func (it *ExascaleDbStorageVaultIterator) Next() (*[oracledatabasepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb).[ExascaleDbStorageVault](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb#cloud_google_com_go_oracledatabase_apiv1_oracledatabasepb_ExascaleDbStorageVault), [error](https://pkg.go.dev/builtin#error))

Next returns the next result. Its second return value is iterator.Done if there are no more results. Once Next returns Done, all subsequent calls will return Done.

### func (*ExascaleDbStorageVaultIterator) PageInfo 
    
    
    func (it *ExascaleDbStorageVaultIterator) PageInfo() *iterator.PageInfo

PageInfo supports pagination. See the [google.golang.org/api/iterator] package for details.

## FailoverAutonomousDatabaseOperation
    
    
    type FailoverAutonomousDatabaseOperation struct {
    	// contains filtered or unexported fields
    }

FailoverAutonomousDatabaseOperation manages a long-running operation from FailoverAutonomousDatabase.

### func (*FailoverAutonomousDatabaseOperation) Done 
    
    
    func (op *FailoverAutonomousDatabaseOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*FailoverAutonomousDatabaseOperation) Metadata 
    
    
    func (op *FailoverAutonomousDatabaseOperation) Metadata() (*[oracledatabasepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb).[OperationMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb#cloud_google_com_go_oracledatabase_apiv1_oracledatabasepb_OperationMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*FailoverAutonomousDatabaseOperation) Name 
    
    
    func (op *FailoverAutonomousDatabaseOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*FailoverAutonomousDatabaseOperation) Poll 
    
    
    func (op *FailoverAutonomousDatabaseOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[oracledatabasepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb).[AutonomousDatabase](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb#cloud_google_com_go_oracledatabase_apiv1_oracledatabasepb_AutonomousDatabase), [error](https://pkg.go.dev/builtin#error))

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*FailoverAutonomousDatabaseOperation) Wait 
    
    
    func (op *FailoverAutonomousDatabaseOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[oracledatabasepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb).[AutonomousDatabase](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb#cloud_google_com_go_oracledatabase_apiv1_oracledatabasepb_AutonomousDatabase), [error](https://pkg.go.dev/builtin#error))

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## GiVersionIterator
    
    
    type GiVersionIterator struct {
    
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
    	InternalFetch func(pageSize [int](https://pkg.go.dev/builtin#int), pageToken [string](https://pkg.go.dev/builtin#string)) (results []*oracledatabasepb.GiVersion, nextPageToken [string](https://pkg.go.dev/builtin#string), err [error](https://pkg.go.dev/builtin#error))
    	// contains filtered or unexported fields
    }

GiVersionIterator manages a stream of *oracledatabasepb.GiVersion.

### func (*GiVersionIterator) All 
    
    
    func (it *GiVersionIterator) All() iter.Seq2[*oracledatabasepb.GiVersion, error]

All returns an iterator. If an error is returned by the iterator, the iterator will stop after that iteration.

### func (*GiVersionIterator) Next 
    
    
    func (it *GiVersionIterator) Next() (*[oracledatabasepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb).[GiVersion](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb#cloud_google_com_go_oracledatabase_apiv1_oracledatabasepb_GiVersion), [error](https://pkg.go.dev/builtin#error))

Next returns the next result. Its second return value is iterator.Done if there are no more results. Once Next returns Done, all subsequent calls will return Done.

### func (*GiVersionIterator) PageInfo 
    
    
    func (it *GiVersionIterator) PageInfo() *iterator.PageInfo

PageInfo supports pagination. See the [google.golang.org/api/iterator] package for details.

## GoldengateConnectionAssignmentIterator
    
    
    type GoldengateConnectionAssignmentIterator struct {
    
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
    	InternalFetch func(pageSize [int](https://pkg.go.dev/builtin#int), pageToken [string](https://pkg.go.dev/builtin#string)) (results []*oracledatabasepb.GoldengateConnectionAssignment, nextPageToken [string](https://pkg.go.dev/builtin#string), err [error](https://pkg.go.dev/builtin#error))
    	// contains filtered or unexported fields
    }

GoldengateConnectionAssignmentIterator manages a stream of *oracledatabasepb.GoldengateConnectionAssignment.

### func (*GoldengateConnectionAssignmentIterator) All 
    
    
    func (it *GoldengateConnectionAssignmentIterator) All() iter.Seq2[*oracledatabasepb.GoldengateConnectionAssignment, error]

All returns an iterator. If an error is returned by the iterator, the iterator will stop after that iteration.

### func (*GoldengateConnectionAssignmentIterator) Next 
    
    
    func (it *GoldengateConnectionAssignmentIterator) Next() (*[oracledatabasepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb).[GoldengateConnectionAssignment](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb#cloud_google_com_go_oracledatabase_apiv1_oracledatabasepb_GoldengateConnectionAssignment), [error](https://pkg.go.dev/builtin#error))

Next returns the next result. Its second return value is iterator.Done if there are no more results. Once Next returns Done, all subsequent calls will return Done.

### func (*GoldengateConnectionAssignmentIterator) PageInfo 
    
    
    func (it *GoldengateConnectionAssignmentIterator) PageInfo() *iterator.PageInfo

PageInfo supports pagination. See the [google.golang.org/api/iterator] package for details.

## GoldengateConnectionIterator
    
    
    type GoldengateConnectionIterator struct {
    
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
    	InternalFetch func(pageSize [int](https://pkg.go.dev/builtin#int), pageToken [string](https://pkg.go.dev/builtin#string)) (results []*oracledatabasepb.GoldengateConnection, nextPageToken [string](https://pkg.go.dev/builtin#string), err [error](https://pkg.go.dev/builtin#error))
    	// contains filtered or unexported fields
    }

GoldengateConnectionIterator manages a stream of *oracledatabasepb.GoldengateConnection.

### func (*GoldengateConnectionIterator) All 
    
    
    func (it *GoldengateConnectionIterator) All() iter.Seq2[*oracledatabasepb.GoldengateConnection, error]

All returns an iterator. If an error is returned by the iterator, the iterator will stop after that iteration.

### func (*GoldengateConnectionIterator) Next 
    
    
    func (it *GoldengateConnectionIterator) Next() (*[oracledatabasepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb).[GoldengateConnection](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb#cloud_google_com_go_oracledatabase_apiv1_oracledatabasepb_GoldengateConnection), [error](https://pkg.go.dev/builtin#error))

Next returns the next result. Its second return value is iterator.Done if there are no more results. Once Next returns Done, all subsequent calls will return Done.

### func (*GoldengateConnectionIterator) PageInfo 
    
    
    func (it *GoldengateConnectionIterator) PageInfo() *iterator.PageInfo

PageInfo supports pagination. See the [google.golang.org/api/iterator] package for details.

## GoldengateConnectionTypeIterator
    
    
    type GoldengateConnectionTypeIterator struct {
    
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
    	InternalFetch func(pageSize [int](https://pkg.go.dev/builtin#int), pageToken [string](https://pkg.go.dev/builtin#string)) (results []*oracledatabasepb.GoldengateConnectionType, nextPageToken [string](https://pkg.go.dev/builtin#string), err [error](https://pkg.go.dev/builtin#error))
    	// contains filtered or unexported fields
    }

GoldengateConnectionTypeIterator manages a stream of *oracledatabasepb.GoldengateConnectionType.

### func (*GoldengateConnectionTypeIterator) All 
    
    
    func (it *GoldengateConnectionTypeIterator) All() iter.Seq2[*oracledatabasepb.GoldengateConnectionType, error]

All returns an iterator. If an error is returned by the iterator, the iterator will stop after that iteration.

### func (*GoldengateConnectionTypeIterator) Next 
    
    
    func (it *GoldengateConnectionTypeIterator) Next() (*[oracledatabasepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb).[GoldengateConnectionType](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb#cloud_google_com_go_oracledatabase_apiv1_oracledatabasepb_GoldengateConnectionType), [error](https://pkg.go.dev/builtin#error))

Next returns the next result. Its second return value is iterator.Done if there are no more results. Once Next returns Done, all subsequent calls will return Done.

### func (*GoldengateConnectionTypeIterator) PageInfo 
    
    
    func (it *GoldengateConnectionTypeIterator) PageInfo() *iterator.PageInfo

PageInfo supports pagination. See the [google.golang.org/api/iterator] package for details.

## GoldengateDeploymentEnvironmentIterator
    
    
    type GoldengateDeploymentEnvironmentIterator struct {
    
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
    	InternalFetch func(pageSize [int](https://pkg.go.dev/builtin#int), pageToken [string](https://pkg.go.dev/builtin#string)) (results []*oracledatabasepb.GoldengateDeploymentEnvironment, nextPageToken [string](https://pkg.go.dev/builtin#string), err [error](https://pkg.go.dev/builtin#error))
    	// contains filtered or unexported fields
    }

GoldengateDeploymentEnvironmentIterator manages a stream of *oracledatabasepb.GoldengateDeploymentEnvironment.

### func (*GoldengateDeploymentEnvironmentIterator) All 
    
    
    func (it *GoldengateDeploymentEnvironmentIterator) All() iter.Seq2[*oracledatabasepb.GoldengateDeploymentEnvironment, error]

All returns an iterator. If an error is returned by the iterator, the iterator will stop after that iteration.

### func (*GoldengateDeploymentEnvironmentIterator) Next 
    
    
    func (it *GoldengateDeploymentEnvironmentIterator) Next() (*[oracledatabasepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb).[GoldengateDeploymentEnvironment](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb#cloud_google_com_go_oracledatabase_apiv1_oracledatabasepb_GoldengateDeploymentEnvironment), [error](https://pkg.go.dev/builtin#error))

Next returns the next result. Its second return value is iterator.Done if there are no more results. Once Next returns Done, all subsequent calls will return Done.

### func (*GoldengateDeploymentEnvironmentIterator) PageInfo 
    
    
    func (it *GoldengateDeploymentEnvironmentIterator) PageInfo() *iterator.PageInfo

PageInfo supports pagination. See the [google.golang.org/api/iterator] package for details.

## GoldengateDeploymentIterator
    
    
    type GoldengateDeploymentIterator struct {
    
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
    	InternalFetch func(pageSize [int](https://pkg.go.dev/builtin#int), pageToken [string](https://pkg.go.dev/builtin#string)) (results []*oracledatabasepb.GoldengateDeployment, nextPageToken [string](https://pkg.go.dev/builtin#string), err [error](https://pkg.go.dev/builtin#error))
    	// contains filtered or unexported fields
    }

GoldengateDeploymentIterator manages a stream of *oracledatabasepb.GoldengateDeployment.

### func (*GoldengateDeploymentIterator) All 
    
    
    func (it *GoldengateDeploymentIterator) All() iter.Seq2[*oracledatabasepb.GoldengateDeployment, error]

All returns an iterator. If an error is returned by the iterator, the iterator will stop after that iteration.

### func (*GoldengateDeploymentIterator) Next 
    
    
    func (it *GoldengateDeploymentIterator) Next() (*[oracledatabasepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb).[GoldengateDeployment](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb#cloud_google_com_go_oracledatabase_apiv1_oracledatabasepb_GoldengateDeployment), [error](https://pkg.go.dev/builtin#error))

Next returns the next result. Its second return value is iterator.Done if there are no more results. Once Next returns Done, all subsequent calls will return Done.

### func (*GoldengateDeploymentIterator) PageInfo 
    
    
    func (it *GoldengateDeploymentIterator) PageInfo() *iterator.PageInfo

PageInfo supports pagination. See the [google.golang.org/api/iterator] package for details.

## GoldengateDeploymentTypeIterator
    
    
    type GoldengateDeploymentTypeIterator struct {
    
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
    	InternalFetch func(pageSize [int](https://pkg.go.dev/builtin#int), pageToken [string](https://pkg.go.dev/builtin#string)) (results []*oracledatabasepb.GoldengateDeploymentType, nextPageToken [string](https://pkg.go.dev/builtin#string), err [error](https://pkg.go.dev/builtin#error))
    	// contains filtered or unexported fields
    }

GoldengateDeploymentTypeIterator manages a stream of *oracledatabasepb.GoldengateDeploymentType.

### func (*GoldengateDeploymentTypeIterator) All 
    
    
    func (it *GoldengateDeploymentTypeIterator) All() iter.Seq2[*oracledatabasepb.GoldengateDeploymentType, error]

All returns an iterator. If an error is returned by the iterator, the iterator will stop after that iteration.

### func (*GoldengateDeploymentTypeIterator) Next 
    
    
    func (it *GoldengateDeploymentTypeIterator) Next() (*[oracledatabasepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb).[GoldengateDeploymentType](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb#cloud_google_com_go_oracledatabase_apiv1_oracledatabasepb_GoldengateDeploymentType), [error](https://pkg.go.dev/builtin#error))

Next returns the next result. Its second return value is iterator.Done if there are no more results. Once Next returns Done, all subsequent calls will return Done.

### func (*GoldengateDeploymentTypeIterator) PageInfo 
    
    
    func (it *GoldengateDeploymentTypeIterator) PageInfo() *iterator.PageInfo

PageInfo supports pagination. See the [google.golang.org/api/iterator] package for details.

## GoldengateDeploymentVersionIterator
    
    
    type GoldengateDeploymentVersionIterator struct {
    
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
    	InternalFetch func(pageSize [int](https://pkg.go.dev/builtin#int), pageToken [string](https://pkg.go.dev/builtin#string)) (results []*oracledatabasepb.GoldengateDeploymentVersion, nextPageToken [string](https://pkg.go.dev/builtin#string), err [error](https://pkg.go.dev/builtin#error))
    	// contains filtered or unexported fields
    }

GoldengateDeploymentVersionIterator manages a stream of *oracledatabasepb.GoldengateDeploymentVersion.

### func (*GoldengateDeploymentVersionIterator) All 
    
    
    func (it *GoldengateDeploymentVersionIterator) All() iter.Seq2[*oracledatabasepb.GoldengateDeploymentVersion, error]

All returns an iterator. If an error is returned by the iterator, the iterator will stop after that iteration.

### func (*GoldengateDeploymentVersionIterator) Next 
    
    
    func (it *GoldengateDeploymentVersionIterator) Next() (*[oracledatabasepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb).[GoldengateDeploymentVersion](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb#cloud_google_com_go_oracledatabase_apiv1_oracledatabasepb_GoldengateDeploymentVersion), [error](https://pkg.go.dev/builtin#error))

Next returns the next result. Its second return value is iterator.Done if there are no more results. Once Next returns Done, all subsequent calls will return Done.

### func (*GoldengateDeploymentVersionIterator) PageInfo 
    
    
    func (it *GoldengateDeploymentVersionIterator) PageInfo() *iterator.PageInfo

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
    
    
    func (it *LocationIterator) PageInfo() *iterator.PageInfo

PageInfo supports pagination. See the [google.golang.org/api/iterator] package for details.

## MinorVersionIterator
    
    
    type MinorVersionIterator struct {
    
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
    	InternalFetch func(pageSize [int](https://pkg.go.dev/builtin#int), pageToken [string](https://pkg.go.dev/builtin#string)) (results []*oracledatabasepb.MinorVersion, nextPageToken [string](https://pkg.go.dev/builtin#string), err [error](https://pkg.go.dev/builtin#error))
    	// contains filtered or unexported fields
    }

MinorVersionIterator manages a stream of *oracledatabasepb.MinorVersion.

### func (*MinorVersionIterator) All 
    
    
    func (it *MinorVersionIterator) All() iter.Seq2[*oracledatabasepb.MinorVersion, error]

All returns an iterator. If an error is returned by the iterator, the iterator will stop after that iteration.

### func (*MinorVersionIterator) Next 
    
    
    func (it *MinorVersionIterator) Next() (*[oracledatabasepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb).[MinorVersion](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb#cloud_google_com_go_oracledatabase_apiv1_oracledatabasepb_MinorVersion), [error](https://pkg.go.dev/builtin#error))

Next returns the next result. Its second return value is iterator.Done if there are no more results. Once Next returns Done, all subsequent calls will return Done.

### func (*MinorVersionIterator) PageInfo 
    
    
    func (it *MinorVersionIterator) PageInfo() *iterator.PageInfo

PageInfo supports pagination. See the [google.golang.org/api/iterator] package for details.

## OdbNetworkIterator
    
    
    type OdbNetworkIterator struct {
    
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
    	InternalFetch func(pageSize [int](https://pkg.go.dev/builtin#int), pageToken [string](https://pkg.go.dev/builtin#string)) (results []*oracledatabasepb.OdbNetwork, nextPageToken [string](https://pkg.go.dev/builtin#string), err [error](https://pkg.go.dev/builtin#error))
    	// contains filtered or unexported fields
    }

OdbNetworkIterator manages a stream of *oracledatabasepb.OdbNetwork.

### func (*OdbNetworkIterator) All 
    
    
    func (it *OdbNetworkIterator) All() iter.Seq2[*oracledatabasepb.OdbNetwork, error]

All returns an iterator. If an error is returned by the iterator, the iterator will stop after that iteration.

### func (*OdbNetworkIterator) Next 
    
    
    func (it *OdbNetworkIterator) Next() (*[oracledatabasepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb).[OdbNetwork](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb#cloud_google_com_go_oracledatabase_apiv1_oracledatabasepb_OdbNetwork), [error](https://pkg.go.dev/builtin#error))

Next returns the next result. Its second return value is iterator.Done if there are no more results. Once Next returns Done, all subsequent calls will return Done.

### func (*OdbNetworkIterator) PageInfo 
    
    
    func (it *OdbNetworkIterator) PageInfo() *iterator.PageInfo

PageInfo supports pagination. See the [google.golang.org/api/iterator] package for details.

## OdbSubnetIterator
    
    
    type OdbSubnetIterator struct {
    
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
    	InternalFetch func(pageSize [int](https://pkg.go.dev/builtin#int), pageToken [string](https://pkg.go.dev/builtin#string)) (results []*oracledatabasepb.OdbSubnet, nextPageToken [string](https://pkg.go.dev/builtin#string), err [error](https://pkg.go.dev/builtin#error))
    	// contains filtered or unexported fields
    }

OdbSubnetIterator manages a stream of *oracledatabasepb.OdbSubnet.

### func (*OdbSubnetIterator) All 
    
    
    func (it *OdbSubnetIterator) All() iter.Seq2[*oracledatabasepb.OdbSubnet, error]

All returns an iterator. If an error is returned by the iterator, the iterator will stop after that iteration.

### func (*OdbSubnetIterator) Next 
    
    
    func (it *OdbSubnetIterator) Next() (*[oracledatabasepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb).[OdbSubnet](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb#cloud_google_com_go_oracledatabase_apiv1_oracledatabasepb_OdbSubnet), [error](https://pkg.go.dev/builtin#error))

Next returns the next result. Its second return value is iterator.Done if there are no more results. Once Next returns Done, all subsequent calls will return Done.

### func (*OdbSubnetIterator) PageInfo 
    
    
    func (it *OdbSubnetIterator) PageInfo() *iterator.PageInfo

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

## PluggableDatabaseIterator
    
    
    type PluggableDatabaseIterator struct {
    
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
    	InternalFetch func(pageSize [int](https://pkg.go.dev/builtin#int), pageToken [string](https://pkg.go.dev/builtin#string)) (results []*oracledatabasepb.PluggableDatabase, nextPageToken [string](https://pkg.go.dev/builtin#string), err [error](https://pkg.go.dev/builtin#error))
    	// contains filtered or unexported fields
    }

PluggableDatabaseIterator manages a stream of *oracledatabasepb.PluggableDatabase.

### func (*PluggableDatabaseIterator) All 
    
    
    func (it *PluggableDatabaseIterator) All() iter.Seq2[*oracledatabasepb.PluggableDatabase, error]

All returns an iterator. If an error is returned by the iterator, the iterator will stop after that iteration.

### func (*PluggableDatabaseIterator) Next 
    
    
    func (it *PluggableDatabaseIterator) Next() (*[oracledatabasepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb).[PluggableDatabase](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb#cloud_google_com_go_oracledatabase_apiv1_oracledatabasepb_PluggableDatabase), [error](https://pkg.go.dev/builtin#error))

Next returns the next result. Its second return value is iterator.Done if there are no more results. Once Next returns Done, all subsequent calls will return Done.

### func (*PluggableDatabaseIterator) PageInfo 
    
    
    func (it *PluggableDatabaseIterator) PageInfo() *iterator.PageInfo

PageInfo supports pagination. See the [google.golang.org/api/iterator] package for details.

## RefreshAutonomousDatabaseOperation
    
    
    type RefreshAutonomousDatabaseOperation struct {
    	// contains filtered or unexported fields
    }

RefreshAutonomousDatabaseOperation manages a long-running operation from RefreshAutonomousDatabase.

### func (*RefreshAutonomousDatabaseOperation) Done 
    
    
    func (op *RefreshAutonomousDatabaseOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*RefreshAutonomousDatabaseOperation) Metadata 
    
    
    func (op *RefreshAutonomousDatabaseOperation) Metadata() (*[oracledatabasepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb).[OperationMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb#cloud_google_com_go_oracledatabase_apiv1_oracledatabasepb_OperationMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*RefreshAutonomousDatabaseOperation) Name 
    
    
    func (op *RefreshAutonomousDatabaseOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*RefreshAutonomousDatabaseOperation) Poll 
    
    
    func (op *RefreshAutonomousDatabaseOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[oracledatabasepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb).[AutonomousDatabase](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb#cloud_google_com_go_oracledatabase_apiv1_oracledatabasepb_AutonomousDatabase), [error](https://pkg.go.dev/builtin#error))

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*RefreshAutonomousDatabaseOperation) Wait 
    
    
    func (op *RefreshAutonomousDatabaseOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[oracledatabasepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb).[AutonomousDatabase](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb#cloud_google_com_go_oracledatabase_apiv1_oracledatabasepb_AutonomousDatabase), [error](https://pkg.go.dev/builtin#error))

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## RemoveVirtualMachineExadbVmClusterOperation
    
    
    type RemoveVirtualMachineExadbVmClusterOperation struct {
    	// contains filtered or unexported fields
    }

RemoveVirtualMachineExadbVmClusterOperation manages a long-running operation from RemoveVirtualMachineExadbVmCluster.

### func (*RemoveVirtualMachineExadbVmClusterOperation) Done 
    
    
    func (op *RemoveVirtualMachineExadbVmClusterOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*RemoveVirtualMachineExadbVmClusterOperation) Metadata 
    
    
    func (op *RemoveVirtualMachineExadbVmClusterOperation) Metadata() (*[oracledatabasepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb).[OperationMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb#cloud_google_com_go_oracledatabase_apiv1_oracledatabasepb_OperationMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*RemoveVirtualMachineExadbVmClusterOperation) Name 
    
    
    func (op *RemoveVirtualMachineExadbVmClusterOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*RemoveVirtualMachineExadbVmClusterOperation) Poll 
    
    
    func (op *RemoveVirtualMachineExadbVmClusterOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[oracledatabasepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb).[ExadbVmCluster](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb#cloud_google_com_go_oracledatabase_apiv1_oracledatabasepb_ExadbVmCluster), [error](https://pkg.go.dev/builtin#error))

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*RemoveVirtualMachineExadbVmClusterOperation) Wait 
    
    
    func (op *RemoveVirtualMachineExadbVmClusterOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[oracledatabasepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb).[ExadbVmCluster](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb#cloud_google_com_go_oracledatabase_apiv1_oracledatabasepb_ExadbVmCluster), [error](https://pkg.go.dev/builtin#error))

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## RestartAutonomousDatabaseOperation
    
    
    type RestartAutonomousDatabaseOperation struct {
    	// contains filtered or unexported fields
    }

RestartAutonomousDatabaseOperation manages a long-running operation from RestartAutonomousDatabase.

### func (*RestartAutonomousDatabaseOperation) Done 
    
    
    func (op *RestartAutonomousDatabaseOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*RestartAutonomousDatabaseOperation) Metadata 
    
    
    func (op *RestartAutonomousDatabaseOperation) Metadata() (*[oracledatabasepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb).[OperationMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb#cloud_google_com_go_oracledatabase_apiv1_oracledatabasepb_OperationMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*RestartAutonomousDatabaseOperation) Name 
    
    
    func (op *RestartAutonomousDatabaseOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*RestartAutonomousDatabaseOperation) Poll 
    
    
    func (op *RestartAutonomousDatabaseOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[oracledatabasepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb).[AutonomousDatabase](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb#cloud_google_com_go_oracledatabase_apiv1_oracledatabasepb_AutonomousDatabase), [error](https://pkg.go.dev/builtin#error))

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*RestartAutonomousDatabaseOperation) Wait 
    
    
    func (op *RestartAutonomousDatabaseOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[oracledatabasepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb).[AutonomousDatabase](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb#cloud_google_com_go_oracledatabase_apiv1_oracledatabasepb_AutonomousDatabase), [error](https://pkg.go.dev/builtin#error))

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## RestoreAutonomousDatabaseOperation
    
    
    type RestoreAutonomousDatabaseOperation struct {
    	// contains filtered or unexported fields
    }

RestoreAutonomousDatabaseOperation manages a long-running operation from RestoreAutonomousDatabase.

### func (*RestoreAutonomousDatabaseOperation) Done 
    
    
    func (op *RestoreAutonomousDatabaseOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*RestoreAutonomousDatabaseOperation) Metadata 
    
    
    func (op *RestoreAutonomousDatabaseOperation) Metadata() (*[oracledatabasepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb).[OperationMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb#cloud_google_com_go_oracledatabase_apiv1_oracledatabasepb_OperationMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*RestoreAutonomousDatabaseOperation) Name 
    
    
    func (op *RestoreAutonomousDatabaseOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*RestoreAutonomousDatabaseOperation) Poll 
    
    
    func (op *RestoreAutonomousDatabaseOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[oracledatabasepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb).[AutonomousDatabase](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb#cloud_google_com_go_oracledatabase_apiv1_oracledatabasepb_AutonomousDatabase), [error](https://pkg.go.dev/builtin#error))

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*RestoreAutonomousDatabaseOperation) Wait 
    
    
    func (op *RestoreAutonomousDatabaseOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[oracledatabasepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb).[AutonomousDatabase](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb#cloud_google_com_go_oracledatabase_apiv1_oracledatabasepb_AutonomousDatabase), [error](https://pkg.go.dev/builtin#error))

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## StartAutonomousDatabaseOperation
    
    
    type StartAutonomousDatabaseOperation struct {
    	// contains filtered or unexported fields
    }

StartAutonomousDatabaseOperation manages a long-running operation from StartAutonomousDatabase.

### func (*StartAutonomousDatabaseOperation) Done 
    
    
    func (op *StartAutonomousDatabaseOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*StartAutonomousDatabaseOperation) Metadata 
    
    
    func (op *StartAutonomousDatabaseOperation) Metadata() (*[oracledatabasepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb).[OperationMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb#cloud_google_com_go_oracledatabase_apiv1_oracledatabasepb_OperationMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*StartAutonomousDatabaseOperation) Name 
    
    
    func (op *StartAutonomousDatabaseOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*StartAutonomousDatabaseOperation) Poll 
    
    
    func (op *StartAutonomousDatabaseOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[oracledatabasepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb).[AutonomousDatabase](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb#cloud_google_com_go_oracledatabase_apiv1_oracledatabasepb_AutonomousDatabase), [error](https://pkg.go.dev/builtin#error))

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*StartAutonomousDatabaseOperation) Wait 
    
    
    func (op *StartAutonomousDatabaseOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[oracledatabasepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb).[AutonomousDatabase](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb#cloud_google_com_go_oracledatabase_apiv1_oracledatabasepb_AutonomousDatabase), [error](https://pkg.go.dev/builtin#error))

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## StartGoldengateDeploymentOperation
    
    
    type StartGoldengateDeploymentOperation struct {
    	// contains filtered or unexported fields
    }

StartGoldengateDeploymentOperation manages a long-running operation from StartGoldengateDeployment.

### func (*StartGoldengateDeploymentOperation) Done 
    
    
    func (op *StartGoldengateDeploymentOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*StartGoldengateDeploymentOperation) Metadata 
    
    
    func (op *StartGoldengateDeploymentOperation) Metadata() (*[oracledatabasepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb).[OperationMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb#cloud_google_com_go_oracledatabase_apiv1_oracledatabasepb_OperationMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*StartGoldengateDeploymentOperation) Name 
    
    
    func (op *StartGoldengateDeploymentOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*StartGoldengateDeploymentOperation) Poll 
    
    
    func (op *StartGoldengateDeploymentOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[oracledatabasepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb).[GoldengateDeployment](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb#cloud_google_com_go_oracledatabase_apiv1_oracledatabasepb_GoldengateDeployment), [error](https://pkg.go.dev/builtin#error))

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*StartGoldengateDeploymentOperation) Wait 
    
    
    func (op *StartGoldengateDeploymentOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[oracledatabasepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb).[GoldengateDeployment](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb#cloud_google_com_go_oracledatabase_apiv1_oracledatabasepb_GoldengateDeployment), [error](https://pkg.go.dev/builtin#error))

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## StopAutonomousDatabaseOperation
    
    
    type StopAutonomousDatabaseOperation struct {
    	// contains filtered or unexported fields
    }

StopAutonomousDatabaseOperation manages a long-running operation from StopAutonomousDatabase.

### func (*StopAutonomousDatabaseOperation) Done 
    
    
    func (op *StopAutonomousDatabaseOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*StopAutonomousDatabaseOperation) Metadata 
    
    
    func (op *StopAutonomousDatabaseOperation) Metadata() (*[oracledatabasepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb).[OperationMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb#cloud_google_com_go_oracledatabase_apiv1_oracledatabasepb_OperationMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*StopAutonomousDatabaseOperation) Name 
    
    
    func (op *StopAutonomousDatabaseOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*StopAutonomousDatabaseOperation) Poll 
    
    
    func (op *StopAutonomousDatabaseOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[oracledatabasepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb).[AutonomousDatabase](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb#cloud_google_com_go_oracledatabase_apiv1_oracledatabasepb_AutonomousDatabase), [error](https://pkg.go.dev/builtin#error))

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*StopAutonomousDatabaseOperation) Wait 
    
    
    func (op *StopAutonomousDatabaseOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[oracledatabasepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb).[AutonomousDatabase](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb#cloud_google_com_go_oracledatabase_apiv1_oracledatabasepb_AutonomousDatabase), [error](https://pkg.go.dev/builtin#error))

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## StopGoldengateDeploymentOperation
    
    
    type StopGoldengateDeploymentOperation struct {
    	// contains filtered or unexported fields
    }

StopGoldengateDeploymentOperation manages a long-running operation from StopGoldengateDeployment.

### func (*StopGoldengateDeploymentOperation) Done 
    
    
    func (op *StopGoldengateDeploymentOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*StopGoldengateDeploymentOperation) Metadata 
    
    
    func (op *StopGoldengateDeploymentOperation) Metadata() (*[oracledatabasepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb).[OperationMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb#cloud_google_com_go_oracledatabase_apiv1_oracledatabasepb_OperationMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*StopGoldengateDeploymentOperation) Name 
    
    
    func (op *StopGoldengateDeploymentOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*StopGoldengateDeploymentOperation) Poll 
    
    
    func (op *StopGoldengateDeploymentOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[oracledatabasepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb).[GoldengateDeployment](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb#cloud_google_com_go_oracledatabase_apiv1_oracledatabasepb_GoldengateDeployment), [error](https://pkg.go.dev/builtin#error))

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*StopGoldengateDeploymentOperation) Wait 
    
    
    func (op *StopGoldengateDeploymentOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[oracledatabasepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb).[GoldengateDeployment](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb#cloud_google_com_go_oracledatabase_apiv1_oracledatabasepb_GoldengateDeployment), [error](https://pkg.go.dev/builtin#error))

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## SwitchoverAutonomousDatabaseOperation
    
    
    type SwitchoverAutonomousDatabaseOperation struct {
    	// contains filtered or unexported fields
    }

SwitchoverAutonomousDatabaseOperation manages a long-running operation from SwitchoverAutonomousDatabase.

### func (*SwitchoverAutonomousDatabaseOperation) Done 
    
    
    func (op *SwitchoverAutonomousDatabaseOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*SwitchoverAutonomousDatabaseOperation) Metadata 
    
    
    func (op *SwitchoverAutonomousDatabaseOperation) Metadata() (*[oracledatabasepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb).[OperationMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb#cloud_google_com_go_oracledatabase_apiv1_oracledatabasepb_OperationMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*SwitchoverAutonomousDatabaseOperation) Name 
    
    
    func (op *SwitchoverAutonomousDatabaseOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*SwitchoverAutonomousDatabaseOperation) Poll 
    
    
    func (op *SwitchoverAutonomousDatabaseOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[oracledatabasepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb).[AutonomousDatabase](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb#cloud_google_com_go_oracledatabase_apiv1_oracledatabasepb_AutonomousDatabase), [error](https://pkg.go.dev/builtin#error))

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*SwitchoverAutonomousDatabaseOperation) Wait 
    
    
    func (op *SwitchoverAutonomousDatabaseOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[oracledatabasepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb).[AutonomousDatabase](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb#cloud_google_com_go_oracledatabase_apiv1_oracledatabasepb_AutonomousDatabase), [error](https://pkg.go.dev/builtin#error))

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## UpdateAutonomousDatabaseOperation
    
    
    type UpdateAutonomousDatabaseOperation struct {
    	// contains filtered or unexported fields
    }

UpdateAutonomousDatabaseOperation manages a long-running operation from UpdateAutonomousDatabase.

### func (*UpdateAutonomousDatabaseOperation) Done 
    
    
    func (op *UpdateAutonomousDatabaseOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*UpdateAutonomousDatabaseOperation) Metadata 
    
    
    func (op *UpdateAutonomousDatabaseOperation) Metadata() (*[oracledatabasepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb).[OperationMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb#cloud_google_com_go_oracledatabase_apiv1_oracledatabasepb_OperationMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*UpdateAutonomousDatabaseOperation) Name 
    
    
    func (op *UpdateAutonomousDatabaseOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*UpdateAutonomousDatabaseOperation) Poll 
    
    
    func (op *UpdateAutonomousDatabaseOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[oracledatabasepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb).[AutonomousDatabase](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb#cloud_google_com_go_oracledatabase_apiv1_oracledatabasepb_AutonomousDatabase), [error](https://pkg.go.dev/builtin#error))

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*UpdateAutonomousDatabaseOperation) Wait 
    
    
    func (op *UpdateAutonomousDatabaseOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[oracledatabasepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb).[AutonomousDatabase](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb#cloud_google_com_go_oracledatabase_apiv1_oracledatabasepb_AutonomousDatabase), [error](https://pkg.go.dev/builtin#error))

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## UpdateExadbVmClusterOperation
    
    
    type UpdateExadbVmClusterOperation struct {
    	// contains filtered or unexported fields
    }

UpdateExadbVmClusterOperation manages a long-running operation from UpdateExadbVmCluster.

### func (*UpdateExadbVmClusterOperation) Done 
    
    
    func (op *UpdateExadbVmClusterOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*UpdateExadbVmClusterOperation) Metadata 
    
    
    func (op *UpdateExadbVmClusterOperation) Metadata() (*[oracledatabasepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb).[OperationMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb#cloud_google_com_go_oracledatabase_apiv1_oracledatabasepb_OperationMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*UpdateExadbVmClusterOperation) Name 
    
    
    func (op *UpdateExadbVmClusterOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*UpdateExadbVmClusterOperation) Poll 
    
    
    func (op *UpdateExadbVmClusterOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[oracledatabasepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb).[ExadbVmCluster](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb#cloud_google_com_go_oracledatabase_apiv1_oracledatabasepb_ExadbVmCluster), [error](https://pkg.go.dev/builtin#error))

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*UpdateExadbVmClusterOperation) Wait 
    
    
    func (op *UpdateExadbVmClusterOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[oracledatabasepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb).[ExadbVmCluster](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/oracledatabase/latest/apiv1/oracledatabasepb#cloud_google_com_go_oracledatabase_apiv1_oracledatabasepb_ExadbVmCluster), [error](https://pkg.go.dev/builtin#error))

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
