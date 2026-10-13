---
url: https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/filestore/latest/apiv1/
title: Cloud Filestore API v1 - Package cloud.google.com/go/filestore/apiv1 (v1.17.0) \u00a0|\u00a0 Go client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:47:29.043082+00:00
---

# Cloud Filestore API v1 - Package cloud.google.com/go/filestore/apiv1 (v1.17.0)  |  Go client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/filestore/latest/apiv1/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Go ](https://docs.cloud.google.com/go/docs)
  * [ Client libraries ](https://docs.cloud.google.com/go/docs/reference)



Send feedback 

#  Cloud Filestore API v1 - Package cloud.google.com/go/filestore/apiv1 (v1.17.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.17.0 (latest)  1.16.0  1.15.0  1.14.0  1.13.0  1.12.0  1.11.0  1.10.3  1.9.3  1.8.8  1.7.4  1.6.1  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0  0.1.0 

**Note:** To get more information about this package, such as access to older versions, view [this package on pkg.go.dev](https://pkg.go.dev/cloud.google.com/go/filestore/apiv1). 

Package filestore is an auto-generated package for the Cloud Filestore API. 

The Cloud Filestore API is used for creating and managing cloud file servers. 

## General documentation

For information that is relevant for all client libraries please reference <https://pkg.go.dev/cloud.google.com/go#pkg-overview>. Some information on this page includes: 

  * [Authentication and Authorization](https://pkg.go.dev/cloud.google.com/go#hdr-Authentication_and_Authorization)
  * [Timeouts and Cancellation](https://pkg.go.dev/cloud.google.com/go#hdr-Timeouts_and_Cancellation)
  * [Testing against Client Libraries](https://pkg.go.dev/cloud.google.com/go#hdr-Testing)
  * [Debugging Client Libraries](https://pkg.go.dev/cloud.google.com/go#hdr-Debugging)
  * [Inspecting errors](https://pkg.go.dev/cloud.google.com/go#hdr-Inspecting_errors)



## Example usage

To get started with this package, create a client.
    
    
    // go get cloud.google.com/go/filestore/apiv1@latest
    ctx := context.Background()
    // This snippet has been automatically generated and should be regarded as a code template only.
    // It will require modifications to work:
    // - It may require correct/in-range values for request initialization.
    // - It may require specifying regional endpoints when creating the service client as shown in:
    //   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    c, err := filestore.NewCloudFilestoreManagerClient(ctx)
    if err != nil {
        // TODO: Handle error.
    }
    defer c.Close()

The client will use your default application credentials. Clients should be reused instead of created as needed. The methods of Client are safe for concurrent use by multiple goroutines. The returned client must be Closed when it is done being used. 

## Using the Client

The following is an example of making an API call with the newly created client, mentioned above.
    
    
    req := &filestorepb.CreateBackupRequest{
        // TODO: Fill request struct fields.
        // See https://pkg.go.dev/cloud.google.com/go/filestore/apiv1/filestorepb#CreateBackupRequest.
    }
    op, err := c.CreateBackup(ctx, req)
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

The ctx passed to NewCloudFilestoreManagerClient is used for authentication requests and for creating the underlying connection, but is not used for subsequent calls. Individual methods on the client use the ctx given to them. 

To close the open connection, use the Close() method.

## Functions 

### func DefaultAuthScopes 
    
    
    func DefaultAuthScopes() [][string](https://pkg.go.dev/builtin#string)

DefaultAuthScopes reports the default set of authentication scopes to use with this package.

## BackupIterator
    
    
    type BackupIterator struct {
    
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
    	InternalFetch func(pageSize [int](https://pkg.go.dev/builtin#int), pageToken [string](https://pkg.go.dev/builtin#string)) (results []*filestorepb.Backup, nextPageToken [string](https://pkg.go.dev/builtin#string), err [error](https://pkg.go.dev/builtin#error))
    	// contains filtered or unexported fields
    }

BackupIterator manages a stream of *filestorepb.Backup.

### func (*BackupIterator) All 
    
    
    func (it *BackupIterator) All() iter.Seq2[*filestorepb.Backup, error]

All returns an iterator. If an error is returned by the iterator, the iterator will stop after that iteration.

### func (*BackupIterator) Next 
    
    
    func (it *BackupIterator) Next() (*[filestorepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/filestore/latest/apiv1/filestorepb).[Backup](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/filestore/latest/apiv1/filestorepb#cloud_google_com_go_filestore_apiv1_filestorepb_Backup), [error](https://pkg.go.dev/builtin#error))

Next returns the next result. Its second return value is iterator.Done if there are no more results. Once Next returns Done, all subsequent calls will return Done.

### func (*BackupIterator) PageInfo 
    
    
    func (it *BackupIterator) PageInfo() *iterator.PageInfo

PageInfo supports pagination. See the [google.golang.org/api/iterator] package for details.

## CloudFilestoreManagerCallOptions
    
    
    type CloudFilestoreManagerCallOptions struct {
    	ListInstances   []gax.CallOption
    	GetInstance     []gax.CallOption
    	CreateInstance  []gax.CallOption
    	UpdateInstance  []gax.CallOption
    	RestoreInstance []gax.CallOption
    	RevertInstance  []gax.CallOption
    	DeleteInstance  []gax.CallOption
    	ListSnapshots   []gax.CallOption
    	GetSnapshot     []gax.CallOption
    	CreateSnapshot  []gax.CallOption
    	DeleteSnapshot  []gax.CallOption
    	UpdateSnapshot  []gax.CallOption
    	ListBackups     []gax.CallOption
    	GetBackup       []gax.CallOption
    	CreateBackup    []gax.CallOption
    	DeleteBackup    []gax.CallOption
    	UpdateBackup    []gax.CallOption
    	PromoteReplica  []gax.CallOption
    	GetLocation     []gax.CallOption
    	ListLocations   []gax.CallOption
    	CancelOperation []gax.CallOption
    	DeleteOperation []gax.CallOption
    	GetOperation    []gax.CallOption
    	ListOperations  []gax.CallOption
    }

CloudFilestoreManagerCallOptions contains the retry settings for each method of CloudFilestoreManagerClient.

## CloudFilestoreManagerClient
    
    
    type CloudFilestoreManagerClient struct {
    
    	// The call options for this service.
    	CallOptions *CloudFilestoreManagerCallOptions
    
    	// LROClient is used internally to handle long-running operations.
    	// It is exposed so that its CallOptions can be modified if required.
    	// Users should not Close this client.
    	LROClient *lroauto.OperationsClient
    	// contains filtered or unexported fields
    }

CloudFilestoreManagerClient is a client for interacting with Cloud Filestore API. Methods, except Close, may be called concurrently. However, fields must not be modified concurrently with method calls.

Configures and manages Filestore resources.

Filestore Manager v1.

The file.googleapis.com service implements the Filestore API and defines the following resource model for managing instances:
    
    
    The service works with a collection of cloud projects, named: /projects/*
    
    Each project has a collection of available locations, named: /locations/*
    
    Each location has a collection of instances and backups, named:
    /instances/* and /backups/* respectively.
    
    As such, Filestore instances are resources of the form:
    /projects/{project_number}/locations/{location_id}/instances/{instance_id}
    and backups are resources of the form:
    /projects/{project_number}/locations/{location_id}/backup/{backup_id}
    

Note that location_id must be a Google Cloud zone for instances, but a Google Cloud region for backups; for example:
    
    
    projects/12345/locations/us-central1-c/instances/my-filestore
    
    projects/12345/locations/us-central1/backups/my-backup
    

### func NewCloudFilestoreManagerClient 
    
    
    func NewCloudFilestoreManagerClient(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...option.ClientOption) (*CloudFilestoreManagerClient, [error](https://pkg.go.dev/builtin#error))

NewCloudFilestoreManagerClient creates a new cloud filestore manager client based on gRPC. The returned client must be Closed when it is done being used to clean up its underlying connections.

Configures and manages Filestore resources.

Filestore Manager v1.

The file.googleapis.com service implements the Filestore API and defines the following resource model for managing instances:
    
    
    The service works with a collection of cloud projects, named: /projects/*
    
    Each project has a collection of available locations, named: /locations/*
    
    Each location has a collection of instances and backups, named:
    /instances/* and /backups/* respectively.
    
    As such, Filestore instances are resources of the form:
    /projects/{project_number}/locations/{location_id}/instances/{instance_id}
    and backups are resources of the form:
    /projects/{project_number}/locations/{location_id}/backup/{backup_id}
    

Note that location_id must be a Google Cloud zone for instances, but a Google Cloud region for backups; for example:
    
    
    projects/12345/locations/us-central1-c/instances/my-filestore
    
    projects/12345/locations/us-central1/backups/my-backup
    

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	filestore "cloud.google.com/go/filestore/apiv1"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := filestore.NewCloudFilestoreManagerClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/filestore/latest/apiv1.html#cloud_google_com_go_filestore_apiv1_CloudFilestoreManagerClient_Close)()
    
    	// TODO: Use client.
    	_ = c
    }
    

### func NewCloudFilestoreManagerRESTClient 
    
    
    func NewCloudFilestoreManagerRESTClient(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...option.ClientOption) (*CloudFilestoreManagerClient, [error](https://pkg.go.dev/builtin#error))

NewCloudFilestoreManagerRESTClient creates a new cloud filestore manager rest client.

Configures and manages Filestore resources.

Filestore Manager v1.

The file.googleapis.com service implements the Filestore API and defines the following resource model for managing instances:
    
    
    The service works with a collection of cloud projects, named: /projects/*
    
    Each project has a collection of available locations, named: /locations/*
    
    Each location has a collection of instances and backups, named:
    /instances/* and /backups/* respectively.
    
    As such, Filestore instances are resources of the form:
    /projects/{project_number}/locations/{location_id}/instances/{instance_id}
    and backups are resources of the form:
    /projects/{project_number}/locations/{location_id}/backup/{backup_id}
    

Note that location_id must be a Google Cloud zone for instances, but a Google Cloud region for backups; for example:
    
    
    projects/12345/locations/us-central1-c/instances/my-filestore
    
    projects/12345/locations/us-central1/backups/my-backup
    

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	filestore "cloud.google.com/go/filestore/apiv1"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := filestore.[NewCloudFilestoreManagerRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/filestore/latest/apiv1.html#cloud_google_com_go_filestore_apiv1_CloudFilestoreManagerClient_NewCloudFilestoreManagerRESTClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/filestore/latest/apiv1.html#cloud_google_com_go_filestore_apiv1_CloudFilestoreManagerClient_Close)()
    
    	// TODO: Use client.
    	_ = c
    }
    

### func (*CloudFilestoreManagerClient) CancelOperation 
    
    
    func (c *CloudFilestoreManagerClient) CancelOperation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[CancelOperationRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#CancelOperationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

CancelOperation is a utility method from google.longrunning.Operations.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	filestore "cloud.google.com/go/filestore/apiv1"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := filestore.NewCloudFilestoreManagerClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/filestore/latest/apiv1.html#cloud_google_com_go_filestore_apiv1_CloudFilestoreManagerClient_Close)()
    
    	req := &longrunningpb.[CancelOperationRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_CancelOperationRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#CancelOperationRequest.
    	}
    	err = c.CancelOperation(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    }
    

### func (*CloudFilestoreManagerClient) Close 
    
    
    func (c *CloudFilestoreManagerClient) Close() [error](https://pkg.go.dev/builtin#error)

Close closes the connection to the API service. **Always** call Close() when the client is no longer required.

### func (*CloudFilestoreManagerClient) Connection (deprecated)
    
    
    func (c *CloudFilestoreManagerClient) Connection() *grpc.ClientConn

Connection returns a connection to the API service.

Deprecated: Connections are now pooled so this method does not always return the same resource.

### func (*CloudFilestoreManagerClient) CreateBackup 
    
    
    func (c *CloudFilestoreManagerClient) CreateBackup(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[filestorepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/filestore/latest/apiv1/filestorepb).[CreateBackupRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/filestore/latest/apiv1/filestorepb#cloud_google_com_go_filestore_apiv1_filestorepb_CreateBackupRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*CreateBackupOperation, [error](https://pkg.go.dev/builtin#error))

CreateBackup creates a backup.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	filestore "cloud.google.com/go/filestore/apiv1"
    	filestorepb "cloud.google.com/go/filestore/apiv1/filestorepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := filestore.NewCloudFilestoreManagerClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/filestore/latest/apiv1.html#cloud_google_com_go_filestore_apiv1_CloudFilestoreManagerClient_Close)()
    
    	req := &filestorepb.CreateBackupRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/filestore/apiv1/filestorepb#CreateBackupRequest.
    	}
    	op, err := c.CreateBackup(ctx, req)
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
    

### func (*CloudFilestoreManagerClient) CreateBackupOperation 
    
    
    func (c *CloudFilestoreManagerClient) CreateBackupOperation(name [string](https://pkg.go.dev/builtin#string)) *CreateBackupOperation

CreateBackupOperation returns a new CreateBackupOperation from a given name. The name must be that of a previously created CreateBackupOperation, possibly from a different process.

### func (*CloudFilestoreManagerClient) CreateInstance 
    
    
    func (c *CloudFilestoreManagerClient) CreateInstance(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[filestorepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/filestore/latest/apiv1/filestorepb).[CreateInstanceRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/filestore/latest/apiv1/filestorepb#cloud_google_com_go_filestore_apiv1_filestorepb_CreateInstanceRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*CreateInstanceOperation, [error](https://pkg.go.dev/builtin#error))

CreateInstance creates an instance. When creating from a backup, the capacity of the new instance needs to be equal to or larger than the capacity of the backup (and also equal to or larger than the minimum capacity of the tier).

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	filestore "cloud.google.com/go/filestore/apiv1"
    	filestorepb "cloud.google.com/go/filestore/apiv1/filestorepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := filestore.NewCloudFilestoreManagerClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/filestore/latest/apiv1.html#cloud_google_com_go_filestore_apiv1_CloudFilestoreManagerClient_Close)()
    
    	req := &filestorepb.CreateInstanceRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/filestore/apiv1/filestorepb#CreateInstanceRequest.
    	}
    	op, err := c.CreateInstance(ctx, req)
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
    

### func (*CloudFilestoreManagerClient) CreateInstanceOperation 
    
    
    func (c *CloudFilestoreManagerClient) CreateInstanceOperation(name [string](https://pkg.go.dev/builtin#string)) *CreateInstanceOperation

CreateInstanceOperation returns a new CreateInstanceOperation from a given name. The name must be that of a previously created CreateInstanceOperation, possibly from a different process.

### func (*CloudFilestoreManagerClient) CreateSnapshot 
    
    
    func (c *CloudFilestoreManagerClient) CreateSnapshot(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[filestorepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/filestore/latest/apiv1/filestorepb).[CreateSnapshotRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/filestore/latest/apiv1/filestorepb#cloud_google_com_go_filestore_apiv1_filestorepb_CreateSnapshotRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*CreateSnapshotOperation, [error](https://pkg.go.dev/builtin#error))

CreateSnapshot creates a snapshot.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	filestore "cloud.google.com/go/filestore/apiv1"
    	filestorepb "cloud.google.com/go/filestore/apiv1/filestorepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := filestore.NewCloudFilestoreManagerClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/filestore/latest/apiv1.html#cloud_google_com_go_filestore_apiv1_CloudFilestoreManagerClient_Close)()
    
    	req := &filestorepb.CreateSnapshotRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/filestore/apiv1/filestorepb#CreateSnapshotRequest.
    	}
    	op, err := c.CreateSnapshot(ctx, req)
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
    

### func (*CloudFilestoreManagerClient) CreateSnapshotOperation 
    
    
    func (c *CloudFilestoreManagerClient) CreateSnapshotOperation(name [string](https://pkg.go.dev/builtin#string)) *CreateSnapshotOperation

CreateSnapshotOperation returns a new CreateSnapshotOperation from a given name. The name must be that of a previously created CreateSnapshotOperation, possibly from a different process.

### func (*CloudFilestoreManagerClient) DeleteBackup 
    
    
    func (c *CloudFilestoreManagerClient) DeleteBackup(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[filestorepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/filestore/latest/apiv1/filestorepb).[DeleteBackupRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/filestore/latest/apiv1/filestorepb#cloud_google_com_go_filestore_apiv1_filestorepb_DeleteBackupRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*DeleteBackupOperation, [error](https://pkg.go.dev/builtin#error))

DeleteBackup deletes a backup.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	filestore "cloud.google.com/go/filestore/apiv1"
    	filestorepb "cloud.google.com/go/filestore/apiv1/filestorepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := filestore.NewCloudFilestoreManagerClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/filestore/latest/apiv1.html#cloud_google_com_go_filestore_apiv1_CloudFilestoreManagerClient_Close)()
    
    	req := &filestorepb.DeleteBackupRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/filestore/apiv1/filestorepb#DeleteBackupRequest.
    	}
    	op, err := c.DeleteBackup(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    
    	err = op.Wait(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    }
    

### func (*CloudFilestoreManagerClient) DeleteBackupOperation 
    
    
    func (c *CloudFilestoreManagerClient) DeleteBackupOperation(name [string](https://pkg.go.dev/builtin#string)) *DeleteBackupOperation

DeleteBackupOperation returns a new DeleteBackupOperation from a given name. The name must be that of a previously created DeleteBackupOperation, possibly from a different process.

### func (*CloudFilestoreManagerClient) DeleteInstance 
    
    
    func (c *CloudFilestoreManagerClient) DeleteInstance(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[filestorepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/filestore/latest/apiv1/filestorepb).[DeleteInstanceRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/filestore/latest/apiv1/filestorepb#cloud_google_com_go_filestore_apiv1_filestorepb_DeleteInstanceRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*DeleteInstanceOperation, [error](https://pkg.go.dev/builtin#error))

DeleteInstance deletes an instance.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	filestore "cloud.google.com/go/filestore/apiv1"
    	filestorepb "cloud.google.com/go/filestore/apiv1/filestorepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := filestore.NewCloudFilestoreManagerClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/filestore/latest/apiv1.html#cloud_google_com_go_filestore_apiv1_CloudFilestoreManagerClient_Close)()
    
    	req := &filestorepb.DeleteInstanceRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/filestore/apiv1/filestorepb#DeleteInstanceRequest.
    	}
    	op, err := c.DeleteInstance(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    
    	err = op.Wait(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    }
    

### func (*CloudFilestoreManagerClient) DeleteInstanceOperation 
    
    
    func (c *CloudFilestoreManagerClient) DeleteInstanceOperation(name [string](https://pkg.go.dev/builtin#string)) *DeleteInstanceOperation

DeleteInstanceOperation returns a new DeleteInstanceOperation from a given name. The name must be that of a previously created DeleteInstanceOperation, possibly from a different process.

### func (*CloudFilestoreManagerClient) DeleteOperation 
    
    
    func (c *CloudFilestoreManagerClient) DeleteOperation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[DeleteOperationRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#DeleteOperationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

DeleteOperation is a utility method from google.longrunning.Operations.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	filestore "cloud.google.com/go/filestore/apiv1"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := filestore.NewCloudFilestoreManagerClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/filestore/latest/apiv1.html#cloud_google_com_go_filestore_apiv1_CloudFilestoreManagerClient_Close)()
    
    	req := &longrunningpb.[DeleteOperationRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_DeleteOperationRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#DeleteOperationRequest.
    	}
    	err = c.DeleteOperation(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    }
    

### func (*CloudFilestoreManagerClient) DeleteSnapshot 
    
    
    func (c *CloudFilestoreManagerClient) DeleteSnapshot(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[filestorepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/filestore/latest/apiv1/filestorepb).[DeleteSnapshotRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/filestore/latest/apiv1/filestorepb#cloud_google_com_go_filestore_apiv1_filestorepb_DeleteSnapshotRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*DeleteSnapshotOperation, [error](https://pkg.go.dev/builtin#error))

DeleteSnapshot deletes a snapshot.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	filestore "cloud.google.com/go/filestore/apiv1"
    	filestorepb "cloud.google.com/go/filestore/apiv1/filestorepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := filestore.NewCloudFilestoreManagerClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/filestore/latest/apiv1.html#cloud_google_com_go_filestore_apiv1_CloudFilestoreManagerClient_Close)()
    
    	req := &filestorepb.DeleteSnapshotRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/filestore/apiv1/filestorepb#DeleteSnapshotRequest.
    	}
    	op, err := c.DeleteSnapshot(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    
    	err = op.Wait(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    }
    

### func (*CloudFilestoreManagerClient) DeleteSnapshotOperation 
    
    
    func (c *CloudFilestoreManagerClient) DeleteSnapshotOperation(name [string](https://pkg.go.dev/builtin#string)) *DeleteSnapshotOperation

DeleteSnapshotOperation returns a new DeleteSnapshotOperation from a given name. The name must be that of a previously created DeleteSnapshotOperation, possibly from a different process.

### func (*CloudFilestoreManagerClient) GetBackup 
    
    
    func (c *CloudFilestoreManagerClient) GetBackup(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[filestorepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/filestore/latest/apiv1/filestorepb).[GetBackupRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/filestore/latest/apiv1/filestorepb#cloud_google_com_go_filestore_apiv1_filestorepb_GetBackupRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[filestorepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/filestore/latest/apiv1/filestorepb).[Backup](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/filestore/latest/apiv1/filestorepb#cloud_google_com_go_filestore_apiv1_filestorepb_Backup), [error](https://pkg.go.dev/builtin#error))

GetBackup gets the details of a specific backup.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	filestore "cloud.google.com/go/filestore/apiv1"
    	filestorepb "cloud.google.com/go/filestore/apiv1/filestorepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := filestore.NewCloudFilestoreManagerClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/filestore/latest/apiv1.html#cloud_google_com_go_filestore_apiv1_CloudFilestoreManagerClient_Close)()
    
    	req := &filestorepb.GetBackupRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/filestore/apiv1/filestorepb#GetBackupRequest.
    	}
    	resp, err := c.GetBackup(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*CloudFilestoreManagerClient) GetInstance 
    
    
    func (c *CloudFilestoreManagerClient) GetInstance(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[filestorepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/filestore/latest/apiv1/filestorepb).[GetInstanceRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/filestore/latest/apiv1/filestorepb#cloud_google_com_go_filestore_apiv1_filestorepb_GetInstanceRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[filestorepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/filestore/latest/apiv1/filestorepb).[Instance](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/filestore/latest/apiv1/filestorepb#cloud_google_com_go_filestore_apiv1_filestorepb_Instance), [error](https://pkg.go.dev/builtin#error))

GetInstance gets the details of a specific instance.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	filestore "cloud.google.com/go/filestore/apiv1"
    	filestorepb "cloud.google.com/go/filestore/apiv1/filestorepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := filestore.NewCloudFilestoreManagerClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/filestore/latest/apiv1.html#cloud_google_com_go_filestore_apiv1_CloudFilestoreManagerClient_Close)()
    
    	req := &filestorepb.GetInstanceRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/filestore/apiv1/filestorepb#GetInstanceRequest.
    	}
    	resp, err := c.GetInstance(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*CloudFilestoreManagerClient) GetLocation 
    
    
    func (c *CloudFilestoreManagerClient) GetLocation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[locationpb](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location).[GetLocationRequest](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#GetLocationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[locationpb](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location).[Location](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#Location), [error](https://pkg.go.dev/builtin#error))

GetLocation gets information about a location.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	filestore "cloud.google.com/go/filestore/apiv1"
    
    	locationpb "google.golang.org/genproto/googleapis/cloud/location"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := filestore.NewCloudFilestoreManagerClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/filestore/latest/apiv1.html#cloud_google_com_go_filestore_apiv1_CloudFilestoreManagerClient_Close)()
    
    	req := &locationpb.GetLocationRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#GetLocationRequest.
    	}
    	resp, err := c.[GetLocation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/filestore/latest/apiv1.html#cloud_google_com_go_filestore_apiv1_CloudFilestoreManagerClient_GetLocation)(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*CloudFilestoreManagerClient) GetOperation 
    
    
    func (c *CloudFilestoreManagerClient) GetOperation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[GetOperationRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#GetOperationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[Operation](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#Operation), [error](https://pkg.go.dev/builtin#error))

GetOperation is a utility method from google.longrunning.Operations.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	filestore "cloud.google.com/go/filestore/apiv1"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := filestore.NewCloudFilestoreManagerClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/filestore/latest/apiv1.html#cloud_google_com_go_filestore_apiv1_CloudFilestoreManagerClient_Close)()
    
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
    

### func (*CloudFilestoreManagerClient) GetSnapshot 
    
    
    func (c *CloudFilestoreManagerClient) GetSnapshot(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[filestorepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/filestore/latest/apiv1/filestorepb).[GetSnapshotRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/filestore/latest/apiv1/filestorepb#cloud_google_com_go_filestore_apiv1_filestorepb_GetSnapshotRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[filestorepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/filestore/latest/apiv1/filestorepb).[Snapshot](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/filestore/latest/apiv1/filestorepb#cloud_google_com_go_filestore_apiv1_filestorepb_Snapshot), [error](https://pkg.go.dev/builtin#error))

GetSnapshot gets the details of a specific snapshot.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	filestore "cloud.google.com/go/filestore/apiv1"
    	filestorepb "cloud.google.com/go/filestore/apiv1/filestorepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := filestore.NewCloudFilestoreManagerClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/filestore/latest/apiv1.html#cloud_google_com_go_filestore_apiv1_CloudFilestoreManagerClient_Close)()
    
    	req := &filestorepb.GetSnapshotRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/filestore/apiv1/filestorepb#GetSnapshotRequest.
    	}
    	resp, err := c.GetSnapshot(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*CloudFilestoreManagerClient) ListBackups 
    
    
    func (c *CloudFilestoreManagerClient) ListBackups(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[filestorepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/filestore/latest/apiv1/filestorepb).[ListBackupsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/filestore/latest/apiv1/filestorepb#cloud_google_com_go_filestore_apiv1_filestorepb_ListBackupsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *BackupIterator

ListBackups lists all backups in a project for either a specified location or for all locations.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	filestore "cloud.google.com/go/filestore/apiv1"
    	filestorepb "cloud.google.com/go/filestore/apiv1/filestorepb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := filestore.NewCloudFilestoreManagerClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/filestore/latest/apiv1.html#cloud_google_com_go_filestore_apiv1_CloudFilestoreManagerClient_Close)()
    
    	req := &filestorepb.ListBackupsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/filestore/apiv1/filestorepb#ListBackupsRequest.
    	}
    	it := c.ListBackups(ctx, req)
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
    		_ = it.Response.(*filestorepb.ListBackupsResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	filestore "cloud.google.com/go/filestore/apiv1"
    	filestorepb "cloud.google.com/go/filestore/apiv1/filestorepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := filestore.NewCloudFilestoreManagerClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/filestore/latest/apiv1.html#cloud_google_com_go_filestore_apiv1_CloudFilestoreManagerClient_Close)()
    
    	req := &filestorepb.ListBackupsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/filestore/apiv1/filestorepb#ListBackupsRequest.
    	}
    	for resp, err := range c.ListBackups(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*CloudFilestoreManagerClient) ListInstances 
    
    
    func (c *CloudFilestoreManagerClient) ListInstances(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[filestorepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/filestore/latest/apiv1/filestorepb).[ListInstancesRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/filestore/latest/apiv1/filestorepb#cloud_google_com_go_filestore_apiv1_filestorepb_ListInstancesRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *InstanceIterator

ListInstances lists all instances in a project for either a specified location or for all locations.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	filestore "cloud.google.com/go/filestore/apiv1"
    	filestorepb "cloud.google.com/go/filestore/apiv1/filestorepb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := filestore.NewCloudFilestoreManagerClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/filestore/latest/apiv1.html#cloud_google_com_go_filestore_apiv1_CloudFilestoreManagerClient_Close)()
    
    	req := &filestorepb.ListInstancesRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/filestore/apiv1/filestorepb#ListInstancesRequest.
    	}
    	it := c.ListInstances(ctx, req)
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
    		_ = it.Response.(*filestorepb.ListInstancesResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	filestore "cloud.google.com/go/filestore/apiv1"
    	filestorepb "cloud.google.com/go/filestore/apiv1/filestorepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := filestore.NewCloudFilestoreManagerClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/filestore/latest/apiv1.html#cloud_google_com_go_filestore_apiv1_CloudFilestoreManagerClient_Close)()
    
    	req := &filestorepb.ListInstancesRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/filestore/apiv1/filestorepb#ListInstancesRequest.
    	}
    	for resp, err := range c.ListInstances(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*CloudFilestoreManagerClient) ListLocations 
    
    
    func (c *CloudFilestoreManagerClient) ListLocations(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[locationpb](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location).[ListLocationsRequest](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#ListLocationsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *LocationIterator

ListLocations lists information about the supported locations for this service.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	filestore "cloud.google.com/go/filestore/apiv1"
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
    	c, err := filestore.NewCloudFilestoreManagerClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/filestore/latest/apiv1.html#cloud_google_com_go_filestore_apiv1_CloudFilestoreManagerClient_Close)()
    
    	req := &locationpb.ListLocationsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#ListLocationsRequest.
    	}
    	it := c.[ListLocations](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/filestore/latest/apiv1.html#cloud_google_com_go_filestore_apiv1_CloudFilestoreManagerClient_ListLocations)(ctx, req)
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
    
    	filestore "cloud.google.com/go/filestore/apiv1"
    
    	locationpb "google.golang.org/genproto/googleapis/cloud/location"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := filestore.NewCloudFilestoreManagerClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/filestore/latest/apiv1.html#cloud_google_com_go_filestore_apiv1_CloudFilestoreManagerClient_Close)()
    
    	req := &locationpb.ListLocationsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#ListLocationsRequest.
    	}
    	for resp, err := range c.[ListLocations](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/filestore/latest/apiv1.html#cloud_google_com_go_filestore_apiv1_CloudFilestoreManagerClient_ListLocations)(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*CloudFilestoreManagerClient) ListOperations 
    
    
    func (c *CloudFilestoreManagerClient) ListOperations(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[ListOperationsRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#ListOperationsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *OperationIterator

ListOperations is a utility method from google.longrunning.Operations.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	filestore "cloud.google.com/go/filestore/apiv1"
    
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
    	c, err := filestore.NewCloudFilestoreManagerClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/filestore/latest/apiv1.html#cloud_google_com_go_filestore_apiv1_CloudFilestoreManagerClient_Close)()
    
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
    
    	filestore "cloud.google.com/go/filestore/apiv1"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := filestore.NewCloudFilestoreManagerClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/filestore/latest/apiv1.html#cloud_google_com_go_filestore_apiv1_CloudFilestoreManagerClient_Close)()
    
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
    

### func (*CloudFilestoreManagerClient) ListSnapshots 
    
    
    func (c *CloudFilestoreManagerClient) ListSnapshots(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[filestorepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/filestore/latest/apiv1/filestorepb).[ListSnapshotsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/filestore/latest/apiv1/filestorepb#cloud_google_com_go_filestore_apiv1_filestorepb_ListSnapshotsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *SnapshotIterator

ListSnapshots lists all snapshots in a project for either a specified location or for all locations.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	filestore "cloud.google.com/go/filestore/apiv1"
    	filestorepb "cloud.google.com/go/filestore/apiv1/filestorepb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := filestore.NewCloudFilestoreManagerClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/filestore/latest/apiv1.html#cloud_google_com_go_filestore_apiv1_CloudFilestoreManagerClient_Close)()
    
    	req := &filestorepb.ListSnapshotsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/filestore/apiv1/filestorepb#ListSnapshotsRequest.
    	}
    	it := c.ListSnapshots(ctx, req)
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
    		_ = it.Response.(*filestorepb.ListSnapshotsResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	filestore "cloud.google.com/go/filestore/apiv1"
    	filestorepb "cloud.google.com/go/filestore/apiv1/filestorepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := filestore.NewCloudFilestoreManagerClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/filestore/latest/apiv1.html#cloud_google_com_go_filestore_apiv1_CloudFilestoreManagerClient_Close)()
    
    	req := &filestorepb.ListSnapshotsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/filestore/apiv1/filestorepb#ListSnapshotsRequest.
    	}
    	for resp, err := range c.ListSnapshots(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*CloudFilestoreManagerClient) PromoteReplica 
    
    
    func (c *CloudFilestoreManagerClient) PromoteReplica(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[filestorepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/filestore/latest/apiv1/filestorepb).[PromoteReplicaRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/filestore/latest/apiv1/filestorepb#cloud_google_com_go_filestore_apiv1_filestorepb_PromoteReplicaRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*PromoteReplicaOperation, [error](https://pkg.go.dev/builtin#error))

PromoteReplica promote the standby instance (replica).

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	filestore "cloud.google.com/go/filestore/apiv1"
    	filestorepb "cloud.google.com/go/filestore/apiv1/filestorepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := filestore.NewCloudFilestoreManagerClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/filestore/latest/apiv1.html#cloud_google_com_go_filestore_apiv1_CloudFilestoreManagerClient_Close)()
    
    	req := &filestorepb.PromoteReplicaRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/filestore/apiv1/filestorepb#PromoteReplicaRequest.
    	}
    	op, err := c.PromoteReplica(ctx, req)
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
    

### func (*CloudFilestoreManagerClient) PromoteReplicaOperation 
    
    
    func (c *CloudFilestoreManagerClient) PromoteReplicaOperation(name [string](https://pkg.go.dev/builtin#string)) *PromoteReplicaOperation

PromoteReplicaOperation returns a new PromoteReplicaOperation from a given name. The name must be that of a previously created PromoteReplicaOperation, possibly from a different process.

### func (*CloudFilestoreManagerClient) RestoreInstance 
    
    
    func (c *CloudFilestoreManagerClient) RestoreInstance(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[filestorepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/filestore/latest/apiv1/filestorepb).[RestoreInstanceRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/filestore/latest/apiv1/filestorepb#cloud_google_com_go_filestore_apiv1_filestorepb_RestoreInstanceRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*RestoreInstanceOperation, [error](https://pkg.go.dev/builtin#error))

RestoreInstance restores an existing instance’s file share from a backup.

The capacity of the instance needs to be equal to or larger than the capacity of the backup (and also equal to or larger than the minimum capacity of the tier).

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	filestore "cloud.google.com/go/filestore/apiv1"
    	filestorepb "cloud.google.com/go/filestore/apiv1/filestorepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := filestore.NewCloudFilestoreManagerClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/filestore/latest/apiv1.html#cloud_google_com_go_filestore_apiv1_CloudFilestoreManagerClient_Close)()
    
    	req := &filestorepb.RestoreInstanceRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/filestore/apiv1/filestorepb#RestoreInstanceRequest.
    	}
    	op, err := c.RestoreInstance(ctx, req)
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
    

### func (*CloudFilestoreManagerClient) RestoreInstanceOperation 
    
    
    func (c *CloudFilestoreManagerClient) RestoreInstanceOperation(name [string](https://pkg.go.dev/builtin#string)) *RestoreInstanceOperation

RestoreInstanceOperation returns a new RestoreInstanceOperation from a given name. The name must be that of a previously created RestoreInstanceOperation, possibly from a different process.

### func (*CloudFilestoreManagerClient) RevertInstance 
    
    
    func (c *CloudFilestoreManagerClient) RevertInstance(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[filestorepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/filestore/latest/apiv1/filestorepb).[RevertInstanceRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/filestore/latest/apiv1/filestorepb#cloud_google_com_go_filestore_apiv1_filestorepb_RevertInstanceRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*RevertInstanceOperation, [error](https://pkg.go.dev/builtin#error))

RevertInstance revert an existing instance’s file system to a specified snapshot.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	filestore "cloud.google.com/go/filestore/apiv1"
    	filestorepb "cloud.google.com/go/filestore/apiv1/filestorepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := filestore.NewCloudFilestoreManagerClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/filestore/latest/apiv1.html#cloud_google_com_go_filestore_apiv1_CloudFilestoreManagerClient_Close)()
    
    	req := &filestorepb.RevertInstanceRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/filestore/apiv1/filestorepb#RevertInstanceRequest.
    	}
    	op, err := c.RevertInstance(ctx, req)
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
    

### func (*CloudFilestoreManagerClient) RevertInstanceOperation 
    
    
    func (c *CloudFilestoreManagerClient) RevertInstanceOperation(name [string](https://pkg.go.dev/builtin#string)) *RevertInstanceOperation

RevertInstanceOperation returns a new RevertInstanceOperation from a given name. The name must be that of a previously created RevertInstanceOperation, possibly from a different process.

### func (*CloudFilestoreManagerClient) UpdateBackup 
    
    
    func (c *CloudFilestoreManagerClient) UpdateBackup(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[filestorepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/filestore/latest/apiv1/filestorepb).[UpdateBackupRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/filestore/latest/apiv1/filestorepb#cloud_google_com_go_filestore_apiv1_filestorepb_UpdateBackupRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*UpdateBackupOperation, [error](https://pkg.go.dev/builtin#error))

UpdateBackup updates the settings of a specific backup.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	filestore "cloud.google.com/go/filestore/apiv1"
    	filestorepb "cloud.google.com/go/filestore/apiv1/filestorepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := filestore.NewCloudFilestoreManagerClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/filestore/latest/apiv1.html#cloud_google_com_go_filestore_apiv1_CloudFilestoreManagerClient_Close)()
    
    	req := &filestorepb.UpdateBackupRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/filestore/apiv1/filestorepb#UpdateBackupRequest.
    	}
    	op, err := c.UpdateBackup(ctx, req)
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
    

### func (*CloudFilestoreManagerClient) UpdateBackupOperation 
    
    
    func (c *CloudFilestoreManagerClient) UpdateBackupOperation(name [string](https://pkg.go.dev/builtin#string)) *UpdateBackupOperation

UpdateBackupOperation returns a new UpdateBackupOperation from a given name. The name must be that of a previously created UpdateBackupOperation, possibly from a different process.

### func (*CloudFilestoreManagerClient) UpdateInstance 
    
    
    func (c *CloudFilestoreManagerClient) UpdateInstance(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[filestorepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/filestore/latest/apiv1/filestorepb).[UpdateInstanceRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/filestore/latest/apiv1/filestorepb#cloud_google_com_go_filestore_apiv1_filestorepb_UpdateInstanceRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*UpdateInstanceOperation, [error](https://pkg.go.dev/builtin#error))

UpdateInstance updates the settings of a specific instance.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	filestore "cloud.google.com/go/filestore/apiv1"
    	filestorepb "cloud.google.com/go/filestore/apiv1/filestorepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := filestore.NewCloudFilestoreManagerClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/filestore/latest/apiv1.html#cloud_google_com_go_filestore_apiv1_CloudFilestoreManagerClient_Close)()
    
    	req := &filestorepb.UpdateInstanceRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/filestore/apiv1/filestorepb#UpdateInstanceRequest.
    	}
    	op, err := c.UpdateInstance(ctx, req)
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
    

### func (*CloudFilestoreManagerClient) UpdateInstanceOperation 
    
    
    func (c *CloudFilestoreManagerClient) UpdateInstanceOperation(name [string](https://pkg.go.dev/builtin#string)) *UpdateInstanceOperation

UpdateInstanceOperation returns a new UpdateInstanceOperation from a given name. The name must be that of a previously created UpdateInstanceOperation, possibly from a different process.

### func (*CloudFilestoreManagerClient) UpdateSnapshot 
    
    
    func (c *CloudFilestoreManagerClient) UpdateSnapshot(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[filestorepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/filestore/latest/apiv1/filestorepb).[UpdateSnapshotRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/filestore/latest/apiv1/filestorepb#cloud_google_com_go_filestore_apiv1_filestorepb_UpdateSnapshotRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*UpdateSnapshotOperation, [error](https://pkg.go.dev/builtin#error))

UpdateSnapshot updates the settings of a specific snapshot.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	filestore "cloud.google.com/go/filestore/apiv1"
    	filestorepb "cloud.google.com/go/filestore/apiv1/filestorepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := filestore.NewCloudFilestoreManagerClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/filestore/latest/apiv1.html#cloud_google_com_go_filestore_apiv1_CloudFilestoreManagerClient_Close)()
    
    	req := &filestorepb.UpdateSnapshotRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/filestore/apiv1/filestorepb#UpdateSnapshotRequest.
    	}
    	op, err := c.UpdateSnapshot(ctx, req)
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
    

### func (*CloudFilestoreManagerClient) UpdateSnapshotOperation 
    
    
    func (c *CloudFilestoreManagerClient) UpdateSnapshotOperation(name [string](https://pkg.go.dev/builtin#string)) *UpdateSnapshotOperation

UpdateSnapshotOperation returns a new UpdateSnapshotOperation from a given name. The name must be that of a previously created UpdateSnapshotOperation, possibly from a different process.

## CreateBackupOperation
    
    
    type CreateBackupOperation struct {
    	// contains filtered or unexported fields
    }

CreateBackupOperation manages a long-running operation from CreateBackup.

### func (*CreateBackupOperation) Done 
    
    
    func (op *CreateBackupOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*CreateBackupOperation) Metadata 
    
    
    func (op *CreateBackupOperation) Metadata() (*[commonpb](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/common).[OperationMetadata](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/common#OperationMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*CreateBackupOperation) Name 
    
    
    func (op *CreateBackupOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*CreateBackupOperation) Poll 
    
    
    func (op *CreateBackupOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[filestorepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/filestore/latest/apiv1/filestorepb).[Backup](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/filestore/latest/apiv1/filestorepb#cloud_google_com_go_filestore_apiv1_filestorepb_Backup), [error](https://pkg.go.dev/builtin#error))

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*CreateBackupOperation) Wait 
    
    
    func (op *CreateBackupOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[filestorepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/filestore/latest/apiv1/filestorepb).[Backup](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/filestore/latest/apiv1/filestorepb#cloud_google_com_go_filestore_apiv1_filestorepb_Backup), [error](https://pkg.go.dev/builtin#error))

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## CreateInstanceOperation
    
    
    type CreateInstanceOperation struct {
    	// contains filtered or unexported fields
    }

CreateInstanceOperation manages a long-running operation from CreateInstance.

### func (*CreateInstanceOperation) Done 
    
    
    func (op *CreateInstanceOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*CreateInstanceOperation) Metadata 
    
    
    func (op *CreateInstanceOperation) Metadata() (*[commonpb](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/common).[OperationMetadata](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/common#OperationMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*CreateInstanceOperation) Name 
    
    
    func (op *CreateInstanceOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*CreateInstanceOperation) Poll 
    
    
    func (op *CreateInstanceOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[filestorepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/filestore/latest/apiv1/filestorepb).[Instance](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/filestore/latest/apiv1/filestorepb#cloud_google_com_go_filestore_apiv1_filestorepb_Instance), [error](https://pkg.go.dev/builtin#error))

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*CreateInstanceOperation) Wait 
    
    
    func (op *CreateInstanceOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[filestorepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/filestore/latest/apiv1/filestorepb).[Instance](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/filestore/latest/apiv1/filestorepb#cloud_google_com_go_filestore_apiv1_filestorepb_Instance), [error](https://pkg.go.dev/builtin#error))

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## CreateSnapshotOperation
    
    
    type CreateSnapshotOperation struct {
    	// contains filtered or unexported fields
    }

CreateSnapshotOperation manages a long-running operation from CreateSnapshot.

### func (*CreateSnapshotOperation) Done 
    
    
    func (op *CreateSnapshotOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*CreateSnapshotOperation) Metadata 
    
    
    func (op *CreateSnapshotOperation) Metadata() (*[commonpb](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/common).[OperationMetadata](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/common#OperationMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*CreateSnapshotOperation) Name 
    
    
    func (op *CreateSnapshotOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*CreateSnapshotOperation) Poll 
    
    
    func (op *CreateSnapshotOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[filestorepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/filestore/latest/apiv1/filestorepb).[Snapshot](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/filestore/latest/apiv1/filestorepb#cloud_google_com_go_filestore_apiv1_filestorepb_Snapshot), [error](https://pkg.go.dev/builtin#error))

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*CreateSnapshotOperation) Wait 
    
    
    func (op *CreateSnapshotOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[filestorepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/filestore/latest/apiv1/filestorepb).[Snapshot](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/filestore/latest/apiv1/filestorepb#cloud_google_com_go_filestore_apiv1_filestorepb_Snapshot), [error](https://pkg.go.dev/builtin#error))

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## DeleteBackupOperation
    
    
    type DeleteBackupOperation struct {
    	// contains filtered or unexported fields
    }

DeleteBackupOperation manages a long-running operation from DeleteBackup.

### func (*DeleteBackupOperation) Done 
    
    
    func (op *DeleteBackupOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*DeleteBackupOperation) Metadata 
    
    
    func (op *DeleteBackupOperation) Metadata() (*[commonpb](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/common).[OperationMetadata](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/common#OperationMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*DeleteBackupOperation) Name 
    
    
    func (op *DeleteBackupOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*DeleteBackupOperation) Poll 
    
    
    func (op *DeleteBackupOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*DeleteBackupOperation) Wait 
    
    
    func (op *DeleteBackupOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## DeleteInstanceOperation
    
    
    type DeleteInstanceOperation struct {
    	// contains filtered or unexported fields
    }

DeleteInstanceOperation manages a long-running operation from DeleteInstance.

### func (*DeleteInstanceOperation) Done 
    
    
    func (op *DeleteInstanceOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*DeleteInstanceOperation) Metadata 
    
    
    func (op *DeleteInstanceOperation) Metadata() (*[commonpb](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/common).[OperationMetadata](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/common#OperationMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*DeleteInstanceOperation) Name 
    
    
    func (op *DeleteInstanceOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*DeleteInstanceOperation) Poll 
    
    
    func (op *DeleteInstanceOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*DeleteInstanceOperation) Wait 
    
    
    func (op *DeleteInstanceOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## DeleteSnapshotOperation
    
    
    type DeleteSnapshotOperation struct {
    	// contains filtered or unexported fields
    }

DeleteSnapshotOperation manages a long-running operation from DeleteSnapshot.

### func (*DeleteSnapshotOperation) Done 
    
    
    func (op *DeleteSnapshotOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*DeleteSnapshotOperation) Metadata 
    
    
    func (op *DeleteSnapshotOperation) Metadata() (*[commonpb](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/common).[OperationMetadata](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/common#OperationMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*DeleteSnapshotOperation) Name 
    
    
    func (op *DeleteSnapshotOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*DeleteSnapshotOperation) Poll 
    
    
    func (op *DeleteSnapshotOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*DeleteSnapshotOperation) Wait 
    
    
    func (op *DeleteSnapshotOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## InstanceIterator
    
    
    type InstanceIterator struct {
    
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
    	InternalFetch func(pageSize [int](https://pkg.go.dev/builtin#int), pageToken [string](https://pkg.go.dev/builtin#string)) (results []*filestorepb.Instance, nextPageToken [string](https://pkg.go.dev/builtin#string), err [error](https://pkg.go.dev/builtin#error))
    	// contains filtered or unexported fields
    }

InstanceIterator manages a stream of *filestorepb.Instance.

### func (*InstanceIterator) All 
    
    
    func (it *InstanceIterator) All() iter.Seq2[*filestorepb.Instance, error]

All returns an iterator. If an error is returned by the iterator, the iterator will stop after that iteration.

### func (*InstanceIterator) Next 
    
    
    func (it *InstanceIterator) Next() (*[filestorepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/filestore/latest/apiv1/filestorepb).[Instance](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/filestore/latest/apiv1/filestorepb#cloud_google_com_go_filestore_apiv1_filestorepb_Instance), [error](https://pkg.go.dev/builtin#error))

Next returns the next result. Its second return value is iterator.Done if there are no more results. Once Next returns Done, all subsequent calls will return Done.

### func (*InstanceIterator) PageInfo 
    
    
    func (it *InstanceIterator) PageInfo() *iterator.PageInfo

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

## PromoteReplicaOperation
    
    
    type PromoteReplicaOperation struct {
    	// contains filtered or unexported fields
    }

PromoteReplicaOperation manages a long-running operation from PromoteReplica.

### func (*PromoteReplicaOperation) Done 
    
    
    func (op *PromoteReplicaOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*PromoteReplicaOperation) Metadata 
    
    
    func (op *PromoteReplicaOperation) Metadata() (*[commonpb](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/common).[OperationMetadata](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/common#OperationMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*PromoteReplicaOperation) Name 
    
    
    func (op *PromoteReplicaOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*PromoteReplicaOperation) Poll 
    
    
    func (op *PromoteReplicaOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[filestorepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/filestore/latest/apiv1/filestorepb).[Instance](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/filestore/latest/apiv1/filestorepb#cloud_google_com_go_filestore_apiv1_filestorepb_Instance), [error](https://pkg.go.dev/builtin#error))

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*PromoteReplicaOperation) Wait 
    
    
    func (op *PromoteReplicaOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[filestorepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/filestore/latest/apiv1/filestorepb).[Instance](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/filestore/latest/apiv1/filestorepb#cloud_google_com_go_filestore_apiv1_filestorepb_Instance), [error](https://pkg.go.dev/builtin#error))

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## RestoreInstanceOperation
    
    
    type RestoreInstanceOperation struct {
    	// contains filtered or unexported fields
    }

RestoreInstanceOperation manages a long-running operation from RestoreInstance.

### func (*RestoreInstanceOperation) Done 
    
    
    func (op *RestoreInstanceOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*RestoreInstanceOperation) Metadata 
    
    
    func (op *RestoreInstanceOperation) Metadata() (*[commonpb](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/common).[OperationMetadata](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/common#OperationMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*RestoreInstanceOperation) Name 
    
    
    func (op *RestoreInstanceOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*RestoreInstanceOperation) Poll 
    
    
    func (op *RestoreInstanceOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[filestorepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/filestore/latest/apiv1/filestorepb).[Instance](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/filestore/latest/apiv1/filestorepb#cloud_google_com_go_filestore_apiv1_filestorepb_Instance), [error](https://pkg.go.dev/builtin#error))

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*RestoreInstanceOperation) Wait 
    
    
    func (op *RestoreInstanceOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[filestorepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/filestore/latest/apiv1/filestorepb).[Instance](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/filestore/latest/apiv1/filestorepb#cloud_google_com_go_filestore_apiv1_filestorepb_Instance), [error](https://pkg.go.dev/builtin#error))

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## RevertInstanceOperation
    
    
    type RevertInstanceOperation struct {
    	// contains filtered or unexported fields
    }

RevertInstanceOperation manages a long-running operation from RevertInstance.

### func (*RevertInstanceOperation) Done 
    
    
    func (op *RevertInstanceOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*RevertInstanceOperation) Metadata 
    
    
    func (op *RevertInstanceOperation) Metadata() (*[commonpb](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/common).[OperationMetadata](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/common#OperationMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*RevertInstanceOperation) Name 
    
    
    func (op *RevertInstanceOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*RevertInstanceOperation) Poll 
    
    
    func (op *RevertInstanceOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[filestorepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/filestore/latest/apiv1/filestorepb).[Instance](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/filestore/latest/apiv1/filestorepb#cloud_google_com_go_filestore_apiv1_filestorepb_Instance), [error](https://pkg.go.dev/builtin#error))

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*RevertInstanceOperation) Wait 
    
    
    func (op *RevertInstanceOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[filestorepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/filestore/latest/apiv1/filestorepb).[Instance](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/filestore/latest/apiv1/filestorepb#cloud_google_com_go_filestore_apiv1_filestorepb_Instance), [error](https://pkg.go.dev/builtin#error))

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## SnapshotIterator
    
    
    type SnapshotIterator struct {
    
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
    	InternalFetch func(pageSize [int](https://pkg.go.dev/builtin#int), pageToken [string](https://pkg.go.dev/builtin#string)) (results []*filestorepb.Snapshot, nextPageToken [string](https://pkg.go.dev/builtin#string), err [error](https://pkg.go.dev/builtin#error))
    	// contains filtered or unexported fields
    }

SnapshotIterator manages a stream of *filestorepb.Snapshot.

### func (*SnapshotIterator) All 
    
    
    func (it *SnapshotIterator) All() iter.Seq2[*filestorepb.Snapshot, error]

All returns an iterator. If an error is returned by the iterator, the iterator will stop after that iteration.

### func (*SnapshotIterator) Next 
    
    
    func (it *SnapshotIterator) Next() (*[filestorepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/filestore/latest/apiv1/filestorepb).[Snapshot](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/filestore/latest/apiv1/filestorepb#cloud_google_com_go_filestore_apiv1_filestorepb_Snapshot), [error](https://pkg.go.dev/builtin#error))

Next returns the next result. Its second return value is iterator.Done if there are no more results. Once Next returns Done, all subsequent calls will return Done.

### func (*SnapshotIterator) PageInfo 
    
    
    func (it *SnapshotIterator) PageInfo() *iterator.PageInfo

PageInfo supports pagination. See the [google.golang.org/api/iterator] package for details.

## UpdateBackupOperation
    
    
    type UpdateBackupOperation struct {
    	// contains filtered or unexported fields
    }

UpdateBackupOperation manages a long-running operation from UpdateBackup.

### func (*UpdateBackupOperation) Done 
    
    
    func (op *UpdateBackupOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*UpdateBackupOperation) Metadata 
    
    
    func (op *UpdateBackupOperation) Metadata() (*[commonpb](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/common).[OperationMetadata](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/common#OperationMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*UpdateBackupOperation) Name 
    
    
    func (op *UpdateBackupOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*UpdateBackupOperation) Poll 
    
    
    func (op *UpdateBackupOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[filestorepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/filestore/latest/apiv1/filestorepb).[Backup](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/filestore/latest/apiv1/filestorepb#cloud_google_com_go_filestore_apiv1_filestorepb_Backup), [error](https://pkg.go.dev/builtin#error))

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*UpdateBackupOperation) Wait 
    
    
    func (op *UpdateBackupOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[filestorepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/filestore/latest/apiv1/filestorepb).[Backup](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/filestore/latest/apiv1/filestorepb#cloud_google_com_go_filestore_apiv1_filestorepb_Backup), [error](https://pkg.go.dev/builtin#error))

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## UpdateInstanceOperation
    
    
    type UpdateInstanceOperation struct {
    	// contains filtered or unexported fields
    }

UpdateInstanceOperation manages a long-running operation from UpdateInstance.

### func (*UpdateInstanceOperation) Done 
    
    
    func (op *UpdateInstanceOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*UpdateInstanceOperation) Metadata 
    
    
    func (op *UpdateInstanceOperation) Metadata() (*[commonpb](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/common).[OperationMetadata](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/common#OperationMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*UpdateInstanceOperation) Name 
    
    
    func (op *UpdateInstanceOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*UpdateInstanceOperation) Poll 
    
    
    func (op *UpdateInstanceOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[filestorepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/filestore/latest/apiv1/filestorepb).[Instance](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/filestore/latest/apiv1/filestorepb#cloud_google_com_go_filestore_apiv1_filestorepb_Instance), [error](https://pkg.go.dev/builtin#error))

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*UpdateInstanceOperation) Wait 
    
    
    func (op *UpdateInstanceOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[filestorepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/filestore/latest/apiv1/filestorepb).[Instance](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/filestore/latest/apiv1/filestorepb#cloud_google_com_go_filestore_apiv1_filestorepb_Instance), [error](https://pkg.go.dev/builtin#error))

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## UpdateSnapshotOperation
    
    
    type UpdateSnapshotOperation struct {
    	// contains filtered or unexported fields
    }

UpdateSnapshotOperation manages a long-running operation from UpdateSnapshot.

### func (*UpdateSnapshotOperation) Done 
    
    
    func (op *UpdateSnapshotOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*UpdateSnapshotOperation) Metadata 
    
    
    func (op *UpdateSnapshotOperation) Metadata() (*[commonpb](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/common).[OperationMetadata](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/common#OperationMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*UpdateSnapshotOperation) Name 
    
    
    func (op *UpdateSnapshotOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*UpdateSnapshotOperation) Poll 
    
    
    func (op *UpdateSnapshotOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[filestorepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/filestore/latest/apiv1/filestorepb).[Snapshot](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/filestore/latest/apiv1/filestorepb#cloud_google_com_go_filestore_apiv1_filestorepb_Snapshot), [error](https://pkg.go.dev/builtin#error))

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*UpdateSnapshotOperation) Wait 
    
    
    func (op *UpdateSnapshotOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[filestorepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/filestore/latest/apiv1/filestorepb).[Snapshot](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/filestore/latest/apiv1/filestorepb#cloud_google_com_go_filestore_apiv1_filestorepb_Snapshot), [error](https://pkg.go.dev/builtin#error))

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
