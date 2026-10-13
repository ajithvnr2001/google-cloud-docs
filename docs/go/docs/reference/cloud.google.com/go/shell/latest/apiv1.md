---
url: https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/shell/latest/apiv1/
title: Cloud Shell API v1 - Package cloud.google.com/go/shell/apiv1 (v1.14.0) \u00a0|\u00a0 Go client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:22:30.809506+00:00
---

# Cloud Shell API v1 - Package cloud.google.com/go/shell/apiv1 (v1.14.0)  |  Go client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/shell/latest/apiv1/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Go ](https://docs.cloud.google.com/go/docs)
  * [ Client libraries ](https://docs.cloud.google.com/go/docs/reference)



Send feedback 

#  Cloud Shell API v1 - Package cloud.google.com/go/shell/apiv1 (v1.14.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.14.0 (latest)  1.13.0  1.12.0  1.11.0  1.10.0  1.9.0  1.8.7  1.7.12  1.6.1  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0 

**Note:** To get more information about this package, such as access to older versions, view [this package on pkg.go.dev](https://pkg.go.dev/cloud.google.com/go/shell/apiv1). 

Package shell is an auto-generated package for the Cloud Shell API. 

Allows users to start, configure, and connect to interactive shell sessions running in the cloud. 

## General documentation

For information that is relevant for all client libraries please reference <https://pkg.go.dev/cloud.google.com/go#pkg-overview>. Some information on this page includes: 

  * [Authentication and Authorization](https://pkg.go.dev/cloud.google.com/go#hdr-Authentication_and_Authorization)
  * [Timeouts and Cancellation](https://pkg.go.dev/cloud.google.com/go#hdr-Timeouts_and_Cancellation)
  * [Testing against Client Libraries](https://pkg.go.dev/cloud.google.com/go#hdr-Testing)
  * [Debugging Client Libraries](https://pkg.go.dev/cloud.google.com/go#hdr-Debugging)
  * [Inspecting errors](https://pkg.go.dev/cloud.google.com/go#hdr-Inspecting_errors)



## Example usage

To get started with this package, create a client.
    
    
    // go get cloud.google.com/go/shell/apiv1@latest
    ctx := context.Background()
    // This snippet has been automatically generated and should be regarded as a code template only.
    // It will require modifications to work:
    // - It may require correct/in-range values for request initialization.
    // - It may require specifying regional endpoints when creating the service client as shown in:
    //   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    c, err := shell.NewCloudShellClient(ctx)
    if err != nil {
        // TODO: Handle error.
    }
    defer c.Close()

The client will use your default application credentials. Clients should be reused instead of created as needed. The methods of Client are safe for concurrent use by multiple goroutines. The returned client must be Closed when it is done being used. 

## Using the Client

The following is an example of making an API call with the newly created client, mentioned above.
    
    
    req := &shellpb.AddPublicKeyRequest{
        // TODO: Fill request struct fields.
        // See https://pkg.go.dev/cloud.google.com/go/shell/apiv1/shellpb#AddPublicKeyRequest.
    }
    op, err := c.AddPublicKey(ctx, req)
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

The ctx passed to NewCloudShellClient is used for authentication requests and for creating the underlying connection, but is not used for subsequent calls. Individual methods on the client use the ctx given to them. 

To close the open connection, use the Close() method.

## Functions 

### func DefaultAuthScopes 
    
    
    func DefaultAuthScopes() [][string](https://pkg.go.dev/builtin#string)

DefaultAuthScopes reports the default set of authentication scopes to use with this package.

## AddPublicKeyOperation
    
    
    type AddPublicKeyOperation struct {
    	// contains filtered or unexported fields
    }

AddPublicKeyOperation manages a long-running operation from AddPublicKey.

### func (*AddPublicKeyOperation) Done 
    
    
    func (op *AddPublicKeyOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*AddPublicKeyOperation) Metadata 
    
    
    func (op *AddPublicKeyOperation) Metadata() (*[shellpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/shell/latest/apiv1/shellpb).[AddPublicKeyMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/shell/latest/apiv1/shellpb#cloud_google_com_go_shell_apiv1_shellpb_AddPublicKeyMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*AddPublicKeyOperation) Name 
    
    
    func (op *AddPublicKeyOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*AddPublicKeyOperation) Poll 
    
    
    func (op *AddPublicKeyOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[shellpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/shell/latest/apiv1/shellpb).[AddPublicKeyResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/shell/latest/apiv1/shellpb#cloud_google_com_go_shell_apiv1_shellpb_AddPublicKeyResponse), [error](https://pkg.go.dev/builtin#error))

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*AddPublicKeyOperation) Wait 
    
    
    func (op *AddPublicKeyOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[shellpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/shell/latest/apiv1/shellpb).[AddPublicKeyResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/shell/latest/apiv1/shellpb#cloud_google_com_go_shell_apiv1_shellpb_AddPublicKeyResponse), [error](https://pkg.go.dev/builtin#error))

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## AuthorizeEnvironmentOperation
    
    
    type AuthorizeEnvironmentOperation struct {
    	// contains filtered or unexported fields
    }

AuthorizeEnvironmentOperation manages a long-running operation from AuthorizeEnvironment.

### func (*AuthorizeEnvironmentOperation) Done 
    
    
    func (op *AuthorizeEnvironmentOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*AuthorizeEnvironmentOperation) Metadata 
    
    
    func (op *AuthorizeEnvironmentOperation) Metadata() (*[shellpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/shell/latest/apiv1/shellpb).[AuthorizeEnvironmentMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/shell/latest/apiv1/shellpb#cloud_google_com_go_shell_apiv1_shellpb_AuthorizeEnvironmentMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*AuthorizeEnvironmentOperation) Name 
    
    
    func (op *AuthorizeEnvironmentOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*AuthorizeEnvironmentOperation) Poll 
    
    
    func (op *AuthorizeEnvironmentOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[shellpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/shell/latest/apiv1/shellpb).[AuthorizeEnvironmentResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/shell/latest/apiv1/shellpb#cloud_google_com_go_shell_apiv1_shellpb_AuthorizeEnvironmentResponse), [error](https://pkg.go.dev/builtin#error))

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*AuthorizeEnvironmentOperation) Wait 
    
    
    func (op *AuthorizeEnvironmentOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[shellpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/shell/latest/apiv1/shellpb).[AuthorizeEnvironmentResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/shell/latest/apiv1/shellpb#cloud_google_com_go_shell_apiv1_shellpb_AuthorizeEnvironmentResponse), [error](https://pkg.go.dev/builtin#error))

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## CloudShellCallOptions
    
    
    type CloudShellCallOptions struct {
    	GetEnvironment       []gax.CallOption
    	StartEnvironment     []gax.CallOption
    	AuthorizeEnvironment []gax.CallOption
    	AddPublicKey         []gax.CallOption
    	RemovePublicKey      []gax.CallOption
    }

CloudShellCallOptions contains the retry settings for each method of CloudShellClient.

## CloudShellClient
    
    
    type CloudShellClient struct {
    
    	// The call options for this service.
    	CallOptions *CloudShellCallOptions
    
    	// LROClient is used internally to handle long-running operations.
    	// It is exposed so that its CallOptions can be modified if required.
    	// Users should not Close this client.
    	LROClient *lroauto.OperationsClient
    	// contains filtered or unexported fields
    }

CloudShellClient is a client for interacting with Cloud Shell API. Methods, except Close, may be called concurrently. However, fields must not be modified concurrently with method calls.

API for interacting with Google Cloud Shell. Each user of Cloud Shell has at least one environment, which has the ID “default”. Environment consists of a Docker image defining what is installed on the environment and a home directory containing the user’s data that will remain across sessions. Clients use this API to start and fetch information about their environment, which can then be used to connect to that environment via a separate SSH client.

### func NewCloudShellClient 
    
    
    func NewCloudShellClient(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...option.ClientOption) (*CloudShellClient, [error](https://pkg.go.dev/builtin#error))

NewCloudShellClient creates a new cloud shell service client based on gRPC. The returned client must be Closed when it is done being used to clean up its underlying connections.

API for interacting with Google Cloud Shell. Each user of Cloud Shell has at least one environment, which has the ID “default”. Environment consists of a Docker image defining what is installed on the environment and a home directory containing the user’s data that will remain across sessions. Clients use this API to start and fetch information about their environment, which can then be used to connect to that environment via a separate SSH client.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	shell "cloud.google.com/go/shell/apiv1"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := shell.[NewCloudShellClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/shell/latest/apiv1.html#cloud_google_com_go_shell_apiv1_CloudShellClient_NewCloudShellClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/shell/latest/apiv1.html#cloud_google_com_go_shell_apiv1_CloudShellClient_Close)()
    
    	// TODO: Use client.
    	_ = c
    }
    

### func NewCloudShellRESTClient 
    
    
    func NewCloudShellRESTClient(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...option.ClientOption) (*CloudShellClient, [error](https://pkg.go.dev/builtin#error))

NewCloudShellRESTClient creates a new cloud shell service rest client.

API for interacting with Google Cloud Shell. Each user of Cloud Shell has at least one environment, which has the ID “default”. Environment consists of a Docker image defining what is installed on the environment and a home directory containing the user’s data that will remain across sessions. Clients use this API to start and fetch information about their environment, which can then be used to connect to that environment via a separate SSH client.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	shell "cloud.google.com/go/shell/apiv1"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := shell.[NewCloudShellRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/shell/latest/apiv1.html#cloud_google_com_go_shell_apiv1_CloudShellClient_NewCloudShellRESTClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/shell/latest/apiv1.html#cloud_google_com_go_shell_apiv1_CloudShellClient_Close)()
    
    	// TODO: Use client.
    	_ = c
    }
    

### func (*CloudShellClient) AddPublicKey 
    
    
    func (c *CloudShellClient) AddPublicKey(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[shellpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/shell/latest/apiv1/shellpb).[AddPublicKeyRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/shell/latest/apiv1/shellpb#cloud_google_com_go_shell_apiv1_shellpb_AddPublicKeyRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*AddPublicKeyOperation, [error](https://pkg.go.dev/builtin#error))

AddPublicKey adds a public SSH key to an environment, allowing clients with the corresponding private key to connect to that environment via SSH. If a key with the same content already exists, this will error with ALREADY_EXISTS.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	shell "cloud.google.com/go/shell/apiv1"
    	shellpb "cloud.google.com/go/shell/apiv1/shellpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := shell.[NewCloudShellClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/shell/latest/apiv1.html#cloud_google_com_go_shell_apiv1_CloudShellClient_NewCloudShellClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/shell/latest/apiv1.html#cloud_google_com_go_shell_apiv1_CloudShellClient_Close)()
    
    	req := &shellpb.AddPublicKeyRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/shell/apiv1/shellpb#AddPublicKeyRequest.
    	}
    	op, err := c.AddPublicKey(ctx, req)
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
    

### func (*CloudShellClient) AddPublicKeyOperation 
    
    
    func (c *CloudShellClient) AddPublicKeyOperation(name [string](https://pkg.go.dev/builtin#string)) *AddPublicKeyOperation

AddPublicKeyOperation returns a new AddPublicKeyOperation from a given name. The name must be that of a previously created AddPublicKeyOperation, possibly from a different process.

### func (*CloudShellClient) AuthorizeEnvironment 
    
    
    func (c *CloudShellClient) AuthorizeEnvironment(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[shellpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/shell/latest/apiv1/shellpb).[AuthorizeEnvironmentRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/shell/latest/apiv1/shellpb#cloud_google_com_go_shell_apiv1_shellpb_AuthorizeEnvironmentRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*AuthorizeEnvironmentOperation, [error](https://pkg.go.dev/builtin#error))

AuthorizeEnvironment sends OAuth credentials to a running environment on behalf of a user. When this completes, the environment will be authorized to run various Google Cloud command line tools without requiring the user to manually authenticate.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	shell "cloud.google.com/go/shell/apiv1"
    	shellpb "cloud.google.com/go/shell/apiv1/shellpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := shell.[NewCloudShellClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/shell/latest/apiv1.html#cloud_google_com_go_shell_apiv1_CloudShellClient_NewCloudShellClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/shell/latest/apiv1.html#cloud_google_com_go_shell_apiv1_CloudShellClient_Close)()
    
    	req := &shellpb.AuthorizeEnvironmentRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/shell/apiv1/shellpb#AuthorizeEnvironmentRequest.
    	}
    	op, err := c.AuthorizeEnvironment(ctx, req)
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
    

### func (*CloudShellClient) AuthorizeEnvironmentOperation 
    
    
    func (c *CloudShellClient) AuthorizeEnvironmentOperation(name [string](https://pkg.go.dev/builtin#string)) *AuthorizeEnvironmentOperation

AuthorizeEnvironmentOperation returns a new AuthorizeEnvironmentOperation from a given name. The name must be that of a previously created AuthorizeEnvironmentOperation, possibly from a different process.

### func (*CloudShellClient) Close 
    
    
    func (c *CloudShellClient) Close() [error](https://pkg.go.dev/builtin#error)

Close closes the connection to the API service. **Always** call Close() when the client is no longer required.

### func (*CloudShellClient) Connection (deprecated)
    
    
    func (c *CloudShellClient) Connection() *grpc.ClientConn

Connection returns a connection to the API service.

Deprecated: Connections are now pooled so this method does not always return the same resource.

### func (*CloudShellClient) GetEnvironment 
    
    
    func (c *CloudShellClient) GetEnvironment(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[shellpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/shell/latest/apiv1/shellpb).[GetEnvironmentRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/shell/latest/apiv1/shellpb#cloud_google_com_go_shell_apiv1_shellpb_GetEnvironmentRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[shellpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/shell/latest/apiv1/shellpb).[Environment](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/shell/latest/apiv1/shellpb#cloud_google_com_go_shell_apiv1_shellpb_Environment), [error](https://pkg.go.dev/builtin#error))

GetEnvironment gets an environment. Returns NOT_FOUND if the environment does not exist.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	shell "cloud.google.com/go/shell/apiv1"
    	shellpb "cloud.google.com/go/shell/apiv1/shellpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := shell.[NewCloudShellClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/shell/latest/apiv1.html#cloud_google_com_go_shell_apiv1_CloudShellClient_NewCloudShellClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/shell/latest/apiv1.html#cloud_google_com_go_shell_apiv1_CloudShellClient_Close)()
    
    	req := &shellpb.GetEnvironmentRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/shell/apiv1/shellpb#GetEnvironmentRequest.
    	}
    	resp, err := c.GetEnvironment(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*CloudShellClient) RemovePublicKey 
    
    
    func (c *CloudShellClient) RemovePublicKey(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[shellpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/shell/latest/apiv1/shellpb).[RemovePublicKeyRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/shell/latest/apiv1/shellpb#cloud_google_com_go_shell_apiv1_shellpb_RemovePublicKeyRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*RemovePublicKeyOperation, [error](https://pkg.go.dev/builtin#error))

RemovePublicKey removes a public SSH key from an environment. Clients will no longer be able to connect to the environment using the corresponding private key. If a key with the same content is not present, this will error with NOT_FOUND.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	shell "cloud.google.com/go/shell/apiv1"
    	shellpb "cloud.google.com/go/shell/apiv1/shellpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := shell.[NewCloudShellClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/shell/latest/apiv1.html#cloud_google_com_go_shell_apiv1_CloudShellClient_NewCloudShellClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/shell/latest/apiv1.html#cloud_google_com_go_shell_apiv1_CloudShellClient_Close)()
    
    	req := &shellpb.RemovePublicKeyRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/shell/apiv1/shellpb#RemovePublicKeyRequest.
    	}
    	op, err := c.RemovePublicKey(ctx, req)
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
    

### func (*CloudShellClient) RemovePublicKeyOperation 
    
    
    func (c *CloudShellClient) RemovePublicKeyOperation(name [string](https://pkg.go.dev/builtin#string)) *RemovePublicKeyOperation

RemovePublicKeyOperation returns a new RemovePublicKeyOperation from a given name. The name must be that of a previously created RemovePublicKeyOperation, possibly from a different process.

### func (*CloudShellClient) StartEnvironment 
    
    
    func (c *CloudShellClient) StartEnvironment(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[shellpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/shell/latest/apiv1/shellpb).[StartEnvironmentRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/shell/latest/apiv1/shellpb#cloud_google_com_go_shell_apiv1_shellpb_StartEnvironmentRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*StartEnvironmentOperation, [error](https://pkg.go.dev/builtin#error))

StartEnvironment starts an existing environment, allowing clients to connect to it. The returned operation will contain an instance of StartEnvironmentMetadata in its metadata field. Users can wait for the environment to start by polling this operation via GetOperation. Once the environment has finished starting and is ready to accept connections, the operation will contain a StartEnvironmentResponse in its response field.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	shell "cloud.google.com/go/shell/apiv1"
    	shellpb "cloud.google.com/go/shell/apiv1/shellpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := shell.[NewCloudShellClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/shell/latest/apiv1.html#cloud_google_com_go_shell_apiv1_CloudShellClient_NewCloudShellClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/shell/latest/apiv1.html#cloud_google_com_go_shell_apiv1_CloudShellClient_Close)()
    
    	req := &shellpb.StartEnvironmentRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/shell/apiv1/shellpb#StartEnvironmentRequest.
    	}
    	op, err := c.StartEnvironment(ctx, req)
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
    

### func (*CloudShellClient) StartEnvironmentOperation 
    
    
    func (c *CloudShellClient) StartEnvironmentOperation(name [string](https://pkg.go.dev/builtin#string)) *StartEnvironmentOperation

StartEnvironmentOperation returns a new StartEnvironmentOperation from a given name. The name must be that of a previously created StartEnvironmentOperation, possibly from a different process.

## RemovePublicKeyOperation
    
    
    type RemovePublicKeyOperation struct {
    	// contains filtered or unexported fields
    }

RemovePublicKeyOperation manages a long-running operation from RemovePublicKey.

### func (*RemovePublicKeyOperation) Done 
    
    
    func (op *RemovePublicKeyOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*RemovePublicKeyOperation) Metadata 
    
    
    func (op *RemovePublicKeyOperation) Metadata() (*[shellpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/shell/latest/apiv1/shellpb).[RemovePublicKeyMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/shell/latest/apiv1/shellpb#cloud_google_com_go_shell_apiv1_shellpb_RemovePublicKeyMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*RemovePublicKeyOperation) Name 
    
    
    func (op *RemovePublicKeyOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*RemovePublicKeyOperation) Poll 
    
    
    func (op *RemovePublicKeyOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[shellpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/shell/latest/apiv1/shellpb).[RemovePublicKeyResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/shell/latest/apiv1/shellpb#cloud_google_com_go_shell_apiv1_shellpb_RemovePublicKeyResponse), [error](https://pkg.go.dev/builtin#error))

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*RemovePublicKeyOperation) Wait 
    
    
    func (op *RemovePublicKeyOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[shellpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/shell/latest/apiv1/shellpb).[RemovePublicKeyResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/shell/latest/apiv1/shellpb#cloud_google_com_go_shell_apiv1_shellpb_RemovePublicKeyResponse), [error](https://pkg.go.dev/builtin#error))

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## StartEnvironmentOperation
    
    
    type StartEnvironmentOperation struct {
    	// contains filtered or unexported fields
    }

StartEnvironmentOperation manages a long-running operation from StartEnvironment.

### func (*StartEnvironmentOperation) Done 
    
    
    func (op *StartEnvironmentOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*StartEnvironmentOperation) Metadata 
    
    
    func (op *StartEnvironmentOperation) Metadata() (*[shellpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/shell/latest/apiv1/shellpb).[StartEnvironmentMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/shell/latest/apiv1/shellpb#cloud_google_com_go_shell_apiv1_shellpb_StartEnvironmentMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*StartEnvironmentOperation) Name 
    
    
    func (op *StartEnvironmentOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*StartEnvironmentOperation) Poll 
    
    
    func (op *StartEnvironmentOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[shellpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/shell/latest/apiv1/shellpb).[StartEnvironmentResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/shell/latest/apiv1/shellpb#cloud_google_com_go_shell_apiv1_shellpb_StartEnvironmentResponse), [error](https://pkg.go.dev/builtin#error))

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*StartEnvironmentOperation) Wait 
    
    
    func (op *StartEnvironmentOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[shellpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/shell/latest/apiv1/shellpb).[StartEnvironmentResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/shell/latest/apiv1/shellpb#cloud_google_com_go_shell_apiv1_shellpb_StartEnvironmentResponse), [error](https://pkg.go.dev/builtin#error))

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
