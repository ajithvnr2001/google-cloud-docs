---
url: https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/
title: Dataform API v1 - Package cloud.google.com/go/dataform/apiv1 (v1.6.0) \u00a0|\u00a0 Go client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:18:04.134451+00:00
---

# Dataform API v1 - Package cloud.google.com/go/dataform/apiv1 (v1.6.0)  |  Go client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Go ](https://docs.cloud.google.com/go/docs)
  * [ Client libraries ](https://docs.cloud.google.com/go/docs/reference)



Send feedback 

#  Dataform API v1 - Package cloud.google.com/go/dataform/apiv1 (v1.6.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.6.0 (latest)  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.1  0.11.2  0.10.3  0.9.9  0.8.3  0.7.1  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 

**Note:** To get more information about this package, such as access to older versions, view [this package on pkg.go.dev](https://pkg.go.dev/cloud.google.com/go/dataform/apiv1). 

Package dataform is an auto-generated package for the Dataform API. 

Service to develop, version control, and operationalize SQL pipelines in BigQuery. 

## General documentation

For information that is relevant for all client libraries please reference <https://pkg.go.dev/cloud.google.com/go#pkg-overview>. Some information on this page includes: 

  * [Authentication and Authorization](https://pkg.go.dev/cloud.google.com/go#hdr-Authentication_and_Authorization)
  * [Timeouts and Cancellation](https://pkg.go.dev/cloud.google.com/go#hdr-Timeouts_and_Cancellation)
  * [Testing against Client Libraries](https://pkg.go.dev/cloud.google.com/go#hdr-Testing)
  * [Debugging Client Libraries](https://pkg.go.dev/cloud.google.com/go#hdr-Debugging)
  * [Inspecting errors](https://pkg.go.dev/cloud.google.com/go#hdr-Inspecting_errors)



## Example usage

To get started with this package, create a client.
    
    
    // go get cloud.google.com/go/dataform/apiv1@latest
    ctx := context.Background()
    // This snippet has been automatically generated and should be regarded as a code template only.
    // It will require modifications to work:
    // - It may require correct/in-range values for request initialization.
    // - It may require specifying regional endpoints when creating the service client as shown in:
    //   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    c, err := dataform.NewClient(ctx)
    if err != nil {
        // TODO: Handle error.
    }
    defer c.Close()

The client will use your default application credentials. Clients should be reused instead of created as needed. The methods of Client are safe for concurrent use by multiple goroutines. The returned client must be Closed when it is done being used. 

## Using the Client

The following is an example of making an API call with the newly created client, mentioned above.
    
    
    req := &dataformpb.CancelWorkflowInvocationRequest{
        // TODO: Fill request struct fields.
        // See https://pkg.go.dev/cloud.google.com/go/dataform/apiv1/dataformpb#CancelWorkflowInvocationRequest.
    }
    resp, err := c.CancelWorkflowInvocation(ctx, req)
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

## CallOptions
    
    
    type CallOptions struct {
    	GetTeamFolder                      []gax.CallOption
    	CreateTeamFolder                   []gax.CallOption
    	UpdateTeamFolder                   []gax.CallOption
    	DeleteTeamFolder                   []gax.CallOption
    	DeleteTeamFolderTree               []gax.CallOption
    	QueryTeamFolderContents            []gax.CallOption
    	SearchTeamFolders                  []gax.CallOption
    	GetFolder                          []gax.CallOption
    	CreateFolder                       []gax.CallOption
    	UpdateFolder                       []gax.CallOption
    	DeleteFolder                       []gax.CallOption
    	DeleteFolderTree                   []gax.CallOption
    	QueryFolderContents                []gax.CallOption
    	QueryUserRootContents              []gax.CallOption
    	MoveFolder                         []gax.CallOption
    	ListRepositories                   []gax.CallOption
    	GetRepository                      []gax.CallOption
    	CreateRepository                   []gax.CallOption
    	UpdateRepository                   []gax.CallOption
    	DeleteRepository                   []gax.CallOption
    	MoveRepository                     []gax.CallOption
    	CommitRepositoryChanges            []gax.CallOption
    	ReadRepositoryFile                 []gax.CallOption
    	QueryRepositoryDirectoryContents   []gax.CallOption
    	FetchRepositoryHistory             []gax.CallOption
    	ComputeRepositoryAccessTokenStatus []gax.CallOption
    	FetchRemoteBranches                []gax.CallOption
    	ListWorkspaces                     []gax.CallOption
    	GetWorkspace                       []gax.CallOption
    	CreateWorkspace                    []gax.CallOption
    	DeleteWorkspace                    []gax.CallOption
    	InstallNpmPackages                 []gax.CallOption
    	PullGitCommits                     []gax.CallOption
    	PushGitCommits                     []gax.CallOption
    	FetchFileGitStatuses               []gax.CallOption
    	FetchGitAheadBehind                []gax.CallOption
    	CommitWorkspaceChanges             []gax.CallOption
    	ResetWorkspaceChanges              []gax.CallOption
    	FetchFileDiff                      []gax.CallOption
    	QueryDirectoryContents             []gax.CallOption
    	SearchFiles                        []gax.CallOption
    	MakeDirectory                      []gax.CallOption
    	RemoveDirectory                    []gax.CallOption
    	MoveDirectory                      []gax.CallOption
    	ReadFile                           []gax.CallOption
    	RemoveFile                         []gax.CallOption
    	MoveFile                           []gax.CallOption
    	WriteFile                          []gax.CallOption
    	ListReleaseConfigs                 []gax.CallOption
    	GetReleaseConfig                   []gax.CallOption
    	CreateReleaseConfig                []gax.CallOption
    	UpdateReleaseConfig                []gax.CallOption
    	DeleteReleaseConfig                []gax.CallOption
    	ListCompilationResults             []gax.CallOption
    	GetCompilationResult               []gax.CallOption
    	CreateCompilationResult            []gax.CallOption
    	QueryCompilationResultActions      []gax.CallOption
    	ListWorkflowConfigs                []gax.CallOption
    	GetWorkflowConfig                  []gax.CallOption
    	CreateWorkflowConfig               []gax.CallOption
    	UpdateWorkflowConfig               []gax.CallOption
    	DeleteWorkflowConfig               []gax.CallOption
    	ListWorkflowInvocations            []gax.CallOption
    	GetWorkflowInvocation              []gax.CallOption
    	CreateWorkflowInvocation           []gax.CallOption
    	DeleteWorkflowInvocation           []gax.CallOption
    	CancelWorkflowInvocation           []gax.CallOption
    	QueryWorkflowInvocationActions     []gax.CallOption
    	GetConfig                          []gax.CallOption
    	UpdateConfig                       []gax.CallOption
    	GetIamPolicy                       []gax.CallOption
    	SetIamPolicy                       []gax.CallOption
    	TestIamPermissions                 []gax.CallOption
    	GetLocation                        []gax.CallOption
    	ListLocations                      []gax.CallOption
    	CancelOperation                    []gax.CallOption
    	DeleteOperation                    []gax.CallOption
    	GetOperation                       []gax.CallOption
    	ListOperations                     []gax.CallOption
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

Client is a client for interacting with Dataform API. Methods, except Close, may be called concurrently. However, fields must not be modified concurrently with method calls.

Dataform is a service to develop, create, document, test, and update curated tables in BigQuery.

### func NewClient 
    
    
    func NewClient(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...option.ClientOption) (*Client, [error](https://pkg.go.dev/builtin#error))

NewClient creates a new dataform client based on gRPC. The returned client must be Closed when it is done being used to clean up its underlying connections.

Dataform is a service to develop, create, document, test, and update curated tables in BigQuery.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dataform "cloud.google.com/go/dataform/apiv1"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataform.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1.html#cloud_google_com_go_dataform_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1.html#cloud_google_com_go_dataform_apiv1_Client_Close)()
    
    	// TODO: Use client.
    	_ = c
    }
    

### func NewRESTClient 
    
    
    func NewRESTClient(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...option.ClientOption) (*Client, [error](https://pkg.go.dev/builtin#error))

NewRESTClient creates a new dataform rest client.

Dataform is a service to develop, create, document, test, and update curated tables in BigQuery.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dataform "cloud.google.com/go/dataform/apiv1"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataform.[NewRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1.html#cloud_google_com_go_dataform_apiv1_Client_NewRESTClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1.html#cloud_google_com_go_dataform_apiv1_Client_Close)()
    
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
    
    	dataform "cloud.google.com/go/dataform/apiv1"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataform.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1.html#cloud_google_com_go_dataform_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1.html#cloud_google_com_go_dataform_apiv1_Client_Close)()
    
    	req := &longrunningpb.[CancelOperationRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_CancelOperationRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#CancelOperationRequest.
    	}
    	err = c.CancelOperation(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    }
    

### func (*Client) CancelWorkflowInvocation 
    
    
    func (c *Client) CancelWorkflowInvocation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dataformpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb).[CancelWorkflowInvocationRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb#cloud_google_com_go_dataform_apiv1_dataformpb_CancelWorkflowInvocationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[dataformpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb).[CancelWorkflowInvocationResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb#cloud_google_com_go_dataform_apiv1_dataformpb_CancelWorkflowInvocationResponse), [error](https://pkg.go.dev/builtin#error))

CancelWorkflowInvocation requests cancellation of a running WorkflowInvocation.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dataform "cloud.google.com/go/dataform/apiv1"
    	dataformpb "cloud.google.com/go/dataform/apiv1/dataformpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataform.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1.html#cloud_google_com_go_dataform_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1.html#cloud_google_com_go_dataform_apiv1_Client_Close)()
    
    	req := &dataformpb.CancelWorkflowInvocationRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dataform/apiv1/dataformpb#CancelWorkflowInvocationRequest.
    	}
    	resp, err := c.CancelWorkflowInvocation(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*Client) Close 
    
    
    func (c *Client) Close() [error](https://pkg.go.dev/builtin#error)

Close closes the connection to the API service. **Always** call Close() when the client is no longer required.

### func (*Client) CommitRepositoryChanges 
    
    
    func (c *Client) CommitRepositoryChanges(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dataformpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb).[CommitRepositoryChangesRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb#cloud_google_com_go_dataform_apiv1_dataformpb_CommitRepositoryChangesRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[dataformpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb).[CommitRepositoryChangesResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb#cloud_google_com_go_dataform_apiv1_dataformpb_CommitRepositoryChangesResponse), [error](https://pkg.go.dev/builtin#error))

CommitRepositoryChanges applies a Git commit to a Repository. The Repository must not have a value for git_remote_settings.url.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dataform "cloud.google.com/go/dataform/apiv1"
    	dataformpb "cloud.google.com/go/dataform/apiv1/dataformpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataform.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1.html#cloud_google_com_go_dataform_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1.html#cloud_google_com_go_dataform_apiv1_Client_Close)()
    
    	req := &dataformpb.CommitRepositoryChangesRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dataform/apiv1/dataformpb#CommitRepositoryChangesRequest.
    	}
    	resp, err := c.CommitRepositoryChanges(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*Client) CommitWorkspaceChanges 
    
    
    func (c *Client) CommitWorkspaceChanges(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dataformpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb).[CommitWorkspaceChangesRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb#cloud_google_com_go_dataform_apiv1_dataformpb_CommitWorkspaceChangesRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[dataformpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb).[CommitWorkspaceChangesResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb#cloud_google_com_go_dataform_apiv1_dataformpb_CommitWorkspaceChangesResponse), [error](https://pkg.go.dev/builtin#error))

CommitWorkspaceChanges applies a Git commit for uncommitted files in a Workspace.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dataform "cloud.google.com/go/dataform/apiv1"
    	dataformpb "cloud.google.com/go/dataform/apiv1/dataformpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataform.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1.html#cloud_google_com_go_dataform_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1.html#cloud_google_com_go_dataform_apiv1_Client_Close)()
    
    	req := &dataformpb.CommitWorkspaceChangesRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dataform/apiv1/dataformpb#CommitWorkspaceChangesRequest.
    	}
    	resp, err := c.CommitWorkspaceChanges(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*Client) ComputeRepositoryAccessTokenStatus 
    
    
    func (c *Client) ComputeRepositoryAccessTokenStatus(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dataformpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb).[ComputeRepositoryAccessTokenStatusRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb#cloud_google_com_go_dataform_apiv1_dataformpb_ComputeRepositoryAccessTokenStatusRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[dataformpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb).[ComputeRepositoryAccessTokenStatusResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb#cloud_google_com_go_dataform_apiv1_dataformpb_ComputeRepositoryAccessTokenStatusResponse), [error](https://pkg.go.dev/builtin#error))

ComputeRepositoryAccessTokenStatus computes a Repository’s Git access token status.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dataform "cloud.google.com/go/dataform/apiv1"
    	dataformpb "cloud.google.com/go/dataform/apiv1/dataformpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataform.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1.html#cloud_google_com_go_dataform_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1.html#cloud_google_com_go_dataform_apiv1_Client_Close)()
    
    	req := &dataformpb.ComputeRepositoryAccessTokenStatusRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dataform/apiv1/dataformpb#ComputeRepositoryAccessTokenStatusRequest.
    	}
    	resp, err := c.ComputeRepositoryAccessTokenStatus(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*Client) Connection (deprecated)
    
    
    func (c *Client) Connection() *grpc.ClientConn

Connection returns a connection to the API service.

Deprecated: Connections are now pooled so this method does not always return the same resource.

### func (*Client) CreateCompilationResult 
    
    
    func (c *Client) CreateCompilationResult(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dataformpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb).[CreateCompilationResultRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb#cloud_google_com_go_dataform_apiv1_dataformpb_CreateCompilationResultRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[dataformpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb).[CompilationResult](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb#cloud_google_com_go_dataform_apiv1_dataformpb_CompilationResult), [error](https://pkg.go.dev/builtin#error))

CreateCompilationResult creates a new CompilationResult in a given project and location.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dataform "cloud.google.com/go/dataform/apiv1"
    	dataformpb "cloud.google.com/go/dataform/apiv1/dataformpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataform.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1.html#cloud_google_com_go_dataform_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1.html#cloud_google_com_go_dataform_apiv1_Client_Close)()
    
    	req := &dataformpb.CreateCompilationResultRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dataform/apiv1/dataformpb#CreateCompilationResultRequest.
    	}
    	resp, err := c.CreateCompilationResult(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*Client) CreateFolder 
    
    
    func (c *Client) CreateFolder(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dataformpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb).[CreateFolderRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb#cloud_google_com_go_dataform_apiv1_dataformpb_CreateFolderRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[dataformpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb).[Folder](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb#cloud_google_com_go_dataform_apiv1_dataformpb_Folder), [error](https://pkg.go.dev/builtin#error))

CreateFolder creates a new Folder in a given project and location.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dataform "cloud.google.com/go/dataform/apiv1"
    	dataformpb "cloud.google.com/go/dataform/apiv1/dataformpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataform.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1.html#cloud_google_com_go_dataform_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1.html#cloud_google_com_go_dataform_apiv1_Client_Close)()
    
    	req := &dataformpb.CreateFolderRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dataform/apiv1/dataformpb#CreateFolderRequest.
    	}
    	resp, err := c.CreateFolder(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*Client) CreateReleaseConfig 
    
    
    func (c *Client) CreateReleaseConfig(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dataformpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb).[CreateReleaseConfigRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb#cloud_google_com_go_dataform_apiv1_dataformpb_CreateReleaseConfigRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[dataformpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb).[ReleaseConfig](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb#cloud_google_com_go_dataform_apiv1_dataformpb_ReleaseConfig), [error](https://pkg.go.dev/builtin#error))

CreateReleaseConfig creates a new ReleaseConfig in a given Repository.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dataform "cloud.google.com/go/dataform/apiv1"
    	dataformpb "cloud.google.com/go/dataform/apiv1/dataformpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataform.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1.html#cloud_google_com_go_dataform_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1.html#cloud_google_com_go_dataform_apiv1_Client_Close)()
    
    	req := &dataformpb.CreateReleaseConfigRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dataform/apiv1/dataformpb#CreateReleaseConfigRequest.
    	}
    	resp, err := c.CreateReleaseConfig(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*Client) CreateRepository 
    
    
    func (c *Client) CreateRepository(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dataformpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb).[CreateRepositoryRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb#cloud_google_com_go_dataform_apiv1_dataformpb_CreateRepositoryRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[dataformpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb).[Repository](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb#cloud_google_com_go_dataform_apiv1_dataformpb_Repository), [error](https://pkg.go.dev/builtin#error))

CreateRepository creates a new Repository in a given project and location.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dataform "cloud.google.com/go/dataform/apiv1"
    	dataformpb "cloud.google.com/go/dataform/apiv1/dataformpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataform.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1.html#cloud_google_com_go_dataform_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1.html#cloud_google_com_go_dataform_apiv1_Client_Close)()
    
    	req := &dataformpb.CreateRepositoryRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dataform/apiv1/dataformpb#CreateRepositoryRequest.
    	}
    	resp, err := c.CreateRepository(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*Client) CreateTeamFolder 
    
    
    func (c *Client) CreateTeamFolder(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dataformpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb).[CreateTeamFolderRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb#cloud_google_com_go_dataform_apiv1_dataformpb_CreateTeamFolderRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[dataformpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb).[TeamFolder](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb#cloud_google_com_go_dataform_apiv1_dataformpb_TeamFolder), [error](https://pkg.go.dev/builtin#error))

CreateTeamFolder creates a new TeamFolder in a given project and location.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dataform "cloud.google.com/go/dataform/apiv1"
    	dataformpb "cloud.google.com/go/dataform/apiv1/dataformpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataform.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1.html#cloud_google_com_go_dataform_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1.html#cloud_google_com_go_dataform_apiv1_Client_Close)()
    
    	req := &dataformpb.CreateTeamFolderRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dataform/apiv1/dataformpb#CreateTeamFolderRequest.
    	}
    	resp, err := c.CreateTeamFolder(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*Client) CreateWorkflowConfig 
    
    
    func (c *Client) CreateWorkflowConfig(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dataformpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb).[CreateWorkflowConfigRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb#cloud_google_com_go_dataform_apiv1_dataformpb_CreateWorkflowConfigRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[dataformpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb).[WorkflowConfig](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb#cloud_google_com_go_dataform_apiv1_dataformpb_WorkflowConfig), [error](https://pkg.go.dev/builtin#error))

CreateWorkflowConfig creates a new WorkflowConfig in a given Repository.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dataform "cloud.google.com/go/dataform/apiv1"
    	dataformpb "cloud.google.com/go/dataform/apiv1/dataformpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataform.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1.html#cloud_google_com_go_dataform_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1.html#cloud_google_com_go_dataform_apiv1_Client_Close)()
    
    	req := &dataformpb.CreateWorkflowConfigRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dataform/apiv1/dataformpb#CreateWorkflowConfigRequest.
    	}
    	resp, err := c.CreateWorkflowConfig(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*Client) CreateWorkflowInvocation 
    
    
    func (c *Client) CreateWorkflowInvocation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dataformpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb).[CreateWorkflowInvocationRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb#cloud_google_com_go_dataform_apiv1_dataformpb_CreateWorkflowInvocationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[dataformpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb).[WorkflowInvocation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb#cloud_google_com_go_dataform_apiv1_dataformpb_WorkflowInvocation), [error](https://pkg.go.dev/builtin#error))

CreateWorkflowInvocation creates a new WorkflowInvocation in a given Repository.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dataform "cloud.google.com/go/dataform/apiv1"
    	dataformpb "cloud.google.com/go/dataform/apiv1/dataformpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataform.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1.html#cloud_google_com_go_dataform_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1.html#cloud_google_com_go_dataform_apiv1_Client_Close)()
    
    	req := &dataformpb.CreateWorkflowInvocationRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dataform/apiv1/dataformpb#CreateWorkflowInvocationRequest.
    	}
    	resp, err := c.CreateWorkflowInvocation(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*Client) CreateWorkspace 
    
    
    func (c *Client) CreateWorkspace(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dataformpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb).[CreateWorkspaceRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb#cloud_google_com_go_dataform_apiv1_dataformpb_CreateWorkspaceRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[dataformpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb).[Workspace](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb#cloud_google_com_go_dataform_apiv1_dataformpb_Workspace), [error](https://pkg.go.dev/builtin#error))

CreateWorkspace creates a new Workspace in a given Repository.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dataform "cloud.google.com/go/dataform/apiv1"
    	dataformpb "cloud.google.com/go/dataform/apiv1/dataformpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataform.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1.html#cloud_google_com_go_dataform_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1.html#cloud_google_com_go_dataform_apiv1_Client_Close)()
    
    	req := &dataformpb.CreateWorkspaceRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dataform/apiv1/dataformpb#CreateWorkspaceRequest.
    	}
    	resp, err := c.CreateWorkspace(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*Client) DeleteFolder 
    
    
    func (c *Client) DeleteFolder(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dataformpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb).[DeleteFolderRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb#cloud_google_com_go_dataform_apiv1_dataformpb_DeleteFolderRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

DeleteFolder deletes a single Folder.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dataform "cloud.google.com/go/dataform/apiv1"
    	dataformpb "cloud.google.com/go/dataform/apiv1/dataformpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataform.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1.html#cloud_google_com_go_dataform_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1.html#cloud_google_com_go_dataform_apiv1_Client_Close)()
    
    	req := &dataformpb.DeleteFolderRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dataform/apiv1/dataformpb#DeleteFolderRequest.
    	}
    	err = c.DeleteFolder(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    }
    

### func (*Client) DeleteFolderTree 
    
    
    func (c *Client) DeleteFolderTree(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dataformpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb).[DeleteFolderTreeRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb#cloud_google_com_go_dataform_apiv1_dataformpb_DeleteFolderTreeRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*DeleteFolderTreeOperation, [error](https://pkg.go.dev/builtin#error))

DeleteFolderTree deletes a Folder with its contents (Folders, Repositories, Workspaces, ReleaseConfigs, and WorkflowConfigs).

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dataform "cloud.google.com/go/dataform/apiv1"
    	dataformpb "cloud.google.com/go/dataform/apiv1/dataformpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataform.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1.html#cloud_google_com_go_dataform_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1.html#cloud_google_com_go_dataform_apiv1_Client_Close)()
    
    	req := &dataformpb.DeleteFolderTreeRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dataform/apiv1/dataformpb#DeleteFolderTreeRequest.
    	}
    	op, err := c.DeleteFolderTree(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    
    	err = op.Wait(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    }
    

### func (*Client) DeleteFolderTreeOperation 
    
    
    func (c *Client) DeleteFolderTreeOperation(name [string](https://pkg.go.dev/builtin#string)) *DeleteFolderTreeOperation

DeleteFolderTreeOperation returns a new DeleteFolderTreeOperation from a given name. The name must be that of a previously created DeleteFolderTreeOperation, possibly from a different process.

### func (*Client) DeleteOperation 
    
    
    func (c *Client) DeleteOperation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[DeleteOperationRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#DeleteOperationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

DeleteOperation is a utility method from google.longrunning.Operations.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dataform "cloud.google.com/go/dataform/apiv1"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataform.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1.html#cloud_google_com_go_dataform_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1.html#cloud_google_com_go_dataform_apiv1_Client_Close)()
    
    	req := &longrunningpb.[DeleteOperationRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/longrunning/latest/autogen/longrunningpb.html#cloud_google_com_go_longrunning_autogen_longrunningpb_DeleteOperationRequest){
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#DeleteOperationRequest.
    	}
    	err = c.DeleteOperation(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    }
    

### func (*Client) DeleteReleaseConfig 
    
    
    func (c *Client) DeleteReleaseConfig(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dataformpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb).[DeleteReleaseConfigRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb#cloud_google_com_go_dataform_apiv1_dataformpb_DeleteReleaseConfigRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

DeleteReleaseConfig deletes a single ReleaseConfig.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dataform "cloud.google.com/go/dataform/apiv1"
    	dataformpb "cloud.google.com/go/dataform/apiv1/dataformpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataform.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1.html#cloud_google_com_go_dataform_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1.html#cloud_google_com_go_dataform_apiv1_Client_Close)()
    
    	req := &dataformpb.DeleteReleaseConfigRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dataform/apiv1/dataformpb#DeleteReleaseConfigRequest.
    	}
    	err = c.DeleteReleaseConfig(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    }
    

### func (*Client) DeleteRepository 
    
    
    func (c *Client) DeleteRepository(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dataformpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb).[DeleteRepositoryRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb#cloud_google_com_go_dataform_apiv1_dataformpb_DeleteRepositoryRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

DeleteRepository deletes a single Repository.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dataform "cloud.google.com/go/dataform/apiv1"
    	dataformpb "cloud.google.com/go/dataform/apiv1/dataformpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataform.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1.html#cloud_google_com_go_dataform_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1.html#cloud_google_com_go_dataform_apiv1_Client_Close)()
    
    	req := &dataformpb.DeleteRepositoryRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dataform/apiv1/dataformpb#DeleteRepositoryRequest.
    	}
    	err = c.DeleteRepository(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    }
    

### func (*Client) DeleteTeamFolder 
    
    
    func (c *Client) DeleteTeamFolder(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dataformpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb).[DeleteTeamFolderRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb#cloud_google_com_go_dataform_apiv1_dataformpb_DeleteTeamFolderRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

DeleteTeamFolder deletes a single TeamFolder.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dataform "cloud.google.com/go/dataform/apiv1"
    	dataformpb "cloud.google.com/go/dataform/apiv1/dataformpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataform.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1.html#cloud_google_com_go_dataform_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1.html#cloud_google_com_go_dataform_apiv1_Client_Close)()
    
    	req := &dataformpb.DeleteTeamFolderRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dataform/apiv1/dataformpb#DeleteTeamFolderRequest.
    	}
    	err = c.DeleteTeamFolder(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    }
    

### func (*Client) DeleteTeamFolderTree 
    
    
    func (c *Client) DeleteTeamFolderTree(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dataformpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb).[DeleteTeamFolderTreeRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb#cloud_google_com_go_dataform_apiv1_dataformpb_DeleteTeamFolderTreeRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*DeleteTeamFolderTreeOperation, [error](https://pkg.go.dev/builtin#error))

DeleteTeamFolderTree deletes a TeamFolder with its contents (Folders, Repositories, Workspaces, ReleaseConfigs, and WorkflowConfigs).

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dataform "cloud.google.com/go/dataform/apiv1"
    	dataformpb "cloud.google.com/go/dataform/apiv1/dataformpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataform.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1.html#cloud_google_com_go_dataform_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1.html#cloud_google_com_go_dataform_apiv1_Client_Close)()
    
    	req := &dataformpb.DeleteTeamFolderTreeRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dataform/apiv1/dataformpb#DeleteTeamFolderTreeRequest.
    	}
    	op, err := c.DeleteTeamFolderTree(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    
    	err = op.Wait(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    }
    

### func (*Client) DeleteTeamFolderTreeOperation 
    
    
    func (c *Client) DeleteTeamFolderTreeOperation(name [string](https://pkg.go.dev/builtin#string)) *DeleteTeamFolderTreeOperation

DeleteTeamFolderTreeOperation returns a new DeleteTeamFolderTreeOperation from a given name. The name must be that of a previously created DeleteTeamFolderTreeOperation, possibly from a different process.

### func (*Client) DeleteWorkflowConfig 
    
    
    func (c *Client) DeleteWorkflowConfig(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dataformpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb).[DeleteWorkflowConfigRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb#cloud_google_com_go_dataform_apiv1_dataformpb_DeleteWorkflowConfigRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

DeleteWorkflowConfig deletes a single WorkflowConfig.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dataform "cloud.google.com/go/dataform/apiv1"
    	dataformpb "cloud.google.com/go/dataform/apiv1/dataformpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataform.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1.html#cloud_google_com_go_dataform_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1.html#cloud_google_com_go_dataform_apiv1_Client_Close)()
    
    	req := &dataformpb.DeleteWorkflowConfigRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dataform/apiv1/dataformpb#DeleteWorkflowConfigRequest.
    	}
    	err = c.DeleteWorkflowConfig(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    }
    

### func (*Client) DeleteWorkflowInvocation 
    
    
    func (c *Client) DeleteWorkflowInvocation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dataformpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb).[DeleteWorkflowInvocationRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb#cloud_google_com_go_dataform_apiv1_dataformpb_DeleteWorkflowInvocationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

DeleteWorkflowInvocation deletes a single WorkflowInvocation.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dataform "cloud.google.com/go/dataform/apiv1"
    	dataformpb "cloud.google.com/go/dataform/apiv1/dataformpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataform.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1.html#cloud_google_com_go_dataform_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1.html#cloud_google_com_go_dataform_apiv1_Client_Close)()
    
    	req := &dataformpb.DeleteWorkflowInvocationRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dataform/apiv1/dataformpb#DeleteWorkflowInvocationRequest.
    	}
    	err = c.DeleteWorkflowInvocation(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    }
    

### func (*Client) DeleteWorkspace 
    
    
    func (c *Client) DeleteWorkspace(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dataformpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb).[DeleteWorkspaceRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb#cloud_google_com_go_dataform_apiv1_dataformpb_DeleteWorkspaceRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

DeleteWorkspace deletes a single Workspace.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dataform "cloud.google.com/go/dataform/apiv1"
    	dataformpb "cloud.google.com/go/dataform/apiv1/dataformpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataform.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1.html#cloud_google_com_go_dataform_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1.html#cloud_google_com_go_dataform_apiv1_Client_Close)()
    
    	req := &dataformpb.DeleteWorkspaceRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dataform/apiv1/dataformpb#DeleteWorkspaceRequest.
    	}
    	err = c.DeleteWorkspace(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    }
    

### func (*Client) FetchFileDiff 
    
    
    func (c *Client) FetchFileDiff(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dataformpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb).[FetchFileDiffRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb#cloud_google_com_go_dataform_apiv1_dataformpb_FetchFileDiffRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[dataformpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb).[FetchFileDiffResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb#cloud_google_com_go_dataform_apiv1_dataformpb_FetchFileDiffResponse), [error](https://pkg.go.dev/builtin#error))

FetchFileDiff fetches Git diff for an uncommitted file in a Workspace.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dataform "cloud.google.com/go/dataform/apiv1"
    	dataformpb "cloud.google.com/go/dataform/apiv1/dataformpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataform.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1.html#cloud_google_com_go_dataform_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1.html#cloud_google_com_go_dataform_apiv1_Client_Close)()
    
    	req := &dataformpb.FetchFileDiffRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dataform/apiv1/dataformpb#FetchFileDiffRequest.
    	}
    	resp, err := c.FetchFileDiff(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*Client) FetchFileGitStatuses 
    
    
    func (c *Client) FetchFileGitStatuses(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dataformpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb).[FetchFileGitStatusesRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb#cloud_google_com_go_dataform_apiv1_dataformpb_FetchFileGitStatusesRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[dataformpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb).[FetchFileGitStatusesResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb#cloud_google_com_go_dataform_apiv1_dataformpb_FetchFileGitStatusesResponse), [error](https://pkg.go.dev/builtin#error))

FetchFileGitStatuses fetches Git statuses for the files in a Workspace.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dataform "cloud.google.com/go/dataform/apiv1"
    	dataformpb "cloud.google.com/go/dataform/apiv1/dataformpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataform.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1.html#cloud_google_com_go_dataform_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1.html#cloud_google_com_go_dataform_apiv1_Client_Close)()
    
    	req := &dataformpb.FetchFileGitStatusesRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dataform/apiv1/dataformpb#FetchFileGitStatusesRequest.
    	}
    	resp, err := c.FetchFileGitStatuses(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*Client) FetchGitAheadBehind 
    
    
    func (c *Client) FetchGitAheadBehind(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dataformpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb).[FetchGitAheadBehindRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb#cloud_google_com_go_dataform_apiv1_dataformpb_FetchGitAheadBehindRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[dataformpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb).[FetchGitAheadBehindResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb#cloud_google_com_go_dataform_apiv1_dataformpb_FetchGitAheadBehindResponse), [error](https://pkg.go.dev/builtin#error))

FetchGitAheadBehind fetches Git ahead/behind against a remote branch.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dataform "cloud.google.com/go/dataform/apiv1"
    	dataformpb "cloud.google.com/go/dataform/apiv1/dataformpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataform.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1.html#cloud_google_com_go_dataform_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1.html#cloud_google_com_go_dataform_apiv1_Client_Close)()
    
    	req := &dataformpb.FetchGitAheadBehindRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dataform/apiv1/dataformpb#FetchGitAheadBehindRequest.
    	}
    	resp, err := c.FetchGitAheadBehind(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*Client) FetchRemoteBranches 
    
    
    func (c *Client) FetchRemoteBranches(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dataformpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb).[FetchRemoteBranchesRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb#cloud_google_com_go_dataform_apiv1_dataformpb_FetchRemoteBranchesRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[dataformpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb).[FetchRemoteBranchesResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb#cloud_google_com_go_dataform_apiv1_dataformpb_FetchRemoteBranchesResponse), [error](https://pkg.go.dev/builtin#error))

FetchRemoteBranches fetches a Repository’s remote branches.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dataform "cloud.google.com/go/dataform/apiv1"
    	dataformpb "cloud.google.com/go/dataform/apiv1/dataformpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataform.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1.html#cloud_google_com_go_dataform_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1.html#cloud_google_com_go_dataform_apiv1_Client_Close)()
    
    	req := &dataformpb.FetchRemoteBranchesRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dataform/apiv1/dataformpb#FetchRemoteBranchesRequest.
    	}
    	resp, err := c.FetchRemoteBranches(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*Client) FetchRepositoryHistory 
    
    
    func (c *Client) FetchRepositoryHistory(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dataformpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb).[FetchRepositoryHistoryRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb#cloud_google_com_go_dataform_apiv1_dataformpb_FetchRepositoryHistoryRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *CommitLogEntryIterator

FetchRepositoryHistory fetches a Repository’s history of commits. The Repository must not have a value for git_remote_settings.url.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	dataform "cloud.google.com/go/dataform/apiv1"
    	dataformpb "cloud.google.com/go/dataform/apiv1/dataformpb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataform.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1.html#cloud_google_com_go_dataform_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1.html#cloud_google_com_go_dataform_apiv1_Client_Close)()
    
    	req := &dataformpb.FetchRepositoryHistoryRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dataform/apiv1/dataformpb#FetchRepositoryHistoryRequest.
    	}
    	it := c.FetchRepositoryHistory(ctx, req)
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
    		_ = it.Response.(*dataformpb.FetchRepositoryHistoryResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	dataform "cloud.google.com/go/dataform/apiv1"
    	dataformpb "cloud.google.com/go/dataform/apiv1/dataformpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataform.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1.html#cloud_google_com_go_dataform_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1.html#cloud_google_com_go_dataform_apiv1_Client_Close)()
    
    	req := &dataformpb.FetchRepositoryHistoryRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dataform/apiv1/dataformpb#FetchRepositoryHistoryRequest.
    	}
    	for resp, err := range c.FetchRepositoryHistory(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*Client) GetCompilationResult 
    
    
    func (c *Client) GetCompilationResult(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dataformpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb).[GetCompilationResultRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb#cloud_google_com_go_dataform_apiv1_dataformpb_GetCompilationResultRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[dataformpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb).[CompilationResult](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb#cloud_google_com_go_dataform_apiv1_dataformpb_CompilationResult), [error](https://pkg.go.dev/builtin#error))

GetCompilationResult fetches a single CompilationResult.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dataform "cloud.google.com/go/dataform/apiv1"
    	dataformpb "cloud.google.com/go/dataform/apiv1/dataformpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataform.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1.html#cloud_google_com_go_dataform_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1.html#cloud_google_com_go_dataform_apiv1_Client_Close)()
    
    	req := &dataformpb.GetCompilationResultRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dataform/apiv1/dataformpb#GetCompilationResultRequest.
    	}
    	resp, err := c.GetCompilationResult(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*Client) GetConfig 
    
    
    func (c *Client) GetConfig(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dataformpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb).[GetConfigRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb#cloud_google_com_go_dataform_apiv1_dataformpb_GetConfigRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[dataformpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb).[Config](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb#cloud_google_com_go_dataform_apiv1_dataformpb_Config), [error](https://pkg.go.dev/builtin#error))

GetConfig get default config for a given project and location.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dataform "cloud.google.com/go/dataform/apiv1"
    	dataformpb "cloud.google.com/go/dataform/apiv1/dataformpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataform.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1.html#cloud_google_com_go_dataform_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1.html#cloud_google_com_go_dataform_apiv1_Client_Close)()
    
    	req := &dataformpb.GetConfigRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dataform/apiv1/dataformpb#GetConfigRequest.
    	}
    	resp, err := c.GetConfig(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*Client) GetFolder 
    
    
    func (c *Client) GetFolder(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dataformpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb).[GetFolderRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb#cloud_google_com_go_dataform_apiv1_dataformpb_GetFolderRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[dataformpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb).[Folder](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb#cloud_google_com_go_dataform_apiv1_dataformpb_Folder), [error](https://pkg.go.dev/builtin#error))

GetFolder fetches a single Folder.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dataform "cloud.google.com/go/dataform/apiv1"
    	dataformpb "cloud.google.com/go/dataform/apiv1/dataformpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataform.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1.html#cloud_google_com_go_dataform_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1.html#cloud_google_com_go_dataform_apiv1_Client_Close)()
    
    	req := &dataformpb.GetFolderRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dataform/apiv1/dataformpb#GetFolderRequest.
    	}
    	resp, err := c.GetFolder(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*Client) GetIamPolicy 
    
    
    func (c *Client) GetIamPolicy(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[iampb](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb).[GetIamPolicyRequest](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb#GetIamPolicyRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[iampb](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb).[Policy](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb#Policy), [error](https://pkg.go.dev/builtin#error))

GetIamPolicy gets the access control policy for a resource. Returns an empty policy if the resource exists and does not have a policy set.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dataform "cloud.google.com/go/dataform/apiv1"
    
    	iampb "cloud.google.com/go/iam/apiv1/iampb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataform.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1.html#cloud_google_com_go_dataform_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1.html#cloud_google_com_go_dataform_apiv1_Client_Close)()
    
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
    

### func (*Client) GetLocation 
    
    
    func (c *Client) GetLocation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[locationpb](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location).[GetLocationRequest](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#GetLocationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[locationpb](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location).[Location](https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#Location), [error](https://pkg.go.dev/builtin#error))

GetLocation gets information about a location.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dataform "cloud.google.com/go/dataform/apiv1"
    
    	locationpb "google.golang.org/genproto/googleapis/cloud/location"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataform.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1.html#cloud_google_com_go_dataform_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1.html#cloud_google_com_go_dataform_apiv1_Client_Close)()
    
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
    

### func (*Client) GetOperation 
    
    
    func (c *Client) GetOperation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[GetOperationRequest](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#GetOperationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[longrunningpb](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb).[Operation](https://pkg.go.dev/cloud.google.com/go/longrunning/autogen/longrunningpb#Operation), [error](https://pkg.go.dev/builtin#error))

GetOperation is a utility method from google.longrunning.Operations.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dataform "cloud.google.com/go/dataform/apiv1"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataform.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1.html#cloud_google_com_go_dataform_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1.html#cloud_google_com_go_dataform_apiv1_Client_Close)()
    
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
    

### func (*Client) GetReleaseConfig 
    
    
    func (c *Client) GetReleaseConfig(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dataformpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb).[GetReleaseConfigRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb#cloud_google_com_go_dataform_apiv1_dataformpb_GetReleaseConfigRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[dataformpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb).[ReleaseConfig](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb#cloud_google_com_go_dataform_apiv1_dataformpb_ReleaseConfig), [error](https://pkg.go.dev/builtin#error))

GetReleaseConfig fetches a single ReleaseConfig.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dataform "cloud.google.com/go/dataform/apiv1"
    	dataformpb "cloud.google.com/go/dataform/apiv1/dataformpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataform.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1.html#cloud_google_com_go_dataform_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1.html#cloud_google_com_go_dataform_apiv1_Client_Close)()
    
    	req := &dataformpb.GetReleaseConfigRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dataform/apiv1/dataformpb#GetReleaseConfigRequest.
    	}
    	resp, err := c.GetReleaseConfig(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*Client) GetRepository 
    
    
    func (c *Client) GetRepository(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dataformpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb).[GetRepositoryRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb#cloud_google_com_go_dataform_apiv1_dataformpb_GetRepositoryRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[dataformpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb).[Repository](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb#cloud_google_com_go_dataform_apiv1_dataformpb_Repository), [error](https://pkg.go.dev/builtin#error))

GetRepository fetches a single Repository.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dataform "cloud.google.com/go/dataform/apiv1"
    	dataformpb "cloud.google.com/go/dataform/apiv1/dataformpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataform.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1.html#cloud_google_com_go_dataform_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1.html#cloud_google_com_go_dataform_apiv1_Client_Close)()
    
    	req := &dataformpb.GetRepositoryRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dataform/apiv1/dataformpb#GetRepositoryRequest.
    	}
    	resp, err := c.GetRepository(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*Client) GetTeamFolder 
    
    
    func (c *Client) GetTeamFolder(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dataformpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb).[GetTeamFolderRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb#cloud_google_com_go_dataform_apiv1_dataformpb_GetTeamFolderRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[dataformpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb).[TeamFolder](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb#cloud_google_com_go_dataform_apiv1_dataformpb_TeamFolder), [error](https://pkg.go.dev/builtin#error))

GetTeamFolder fetches a single TeamFolder.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dataform "cloud.google.com/go/dataform/apiv1"
    	dataformpb "cloud.google.com/go/dataform/apiv1/dataformpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataform.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1.html#cloud_google_com_go_dataform_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1.html#cloud_google_com_go_dataform_apiv1_Client_Close)()
    
    	req := &dataformpb.GetTeamFolderRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dataform/apiv1/dataformpb#GetTeamFolderRequest.
    	}
    	resp, err := c.GetTeamFolder(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*Client) GetWorkflowConfig 
    
    
    func (c *Client) GetWorkflowConfig(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dataformpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb).[GetWorkflowConfigRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb#cloud_google_com_go_dataform_apiv1_dataformpb_GetWorkflowConfigRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[dataformpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb).[WorkflowConfig](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb#cloud_google_com_go_dataform_apiv1_dataformpb_WorkflowConfig), [error](https://pkg.go.dev/builtin#error))

GetWorkflowConfig fetches a single WorkflowConfig.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dataform "cloud.google.com/go/dataform/apiv1"
    	dataformpb "cloud.google.com/go/dataform/apiv1/dataformpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataform.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1.html#cloud_google_com_go_dataform_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1.html#cloud_google_com_go_dataform_apiv1_Client_Close)()
    
    	req := &dataformpb.GetWorkflowConfigRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dataform/apiv1/dataformpb#GetWorkflowConfigRequest.
    	}
    	resp, err := c.GetWorkflowConfig(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*Client) GetWorkflowInvocation 
    
    
    func (c *Client) GetWorkflowInvocation(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dataformpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb).[GetWorkflowInvocationRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb#cloud_google_com_go_dataform_apiv1_dataformpb_GetWorkflowInvocationRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[dataformpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb).[WorkflowInvocation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb#cloud_google_com_go_dataform_apiv1_dataformpb_WorkflowInvocation), [error](https://pkg.go.dev/builtin#error))

GetWorkflowInvocation fetches a single WorkflowInvocation.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dataform "cloud.google.com/go/dataform/apiv1"
    	dataformpb "cloud.google.com/go/dataform/apiv1/dataformpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataform.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1.html#cloud_google_com_go_dataform_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1.html#cloud_google_com_go_dataform_apiv1_Client_Close)()
    
    	req := &dataformpb.GetWorkflowInvocationRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dataform/apiv1/dataformpb#GetWorkflowInvocationRequest.
    	}
    	resp, err := c.GetWorkflowInvocation(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*Client) GetWorkspace 
    
    
    func (c *Client) GetWorkspace(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dataformpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb).[GetWorkspaceRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb#cloud_google_com_go_dataform_apiv1_dataformpb_GetWorkspaceRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[dataformpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb).[Workspace](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb#cloud_google_com_go_dataform_apiv1_dataformpb_Workspace), [error](https://pkg.go.dev/builtin#error))

GetWorkspace fetches a single Workspace.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dataform "cloud.google.com/go/dataform/apiv1"
    	dataformpb "cloud.google.com/go/dataform/apiv1/dataformpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataform.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1.html#cloud_google_com_go_dataform_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1.html#cloud_google_com_go_dataform_apiv1_Client_Close)()
    
    	req := &dataformpb.GetWorkspaceRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dataform/apiv1/dataformpb#GetWorkspaceRequest.
    	}
    	resp, err := c.GetWorkspace(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*Client) InstallNpmPackages 
    
    
    func (c *Client) InstallNpmPackages(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dataformpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb).[InstallNpmPackagesRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb#cloud_google_com_go_dataform_apiv1_dataformpb_InstallNpmPackagesRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[dataformpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb).[InstallNpmPackagesResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb#cloud_google_com_go_dataform_apiv1_dataformpb_InstallNpmPackagesResponse), [error](https://pkg.go.dev/builtin#error))

InstallNpmPackages installs dependency NPM packages (inside a Workspace).

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dataform "cloud.google.com/go/dataform/apiv1"
    	dataformpb "cloud.google.com/go/dataform/apiv1/dataformpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataform.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1.html#cloud_google_com_go_dataform_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1.html#cloud_google_com_go_dataform_apiv1_Client_Close)()
    
    	req := &dataformpb.InstallNpmPackagesRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dataform/apiv1/dataformpb#InstallNpmPackagesRequest.
    	}
    	resp, err := c.InstallNpmPackages(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*Client) ListCompilationResults 
    
    
    func (c *Client) ListCompilationResults(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dataformpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb).[ListCompilationResultsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb#cloud_google_com_go_dataform_apiv1_dataformpb_ListCompilationResultsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *CompilationResultIterator

ListCompilationResults lists CompilationResults in a given Repository.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	dataform "cloud.google.com/go/dataform/apiv1"
    	dataformpb "cloud.google.com/go/dataform/apiv1/dataformpb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataform.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1.html#cloud_google_com_go_dataform_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1.html#cloud_google_com_go_dataform_apiv1_Client_Close)()
    
    	req := &dataformpb.ListCompilationResultsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dataform/apiv1/dataformpb#ListCompilationResultsRequest.
    	}
    	it := c.ListCompilationResults(ctx, req)
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
    		_ = it.Response.(*dataformpb.ListCompilationResultsResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	dataform "cloud.google.com/go/dataform/apiv1"
    	dataformpb "cloud.google.com/go/dataform/apiv1/dataformpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataform.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1.html#cloud_google_com_go_dataform_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1.html#cloud_google_com_go_dataform_apiv1_Client_Close)()
    
    	req := &dataformpb.ListCompilationResultsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dataform/apiv1/dataformpb#ListCompilationResultsRequest.
    	}
    	for resp, err := range c.ListCompilationResults(ctx, req).All() {
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
    
    	dataform "cloud.google.com/go/dataform/apiv1"
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
    	c, err := dataform.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1.html#cloud_google_com_go_dataform_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1.html#cloud_google_com_go_dataform_apiv1_Client_Close)()
    
    	req := &locationpb.ListLocationsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#ListLocationsRequest.
    	}
    	it := c.[ListLocations](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1.html#cloud_google_com_go_dataform_apiv1_Client_ListLocations)(ctx, req)
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
    
    	dataform "cloud.google.com/go/dataform/apiv1"
    
    	locationpb "google.golang.org/genproto/googleapis/cloud/location"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataform.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1.html#cloud_google_com_go_dataform_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1.html#cloud_google_com_go_dataform_apiv1_Client_Close)()
    
    	req := &locationpb.ListLocationsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/google.golang.org/genproto/googleapis/cloud/location#ListLocationsRequest.
    	}
    	for resp, err := range c.[ListLocations](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1.html#cloud_google_com_go_dataform_apiv1_Client_ListLocations)(ctx, req).All() {
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
    
    	dataform "cloud.google.com/go/dataform/apiv1"
    
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
    	c, err := dataform.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1.html#cloud_google_com_go_dataform_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1.html#cloud_google_com_go_dataform_apiv1_Client_Close)()
    
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
    
    	dataform "cloud.google.com/go/dataform/apiv1"
    
    	longrunningpb "cloud.google.com/go/longrunning/autogen/longrunningpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataform.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1.html#cloud_google_com_go_dataform_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1.html#cloud_google_com_go_dataform_apiv1_Client_Close)()
    
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
    

### func (*Client) ListReleaseConfigs 
    
    
    func (c *Client) ListReleaseConfigs(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dataformpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb).[ListReleaseConfigsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb#cloud_google_com_go_dataform_apiv1_dataformpb_ListReleaseConfigsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *ReleaseConfigIterator

ListReleaseConfigs lists ReleaseConfigs in a given Repository.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	dataform "cloud.google.com/go/dataform/apiv1"
    	dataformpb "cloud.google.com/go/dataform/apiv1/dataformpb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataform.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1.html#cloud_google_com_go_dataform_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1.html#cloud_google_com_go_dataform_apiv1_Client_Close)()
    
    	req := &dataformpb.ListReleaseConfigsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dataform/apiv1/dataformpb#ListReleaseConfigsRequest.
    	}
    	it := c.ListReleaseConfigs(ctx, req)
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
    		_ = it.Response.(*dataformpb.ListReleaseConfigsResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	dataform "cloud.google.com/go/dataform/apiv1"
    	dataformpb "cloud.google.com/go/dataform/apiv1/dataformpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataform.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1.html#cloud_google_com_go_dataform_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1.html#cloud_google_com_go_dataform_apiv1_Client_Close)()
    
    	req := &dataformpb.ListReleaseConfigsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dataform/apiv1/dataformpb#ListReleaseConfigsRequest.
    	}
    	for resp, err := range c.ListReleaseConfigs(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*Client) ListRepositories 
    
    
    func (c *Client) ListRepositories(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dataformpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb).[ListRepositoriesRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb#cloud_google_com_go_dataform_apiv1_dataformpb_ListRepositoriesRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *RepositoryIterator

ListRepositories lists Repositories in a given project and location.

Note: This method can return repositories not shown in the Dataform UI (at <https://console.cloud.google.com/bigquery/dataform>).

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	dataform "cloud.google.com/go/dataform/apiv1"
    	dataformpb "cloud.google.com/go/dataform/apiv1/dataformpb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataform.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1.html#cloud_google_com_go_dataform_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1.html#cloud_google_com_go_dataform_apiv1_Client_Close)()
    
    	req := &dataformpb.ListRepositoriesRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dataform/apiv1/dataformpb#ListRepositoriesRequest.
    	}
    	it := c.ListRepositories(ctx, req)
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
    		_ = it.Response.(*dataformpb.ListRepositoriesResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	dataform "cloud.google.com/go/dataform/apiv1"
    	dataformpb "cloud.google.com/go/dataform/apiv1/dataformpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataform.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1.html#cloud_google_com_go_dataform_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1.html#cloud_google_com_go_dataform_apiv1_Client_Close)()
    
    	req := &dataformpb.ListRepositoriesRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dataform/apiv1/dataformpb#ListRepositoriesRequest.
    	}
    	for resp, err := range c.ListRepositories(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*Client) ListWorkflowConfigs 
    
    
    func (c *Client) ListWorkflowConfigs(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dataformpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb).[ListWorkflowConfigsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb#cloud_google_com_go_dataform_apiv1_dataformpb_ListWorkflowConfigsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *WorkflowConfigIterator

ListWorkflowConfigs lists WorkflowConfigs in a given Repository.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	dataform "cloud.google.com/go/dataform/apiv1"
    	dataformpb "cloud.google.com/go/dataform/apiv1/dataformpb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataform.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1.html#cloud_google_com_go_dataform_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1.html#cloud_google_com_go_dataform_apiv1_Client_Close)()
    
    	req := &dataformpb.ListWorkflowConfigsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dataform/apiv1/dataformpb#ListWorkflowConfigsRequest.
    	}
    	it := c.ListWorkflowConfigs(ctx, req)
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
    		_ = it.Response.(*dataformpb.ListWorkflowConfigsResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	dataform "cloud.google.com/go/dataform/apiv1"
    	dataformpb "cloud.google.com/go/dataform/apiv1/dataformpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataform.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1.html#cloud_google_com_go_dataform_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1.html#cloud_google_com_go_dataform_apiv1_Client_Close)()
    
    	req := &dataformpb.ListWorkflowConfigsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dataform/apiv1/dataformpb#ListWorkflowConfigsRequest.
    	}
    	for resp, err := range c.ListWorkflowConfigs(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*Client) ListWorkflowInvocations 
    
    
    func (c *Client) ListWorkflowInvocations(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dataformpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb).[ListWorkflowInvocationsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb#cloud_google_com_go_dataform_apiv1_dataformpb_ListWorkflowInvocationsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *WorkflowInvocationIterator

ListWorkflowInvocations lists WorkflowInvocations in a given Repository.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	dataform "cloud.google.com/go/dataform/apiv1"
    	dataformpb "cloud.google.com/go/dataform/apiv1/dataformpb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataform.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1.html#cloud_google_com_go_dataform_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1.html#cloud_google_com_go_dataform_apiv1_Client_Close)()
    
    	req := &dataformpb.ListWorkflowInvocationsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dataform/apiv1/dataformpb#ListWorkflowInvocationsRequest.
    	}
    	it := c.ListWorkflowInvocations(ctx, req)
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
    		_ = it.Response.(*dataformpb.ListWorkflowInvocationsResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	dataform "cloud.google.com/go/dataform/apiv1"
    	dataformpb "cloud.google.com/go/dataform/apiv1/dataformpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataform.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1.html#cloud_google_com_go_dataform_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1.html#cloud_google_com_go_dataform_apiv1_Client_Close)()
    
    	req := &dataformpb.ListWorkflowInvocationsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dataform/apiv1/dataformpb#ListWorkflowInvocationsRequest.
    	}
    	for resp, err := range c.ListWorkflowInvocations(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*Client) ListWorkspaces 
    
    
    func (c *Client) ListWorkspaces(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dataformpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb).[ListWorkspacesRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb#cloud_google_com_go_dataform_apiv1_dataformpb_ListWorkspacesRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *WorkspaceIterator

ListWorkspaces lists Workspaces in a given Repository.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	dataform "cloud.google.com/go/dataform/apiv1"
    	dataformpb "cloud.google.com/go/dataform/apiv1/dataformpb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataform.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1.html#cloud_google_com_go_dataform_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1.html#cloud_google_com_go_dataform_apiv1_Client_Close)()
    
    	req := &dataformpb.ListWorkspacesRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dataform/apiv1/dataformpb#ListWorkspacesRequest.
    	}
    	it := c.ListWorkspaces(ctx, req)
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
    		_ = it.Response.(*dataformpb.ListWorkspacesResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	dataform "cloud.google.com/go/dataform/apiv1"
    	dataformpb "cloud.google.com/go/dataform/apiv1/dataformpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataform.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1.html#cloud_google_com_go_dataform_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1.html#cloud_google_com_go_dataform_apiv1_Client_Close)()
    
    	req := &dataformpb.ListWorkspacesRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dataform/apiv1/dataformpb#ListWorkspacesRequest.
    	}
    	for resp, err := range c.ListWorkspaces(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*Client) MakeDirectory 
    
    
    func (c *Client) MakeDirectory(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dataformpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb).[MakeDirectoryRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb#cloud_google_com_go_dataform_apiv1_dataformpb_MakeDirectoryRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[dataformpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb).[MakeDirectoryResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb#cloud_google_com_go_dataform_apiv1_dataformpb_MakeDirectoryResponse), [error](https://pkg.go.dev/builtin#error))

MakeDirectory creates a directory inside a Workspace.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dataform "cloud.google.com/go/dataform/apiv1"
    	dataformpb "cloud.google.com/go/dataform/apiv1/dataformpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataform.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1.html#cloud_google_com_go_dataform_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1.html#cloud_google_com_go_dataform_apiv1_Client_Close)()
    
    	req := &dataformpb.MakeDirectoryRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dataform/apiv1/dataformpb#MakeDirectoryRequest.
    	}
    	resp, err := c.MakeDirectory(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*Client) MoveDirectory 
    
    
    func (c *Client) MoveDirectory(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dataformpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb).[MoveDirectoryRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb#cloud_google_com_go_dataform_apiv1_dataformpb_MoveDirectoryRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[dataformpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb).[MoveDirectoryResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb#cloud_google_com_go_dataform_apiv1_dataformpb_MoveDirectoryResponse), [error](https://pkg.go.dev/builtin#error))

MoveDirectory moves a directory (inside a Workspace), and all of its contents, to a new location.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dataform "cloud.google.com/go/dataform/apiv1"
    	dataformpb "cloud.google.com/go/dataform/apiv1/dataformpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataform.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1.html#cloud_google_com_go_dataform_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1.html#cloud_google_com_go_dataform_apiv1_Client_Close)()
    
    	req := &dataformpb.MoveDirectoryRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dataform/apiv1/dataformpb#MoveDirectoryRequest.
    	}
    	resp, err := c.MoveDirectory(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*Client) MoveFile 
    
    
    func (c *Client) MoveFile(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dataformpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb).[MoveFileRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb#cloud_google_com_go_dataform_apiv1_dataformpb_MoveFileRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[dataformpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb).[MoveFileResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb#cloud_google_com_go_dataform_apiv1_dataformpb_MoveFileResponse), [error](https://pkg.go.dev/builtin#error))

MoveFile moves a file (inside a Workspace) to a new location.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dataform "cloud.google.com/go/dataform/apiv1"
    	dataformpb "cloud.google.com/go/dataform/apiv1/dataformpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataform.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1.html#cloud_google_com_go_dataform_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1.html#cloud_google_com_go_dataform_apiv1_Client_Close)()
    
    	req := &dataformpb.MoveFileRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dataform/apiv1/dataformpb#MoveFileRequest.
    	}
    	resp, err := c.MoveFile(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*Client) MoveFolder 
    
    
    func (c *Client) MoveFolder(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dataformpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb).[MoveFolderRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb#cloud_google_com_go_dataform_apiv1_dataformpb_MoveFolderRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*MoveFolderOperation, [error](https://pkg.go.dev/builtin#error))

MoveFolder moves a Folder to a new Folder, TeamFolder, or the root location.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dataform "cloud.google.com/go/dataform/apiv1"
    	dataformpb "cloud.google.com/go/dataform/apiv1/dataformpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataform.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1.html#cloud_google_com_go_dataform_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1.html#cloud_google_com_go_dataform_apiv1_Client_Close)()
    
    	req := &dataformpb.MoveFolderRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dataform/apiv1/dataformpb#MoveFolderRequest.
    	}
    	op, err := c.MoveFolder(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    
    	err = op.Wait(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    }
    

### func (*Client) MoveFolderOperation 
    
    
    func (c *Client) MoveFolderOperation(name [string](https://pkg.go.dev/builtin#string)) *MoveFolderOperation

MoveFolderOperation returns a new MoveFolderOperation from a given name. The name must be that of a previously created MoveFolderOperation, possibly from a different process.

### func (*Client) MoveRepository 
    
    
    func (c *Client) MoveRepository(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dataformpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb).[MoveRepositoryRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb#cloud_google_com_go_dataform_apiv1_dataformpb_MoveRepositoryRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*MoveRepositoryOperation, [error](https://pkg.go.dev/builtin#error))

MoveRepository moves a Repository to a new location.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dataform "cloud.google.com/go/dataform/apiv1"
    	dataformpb "cloud.google.com/go/dataform/apiv1/dataformpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataform.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1.html#cloud_google_com_go_dataform_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1.html#cloud_google_com_go_dataform_apiv1_Client_Close)()
    
    	req := &dataformpb.MoveRepositoryRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dataform/apiv1/dataformpb#MoveRepositoryRequest.
    	}
    	op, err := c.MoveRepository(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    
    	err = op.Wait(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    }
    

### func (*Client) MoveRepositoryOperation 
    
    
    func (c *Client) MoveRepositoryOperation(name [string](https://pkg.go.dev/builtin#string)) *MoveRepositoryOperation

MoveRepositoryOperation returns a new MoveRepositoryOperation from a given name. The name must be that of a previously created MoveRepositoryOperation, possibly from a different process.

### func (*Client) PullGitCommits 
    
    
    func (c *Client) PullGitCommits(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dataformpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb).[PullGitCommitsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb#cloud_google_com_go_dataform_apiv1_dataformpb_PullGitCommitsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[dataformpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb).[PullGitCommitsResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb#cloud_google_com_go_dataform_apiv1_dataformpb_PullGitCommitsResponse), [error](https://pkg.go.dev/builtin#error))

PullGitCommits pulls Git commits from the Repository’s remote into a Workspace.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dataform "cloud.google.com/go/dataform/apiv1"
    	dataformpb "cloud.google.com/go/dataform/apiv1/dataformpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataform.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1.html#cloud_google_com_go_dataform_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1.html#cloud_google_com_go_dataform_apiv1_Client_Close)()
    
    	req := &dataformpb.PullGitCommitsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dataform/apiv1/dataformpb#PullGitCommitsRequest.
    	}
    	resp, err := c.PullGitCommits(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*Client) PushGitCommits 
    
    
    func (c *Client) PushGitCommits(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dataformpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb).[PushGitCommitsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb#cloud_google_com_go_dataform_apiv1_dataformpb_PushGitCommitsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[dataformpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb).[PushGitCommitsResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb#cloud_google_com_go_dataform_apiv1_dataformpb_PushGitCommitsResponse), [error](https://pkg.go.dev/builtin#error))

PushGitCommits pushes Git commits from a Workspace to the Repository’s remote.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dataform "cloud.google.com/go/dataform/apiv1"
    	dataformpb "cloud.google.com/go/dataform/apiv1/dataformpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataform.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1.html#cloud_google_com_go_dataform_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1.html#cloud_google_com_go_dataform_apiv1_Client_Close)()
    
    	req := &dataformpb.PushGitCommitsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dataform/apiv1/dataformpb#PushGitCommitsRequest.
    	}
    	resp, err := c.PushGitCommits(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*Client) QueryCompilationResultActions 
    
    
    func (c *Client) QueryCompilationResultActions(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dataformpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb).[QueryCompilationResultActionsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb#cloud_google_com_go_dataform_apiv1_dataformpb_QueryCompilationResultActionsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *CompilationResultActionIterator

QueryCompilationResultActions returns CompilationResultActions in a given CompilationResult.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	dataform "cloud.google.com/go/dataform/apiv1"
    	dataformpb "cloud.google.com/go/dataform/apiv1/dataformpb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataform.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1.html#cloud_google_com_go_dataform_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1.html#cloud_google_com_go_dataform_apiv1_Client_Close)()
    
    	req := &dataformpb.QueryCompilationResultActionsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dataform/apiv1/dataformpb#QueryCompilationResultActionsRequest.
    	}
    	it := c.QueryCompilationResultActions(ctx, req)
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
    		_ = it.Response.(*dataformpb.QueryCompilationResultActionsResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	dataform "cloud.google.com/go/dataform/apiv1"
    	dataformpb "cloud.google.com/go/dataform/apiv1/dataformpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataform.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1.html#cloud_google_com_go_dataform_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1.html#cloud_google_com_go_dataform_apiv1_Client_Close)()
    
    	req := &dataformpb.QueryCompilationResultActionsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dataform/apiv1/dataformpb#QueryCompilationResultActionsRequest.
    	}
    	for resp, err := range c.QueryCompilationResultActions(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*Client) QueryDirectoryContents 
    
    
    func (c *Client) QueryDirectoryContents(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dataformpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb).[QueryDirectoryContentsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb#cloud_google_com_go_dataform_apiv1_dataformpb_QueryDirectoryContentsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *DirectoryEntryIterator

QueryDirectoryContents returns the contents of a given Workspace directory.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	dataform "cloud.google.com/go/dataform/apiv1"
    	dataformpb "cloud.google.com/go/dataform/apiv1/dataformpb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataform.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1.html#cloud_google_com_go_dataform_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1.html#cloud_google_com_go_dataform_apiv1_Client_Close)()
    
    	req := &dataformpb.QueryDirectoryContentsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dataform/apiv1/dataformpb#QueryDirectoryContentsRequest.
    	}
    	it := c.QueryDirectoryContents(ctx, req)
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
    		_ = it.Response.(*dataformpb.QueryDirectoryContentsResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	dataform "cloud.google.com/go/dataform/apiv1"
    	dataformpb "cloud.google.com/go/dataform/apiv1/dataformpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataform.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1.html#cloud_google_com_go_dataform_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1.html#cloud_google_com_go_dataform_apiv1_Client_Close)()
    
    	req := &dataformpb.QueryDirectoryContentsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dataform/apiv1/dataformpb#QueryDirectoryContentsRequest.
    	}
    	for resp, err := range c.QueryDirectoryContents(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*Client) QueryFolderContents 
    
    
    func (c *Client) QueryFolderContents(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dataformpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb).[QueryFolderContentsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb#cloud_google_com_go_dataform_apiv1_dataformpb_QueryFolderContentsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *QueryFolderContentsResponse_FolderContentsEntryIterator

QueryFolderContents returns the contents of a given Folder.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	dataform "cloud.google.com/go/dataform/apiv1"
    	dataformpb "cloud.google.com/go/dataform/apiv1/dataformpb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataform.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1.html#cloud_google_com_go_dataform_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1.html#cloud_google_com_go_dataform_apiv1_Client_Close)()
    
    	req := &dataformpb.QueryFolderContentsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dataform/apiv1/dataformpb#QueryFolderContentsRequest.
    	}
    	it := c.QueryFolderContents(ctx, req)
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
    		_ = it.Response.(*dataformpb.QueryFolderContentsResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	dataform "cloud.google.com/go/dataform/apiv1"
    	dataformpb "cloud.google.com/go/dataform/apiv1/dataformpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataform.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1.html#cloud_google_com_go_dataform_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1.html#cloud_google_com_go_dataform_apiv1_Client_Close)()
    
    	req := &dataformpb.QueryFolderContentsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dataform/apiv1/dataformpb#QueryFolderContentsRequest.
    	}
    	for resp, err := range c.QueryFolderContents(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*Client) QueryRepositoryDirectoryContents 
    
    
    func (c *Client) QueryRepositoryDirectoryContents(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dataformpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb).[QueryRepositoryDirectoryContentsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb#cloud_google_com_go_dataform_apiv1_dataformpb_QueryRepositoryDirectoryContentsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *DirectoryEntryIterator

QueryRepositoryDirectoryContents returns the contents of a given Repository directory. The Repository must not have a value for git_remote_settings.url.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	dataform "cloud.google.com/go/dataform/apiv1"
    	dataformpb "cloud.google.com/go/dataform/apiv1/dataformpb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataform.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1.html#cloud_google_com_go_dataform_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1.html#cloud_google_com_go_dataform_apiv1_Client_Close)()
    
    	req := &dataformpb.QueryRepositoryDirectoryContentsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dataform/apiv1/dataformpb#QueryRepositoryDirectoryContentsRequest.
    	}
    	it := c.QueryRepositoryDirectoryContents(ctx, req)
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
    		_ = it.Response.(*dataformpb.QueryRepositoryDirectoryContentsResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	dataform "cloud.google.com/go/dataform/apiv1"
    	dataformpb "cloud.google.com/go/dataform/apiv1/dataformpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataform.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1.html#cloud_google_com_go_dataform_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1.html#cloud_google_com_go_dataform_apiv1_Client_Close)()
    
    	req := &dataformpb.QueryRepositoryDirectoryContentsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dataform/apiv1/dataformpb#QueryRepositoryDirectoryContentsRequest.
    	}
    	for resp, err := range c.QueryRepositoryDirectoryContents(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*Client) QueryTeamFolderContents 
    
    
    func (c *Client) QueryTeamFolderContents(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dataformpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb).[QueryTeamFolderContentsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb#cloud_google_com_go_dataform_apiv1_dataformpb_QueryTeamFolderContentsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *QueryTeamFolderContentsResponse_TeamFolderContentsEntryIterator

QueryTeamFolderContents returns the contents of a given TeamFolder.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	dataform "cloud.google.com/go/dataform/apiv1"
    	dataformpb "cloud.google.com/go/dataform/apiv1/dataformpb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataform.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1.html#cloud_google_com_go_dataform_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1.html#cloud_google_com_go_dataform_apiv1_Client_Close)()
    
    	req := &dataformpb.QueryTeamFolderContentsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dataform/apiv1/dataformpb#QueryTeamFolderContentsRequest.
    	}
    	it := c.QueryTeamFolderContents(ctx, req)
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
    		_ = it.Response.(*dataformpb.QueryTeamFolderContentsResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	dataform "cloud.google.com/go/dataform/apiv1"
    	dataformpb "cloud.google.com/go/dataform/apiv1/dataformpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataform.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1.html#cloud_google_com_go_dataform_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1.html#cloud_google_com_go_dataform_apiv1_Client_Close)()
    
    	req := &dataformpb.QueryTeamFolderContentsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dataform/apiv1/dataformpb#QueryTeamFolderContentsRequest.
    	}
    	for resp, err := range c.QueryTeamFolderContents(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*Client) QueryUserRootContents 
    
    
    func (c *Client) QueryUserRootContents(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dataformpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb).[QueryUserRootContentsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb#cloud_google_com_go_dataform_apiv1_dataformpb_QueryUserRootContentsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *QueryUserRootContentsResponse_RootContentsEntryIterator

QueryUserRootContents returns the contents of a caller’s root folder in a given location. The root folder contains all resources that are created by the user and not contained in any other folder.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	dataform "cloud.google.com/go/dataform/apiv1"
    	dataformpb "cloud.google.com/go/dataform/apiv1/dataformpb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataform.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1.html#cloud_google_com_go_dataform_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1.html#cloud_google_com_go_dataform_apiv1_Client_Close)()
    
    	req := &dataformpb.QueryUserRootContentsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dataform/apiv1/dataformpb#QueryUserRootContentsRequest.
    	}
    	it := c.QueryUserRootContents(ctx, req)
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
    		_ = it.Response.(*dataformpb.QueryUserRootContentsResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	dataform "cloud.google.com/go/dataform/apiv1"
    	dataformpb "cloud.google.com/go/dataform/apiv1/dataformpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataform.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1.html#cloud_google_com_go_dataform_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1.html#cloud_google_com_go_dataform_apiv1_Client_Close)()
    
    	req := &dataformpb.QueryUserRootContentsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dataform/apiv1/dataformpb#QueryUserRootContentsRequest.
    	}
    	for resp, err := range c.QueryUserRootContents(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*Client) QueryWorkflowInvocationActions 
    
    
    func (c *Client) QueryWorkflowInvocationActions(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dataformpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb).[QueryWorkflowInvocationActionsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb#cloud_google_com_go_dataform_apiv1_dataformpb_QueryWorkflowInvocationActionsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *WorkflowInvocationActionIterator

QueryWorkflowInvocationActions returns WorkflowInvocationActions in a given WorkflowInvocation.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	dataform "cloud.google.com/go/dataform/apiv1"
    	dataformpb "cloud.google.com/go/dataform/apiv1/dataformpb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataform.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1.html#cloud_google_com_go_dataform_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1.html#cloud_google_com_go_dataform_apiv1_Client_Close)()
    
    	req := &dataformpb.QueryWorkflowInvocationActionsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dataform/apiv1/dataformpb#QueryWorkflowInvocationActionsRequest.
    	}
    	it := c.QueryWorkflowInvocationActions(ctx, req)
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
    		_ = it.Response.(*dataformpb.QueryWorkflowInvocationActionsResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	dataform "cloud.google.com/go/dataform/apiv1"
    	dataformpb "cloud.google.com/go/dataform/apiv1/dataformpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataform.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1.html#cloud_google_com_go_dataform_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1.html#cloud_google_com_go_dataform_apiv1_Client_Close)()
    
    	req := &dataformpb.QueryWorkflowInvocationActionsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dataform/apiv1/dataformpb#QueryWorkflowInvocationActionsRequest.
    	}
    	for resp, err := range c.QueryWorkflowInvocationActions(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*Client) ReadFile 
    
    
    func (c *Client) ReadFile(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dataformpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb).[ReadFileRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb#cloud_google_com_go_dataform_apiv1_dataformpb_ReadFileRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[dataformpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb).[ReadFileResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb#cloud_google_com_go_dataform_apiv1_dataformpb_ReadFileResponse), [error](https://pkg.go.dev/builtin#error))

ReadFile returns the contents of a file (inside a Workspace).

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dataform "cloud.google.com/go/dataform/apiv1"
    	dataformpb "cloud.google.com/go/dataform/apiv1/dataformpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataform.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1.html#cloud_google_com_go_dataform_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1.html#cloud_google_com_go_dataform_apiv1_Client_Close)()
    
    	req := &dataformpb.ReadFileRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dataform/apiv1/dataformpb#ReadFileRequest.
    	}
    	resp, err := c.ReadFile(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*Client) ReadRepositoryFile 
    
    
    func (c *Client) ReadRepositoryFile(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dataformpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb).[ReadRepositoryFileRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb#cloud_google_com_go_dataform_apiv1_dataformpb_ReadRepositoryFileRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[dataformpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb).[ReadRepositoryFileResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb#cloud_google_com_go_dataform_apiv1_dataformpb_ReadRepositoryFileResponse), [error](https://pkg.go.dev/builtin#error))

ReadRepositoryFile returns the contents of a file (inside a Repository). The Repository must not have a value for git_remote_settings.url.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dataform "cloud.google.com/go/dataform/apiv1"
    	dataformpb "cloud.google.com/go/dataform/apiv1/dataformpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataform.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1.html#cloud_google_com_go_dataform_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1.html#cloud_google_com_go_dataform_apiv1_Client_Close)()
    
    	req := &dataformpb.ReadRepositoryFileRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dataform/apiv1/dataformpb#ReadRepositoryFileRequest.
    	}
    	resp, err := c.ReadRepositoryFile(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*Client) RemoveDirectory 
    
    
    func (c *Client) RemoveDirectory(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dataformpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb).[RemoveDirectoryRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb#cloud_google_com_go_dataform_apiv1_dataformpb_RemoveDirectoryRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[dataformpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb).[RemoveDirectoryResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb#cloud_google_com_go_dataform_apiv1_dataformpb_RemoveDirectoryResponse), [error](https://pkg.go.dev/builtin#error))

RemoveDirectory deletes a directory (inside a Workspace) and all of its contents.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dataform "cloud.google.com/go/dataform/apiv1"
    	dataformpb "cloud.google.com/go/dataform/apiv1/dataformpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataform.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1.html#cloud_google_com_go_dataform_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1.html#cloud_google_com_go_dataform_apiv1_Client_Close)()
    
    	req := &dataformpb.RemoveDirectoryRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dataform/apiv1/dataformpb#RemoveDirectoryRequest.
    	}
    	resp, err := c.RemoveDirectory(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*Client) RemoveFile 
    
    
    func (c *Client) RemoveFile(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dataformpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb).[RemoveFileRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb#cloud_google_com_go_dataform_apiv1_dataformpb_RemoveFileRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[dataformpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb).[RemoveFileResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb#cloud_google_com_go_dataform_apiv1_dataformpb_RemoveFileResponse), [error](https://pkg.go.dev/builtin#error))

RemoveFile deletes a file (inside a Workspace).

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dataform "cloud.google.com/go/dataform/apiv1"
    	dataformpb "cloud.google.com/go/dataform/apiv1/dataformpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataform.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1.html#cloud_google_com_go_dataform_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1.html#cloud_google_com_go_dataform_apiv1_Client_Close)()
    
    	req := &dataformpb.RemoveFileRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dataform/apiv1/dataformpb#RemoveFileRequest.
    	}
    	resp, err := c.RemoveFile(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*Client) ResetWorkspaceChanges 
    
    
    func (c *Client) ResetWorkspaceChanges(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dataformpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb).[ResetWorkspaceChangesRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb#cloud_google_com_go_dataform_apiv1_dataformpb_ResetWorkspaceChangesRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[dataformpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb).[ResetWorkspaceChangesResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb#cloud_google_com_go_dataform_apiv1_dataformpb_ResetWorkspaceChangesResponse), [error](https://pkg.go.dev/builtin#error))

ResetWorkspaceChanges performs a Git reset for uncommitted files in a Workspace.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dataform "cloud.google.com/go/dataform/apiv1"
    	dataformpb "cloud.google.com/go/dataform/apiv1/dataformpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataform.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1.html#cloud_google_com_go_dataform_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1.html#cloud_google_com_go_dataform_apiv1_Client_Close)()
    
    	req := &dataformpb.ResetWorkspaceChangesRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dataform/apiv1/dataformpb#ResetWorkspaceChangesRequest.
    	}
    	resp, err := c.ResetWorkspaceChanges(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*Client) SearchFiles 
    
    
    func (c *Client) SearchFiles(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dataformpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb).[SearchFilesRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb#cloud_google_com_go_dataform_apiv1_dataformpb_SearchFilesRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *SearchResultIterator

SearchFiles finds the contents of a given Workspace directory by filter.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	dataform "cloud.google.com/go/dataform/apiv1"
    	dataformpb "cloud.google.com/go/dataform/apiv1/dataformpb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataform.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1.html#cloud_google_com_go_dataform_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1.html#cloud_google_com_go_dataform_apiv1_Client_Close)()
    
    	req := &dataformpb.SearchFilesRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dataform/apiv1/dataformpb#SearchFilesRequest.
    	}
    	it := c.SearchFiles(ctx, req)
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
    		_ = it.Response.(*dataformpb.SearchFilesResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	dataform "cloud.google.com/go/dataform/apiv1"
    	dataformpb "cloud.google.com/go/dataform/apiv1/dataformpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataform.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1.html#cloud_google_com_go_dataform_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1.html#cloud_google_com_go_dataform_apiv1_Client_Close)()
    
    	req := &dataformpb.SearchFilesRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dataform/apiv1/dataformpb#SearchFilesRequest.
    	}
    	for resp, err := range c.SearchFiles(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*Client) SearchTeamFolders 
    
    
    func (c *Client) SearchTeamFolders(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dataformpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb).[SearchTeamFoldersRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb#cloud_google_com_go_dataform_apiv1_dataformpb_SearchTeamFoldersRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) *SearchTeamFoldersResponse_TeamFolderSearchResultIterator

SearchTeamFolders returns all TeamFolders in a given location that the caller has access to and match the provided filter.

#### Examples
    
    
    package main
    
    import (
    	"context"
    
    	dataform "cloud.google.com/go/dataform/apiv1"
    	dataformpb "cloud.google.com/go/dataform/apiv1/dataformpb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataform.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1.html#cloud_google_com_go_dataform_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1.html#cloud_google_com_go_dataform_apiv1_Client_Close)()
    
    	req := &dataformpb.SearchTeamFoldersRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dataform/apiv1/dataformpb#SearchTeamFoldersRequest.
    	}
    	it := c.SearchTeamFolders(ctx, req)
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
    		_ = it.Response.(*dataformpb.SearchTeamFoldersResponse)
    	}
    }
    

##### all
    
    
    package main
    
    import (
    	"context"
    
    	dataform "cloud.google.com/go/dataform/apiv1"
    	dataformpb "cloud.google.com/go/dataform/apiv1/dataformpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataform.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1.html#cloud_google_com_go_dataform_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1.html#cloud_google_com_go_dataform_apiv1_Client_Close)()
    
    	req := &dataformpb.SearchTeamFoldersRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dataform/apiv1/dataformpb#SearchTeamFoldersRequest.
    	}
    	for resp, err := range c.SearchTeamFolders(ctx, req).All() {
    		if err != nil {
    			// TODO: Handle error and break/return/continue. Iteration will stop after any error.
    		}
    		// TODO: Use resp.
    		_ = resp
    	}
    }
    

### func (*Client) SetIamPolicy 
    
    
    func (c *Client) SetIamPolicy(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[iampb](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb).[SetIamPolicyRequest](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb#SetIamPolicyRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[iampb](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb).[Policy](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb#Policy), [error](https://pkg.go.dev/builtin#error))

SetIamPolicy sets the access control policy on the specified resource. Replaces any existing policy.

Can return NOT_FOUND, INVALID_ARGUMENT, and PERMISSION_DENIED errors.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dataform "cloud.google.com/go/dataform/apiv1"
    
    	iampb "cloud.google.com/go/iam/apiv1/iampb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataform.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1.html#cloud_google_com_go_dataform_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1.html#cloud_google_com_go_dataform_apiv1_Client_Close)()
    
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
    

### func (*Client) TestIamPermissions 
    
    
    func (c *Client) TestIamPermissions(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[iampb](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb).[TestIamPermissionsRequest](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb#TestIamPermissionsRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[iampb](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb).[TestIamPermissionsResponse](https://pkg.go.dev/cloud.google.com/go/iam/apiv1/iampb#TestIamPermissionsResponse), [error](https://pkg.go.dev/builtin#error))

TestIamPermissions returns permissions that a caller has on the specified resource. If the resource does not exist, this will return an empty set of permissions, not a NOT_FOUND error.

Note: This operation is designed to be used for building permission-aware UIs and command-line tools, not for authorization checking. This operation may “fail open” without warning.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dataform "cloud.google.com/go/dataform/apiv1"
    
    	iampb "cloud.google.com/go/iam/apiv1/iampb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataform.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1.html#cloud_google_com_go_dataform_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1.html#cloud_google_com_go_dataform_apiv1_Client_Close)()
    
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
    

### func (*Client) UpdateConfig 
    
    
    func (c *Client) UpdateConfig(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dataformpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb).[UpdateConfigRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb#cloud_google_com_go_dataform_apiv1_dataformpb_UpdateConfigRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[dataformpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb).[Config](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb#cloud_google_com_go_dataform_apiv1_dataformpb_Config), [error](https://pkg.go.dev/builtin#error))

UpdateConfig update default config for a given project and location.

Note: This method does not fully implement AIP/134 (at <https://google.aip.dev/134>). The wildcard entry (*) is treated as a bad request, and when the field_mask is omitted, the request is treated as a full update on all modifiable fields.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dataform "cloud.google.com/go/dataform/apiv1"
    	dataformpb "cloud.google.com/go/dataform/apiv1/dataformpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataform.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1.html#cloud_google_com_go_dataform_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1.html#cloud_google_com_go_dataform_apiv1_Client_Close)()
    
    	req := &dataformpb.UpdateConfigRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dataform/apiv1/dataformpb#UpdateConfigRequest.
    	}
    	resp, err := c.UpdateConfig(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*Client) UpdateFolder 
    
    
    func (c *Client) UpdateFolder(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dataformpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb).[UpdateFolderRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb#cloud_google_com_go_dataform_apiv1_dataformpb_UpdateFolderRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[dataformpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb).[Folder](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb#cloud_google_com_go_dataform_apiv1_dataformpb_Folder), [error](https://pkg.go.dev/builtin#error))

UpdateFolder updates a single Folder.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dataform "cloud.google.com/go/dataform/apiv1"
    	dataformpb "cloud.google.com/go/dataform/apiv1/dataformpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataform.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1.html#cloud_google_com_go_dataform_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1.html#cloud_google_com_go_dataform_apiv1_Client_Close)()
    
    	req := &dataformpb.UpdateFolderRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dataform/apiv1/dataformpb#UpdateFolderRequest.
    	}
    	resp, err := c.UpdateFolder(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*Client) UpdateReleaseConfig 
    
    
    func (c *Client) UpdateReleaseConfig(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dataformpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb).[UpdateReleaseConfigRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb#cloud_google_com_go_dataform_apiv1_dataformpb_UpdateReleaseConfigRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[dataformpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb).[ReleaseConfig](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb#cloud_google_com_go_dataform_apiv1_dataformpb_ReleaseConfig), [error](https://pkg.go.dev/builtin#error))

UpdateReleaseConfig updates a single ReleaseConfig.

Note: This method does not fully implement AIP/134 (at <https://google.aip.dev/134>). The wildcard entry (*) is treated as a bad request, and when the field_mask is omitted, the request is treated as a full update on all modifiable fields.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dataform "cloud.google.com/go/dataform/apiv1"
    	dataformpb "cloud.google.com/go/dataform/apiv1/dataformpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataform.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1.html#cloud_google_com_go_dataform_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1.html#cloud_google_com_go_dataform_apiv1_Client_Close)()
    
    	req := &dataformpb.UpdateReleaseConfigRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dataform/apiv1/dataformpb#UpdateReleaseConfigRequest.
    	}
    	resp, err := c.UpdateReleaseConfig(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*Client) UpdateRepository 
    
    
    func (c *Client) UpdateRepository(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dataformpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb).[UpdateRepositoryRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb#cloud_google_com_go_dataform_apiv1_dataformpb_UpdateRepositoryRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[dataformpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb).[Repository](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb#cloud_google_com_go_dataform_apiv1_dataformpb_Repository), [error](https://pkg.go.dev/builtin#error))

UpdateRepository updates a single Repository.

Note: This method does not fully implement AIP/134 (at <https://google.aip.dev/134>). The wildcard entry (*) is treated as a bad request, and when the field_mask is omitted, the request is treated as a full update on all modifiable fields.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dataform "cloud.google.com/go/dataform/apiv1"
    	dataformpb "cloud.google.com/go/dataform/apiv1/dataformpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataform.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1.html#cloud_google_com_go_dataform_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1.html#cloud_google_com_go_dataform_apiv1_Client_Close)()
    
    	req := &dataformpb.UpdateRepositoryRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dataform/apiv1/dataformpb#UpdateRepositoryRequest.
    	}
    	resp, err := c.UpdateRepository(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*Client) UpdateTeamFolder 
    
    
    func (c *Client) UpdateTeamFolder(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dataformpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb).[UpdateTeamFolderRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb#cloud_google_com_go_dataform_apiv1_dataformpb_UpdateTeamFolderRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[dataformpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb).[TeamFolder](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb#cloud_google_com_go_dataform_apiv1_dataformpb_TeamFolder), [error](https://pkg.go.dev/builtin#error))

UpdateTeamFolder updates a single TeamFolder.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dataform "cloud.google.com/go/dataform/apiv1"
    	dataformpb "cloud.google.com/go/dataform/apiv1/dataformpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataform.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1.html#cloud_google_com_go_dataform_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1.html#cloud_google_com_go_dataform_apiv1_Client_Close)()
    
    	req := &dataformpb.UpdateTeamFolderRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dataform/apiv1/dataformpb#UpdateTeamFolderRequest.
    	}
    	resp, err := c.UpdateTeamFolder(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*Client) UpdateWorkflowConfig 
    
    
    func (c *Client) UpdateWorkflowConfig(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dataformpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb).[UpdateWorkflowConfigRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb#cloud_google_com_go_dataform_apiv1_dataformpb_UpdateWorkflowConfigRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[dataformpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb).[WorkflowConfig](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb#cloud_google_com_go_dataform_apiv1_dataformpb_WorkflowConfig), [error](https://pkg.go.dev/builtin#error))

UpdateWorkflowConfig updates a single WorkflowConfig.

Note: This method does not fully implement AIP/134 (at <https://google.aip.dev/134>). The wildcard entry (*) is treated as a bad request, and when the field_mask is omitted, the request is treated as a full update on all modifiable fields.

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dataform "cloud.google.com/go/dataform/apiv1"
    	dataformpb "cloud.google.com/go/dataform/apiv1/dataformpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataform.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1.html#cloud_google_com_go_dataform_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1.html#cloud_google_com_go_dataform_apiv1_Client_Close)()
    
    	req := &dataformpb.UpdateWorkflowConfigRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dataform/apiv1/dataformpb#UpdateWorkflowConfigRequest.
    	}
    	resp, err := c.UpdateWorkflowConfig(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### func (*Client) WriteFile 
    
    
    func (c *Client) WriteFile(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[dataformpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb).[WriteFileRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb#cloud_google_com_go_dataform_apiv1_dataformpb_WriteFileRequest), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) (*[dataformpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb).[WriteFileResponse](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb#cloud_google_com_go_dataform_apiv1_dataformpb_WriteFileResponse), [error](https://pkg.go.dev/builtin#error))

WriteFile writes to a file (inside a Workspace).

#### Example
    
    
    package main
    
    import (
    	"context"
    
    	dataform "cloud.google.com/go/dataform/apiv1"
    	dataformpb "cloud.google.com/go/dataform/apiv1/dataformpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataform.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1.html#cloud_google_com_go_dataform_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1.html#cloud_google_com_go_dataform_apiv1_Client_Close)()
    
    	req := &dataformpb.WriteFileRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dataform/apiv1/dataformpb#WriteFileRequest.
    	}
    	resp, err := c.WriteFile(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

## CommitLogEntryIterator
    
    
    type CommitLogEntryIterator struct {
    
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
    	InternalFetch func(pageSize [int](https://pkg.go.dev/builtin#int), pageToken [string](https://pkg.go.dev/builtin#string)) (results []*dataformpb.CommitLogEntry, nextPageToken [string](https://pkg.go.dev/builtin#string), err [error](https://pkg.go.dev/builtin#error))
    	// contains filtered or unexported fields
    }

CommitLogEntryIterator manages a stream of *dataformpb.CommitLogEntry.

### func (*CommitLogEntryIterator) All 
    
    
    func (it *CommitLogEntryIterator) All() iter.Seq2[*dataformpb.CommitLogEntry, error]

All returns an iterator. If an error is returned by the iterator, the iterator will stop after that iteration.

### func (*CommitLogEntryIterator) Next 
    
    
    func (it *CommitLogEntryIterator) Next() (*[dataformpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb).[CommitLogEntry](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb#cloud_google_com_go_dataform_apiv1_dataformpb_CommitLogEntry), [error](https://pkg.go.dev/builtin#error))

Next returns the next result. Its second return value is iterator.Done if there are no more results. Once Next returns Done, all subsequent calls will return Done.

### func (*CommitLogEntryIterator) PageInfo 
    
    
    func (it *CommitLogEntryIterator) PageInfo() *iterator.PageInfo

PageInfo supports pagination. See the [google.golang.org/api/iterator] package for details.

## CompilationResultActionIterator
    
    
    type CompilationResultActionIterator struct {
    
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
    	InternalFetch func(pageSize [int](https://pkg.go.dev/builtin#int), pageToken [string](https://pkg.go.dev/builtin#string)) (results []*dataformpb.CompilationResultAction, nextPageToken [string](https://pkg.go.dev/builtin#string), err [error](https://pkg.go.dev/builtin#error))
    	// contains filtered or unexported fields
    }

CompilationResultActionIterator manages a stream of *dataformpb.CompilationResultAction.

### func (*CompilationResultActionIterator) All 
    
    
    func (it *CompilationResultActionIterator) All() iter.Seq2[*dataformpb.CompilationResultAction, error]

All returns an iterator. If an error is returned by the iterator, the iterator will stop after that iteration.

### func (*CompilationResultActionIterator) Next 
    
    
    func (it *CompilationResultActionIterator) Next() (*[dataformpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb).[CompilationResultAction](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb#cloud_google_com_go_dataform_apiv1_dataformpb_CompilationResultAction), [error](https://pkg.go.dev/builtin#error))

Next returns the next result. Its second return value is iterator.Done if there are no more results. Once Next returns Done, all subsequent calls will return Done.

### func (*CompilationResultActionIterator) PageInfo 
    
    
    func (it *CompilationResultActionIterator) PageInfo() *iterator.PageInfo

PageInfo supports pagination. See the [google.golang.org/api/iterator] package for details.

## CompilationResultIterator
    
    
    type CompilationResultIterator struct {
    
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
    	InternalFetch func(pageSize [int](https://pkg.go.dev/builtin#int), pageToken [string](https://pkg.go.dev/builtin#string)) (results []*dataformpb.CompilationResult, nextPageToken [string](https://pkg.go.dev/builtin#string), err [error](https://pkg.go.dev/builtin#error))
    	// contains filtered or unexported fields
    }

CompilationResultIterator manages a stream of *dataformpb.CompilationResult.

### func (*CompilationResultIterator) All 
    
    
    func (it *CompilationResultIterator) All() iter.Seq2[*dataformpb.CompilationResult, error]

All returns an iterator. If an error is returned by the iterator, the iterator will stop after that iteration.

### func (*CompilationResultIterator) Next 
    
    
    func (it *CompilationResultIterator) Next() (*[dataformpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb).[CompilationResult](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb#cloud_google_com_go_dataform_apiv1_dataformpb_CompilationResult), [error](https://pkg.go.dev/builtin#error))

Next returns the next result. Its second return value is iterator.Done if there are no more results. Once Next returns Done, all subsequent calls will return Done.

### func (*CompilationResultIterator) PageInfo 
    
    
    func (it *CompilationResultIterator) PageInfo() *iterator.PageInfo

PageInfo supports pagination. See the [google.golang.org/api/iterator] package for details.

## DeleteFolderTreeOperation
    
    
    type DeleteFolderTreeOperation struct {
    	// contains filtered or unexported fields
    }

DeleteFolderTreeOperation manages a long-running operation from DeleteFolderTree.

### func (*DeleteFolderTreeOperation) Done 
    
    
    func (op *DeleteFolderTreeOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*DeleteFolderTreeOperation) Metadata 
    
    
    func (op *DeleteFolderTreeOperation) Metadata() (*[dataformpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb).[DeleteFolderTreeMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb#cloud_google_com_go_dataform_apiv1_dataformpb_DeleteFolderTreeMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*DeleteFolderTreeOperation) Name 
    
    
    func (op *DeleteFolderTreeOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*DeleteFolderTreeOperation) Poll 
    
    
    func (op *DeleteFolderTreeOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*DeleteFolderTreeOperation) Wait 
    
    
    func (op *DeleteFolderTreeOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## DeleteTeamFolderTreeOperation
    
    
    type DeleteTeamFolderTreeOperation struct {
    	// contains filtered or unexported fields
    }

DeleteTeamFolderTreeOperation manages a long-running operation from DeleteTeamFolderTree.

### func (*DeleteTeamFolderTreeOperation) Done 
    
    
    func (op *DeleteTeamFolderTreeOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*DeleteTeamFolderTreeOperation) Metadata 
    
    
    func (op *DeleteTeamFolderTreeOperation) Metadata() (*[dataformpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb).[DeleteFolderTreeMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb#cloud_google_com_go_dataform_apiv1_dataformpb_DeleteFolderTreeMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*DeleteTeamFolderTreeOperation) Name 
    
    
    func (op *DeleteTeamFolderTreeOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*DeleteTeamFolderTreeOperation) Poll 
    
    
    func (op *DeleteTeamFolderTreeOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*DeleteTeamFolderTreeOperation) Wait 
    
    
    func (op *DeleteTeamFolderTreeOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## DirectoryEntryIterator
    
    
    type DirectoryEntryIterator struct {
    
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
    	InternalFetch func(pageSize [int](https://pkg.go.dev/builtin#int), pageToken [string](https://pkg.go.dev/builtin#string)) (results []*dataformpb.DirectoryEntry, nextPageToken [string](https://pkg.go.dev/builtin#string), err [error](https://pkg.go.dev/builtin#error))
    	// contains filtered or unexported fields
    }

DirectoryEntryIterator manages a stream of *dataformpb.DirectoryEntry.

### func (*DirectoryEntryIterator) All 
    
    
    func (it *DirectoryEntryIterator) All() iter.Seq2[*dataformpb.DirectoryEntry, error]

All returns an iterator. If an error is returned by the iterator, the iterator will stop after that iteration.

### func (*DirectoryEntryIterator) Next 
    
    
    func (it *DirectoryEntryIterator) Next() (*[dataformpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb).[DirectoryEntry](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb#cloud_google_com_go_dataform_apiv1_dataformpb_DirectoryEntry), [error](https://pkg.go.dev/builtin#error))

Next returns the next result. Its second return value is iterator.Done if there are no more results. Once Next returns Done, all subsequent calls will return Done.

### func (*DirectoryEntryIterator) PageInfo 
    
    
    func (it *DirectoryEntryIterator) PageInfo() *iterator.PageInfo

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

## MoveFolderOperation
    
    
    type MoveFolderOperation struct {
    	// contains filtered or unexported fields
    }

MoveFolderOperation manages a long-running operation from MoveFolder.

### func (*MoveFolderOperation) Done 
    
    
    func (op *MoveFolderOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*MoveFolderOperation) Metadata 
    
    
    func (op *MoveFolderOperation) Metadata() (*[dataformpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb).[MoveFolderMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb#cloud_google_com_go_dataform_apiv1_dataformpb_MoveFolderMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*MoveFolderOperation) Name 
    
    
    func (op *MoveFolderOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*MoveFolderOperation) Poll 
    
    
    func (op *MoveFolderOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*MoveFolderOperation) Wait 
    
    
    func (op *MoveFolderOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

Wait blocks until the long-running operation is completed, returning the response and any errors encountered.

See documentation of Poll for error-handling information.

## MoveRepositoryOperation
    
    
    type MoveRepositoryOperation struct {
    	// contains filtered or unexported fields
    }

MoveRepositoryOperation manages a long-running operation from MoveRepository.

### func (*MoveRepositoryOperation) Done 
    
    
    func (op *MoveRepositoryOperation) Done() [bool](https://pkg.go.dev/builtin#bool)

Done reports whether the long-running operation has completed.

### func (*MoveRepositoryOperation) Metadata 
    
    
    func (op *MoveRepositoryOperation) Metadata() (*[dataformpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb).[MoveRepositoryMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb#cloud_google_com_go_dataform_apiv1_dataformpb_MoveRepositoryMetadata), [error](https://pkg.go.dev/builtin#error))

Metadata returns metadata associated with the long-running operation. Metadata itself does not contact the server, but Poll does. To get the latest metadata, call this method after a successful call to Poll. If the metadata is not available, the returned metadata and error are both nil.

### func (*MoveRepositoryOperation) Name 
    
    
    func (op *MoveRepositoryOperation) Name() [string](https://pkg.go.dev/builtin#string)

Name returns the name of the long-running operation. The name is assigned by the server and is unique within the service from which the operation is created.

### func (*MoveRepositoryOperation) Poll 
    
    
    func (op *MoveRepositoryOperation) Poll(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

Poll fetches the latest state of the long-running operation.

Poll also fetches the latest metadata, which can be retrieved by Metadata.

If Poll fails, the error is returned and op is unmodified. If Poll succeeds and the operation has completed with failure, the error is returned and op.Done will return true. If Poll succeeds and the operation has completed successfully, op.Done will return true, and the response of the operation is returned. If Poll succeeds and the operation has not completed, the returned response and error are both nil.

### func (*MoveRepositoryOperation) Wait 
    
    
    func (op *MoveRepositoryOperation) Wait(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), opts ...[gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2).[CallOption](https://pkg.go.dev/github.com/googleapis/gax-go/v2#CallOption)) [error](https://pkg.go.dev/builtin#error)

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

## QueryFolderContentsResponse_FolderContentsEntryIterator
    
    
    type QueryFolderContentsResponse_FolderContentsEntryIterator struct {
    
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
    	InternalFetch func(pageSize [int](https://pkg.go.dev/builtin#int), pageToken [string](https://pkg.go.dev/builtin#string)) (results []*dataformpb.QueryFolderContentsResponse_FolderContentsEntry, nextPageToken [string](https://pkg.go.dev/builtin#string), err [error](https://pkg.go.dev/builtin#error))
    	// contains filtered or unexported fields
    }

QueryFolderContentsResponse_FolderContentsEntryIterator manages a stream of *dataformpb.QueryFolderContentsResponse_FolderContentsEntry.

### func (*QueryFolderContentsResponse_FolderContentsEntryIterator) All 
    
    
    func (it *QueryFolderContentsResponse_FolderContentsEntryIterator) All() iter.Seq2[*dataformpb.QueryFolderContentsResponse_FolderContentsEntry, error]

All returns an iterator. If an error is returned by the iterator, the iterator will stop after that iteration.

### func (*QueryFolderContentsResponse_FolderContentsEntryIterator) Next 
    
    
    func (it *QueryFolderContentsResponse_FolderContentsEntryIterator) Next() (*[dataformpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb).[QueryFolderContentsResponse_FolderContentsEntry](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb#cloud_google_com_go_dataform_apiv1_dataformpb_QueryFolderContentsResponse_FolderContentsEntry), [error](https://pkg.go.dev/builtin#error))

Next returns the next result. Its second return value is iterator.Done if there are no more results. Once Next returns Done, all subsequent calls will return Done.

### func (*QueryFolderContentsResponse_FolderContentsEntryIterator) PageInfo 
    
    
    func (it *QueryFolderContentsResponse_FolderContentsEntryIterator) PageInfo() *iterator.PageInfo

PageInfo supports pagination. See the [google.golang.org/api/iterator] package for details.

## QueryTeamFolderContentsResponse_TeamFolderContentsEntryIterator
    
    
    type QueryTeamFolderContentsResponse_TeamFolderContentsEntryIterator struct {
    
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
    	InternalFetch func(pageSize [int](https://pkg.go.dev/builtin#int), pageToken [string](https://pkg.go.dev/builtin#string)) (results []*dataformpb.QueryTeamFolderContentsResponse_TeamFolderContentsEntry, nextPageToken [string](https://pkg.go.dev/builtin#string), err [error](https://pkg.go.dev/builtin#error))
    	// contains filtered or unexported fields
    }

QueryTeamFolderContentsResponse_TeamFolderContentsEntryIterator manages a stream of *dataformpb.QueryTeamFolderContentsResponse_TeamFolderContentsEntry.

### func (*QueryTeamFolderContentsResponse_TeamFolderContentsEntryIterator) All 
    
    
    func (it *QueryTeamFolderContentsResponse_TeamFolderContentsEntryIterator) All() iter.Seq2[*dataformpb.QueryTeamFolderContentsResponse_TeamFolderContentsEntry, error]

All returns an iterator. If an error is returned by the iterator, the iterator will stop after that iteration.

### func (*QueryTeamFolderContentsResponse_TeamFolderContentsEntryIterator) Next 
    
    
    func (it *QueryTeamFolderContentsResponse_TeamFolderContentsEntryIterator) Next() (*[dataformpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb).[QueryTeamFolderContentsResponse_TeamFolderContentsEntry](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb#cloud_google_com_go_dataform_apiv1_dataformpb_QueryTeamFolderContentsResponse_TeamFolderContentsEntry), [error](https://pkg.go.dev/builtin#error))

Next returns the next result. Its second return value is iterator.Done if there are no more results. Once Next returns Done, all subsequent calls will return Done.

### func (*QueryTeamFolderContentsResponse_TeamFolderContentsEntryIterator) PageInfo 
    
    
    func (it *QueryTeamFolderContentsResponse_TeamFolderContentsEntryIterator) PageInfo() *iterator.PageInfo

PageInfo supports pagination. See the [google.golang.org/api/iterator] package for details.

## QueryUserRootContentsResponse_RootContentsEntryIterator
    
    
    type QueryUserRootContentsResponse_RootContentsEntryIterator struct {
    
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
    	InternalFetch func(pageSize [int](https://pkg.go.dev/builtin#int), pageToken [string](https://pkg.go.dev/builtin#string)) (results []*dataformpb.QueryUserRootContentsResponse_RootContentsEntry, nextPageToken [string](https://pkg.go.dev/builtin#string), err [error](https://pkg.go.dev/builtin#error))
    	// contains filtered or unexported fields
    }

QueryUserRootContentsResponse_RootContentsEntryIterator manages a stream of *dataformpb.QueryUserRootContentsResponse_RootContentsEntry.

### func (*QueryUserRootContentsResponse_RootContentsEntryIterator) All 
    
    
    func (it *QueryUserRootContentsResponse_RootContentsEntryIterator) All() iter.Seq2[*dataformpb.QueryUserRootContentsResponse_RootContentsEntry, error]

All returns an iterator. If an error is returned by the iterator, the iterator will stop after that iteration.

### func (*QueryUserRootContentsResponse_RootContentsEntryIterator) Next 
    
    
    func (it *QueryUserRootContentsResponse_RootContentsEntryIterator) Next() (*[dataformpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb).[QueryUserRootContentsResponse_RootContentsEntry](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb#cloud_google_com_go_dataform_apiv1_dataformpb_QueryUserRootContentsResponse_RootContentsEntry), [error](https://pkg.go.dev/builtin#error))

Next returns the next result. Its second return value is iterator.Done if there are no more results. Once Next returns Done, all subsequent calls will return Done.

### func (*QueryUserRootContentsResponse_RootContentsEntryIterator) PageInfo 
    
    
    func (it *QueryUserRootContentsResponse_RootContentsEntryIterator) PageInfo() *iterator.PageInfo

PageInfo supports pagination. See the [google.golang.org/api/iterator] package for details.

## ReleaseConfigIterator
    
    
    type ReleaseConfigIterator struct {
    
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
    	InternalFetch func(pageSize [int](https://pkg.go.dev/builtin#int), pageToken [string](https://pkg.go.dev/builtin#string)) (results []*dataformpb.ReleaseConfig, nextPageToken [string](https://pkg.go.dev/builtin#string), err [error](https://pkg.go.dev/builtin#error))
    	// contains filtered or unexported fields
    }

ReleaseConfigIterator manages a stream of *dataformpb.ReleaseConfig.

### func (*ReleaseConfigIterator) All 
    
    
    func (it *ReleaseConfigIterator) All() iter.Seq2[*dataformpb.ReleaseConfig, error]

All returns an iterator. If an error is returned by the iterator, the iterator will stop after that iteration.

### func (*ReleaseConfigIterator) Next 
    
    
    func (it *ReleaseConfigIterator) Next() (*[dataformpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb).[ReleaseConfig](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb#cloud_google_com_go_dataform_apiv1_dataformpb_ReleaseConfig), [error](https://pkg.go.dev/builtin#error))

Next returns the next result. Its second return value is iterator.Done if there are no more results. Once Next returns Done, all subsequent calls will return Done.

### func (*ReleaseConfigIterator) PageInfo 
    
    
    func (it *ReleaseConfigIterator) PageInfo() *iterator.PageInfo

PageInfo supports pagination. See the [google.golang.org/api/iterator] package for details.

## RepositoryIterator
    
    
    type RepositoryIterator struct {
    
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
    	InternalFetch func(pageSize [int](https://pkg.go.dev/builtin#int), pageToken [string](https://pkg.go.dev/builtin#string)) (results []*dataformpb.Repository, nextPageToken [string](https://pkg.go.dev/builtin#string), err [error](https://pkg.go.dev/builtin#error))
    	// contains filtered or unexported fields
    }

RepositoryIterator manages a stream of *dataformpb.Repository.

### func (*RepositoryIterator) All 
    
    
    func (it *RepositoryIterator) All() iter.Seq2[*dataformpb.Repository, error]

All returns an iterator. If an error is returned by the iterator, the iterator will stop after that iteration.

### func (*RepositoryIterator) Next 
    
    
    func (it *RepositoryIterator) Next() (*[dataformpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb).[Repository](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb#cloud_google_com_go_dataform_apiv1_dataformpb_Repository), [error](https://pkg.go.dev/builtin#error))

Next returns the next result. Its second return value is iterator.Done if there are no more results. Once Next returns Done, all subsequent calls will return Done.

### func (*RepositoryIterator) PageInfo 
    
    
    func (it *RepositoryIterator) PageInfo() *iterator.PageInfo

PageInfo supports pagination. See the [google.golang.org/api/iterator] package for details.

## SearchResultIterator
    
    
    type SearchResultIterator struct {
    
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
    	InternalFetch func(pageSize [int](https://pkg.go.dev/builtin#int), pageToken [string](https://pkg.go.dev/builtin#string)) (results []*dataformpb.SearchResult, nextPageToken [string](https://pkg.go.dev/builtin#string), err [error](https://pkg.go.dev/builtin#error))
    	// contains filtered or unexported fields
    }

SearchResultIterator manages a stream of *dataformpb.SearchResult.

### func (*SearchResultIterator) All 
    
    
    func (it *SearchResultIterator) All() iter.Seq2[*dataformpb.SearchResult, error]

All returns an iterator. If an error is returned by the iterator, the iterator will stop after that iteration.

### func (*SearchResultIterator) Next 
    
    
    func (it *SearchResultIterator) Next() (*[dataformpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb).[SearchResult](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb#cloud_google_com_go_dataform_apiv1_dataformpb_SearchResult), [error](https://pkg.go.dev/builtin#error))

Next returns the next result. Its second return value is iterator.Done if there are no more results. Once Next returns Done, all subsequent calls will return Done.

### func (*SearchResultIterator) PageInfo 
    
    
    func (it *SearchResultIterator) PageInfo() *iterator.PageInfo

PageInfo supports pagination. See the [google.golang.org/api/iterator] package for details.

## SearchTeamFoldersResponse_TeamFolderSearchResultIterator
    
    
    type SearchTeamFoldersResponse_TeamFolderSearchResultIterator struct {
    
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
    	InternalFetch func(pageSize [int](https://pkg.go.dev/builtin#int), pageToken [string](https://pkg.go.dev/builtin#string)) (results []*dataformpb.SearchTeamFoldersResponse_TeamFolderSearchResult, nextPageToken [string](https://pkg.go.dev/builtin#string), err [error](https://pkg.go.dev/builtin#error))
    	// contains filtered or unexported fields
    }

SearchTeamFoldersResponse_TeamFolderSearchResultIterator manages a stream of *dataformpb.SearchTeamFoldersResponse_TeamFolderSearchResult.

### func (*SearchTeamFoldersResponse_TeamFolderSearchResultIterator) All 
    
    
    func (it *SearchTeamFoldersResponse_TeamFolderSearchResultIterator) All() iter.Seq2[*dataformpb.SearchTeamFoldersResponse_TeamFolderSearchResult, error]

All returns an iterator. If an error is returned by the iterator, the iterator will stop after that iteration.

### func (*SearchTeamFoldersResponse_TeamFolderSearchResultIterator) Next 
    
    
    func (it *SearchTeamFoldersResponse_TeamFolderSearchResultIterator) Next() (*[dataformpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb).[SearchTeamFoldersResponse_TeamFolderSearchResult](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb#cloud_google_com_go_dataform_apiv1_dataformpb_SearchTeamFoldersResponse_TeamFolderSearchResult), [error](https://pkg.go.dev/builtin#error))

Next returns the next result. Its second return value is iterator.Done if there are no more results. Once Next returns Done, all subsequent calls will return Done.

### func (*SearchTeamFoldersResponse_TeamFolderSearchResultIterator) PageInfo 
    
    
    func (it *SearchTeamFoldersResponse_TeamFolderSearchResultIterator) PageInfo() *iterator.PageInfo

PageInfo supports pagination. See the [google.golang.org/api/iterator] package for details.

## WorkflowConfigIterator
    
    
    type WorkflowConfigIterator struct {
    
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
    	InternalFetch func(pageSize [int](https://pkg.go.dev/builtin#int), pageToken [string](https://pkg.go.dev/builtin#string)) (results []*dataformpb.WorkflowConfig, nextPageToken [string](https://pkg.go.dev/builtin#string), err [error](https://pkg.go.dev/builtin#error))
    	// contains filtered or unexported fields
    }

WorkflowConfigIterator manages a stream of *dataformpb.WorkflowConfig.

### func (*WorkflowConfigIterator) All 
    
    
    func (it *WorkflowConfigIterator) All() iter.Seq2[*dataformpb.WorkflowConfig, error]

All returns an iterator. If an error is returned by the iterator, the iterator will stop after that iteration.

### func (*WorkflowConfigIterator) Next 
    
    
    func (it *WorkflowConfigIterator) Next() (*[dataformpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb).[WorkflowConfig](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb#cloud_google_com_go_dataform_apiv1_dataformpb_WorkflowConfig), [error](https://pkg.go.dev/builtin#error))

Next returns the next result. Its second return value is iterator.Done if there are no more results. Once Next returns Done, all subsequent calls will return Done.

### func (*WorkflowConfigIterator) PageInfo 
    
    
    func (it *WorkflowConfigIterator) PageInfo() *iterator.PageInfo

PageInfo supports pagination. See the [google.golang.org/api/iterator] package for details.

## WorkflowInvocationActionIterator
    
    
    type WorkflowInvocationActionIterator struct {
    
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
    	InternalFetch func(pageSize [int](https://pkg.go.dev/builtin#int), pageToken [string](https://pkg.go.dev/builtin#string)) (results []*dataformpb.WorkflowInvocationAction, nextPageToken [string](https://pkg.go.dev/builtin#string), err [error](https://pkg.go.dev/builtin#error))
    	// contains filtered or unexported fields
    }

WorkflowInvocationActionIterator manages a stream of *dataformpb.WorkflowInvocationAction.

### func (*WorkflowInvocationActionIterator) All 
    
    
    func (it *WorkflowInvocationActionIterator) All() iter.Seq2[*dataformpb.WorkflowInvocationAction, error]

All returns an iterator. If an error is returned by the iterator, the iterator will stop after that iteration.

### func (*WorkflowInvocationActionIterator) Next 
    
    
    func (it *WorkflowInvocationActionIterator) Next() (*[dataformpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb).[WorkflowInvocationAction](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb#cloud_google_com_go_dataform_apiv1_dataformpb_WorkflowInvocationAction), [error](https://pkg.go.dev/builtin#error))

Next returns the next result. Its second return value is iterator.Done if there are no more results. Once Next returns Done, all subsequent calls will return Done.

### func (*WorkflowInvocationActionIterator) PageInfo 
    
    
    func (it *WorkflowInvocationActionIterator) PageInfo() *iterator.PageInfo

PageInfo supports pagination. See the [google.golang.org/api/iterator] package for details.

## WorkflowInvocationIterator
    
    
    type WorkflowInvocationIterator struct {
    
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
    	InternalFetch func(pageSize [int](https://pkg.go.dev/builtin#int), pageToken [string](https://pkg.go.dev/builtin#string)) (results []*dataformpb.WorkflowInvocation, nextPageToken [string](https://pkg.go.dev/builtin#string), err [error](https://pkg.go.dev/builtin#error))
    	// contains filtered or unexported fields
    }

WorkflowInvocationIterator manages a stream of *dataformpb.WorkflowInvocation.

### func (*WorkflowInvocationIterator) All 
    
    
    func (it *WorkflowInvocationIterator) All() iter.Seq2[*dataformpb.WorkflowInvocation, error]

All returns an iterator. If an error is returned by the iterator, the iterator will stop after that iteration.

### func (*WorkflowInvocationIterator) Next 
    
    
    func (it *WorkflowInvocationIterator) Next() (*[dataformpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb).[WorkflowInvocation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb#cloud_google_com_go_dataform_apiv1_dataformpb_WorkflowInvocation), [error](https://pkg.go.dev/builtin#error))

Next returns the next result. Its second return value is iterator.Done if there are no more results. Once Next returns Done, all subsequent calls will return Done.

### func (*WorkflowInvocationIterator) PageInfo 
    
    
    func (it *WorkflowInvocationIterator) PageInfo() *iterator.PageInfo

PageInfo supports pagination. See the [google.golang.org/api/iterator] package for details.

## WorkspaceIterator
    
    
    type WorkspaceIterator struct {
    
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
    	InternalFetch func(pageSize [int](https://pkg.go.dev/builtin#int), pageToken [string](https://pkg.go.dev/builtin#string)) (results []*dataformpb.Workspace, nextPageToken [string](https://pkg.go.dev/builtin#string), err [error](https://pkg.go.dev/builtin#error))
    	// contains filtered or unexported fields
    }

WorkspaceIterator manages a stream of *dataformpb.Workspace.

### func (*WorkspaceIterator) All 
    
    
    func (it *WorkspaceIterator) All() iter.Seq2[*dataformpb.Workspace, error]

All returns an iterator. If an error is returned by the iterator, the iterator will stop after that iteration.

### func (*WorkspaceIterator) Next 
    
    
    func (it *WorkspaceIterator) Next() (*[dataformpb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb).[Workspace](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataform/latest/apiv1/dataformpb#cloud_google_com_go_dataform_apiv1_dataformpb_Workspace), [error](https://pkg.go.dev/builtin#error))

Next returns the next result. Its second return value is iterator.Done if there are no more results. Once Next returns Done, all subsequent calls will return Done.

### func (*WorkspaceIterator) PageInfo 
    
    
    func (it *WorkspaceIterator) PageInfo() *iterator.PageInfo

PageInfo supports pagination. See the [google.golang.org/api/iterator] package for details.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
