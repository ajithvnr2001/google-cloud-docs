---
url: https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/
title: Cloud Resource Manager API v3 - Package cloud.google.com/go/resourcemanager/apiv3 (v1.17.0) \u00a0|\u00a0 Go client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:12:56.015237+00:00
---

# Cloud Resource Manager API v3 - Package cloud.google.com/go/resourcemanager/apiv3 (v1.17.0)  |  Go client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Go ](https://docs.cloud.google.com/go/docs)
  * [ Client libraries ](https://docs.cloud.google.com/go/docs/reference)



Send feedback 

#  Cloud Resource Manager API v3 - Package cloud.google.com/go/resourcemanager/apiv3 (v1.17.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.17.0 (latest)  1.16.0  1.15.0  1.14.0  1.13.0  1.12.0  1.11.0  1.10.7  1.9.12  1.8.2  1.7.0  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0  0.2.0 

**Note:** To get more information about this package, such as access to older versions, view [this package on pkg.go.dev](https://pkg.go.dev/cloud.google.com/go/resourcemanager/apiv3). 

Package resourcemanager is an auto-generated package for the Cloud Resource Manager API. 

Creates, reads, and updates metadata for Google Cloud Platform resource containers. 

## General documentation

For information that is relevant for all client libraries please reference <https://pkg.go.dev/cloud.google.com/go#pkg-overview>. Some information on this page includes: 

  * [Authentication and Authorization](https://pkg.go.dev/cloud.google.com/go#hdr-Authentication_and_Authorization)
  * [Timeouts and Cancellation](https://pkg.go.dev/cloud.google.com/go#hdr-Timeouts_and_Cancellation)
  * [Testing against Client Libraries](https://pkg.go.dev/cloud.google.com/go#hdr-Testing)
  * [Debugging Client Libraries](https://pkg.go.dev/cloud.google.com/go#hdr-Debugging)
  * [Inspecting errors](https://pkg.go.dev/cloud.google.com/go#hdr-Inspecting_errors)



## Example usage

To get started with this package, create a client.
    
    
    // go get cloud.google.com/go/resourcemanager/apiv3@latest
    ctx := context.Background()
    // This snippet has been automatically generated and should be regarded as a code template only.
    // It will require modifications to work:
    // - It may require correct/in-range values for request initialization.
    // - It may require specifying regional endpoints when creating the service client as shown in:
    //   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    c, err := resourcemanager.NewFoldersClient(ctx)
    if err != nil {
        // TODO: Handle error.
    }
    defer c.Close()

The client will use your default application credentials. Clients should be reused instead of created as needed. The methods of Client are safe for concurrent use by multiple goroutines. The returned client must be Closed when it is done being used. 

## Using the Client

The following is an example of making an API call with the newly created client, mentioned above.
    
    
    req := &resourcemanagerpb.CreateFolderRequest{
        // TODO: Fill request struct fields.
        // See https://pkg.go.dev/cloud.google.com/go/resourcemanager/apiv3/resourcemanagerpb#CreateFolderRequest.
    }
    op, err := c.CreateFolder(ctx, req)
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

The ctx passed to NewFoldersClient is used for authentication requests and for creating the underlying connection, but is not used for subsequent calls. Individual methods on the client use the ctx given to them. 

To close the open connection, use the Close() method.

## Functions 

### func DefaultAuthScopes 
    
    
    func DefaultAuthScopes() [][string](https://pkg.go.dev/builtin#string)

DefaultAuthScopes reports the default set of authentication scopes to use with this package.

## CreateFolderOperation
    
    
    type CreateFolderOperation struct {
    	// contains filtered or unexported fields
    }

CreateFolderOperation manages a long-running operation from CreateFolder.

### func (*CreateFolderOperation) Done 
    
    
    func (op *CreateFolderOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*CreateFolderOperation) Metadata 
    
    
    func (op *CreateFolderOperation) Metadata() (*[resourcemanagerpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb).[CreateFolderMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb#cloud_google_com_go_resourcemanager_apiv3_resourcemanagerpb_CreateFolderMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*CreateFolderOperation) Name 
    
    
    func (op *CreateFolderOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*CreateFolderOperation) Poll 
    
    
    func (op *CreateFolderOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[resourcemanagerpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb).[Folder](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb#cloud_google_com_go_resourcemanager_apiv3_resourcemanagerpb_Folder), [error](https://pkg.go.dev/builtin#error))

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*CreateFolderOperation) Wait 
    
    
    func (op *CreateFolderOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[resourcemanagerpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb).[Folder](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb#cloud_google_com_go_resourcemanager_apiv3_resourcemanagerpb_Folder), [error](https://pkg.go.dev/builtin#error))

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## CreateProjectOperation
    
    
    type CreateProjectOperation struct {
    	// contains filtered or unexported fields
    }

CreateProjectOperation manages a long-running operation from CreateProject.

### func (*CreateProjectOperation) Done 
    
    
    func (op *CreateProjectOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*CreateProjectOperation) Metadata 
    
    
    func (op *CreateProjectOperation) Metadata() (*[resourcemanagerpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb).[CreateProjectMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb#cloud_google_com_go_resourcemanager_apiv3_resourcemanagerpb_CreateProjectMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*CreateProjectOperation) Name 
    
    
    func (op *CreateProjectOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*CreateProjectOperation) Poll 
    
    
    func (op *CreateProjectOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[resourcemanagerpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb).[Project](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb#cloud_google_com_go_resourcemanager_apiv3_resourcemanagerpb_Project), [error](https://pkg.go.dev/builtin#error))

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*CreateProjectOperation) Wait 
    
    
    func (op *CreateProjectOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[resourcemanagerpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb).[Project](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb#cloud_google_com_go_resourcemanager_apiv3_resourcemanagerpb_Project), [error](https://pkg.go.dev/builtin#error))

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## CreateTagBindingOperation
    
    
    type CreateTagBindingOperation struct {
    	// contains filtered or unexported fields
    }

CreateTagBindingOperation manages a long-running operation from CreateTagBinding.

### func (*CreateTagBindingOperation) Done 
    
    
    func (op *CreateTagBindingOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*CreateTagBindingOperation) Metadata 
    
    
    func (op *CreateTagBindingOperation) Metadata() (*[resourcemanagerpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb).[CreateTagBindingMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb#cloud_google_com_go_resourcemanager_apiv3_resourcemanagerpb_CreateTagBindingMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*CreateTagBindingOperation) Name 
    
    
    func (op *CreateTagBindingOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*CreateTagBindingOperation) Poll 
    
    
    func (op *CreateTagBindingOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[resourcemanagerpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb).[TagBinding](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb#cloud_google_com_go_resourcemanager_apiv3_resourcemanagerpb_TagBinding), [error](https://pkg.go.dev/builtin#error))

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*CreateTagBindingOperation) Wait 
    
    
    func (op *CreateTagBindingOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[resourcemanagerpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb).[TagBinding](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb#cloud_google_com_go_resourcemanager_apiv3_resourcemanagerpb_TagBinding), [error](https://pkg.go.dev/builtin#error))

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## CreateTagHoldOperation
    
    
    type CreateTagHoldOperation struct {
    	// contains filtered or unexported fields
    }

CreateTagHoldOperation manages a long-running operation from CreateTagHold.

### func (*CreateTagHoldOperation) Done 
    
    
    func (op *CreateTagHoldOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*CreateTagHoldOperation) Metadata 
    
    
    func (op *CreateTagHoldOperation) Metadata() (*[resourcemanagerpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb).[CreateTagHoldMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb#cloud_google_com_go_resourcemanager_apiv3_resourcemanagerpb_CreateTagHoldMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*CreateTagHoldOperation) Name 
    
    
    func (op *CreateTagHoldOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*CreateTagHoldOperation) Poll 
    
    
    func (op *CreateTagHoldOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[resourcemanagerpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb).[TagHold](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb#cloud_google_com_go_resourcemanager_apiv3_resourcemanagerpb_TagHold), [error](https://pkg.go.dev/builtin#error))

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*CreateTagHoldOperation) Wait 
    
    
    func (op *CreateTagHoldOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[resourcemanagerpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb).[TagHold](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb#cloud_google_com_go_resourcemanager_apiv3_resourcemanagerpb_TagHold), [error](https://pkg.go.dev/builtin#error))

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## CreateTagKeyOperation
    
    
    type CreateTagKeyOperation struct {
    	// contains filtered or unexported fields
    }

CreateTagKeyOperation manages a long-running operation from CreateTagKey.

### func (*CreateTagKeyOperation) Done 
    
    
    func (op *CreateTagKeyOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*CreateTagKeyOperation) Metadata 
    
    
    func (op *CreateTagKeyOperation) Metadata() (*[resourcemanagerpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb).[CreateTagKeyMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb#cloud_google_com_go_resourcemanager_apiv3_resourcemanagerpb_CreateTagKeyMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*CreateTagKeyOperation) Name 
    
    
    func (op *CreateTagKeyOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*CreateTagKeyOperation) Poll 
    
    
    func (op *CreateTagKeyOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[resourcemanagerpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb).[TagKey](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb#cloud_google_com_go_resourcemanager_apiv3_resourcemanagerpb_TagKey), [error](https://pkg.go.dev/builtin#error))

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*CreateTagKeyOperation) Wait 
    
    
    func (op *CreateTagKeyOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[resourcemanagerpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb).[TagKey](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb#cloud_google_com_go_resourcemanager_apiv3_resourcemanagerpb_TagKey), [error](https://pkg.go.dev/builtin#error))

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## CreateTagValueOperation
    
    
    type CreateTagValueOperation struct {
    	// contains filtered or unexported fields
    }

CreateTagValueOperation manages a long-running operation from CreateTagValue.

### func (*CreateTagValueOperation) Done 
    
    
    func (op *CreateTagValueOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*CreateTagValueOperation) Metadata 
    
    
    func (op *CreateTagValueOperation) Metadata() (*[resourcemanagerpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb).[CreateTagValueMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb#cloud_google_com_go_resourcemanager_apiv3_resourcemanagerpb_CreateTagValueMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*CreateTagValueOperation) Name 
    
    
    func (op *CreateTagValueOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*CreateTagValueOperation) Poll 
    
    
    func (op *CreateTagValueOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[resourcemanagerpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb).[TagValue](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb#cloud_google_com_go_resourcemanager_apiv3_resourcemanagerpb_TagValue), [error](https://pkg.go.dev/builtin#error))

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*CreateTagValueOperation) Wait 
    
    
    func (op *CreateTagValueOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[resourcemanagerpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb).[TagValue](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb#cloud_google_com_go_resourcemanager_apiv3_resourcemanagerpb_TagValue), [error](https://pkg.go.dev/builtin#error))

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## DeleteFolderOperation
    
    
    type DeleteFolderOperation struct {
    	// contains filtered or unexported fields
    }

DeleteFolderOperation manages a long-running operation from DeleteFolder.

### func (*DeleteFolderOperation) Done 
    
    
    func (op *DeleteFolderOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*DeleteFolderOperation) Metadata 
    
    
    func (op *DeleteFolderOperation) Metadata() (*[resourcemanagerpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb).[DeleteFolderMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb#cloud_google_com_go_resourcemanager_apiv3_resourcemanagerpb_DeleteFolderMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*DeleteFolderOperation) Name 
    
    
    func (op *DeleteFolderOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*DeleteFolderOperation) Poll 
    
    
    func (op *DeleteFolderOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[resourcemanagerpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb).[Folder](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb#cloud_google_com_go_resourcemanager_apiv3_resourcemanagerpb_Folder), [error](https://pkg.go.dev/builtin#error))

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*DeleteFolderOperation) Wait 
    
    
    func (op *DeleteFolderOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[resourcemanagerpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb).[Folder](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb#cloud_google_com_go_resourcemanager_apiv3_resourcemanagerpb_Folder), [error](https://pkg.go.dev/builtin#error))

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## DeleteProjectOperation
    
    
    type DeleteProjectOperation struct {
    	// contains filtered or unexported fields
    }

DeleteProjectOperation manages a long-running operation from DeleteProject.

### func (*DeleteProjectOperation) Done 
    
    
    func (op *DeleteProjectOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*DeleteProjectOperation) Metadata 
    
    
    func (op *DeleteProjectOperation) Metadata() (*[resourcemanagerpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb).[DeleteProjectMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb#cloud_google_com_go_resourcemanager_apiv3_resourcemanagerpb_DeleteProjectMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*DeleteProjectOperation) Name 
    
    
    func (op *DeleteProjectOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*DeleteProjectOperation) Poll 
    
    
    func (op *DeleteProjectOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[resourcemanagerpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb).[Project](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb#cloud_google_com_go_resourcemanager_apiv3_resourcemanagerpb_Project), [error](https://pkg.go.dev/builtin#error))

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*DeleteProjectOperation) Wait 
    
    
    func (op *DeleteProjectOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[resourcemanagerpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb).[Project](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb#cloud_google_com_go_resourcemanager_apiv3_resourcemanagerpb_Project), [error](https://pkg.go.dev/builtin#error))

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## DeleteTagBindingOperation
    
    
    type DeleteTagBindingOperation struct {
    	// contains filtered or unexported fields
    }

DeleteTagBindingOperation manages a long-running operation from DeleteTagBinding.

### func (*DeleteTagBindingOperation) Done 
    
    
    func (op *DeleteTagBindingOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*DeleteTagBindingOperation) Metadata 
    
    
    func (op *DeleteTagBindingOperation) Metadata() (*[resourcemanagerpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb).[DeleteTagBindingMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb#cloud_google_com_go_resourcemanager_apiv3_resourcemanagerpb_DeleteTagBindingMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*DeleteTagBindingOperation) Name 
    
    
    func (op *DeleteTagBindingOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*DeleteTagBindingOperation) Poll 
    
    
    func (op *DeleteTagBindingOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*DeleteTagBindingOperation) Wait 
    
    
    func (op *DeleteTagBindingOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## DeleteTagHoldOperation
    
    
    type DeleteTagHoldOperation struct {
    	// contains filtered or unexported fields
    }

DeleteTagHoldOperation manages a long-running operation from DeleteTagHold.

### func (*DeleteTagHoldOperation) Done 
    
    
    func (op *DeleteTagHoldOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*DeleteTagHoldOperation) Metadata 
    
    
    func (op *DeleteTagHoldOperation) Metadata() (*[resourcemanagerpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb).[DeleteTagHoldMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb#cloud_google_com_go_resourcemanager_apiv3_resourcemanagerpb_DeleteTagHoldMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*DeleteTagHoldOperation) Name 
    
    
    func (op *DeleteTagHoldOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*DeleteTagHoldOperation) Poll 
    
    
    func (op *DeleteTagHoldOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*DeleteTagHoldOperation) Wait 
    
    
    func (op *DeleteTagHoldOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## DeleteTagKeyOperation
    
    
    type DeleteTagKeyOperation struct {
    	// contains filtered or unexported fields
    }

DeleteTagKeyOperation manages a long-running operation from DeleteTagKey.

### func (*DeleteTagKeyOperation) Done 
    
    
    func (op *DeleteTagKeyOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*DeleteTagKeyOperation) Metadata 
    
    
    func (op *DeleteTagKeyOperation) Metadata() (*[resourcemanagerpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb).[DeleteTagKeyMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb#cloud_google_com_go_resourcemanager_apiv3_resourcemanagerpb_DeleteTagKeyMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*DeleteTagKeyOperation) Name 
    
    
    func (op *DeleteTagKeyOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*DeleteTagKeyOperation) Poll 
    
    
    func (op *DeleteTagKeyOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[resourcemanagerpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb).[TagKey](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb#cloud_google_com_go_resourcemanager_apiv3_resourcemanagerpb_TagKey), [error](https://pkg.go.dev/builtin#error))

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*DeleteTagKeyOperation) Wait 
    
    
    func (op *DeleteTagKeyOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[resourcemanagerpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb).[TagKey](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb#cloud_google_com_go_resourcemanager_apiv3_resourcemanagerpb_TagKey), [error](https://pkg.go.dev/builtin#error))

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## DeleteTagValueOperation
    
    
    type DeleteTagValueOperation struct {
    	// contains filtered or unexported fields
    }

DeleteTagValueOperation manages a long-running operation from DeleteTagValue.

### func (*DeleteTagValueOperation) Done 
    
    
    func (op *DeleteTagValueOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*DeleteTagValueOperation) Metadata 
    
    
    func (op *DeleteTagValueOperation) Metadata() (*[resourcemanagerpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb).[DeleteTagValueMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb#cloud_google_com_go_resourcemanager_apiv3_resourcemanagerpb_DeleteTagValueMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*DeleteTagValueOperation) Name 
    
    
    func (op *DeleteTagValueOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*DeleteTagValueOperation) Poll 
    
    
    func (op *DeleteTagValueOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[resourcemanagerpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb).[TagValue](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb#cloud_google_com_go_resourcemanager_apiv3_resourcemanagerpb_TagValue), [error](https://pkg.go.dev/builtin#error))

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*DeleteTagValueOperation) Wait 
    
    
    func (op *DeleteTagValueOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[resourcemanagerpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb).[TagValue](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb#cloud_google_com_go_resourcemanager_apiv3_resourcemanagerpb_TagValue), [error](https://pkg.go.dev/builtin#error))

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## EffectiveTagIterator
    
    
    type EffectiveTagIterator struct {
    
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
    	InternalFetch func(pageSize [int](https://pkg.go.dev/builtin#int), pageToken [string](https://pkg.go.dev/builtin#string)) (results []*resourcemanagerpb.EffectiveTag, nextPageToken [string](https://pkg.go.dev/builtin#string), err [error](https://pkg.go.dev/builtin#error))
    	// contains filtered or unexported fields
    }

EffectiveTagIterator manages a stream of *resourcemanagerpb.EffectiveTag.

### func (*EffectiveTagIterator) All 
    
    
    func (it *EffectiveTagIterator) All() iter.Seq2[*resourcemanagerpb.EffectiveTag, error]

All returns an iterator. If an error is returned by the iterator, the iterator will stop after that iteration.

### func (*EffectiveTagIterator) Next 
    
    
    func (it *EffectiveTagIterator) Next() (*[resourcemanagerpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb).[EffectiveTag](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb#cloud_google_com_go_resourcemanager_apiv3_resourcemanagerpb_EffectiveTag), [error](https://pkg.go.dev/builtin#error))

Next returns the next result. Its second return value is iterator.Done if there are no more results. Once Next returns Done, all subsequent calls will return Done.

### func (*EffectiveTagIterator) PageInfo 
    
    
    func (it *EffectiveTagIterator) PageInfo() *iterator.PageInfo

PageInfo supports pagination. See the [google.golang.org/api/iterator] package for details.

## FolderIterator
    
    
    type FolderIterator struct {
    
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
    	InternalFetch func(pageSize [int](https://pkg.go.dev/builtin#int), pageToken [string](https://pkg.go.dev/builtin#string)) (results []*resourcemanagerpb.Folder, nextPageToken [string](https://pkg.go.dev/builtin#string), err [error](https://pkg.go.dev/builtin#error))
    	// contains filtered or unexported fields
    }

FolderIterator manages a stream of *resourcemanagerpb.Folder.

### func (*FolderIterator) All 
    
    
    func (it *FolderIterator) All() iter.Seq2[*resourcemanagerpb.Folder, error]

All returns an iterator. If an error is returned by the iterator, the iterator will stop after that iteration.

### func (*FolderIterator) Next 
    
    
    func (it *FolderIterator) Next() (*[resourcemanagerpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb).[Folder](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb#cloud_google_com_go_resourcemanager_apiv3_resourcemanagerpb_Folder), [error](https://pkg.go.dev/builtin#error))

Next returns the next result. Its second return value is iterator.Done if there are no more results. Once Next returns Done, all subsequent calls will return Done.

### func (*FolderIterator) PageInfo 
    
    
    func (it *FolderIterator) PageInfo() *iterator.PageInfo

PageInfo supports pagination. See the [google.golang.org/api/iterator] package for details.

## FoldersCallOptions
    
    
    type FoldersCallOptions struct {
    	GetFolder          []gax.CallOption
    	ListFolders        []gax.CallOption
    	SearchFolders      []gax.CallOption
    	CreateFolder       []gax.CallOption
    	UpdateFolder       []gax.CallOption
    	MoveFolder         []gax.CallOption
    	DeleteFolder       []gax.CallOption
    	UndeleteFolder     []gax.CallOption
    	GetIamPolicy       []gax.CallOption
    	SetIamPolicy       []gax.CallOption
    	TestIamPermissions []gax.CallOption
    	GetOperation       []gax.CallOption
    }

FoldersCallOptions contains the retry settings for each method of FoldersClient.

## FoldersClient
    
    
    type FoldersClient struct {
    
    	// The call options for this service.
    	CallOptions *FoldersCallOptions
    
    	// LROClient is used internally to handle long-running operations.
    	// It is exposed so that its CallOptions can be modified if required.
    	// Users should not Close this client.
    	LROClient *lroauto.OperationsClient
    	// contains filtered or unexported fields
    }

FoldersClient is a client for interacting with Cloud Resource Manager API. Methods, except Close, may be called concurrently. However, fields must not be modified concurrently with method calls.

Manages Cloud Platform folder resources. Folders can be used to organize the resources under an organization and to control the policies applied to groups of resources.

### func NewFoldersClient 
    
    
    func NewFoldersClient(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...option.ClientOption) (*FoldersClient, [error](https://pkg.go.dev/builtin#error))

NewFoldersClient creates a new folders client based on gRPC. The returned client must be Closed when it is done being used to clean up its underlying connections.

Manages Cloud Platform folder resources. Folders can be used to organize the resources under an organization and to control the policies applied to groups of resources.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	resourcemanager "cloud.google.com/go/resourcemanager/apiv3"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := resourcemanager.NewFoldersClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	// TODO: Use client.
    	_ = c
    }
    

### func NewFoldersRESTClient 
    
    
    func NewFoldersRESTClient(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...option.ClientOption) (*FoldersClient, [error](https://pkg.go.dev/builtin#error))

NewFoldersRESTClient creates a new folders rest client.

Manages Cloud Platform folder resources. Folders can be used to organize the resources under an organization and to control the policies applied to groups of resources.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	resourcemanager "cloud.google.com/go/resourcemanager/apiv3"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := resourcemanager.[NewFoldersRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3.html#cloud_google_com_go_resourcemanager_apiv3_FoldersClient_NewFoldersRESTClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	// TODO: Use client.
    	_ = c
    }
    

### func (*FoldersClient) Close 
    
    
    func (c *FoldersClient) Close() [error](https://pkg.go.dev/builtin#error)

Close closes the connection to the API service. **Always** call Close() when the client is no longer required.

### func (*FoldersClient) Connection (deprecated)
    
    
    func (c *FoldersClient) Connection() *grpc.ClientConn

Connection returns a connection to the API service.

Deprecated: Connections are now pooled so this method does not always return the same resource.

### func (*FoldersClient) CreateFolder 
    
    
    func (c *FoldersClient) CreateFolder(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[resourcemanagerpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb).[CreateFolderRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb#cloud_google_com_go_resourcemanager_apiv3_resourcemanagerpb_CreateFolderRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*CreateFolderOperation, [error](https://pkg.go.dev/builtin#error))

CreateFolder creates a folder in the resource hierarchy. Returns an Operation which can be used to track the progress of the folder creation workflow. Upon success, the Operation.response field will be populated with the created Folder.

In order to succeed, the addition of this new folder must not violate the folder naming, height, or fanout constraints.
    
    
    The folder’s display_name must be distinct from all other folders that
    share its parent.
    
    The addition of the folder must not cause the active folder hierarchy
    to exceed a height of 10. Note, the full active + deleted folder hierarchy
    is allowed to reach a height of 20; this provides additional headroom when
    moving folders that contain deleted folders.
    
    The addition of the folder must not cause the total number of folders
    under its parent to exceed 300.
    

If the operation fails due to a folder constraint violation, some errors may be returned by the CreateFolder request, with status code FAILED_PRECONDITION and an error description. Other folder constraint violations will be communicated in the Operation, with the specific PreconditionFailure returned in the details list in the Operation.error field.

The caller must have resourcemanager.folders.create permission on the identified parent.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	resourcemanager "cloud.google.com/go/resourcemanager/apiv3"
    
    	resourcemanagerpb "cloud.google.com/go/resourcemanager/apiv3/resourcemanagerpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := resourcemanager.NewFoldersClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &resourcemanagerpb.CreateFolderRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/resourcemanager/apiv3/resourcemanagerpb#CreateFolderRequest.
    	}
    	op, err := c.CreateFolder(ctx, req)
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
    

### func (*FoldersClient) CreateFolderOperation 
    
    
    func (c *FoldersClient) CreateFolderOperation(name [string](https://pkg.go.dev/builtin#string)) *CreateFolderOperation

CreateFolderOperation returns a new CreateFolderOperation from a given name. The name must be that of a previously created CreateFolderOperation, possibly from a different process.

### func (*FoldersClient) DeleteFolder 
    
    
    func (c *FoldersClient) DeleteFolder(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[resourcemanagerpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb).[DeleteFolderRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb#cloud_google_com_go_resourcemanager_apiv3_resourcemanagerpb_DeleteFolderRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*DeleteFolderOperation, [error](https://pkg.go.dev/builtin#error))

DeleteFolder requests deletion of a folder. The folder is moved into the DELETE_REQUESTED state immediately, and is deleted approximately 30 days later. This method may only be called on an empty folder, where a folder is empty if it doesn’t contain any folders or projects in the [ACTIVE][google.cloud.resourcemanager.v3.Folder.State.ACTIVE (at <http://google.cloud.resourcemanager.v3.Folder.State.ACTIVE>)] state. If called on a folder in DELETE_REQUESTED state the operation will result in a no-op success. The caller must have resourcemanager.folders.delete permission on the identified folder.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	resourcemanager "cloud.google.com/go/resourcemanager/apiv3"
    
    	resourcemanagerpb "cloud.google.com/go/resourcemanager/apiv3/resourcemanagerpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := resourcemanager.NewFoldersClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &resourcemanagerpb.DeleteFolderRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/resourcemanager/apiv3/resourcemanagerpb#DeleteFolderRequest.
    	}
    	op, err := c.DeleteFolder(ctx, req)
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
    

### func (*FoldersClient) DeleteFolderOperation 
    
    
    func (c *FoldersClient) DeleteFolderOperation(name [string](https://pkg.go.dev/builtin#string)) *DeleteFolderOperation

DeleteFolderOperation returns a new DeleteFolderOperation from a given name. The name must be that of a previously created DeleteFolderOperation, possibly from a different process.

### func (*FoldersClient) GetFolder 
    
    
    func (c *FoldersClient) GetFolder(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[resourcemanagerpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb).[GetFolderRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb#cloud_google_com_go_resourcemanager_apiv3_resourcemanagerpb_GetFolderRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[resourcemanagerpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb).[Folder](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb#cloud_google_com_go_resourcemanager_apiv3_resourcemanagerpb_Folder), [error](https://pkg.go.dev/builtin#error))

GetFolder retrieves a folder identified by the supplied resource name. Valid folder resource names have the format folders/{folder_id} (for example, folders/1234). The caller must have resourcemanager.folders.get permission on the identified folder.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	resourcemanager "cloud.google.com/go/resourcemanager/apiv3"
    
    	resourcemanagerpb "cloud.google.com/go/resourcemanager/apiv3/resourcemanagerpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := resourcemanager.NewFoldersClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &resourcemanagerpb.GetFolderRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/resourcemanager/apiv3/resourcemanagerpb#GetFolderRequest.
    	}
    	resp, err := c.GetFolder(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*FoldersClient) GetIamPolicy 
    
    
    func (c *FoldersClient) GetIamPolicy(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[iampb](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb).[GetIamPolicyRequest](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb#GetIamPolicyRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[iampb](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb).[Policy](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb#Policy), [error](https://pkg.go.dev/builtin#error))

GetIamPolicy gets the access control policy for a folder. The returned policy may be empty if no such policy or resource exists. The resource field should be the folder’s resource name, for example: “folders/1234”. The caller must have resourcemanager.folders.getIamPolicy permission on the identified folder.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	iampb "cloud.google.com/go/iam/apiv1/iampb"
    
    	resourcemanager "cloud.google.com/go/resourcemanager/apiv3"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := resourcemanager.NewFoldersClient(ctx)
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
    

### func (*FoldersClient) GetOperation 
    
    
    func (c *FoldersClient) GetOperation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[GetOperationRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#GetOperationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[Operation](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#Operation), [error](https://pkg.go.dev/builtin#error))

GetOperation is a utility method from google.longrunning.Operations.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    
    	resourcemanager "cloud.google.com/go/resourcemanager/apiv3"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := resourcemanager.NewFoldersClient(ctx)
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
    

### func (*FoldersClient) ListFolders 
    
    
    func (c *FoldersClient) ListFolders(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[resourcemanagerpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb).[ListFoldersRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb#cloud_google_com_go_resourcemanager_apiv3_resourcemanagerpb_ListFoldersRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *FolderIterator

ListFolders lists the folders that are direct descendants of supplied parent resource. list() provides a strongly consistent view of the folders underneath the specified parent resource. list() returns folders sorted based upon the (ascending) lexical ordering of their display_name. The caller must have resourcemanager.folders.list permission on the identified parent.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	resourcemanager "cloud.google.com/go/resourcemanager/apiv3"
    
    	resourcemanagerpb "cloud.google.com/go/resourcemanager/apiv3/resourcemanagerpb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := resourcemanager.NewFoldersClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &resourcemanagerpb.ListFoldersRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/resourcemanager/apiv3/resourcemanagerpb#ListFoldersRequest.
    	}
    	it := c.ListFolders(ctx, req)
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
    		_ = it.Response.(*resourcemanagerpb.ListFoldersResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	resourcemanager "cloud.google.com/go/resourcemanager/apiv3"
    	resourcemanagerpb "cloud.google.com/go/resourcemanager/apiv3/resourcemanagerpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := resourcemanager.NewFoldersClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &resourcemanagerpb.ListFoldersRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/resourcemanager/apiv3/resourcemanagerpb#ListFoldersRequest.
    	}
    	for resp, err := range c.ListFolders(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*FoldersClient) MoveFolder 
    
    
    func (c *FoldersClient) MoveFolder(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[resourcemanagerpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb).[MoveFolderRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb#cloud_google_com_go_resourcemanager_apiv3_resourcemanagerpb_MoveFolderRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*MoveFolderOperation, [error](https://pkg.go.dev/builtin#error))

MoveFolder moves a folder under a new resource parent. Returns an Operation which can be used to track the progress of the folder move workflow. Upon success, the Operation.response field will be populated with the moved folder. Upon failure, a FolderOperationError categorizing the failure cause will be returned - if the failure occurs synchronously then the FolderOperationError will be returned in the Status.details field. If it occurs asynchronously, then the FolderOperation will be returned in the Operation.error field. In addition, the Operation.metadata field will be populated with a FolderOperation message as an aid to stateless clients. Folder moves will be rejected if they violate either the naming, height, or fanout constraints described in the CreateFolder documentation. The caller must have resourcemanager.folders.move permission on the folder’s current and proposed new parent.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	resourcemanager "cloud.google.com/go/resourcemanager/apiv3"
    
    	resourcemanagerpb "cloud.google.com/go/resourcemanager/apiv3/resourcemanagerpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := resourcemanager.NewFoldersClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &resourcemanagerpb.MoveFolderRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/resourcemanager/apiv3/resourcemanagerpb#MoveFolderRequest.
    	}
    	op, err := c.MoveFolder(ctx, req)
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
    

### func (*FoldersClient) MoveFolderOperation 
    
    
    func (c *FoldersClient) MoveFolderOperation(name [string](https://pkg.go.dev/builtin#string)) *MoveFolderOperation

MoveFolderOperation returns a new MoveFolderOperation from a given name. The name must be that of a previously created MoveFolderOperation, possibly from a different process.

### func (*FoldersClient) SearchFolders 
    
    
    func (c *FoldersClient) SearchFolders(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[resourcemanagerpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb).[SearchFoldersRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb#cloud_google_com_go_resourcemanager_apiv3_resourcemanagerpb_SearchFoldersRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *FolderIterator

SearchFolders search for folders that match specific filter criteria. search() provides an eventually consistent view of the folders a user has access to which meet the specified filter criteria.

This will only return folders on which the caller has the permission resourcemanager.folders.get.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	resourcemanager "cloud.google.com/go/resourcemanager/apiv3"
    
    	resourcemanagerpb "cloud.google.com/go/resourcemanager/apiv3/resourcemanagerpb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := resourcemanager.NewFoldersClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &resourcemanagerpb.SearchFoldersRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/resourcemanager/apiv3/resourcemanagerpb#SearchFoldersRequest.
    	}
    	it := c.SearchFolders(ctx, req)
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
    		_ = it.Response.(*resourcemanagerpb.SearchFoldersResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	resourcemanager "cloud.google.com/go/resourcemanager/apiv3"
    	resourcemanagerpb "cloud.google.com/go/resourcemanager/apiv3/resourcemanagerpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := resourcemanager.NewFoldersClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &resourcemanagerpb.SearchFoldersRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/resourcemanager/apiv3/resourcemanagerpb#SearchFoldersRequest.
    	}
    	for resp, err := range c.SearchFolders(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*FoldersClient) SetIamPolicy 
    
    
    func (c *FoldersClient) SetIamPolicy(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[iampb](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb).[SetIamPolicyRequest](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb#SetIamPolicyRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[iampb](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb).[Policy](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb#Policy), [error](https://pkg.go.dev/builtin#error))

SetIamPolicy sets the access control policy on a folder, replacing any existing policy. The resource field should be the folder’s resource name, for example: “folders/1234”. The caller must have resourcemanager.folders.setIamPolicy permission on the identified folder.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	iampb "cloud.google.com/go/iam/apiv1/iampb"
    
    	resourcemanager "cloud.google.com/go/resourcemanager/apiv3"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := resourcemanager.NewFoldersClient(ctx)
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
    

### func (*FoldersClient) TestIamPermissions 
    
    
    func (c *FoldersClient) TestIamPermissions(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[iampb](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb).[TestIamPermissionsRequest](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb#TestIamPermissionsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[iampb](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb).[TestIamPermissionsResponse](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb#TestIamPermissionsResponse), [error](https://pkg.go.dev/builtin#error))

TestIamPermissions returns permissions that a caller has on the specified folder. The resource field should be the folder’s resource name, for example: “folders/1234”.

There are no permissions required for making this API call.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	iampb "cloud.google.com/go/iam/apiv1/iampb"
    
    	resourcemanager "cloud.google.com/go/resourcemanager/apiv3"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := resourcemanager.NewFoldersClient(ctx)
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
    

### func (*FoldersClient) UndeleteFolder 
    
    
    func (c *FoldersClient) UndeleteFolder(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[resourcemanagerpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb).[UndeleteFolderRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb#cloud_google_com_go_resourcemanager_apiv3_resourcemanagerpb_UndeleteFolderRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*UndeleteFolderOperation, [error](https://pkg.go.dev/builtin#error))

UndeleteFolder cancels the deletion request for a folder. This method may be called on a folder in any state. If the folder is in the [ACTIVE][google.cloud.resourcemanager.v3.Folder.State.ACTIVE (at <http://google.cloud.resourcemanager.v3.Folder.State.ACTIVE>)] state the result will be a no-op success. In order to succeed, the folder’s parent must be in the [ACTIVE][google.cloud.resourcemanager.v3.Folder.State.ACTIVE (at <http://google.cloud.resourcemanager.v3.Folder.State.ACTIVE>)] state. In addition, reintroducing the folder into the tree must not violate folder naming, height, and fanout constraints described in the CreateFolder documentation. The caller must have resourcemanager.folders.undelete permission on the identified folder.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	resourcemanager "cloud.google.com/go/resourcemanager/apiv3"
    
    	resourcemanagerpb "cloud.google.com/go/resourcemanager/apiv3/resourcemanagerpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := resourcemanager.NewFoldersClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &resourcemanagerpb.UndeleteFolderRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/resourcemanager/apiv3/resourcemanagerpb#UndeleteFolderRequest.
    	}
    	op, err := c.UndeleteFolder(ctx, req)
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
    

### func (*FoldersClient) UndeleteFolderOperation 
    
    
    func (c *FoldersClient) UndeleteFolderOperation(name [string](https://pkg.go.dev/builtin#string)) *UndeleteFolderOperation

UndeleteFolderOperation returns a new UndeleteFolderOperation from a given name. The name must be that of a previously created UndeleteFolderOperation, possibly from a different process.

### func (*FoldersClient) UpdateFolder 
    
    
    func (c *FoldersClient) UpdateFolder(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[resourcemanagerpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb).[UpdateFolderRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb#cloud_google_com_go_resourcemanager_apiv3_resourcemanagerpb_UpdateFolderRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*UpdateFolderOperation, [error](https://pkg.go.dev/builtin#error))

UpdateFolder updates a folder, changing its display_name. Changes to the folder display_name will be rejected if they violate either the display_name formatting rules or the naming constraints described in the CreateFolder documentation.

The folder’s display_name must start and end with a letter or digit, may contain letters, digits, spaces, hyphens and underscores and can be between 3 and 30 characters. This is captured by the regular expression: [\p{L}\p{N}][\p{L}\p{N}_- ]{1,28}[\p{L}\p{N}]. The caller must have resourcemanager.folders.update permission on the identified folder.

If the update fails due to the unique name constraint then a PreconditionFailure explaining this violation will be returned in the Status.details field.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	resourcemanager "cloud.google.com/go/resourcemanager/apiv3"
    
    	resourcemanagerpb "cloud.google.com/go/resourcemanager/apiv3/resourcemanagerpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := resourcemanager.NewFoldersClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &resourcemanagerpb.UpdateFolderRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/resourcemanager/apiv3/resourcemanagerpb#UpdateFolderRequest.
    	}
    	op, err := c.UpdateFolder(ctx, req)
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
    

### func (*FoldersClient) UpdateFolderOperation 
    
    
    func (c *FoldersClient) UpdateFolderOperation(name [string](https://pkg.go.dev/builtin#string)) *UpdateFolderOperation

UpdateFolderOperation returns a new UpdateFolderOperation from a given name. The name must be that of a previously created UpdateFolderOperation, possibly from a different process.

## MoveFolderOperation
    
    
    type MoveFolderOperation struct {
    	// contains filtered or unexported fields
    }

MoveFolderOperation manages a long-running operation from MoveFolder.

### func (*MoveFolderOperation) Done 
    
    
    func (op *MoveFolderOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*MoveFolderOperation) Metadata 
    
    
    func (op *MoveFolderOperation) Metadata() (*[resourcemanagerpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb).[MoveFolderMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb#cloud_google_com_go_resourcemanager_apiv3_resourcemanagerpb_MoveFolderMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*MoveFolderOperation) Name 
    
    
    func (op *MoveFolderOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*MoveFolderOperation) Poll 
    
    
    func (op *MoveFolderOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[resourcemanagerpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb).[Folder](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb#cloud_google_com_go_resourcemanager_apiv3_resourcemanagerpb_Folder), [error](https://pkg.go.dev/builtin#error))

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*MoveFolderOperation) Wait 
    
    
    func (op *MoveFolderOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[resourcemanagerpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb).[Folder](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb#cloud_google_com_go_resourcemanager_apiv3_resourcemanagerpb_Folder), [error](https://pkg.go.dev/builtin#error))

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## MoveProjectOperation
    
    
    type MoveProjectOperation struct {
    	// contains filtered or unexported fields
    }

MoveProjectOperation manages a long-running operation from MoveProject.

### func (*MoveProjectOperation) Done 
    
    
    func (op *MoveProjectOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*MoveProjectOperation) Metadata 
    
    
    func (op *MoveProjectOperation) Metadata() (*[resourcemanagerpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb).[MoveProjectMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb#cloud_google_com_go_resourcemanager_apiv3_resourcemanagerpb_MoveProjectMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*MoveProjectOperation) Name 
    
    
    func (op *MoveProjectOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*MoveProjectOperation) Poll 
    
    
    func (op *MoveProjectOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[resourcemanagerpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb).[Project](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb#cloud_google_com_go_resourcemanager_apiv3_resourcemanagerpb_Project), [error](https://pkg.go.dev/builtin#error))

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*MoveProjectOperation) Wait 
    
    
    func (op *MoveProjectOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[resourcemanagerpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb).[Project](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb#cloud_google_com_go_resourcemanager_apiv3_resourcemanagerpb_Project), [error](https://pkg.go.dev/builtin#error))

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## OrganizationIterator
    
    
    type OrganizationIterator struct {
    
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
    	InternalFetch func(pageSize [int](https://pkg.go.dev/builtin#int), pageToken [string](https://pkg.go.dev/builtin#string)) (results []*resourcemanagerpb.Organization, nextPageToken [string](https://pkg.go.dev/builtin#string), err [error](https://pkg.go.dev/builtin#error))
    	// contains filtered or unexported fields
    }

OrganizationIterator manages a stream of *resourcemanagerpb.Organization.

### func (*OrganizationIterator) All 
    
    
    func (it *OrganizationIterator) All() iter.Seq2[*resourcemanagerpb.Organization, error]

All returns an iterator. If an error is returned by the iterator, the iterator will stop after that iteration.

### func (*OrganizationIterator) Next 
    
    
    func (it *OrganizationIterator) Next() (*[resourcemanagerpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb).[Organization](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb#cloud_google_com_go_resourcemanager_apiv3_resourcemanagerpb_Organization), [error](https://pkg.go.dev/builtin#error))

Next returns the next result. Its second return value is iterator.Done if there are no more results. Once Next returns Done, all subsequent calls will return Done.

### func (*OrganizationIterator) PageInfo 
    
    
    func (it *OrganizationIterator) PageInfo() *iterator.PageInfo

PageInfo supports pagination. See the [google.golang.org/api/iterator] package for details.

## OrganizationsCallOptions
    
    
    type OrganizationsCallOptions struct {
    	GetOrganization     []gax.CallOption
    	SearchOrganizations []gax.CallOption
    	GetIamPolicy        []gax.CallOption
    	SetIamPolicy        []gax.CallOption
    	TestIamPermissions  []gax.CallOption
    	GetOperation        []gax.CallOption
    }

OrganizationsCallOptions contains the retry settings for each method of OrganizationsClient.

## OrganizationsClient
    
    
    type OrganizationsClient struct {
    
    	// The call options for this service.
    	CallOptions *OrganizationsCallOptions
    	// contains filtered or unexported fields
    }

OrganizationsClient is a client for interacting with Cloud Resource Manager API. Methods, except Close, may be called concurrently. However, fields must not be modified concurrently with method calls.

Allows users to manage their organization resources.

### func NewOrganizationsClient 
    
    
    func NewOrganizationsClient(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...option.ClientOption) (*OrganizationsClient, [error](https://pkg.go.dev/builtin#error))

NewOrganizationsClient creates a new organizations client based on gRPC. The returned client must be Closed when it is done being used to clean up its underlying connections.

Allows users to manage their organization resources.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	resourcemanager "cloud.google.com/go/resourcemanager/apiv3"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := resourcemanager.NewOrganizationsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	// TODO: Use client.
    	_ = c
    }
    

### func NewOrganizationsRESTClient 
    
    
    func NewOrganizationsRESTClient(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...option.ClientOption) (*OrganizationsClient, [error](https://pkg.go.dev/builtin#error))

NewOrganizationsRESTClient creates a new organizations rest client.

Allows users to manage their organization resources.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	resourcemanager "cloud.google.com/go/resourcemanager/apiv3"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := resourcemanager.[NewOrganizationsRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3.html#cloud_google_com_go_resourcemanager_apiv3_OrganizationsClient_NewOrganizationsRESTClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	// TODO: Use client.
    	_ = c
    }
    

### func (*OrganizationsClient) Close 
    
    
    func (c *OrganizationsClient) Close() [error](https://pkg.go.dev/builtin#error)

Close closes the connection to the API service. **Always** call Close() when the client is no longer required.

### func (*OrganizationsClient) Connection (deprecated)
    
    
    func (c *OrganizationsClient) Connection() *grpc.ClientConn

Connection returns a connection to the API service.

Deprecated: Connections are now pooled so this method does not always return the same resource.

### func (*OrganizationsClient) GetIamPolicy 
    
    
    func (c *OrganizationsClient) GetIamPolicy(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[iampb](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb).[GetIamPolicyRequest](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb#GetIamPolicyRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[iampb](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb).[Policy](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb#Policy), [error](https://pkg.go.dev/builtin#error))

GetIamPolicy gets the access control policy for an organization resource. The policy may be empty if no such policy or resource exists. The resource field should be the organization’s resource name, for example: “organizations/123”.

Authorization requires the IAM permission resourcemanager.organizations.getIamPolicy on the specified organization.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	iampb "cloud.google.com/go/iam/apiv1/iampb"
    
    	resourcemanager "cloud.google.com/go/resourcemanager/apiv3"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := resourcemanager.NewOrganizationsClient(ctx)
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
    

### func (*OrganizationsClient) GetOperation 
    
    
    func (c *OrganizationsClient) GetOperation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[GetOperationRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#GetOperationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[Operation](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#Operation), [error](https://pkg.go.dev/builtin#error))

GetOperation is a utility method from google.longrunning.Operations.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    
    	resourcemanager "cloud.google.com/go/resourcemanager/apiv3"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := resourcemanager.NewOrganizationsClient(ctx)
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
    

### func (*OrganizationsClient) GetOrganization 
    
    
    func (c *OrganizationsClient) GetOrganization(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[resourcemanagerpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb).[GetOrganizationRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb#cloud_google_com_go_resourcemanager_apiv3_resourcemanagerpb_GetOrganizationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[resourcemanagerpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb).[Organization](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb#cloud_google_com_go_resourcemanager_apiv3_resourcemanagerpb_Organization), [error](https://pkg.go.dev/builtin#error))

GetOrganization fetches an organization resource identified by the specified resource name.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	resourcemanager "cloud.google.com/go/resourcemanager/apiv3"
    
    	resourcemanagerpb "cloud.google.com/go/resourcemanager/apiv3/resourcemanagerpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := resourcemanager.NewOrganizationsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &resourcemanagerpb.GetOrganizationRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/resourcemanager/apiv3/resourcemanagerpb#GetOrganizationRequest.
    	}
    	resp, err := c.GetOrganization(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*OrganizationsClient) SearchOrganizations 
    
    
    func (c *OrganizationsClient) SearchOrganizations(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[resourcemanagerpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb).[SearchOrganizationsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb#cloud_google_com_go_resourcemanager_apiv3_resourcemanagerpb_SearchOrganizationsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *OrganizationIterator

SearchOrganizations searches organization resources that are visible to the user and satisfy the specified filter. This method returns organizations in an unspecified order. New organizations do not necessarily appear at the end of the results, and may take a small amount of time to appear.

Search will only return organizations on which the user has the permission resourcemanager.organizations.get

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	resourcemanager "cloud.google.com/go/resourcemanager/apiv3"
    
    	resourcemanagerpb "cloud.google.com/go/resourcemanager/apiv3/resourcemanagerpb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := resourcemanager.NewOrganizationsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &resourcemanagerpb.SearchOrganizationsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/resourcemanager/apiv3/resourcemanagerpb#SearchOrganizationsRequest.
    	}
    	it := c.SearchOrganizations(ctx, req)
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
    		_ = it.Response.(*resourcemanagerpb.SearchOrganizationsResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	resourcemanager "cloud.google.com/go/resourcemanager/apiv3"
    	resourcemanagerpb "cloud.google.com/go/resourcemanager/apiv3/resourcemanagerpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := resourcemanager.NewOrganizationsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &resourcemanagerpb.SearchOrganizationsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/resourcemanager/apiv3/resourcemanagerpb#SearchOrganizationsRequest.
    	}
    	for resp, err := range c.SearchOrganizations(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*OrganizationsClient) SetIamPolicy 
    
    
    func (c *OrganizationsClient) SetIamPolicy(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[iampb](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb).[SetIamPolicyRequest](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb#SetIamPolicyRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[iampb](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb).[Policy](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb#Policy), [error](https://pkg.go.dev/builtin#error))

SetIamPolicy sets the access control policy on an organization resource. Replaces any existing policy. The resource field should be the organization’s resource name, for example: “organizations/123”.

Authorization requires the IAM permission resourcemanager.organizations.setIamPolicy on the specified organization.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	iampb "cloud.google.com/go/iam/apiv1/iampb"
    
    	resourcemanager "cloud.google.com/go/resourcemanager/apiv3"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := resourcemanager.NewOrganizationsClient(ctx)
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
    

### func (*OrganizationsClient) TestIamPermissions 
    
    
    func (c *OrganizationsClient) TestIamPermissions(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[iampb](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb).[TestIamPermissionsRequest](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb#TestIamPermissionsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[iampb](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb).[TestIamPermissionsResponse](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb#TestIamPermissionsResponse), [error](https://pkg.go.dev/builtin#error))

TestIamPermissions returns the permissions that a caller has on the specified organization. The resource field should be the organization’s resource name, for example: “organizations/123”.

There are no permissions required for making this API call.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	iampb "cloud.google.com/go/iam/apiv1/iampb"
    
    	resourcemanager "cloud.google.com/go/resourcemanager/apiv3"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := resourcemanager.NewOrganizationsClient(ctx)
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
    

## ProjectIterator
    
    
    type ProjectIterator struct {
    
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
    	InternalFetch func(pageSize [int](https://pkg.go.dev/builtin#int), pageToken [string](https://pkg.go.dev/builtin#string)) (results []*resourcemanagerpb.Project, nextPageToken [string](https://pkg.go.dev/builtin#string), err [error](https://pkg.go.dev/builtin#error))
    	// contains filtered or unexported fields
    }

ProjectIterator manages a stream of *resourcemanagerpb.Project.

### func (*ProjectIterator) All 
    
    
    func (it *ProjectIterator) All() iter.Seq2[*resourcemanagerpb.Project, error]

All returns an iterator. If an error is returned by the iterator, the iterator will stop after that iteration.

### func (*ProjectIterator) Next 
    
    
    func (it *ProjectIterator) Next() (*[resourcemanagerpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb).[Project](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb#cloud_google_com_go_resourcemanager_apiv3_resourcemanagerpb_Project), [error](https://pkg.go.dev/builtin#error))

Next returns the next result. Its second return value is iterator.Done if there are no more results. Once Next returns Done, all subsequent calls will return Done.

### func (*ProjectIterator) PageInfo 
    
    
    func (it *ProjectIterator) PageInfo() *iterator.PageInfo

PageInfo supports pagination. See the [google.golang.org/api/iterator] package for details.

## ProjectsCallOptions
    
    
    type ProjectsCallOptions struct {
    	GetProject         []gax.CallOption
    	ListProjects       []gax.CallOption
    	SearchProjects     []gax.CallOption
    	CreateProject      []gax.CallOption
    	UpdateProject      []gax.CallOption
    	MoveProject        []gax.CallOption
    	DeleteProject      []gax.CallOption
    	UndeleteProject    []gax.CallOption
    	GetIamPolicy       []gax.CallOption
    	SetIamPolicy       []gax.CallOption
    	TestIamPermissions []gax.CallOption
    	GetOperation       []gax.CallOption
    }

ProjectsCallOptions contains the retry settings for each method of ProjectsClient.

## ProjectsClient
    
    
    type ProjectsClient struct {
    
    	// The call options for this service.
    	CallOptions *ProjectsCallOptions
    
    	// LROClient is used internally to handle long-running operations.
    	// It is exposed so that its CallOptions can be modified if required.
    	// Users should not Close this client.
    	LROClient *lroauto.OperationsClient
    	// contains filtered or unexported fields
    }

ProjectsClient is a client for interacting with Cloud Resource Manager API. Methods, except Close, may be called concurrently. However, fields must not be modified concurrently with method calls.

Manages Google Cloud Projects.

### func NewProjectsClient 
    
    
    func NewProjectsClient(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...option.ClientOption) (*ProjectsClient, [error](https://pkg.go.dev/builtin#error))

NewProjectsClient creates a new projects client based on gRPC. The returned client must be Closed when it is done being used to clean up its underlying connections.

Manages Google Cloud Projects.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	resourcemanager "cloud.google.com/go/resourcemanager/apiv3"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := resourcemanager.NewProjectsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	// TODO: Use client.
    	_ = c
    }
    

### func NewProjectsRESTClient 
    
    
    func NewProjectsRESTClient(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...option.ClientOption) (*ProjectsClient, [error](https://pkg.go.dev/builtin#error))

NewProjectsRESTClient creates a new projects rest client.

Manages Google Cloud Projects.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	resourcemanager "cloud.google.com/go/resourcemanager/apiv3"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := resourcemanager.[NewProjectsRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3.html#cloud_google_com_go_resourcemanager_apiv3_ProjectsClient_NewProjectsRESTClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	// TODO: Use client.
    	_ = c
    }
    

### func (*ProjectsClient) Close 
    
    
    func (c *ProjectsClient) Close() [error](https://pkg.go.dev/builtin#error)

Close closes the connection to the API service. **Always** call Close() when the client is no longer required.

### func (*ProjectsClient) Connection (deprecated)
    
    
    func (c *ProjectsClient) Connection() *grpc.ClientConn

Connection returns a connection to the API service.

Deprecated: Connections are now pooled so this method does not always return the same resource.

### func (*ProjectsClient) CreateProject 
    
    
    func (c *ProjectsClient) CreateProject(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[resourcemanagerpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb).[CreateProjectRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb#cloud_google_com_go_resourcemanager_apiv3_resourcemanagerpb_CreateProjectRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*CreateProjectOperation, [error](https://pkg.go.dev/builtin#error))

CreateProject request that a new project be created. The result is an Operation which can be used to track the creation process. This process usually takes a few seconds, but can sometimes take much longer. The tracking Operation is automatically deleted after a few hours, so there is no need to call DeleteOperation.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	resourcemanager "cloud.google.com/go/resourcemanager/apiv3"
    
    	resourcemanagerpb "cloud.google.com/go/resourcemanager/apiv3/resourcemanagerpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := resourcemanager.NewProjectsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &resourcemanagerpb.CreateProjectRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/resourcemanager/apiv3/resourcemanagerpb#CreateProjectRequest.
    	}
    	op, err := c.CreateProject(ctx, req)
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
    

### func (*ProjectsClient) CreateProjectOperation 
    
    
    func (c *ProjectsClient) CreateProjectOperation(name [string](https://pkg.go.dev/builtin#string)) *CreateProjectOperation

CreateProjectOperation returns a new CreateProjectOperation from a given name. The name must be that of a previously created CreateProjectOperation, possibly from a different process.

### func (*ProjectsClient) DeleteProject 
    
    
    func (c *ProjectsClient) DeleteProject(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[resourcemanagerpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb).[DeleteProjectRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb#cloud_google_com_go_resourcemanager_apiv3_resourcemanagerpb_DeleteProjectRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*DeleteProjectOperation, [error](https://pkg.go.dev/builtin#error))

DeleteProject marks the project identified by the specified name (for example, projects/415104041262) for deletion.

This method will only affect the project if it has a lifecycle state of [ACTIVE][google.cloud.resourcemanager.v3.Project.State.ACTIVE (at <http://google.cloud.resourcemanager.v3.Project.State.ACTIVE>)].

This method changes the Project’s lifecycle state from [ACTIVE][google.cloud.resourcemanager.v3.Project.State.ACTIVE (at <http://google.cloud.resourcemanager.v3.Project.State.ACTIVE>)] to DELETE_REQUESTED. The deletion starts at an unspecified time, at which point the Project is no longer accessible.

Until the deletion completes, you can check the lifecycle state checked by retrieving the project with [GetProject] [google.cloud.resourcemanager.v3.Projects.GetProject], and the project remains visible to [ListProjects] [google.cloud.resourcemanager.v3.Projects.ListProjects]. However, you cannot update the project.

After the deletion completes, the project is not retrievable by the [GetProject] [google.cloud.resourcemanager.v3.Projects.GetProject], [ListProjects] [google.cloud.resourcemanager.v3.Projects.ListProjects], and SearchProjects methods.

This method behaves idempotently, such that deleting a DELETE_REQUESTED project will not cause an error, but also won’t do anything.

The caller must have resourcemanager.projects.delete permissions for this project.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	resourcemanager "cloud.google.com/go/resourcemanager/apiv3"
    
    	resourcemanagerpb "cloud.google.com/go/resourcemanager/apiv3/resourcemanagerpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := resourcemanager.NewProjectsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &resourcemanagerpb.DeleteProjectRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/resourcemanager/apiv3/resourcemanagerpb#DeleteProjectRequest.
    	}
    	op, err := c.DeleteProject(ctx, req)
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
    

### func (*ProjectsClient) DeleteProjectOperation 
    
    
    func (c *ProjectsClient) DeleteProjectOperation(name [string](https://pkg.go.dev/builtin#string)) *DeleteProjectOperation

DeleteProjectOperation returns a new DeleteProjectOperation from a given name. The name must be that of a previously created DeleteProjectOperation, possibly from a different process.

### func (*ProjectsClient) GetIamPolicy 
    
    
    func (c *ProjectsClient) GetIamPolicy(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[iampb](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb).[GetIamPolicyRequest](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb#GetIamPolicyRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[iampb](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb).[Policy](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb#Policy), [error](https://pkg.go.dev/builtin#error))

GetIamPolicy returns the IAM access control policy for the specified project, in the format projects/{ProjectIdOrNumber} e.g. projects/123. Permission is denied if the policy or the resource do not exist.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	iampb "cloud.google.com/go/iam/apiv1/iampb"
    
    	resourcemanager "cloud.google.com/go/resourcemanager/apiv3"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := resourcemanager.NewProjectsClient(ctx)
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
    

### func (*ProjectsClient) GetOperation 
    
    
    func (c *ProjectsClient) GetOperation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[GetOperationRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#GetOperationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[Operation](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#Operation), [error](https://pkg.go.dev/builtin#error))

GetOperation is a utility method from google.longrunning.Operations.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    
    	resourcemanager "cloud.google.com/go/resourcemanager/apiv3"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := resourcemanager.NewProjectsClient(ctx)
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
    

### func (*ProjectsClient) GetProject 
    
    
    func (c *ProjectsClient) GetProject(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[resourcemanagerpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb).[GetProjectRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb#cloud_google_com_go_resourcemanager_apiv3_resourcemanagerpb_GetProjectRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[resourcemanagerpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb).[Project](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb#cloud_google_com_go_resourcemanager_apiv3_resourcemanagerpb_Project), [error](https://pkg.go.dev/builtin#error))

GetProject retrieves the project identified by the specified name (for example, projects/415104041262).

The caller must have resourcemanager.projects.get permission for this project.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	resourcemanager "cloud.google.com/go/resourcemanager/apiv3"
    
    	resourcemanagerpb "cloud.google.com/go/resourcemanager/apiv3/resourcemanagerpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := resourcemanager.NewProjectsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &resourcemanagerpb.GetProjectRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/resourcemanager/apiv3/resourcemanagerpb#GetProjectRequest.
    	}
    	resp, err := c.GetProject(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*ProjectsClient) ListProjects 
    
    
    func (c *ProjectsClient) ListProjects(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[resourcemanagerpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb).[ListProjectsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb#cloud_google_com_go_resourcemanager_apiv3_resourcemanagerpb_ListProjectsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *ProjectIterator

ListProjects lists projects that are direct children of the specified folder or organization resource. list() provides a strongly consistent view of the projects underneath the specified parent resource. list() returns projects sorted based upon the (ascending) lexical ordering of their display_name. The caller must have resourcemanager.projects.list permission on the identified parent.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	resourcemanager "cloud.google.com/go/resourcemanager/apiv3"
    
    	resourcemanagerpb "cloud.google.com/go/resourcemanager/apiv3/resourcemanagerpb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := resourcemanager.NewProjectsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &resourcemanagerpb.ListProjectsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/resourcemanager/apiv3/resourcemanagerpb#ListProjectsRequest.
    	}
    	it := c.ListProjects(ctx, req)
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
    		_ = it.Response.(*resourcemanagerpb.ListProjectsResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	resourcemanager "cloud.google.com/go/resourcemanager/apiv3"
    	resourcemanagerpb "cloud.google.com/go/resourcemanager/apiv3/resourcemanagerpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := resourcemanager.NewProjectsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &resourcemanagerpb.ListProjectsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/resourcemanager/apiv3/resourcemanagerpb#ListProjectsRequest.
    	}
    	for resp, err := range c.ListProjects(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*ProjectsClient) MoveProject 
    
    
    func (c *ProjectsClient) MoveProject(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[resourcemanagerpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb).[MoveProjectRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb#cloud_google_com_go_resourcemanager_apiv3_resourcemanagerpb_MoveProjectRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*MoveProjectOperation, [error](https://pkg.go.dev/builtin#error))

MoveProject move a project to another place in your resource hierarchy, under a new resource parent.

Returns an operation which can be used to track the process of the project move workflow. Upon success, the Operation.response field will be populated with the moved project.

The caller must have resourcemanager.projects.move permission on the project, on the project’s current and proposed new parent.

If project has no current parent, or it currently does not have an associated organization resource, you will also need the resourcemanager.projects.setIamPolicy permission in the project.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	resourcemanager "cloud.google.com/go/resourcemanager/apiv3"
    
    	resourcemanagerpb "cloud.google.com/go/resourcemanager/apiv3/resourcemanagerpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := resourcemanager.NewProjectsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &resourcemanagerpb.MoveProjectRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/resourcemanager/apiv3/resourcemanagerpb#MoveProjectRequest.
    	}
    	op, err := c.MoveProject(ctx, req)
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
    

### func (*ProjectsClient) MoveProjectOperation 
    
    
    func (c *ProjectsClient) MoveProjectOperation(name [string](https://pkg.go.dev/builtin#string)) *MoveProjectOperation

MoveProjectOperation returns a new MoveProjectOperation from a given name. The name must be that of a previously created MoveProjectOperation, possibly from a different process.

### func (*ProjectsClient) SearchProjects 
    
    
    func (c *ProjectsClient) SearchProjects(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[resourcemanagerpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb).[SearchProjectsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb#cloud_google_com_go_resourcemanager_apiv3_resourcemanagerpb_SearchProjectsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *ProjectIterator

SearchProjects search for projects that the caller has both resourcemanager.projects.get permission on, and also satisfy the specified query.

This method returns projects in an unspecified order.

This method is eventually consistent with project mutations; this means that a newly created project may not appear in the results or recent updates to an existing project may not be reflected in the results. To retrieve the latest state of a project, use the GetProject method.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	resourcemanager "cloud.google.com/go/resourcemanager/apiv3"
    
    	resourcemanagerpb "cloud.google.com/go/resourcemanager/apiv3/resourcemanagerpb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := resourcemanager.NewProjectsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &resourcemanagerpb.SearchProjectsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/resourcemanager/apiv3/resourcemanagerpb#SearchProjectsRequest.
    	}
    	it := c.SearchProjects(ctx, req)
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
    		_ = it.Response.(*resourcemanagerpb.SearchProjectsResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	resourcemanager "cloud.google.com/go/resourcemanager/apiv3"
    	resourcemanagerpb "cloud.google.com/go/resourcemanager/apiv3/resourcemanagerpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := resourcemanager.NewProjectsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &resourcemanagerpb.SearchProjectsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/resourcemanager/apiv3/resourcemanagerpb#SearchProjectsRequest.
    	}
    	for resp, err := range c.SearchProjects(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*ProjectsClient) SetIamPolicy 
    
    
    func (c *ProjectsClient) SetIamPolicy(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[iampb](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb).[SetIamPolicyRequest](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb#SetIamPolicyRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[iampb](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb).[Policy](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb#Policy), [error](https://pkg.go.dev/builtin#error))

SetIamPolicy sets the IAM access control policy for the specified project, in the format projects/{ProjectIdOrNumber} e.g. projects/123.

CAUTION: This method will replace the existing policy, and cannot be used to append additional IAM settings.

Note: Removing service accounts from policies or changing their roles can render services completely inoperable. It is important to understand how the service account is being used before removing or updating its roles.

The following constraints apply when using setIamPolicy():
    
    
    Project does not support allUsers and allAuthenticatedUsers as
    members in a Binding of a Policy.
    
    The owner role can be granted to a user, serviceAccount, or a group
    that is part of an organization. For example,
    group@myownpersonaldomain.com (at mailto:group@myownpersonaldomain.com) could be added as an owner to a project in
    the myownpersonaldomain.com (at http://myownpersonaldomain.com) organization, but not the examplepetstore.com (at http://examplepetstore.com)
    organization.
    
    Service accounts can be made owners of a project directly
    without any restrictions. However, to be added as an owner, a user must be
    invited using the Cloud Platform console and must accept the invitation.
    
    A user cannot be granted the owner role using setIamPolicy(). The user
    must be granted the owner role using the Cloud Platform Console and must
    explicitly accept the invitation.
    
    Invitations to grant the owner role cannot be sent using
    setIamPolicy();
    they must be sent only using the Cloud Platform Console.
    
    If the project is not part of an organization, there must be at least
    one owner who has accepted the Terms of Service (ToS) agreement in the
    policy. Calling setIamPolicy() to remove the last ToS-accepted owner
    from the policy will fail. This restriction also applies to legacy
    projects that no longer have owners who have accepted the ToS. Edits to
    IAM policies will be rejected until the lack of a ToS-accepting owner is
    rectified. If the project is part of an organization, you can remove all
    owners, potentially making the organization inaccessible.
    

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	iampb "cloud.google.com/go/iam/apiv1/iampb"
    
    	resourcemanager "cloud.google.com/go/resourcemanager/apiv3"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := resourcemanager.NewProjectsClient(ctx)
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
    

### func (*ProjectsClient) TestIamPermissions 
    
    
    func (c *ProjectsClient) TestIamPermissions(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[iampb](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb).[TestIamPermissionsRequest](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb#TestIamPermissionsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[iampb](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb).[TestIamPermissionsResponse](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb#TestIamPermissionsResponse), [error](https://pkg.go.dev/builtin#error))

TestIamPermissions returns permissions that a caller has on the specified project, in the format projects/{ProjectIdOrNumber} e.g. projects/123…

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	iampb "cloud.google.com/go/iam/apiv1/iampb"
    
    	resourcemanager "cloud.google.com/go/resourcemanager/apiv3"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := resourcemanager.NewProjectsClient(ctx)
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
    

### func (*ProjectsClient) UndeleteProject 
    
    
    func (c *ProjectsClient) UndeleteProject(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[resourcemanagerpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb).[UndeleteProjectRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb#cloud_google_com_go_resourcemanager_apiv3_resourcemanagerpb_UndeleteProjectRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*UndeleteProjectOperation, [error](https://pkg.go.dev/builtin#error))

UndeleteProject restores the project identified by the specified name (for example, projects/415104041262). You can only use this method for a project that has a lifecycle state of [DELETE_REQUESTED] [Projects.State.DELETE_REQUESTED]. After deletion starts, the project cannot be restored.

The caller must have resourcemanager.projects.undelete permission for this project.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	resourcemanager "cloud.google.com/go/resourcemanager/apiv3"
    
    	resourcemanagerpb "cloud.google.com/go/resourcemanager/apiv3/resourcemanagerpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := resourcemanager.NewProjectsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &resourcemanagerpb.UndeleteProjectRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/resourcemanager/apiv3/resourcemanagerpb#UndeleteProjectRequest.
    	}
    	op, err := c.UndeleteProject(ctx, req)
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
    

### func (*ProjectsClient) UndeleteProjectOperation 
    
    
    func (c *ProjectsClient) UndeleteProjectOperation(name [string](https://pkg.go.dev/builtin#string)) *UndeleteProjectOperation

UndeleteProjectOperation returns a new UndeleteProjectOperation from a given name. The name must be that of a previously created UndeleteProjectOperation, possibly from a different process.

### func (*ProjectsClient) UpdateProject 
    
    
    func (c *ProjectsClient) UpdateProject(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[resourcemanagerpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb).[UpdateProjectRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb#cloud_google_com_go_resourcemanager_apiv3_resourcemanagerpb_UpdateProjectRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*UpdateProjectOperation, [error](https://pkg.go.dev/builtin#error))

UpdateProject updates the display_name and labels of the project identified by the specified name (for example, projects/415104041262). Deleting all labels requires an update mask for labels field.

The caller must have resourcemanager.projects.update permission for this project.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	resourcemanager "cloud.google.com/go/resourcemanager/apiv3"
    
    	resourcemanagerpb "cloud.google.com/go/resourcemanager/apiv3/resourcemanagerpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := resourcemanager.NewProjectsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &resourcemanagerpb.UpdateProjectRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/resourcemanager/apiv3/resourcemanagerpb#UpdateProjectRequest.
    	}
    	op, err := c.UpdateProject(ctx, req)
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
    

### func (*ProjectsClient) UpdateProjectOperation 
    
    
    func (c *ProjectsClient) UpdateProjectOperation(name [string](https://pkg.go.dev/builtin#string)) *UpdateProjectOperation

UpdateProjectOperation returns a new UpdateProjectOperation from a given name. The name must be that of a previously created UpdateProjectOperation, possibly from a different process.

## TagBindingIterator
    
    
    type TagBindingIterator struct {
    
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
    	InternalFetch func(pageSize [int](https://pkg.go.dev/builtin#int), pageToken [string](https://pkg.go.dev/builtin#string)) (results []*resourcemanagerpb.TagBinding, nextPageToken [string](https://pkg.go.dev/builtin#string), err [error](https://pkg.go.dev/builtin#error))
    	// contains filtered or unexported fields
    }

TagBindingIterator manages a stream of *resourcemanagerpb.TagBinding.

### func (*TagBindingIterator) All 
    
    
    func (it *TagBindingIterator) All() iter.Seq2[*resourcemanagerpb.TagBinding, error]

All returns an iterator. If an error is returned by the iterator, the iterator will stop after that iteration.

### func (*TagBindingIterator) Next 
    
    
    func (it *TagBindingIterator) Next() (*[resourcemanagerpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb).[TagBinding](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb#cloud_google_com_go_resourcemanager_apiv3_resourcemanagerpb_TagBinding), [error](https://pkg.go.dev/builtin#error))

Next returns the next result. Its second return value is iterator.Done if there are no more results. Once Next returns Done, all subsequent calls will return Done.

### func (*TagBindingIterator) PageInfo 
    
    
    func (it *TagBindingIterator) PageInfo() *iterator.PageInfo

PageInfo supports pagination. See the [google.golang.org/api/iterator] package for details.

## TagBindingsCallOptions
    
    
    type TagBindingsCallOptions struct {
    	ListTagBindings   []gax.CallOption
    	CreateTagBinding  []gax.CallOption
    	DeleteTagBinding  []gax.CallOption
    	ListEffectiveTags []gax.CallOption
    	GetOperation      []gax.CallOption
    }

TagBindingsCallOptions contains the retry settings for each method of TagBindingsClient.

## TagBindingsClient
    
    
    type TagBindingsClient struct {
    
    	// The call options for this service.
    	CallOptions *TagBindingsCallOptions
    
    	// LROClient is used internally to handle long-running operations.
    	// It is exposed so that its CallOptions can be modified if required.
    	// Users should not Close this client.
    	LROClient *lroauto.OperationsClient
    	// contains filtered or unexported fields
    }

TagBindingsClient is a client for interacting with Cloud Resource Manager API. Methods, except Close, may be called concurrently. However, fields must not be modified concurrently with method calls.

Allow users to create and manage TagBindings between TagValues and different Google Cloud resources throughout the GCP resource hierarchy.

### func NewTagBindingsClient 
    
    
    func NewTagBindingsClient(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...option.ClientOption) (*TagBindingsClient, [error](https://pkg.go.dev/builtin#error))

NewTagBindingsClient creates a new tag bindings client based on gRPC. The returned client must be Closed when it is done being used to clean up its underlying connections.

Allow users to create and manage TagBindings between TagValues and different Google Cloud resources throughout the GCP resource hierarchy.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	resourcemanager "cloud.google.com/go/resourcemanager/apiv3"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := resourcemanager.NewTagBindingsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	// TODO: Use client.
    	_ = c
    }
    

### func NewTagBindingsRESTClient 
    
    
    func NewTagBindingsRESTClient(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...option.ClientOption) (*TagBindingsClient, [error](https://pkg.go.dev/builtin#error))

NewTagBindingsRESTClient creates a new tag bindings rest client.

Allow users to create and manage TagBindings between TagValues and different Google Cloud resources throughout the GCP resource hierarchy.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	resourcemanager "cloud.google.com/go/resourcemanager/apiv3"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := resourcemanager.[NewTagBindingsRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3.html#cloud_google_com_go_resourcemanager_apiv3_TagBindingsClient_NewTagBindingsRESTClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	// TODO: Use client.
    	_ = c
    }
    

### func (*TagBindingsClient) Close 
    
    
    func (c *TagBindingsClient) Close() [error](https://pkg.go.dev/builtin#error)

Close closes the connection to the API service. **Always** call Close() when the client is no longer required.

### func (*TagBindingsClient) Connection (deprecated)
    
    
    func (c *TagBindingsClient) Connection() *grpc.ClientConn

Connection returns a connection to the API service.

Deprecated: Connections are now pooled so this method does not always return the same resource.

### func (*TagBindingsClient) CreateTagBinding 
    
    
    func (c *TagBindingsClient) CreateTagBinding(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[resourcemanagerpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb).[CreateTagBindingRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb#cloud_google_com_go_resourcemanager_apiv3_resourcemanagerpb_CreateTagBindingRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*CreateTagBindingOperation, [error](https://pkg.go.dev/builtin#error))

CreateTagBinding creates a TagBinding between a TagValue and a Google Cloud resource.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	resourcemanager "cloud.google.com/go/resourcemanager/apiv3"
    
    	resourcemanagerpb "cloud.google.com/go/resourcemanager/apiv3/resourcemanagerpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := resourcemanager.NewTagBindingsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &resourcemanagerpb.CreateTagBindingRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/resourcemanager/apiv3/resourcemanagerpb#CreateTagBindingRequest.
    	}
    	op, err := c.CreateTagBinding(ctx, req)
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
    

### func (*TagBindingsClient) CreateTagBindingOperation 
    
    
    func (c *TagBindingsClient) CreateTagBindingOperation(name [string](https://pkg.go.dev/builtin#string)) *CreateTagBindingOperation

CreateTagBindingOperation returns a new CreateTagBindingOperation from a given name. The name must be that of a previously created CreateTagBindingOperation, possibly from a different process.

### func (*TagBindingsClient) DeleteTagBinding 
    
    
    func (c *TagBindingsClient) DeleteTagBinding(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[resourcemanagerpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb).[DeleteTagBindingRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb#cloud_google_com_go_resourcemanager_apiv3_resourcemanagerpb_DeleteTagBindingRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*DeleteTagBindingOperation, [error](https://pkg.go.dev/builtin#error))

DeleteTagBinding deletes a TagBinding.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	resourcemanager "cloud.google.com/go/resourcemanager/apiv3"
    
    	resourcemanagerpb "cloud.google.com/go/resourcemanager/apiv3/resourcemanagerpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := resourcemanager.NewTagBindingsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &resourcemanagerpb.DeleteTagBindingRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/resourcemanager/apiv3/resourcemanagerpb#DeleteTagBindingRequest.
    	}
    	op, err := c.DeleteTagBinding(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    
    	err = op.Wait(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    }
    

### func (*TagBindingsClient) DeleteTagBindingOperation 
    
    
    func (c *TagBindingsClient) DeleteTagBindingOperation(name [string](https://pkg.go.dev/builtin#string)) *DeleteTagBindingOperation

DeleteTagBindingOperation returns a new DeleteTagBindingOperation from a given name. The name must be that of a previously created DeleteTagBindingOperation, possibly from a different process.

### func (*TagBindingsClient) GetOperation 
    
    
    func (c *TagBindingsClient) GetOperation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[GetOperationRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#GetOperationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[Operation](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#Operation), [error](https://pkg.go.dev/builtin#error))

GetOperation is a utility method from google.longrunning.Operations.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    	resourcemanager "cloud.google.com/go/resourcemanager/apiv3"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := resourcemanager.NewTagBindingsClient(ctx)
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
    

### func (*TagBindingsClient) ListEffectiveTags 
    
    
    func (c *TagBindingsClient) ListEffectiveTags(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[resourcemanagerpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb).[ListEffectiveTagsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb#cloud_google_com_go_resourcemanager_apiv3_resourcemanagerpb_ListEffectiveTagsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *EffectiveTagIterator

ListEffectiveTags return a list of effective tags for the given Google Cloud resource, as specified in parent.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	resourcemanager "cloud.google.com/go/resourcemanager/apiv3"
    
    	resourcemanagerpb "cloud.google.com/go/resourcemanager/apiv3/resourcemanagerpb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := resourcemanager.NewTagBindingsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &resourcemanagerpb.ListEffectiveTagsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/resourcemanager/apiv3/resourcemanagerpb#ListEffectiveTagsRequest.
    	}
    	it := c.ListEffectiveTags(ctx, req)
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
    		_ = it.Response.(*resourcemanagerpb.ListEffectiveTagsResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	resourcemanager "cloud.google.com/go/resourcemanager/apiv3"
    	resourcemanagerpb "cloud.google.com/go/resourcemanager/apiv3/resourcemanagerpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := resourcemanager.NewTagBindingsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &resourcemanagerpb.ListEffectiveTagsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/resourcemanager/apiv3/resourcemanagerpb#ListEffectiveTagsRequest.
    	}
    	for resp, err := range c.ListEffectiveTags(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*TagBindingsClient) ListTagBindings 
    
    
    func (c *TagBindingsClient) ListTagBindings(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[resourcemanagerpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb).[ListTagBindingsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb#cloud_google_com_go_resourcemanager_apiv3_resourcemanagerpb_ListTagBindingsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *TagBindingIterator

ListTagBindings lists the TagBindings for the given Google Cloud resource, as specified with parent.

NOTE: The parent field is expected to be a full resource name: <https://cloud.google.com/apis/design/resource_names#full_resource_name> (at <https://cloud.google.com/apis/design/resource_names#full_resource_name>)

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	resourcemanager "cloud.google.com/go/resourcemanager/apiv3"
    
    	resourcemanagerpb "cloud.google.com/go/resourcemanager/apiv3/resourcemanagerpb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := resourcemanager.NewTagBindingsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &resourcemanagerpb.ListTagBindingsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/resourcemanager/apiv3/resourcemanagerpb#ListTagBindingsRequest.
    	}
    	it := c.ListTagBindings(ctx, req)
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
    		_ = it.Response.(*resourcemanagerpb.ListTagBindingsResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	resourcemanager "cloud.google.com/go/resourcemanager/apiv3"
    	resourcemanagerpb "cloud.google.com/go/resourcemanager/apiv3/resourcemanagerpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := resourcemanager.NewTagBindingsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &resourcemanagerpb.ListTagBindingsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/resourcemanager/apiv3/resourcemanagerpb#ListTagBindingsRequest.
    	}
    	for resp, err := range c.ListTagBindings(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

## TagHoldIterator
    
    
    type TagHoldIterator struct {
    
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
    	InternalFetch func(pageSize [int](https://pkg.go.dev/builtin#int), pageToken [string](https://pkg.go.dev/builtin#string)) (results []*resourcemanagerpb.TagHold, nextPageToken [string](https://pkg.go.dev/builtin#string), err [error](https://pkg.go.dev/builtin#error))
    	// contains filtered or unexported fields
    }

TagHoldIterator manages a stream of *resourcemanagerpb.TagHold.

### func (*TagHoldIterator) All 
    
    
    func (it *TagHoldIterator) All() iter.Seq2[*resourcemanagerpb.TagHold, error]

All returns an iterator. If an error is returned by the iterator, the iterator will stop after that iteration.

### func (*TagHoldIterator) Next 
    
    
    func (it *TagHoldIterator) Next() (*[resourcemanagerpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb).[TagHold](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb#cloud_google_com_go_resourcemanager_apiv3_resourcemanagerpb_TagHold), [error](https://pkg.go.dev/builtin#error))

Next returns the next result. Its second return value is iterator.Done if there are no more results. Once Next returns Done, all subsequent calls will return Done.

### func (*TagHoldIterator) PageInfo 
    
    
    func (it *TagHoldIterator) PageInfo() *iterator.PageInfo

PageInfo supports pagination. See the [google.golang.org/api/iterator] package for details.

## TagHoldsCallOptions
    
    
    type TagHoldsCallOptions struct {
    	CreateTagHold []gax.CallOption
    	DeleteTagHold []gax.CallOption
    	ListTagHolds  []gax.CallOption
    	GetOperation  []gax.CallOption
    }

TagHoldsCallOptions contains the retry settings for each method of TagHoldsClient.

## TagHoldsClient
    
    
    type TagHoldsClient struct {
    
    	// The call options for this service.
    	CallOptions *TagHoldsCallOptions
    
    	// LROClient is used internally to handle long-running operations.
    	// It is exposed so that its CallOptions can be modified if required.
    	// Users should not Close this client.
    	LROClient *lroauto.OperationsClient
    	// contains filtered or unexported fields
    }

TagHoldsClient is a client for interacting with Cloud Resource Manager API. Methods, except Close, may be called concurrently. However, fields must not be modified concurrently with method calls.

Allow users to create and manage TagHolds for TagValues. TagHolds represent the use of a Tag Value that is not captured by TagBindings but should still block TagValue deletion (such as a reference in a policy condition). This service provides isolated failure domains by cloud location so that TagHolds can be managed in the same location as their usage.

### func NewTagHoldsClient 
    
    
    func NewTagHoldsClient(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...option.ClientOption) (*TagHoldsClient, [error](https://pkg.go.dev/builtin#error))

NewTagHoldsClient creates a new tag holds client based on gRPC. The returned client must be Closed when it is done being used to clean up its underlying connections.

Allow users to create and manage TagHolds for TagValues. TagHolds represent the use of a Tag Value that is not captured by TagBindings but should still block TagValue deletion (such as a reference in a policy condition). This service provides isolated failure domains by cloud location so that TagHolds can be managed in the same location as their usage.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	resourcemanager "cloud.google.com/go/resourcemanager/apiv3"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := resourcemanager.NewTagHoldsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	// TODO: Use client.
    	_ = c
    }
    

### func NewTagHoldsRESTClient 
    
    
    func NewTagHoldsRESTClient(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...option.ClientOption) (*TagHoldsClient, [error](https://pkg.go.dev/builtin#error))

NewTagHoldsRESTClient creates a new tag holds rest client.

Allow users to create and manage TagHolds for TagValues. TagHolds represent the use of a Tag Value that is not captured by TagBindings but should still block TagValue deletion (such as a reference in a policy condition). This service provides isolated failure domains by cloud location so that TagHolds can be managed in the same location as their usage.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	resourcemanager "cloud.google.com/go/resourcemanager/apiv3"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := resourcemanager.[NewTagHoldsRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3.html#cloud_google_com_go_resourcemanager_apiv3_TagHoldsClient_NewTagHoldsRESTClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	// TODO: Use client.
    	_ = c
    }
    

### func (*TagHoldsClient) Close 
    
    
    func (c *TagHoldsClient) Close() [error](https://pkg.go.dev/builtin#error)

Close closes the connection to the API service. **Always** call Close() when the client is no longer required.

### func (*TagHoldsClient) Connection (deprecated)
    
    
    func (c *TagHoldsClient) Connection() *grpc.ClientConn

Connection returns a connection to the API service.

Deprecated: Connections are now pooled so this method does not always return the same resource.

### func (*TagHoldsClient) CreateTagHold 
    
    
    func (c *TagHoldsClient) CreateTagHold(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[resourcemanagerpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb).[CreateTagHoldRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb#cloud_google_com_go_resourcemanager_apiv3_resourcemanagerpb_CreateTagHoldRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*CreateTagHoldOperation, [error](https://pkg.go.dev/builtin#error))

CreateTagHold creates a TagHold. Returns ALREADY_EXISTS if a TagHold with the same resource and origin exists under the same TagValue.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	resourcemanager "cloud.google.com/go/resourcemanager/apiv3"
    
    	resourcemanagerpb "cloud.google.com/go/resourcemanager/apiv3/resourcemanagerpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := resourcemanager.NewTagHoldsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &resourcemanagerpb.CreateTagHoldRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/resourcemanager/apiv3/resourcemanagerpb#CreateTagHoldRequest.
    	}
    	op, err := c.CreateTagHold(ctx, req)
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
    

### func (*TagHoldsClient) CreateTagHoldOperation 
    
    
    func (c *TagHoldsClient) CreateTagHoldOperation(name [string](https://pkg.go.dev/builtin#string)) *CreateTagHoldOperation

CreateTagHoldOperation returns a new CreateTagHoldOperation from a given name. The name must be that of a previously created CreateTagHoldOperation, possibly from a different process.

### func (*TagHoldsClient) DeleteTagHold 
    
    
    func (c *TagHoldsClient) DeleteTagHold(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[resourcemanagerpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb).[DeleteTagHoldRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb#cloud_google_com_go_resourcemanager_apiv3_resourcemanagerpb_DeleteTagHoldRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*DeleteTagHoldOperation, [error](https://pkg.go.dev/builtin#error))

DeleteTagHold deletes a TagHold.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	resourcemanager "cloud.google.com/go/resourcemanager/apiv3"
    
    	resourcemanagerpb "cloud.google.com/go/resourcemanager/apiv3/resourcemanagerpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := resourcemanager.NewTagHoldsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &resourcemanagerpb.DeleteTagHoldRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/resourcemanager/apiv3/resourcemanagerpb#DeleteTagHoldRequest.
    	}
    	op, err := c.DeleteTagHold(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    
    	err = op.Wait(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    }
    

### func (*TagHoldsClient) DeleteTagHoldOperation 
    
    
    func (c *TagHoldsClient) DeleteTagHoldOperation(name [string](https://pkg.go.dev/builtin#string)) *DeleteTagHoldOperation

DeleteTagHoldOperation returns a new DeleteTagHoldOperation from a given name. The name must be that of a previously created DeleteTagHoldOperation, possibly from a different process.

### func (*TagHoldsClient) GetOperation 
    
    
    func (c *TagHoldsClient) GetOperation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[GetOperationRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#GetOperationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[Operation](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#Operation), [error](https://pkg.go.dev/builtin#error))

GetOperation is a utility method from google.longrunning.Operations.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    	resourcemanager "cloud.google.com/go/resourcemanager/apiv3"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := resourcemanager.NewTagHoldsClient(ctx)
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
    

### func (*TagHoldsClient) ListTagHolds 
    
    
    func (c *TagHoldsClient) ListTagHolds(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[resourcemanagerpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb).[ListTagHoldsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb#cloud_google_com_go_resourcemanager_apiv3_resourcemanagerpb_ListTagHoldsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *TagHoldIterator

ListTagHolds lists TagHolds under a TagValue.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	resourcemanager "cloud.google.com/go/resourcemanager/apiv3"
    
    	resourcemanagerpb "cloud.google.com/go/resourcemanager/apiv3/resourcemanagerpb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := resourcemanager.NewTagHoldsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &resourcemanagerpb.ListTagHoldsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/resourcemanager/apiv3/resourcemanagerpb#ListTagHoldsRequest.
    	}
    	it := c.ListTagHolds(ctx, req)
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
    		_ = it.Response.(*resourcemanagerpb.ListTagHoldsResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	resourcemanager "cloud.google.com/go/resourcemanager/apiv3"
    	resourcemanagerpb "cloud.google.com/go/resourcemanager/apiv3/resourcemanagerpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := resourcemanager.NewTagHoldsClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &resourcemanagerpb.ListTagHoldsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/resourcemanager/apiv3/resourcemanagerpb#ListTagHoldsRequest.
    	}
    	for resp, err := range c.ListTagHolds(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

## TagKeyIterator
    
    
    type TagKeyIterator struct {
    
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
    	InternalFetch func(pageSize [int](https://pkg.go.dev/builtin#int), pageToken [string](https://pkg.go.dev/builtin#string)) (results []*resourcemanagerpb.TagKey, nextPageToken [string](https://pkg.go.dev/builtin#string), err [error](https://pkg.go.dev/builtin#error))
    	// contains filtered or unexported fields
    }

TagKeyIterator manages a stream of *resourcemanagerpb.TagKey.

### func (*TagKeyIterator) All 
    
    
    func (it *TagKeyIterator) All() iter.Seq2[*resourcemanagerpb.TagKey, error]

All returns an iterator. If an error is returned by the iterator, the iterator will stop after that iteration.

### func (*TagKeyIterator) Next 
    
    
    func (it *TagKeyIterator) Next() (*[resourcemanagerpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb).[TagKey](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb#cloud_google_com_go_resourcemanager_apiv3_resourcemanagerpb_TagKey), [error](https://pkg.go.dev/builtin#error))

Next returns the next result. Its second return value is iterator.Done if there are no more results. Once Next returns Done, all subsequent calls will return Done.

### func (*TagKeyIterator) PageInfo 
    
    
    func (it *TagKeyIterator) PageInfo() *iterator.PageInfo

PageInfo supports pagination. See the [google.golang.org/api/iterator] package for details.

## TagKeysCallOptions
    
    
    type TagKeysCallOptions struct {
    	ListTagKeys         []gax.CallOption
    	GetTagKey           []gax.CallOption
    	GetNamespacedTagKey []gax.CallOption
    	CreateTagKey        []gax.CallOption
    	UpdateTagKey        []gax.CallOption
    	DeleteTagKey        []gax.CallOption
    	GetIamPolicy        []gax.CallOption
    	SetIamPolicy        []gax.CallOption
    	TestIamPermissions  []gax.CallOption
    	GetOperation        []gax.CallOption
    }

TagKeysCallOptions contains the retry settings for each method of TagKeysClient.

## TagKeysClient
    
    
    type TagKeysClient struct {
    
    	// The call options for this service.
    	CallOptions *TagKeysCallOptions
    
    	// LROClient is used internally to handle long-running operations.
    	// It is exposed so that its CallOptions can be modified if required.
    	// Users should not Close this client.
    	LROClient *lroauto.OperationsClient
    	// contains filtered or unexported fields
    }

TagKeysClient is a client for interacting with Cloud Resource Manager API. Methods, except Close, may be called concurrently. However, fields must not be modified concurrently with method calls.

Allow users to create and manage tag keys.

### func NewTagKeysClient 
    
    
    func NewTagKeysClient(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...option.ClientOption) (*TagKeysClient, [error](https://pkg.go.dev/builtin#error))

NewTagKeysClient creates a new tag keys client based on gRPC. The returned client must be Closed when it is done being used to clean up its underlying connections.

Allow users to create and manage tag keys.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	resourcemanager "cloud.google.com/go/resourcemanager/apiv3"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := resourcemanager.NewTagKeysClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	// TODO: Use client.
    	_ = c
    }
    

### func NewTagKeysRESTClient 
    
    
    func NewTagKeysRESTClient(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...option.ClientOption) (*TagKeysClient, [error](https://pkg.go.dev/builtin#error))

NewTagKeysRESTClient creates a new tag keys rest client.

Allow users to create and manage tag keys.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	resourcemanager "cloud.google.com/go/resourcemanager/apiv3"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := resourcemanager.[NewTagKeysRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3.html#cloud_google_com_go_resourcemanager_apiv3_TagKeysClient_NewTagKeysRESTClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	// TODO: Use client.
    	_ = c
    }
    

### func (*TagKeysClient) Close 
    
    
    func (c *TagKeysClient) Close() [error](https://pkg.go.dev/builtin#error)

Close closes the connection to the API service. **Always** call Close() when the client is no longer required.

### func (*TagKeysClient) Connection (deprecated)
    
    
    func (c *TagKeysClient) Connection() *grpc.ClientConn

Connection returns a connection to the API service.

Deprecated: Connections are now pooled so this method does not always return the same resource.

### func (*TagKeysClient) CreateTagKey 
    
    
    func (c *TagKeysClient) CreateTagKey(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[resourcemanagerpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb).[CreateTagKeyRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb#cloud_google_com_go_resourcemanager_apiv3_resourcemanagerpb_CreateTagKeyRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*CreateTagKeyOperation, [error](https://pkg.go.dev/builtin#error))

CreateTagKey creates a new TagKey. If another request with the same parameters is sent while the original request is in process, the second request will receive an error. A maximum of 1000 TagKeys can exist under a parent at any given time.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	resourcemanager "cloud.google.com/go/resourcemanager/apiv3"
    
    	resourcemanagerpb "cloud.google.com/go/resourcemanager/apiv3/resourcemanagerpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := resourcemanager.NewTagKeysClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &resourcemanagerpb.CreateTagKeyRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/resourcemanager/apiv3/resourcemanagerpb#CreateTagKeyRequest.
    	}
    	op, err := c.CreateTagKey(ctx, req)
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
    

### func (*TagKeysClient) CreateTagKeyOperation 
    
    
    func (c *TagKeysClient) CreateTagKeyOperation(name [string](https://pkg.go.dev/builtin#string)) *CreateTagKeyOperation

CreateTagKeyOperation returns a new CreateTagKeyOperation from a given name. The name must be that of a previously created CreateTagKeyOperation, possibly from a different process.

### func (*TagKeysClient) DeleteTagKey 
    
    
    func (c *TagKeysClient) DeleteTagKey(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[resourcemanagerpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb).[DeleteTagKeyRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb#cloud_google_com_go_resourcemanager_apiv3_resourcemanagerpb_DeleteTagKeyRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*DeleteTagKeyOperation, [error](https://pkg.go.dev/builtin#error))

DeleteTagKey deletes a TagKey. The TagKey cannot be deleted if it has any child TagValues.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	resourcemanager "cloud.google.com/go/resourcemanager/apiv3"
    
    	resourcemanagerpb "cloud.google.com/go/resourcemanager/apiv3/resourcemanagerpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := resourcemanager.NewTagKeysClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &resourcemanagerpb.DeleteTagKeyRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/resourcemanager/apiv3/resourcemanagerpb#DeleteTagKeyRequest.
    	}
    	op, err := c.DeleteTagKey(ctx, req)
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
    

### func (*TagKeysClient) DeleteTagKeyOperation 
    
    
    func (c *TagKeysClient) DeleteTagKeyOperation(name [string](https://pkg.go.dev/builtin#string)) *DeleteTagKeyOperation

DeleteTagKeyOperation returns a new DeleteTagKeyOperation from a given name. The name must be that of a previously created DeleteTagKeyOperation, possibly from a different process.

### func (*TagKeysClient) GetIamPolicy 
    
    
    func (c *TagKeysClient) GetIamPolicy(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[iampb](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb).[GetIamPolicyRequest](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb#GetIamPolicyRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[iampb](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb).[Policy](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb#Policy), [error](https://pkg.go.dev/builtin#error))

GetIamPolicy gets the access control policy for a TagKey. The returned policy may be empty if no such policy or resource exists. The resource field should be the TagKey’s resource name. For example, “tagKeys/1234”. The caller must have cloudresourcemanager.googleapis.com/tagKeys.getIamPolicy permission on the specified TagKey.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	iampb "cloud.google.com/go/iam/apiv1/iampb"
    
    	resourcemanager "cloud.google.com/go/resourcemanager/apiv3"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := resourcemanager.NewTagKeysClient(ctx)
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
    

### func (*TagKeysClient) GetNamespacedTagKey 
    
    
    func (c *TagKeysClient) GetNamespacedTagKey(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[resourcemanagerpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb).[GetNamespacedTagKeyRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb#cloud_google_com_go_resourcemanager_apiv3_resourcemanagerpb_GetNamespacedTagKeyRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[resourcemanagerpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb).[TagKey](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb#cloud_google_com_go_resourcemanager_apiv3_resourcemanagerpb_TagKey), [error](https://pkg.go.dev/builtin#error))

GetNamespacedTagKey retrieves a TagKey by its namespaced name. This method will return PERMISSION_DENIED if the key does not exist or the user does not have permission to view it.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	resourcemanager "cloud.google.com/go/resourcemanager/apiv3"
    
    	resourcemanagerpb "cloud.google.com/go/resourcemanager/apiv3/resourcemanagerpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := resourcemanager.NewTagKeysClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &resourcemanagerpb.GetNamespacedTagKeyRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/resourcemanager/apiv3/resourcemanagerpb#GetNamespacedTagKeyRequest.
    	}
    	resp, err := c.GetNamespacedTagKey(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*TagKeysClient) GetOperation 
    
    
    func (c *TagKeysClient) GetOperation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[GetOperationRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#GetOperationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[Operation](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#Operation), [error](https://pkg.go.dev/builtin#error))

GetOperation is a utility method from google.longrunning.Operations.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    
    	resourcemanager "cloud.google.com/go/resourcemanager/apiv3"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := resourcemanager.NewTagKeysClient(ctx)
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
    

### func (*TagKeysClient) GetTagKey 
    
    
    func (c *TagKeysClient) GetTagKey(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[resourcemanagerpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb).[GetTagKeyRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb#cloud_google_com_go_resourcemanager_apiv3_resourcemanagerpb_GetTagKeyRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[resourcemanagerpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb).[TagKey](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb#cloud_google_com_go_resourcemanager_apiv3_resourcemanagerpb_TagKey), [error](https://pkg.go.dev/builtin#error))

GetTagKey retrieves a TagKey. This method will return PERMISSION_DENIED if the key does not exist or the user does not have permission to view it.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	resourcemanager "cloud.google.com/go/resourcemanager/apiv3"
    
    	resourcemanagerpb "cloud.google.com/go/resourcemanager/apiv3/resourcemanagerpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := resourcemanager.NewTagKeysClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &resourcemanagerpb.GetTagKeyRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/resourcemanager/apiv3/resourcemanagerpb#GetTagKeyRequest.
    	}
    	resp, err := c.GetTagKey(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*TagKeysClient) ListTagKeys 
    
    
    func (c *TagKeysClient) ListTagKeys(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[resourcemanagerpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb).[ListTagKeysRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb#cloud_google_com_go_resourcemanager_apiv3_resourcemanagerpb_ListTagKeysRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *TagKeyIterator

ListTagKeys lists all TagKeys for a parent resource.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	resourcemanager "cloud.google.com/go/resourcemanager/apiv3"
    
    	resourcemanagerpb "cloud.google.com/go/resourcemanager/apiv3/resourcemanagerpb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := resourcemanager.NewTagKeysClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &resourcemanagerpb.ListTagKeysRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/resourcemanager/apiv3/resourcemanagerpb#ListTagKeysRequest.
    	}
    	it := c.ListTagKeys(ctx, req)
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
    		_ = it.Response.(*resourcemanagerpb.ListTagKeysResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	resourcemanager "cloud.google.com/go/resourcemanager/apiv3"
    	resourcemanagerpb "cloud.google.com/go/resourcemanager/apiv3/resourcemanagerpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := resourcemanager.NewTagKeysClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &resourcemanagerpb.ListTagKeysRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/resourcemanager/apiv3/resourcemanagerpb#ListTagKeysRequest.
    	}
    	for resp, err := range c.ListTagKeys(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*TagKeysClient) SetIamPolicy 
    
    
    func (c *TagKeysClient) SetIamPolicy(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[iampb](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb).[SetIamPolicyRequest](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb#SetIamPolicyRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[iampb](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb).[Policy](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb#Policy), [error](https://pkg.go.dev/builtin#error))

SetIamPolicy sets the access control policy on a TagKey, replacing any existing policy. The resource field should be the TagKey’s resource name. For example, “tagKeys/1234”. The caller must have resourcemanager.tagKeys.setIamPolicy permission on the identified tagValue.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	iampb "cloud.google.com/go/iam/apiv1/iampb"
    
    	resourcemanager "cloud.google.com/go/resourcemanager/apiv3"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := resourcemanager.NewTagKeysClient(ctx)
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
    

### func (*TagKeysClient) TestIamPermissions 
    
    
    func (c *TagKeysClient) TestIamPermissions(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[iampb](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb).[TestIamPermissionsRequest](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb#TestIamPermissionsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[iampb](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb).[TestIamPermissionsResponse](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb#TestIamPermissionsResponse), [error](https://pkg.go.dev/builtin#error))

TestIamPermissions returns permissions that a caller has on the specified TagKey. The resource field should be the TagKey’s resource name. For example, “tagKeys/1234”.

There are no permissions required for making this API call.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	iampb "cloud.google.com/go/iam/apiv1/iampb"
    
    	resourcemanager "cloud.google.com/go/resourcemanager/apiv3"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := resourcemanager.NewTagKeysClient(ctx)
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
    

### func (*TagKeysClient) UpdateTagKey 
    
    
    func (c *TagKeysClient) UpdateTagKey(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[resourcemanagerpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb).[UpdateTagKeyRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb#cloud_google_com_go_resourcemanager_apiv3_resourcemanagerpb_UpdateTagKeyRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*UpdateTagKeyOperation, [error](https://pkg.go.dev/builtin#error))

UpdateTagKey updates the attributes of the TagKey resource.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	resourcemanager "cloud.google.com/go/resourcemanager/apiv3"
    
    	resourcemanagerpb "cloud.google.com/go/resourcemanager/apiv3/resourcemanagerpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := resourcemanager.NewTagKeysClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &resourcemanagerpb.UpdateTagKeyRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/resourcemanager/apiv3/resourcemanagerpb#UpdateTagKeyRequest.
    	}
    	op, err := c.UpdateTagKey(ctx, req)
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
    

### func (*TagKeysClient) UpdateTagKeyOperation 
    
    
    func (c *TagKeysClient) UpdateTagKeyOperation(name [string](https://pkg.go.dev/builtin#string)) *UpdateTagKeyOperation

UpdateTagKeyOperation returns a new UpdateTagKeyOperation from a given name. The name must be that of a previously created UpdateTagKeyOperation, possibly from a different process.

## TagValueIterator
    
    
    type TagValueIterator struct {
    
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
    	InternalFetch func(pageSize [int](https://pkg.go.dev/builtin#int), pageToken [string](https://pkg.go.dev/builtin#string)) (results []*resourcemanagerpb.TagValue, nextPageToken [string](https://pkg.go.dev/builtin#string), err [error](https://pkg.go.dev/builtin#error))
    	// contains filtered or unexported fields
    }

TagValueIterator manages a stream of *resourcemanagerpb.TagValue.

### func (*TagValueIterator) All 
    
    
    func (it *TagValueIterator) All() iter.Seq2[*resourcemanagerpb.TagValue, error]

All returns an iterator. If an error is returned by the iterator, the iterator will stop after that iteration.

### func (*TagValueIterator) Next 
    
    
    func (it *TagValueIterator) Next() (*[resourcemanagerpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb).[TagValue](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb#cloud_google_com_go_resourcemanager_apiv3_resourcemanagerpb_TagValue), [error](https://pkg.go.dev/builtin#error))

Next returns the next result. Its second return value is iterator.Done if there are no more results. Once Next returns Done, all subsequent calls will return Done.

### func (*TagValueIterator) PageInfo 
    
    
    func (it *TagValueIterator) PageInfo() *iterator.PageInfo

PageInfo supports pagination. See the [google.golang.org/api/iterator] package for details.

## TagValuesCallOptions
    
    
    type TagValuesCallOptions struct {
    	ListTagValues         []gax.CallOption
    	GetTagValue           []gax.CallOption
    	GetNamespacedTagValue []gax.CallOption
    	CreateTagValue        []gax.CallOption
    	UpdateTagValue        []gax.CallOption
    	DeleteTagValue        []gax.CallOption
    	GetIamPolicy          []gax.CallOption
    	SetIamPolicy          []gax.CallOption
    	TestIamPermissions    []gax.CallOption
    	GetOperation          []gax.CallOption
    }

TagValuesCallOptions contains the retry settings for each method of TagValuesClient.

## TagValuesClient
    
    
    type TagValuesClient struct {
    
    	// The call options for this service.
    	CallOptions *TagValuesCallOptions
    
    	// LROClient is used internally to handle long-running operations.
    	// It is exposed so that its CallOptions can be modified if required.
    	// Users should not Close this client.
    	LROClient *lroauto.OperationsClient
    	// contains filtered or unexported fields
    }

TagValuesClient is a client for interacting with Cloud Resource Manager API. Methods, except Close, may be called concurrently. However, fields must not be modified concurrently with method calls.

Allow users to create and manage tag values.

### func NewTagValuesClient 
    
    
    func NewTagValuesClient(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...option.ClientOption) (*TagValuesClient, [error](https://pkg.go.dev/builtin#error))

NewTagValuesClient creates a new tag values client based on gRPC. The returned client must be Closed when it is done being used to clean up its underlying connections.

Allow users to create and manage tag values.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	resourcemanager "cloud.google.com/go/resourcemanager/apiv3"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := resourcemanager.NewTagValuesClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	// TODO: Use client.
    	_ = c
    }
    

### func NewTagValuesRESTClient 
    
    
    func NewTagValuesRESTClient(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...option.ClientOption) (*TagValuesClient, [error](https://pkg.go.dev/builtin#error))

NewTagValuesRESTClient creates a new tag values rest client.

Allow users to create and manage tag values.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	resourcemanager "cloud.google.com/go/resourcemanager/apiv3"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := resourcemanager.[NewTagValuesRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3.html#cloud_google_com_go_resourcemanager_apiv3_TagValuesClient_NewTagValuesRESTClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	// TODO: Use client.
    	_ = c
    }
    

### func (*TagValuesClient) Close 
    
    
    func (c *TagValuesClient) Close() [error](https://pkg.go.dev/builtin#error)

Close closes the connection to the API service. **Always** call Close() when the client is no longer required.

### func (*TagValuesClient) Connection (deprecated)
    
    
    func (c *TagValuesClient) Connection() *grpc.ClientConn

Connection returns a connection to the API service.

Deprecated: Connections are now pooled so this method does not always return the same resource.

### func (*TagValuesClient) CreateTagValue 
    
    
    func (c *TagValuesClient) CreateTagValue(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[resourcemanagerpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb).[CreateTagValueRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb#cloud_google_com_go_resourcemanager_apiv3_resourcemanagerpb_CreateTagValueRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*CreateTagValueOperation, [error](https://pkg.go.dev/builtin#error))

CreateTagValue creates a TagValue as a child of the specified TagKey. If a another request with the same parameters is sent while the original request is in process the second request will receive an error. A maximum of 1000 TagValues can exist under a TagKey at any given time.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	resourcemanager "cloud.google.com/go/resourcemanager/apiv3"
    
    	resourcemanagerpb "cloud.google.com/go/resourcemanager/apiv3/resourcemanagerpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := resourcemanager.NewTagValuesClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &resourcemanagerpb.CreateTagValueRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/resourcemanager/apiv3/resourcemanagerpb#CreateTagValueRequest.
    	}
    	op, err := c.CreateTagValue(ctx, req)
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
    

### func (*TagValuesClient) CreateTagValueOperation 
    
    
    func (c *TagValuesClient) CreateTagValueOperation(name [string](https://pkg.go.dev/builtin#string)) *CreateTagValueOperation

CreateTagValueOperation returns a new CreateTagValueOperation from a given name. The name must be that of a previously created CreateTagValueOperation, possibly from a different process.

### func (*TagValuesClient) DeleteTagValue 
    
    
    func (c *TagValuesClient) DeleteTagValue(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[resourcemanagerpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb).[DeleteTagValueRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb#cloud_google_com_go_resourcemanager_apiv3_resourcemanagerpb_DeleteTagValueRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*DeleteTagValueOperation, [error](https://pkg.go.dev/builtin#error))

DeleteTagValue deletes a TagValue. The TagValue cannot have any bindings when it is deleted.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	resourcemanager "cloud.google.com/go/resourcemanager/apiv3"
    
    	resourcemanagerpb "cloud.google.com/go/resourcemanager/apiv3/resourcemanagerpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := resourcemanager.NewTagValuesClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &resourcemanagerpb.DeleteTagValueRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/resourcemanager/apiv3/resourcemanagerpb#DeleteTagValueRequest.
    	}
    	op, err := c.DeleteTagValue(ctx, req)
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
    

### func (*TagValuesClient) DeleteTagValueOperation 
    
    
    func (c *TagValuesClient) DeleteTagValueOperation(name [string](https://pkg.go.dev/builtin#string)) *DeleteTagValueOperation

DeleteTagValueOperation returns a new DeleteTagValueOperation from a given name. The name must be that of a previously created DeleteTagValueOperation, possibly from a different process.

### func (*TagValuesClient) GetIamPolicy 
    
    
    func (c *TagValuesClient) GetIamPolicy(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[iampb](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb).[GetIamPolicyRequest](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb#GetIamPolicyRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[iampb](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb).[Policy](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb#Policy), [error](https://pkg.go.dev/builtin#error))

GetIamPolicy gets the access control policy for a TagValue. The returned policy may be empty if no such policy or resource exists. The resource field should be the TagValue’s resource name. For example: tagValues/1234. The caller must have the cloudresourcemanager.googleapis.com/tagValues.getIamPolicy permission on the identified TagValue to get the access control policy.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	iampb "cloud.google.com/go/iam/apiv1/iampb"
    
    	resourcemanager "cloud.google.com/go/resourcemanager/apiv3"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := resourcemanager.NewTagValuesClient(ctx)
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
    

### func (*TagValuesClient) GetNamespacedTagValue 
    
    
    func (c *TagValuesClient) GetNamespacedTagValue(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[resourcemanagerpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb).[GetNamespacedTagValueRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb#cloud_google_com_go_resourcemanager_apiv3_resourcemanagerpb_GetNamespacedTagValueRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[resourcemanagerpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb).[TagValue](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb#cloud_google_com_go_resourcemanager_apiv3_resourcemanagerpb_TagValue), [error](https://pkg.go.dev/builtin#error))

GetNamespacedTagValue retrieves a TagValue by its namespaced name. This method will return PERMISSION_DENIED if the value does not exist or the user does not have permission to view it.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	resourcemanager "cloud.google.com/go/resourcemanager/apiv3"
    
    	resourcemanagerpb "cloud.google.com/go/resourcemanager/apiv3/resourcemanagerpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := resourcemanager.NewTagValuesClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &resourcemanagerpb.GetNamespacedTagValueRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/resourcemanager/apiv3/resourcemanagerpb#GetNamespacedTagValueRequest.
    	}
    	resp, err := c.GetNamespacedTagValue(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*TagValuesClient) GetOperation 
    
    
    func (c *TagValuesClient) GetOperation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[GetOperationRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#GetOperationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[Operation](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#Operation), [error](https://pkg.go.dev/builtin#error))

GetOperation is a utility method from google.longrunning.Operations.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    
    	resourcemanager "cloud.google.com/go/resourcemanager/apiv3"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := resourcemanager.NewTagValuesClient(ctx)
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
    

### func (*TagValuesClient) GetTagValue 
    
    
    func (c *TagValuesClient) GetTagValue(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[resourcemanagerpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb).[GetTagValueRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb#cloud_google_com_go_resourcemanager_apiv3_resourcemanagerpb_GetTagValueRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[resourcemanagerpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb).[TagValue](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb#cloud_google_com_go_resourcemanager_apiv3_resourcemanagerpb_TagValue), [error](https://pkg.go.dev/builtin#error))

GetTagValue retrieves a TagValue. This method will return PERMISSION_DENIED if the value does not exist or the user does not have permission to view it.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	resourcemanager "cloud.google.com/go/resourcemanager/apiv3"
    
    	resourcemanagerpb "cloud.google.com/go/resourcemanager/apiv3/resourcemanagerpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := resourcemanager.NewTagValuesClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &resourcemanagerpb.GetTagValueRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/resourcemanager/apiv3/resourcemanagerpb#GetTagValueRequest.
    	}
    	resp, err := c.GetTagValue(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*TagValuesClient) ListTagValues 
    
    
    func (c *TagValuesClient) ListTagValues(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[resourcemanagerpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb).[ListTagValuesRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb#cloud_google_com_go_resourcemanager_apiv3_resourcemanagerpb_ListTagValuesRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *TagValueIterator

ListTagValues lists all TagValues for a specific TagKey.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	resourcemanager "cloud.google.com/go/resourcemanager/apiv3"
    
    	resourcemanagerpb "cloud.google.com/go/resourcemanager/apiv3/resourcemanagerpb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := resourcemanager.NewTagValuesClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &resourcemanagerpb.ListTagValuesRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/resourcemanager/apiv3/resourcemanagerpb#ListTagValuesRequest.
    	}
    	it := c.ListTagValues(ctx, req)
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
    		_ = it.Response.(*resourcemanagerpb.ListTagValuesResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	resourcemanager "cloud.google.com/go/resourcemanager/apiv3"
    	resourcemanagerpb "cloud.google.com/go/resourcemanager/apiv3/resourcemanagerpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := resourcemanager.NewTagValuesClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &resourcemanagerpb.ListTagValuesRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/resourcemanager/apiv3/resourcemanagerpb#ListTagValuesRequest.
    	}
    	for resp, err := range c.ListTagValues(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*TagValuesClient) SetIamPolicy 
    
    
    func (c *TagValuesClient) SetIamPolicy(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[iampb](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb).[SetIamPolicyRequest](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb#SetIamPolicyRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[iampb](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb).[Policy](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb#Policy), [error](https://pkg.go.dev/builtin#error))

SetIamPolicy sets the access control policy on a TagValue, replacing any existing policy. The resource field should be the TagValue’s resource name. For example: tagValues/1234. The caller must have resourcemanager.tagValues.setIamPolicy permission on the identified tagValue.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	iampb "cloud.google.com/go/iam/apiv1/iampb"
    
    	resourcemanager "cloud.google.com/go/resourcemanager/apiv3"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := resourcemanager.NewTagValuesClient(ctx)
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
    

### func (*TagValuesClient) TestIamPermissions 
    
    
    func (c *TagValuesClient) TestIamPermissions(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[iampb](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb).[TestIamPermissionsRequest](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb#TestIamPermissionsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[iampb](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb).[TestIamPermissionsResponse](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb#TestIamPermissionsResponse), [error](https://pkg.go.dev/builtin#error))

TestIamPermissions returns permissions that a caller has on the specified TagValue. The resource field should be the TagValue’s resource name. For example: tagValues/1234.

There are no permissions required for making this API call.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	iampb "cloud.google.com/go/iam/apiv1/iampb"
    
    	resourcemanager "cloud.google.com/go/resourcemanager/apiv3"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := resourcemanager.NewTagValuesClient(ctx)
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
    

### func (*TagValuesClient) UpdateTagValue 
    
    
    func (c *TagValuesClient) UpdateTagValue(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[resourcemanagerpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb).[UpdateTagValueRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb#cloud_google_com_go_resourcemanager_apiv3_resourcemanagerpb_UpdateTagValueRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*UpdateTagValueOperation, [error](https://pkg.go.dev/builtin#error))

UpdateTagValue updates the attributes of the TagValue resource.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	resourcemanager "cloud.google.com/go/resourcemanager/apiv3"
    
    	resourcemanagerpb "cloud.google.com/go/resourcemanager/apiv3/resourcemanagerpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := resourcemanager.NewTagValuesClient(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &resourcemanagerpb.UpdateTagValueRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/resourcemanager/apiv3/resourcemanagerpb#UpdateTagValueRequest.
    	}
    	op, err := c.UpdateTagValue(ctx, req)
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
    

### func (*TagValuesClient) UpdateTagValueOperation 
    
    
    func (c *TagValuesClient) UpdateTagValueOperation(name [string](https://pkg.go.dev/builtin#string)) *UpdateTagValueOperation

UpdateTagValueOperation returns a new UpdateTagValueOperation from a given name. The name must be that of a previously created UpdateTagValueOperation, possibly from a different process.

## UndeleteFolderOperation
    
    
    type UndeleteFolderOperation struct {
    	// contains filtered or unexported fields
    }

UndeleteFolderOperation manages a long-running operation from UndeleteFolder.

### func (*UndeleteFolderOperation) Done 
    
    
    func (op *UndeleteFolderOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*UndeleteFolderOperation) Metadata 
    
    
    func (op *UndeleteFolderOperation) Metadata() (*[resourcemanagerpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb).[UndeleteFolderMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb#cloud_google_com_go_resourcemanager_apiv3_resourcemanagerpb_UndeleteFolderMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*UndeleteFolderOperation) Name 
    
    
    func (op *UndeleteFolderOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*UndeleteFolderOperation) Poll 
    
    
    func (op *UndeleteFolderOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[resourcemanagerpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb).[Folder](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb#cloud_google_com_go_resourcemanager_apiv3_resourcemanagerpb_Folder), [error](https://pkg.go.dev/builtin#error))

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*UndeleteFolderOperation) Wait 
    
    
    func (op *UndeleteFolderOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[resourcemanagerpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb).[Folder](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb#cloud_google_com_go_resourcemanager_apiv3_resourcemanagerpb_Folder), [error](https://pkg.go.dev/builtin#error))

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## UndeleteProjectOperation
    
    
    type UndeleteProjectOperation struct {
    	// contains filtered or unexported fields
    }

UndeleteProjectOperation manages a long-running operation from UndeleteProject.

### func (*UndeleteProjectOperation) Done 
    
    
    func (op *UndeleteProjectOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*UndeleteProjectOperation) Metadata 
    
    
    func (op *UndeleteProjectOperation) Metadata() (*[resourcemanagerpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb).[UndeleteProjectMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb#cloud_google_com_go_resourcemanager_apiv3_resourcemanagerpb_UndeleteProjectMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*UndeleteProjectOperation) Name 
    
    
    func (op *UndeleteProjectOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*UndeleteProjectOperation) Poll 
    
    
    func (op *UndeleteProjectOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[resourcemanagerpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb).[Project](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb#cloud_google_com_go_resourcemanager_apiv3_resourcemanagerpb_Project), [error](https://pkg.go.dev/builtin#error))

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*UndeleteProjectOperation) Wait 
    
    
    func (op *UndeleteProjectOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[resourcemanagerpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb).[Project](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb#cloud_google_com_go_resourcemanager_apiv3_resourcemanagerpb_Project), [error](https://pkg.go.dev/builtin#error))

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## UpdateFolderOperation
    
    
    type UpdateFolderOperation struct {
    	// contains filtered or unexported fields
    }

UpdateFolderOperation manages a long-running operation from UpdateFolder.

### func (*UpdateFolderOperation) Done 
    
    
    func (op *UpdateFolderOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*UpdateFolderOperation) Metadata 
    
    
    func (op *UpdateFolderOperation) Metadata() (*[resourcemanagerpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb).[UpdateFolderMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb#cloud_google_com_go_resourcemanager_apiv3_resourcemanagerpb_UpdateFolderMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*UpdateFolderOperation) Name 
    
    
    func (op *UpdateFolderOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*UpdateFolderOperation) Poll 
    
    
    func (op *UpdateFolderOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[resourcemanagerpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb).[Folder](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb#cloud_google_com_go_resourcemanager_apiv3_resourcemanagerpb_Folder), [error](https://pkg.go.dev/builtin#error))

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*UpdateFolderOperation) Wait 
    
    
    func (op *UpdateFolderOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[resourcemanagerpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb).[Folder](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb#cloud_google_com_go_resourcemanager_apiv3_resourcemanagerpb_Folder), [error](https://pkg.go.dev/builtin#error))

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## UpdateProjectOperation
    
    
    type UpdateProjectOperation struct {
    	// contains filtered or unexported fields
    }

UpdateProjectOperation manages a long-running operation from UpdateProject.

### func (*UpdateProjectOperation) Done 
    
    
    func (op *UpdateProjectOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*UpdateProjectOperation) Metadata 
    
    
    func (op *UpdateProjectOperation) Metadata() (*[resourcemanagerpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb).[UpdateProjectMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb#cloud_google_com_go_resourcemanager_apiv3_resourcemanagerpb_UpdateProjectMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*UpdateProjectOperation) Name 
    
    
    func (op *UpdateProjectOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*UpdateProjectOperation) Poll 
    
    
    func (op *UpdateProjectOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[resourcemanagerpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb).[Project](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb#cloud_google_com_go_resourcemanager_apiv3_resourcemanagerpb_Project), [error](https://pkg.go.dev/builtin#error))

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*UpdateProjectOperation) Wait 
    
    
    func (op *UpdateProjectOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[resourcemanagerpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb).[Project](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb#cloud_google_com_go_resourcemanager_apiv3_resourcemanagerpb_Project), [error](https://pkg.go.dev/builtin#error))

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## UpdateTagKeyOperation
    
    
    type UpdateTagKeyOperation struct {
    	// contains filtered or unexported fields
    }

UpdateTagKeyOperation manages a long-running operation from UpdateTagKey.

### func (*UpdateTagKeyOperation) Done 
    
    
    func (op *UpdateTagKeyOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*UpdateTagKeyOperation) Metadata 
    
    
    func (op *UpdateTagKeyOperation) Metadata() (*[resourcemanagerpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb).[UpdateTagKeyMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb#cloud_google_com_go_resourcemanager_apiv3_resourcemanagerpb_UpdateTagKeyMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*UpdateTagKeyOperation) Name 
    
    
    func (op *UpdateTagKeyOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*UpdateTagKeyOperation) Poll 
    
    
    func (op *UpdateTagKeyOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[resourcemanagerpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb).[TagKey](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb#cloud_google_com_go_resourcemanager_apiv3_resourcemanagerpb_TagKey), [error](https://pkg.go.dev/builtin#error))

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*UpdateTagKeyOperation) Wait 
    
    
    func (op *UpdateTagKeyOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[resourcemanagerpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb).[TagKey](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb#cloud_google_com_go_resourcemanager_apiv3_resourcemanagerpb_TagKey), [error](https://pkg.go.dev/builtin#error))

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## UpdateTagValueOperation
    
    
    type UpdateTagValueOperation struct {
    	// contains filtered or unexported fields
    }

UpdateTagValueOperation manages a long-running operation from UpdateTagValue.

### func (*UpdateTagValueOperation) Done 
    
    
    func (op *UpdateTagValueOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*UpdateTagValueOperation) Metadata 
    
    
    func (op *UpdateTagValueOperation) Metadata() (*[resourcemanagerpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb).[UpdateTagValueMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb#cloud_google_com_go_resourcemanager_apiv3_resourcemanagerpb_UpdateTagValueMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*UpdateTagValueOperation) Name 
    
    
    func (op *UpdateTagValueOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*UpdateTagValueOperation) Poll 
    
    
    func (op *UpdateTagValueOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[resourcemanagerpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb).[TagValue](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb#cloud_google_com_go_resourcemanager_apiv3_resourcemanagerpb_TagValue), [error](https://pkg.go.dev/builtin#error))

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*UpdateTagValueOperation) Wait 
    
    
    func (op *UpdateTagValueOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[resourcemanagerpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb).[TagValue](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/resourcemanager/latest/apiv3/resourcemanagerpb#cloud_google_com_go_resourcemanager_apiv3_resourcemanagerpb_TagValue), [error](https://pkg.go.dev/builtin#error))

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
