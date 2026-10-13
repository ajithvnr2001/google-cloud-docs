---
url: https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/metastore/latest/apiv1/
title: Dataproc Metastore API v1 - Package cloud.google.com/go/metastore/apiv1 (v1.21.0) \u00a0|\u00a0 Go client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:59:06.384646+00:00
---

# Dataproc Metastore API v1 - Package cloud.google.com/go/metastore/apiv1 (v1.21.0)  |  Go client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/metastore/latest/apiv1/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Go ](https://docs.cloud.google.com/go/docs)
  * [ Client libraries ](https://docs.cloud.google.com/go/docs/reference)



Send feedback 

#  Dataproc Metastore API v1 - Package cloud.google.com/go/metastore/apiv1 (v1.21.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.21.0 (latest)  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.8  1.13.11  1.12.0  1.11.1  1.10.1  1.9.1  1.8.0  1.7.0  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0  0.2.0 

**Note:** To get more information about this package, such as access to older versions, view [this package on pkg.go.dev](https://pkg.go.dev/cloud.google.com/go/metastore/apiv1). 

Package metastore is an auto-generated package for the Dataproc Metastore API. 

The Dataproc Metastore API is used to manage the lifecycle and configuration of metastore services. 

## General documentation

For information that is relevant for all client libraries please reference <https://pkg.go.dev/cloud.google.com/go#pkg-overview>. Some information on this page includes: 

  * [Authentication and Authorization](https://pkg.go.dev/cloud.google.com/go#hdr-Authentication_and_Authorization)
  * [Timeouts and Cancellation](https://pkg.go.dev/cloud.google.com/go#hdr-Timeouts_and_Cancellation)
  * [Testing against Client Libraries](https://pkg.go.dev/cloud.google.com/go#hdr-Testing)
  * [Debugging Client Libraries](https://pkg.go.dev/cloud.google.com/go#hdr-Debugging)
  * [Inspecting errors](https://pkg.go.dev/cloud.google.com/go#hdr-Inspecting_errors)



## Example usage

To get started with this package, create a client.
    
    
    // go get cloud.google.com/go/metastore/apiv1@latest
    ctx := context.Background()
    // This snippet has been automatically generated and should be regarded as a code template only.
    // It will require modifications to work:
    // - It may require correct/in-range values for request initialization.
    // - It may require specifying regional endpoints when creating the service client as shown in:
    //   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    c, err := metastore.NewDataprocMetastoreClient(ctx)
    if err != nil {
        // TODO: Handle error.
    }
    defer c.Close()

The client will use your default application credentials. Clients should be reused instead of created as needed. The methods of Client are safe for concurrent use by multiple goroutines. The returned client must be Closed when it is done being used. 

## Using the Client

The following is an example of making an API call with the newly created client, mentioned above.
    
    
    req := &metastorepb.AlterMetadataResourceLocationRequest{
        // TODO: Fill request struct fields.
        // See https://pkg.go.dev/cloud.google.com/go/metastore/apiv1/metastorepb#AlterMetadataResourceLocationRequest.
    }
    op, err := c.AlterMetadataResourceLocation(ctx, req)
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

The ctx passed to NewDataprocMetastoreClient is used for authentication requests and for creating the underlying connection, but is not used for subsequent calls. Individual methods on the client use the ctx given to them. 

To close the open connection, use the Close() method.

## Functions 

### func DefaultAuthScopes 
    
    
    func DefaultAuthScopes() [][string](https://pkg.go.dev/builtin#string)

DefaultAuthScopes reports the default set of authentication scopes to use with this package.

## AlterMetadataResourceLocationOperation
    
    
    type AlterMetadataResourceLocationOperation struct {
    	// contains filtered or unexported fields
    }

AlterMetadataResourceLocationOperation manages a long-running operation from AlterMetadataResourceLocation.

### func (*AlterMetadataResourceLocationOperation) Done 
    
    
    func (op *AlterMetadataResourceLocationOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*AlterMetadataResourceLocationOperation) Metadata 
    
    
    func (op *AlterMetadataResourceLocationOperation) Metadata() (*[metastorepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/metastore/latest/apiv1/metastorepb).[OperationMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/metastore/latest/apiv1/metastorepb#cloud_google_com_go_metastore_apiv1_metastorepb_OperationMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*AlterMetadataResourceLocationOperation) Name 
    
    
    func (op *AlterMetadataResourceLocationOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*AlterMetadataResourceLocationOperation) Poll 
    
    
    func (op *AlterMetadataResourceLocationOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[metastorepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/metastore/latest/apiv1/metastorepb).[AlterMetadataResourceLocationResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/metastore/latest/apiv1/metastorepb#cloud_google_com_go_metastore_apiv1_metastorepb_AlterMetadataResourceLocationResponse), [error](https://pkg.go.dev/builtin#error))

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*AlterMetadataResourceLocationOperation) Wait 
    
    
    func (op *AlterMetadataResourceLocationOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[metastorepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/metastore/latest/apiv1/metastorepb).[AlterMetadataResourceLocationResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/metastore/latest/apiv1/metastorepb#cloud_google_com_go_metastore_apiv1_metastorepb_AlterMetadataResourceLocationResponse), [error](https://pkg.go.dev/builtin#error))

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

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
    	InternalFetch func(pageSize [int](https://pkg.go.dev/builtin#int), pageToken [string](https://pkg.go.dev/builtin#string)) (results []*metastorepb.Backup, nextPageToken [string](https://pkg.go.dev/builtin#string), err [error](https://pkg.go.dev/builtin#error))
    	// contains filtered or unexported fields
    }

BackupIterator manages a stream of *metastorepb.Backup.

### func (*BackupIterator) All 
    
    
    func (it *BackupIterator) All() iter.Seq2[*metastorepb.Backup, error]

All returns an iterator. If an error is returned by the iterator, the iterator will stop after that iteration.

### func (*BackupIterator) Next 
    
    
    func (it *BackupIterator) Next() (*[metastorepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/metastore/latest/apiv1/metastorepb).[Backup](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/metastore/latest/apiv1/metastorepb#cloud_google_com_go_metastore_apiv1_metastorepb_Backup), [error](https://pkg.go.dev/builtin#error))

Next returns the next result. Its second return value is iterator.Done if there are no more results. Once Next returns Done, all subsequent calls will return Done.

### func (*BackupIterator) PageInfo 
    
    
    func (it *BackupIterator) PageInfo() *iterator.PageInfo

PageInfo supports pagination. See the [google.golang.org/api/iterator] package for details.

## CreateBackupOperation
    
    
    type CreateBackupOperation struct {
    	// contains filtered or unexported fields
    }

CreateBackupOperation manages a long-running operation from CreateBackup.

### func (*CreateBackupOperation) Done 
    
    
    func (op *CreateBackupOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*CreateBackupOperation) Metadata 
    
    
    func (op *CreateBackupOperation) Metadata() (*[metastorepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/metastore/latest/apiv1/metastorepb).[OperationMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/metastore/latest/apiv1/metastorepb#cloud_google_com_go_metastore_apiv1_metastorepb_OperationMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*CreateBackupOperation) Name 
    
    
    func (op *CreateBackupOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*CreateBackupOperation) Poll 
    
    
    func (op *CreateBackupOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[metastorepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/metastore/latest/apiv1/metastorepb).[Backup](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/metastore/latest/apiv1/metastorepb#cloud_google_com_go_metastore_apiv1_metastorepb_Backup), [error](https://pkg.go.dev/builtin#error))

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*CreateBackupOperation) Wait 
    
    
    func (op *CreateBackupOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[metastorepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/metastore/latest/apiv1/metastorepb).[Backup](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/metastore/latest/apiv1/metastorepb#cloud_google_com_go_metastore_apiv1_metastorepb_Backup), [error](https://pkg.go.dev/builtin#error))

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## CreateFederationOperation
    
    
    type CreateFederationOperation struct {
    	// contains filtered or unexported fields
    }

CreateFederationOperation manages a long-running operation from CreateFederation.

### func (*CreateFederationOperation) Done 
    
    
    func (op *CreateFederationOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*CreateFederationOperation) Metadata 
    
    
    func (op *CreateFederationOperation) Metadata() (*[metastorepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/metastore/latest/apiv1/metastorepb).[OperationMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/metastore/latest/apiv1/metastorepb#cloud_google_com_go_metastore_apiv1_metastorepb_OperationMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*CreateFederationOperation) Name 
    
    
    func (op *CreateFederationOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*CreateFederationOperation) Poll 
    
    
    func (op *CreateFederationOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[metastorepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/metastore/latest/apiv1/metastorepb).[Federation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/metastore/latest/apiv1/metastorepb#cloud_google_com_go_metastore_apiv1_metastorepb_Federation), [error](https://pkg.go.dev/builtin#error))

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*CreateFederationOperation) Wait 
    
    
    func (op *CreateFederationOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[metastorepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/metastore/latest/apiv1/metastorepb).[Federation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/metastore/latest/apiv1/metastorepb#cloud_google_com_go_metastore_apiv1_metastorepb_Federation), [error](https://pkg.go.dev/builtin#error))

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## CreateMetadataImportOperation
    
    
    type CreateMetadataImportOperation struct {
    	// contains filtered or unexported fields
    }

CreateMetadataImportOperation manages a long-running operation from CreateMetadataImport.

### func (*CreateMetadataImportOperation) Done 
    
    
    func (op *CreateMetadataImportOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*CreateMetadataImportOperation) Metadata 
    
    
    func (op *CreateMetadataImportOperation) Metadata() (*[metastorepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/metastore/latest/apiv1/metastorepb).[OperationMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/metastore/latest/apiv1/metastorepb#cloud_google_com_go_metastore_apiv1_metastorepb_OperationMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*CreateMetadataImportOperation) Name 
    
    
    func (op *CreateMetadataImportOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*CreateMetadataImportOperation) Poll 
    
    
    func (op *CreateMetadataImportOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[metastorepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/metastore/latest/apiv1/metastorepb).[MetadataImport](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/metastore/latest/apiv1/metastorepb#cloud_google_com_go_metastore_apiv1_metastorepb_MetadataImport), [error](https://pkg.go.dev/builtin#error))

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*CreateMetadataImportOperation) Wait 
    
    
    func (op *CreateMetadataImportOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[metastorepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/metastore/latest/apiv1/metastorepb).[MetadataImport](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/metastore/latest/apiv1/metastorepb#cloud_google_com_go_metastore_apiv1_metastorepb_MetadataImport), [error](https://pkg.go.dev/builtin#error))

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## CreateServiceOperation
    
    
    type CreateServiceOperation struct {
    	// contains filtered or unexported fields
    }

CreateServiceOperation manages a long-running operation from CreateService.

### func (*CreateServiceOperation) Done 
    
    
    func (op *CreateServiceOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*CreateServiceOperation) Metadata 
    
    
    func (op *CreateServiceOperation) Metadata() (*[metastorepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/metastore/latest/apiv1/metastorepb).[OperationMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/metastore/latest/apiv1/metastorepb#cloud_google_com_go_metastore_apiv1_metastorepb_OperationMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*CreateServiceOperation) Name 
    
    
    func (op *CreateServiceOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*CreateServiceOperation) Poll 
    
    
    func (op *CreateServiceOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[metastorepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/metastore/latest/apiv1/metastorepb).[Service](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/metastore/latest/apiv1/metastorepb#cloud_google_com_go_metastore_apiv1_metastorepb_Service), [error](https://pkg.go.dev/builtin#error))

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*CreateServiceOperation) Wait 
    
    
    func (op *CreateServiceOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[metastorepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/metastore/latest/apiv1/metastorepb).[Service](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/metastore/latest/apiv1/metastorepb#cloud_google_com_go_metastore_apiv1_metastorepb_Service), [error](https://pkg.go.dev/builtin#error))

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## DataprocMetastoreCallOptions
    
    
    type DataprocMetastoreCallOptions struct {
    	ListServices                  []gax.CallOption
    	GetService                    []gax.CallOption
    	CreateService                 []gax.CallOption
    	UpdateService                 []gax.CallOption
    	DeleteService                 []gax.CallOption
    	ListMetadataImports           []gax.CallOption
    	GetMetadataImport             []gax.CallOption
    	CreateMetadataImport          []gax.CallOption
    	UpdateMetadataImport          []gax.CallOption
    	ExportMetadata                []gax.CallOption
    	RestoreService                []gax.CallOption
    	ListBackups                   []gax.CallOption
    	GetBackup                     []gax.CallOption
    	CreateBackup                  []gax.CallOption
    	DeleteBackup                  []gax.CallOption
    	QueryMetadata                 []gax.CallOption
    	MoveTableToDatabase           []gax.CallOption
    	AlterMetadataResourceLocation []gax.CallOption
    	GetLocation                   []gax.CallOption
    	ListLocations                 []gax.CallOption
    	GetIamPolicy                  []gax.CallOption
    	SetIamPolicy                  []gax.CallOption
    	TestIamPermissions            []gax.CallOption
    	CancelOperation               []gax.CallOption
    	DeleteOperation               []gax.CallOption
    	GetOperation                  []gax.CallOption
    	ListOperations                []gax.CallOption
    }

DataprocMetastoreCallOptions contains the retry settings for each method of DataprocMetastoreClient.

## DataprocMetastoreClient
    
    
    type DataprocMetastoreClient struct {
    
    	// The call options for this service.
    	CallOptions *DataprocMetastoreCallOptions
    
    	// LROClient is used internally to handle long-running operations.
    	// It is exposed so that its CallOptions can be modified if required.
    	// Users should not Close this client.
    	LROClient *lroauto.OperationsClient
    	// contains filtered or unexported fields
    }

DataprocMetastoreClient is a client for interacting with Dataproc Metastore API. Methods, except Close, may be called concurrently. However, fields must not be modified concurrently with method calls.

Configures and manages metastore services. Metastore services are fully managed, highly available, autoscaled, autohealing, OSS-native deployments of technical metadata management software. Each metastore service exposes a network endpoint through which metadata queries are served. Metadata queries can originate from a variety of sources, including Apache Hive, Apache Presto, and Apache Spark.

The Dataproc Metastore API defines the following resource model:
    
    
    The service works with a collection of Google Cloud projects, named:
    /projects/*
    
    Each project has a collection of available locations, named: /locations/*
    (a location must refer to a Google Cloud region)
    
    Each location has a collection of services, named: /services/*
    
    Dataproc Metastore services are resources with names of the form:
    

/projects/{project_number}/locations/{location_id}/services/{service_id}.

### func NewDataprocMetastoreClient 
    
    
    func NewDataprocMetastoreClient(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...option.ClientOption) (*DataprocMetastoreClient, [error](https://pkg.go.dev/builtin#error))

NewDataprocMetastoreClient creates a new dataproc metastore client based on gRPC. The returned client must be Closed when it is done being used to clean up its underlying connections.

Configures and manages metastore services. Metastore services are fully managed, highly available, autoscaled, autohealing, OSS-native deployments of technical metadata management software. Each metastore service exposes a network endpoint through which metadata queries are served. Metadata queries can originate from a variety of sources, including Apache Hive, Apache Presto, and Apache Spark.

The Dataproc Metastore API defines the following resource model:
    
    
    The service works with a collection of Google Cloud projects, named:
    /projects/*
    
    Each project has a collection of available locations, named: /locations/*
    (a location must refer to a Google Cloud region)
    
    Each location has a collection of services, named: /services/*
    
    Dataproc Metastore services are resources with names of the form:
    

/projects/{project_number}/locations/{location_id}/services/{service_id}.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	metastore "cloud.google.com/go/metastore/apiv1"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := metastore.NewDataprocMetastoreClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	// TODO: Use client.
    	_ = c
    }
    

### func NewDataprocMetastoreRESTClient 
    
    
    func NewDataprocMetastoreRESTClient(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...option.ClientOption) (*DataprocMetastoreClient, [error](https://pkg.go.dev/builtin#error))

NewDataprocMetastoreRESTClient creates a new dataproc metastore rest client.

Configures and manages metastore services. Metastore services are fully managed, highly available, autoscaled, autohealing, OSS-native deployments of technical metadata management software. Each metastore service exposes a network endpoint through which metadata queries are served. Metadata queries can originate from a variety of sources, including Apache Hive, Apache Presto, and Apache Spark.

The Dataproc Metastore API defines the following resource model:
    
    
    The service works with a collection of Google Cloud projects, named:
    /projects/*
    
    Each project has a collection of available locations, named: /locations/*
    (a location must refer to a Google Cloud region)
    
    Each location has a collection of services, named: /services/*
    
    Dataproc Metastore services are resources with names of the form:
    

/projects/{project_number}/locations/{location_id}/services/{service_id}.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	metastore "cloud.google.com/go/metastore/apiv1"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := metastore.[NewDataprocMetastoreRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/metastore/latest/apiv1.html#cloud_google_com_go_metastore_apiv1_DataprocMetastoreClient_NewDataprocMetastoreRESTClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	// TODO: Use client.
    	_ = c
    }
    

### func (*DataprocMetastoreClient) AlterMetadataResourceLocation 
    
    
    func (c *DataprocMetastoreClient) AlterMetadataResourceLocation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[metastorepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/metastore/latest/apiv1/metastorepb).[AlterMetadataResourceLocationRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/metastore/latest/apiv1/metastorepb#cloud_google_com_go_metastore_apiv1_metastorepb_AlterMetadataResourceLocationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*AlterMetadataResourceLocationOperation, [error](https://pkg.go.dev/builtin#error))

AlterMetadataResourceLocation alter metadata resource location. The metadata resource can be a database, table, or partition. This functionality only updates the parent directory for the respective metadata resource and does not transfer any existing data to the new location.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	metastore "cloud.google.com/go/metastore/apiv1"
    
    	metastorepb "cloud.google.com/go/metastore/apiv1/metastorepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := metastore.NewDataprocMetastoreClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &metastorepb.AlterMetadataResourceLocationRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/metastore/apiv1/metastorepb#AlterMetadataResourceLocationRequest.
    	}
    	op, err := c.AlterMetadataResourceLocation(ctx, req)
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
    

### func (*DataprocMetastoreClient) AlterMetadataResourceLocationOperation 
    
    
    func (c *DataprocMetastoreClient) AlterMetadataResourceLocationOperation(name [string](https://pkg.go.dev/builtin#string)) *AlterMetadataResourceLocationOperation

AlterMetadataResourceLocationOperation returns a new AlterMetadataResourceLocationOperation from a given name. The name must be that of a previously created AlterMetadataResourceLocationOperation, possibly from a different process.

### func (*DataprocMetastoreClient) CancelOperation 
    
    
    func (c *DataprocMetastoreClient) CancelOperation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[CancelOperationRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#CancelOperationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

CancelOperation is a utility method from google.longrunning.Operations.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    
    	metastore "cloud.google.com/go/metastore/apiv1"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := metastore.NewDataprocMetastoreClient(ctx)
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
    

### func (*DataprocMetastoreClient) Close 
    
    
    func (c *DataprocMetastoreClient) Close() [error](https://pkg.go.dev/builtin#error)

Close closes the connection to the API service. **Always** call Close() when the client is no longer required.

### func (*DataprocMetastoreClient) Connection (deprecated)
    
    
    func (c *DataprocMetastoreClient) Connection() *grpc.ClientConn

Connection returns a connection to the API service.

Deprecated: Connections are now pooled so this method does not always return the same resource.

### func (*DataprocMetastoreClient) CreateBackup 
    
    
    func (c *DataprocMetastoreClient) CreateBackup(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[metastorepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/metastore/latest/apiv1/metastorepb).[CreateBackupRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/metastore/latest/apiv1/metastorepb#cloud_google_com_go_metastore_apiv1_metastorepb_CreateBackupRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*CreateBackupOperation, [error](https://pkg.go.dev/builtin#error))

CreateBackup creates a new backup in a given project and location.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	metastore "cloud.google.com/go/metastore/apiv1"
    
    	metastorepb "cloud.google.com/go/metastore/apiv1/metastorepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := metastore.NewDataprocMetastoreClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &metastorepb.CreateBackupRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/metastore/apiv1/metastorepb#CreateBackupRequest.
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
    

### func (*DataprocMetastoreClient) CreateBackupOperation 
    
    
    func (c *DataprocMetastoreClient) CreateBackupOperation(name [string](https://pkg.go.dev/builtin#string)) *CreateBackupOperation

CreateBackupOperation returns a new CreateBackupOperation from a given name. The name must be that of a previously created CreateBackupOperation, possibly from a different process.

### func (*DataprocMetastoreClient) CreateMetadataImport 
    
    
    func (c *DataprocMetastoreClient) CreateMetadataImport(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[metastorepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/metastore/latest/apiv1/metastorepb).[CreateMetadataImportRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/metastore/latest/apiv1/metastorepb#cloud_google_com_go_metastore_apiv1_metastorepb_CreateMetadataImportRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*CreateMetadataImportOperation, [error](https://pkg.go.dev/builtin#error))

CreateMetadataImport creates a new MetadataImport in a given project and location.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	metastore "cloud.google.com/go/metastore/apiv1"
    
    	metastorepb "cloud.google.com/go/metastore/apiv1/metastorepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := metastore.NewDataprocMetastoreClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &metastorepb.CreateMetadataImportRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/metastore/apiv1/metastorepb#CreateMetadataImportRequest.
    	}
    	op, err := c.CreateMetadataImport(ctx, req)
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
    

### func (*DataprocMetastoreClient) CreateMetadataImportOperation 
    
    
    func (c *DataprocMetastoreClient) CreateMetadataImportOperation(name [string](https://pkg.go.dev/builtin#string)) *CreateMetadataImportOperation

CreateMetadataImportOperation returns a new CreateMetadataImportOperation from a given name. The name must be that of a previously created CreateMetadataImportOperation, possibly from a different process.

### func (*DataprocMetastoreClient) CreateService 
    
    
    func (c *DataprocMetastoreClient) CreateService(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[metastorepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/metastore/latest/apiv1/metastorepb).[CreateServiceRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/metastore/latest/apiv1/metastorepb#cloud_google_com_go_metastore_apiv1_metastorepb_CreateServiceRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*CreateServiceOperation, [error](https://pkg.go.dev/builtin#error))

CreateService creates a metastore service in a project and location.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	metastore "cloud.google.com/go/metastore/apiv1"
    
    	metastorepb "cloud.google.com/go/metastore/apiv1/metastorepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := metastore.NewDataprocMetastoreClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &metastorepb.CreateServiceRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/metastore/apiv1/metastorepb#CreateServiceRequest.
    	}
    	op, err := c.CreateService(ctx, req)
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
    

### func (*DataprocMetastoreClient) CreateServiceOperation 
    
    
    func (c *DataprocMetastoreClient) CreateServiceOperation(name [string](https://pkg.go.dev/builtin#string)) *CreateServiceOperation

CreateServiceOperation returns a new CreateServiceOperation from a given name. The name must be that of a previously created CreateServiceOperation, possibly from a different process.

### func (*DataprocMetastoreClient) DeleteBackup 
    
    
    func (c *DataprocMetastoreClient) DeleteBackup(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[metastorepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/metastore/latest/apiv1/metastorepb).[DeleteBackupRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/metastore/latest/apiv1/metastorepb#cloud_google_com_go_metastore_apiv1_metastorepb_DeleteBackupRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*DeleteBackupOperation, [error](https://pkg.go.dev/builtin#error))

DeleteBackup deletes a single backup.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	metastore "cloud.google.com/go/metastore/apiv1"
    
    	metastorepb "cloud.google.com/go/metastore/apiv1/metastorepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := metastore.NewDataprocMetastoreClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &metastorepb.DeleteBackupRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/metastore/apiv1/metastorepb#DeleteBackupRequest.
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
    

### func (*DataprocMetastoreClient) DeleteBackupOperation 
    
    
    func (c *DataprocMetastoreClient) DeleteBackupOperation(name [string](https://pkg.go.dev/builtin#string)) *DeleteBackupOperation

DeleteBackupOperation returns a new DeleteBackupOperation from a given name. The name must be that of a previously created DeleteBackupOperation, possibly from a different process.

### func (*DataprocMetastoreClient) DeleteOperation 
    
    
    func (c *DataprocMetastoreClient) DeleteOperation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[DeleteOperationRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#DeleteOperationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

DeleteOperation is a utility method from google.longrunning.Operations.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    
    	metastore "cloud.google.com/go/metastore/apiv1"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := metastore.NewDataprocMetastoreClient(ctx)
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
    

### func (*DataprocMetastoreClient) DeleteService 
    
    
    func (c *DataprocMetastoreClient) DeleteService(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[metastorepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/metastore/latest/apiv1/metastorepb).[DeleteServiceRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/metastore/latest/apiv1/metastorepb#cloud_google_com_go_metastore_apiv1_metastorepb_DeleteServiceRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*DeleteServiceOperation, [error](https://pkg.go.dev/builtin#error))

DeleteService deletes a single service.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	metastore "cloud.google.com/go/metastore/apiv1"
    
    	metastorepb "cloud.google.com/go/metastore/apiv1/metastorepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := metastore.NewDataprocMetastoreClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &metastorepb.DeleteServiceRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/metastore/apiv1/metastorepb#DeleteServiceRequest.
    	}
    	op, err := c.DeleteService(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    
    	err = op.Wait(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    }
    

### func (*DataprocMetastoreClient) DeleteServiceOperation 
    
    
    func (c *DataprocMetastoreClient) DeleteServiceOperation(name [string](https://pkg.go.dev/builtin#string)) *DeleteServiceOperation

DeleteServiceOperation returns a new DeleteServiceOperation from a given name. The name must be that of a previously created DeleteServiceOperation, possibly from a different process.

### func (*DataprocMetastoreClient) ExportMetadata 
    
    
    func (c *DataprocMetastoreClient) ExportMetadata(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[metastorepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/metastore/latest/apiv1/metastorepb).[ExportMetadataRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/metastore/latest/apiv1/metastorepb#cloud_google_com_go_metastore_apiv1_metastorepb_ExportMetadataRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*ExportMetadataOperation, [error](https://pkg.go.dev/builtin#error))

ExportMetadata exports metadata from a service.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	metastore "cloud.google.com/go/metastore/apiv1"
    
    	metastorepb "cloud.google.com/go/metastore/apiv1/metastorepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := metastore.NewDataprocMetastoreClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &metastorepb.ExportMetadataRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/metastore/apiv1/metastorepb#ExportMetadataRequest.
    	}
    	op, err := c.ExportMetadata(ctx, req)
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
    

### func (*DataprocMetastoreClient) ExportMetadataOperation 
    
    
    func (c *DataprocMetastoreClient) ExportMetadataOperation(name [string](https://pkg.go.dev/builtin#string)) *ExportMetadataOperation

ExportMetadataOperation returns a new ExportMetadataOperation from a given name. The name must be that of a previously created ExportMetadataOperation, possibly from a different process.

### func (*DataprocMetastoreClient) GetBackup 
    
    
    func (c *DataprocMetastoreClient) GetBackup(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[metastorepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/metastore/latest/apiv1/metastorepb).[GetBackupRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/metastore/latest/apiv1/metastorepb#cloud_google_com_go_metastore_apiv1_metastorepb_GetBackupRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[metastorepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/metastore/latest/apiv1/metastorepb).[Backup](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/metastore/latest/apiv1/metastorepb#cloud_google_com_go_metastore_apiv1_metastorepb_Backup), [error](https://pkg.go.dev/builtin#error))

GetBackup gets details of a single backup.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	metastore "cloud.google.com/go/metastore/apiv1"
    
    	metastorepb "cloud.google.com/go/metastore/apiv1/metastorepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := metastore.NewDataprocMetastoreClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &metastorepb.GetBackupRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/metastore/apiv1/metastorepb#GetBackupRequest.
    	}
    	resp, err := c.GetBackup(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*DataprocMetastoreClient) GetIamPolicy 
    
    
    func (c *DataprocMetastoreClient) GetIamPolicy(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[iampb](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb).[GetIamPolicyRequest](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb#GetIamPolicyRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[iampb](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb).[Policy](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb#Policy), [error](https://pkg.go.dev/builtin#error))

GetIamPolicy gets the access control policy for a resource. Returns an empty policy if the resource exists and does not have a policy set.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	iampb "cloud.google.com/go/iam/apiv1/iampb"
    
    	metastore "cloud.google.com/go/metastore/apiv1"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := metastore.NewDataprocMetastoreClient(ctx)
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
    

### func (*DataprocMetastoreClient) GetLocation 
    
    
    func (c *DataprocMetastoreClient) GetLocation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[locationpb](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location).[GetLocationRequest](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#GetLocationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[locationpb](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location).[Location](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#Location), [error](https://pkg.go.dev/builtin#error))

GetLocation gets information about a location.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	metastore "cloud.google.com/go/metastore/apiv1"
    
    	locationpb "google.golang.org/genproto/googleapis/cloud/location"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := metastore.NewDataprocMetastoreClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &locationpb.GetLocationRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#GetLocationRequest.
    	}
    	resp, err := c.GetLocation(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*DataprocMetastoreClient) GetMetadataImport 
    
    
    func (c *DataprocMetastoreClient) GetMetadataImport(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[metastorepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/metastore/latest/apiv1/metastorepb).[GetMetadataImportRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/metastore/latest/apiv1/metastorepb#cloud_google_com_go_metastore_apiv1_metastorepb_GetMetadataImportRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[metastorepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/metastore/latest/apiv1/metastorepb).[MetadataImport](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/metastore/latest/apiv1/metastorepb#cloud_google_com_go_metastore_apiv1_metastorepb_MetadataImport), [error](https://pkg.go.dev/builtin#error))

GetMetadataImport gets details of a single import.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	metastore "cloud.google.com/go/metastore/apiv1"
    
    	metastorepb "cloud.google.com/go/metastore/apiv1/metastorepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := metastore.NewDataprocMetastoreClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &metastorepb.GetMetadataImportRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/metastore/apiv1/metastorepb#GetMetadataImportRequest.
    	}
    	resp, err := c.GetMetadataImport(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*DataprocMetastoreClient) GetOperation 
    
    
    func (c *DataprocMetastoreClient) GetOperation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[GetOperationRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#GetOperationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[Operation](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#Operation), [error](https://pkg.go.dev/builtin#error))

GetOperation is a utility method from google.longrunning.Operations.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    
    	metastore "cloud.google.com/go/metastore/apiv1"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := metastore.NewDataprocMetastoreClient(ctx)
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
    

### func (*DataprocMetastoreClient) GetService 
    
    
    func (c *DataprocMetastoreClient) GetService(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[metastorepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/metastore/latest/apiv1/metastorepb).[GetServiceRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/metastore/latest/apiv1/metastorepb#cloud_google_com_go_metastore_apiv1_metastorepb_GetServiceRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[metastorepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/metastore/latest/apiv1/metastorepb).[Service](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/metastore/latest/apiv1/metastorepb#cloud_google_com_go_metastore_apiv1_metastorepb_Service), [error](https://pkg.go.dev/builtin#error))

GetService gets the details of a single service.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	metastore "cloud.google.com/go/metastore/apiv1"
    
    	metastorepb "cloud.google.com/go/metastore/apiv1/metastorepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := metastore.NewDataprocMetastoreClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &metastorepb.GetServiceRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/metastore/apiv1/metastorepb#GetServiceRequest.
    	}
    	resp, err := c.GetService(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*DataprocMetastoreClient) ListBackups 
    
    
    func (c *DataprocMetastoreClient) ListBackups(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[metastorepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/metastore/latest/apiv1/metastorepb).[ListBackupsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/metastore/latest/apiv1/metastorepb#cloud_google_com_go_metastore_apiv1_metastorepb_ListBackupsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *BackupIterator

ListBackups lists backups in a service.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	metastore "cloud.google.com/go/metastore/apiv1"
    
    	metastorepb "cloud.google.com/go/metastore/apiv1/metastorepb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := metastore.NewDataprocMetastoreClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &metastorepb.ListBackupsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/metastore/apiv1/metastorepb#ListBackupsRequest.
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
    		_ = it.Response.(*metastorepb.ListBackupsResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	metastore "cloud.google.com/go/metastore/apiv1"
    
    	metastorepb "cloud.google.com/go/metastore/apiv1/metastorepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := metastore.NewDataprocMetastoreClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &metastorepb.ListBackupsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/metastore/apiv1/metastorepb#ListBackupsRequest.
    	}
    	for resp, err := range c.ListBackups(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*DataprocMetastoreClient) ListLocations 
    
    
    func (c *DataprocMetastoreClient) ListLocations(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[locationpb](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location).[ListLocationsRequest](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#ListLocationsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *LocationIterator

ListLocations lists information about the supported locations for this service.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	metastore "cloud.google.com/go/metastore/apiv1"
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
    	c, err := metastore.NewDataprocMetastoreClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &locationpb.ListLocationsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#ListLocationsRequest.
    	}
    	it := c.ListLocations(ctx, req)
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
    
    	metastore "cloud.google.com/go/metastore/apiv1"
    
    	locationpb "google.golang.org/genproto/googleapis/cloud/location"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := metastore.NewDataprocMetastoreClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &locationpb.ListLocationsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#ListLocationsRequest.
    	}
    	for resp, err := range c.ListLocations(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*DataprocMetastoreClient) ListMetadataImports 
    
    
    func (c *DataprocMetastoreClient) ListMetadataImports(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[metastorepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/metastore/latest/apiv1/metastorepb).[ListMetadataImportsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/metastore/latest/apiv1/metastorepb#cloud_google_com_go_metastore_apiv1_metastorepb_ListMetadataImportsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *MetadataImportIterator

ListMetadataImports lists imports in a service.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	metastore "cloud.google.com/go/metastore/apiv1"
    
    	metastorepb "cloud.google.com/go/metastore/apiv1/metastorepb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := metastore.NewDataprocMetastoreClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &metastorepb.ListMetadataImportsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/metastore/apiv1/metastorepb#ListMetadataImportsRequest.
    	}
    	it := c.ListMetadataImports(ctx, req)
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
    		_ = it.Response.(*metastorepb.ListMetadataImportsResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	metastore "cloud.google.com/go/metastore/apiv1"
    
    	metastorepb "cloud.google.com/go/metastore/apiv1/metastorepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := metastore.NewDataprocMetastoreClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &metastorepb.ListMetadataImportsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/metastore/apiv1/metastorepb#ListMetadataImportsRequest.
    	}
    	for resp, err := range c.ListMetadataImports(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*DataprocMetastoreClient) ListOperations 
    
    
    func (c *DataprocMetastoreClient) ListOperations(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[ListOperationsRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#ListOperationsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *OperationIterator

ListOperations is a utility method from google.longrunning.Operations.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    
    	metastore "cloud.google.com/go/metastore/apiv1"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := metastore.NewDataprocMetastoreClient(ctx)
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
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    	metastore "cloud.google.com/go/metastore/apiv1"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := metastore.NewDataprocMetastoreClient(ctx)
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
    

### func (*DataprocMetastoreClient) ListServices 
    
    
    func (c *DataprocMetastoreClient) ListServices(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[metastorepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/metastore/latest/apiv1/metastorepb).[ListServicesRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/metastore/latest/apiv1/metastorepb#cloud_google_com_go_metastore_apiv1_metastorepb_ListServicesRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *ServiceIterator

ListServices lists services in a project and location.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	metastore "cloud.google.com/go/metastore/apiv1"
    
    	metastorepb "cloud.google.com/go/metastore/apiv1/metastorepb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := metastore.NewDataprocMetastoreClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &metastorepb.ListServicesRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/metastore/apiv1/metastorepb#ListServicesRequest.
    	}
    	it := c.ListServices(ctx, req)
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
    		_ = it.Response.(*metastorepb.ListServicesResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	metastore "cloud.google.com/go/metastore/apiv1"
    
    	metastorepb "cloud.google.com/go/metastore/apiv1/metastorepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := metastore.NewDataprocMetastoreClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &metastorepb.ListServicesRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/metastore/apiv1/metastorepb#ListServicesRequest.
    	}
    	for resp, err := range c.ListServices(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*DataprocMetastoreClient) MoveTableToDatabase 
    
    
    func (c *DataprocMetastoreClient) MoveTableToDatabase(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[metastorepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/metastore/latest/apiv1/metastorepb).[MoveTableToDatabaseRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/metastore/latest/apiv1/metastorepb#cloud_google_com_go_metastore_apiv1_metastorepb_MoveTableToDatabaseRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*MoveTableToDatabaseOperation, [error](https://pkg.go.dev/builtin#error))

MoveTableToDatabase move a table to another database.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	metastore "cloud.google.com/go/metastore/apiv1"
    
    	metastorepb "cloud.google.com/go/metastore/apiv1/metastorepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := metastore.NewDataprocMetastoreClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &metastorepb.MoveTableToDatabaseRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/metastore/apiv1/metastorepb#MoveTableToDatabaseRequest.
    	}
    	op, err := c.MoveTableToDatabase(ctx, req)
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
    

### func (*DataprocMetastoreClient) MoveTableToDatabaseOperation 
    
    
    func (c *DataprocMetastoreClient) MoveTableToDatabaseOperation(name [string](https://pkg.go.dev/builtin#string)) *MoveTableToDatabaseOperation

MoveTableToDatabaseOperation returns a new MoveTableToDatabaseOperation from a given name. The name must be that of a previously created MoveTableToDatabaseOperation, possibly from a different process.

### func (*DataprocMetastoreClient) QueryMetadata 
    
    
    func (c *DataprocMetastoreClient) QueryMetadata(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[metastorepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/metastore/latest/apiv1/metastorepb).[QueryMetadataRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/metastore/latest/apiv1/metastorepb#cloud_google_com_go_metastore_apiv1_metastorepb_QueryMetadataRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*QueryMetadataOperation, [error](https://pkg.go.dev/builtin#error))

QueryMetadata query DPMS metadata.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	metastore "cloud.google.com/go/metastore/apiv1"
    
    	metastorepb "cloud.google.com/go/metastore/apiv1/metastorepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := metastore.NewDataprocMetastoreClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &metastorepb.QueryMetadataRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/metastore/apiv1/metastorepb#QueryMetadataRequest.
    	}
    	op, err := c.QueryMetadata(ctx, req)
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
    

### func (*DataprocMetastoreClient) QueryMetadataOperation 
    
    
    func (c *DataprocMetastoreClient) QueryMetadataOperation(name [string](https://pkg.go.dev/builtin#string)) *QueryMetadataOperation

QueryMetadataOperation returns a new QueryMetadataOperation from a given name. The name must be that of a previously created QueryMetadataOperation, possibly from a different process.

### func (*DataprocMetastoreClient) RestoreService 
    
    
    func (c *DataprocMetastoreClient) RestoreService(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[metastorepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/metastore/latest/apiv1/metastorepb).[RestoreServiceRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/metastore/latest/apiv1/metastorepb#cloud_google_com_go_metastore_apiv1_metastorepb_RestoreServiceRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*RestoreServiceOperation, [error](https://pkg.go.dev/builtin#error))

RestoreService restores a service from a backup.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	metastore "cloud.google.com/go/metastore/apiv1"
    
    	metastorepb "cloud.google.com/go/metastore/apiv1/metastorepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := metastore.NewDataprocMetastoreClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &metastorepb.RestoreServiceRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/metastore/apiv1/metastorepb#RestoreServiceRequest.
    	}
    	op, err := c.RestoreService(ctx, req)
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
    

### func (*DataprocMetastoreClient) RestoreServiceOperation 
    
    
    func (c *DataprocMetastoreClient) RestoreServiceOperation(name [string](https://pkg.go.dev/builtin#string)) *RestoreServiceOperation

RestoreServiceOperation returns a new RestoreServiceOperation from a given name. The name must be that of a previously created RestoreServiceOperation, possibly from a different process.

### func (*DataprocMetastoreClient) SetIamPolicy 
    
    
    func (c *DataprocMetastoreClient) SetIamPolicy(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[iampb](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb).[SetIamPolicyRequest](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb#SetIamPolicyRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[iampb](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb).[Policy](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb#Policy), [error](https://pkg.go.dev/builtin#error))

SetIamPolicy sets the access control policy on the specified resource. Replaces any existing policy.

Can return NOT_FOUND, INVALID_ARGUMENT, and PERMISSION_DENIED errors.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	iampb "cloud.google.com/go/iam/apiv1/iampb"
    
    	metastore "cloud.google.com/go/metastore/apiv1"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := metastore.NewDataprocMetastoreClient(ctx)
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
    

### func (*DataprocMetastoreClient) TestIamPermissions 
    
    
    func (c *DataprocMetastoreClient) TestIamPermissions(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[iampb](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb).[TestIamPermissionsRequest](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb#TestIamPermissionsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[iampb](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb).[TestIamPermissionsResponse](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb#TestIamPermissionsResponse), [error](https://pkg.go.dev/builtin#error))

TestIamPermissions returns permissions that a caller has on the specified resource. If the resource does not exist, this will return an empty set of permissions, not a NOT_FOUND error.

Note: This operation is designed to be used for building permission-aware UIs and command-line tools, not for authorization checking. This operation may “fail open” without warning.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	iampb "cloud.google.com/go/iam/apiv1/iampb"
    
    	metastore "cloud.google.com/go/metastore/apiv1"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := metastore.NewDataprocMetastoreClient(ctx)
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
    

### func (*DataprocMetastoreClient) UpdateMetadataImport 
    
    
    func (c *DataprocMetastoreClient) UpdateMetadataImport(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[metastorepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/metastore/latest/apiv1/metastorepb).[UpdateMetadataImportRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/metastore/latest/apiv1/metastorepb#cloud_google_com_go_metastore_apiv1_metastorepb_UpdateMetadataImportRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*UpdateMetadataImportOperation, [error](https://pkg.go.dev/builtin#error))

UpdateMetadataImport updates a single import. Only the description field of MetadataImport is supported to be updated.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	metastore "cloud.google.com/go/metastore/apiv1"
    
    	metastorepb "cloud.google.com/go/metastore/apiv1/metastorepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := metastore.NewDataprocMetastoreClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &metastorepb.UpdateMetadataImportRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/metastore/apiv1/metastorepb#UpdateMetadataImportRequest.
    	}
    	op, err := c.UpdateMetadataImport(ctx, req)
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
    

### func (*DataprocMetastoreClient) UpdateMetadataImportOperation 
    
    
    func (c *DataprocMetastoreClient) UpdateMetadataImportOperation(name [string](https://pkg.go.dev/builtin#string)) *UpdateMetadataImportOperation

UpdateMetadataImportOperation returns a new UpdateMetadataImportOperation from a given name. The name must be that of a previously created UpdateMetadataImportOperation, possibly from a different process.

### func (*DataprocMetastoreClient) UpdateService 
    
    
    func (c *DataprocMetastoreClient) UpdateService(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[metastorepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/metastore/latest/apiv1/metastorepb).[UpdateServiceRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/metastore/latest/apiv1/metastorepb#cloud_google_com_go_metastore_apiv1_metastorepb_UpdateServiceRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*UpdateServiceOperation, [error](https://pkg.go.dev/builtin#error))

UpdateService updates the parameters of a single service.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	metastore "cloud.google.com/go/metastore/apiv1"
    
    	metastorepb "cloud.google.com/go/metastore/apiv1/metastorepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := metastore.NewDataprocMetastoreClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &metastorepb.UpdateServiceRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/metastore/apiv1/metastorepb#UpdateServiceRequest.
    	}
    	op, err := c.UpdateService(ctx, req)
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
    

### func (*DataprocMetastoreClient) UpdateServiceOperation 
    
    
    func (c *DataprocMetastoreClient) UpdateServiceOperation(name [string](https://pkg.go.dev/builtin#string)) *UpdateServiceOperation

UpdateServiceOperation returns a new UpdateServiceOperation from a given name. The name must be that of a previously created UpdateServiceOperation, possibly from a different process.

## DataprocMetastoreFederationCallOptions
    
    
    type DataprocMetastoreFederationCallOptions struct {
    	ListFederations    []gax.CallOption
    	GetFederation      []gax.CallOption
    	CreateFederation   []gax.CallOption
    	UpdateFederation   []gax.CallOption
    	DeleteFederation   []gax.CallOption
    	GetLocation        []gax.CallOption
    	ListLocations      []gax.CallOption
    	GetIamPolicy       []gax.CallOption
    	SetIamPolicy       []gax.CallOption
    	TestIamPermissions []gax.CallOption
    	CancelOperation    []gax.CallOption
    	DeleteOperation    []gax.CallOption
    	GetOperation       []gax.CallOption
    	ListOperations     []gax.CallOption
    }

DataprocMetastoreFederationCallOptions contains the retry settings for each method of DataprocMetastoreFederationClient.

## DataprocMetastoreFederationClient
    
    
    type DataprocMetastoreFederationClient struct {
    
    	// The call options for this service.
    	CallOptions *DataprocMetastoreFederationCallOptions
    
    	// LROClient is used internally to handle long-running operations.
    	// It is exposed so that its CallOptions can be modified if required.
    	// Users should not Close this client.
    	LROClient *lroauto.OperationsClient
    	// contains filtered or unexported fields
    }

DataprocMetastoreFederationClient is a client for interacting with Dataproc Metastore API. Methods, except Close, may be called concurrently. However, fields must not be modified concurrently with method calls.

Configures and manages metastore federation services. Dataproc Metastore Federation Service allows federating a collection of backend metastores like BigQuery, Dataplex Lakes, and other Dataproc Metastores. The Federation Service exposes a gRPC URL through which metadata from the backend metastores are served at query time.

The Dataproc Metastore Federation API defines the following resource model:
    
    
    The service works with a collection of Google Cloud projects.
    
    Each project has a collection of available locations.
    
    Each location has a collection of federations.
    
    Dataproc Metastore Federations are resources with names of the
    form:
    projects/{project_number}/locations/{location_id}/federations/{federation_id}.
    

### func NewDataprocMetastoreFederationClient 
    
    
    func NewDataprocMetastoreFederationClient(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...option.ClientOption) (*DataprocMetastoreFederationClient, [error](https://pkg.go.dev/builtin#error))

NewDataprocMetastoreFederationClient creates a new dataproc metastore federation client based on gRPC. The returned client must be Closed when it is done being used to clean up its underlying connections.

Configures and manages metastore federation services. Dataproc Metastore Federation Service allows federating a collection of backend metastores like BigQuery, Dataplex Lakes, and other Dataproc Metastores. The Federation Service exposes a gRPC URL through which metadata from the backend metastores are served at query time.

The Dataproc Metastore Federation API defines the following resource model:
    
    
    The service works with a collection of Google Cloud projects.
    
    Each project has a collection of available locations.
    
    Each location has a collection of federations.
    
    Dataproc Metastore Federations are resources with names of the
    form:
    projects/{project_number}/locations/{location_id}/federations/{federation_id}.
    

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	metastore "cloud.google.com/go/metastore/apiv1"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := metastore.NewDataprocMetastoreFederationClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	// TODO: Use client.
    	_ = c
    }
    

### func NewDataprocMetastoreFederationRESTClient 
    
    
    func NewDataprocMetastoreFederationRESTClient(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...option.ClientOption) (*DataprocMetastoreFederationClient, [error](https://pkg.go.dev/builtin#error))

NewDataprocMetastoreFederationRESTClient creates a new dataproc metastore federation rest client.

Configures and manages metastore federation services. Dataproc Metastore Federation Service allows federating a collection of backend metastores like BigQuery, Dataplex Lakes, and other Dataproc Metastores. The Federation Service exposes a gRPC URL through which metadata from the backend metastores are served at query time.

The Dataproc Metastore Federation API defines the following resource model:
    
    
    The service works with a collection of Google Cloud projects.
    
    Each project has a collection of available locations.
    
    Each location has a collection of federations.
    
    Dataproc Metastore Federations are resources with names of the
    form:
    projects/{project_number}/locations/{location_id}/federations/{federation_id}.
    

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	metastore "cloud.google.com/go/metastore/apiv1"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := metastore.[NewDataprocMetastoreFederationRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/metastore/latest/apiv1.html#cloud_google_com_go_metastore_apiv1_DataprocMetastoreFederationClient_NewDataprocMetastoreFederationRESTClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	// TODO: Use client.
    	_ = c
    }
    

### func (*DataprocMetastoreFederationClient) CancelOperation 
    
    
    func (c *DataprocMetastoreFederationClient) CancelOperation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[CancelOperationRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#CancelOperationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

CancelOperation is a utility method from google.longrunning.Operations.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    
    	metastore "cloud.google.com/go/metastore/apiv1"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := metastore.NewDataprocMetastoreFederationClient(ctx)
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
    

### func (*DataprocMetastoreFederationClient) Close 
    
    
    func (c *DataprocMetastoreFederationClient) Close() [error](https://pkg.go.dev/builtin#error)

Close closes the connection to the API service. **Always** call Close() when the client is no longer required.

### func (*DataprocMetastoreFederationClient) Connection (deprecated)
    
    
    func (c *DataprocMetastoreFederationClient) Connection() *grpc.ClientConn

Connection returns a connection to the API service.

Deprecated: Connections are now pooled so this method does not always return the same resource.

### func (*DataprocMetastoreFederationClient) CreateFederation 
    
    
    func (c *DataprocMetastoreFederationClient) CreateFederation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[metastorepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/metastore/latest/apiv1/metastorepb).[CreateFederationRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/metastore/latest/apiv1/metastorepb#cloud_google_com_go_metastore_apiv1_metastorepb_CreateFederationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*CreateFederationOperation, [error](https://pkg.go.dev/builtin#error))

CreateFederation creates a metastore federation in a project and location.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	metastore "cloud.google.com/go/metastore/apiv1"
    
    	metastorepb "cloud.google.com/go/metastore/apiv1/metastorepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := metastore.NewDataprocMetastoreFederationClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &metastorepb.CreateFederationRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/metastore/apiv1/metastorepb#CreateFederationRequest.
    	}
    	op, err := c.CreateFederation(ctx, req)
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
    

### func (*DataprocMetastoreFederationClient) CreateFederationOperation 
    
    
    func (c *DataprocMetastoreFederationClient) CreateFederationOperation(name [string](https://pkg.go.dev/builtin#string)) *CreateFederationOperation

CreateFederationOperation returns a new CreateFederationOperation from a given name. The name must be that of a previously created CreateFederationOperation, possibly from a different process.

### func (*DataprocMetastoreFederationClient) DeleteFederation 
    
    
    func (c *DataprocMetastoreFederationClient) DeleteFederation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[metastorepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/metastore/latest/apiv1/metastorepb).[DeleteFederationRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/metastore/latest/apiv1/metastorepb#cloud_google_com_go_metastore_apiv1_metastorepb_DeleteFederationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*DeleteFederationOperation, [error](https://pkg.go.dev/builtin#error))

DeleteFederation deletes a single federation.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	metastore "cloud.google.com/go/metastore/apiv1"
    
    	metastorepb "cloud.google.com/go/metastore/apiv1/metastorepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := metastore.NewDataprocMetastoreFederationClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &metastorepb.DeleteFederationRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/metastore/apiv1/metastorepb#DeleteFederationRequest.
    	}
    	op, err := c.DeleteFederation(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    
    	err = op.Wait(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    }
    

### func (*DataprocMetastoreFederationClient) DeleteFederationOperation 
    
    
    func (c *DataprocMetastoreFederationClient) DeleteFederationOperation(name [string](https://pkg.go.dev/builtin#string)) *DeleteFederationOperation

DeleteFederationOperation returns a new DeleteFederationOperation from a given name. The name must be that of a previously created DeleteFederationOperation, possibly from a different process.

### func (*DataprocMetastoreFederationClient) DeleteOperation 
    
    
    func (c *DataprocMetastoreFederationClient) DeleteOperation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[DeleteOperationRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#DeleteOperationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

DeleteOperation is a utility method from google.longrunning.Operations.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    
    	metastore "cloud.google.com/go/metastore/apiv1"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := metastore.NewDataprocMetastoreFederationClient(ctx)
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
    

### func (*DataprocMetastoreFederationClient) GetFederation 
    
    
    func (c *DataprocMetastoreFederationClient) GetFederation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[metastorepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/metastore/latest/apiv1/metastorepb).[GetFederationRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/metastore/latest/apiv1/metastorepb#cloud_google_com_go_metastore_apiv1_metastorepb_GetFederationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[metastorepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/metastore/latest/apiv1/metastorepb).[Federation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/metastore/latest/apiv1/metastorepb#cloud_google_com_go_metastore_apiv1_metastorepb_Federation), [error](https://pkg.go.dev/builtin#error))

GetFederation gets the details of a single federation.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	metastore "cloud.google.com/go/metastore/apiv1"
    
    	metastorepb "cloud.google.com/go/metastore/apiv1/metastorepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := metastore.NewDataprocMetastoreFederationClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &metastorepb.GetFederationRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/metastore/apiv1/metastorepb#GetFederationRequest.
    	}
    	resp, err := c.GetFederation(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*DataprocMetastoreFederationClient) GetIamPolicy 
    
    
    func (c *DataprocMetastoreFederationClient) GetIamPolicy(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[iampb](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb).[GetIamPolicyRequest](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb#GetIamPolicyRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[iampb](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb).[Policy](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb#Policy), [error](https://pkg.go.dev/builtin#error))

GetIamPolicy gets the access control policy for a resource. Returns an empty policy if the resource exists and does not have a policy set.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	iampb "cloud.google.com/go/iam/apiv1/iampb"
    
    	metastore "cloud.google.com/go/metastore/apiv1"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := metastore.NewDataprocMetastoreFederationClient(ctx)
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
    

### func (*DataprocMetastoreFederationClient) GetLocation 
    
    
    func (c *DataprocMetastoreFederationClient) GetLocation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[locationpb](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location).[GetLocationRequest](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#GetLocationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[locationpb](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location).[Location](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#Location), [error](https://pkg.go.dev/builtin#error))

GetLocation gets information about a location.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	metastore "cloud.google.com/go/metastore/apiv1"
    
    	locationpb "google.golang.org/genproto/googleapis/cloud/location"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := metastore.NewDataprocMetastoreFederationClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &locationpb.GetLocationRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#GetLocationRequest.
    	}
    	resp, err := c.GetLocation(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*DataprocMetastoreFederationClient) GetOperation 
    
    
    func (c *DataprocMetastoreFederationClient) GetOperation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[GetOperationRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#GetOperationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[Operation](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#Operation), [error](https://pkg.go.dev/builtin#error))

GetOperation is a utility method from google.longrunning.Operations.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    
    	metastore "cloud.google.com/go/metastore/apiv1"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := metastore.NewDataprocMetastoreFederationClient(ctx)
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
    

### func (*DataprocMetastoreFederationClient) ListFederations 
    
    
    func (c *DataprocMetastoreFederationClient) ListFederations(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[metastorepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/metastore/latest/apiv1/metastorepb).[ListFederationsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/metastore/latest/apiv1/metastorepb#cloud_google_com_go_metastore_apiv1_metastorepb_ListFederationsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *FederationIterator

ListFederations lists federations in a project and location.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	metastore "cloud.google.com/go/metastore/apiv1"
    
    	metastorepb "cloud.google.com/go/metastore/apiv1/metastorepb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := metastore.NewDataprocMetastoreFederationClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &metastorepb.ListFederationsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/metastore/apiv1/metastorepb#ListFederationsRequest.
    	}
    	it := c.ListFederations(ctx, req)
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
    		_ = it.Response.(*metastorepb.ListFederationsResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	metastore "cloud.google.com/go/metastore/apiv1"
    
    	metastorepb "cloud.google.com/go/metastore/apiv1/metastorepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := metastore.NewDataprocMetastoreFederationClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &metastorepb.ListFederationsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/metastore/apiv1/metastorepb#ListFederationsRequest.
    	}
    	for resp, err := range c.ListFederations(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*DataprocMetastoreFederationClient) ListLocations 
    
    
    func (c *DataprocMetastoreFederationClient) ListLocations(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[locationpb](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location).[ListLocationsRequest](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#ListLocationsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *LocationIterator

ListLocations lists information about the supported locations for this service.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	metastore "cloud.google.com/go/metastore/apiv1"
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
    	c, err := metastore.NewDataprocMetastoreFederationClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &locationpb.ListLocationsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#ListLocationsRequest.
    	}
    	it := c.ListLocations(ctx, req)
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
    
    	metastore "cloud.google.com/go/metastore/apiv1"
    
    	locationpb "google.golang.org/genproto/googleapis/cloud/location"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := metastore.NewDataprocMetastoreFederationClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &locationpb.ListLocationsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#ListLocationsRequest.
    	}
    	for resp, err := range c.ListLocations(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*DataprocMetastoreFederationClient) ListOperations 
    
    
    func (c *DataprocMetastoreFederationClient) ListOperations(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[ListOperationsRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#ListOperationsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *OperationIterator

ListOperations is a utility method from google.longrunning.Operations.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    
    	metastore "cloud.google.com/go/metastore/apiv1"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := metastore.NewDataprocMetastoreFederationClient(ctx)
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
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    	metastore "cloud.google.com/go/metastore/apiv1"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := metastore.NewDataprocMetastoreFederationClient(ctx)
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
    

### func (*DataprocMetastoreFederationClient) SetIamPolicy 
    
    
    func (c *DataprocMetastoreFederationClient) SetIamPolicy(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[iampb](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb).[SetIamPolicyRequest](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb#SetIamPolicyRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[iampb](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb).[Policy](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb#Policy), [error](https://pkg.go.dev/builtin#error))

SetIamPolicy sets the access control policy on the specified resource. Replaces any existing policy.

Can return NOT_FOUND, INVALID_ARGUMENT, and PERMISSION_DENIED errors.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	iampb "cloud.google.com/go/iam/apiv1/iampb"
    
    	metastore "cloud.google.com/go/metastore/apiv1"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := metastore.NewDataprocMetastoreFederationClient(ctx)
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
    

### func (*DataprocMetastoreFederationClient) TestIamPermissions 
    
    
    func (c *DataprocMetastoreFederationClient) TestIamPermissions(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[iampb](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb).[TestIamPermissionsRequest](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb#TestIamPermissionsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[iampb](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb).[TestIamPermissionsResponse](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb#TestIamPermissionsResponse), [error](https://pkg.go.dev/builtin#error))

TestIamPermissions returns permissions that a caller has on the specified resource. If the resource does not exist, this will return an empty set of permissions, not a NOT_FOUND error.

Note: This operation is designed to be used for building permission-aware UIs and command-line tools, not for authorization checking. This operation may “fail open” without warning.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	iampb "cloud.google.com/go/iam/apiv1/iampb"
    
    	metastore "cloud.google.com/go/metastore/apiv1"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := metastore.NewDataprocMetastoreFederationClient(ctx)
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
    

### func (*DataprocMetastoreFederationClient) UpdateFederation 
    
    
    func (c *DataprocMetastoreFederationClient) UpdateFederation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[metastorepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/metastore/latest/apiv1/metastorepb).[UpdateFederationRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/metastore/latest/apiv1/metastorepb#cloud_google_com_go_metastore_apiv1_metastorepb_UpdateFederationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*UpdateFederationOperation, [error](https://pkg.go.dev/builtin#error))

UpdateFederation updates the fields of a federation.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	metastore "cloud.google.com/go/metastore/apiv1"
    
    	metastorepb "cloud.google.com/go/metastore/apiv1/metastorepb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := metastore.NewDataprocMetastoreFederationClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &metastorepb.UpdateFederationRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/metastore/apiv1/metastorepb#UpdateFederationRequest.
    	}
    	op, err := c.UpdateFederation(ctx, req)
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
    

### func (*DataprocMetastoreFederationClient) UpdateFederationOperation 
    
    
    func (c *DataprocMetastoreFederationClient) UpdateFederationOperation(name [string](https://pkg.go.dev/builtin#string)) *UpdateFederationOperation

UpdateFederationOperation returns a new UpdateFederationOperation from a given name. The name must be that of a previously created UpdateFederationOperation, possibly from a different process.

## DeleteBackupOperation
    
    
    type DeleteBackupOperation struct {
    	// contains filtered or unexported fields
    }

DeleteBackupOperation manages a long-running operation from DeleteBackup.

### func (*DeleteBackupOperation) Done 
    
    
    func (op *DeleteBackupOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*DeleteBackupOperation) Metadata 
    
    
    func (op *DeleteBackupOperation) Metadata() (*[metastorepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/metastore/latest/apiv1/metastorepb).[OperationMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/metastore/latest/apiv1/metastorepb#cloud_google_com_go_metastore_apiv1_metastorepb_OperationMetadata), [error](https://pkg.go.dev/builtin#error))

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

## DeleteFederationOperation
    
    
    type DeleteFederationOperation struct {
    	// contains filtered or unexported fields
    }

DeleteFederationOperation manages a long-running operation from DeleteFederation.

### func (*DeleteFederationOperation) Done 
    
    
    func (op *DeleteFederationOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*DeleteFederationOperation) Metadata 
    
    
    func (op *DeleteFederationOperation) Metadata() (*[metastorepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/metastore/latest/apiv1/metastorepb).[OperationMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/metastore/latest/apiv1/metastorepb#cloud_google_com_go_metastore_apiv1_metastorepb_OperationMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*DeleteFederationOperation) Name 
    
    
    func (op *DeleteFederationOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*DeleteFederationOperation) Poll 
    
    
    func (op *DeleteFederationOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*DeleteFederationOperation) Wait 
    
    
    func (op *DeleteFederationOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## DeleteServiceOperation
    
    
    type DeleteServiceOperation struct {
    	// contains filtered or unexported fields
    }

DeleteServiceOperation manages a long-running operation from DeleteService.

### func (*DeleteServiceOperation) Done 
    
    
    func (op *DeleteServiceOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*DeleteServiceOperation) Metadata 
    
    
    func (op *DeleteServiceOperation) Metadata() (*[metastorepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/metastore/latest/apiv1/metastorepb).[OperationMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/metastore/latest/apiv1/metastorepb#cloud_google_com_go_metastore_apiv1_metastorepb_OperationMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*DeleteServiceOperation) Name 
    
    
    func (op *DeleteServiceOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*DeleteServiceOperation) Poll 
    
    
    func (op *DeleteServiceOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*DeleteServiceOperation) Wait 
    
    
    func (op *DeleteServiceOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## ExportMetadataOperation
    
    
    type ExportMetadataOperation struct {
    	// contains filtered or unexported fields
    }

ExportMetadataOperation manages a long-running operation from ExportMetadata.

### func (*ExportMetadataOperation) Done 
    
    
    func (op *ExportMetadataOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*ExportMetadataOperation) Metadata 
    
    
    func (op *ExportMetadataOperation) Metadata() (*[metastorepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/metastore/latest/apiv1/metastorepb).[OperationMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/metastore/latest/apiv1/metastorepb#cloud_google_com_go_metastore_apiv1_metastorepb_OperationMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*ExportMetadataOperation) Name 
    
    
    func (op *ExportMetadataOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*ExportMetadataOperation) Poll 
    
    
    func (op *ExportMetadataOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[metastorepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/metastore/latest/apiv1/metastorepb).[MetadataExport](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/metastore/latest/apiv1/metastorepb#cloud_google_com_go_metastore_apiv1_metastorepb_MetadataExport), [error](https://pkg.go.dev/builtin#error))

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*ExportMetadataOperation) Wait 
    
    
    func (op *ExportMetadataOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[metastorepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/metastore/latest/apiv1/metastorepb).[MetadataExport](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/metastore/latest/apiv1/metastorepb#cloud_google_com_go_metastore_apiv1_metastorepb_MetadataExport), [error](https://pkg.go.dev/builtin#error))

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## FederationIterator
    
    
    type FederationIterator struct {
    
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
    	InternalFetch func(pageSize [int](https://pkg.go.dev/builtin#int), pageToken [string](https://pkg.go.dev/builtin#string)) (results []*metastorepb.Federation, nextPageToken [string](https://pkg.go.dev/builtin#string), err [error](https://pkg.go.dev/builtin#error))
    	// contains filtered or unexported fields
    }

FederationIterator manages a stream of *metastorepb.Federation.

### func (*FederationIterator) All 
    
    
    func (it *FederationIterator) All() iter.Seq2[*metastorepb.Federation, error]

All returns an iterator. If an error is returned by the iterator, the iterator will stop after that iteration.

### func (*FederationIterator) Next 
    
    
    func (it *FederationIterator) Next() (*[metastorepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/metastore/latest/apiv1/metastorepb).[Federation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/metastore/latest/apiv1/metastorepb#cloud_google_com_go_metastore_apiv1_metastorepb_Federation), [error](https://pkg.go.dev/builtin#error))

Next returns the next result. Its second return value is iterator.Done if there are no more results. Once Next returns Done, all subsequent calls will return Done.

### func (*FederationIterator) PageInfo 
    
    
    func (it *FederationIterator) PageInfo() *iterator.PageInfo

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

## MetadataImportIterator
    
    
    type MetadataImportIterator struct {
    
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
    	InternalFetch func(pageSize [int](https://pkg.go.dev/builtin#int), pageToken [string](https://pkg.go.dev/builtin#string)) (results []*metastorepb.MetadataImport, nextPageToken [string](https://pkg.go.dev/builtin#string), err [error](https://pkg.go.dev/builtin#error))
    	// contains filtered or unexported fields
    }

MetadataImportIterator manages a stream of *metastorepb.MetadataImport.

### func (*MetadataImportIterator) All 
    
    
    func (it *MetadataImportIterator) All() iter.Seq2[*metastorepb.MetadataImport, error]

All returns an iterator. If an error is returned by the iterator, the iterator will stop after that iteration.

### func (*MetadataImportIterator) Next 
    
    
    func (it *MetadataImportIterator) Next() (*[metastorepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/metastore/latest/apiv1/metastorepb).[MetadataImport](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/metastore/latest/apiv1/metastorepb#cloud_google_com_go_metastore_apiv1_metastorepb_MetadataImport), [error](https://pkg.go.dev/builtin#error))

Next returns the next result. Its second return value is iterator.Done if there are no more results. Once Next returns Done, all subsequent calls will return Done.

### func (*MetadataImportIterator) PageInfo 
    
    
    func (it *MetadataImportIterator) PageInfo() *iterator.PageInfo

PageInfo supports pagination. See the [google.golang.org/api/iterator] package for details.

## MoveTableToDatabaseOperation
    
    
    type MoveTableToDatabaseOperation struct {
    	// contains filtered or unexported fields
    }

MoveTableToDatabaseOperation manages a long-running operation from MoveTableToDatabase.

### func (*MoveTableToDatabaseOperation) Done 
    
    
    func (op *MoveTableToDatabaseOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*MoveTableToDatabaseOperation) Metadata 
    
    
    func (op *MoveTableToDatabaseOperation) Metadata() (*[metastorepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/metastore/latest/apiv1/metastorepb).[OperationMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/metastore/latest/apiv1/metastorepb#cloud_google_com_go_metastore_apiv1_metastorepb_OperationMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*MoveTableToDatabaseOperation) Name 
    
    
    func (op *MoveTableToDatabaseOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*MoveTableToDatabaseOperation) Poll 
    
    
    func (op *MoveTableToDatabaseOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[metastorepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/metastore/latest/apiv1/metastorepb).[MoveTableToDatabaseResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/metastore/latest/apiv1/metastorepb#cloud_google_com_go_metastore_apiv1_metastorepb_MoveTableToDatabaseResponse), [error](https://pkg.go.dev/builtin#error))

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*MoveTableToDatabaseOperation) Wait 
    
    
    func (op *MoveTableToDatabaseOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[metastorepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/metastore/latest/apiv1/metastorepb).[MoveTableToDatabaseResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/metastore/latest/apiv1/metastorepb#cloud_google_com_go_metastore_apiv1_metastorepb_MoveTableToDatabaseResponse), [error](https://pkg.go.dev/builtin#error))

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

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

## QueryMetadataOperation
    
    
    type QueryMetadataOperation struct {
    	// contains filtered or unexported fields
    }

QueryMetadataOperation manages a long-running operation from QueryMetadata.

### func (*QueryMetadataOperation) Done 
    
    
    func (op *QueryMetadataOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*QueryMetadataOperation) Metadata 
    
    
    func (op *QueryMetadataOperation) Metadata() (*[metastorepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/metastore/latest/apiv1/metastorepb).[OperationMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/metastore/latest/apiv1/metastorepb#cloud_google_com_go_metastore_apiv1_metastorepb_OperationMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*QueryMetadataOperation) Name 
    
    
    func (op *QueryMetadataOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*QueryMetadataOperation) Poll 
    
    
    func (op *QueryMetadataOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[metastorepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/metastore/latest/apiv1/metastorepb).[QueryMetadataResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/metastore/latest/apiv1/metastorepb#cloud_google_com_go_metastore_apiv1_metastorepb_QueryMetadataResponse), [error](https://pkg.go.dev/builtin#error))

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*QueryMetadataOperation) Wait 
    
    
    func (op *QueryMetadataOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[metastorepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/metastore/latest/apiv1/metastorepb).[QueryMetadataResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/metastore/latest/apiv1/metastorepb#cloud_google_com_go_metastore_apiv1_metastorepb_QueryMetadataResponse), [error](https://pkg.go.dev/builtin#error))

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## RestoreServiceOperation
    
    
    type RestoreServiceOperation struct {
    	// contains filtered or unexported fields
    }

RestoreServiceOperation manages a long-running operation from RestoreService.

### func (*RestoreServiceOperation) Done 
    
    
    func (op *RestoreServiceOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*RestoreServiceOperation) Metadata 
    
    
    func (op *RestoreServiceOperation) Metadata() (*[metastorepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/metastore/latest/apiv1/metastorepb).[OperationMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/metastore/latest/apiv1/metastorepb#cloud_google_com_go_metastore_apiv1_metastorepb_OperationMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*RestoreServiceOperation) Name 
    
    
    func (op *RestoreServiceOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*RestoreServiceOperation) Poll 
    
    
    func (op *RestoreServiceOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[metastorepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/metastore/latest/apiv1/metastorepb).[Restore](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/metastore/latest/apiv1/metastorepb#cloud_google_com_go_metastore_apiv1_metastorepb_Restore), [error](https://pkg.go.dev/builtin#error))

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*RestoreServiceOperation) Wait 
    
    
    func (op *RestoreServiceOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[metastorepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/metastore/latest/apiv1/metastorepb).[Restore](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/metastore/latest/apiv1/metastorepb#cloud_google_com_go_metastore_apiv1_metastorepb_Restore), [error](https://pkg.go.dev/builtin#error))

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## ServiceIterator
    
    
    type ServiceIterator struct {
    
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
    	InternalFetch func(pageSize [int](https://pkg.go.dev/builtin#int), pageToken [string](https://pkg.go.dev/builtin#string)) (results []*metastorepb.Service, nextPageToken [string](https://pkg.go.dev/builtin#string), err [error](https://pkg.go.dev/builtin#error))
    	// contains filtered or unexported fields
    }

ServiceIterator manages a stream of *metastorepb.Service.

### func (*ServiceIterator) All 
    
    
    func (it *ServiceIterator) All() iter.Seq2[*metastorepb.Service, error]

All returns an iterator. If an error is returned by the iterator, the iterator will stop after that iteration.

### func (*ServiceIterator) Next 
    
    
    func (it *ServiceIterator) Next() (*[metastorepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/metastore/latest/apiv1/metastorepb).[Service](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/metastore/latest/apiv1/metastorepb#cloud_google_com_go_metastore_apiv1_metastorepb_Service), [error](https://pkg.go.dev/builtin#error))

Next returns the next result. Its second return value is iterator.Done if there are no more results. Once Next returns Done, all subsequent calls will return Done.

### func (*ServiceIterator) PageInfo 
    
    
    func (it *ServiceIterator) PageInfo() *iterator.PageInfo

PageInfo supports pagination. See the [google.golang.org/api/iterator] package for details.

## UpdateFederationOperation
    
    
    type UpdateFederationOperation struct {
    	// contains filtered or unexported fields
    }

UpdateFederationOperation manages a long-running operation from UpdateFederation.

### func (*UpdateFederationOperation) Done 
    
    
    func (op *UpdateFederationOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*UpdateFederationOperation) Metadata 
    
    
    func (op *UpdateFederationOperation) Metadata() (*[metastorepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/metastore/latest/apiv1/metastorepb).[OperationMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/metastore/latest/apiv1/metastorepb#cloud_google_com_go_metastore_apiv1_metastorepb_OperationMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*UpdateFederationOperation) Name 
    
    
    func (op *UpdateFederationOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*UpdateFederationOperation) Poll 
    
    
    func (op *UpdateFederationOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[metastorepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/metastore/latest/apiv1/metastorepb).[Federation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/metastore/latest/apiv1/metastorepb#cloud_google_com_go_metastore_apiv1_metastorepb_Federation), [error](https://pkg.go.dev/builtin#error))

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*UpdateFederationOperation) Wait 
    
    
    func (op *UpdateFederationOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[metastorepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/metastore/latest/apiv1/metastorepb).[Federation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/metastore/latest/apiv1/metastorepb#cloud_google_com_go_metastore_apiv1_metastorepb_Federation), [error](https://pkg.go.dev/builtin#error))

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## UpdateMetadataImportOperation
    
    
    type UpdateMetadataImportOperation struct {
    	// contains filtered or unexported fields
    }

UpdateMetadataImportOperation manages a long-running operation from UpdateMetadataImport.

### func (*UpdateMetadataImportOperation) Done 
    
    
    func (op *UpdateMetadataImportOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*UpdateMetadataImportOperation) Metadata 
    
    
    func (op *UpdateMetadataImportOperation) Metadata() (*[metastorepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/metastore/latest/apiv1/metastorepb).[OperationMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/metastore/latest/apiv1/metastorepb#cloud_google_com_go_metastore_apiv1_metastorepb_OperationMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*UpdateMetadataImportOperation) Name 
    
    
    func (op *UpdateMetadataImportOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*UpdateMetadataImportOperation) Poll 
    
    
    func (op *UpdateMetadataImportOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[metastorepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/metastore/latest/apiv1/metastorepb).[MetadataImport](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/metastore/latest/apiv1/metastorepb#cloud_google_com_go_metastore_apiv1_metastorepb_MetadataImport), [error](https://pkg.go.dev/builtin#error))

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*UpdateMetadataImportOperation) Wait 
    
    
    func (op *UpdateMetadataImportOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[metastorepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/metastore/latest/apiv1/metastorepb).[MetadataImport](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/metastore/latest/apiv1/metastorepb#cloud_google_com_go_metastore_apiv1_metastorepb_MetadataImport), [error](https://pkg.go.dev/builtin#error))

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## UpdateServiceOperation
    
    
    type UpdateServiceOperation struct {
    	// contains filtered or unexported fields
    }

UpdateServiceOperation manages a long-running operation from UpdateService.

### func (*UpdateServiceOperation) Done 
    
    
    func (op *UpdateServiceOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*UpdateServiceOperation) Metadata 
    
    
    func (op *UpdateServiceOperation) Metadata() (*[metastorepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/metastore/latest/apiv1/metastorepb).[OperationMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/metastore/latest/apiv1/metastorepb#cloud_google_com_go_metastore_apiv1_metastorepb_OperationMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*UpdateServiceOperation) Name 
    
    
    func (op *UpdateServiceOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*UpdateServiceOperation) Poll 
    
    
    func (op *UpdateServiceOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[metastorepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/metastore/latest/apiv1/metastorepb).[Service](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/metastore/latest/apiv1/metastorepb#cloud_google_com_go_metastore_apiv1_metastorepb_Service), [error](https://pkg.go.dev/builtin#error))

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*UpdateServiceOperation) Wait 
    
    
    func (op *UpdateServiceOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[metastorepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/metastore/latest/apiv1/metastorepb).[Service](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/metastore/latest/apiv1/metastorepb#cloud_google_com_go_metastore_apiv1_metastorepb_Service), [error](https://pkg.go.dev/builtin#error))

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
