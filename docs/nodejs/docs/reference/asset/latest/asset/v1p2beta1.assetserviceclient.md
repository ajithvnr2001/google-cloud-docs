---
url: https://docs.cloud.google.com/nodejs/docs/reference/asset/latest/asset/v1p2beta1.assetserviceclient
title: Class v1p2beta1.AssetServiceClient (7.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:33:14.988785+00:00
---

# Class v1p2beta1.AssetServiceClient (7.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/asset/latest/asset/v1p2beta1.assetserviceclient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class v1p2beta1.AssetServiceClient (7.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

7.1.1 (latest)  7.0.1  6.3.3  5.5.0  5.3.0  5.2.0  5.1.0  5.0.1  4.6.3  4.5.0  4.4.0  4.3.0  4.2.0  4.1.0  3.23.1  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.1  3.15.5  3.14.1  3.13.0 

Asset service definition. v1p2beta1

## Package

[@google-cloud/asset](https://docs.cloud.google.com/nodejs/docs/reference/asset/latest/overview.html)

## Constructors 

### (constructor)(opts, gaxInstance)
    
    
    constructor(opts?: ClientOptions, gaxInstance?: typeof gax | typeof gax.fallback);

Construct an instance of AssetServiceClient.

**Parameters**  
---  
**Name** | **Description**  
`opts` |  `ClientOptions`   
  
`gaxInstance` |  `typeof gax | typeof fallback`   
: loaded instance of `google-gax`. Useful if you need to avoid loading the default gRPC version and want to use the fallback HTTP implementation. Load only fallback version and pass it to the constructor: ``` const gax = require('google-gax/build/src/fallback'); // avoids loading google-gax with gRPC const client = new AssetServiceClient({fallback: true}, gax); ```  
  
## Properties 

### apiEndpoint
    
    
    get apiEndpoint(): string;

The DNS address for this API service.

### apiEndpoint
    
    
    static get apiEndpoint(): string;

The DNS address for this API service - same as servicePath.

### assetServiceStub
    
    
    assetServiceStub?: Promise<{
            [name: string]: Function;
        }>;

### auth
    
    
    auth: gax.GoogleAuth;

### descriptors
    
    
    descriptors: Descriptors;

### innerApiCalls
    
    
    innerApiCalls: {
            [name: string]: Function;
        };

### pathTemplates
    
    
    pathTemplates: {
            [name: string]: gax.PathTemplate;
        };

### port
    
    
    static get port(): number;

The port for this API service.

### scopes
    
    
    static get scopes(): string[];

The scopes needed to make gRPC calls for every method defined in this service.

### servicePath
    
    
    static get servicePath(): string;

The DNS address for this API service.

### universeDomain
    
    
    get universeDomain(): string;

### warn
    
    
    warn: (code: string, message: string, warnType?: string) => void;

## Methods 

### accessLevelPath(accessPolicy, accessLevel)
    
    
    accessLevelPath(accessPolicy: string, accessLevel: string): string;

Return a fully-qualified accessLevel resource name string.

**Parameters**  
---  
**Name** | **Description**  
`accessPolicy` |  `string`   
  
`accessLevel` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### accessPolicyPath(accessPolicy)
    
    
    accessPolicyPath(accessPolicy: string): string;

Return a fully-qualified accessPolicy resource name string.

**Parameter**  
---  
**Name** | **Description**  
`accessPolicy` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### close()
    
    
    close(): Promise<void>;

Terminate the gRPC channel and close the client.

The client will no longer be usable and all future behavior is undefined.

**Returns**  
---  
**Type** | **Description**  
`Promise<void>` | {Promise} A promise that resolves when the client is closed.  
  
### createFeed(request, options)
    
    
    createFeed(request?: protos.google.cloud.asset.v1p2beta1.ICreateFeedRequest, options?: CallOptions): Promise<[
            protos.google.cloud.asset.v1p2beta1.IFeed,
            protos.google.cloud.asset.v1p2beta1.ICreateFeedRequest | undefined,
            {} | undefined
        ]>;

Creates a feed in a parent project/folder/organization to listen to its asset updates.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateFeedRequest](https://docs.cloud.google.com/nodejs/docs/reference/asset/latest/asset/protos.google.cloud.asset.v1p2beta1.icreatefeedrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.asset.v1p2beta1.IFeed](https://docs.cloud.google.com/nodejs/docs/reference/asset/latest/asset/protos.google.cloud.asset.v1p2beta1.ifeed), [protos.google.cloud.asset.v1p2beta1.ICreateFeedRequest](https://docs.cloud.google.com/nodejs/docs/reference/asset/latest/asset/protos.google.cloud.asset.v1p2beta1.icreatefeedrequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [Feed](https://docs.cloud.google.com/nodejs/docs/reference/asset/latest/asset/protos.google.cloud.asset.v1p2beta1.feed). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The name of the project/folder/organization where this feed
       *  should be created in. It can only be an organization number (such as
       *  "organizations/123"), a folder number (such as "folders/123"), a project ID
       *  (such as "projects/my-project-id"), or a project number (such as
       *  "projects/12345").
       */
      // const parent = 'abc123'
      /**
       *  Required. This is the client-assigned asset feed identifier and it needs to
       *  be unique under a specific parent project/folder/organization.
       */
      // const feedId = 'abc123'
      /**
       *  Required. The feed details. The field `name` must be empty and it will be
       *  generated in the format of: projects/project_number/feeds/feed_id
       *  folders/folder_number/feeds/feed_id
       *  organizations/organization_number/feeds/feed_id
       */
      // const feed = {}
    
      // Imports the Asset library
      const {AssetServiceClient} = require('[@google-cloud/asset](https://docs.cloud.google.com/nodejs/docs/reference/asset/latest/overview.html)').v1p2beta1;
    
      // Instantiates a client
      const assetClient = new [AssetServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/asset/latest/overview.html)();
    
      async function callCreateFeed() {
        // Construct request
        const request = {
          parent,
          feedId,
          feed,
        };
    
        // Run request
        const response = await assetClient.createFeed(request);
        console.log(response);
      }
    
      callCreateFeed();
    
    

### createFeed(request, options, callback)
    
    
    createFeed(request: protos.google.cloud.asset.v1p2beta1.ICreateFeedRequest, options: CallOptions, callback: Callback<protos.google.cloud.asset.v1p2beta1.IFeed, protos.google.cloud.asset.v1p2beta1.ICreateFeedRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateFeedRequest](https://docs.cloud.google.com/nodejs/docs/reference/asset/latest/asset/protos.google.cloud.asset.v1p2beta1.icreatefeedrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.asset.v1p2beta1.IFeed](https://docs.cloud.google.com/nodejs/docs/reference/asset/latest/asset/protos.google.cloud.asset.v1p2beta1.ifeed), [protos.google.cloud.asset.v1p2beta1.ICreateFeedRequest](https://docs.cloud.google.com/nodejs/docs/reference/asset/latest/asset/protos.google.cloud.asset.v1p2beta1.icreatefeedrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createFeed(request, callback)
    
    
    createFeed(request: protos.google.cloud.asset.v1p2beta1.ICreateFeedRequest, callback: Callback<protos.google.cloud.asset.v1p2beta1.IFeed, protos.google.cloud.asset.v1p2beta1.ICreateFeedRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateFeedRequest](https://docs.cloud.google.com/nodejs/docs/reference/asset/latest/asset/protos.google.cloud.asset.v1p2beta1.icreatefeedrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.asset.v1p2beta1.IFeed](https://docs.cloud.google.com/nodejs/docs/reference/asset/latest/asset/protos.google.cloud.asset.v1p2beta1.ifeed), [protos.google.cloud.asset.v1p2beta1.ICreateFeedRequest](https://docs.cloud.google.com/nodejs/docs/reference/asset/latest/asset/protos.google.cloud.asset.v1p2beta1.icreatefeedrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteFeed(request, options)
    
    
    deleteFeed(request?: protos.google.cloud.asset.v1p2beta1.IDeleteFeedRequest, options?: CallOptions): Promise<[
            protos.google.protobuf.IEmpty,
            protos.google.cloud.asset.v1p2beta1.IDeleteFeedRequest | undefined,
            {} | undefined
        ]>;

Deletes an asset feed.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteFeedRequest](https://docs.cloud.google.com/nodejs/docs/reference/asset/latest/asset/protos.google.cloud.asset.v1p2beta1.ideletefeedrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/asset/latest/asset/protos.google.protobuf.iempty), [protos.google.cloud.asset.v1p2beta1.IDeleteFeedRequest](https://docs.cloud.google.com/nodejs/docs/reference/asset/latest/asset/protos.google.cloud.asset.v1p2beta1.ideletefeedrequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [Empty](https://docs.cloud.google.com/nodejs/docs/reference/asset/latest/asset/protos.google.protobuf.empty). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The name of the feed and it must be in the format of:
       *  projects/project_number/feeds/feed_id
       *  folders/folder_number/feeds/feed_id
       *  organizations/organization_number/feeds/feed_id
       */
      // const name = 'abc123'
    
      // Imports the Asset library
      const {AssetServiceClient} = require('[@google-cloud/asset](https://docs.cloud.google.com/nodejs/docs/reference/asset/latest/overview.html)').v1p2beta1;
    
      // Instantiates a client
      const assetClient = new [AssetServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/asset/latest/overview.html)();
    
      async function callDeleteFeed() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await assetClient.deleteFeed(request);
        console.log(response);
      }
    
      callDeleteFeed();
    
    

### deleteFeed(request, options, callback)
    
    
    deleteFeed(request: protos.google.cloud.asset.v1p2beta1.IDeleteFeedRequest, options: CallOptions, callback: Callback<protos.google.protobuf.IEmpty, protos.google.cloud.asset.v1p2beta1.IDeleteFeedRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteFeedRequest](https://docs.cloud.google.com/nodejs/docs/reference/asset/latest/asset/protos.google.cloud.asset.v1p2beta1.ideletefeedrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/asset/latest/asset/protos.google.protobuf.iempty), [protos.google.cloud.asset.v1p2beta1.IDeleteFeedRequest](https://docs.cloud.google.com/nodejs/docs/reference/asset/latest/asset/protos.google.cloud.asset.v1p2beta1.ideletefeedrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteFeed(request, callback)
    
    
    deleteFeed(request: protos.google.cloud.asset.v1p2beta1.IDeleteFeedRequest, callback: Callback<protos.google.protobuf.IEmpty, protos.google.cloud.asset.v1p2beta1.IDeleteFeedRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteFeedRequest](https://docs.cloud.google.com/nodejs/docs/reference/asset/latest/asset/protos.google.cloud.asset.v1p2beta1.ideletefeedrequest)`   
  
`callback` |  `Callback<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/asset/latest/asset/protos.google.protobuf.iempty), [protos.google.cloud.asset.v1p2beta1.IDeleteFeedRequest](https://docs.cloud.google.com/nodejs/docs/reference/asset/latest/asset/protos.google.cloud.asset.v1p2beta1.ideletefeedrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### folderFeedPath(folder, feed)
    
    
    folderFeedPath(folder: string, feed: string): string;

Return a fully-qualified folderFeed resource name string.

**Parameters**  
---  
**Name** | **Description**  
`folder` |  `string`   
  
`feed` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### getFeed(request, options)
    
    
    getFeed(request?: protos.google.cloud.asset.v1p2beta1.IGetFeedRequest, options?: CallOptions): Promise<[
            protos.google.cloud.asset.v1p2beta1.IFeed,
            protos.google.cloud.asset.v1p2beta1.IGetFeedRequest | undefined,
            {} | undefined
        ]>;

Gets details about an asset feed.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetFeedRequest](https://docs.cloud.google.com/nodejs/docs/reference/asset/latest/asset/protos.google.cloud.asset.v1p2beta1.igetfeedrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.asset.v1p2beta1.IFeed](https://docs.cloud.google.com/nodejs/docs/reference/asset/latest/asset/protos.google.cloud.asset.v1p2beta1.ifeed), [protos.google.cloud.asset.v1p2beta1.IGetFeedRequest](https://docs.cloud.google.com/nodejs/docs/reference/asset/latest/asset/protos.google.cloud.asset.v1p2beta1.igetfeedrequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [Feed](https://docs.cloud.google.com/nodejs/docs/reference/asset/latest/asset/protos.google.cloud.asset.v1p2beta1.feed). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The name of the Feed and it must be in the format of:
       *  projects/project_number/feeds/feed_id
       *  folders/folder_number/feeds/feed_id
       *  organizations/organization_number/feeds/feed_id
       */
      // const name = 'abc123'
    
      // Imports the Asset library
      const {AssetServiceClient} = require('[@google-cloud/asset](https://docs.cloud.google.com/nodejs/docs/reference/asset/latest/overview.html)').v1p2beta1;
    
      // Instantiates a client
      const assetClient = new [AssetServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/asset/latest/overview.html)();
    
      async function callGetFeed() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await assetClient.getFeed(request);
        console.log(response);
      }
    
      callGetFeed();
    
    

### getFeed(request, options, callback)
    
    
    getFeed(request: protos.google.cloud.asset.v1p2beta1.IGetFeedRequest, options: CallOptions, callback: Callback<protos.google.cloud.asset.v1p2beta1.IFeed, protos.google.cloud.asset.v1p2beta1.IGetFeedRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetFeedRequest](https://docs.cloud.google.com/nodejs/docs/reference/asset/latest/asset/protos.google.cloud.asset.v1p2beta1.igetfeedrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.asset.v1p2beta1.IFeed](https://docs.cloud.google.com/nodejs/docs/reference/asset/latest/asset/protos.google.cloud.asset.v1p2beta1.ifeed), [protos.google.cloud.asset.v1p2beta1.IGetFeedRequest](https://docs.cloud.google.com/nodejs/docs/reference/asset/latest/asset/protos.google.cloud.asset.v1p2beta1.igetfeedrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getFeed(request, callback)
    
    
    getFeed(request: protos.google.cloud.asset.v1p2beta1.IGetFeedRequest, callback: Callback<protos.google.cloud.asset.v1p2beta1.IFeed, protos.google.cloud.asset.v1p2beta1.IGetFeedRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetFeedRequest](https://docs.cloud.google.com/nodejs/docs/reference/asset/latest/asset/protos.google.cloud.asset.v1p2beta1.igetfeedrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.asset.v1p2beta1.IFeed](https://docs.cloud.google.com/nodejs/docs/reference/asset/latest/asset/protos.google.cloud.asset.v1p2beta1.ifeed), [protos.google.cloud.asset.v1p2beta1.IGetFeedRequest](https://docs.cloud.google.com/nodejs/docs/reference/asset/latest/asset/protos.google.cloud.asset.v1p2beta1.igetfeedrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getProjectId()
    
    
    getProjectId(): Promise<string>;

**Returns**  
---  
**Type** | **Description**  
`Promise<string>` |   
  
### getProjectId(callback)
    
    
    getProjectId(callback: Callback<string, undefined, undefined>): void;

**Parameter**  
---  
**Name** | **Description**  
`callback` |  `Callback<string, undefined, undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### initialize()
    
    
    initialize(): Promise<{
            [name: string]: Function;
        }>;

Initialize the client. Performs asynchronous operations (such as authentication) and prepares the client. This function will be called automatically when any class method is called for the first time, but if you need to initialize it before calling an actual method, feel free to call initialize() directly.

You can await on this method if you want to make sure the client is initialized.

**Returns**  
---  
**Type** | **Description**  
`Promise<{ [name: string]: Function; }>` | {Promise} A promise that resolves to an authenticated service stub.  
  
### listFeeds(request, options)
    
    
    listFeeds(request?: protos.google.cloud.asset.v1p2beta1.IListFeedsRequest, options?: CallOptions): Promise<[
            protos.google.cloud.asset.v1p2beta1.IListFeedsResponse,
            protos.google.cloud.asset.v1p2beta1.IListFeedsRequest | undefined,
            {} | undefined
        ]>;

Lists all asset feeds in a parent project/folder/organization.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListFeedsRequest](https://docs.cloud.google.com/nodejs/docs/reference/asset/latest/asset/protos.google.cloud.asset.v1p2beta1.ilistfeedsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.asset.v1p2beta1.IListFeedsResponse](https://docs.cloud.google.com/nodejs/docs/reference/asset/latest/asset/protos.google.cloud.asset.v1p2beta1.ilistfeedsresponse), [protos.google.cloud.asset.v1p2beta1.IListFeedsRequest](https://docs.cloud.google.com/nodejs/docs/reference/asset/latest/asset/protos.google.cloud.asset.v1p2beta1.ilistfeedsrequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [ListFeedsResponse](https://docs.cloud.google.com/nodejs/docs/reference/asset/latest/asset/protos.google.cloud.asset.v1p2beta1.listfeedsresponse). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The parent project/folder/organization whose feeds are to be
       *  listed. It can only be using project/folder/organization number (such as
       *  "folders/12345")", or a project ID (such as "projects/my-project-id").
       */
      // const parent = 'abc123'
    
      // Imports the Asset library
      const {AssetServiceClient} = require('[@google-cloud/asset](https://docs.cloud.google.com/nodejs/docs/reference/asset/latest/overview.html)').v1p2beta1;
    
      // Instantiates a client
      const assetClient = new [AssetServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/asset/latest/overview.html)();
    
      async function callListFeeds() {
        // Construct request
        const request = {
          parent,
        };
    
        // Run request
        const response = await assetClient.listFeeds(request);
        console.log(response);
      }
    
      callListFeeds();
    
    

### listFeeds(request, options, callback)
    
    
    listFeeds(request: protos.google.cloud.asset.v1p2beta1.IListFeedsRequest, options: CallOptions, callback: Callback<protos.google.cloud.asset.v1p2beta1.IListFeedsResponse, protos.google.cloud.asset.v1p2beta1.IListFeedsRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListFeedsRequest](https://docs.cloud.google.com/nodejs/docs/reference/asset/latest/asset/protos.google.cloud.asset.v1p2beta1.ilistfeedsrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.asset.v1p2beta1.IListFeedsResponse](https://docs.cloud.google.com/nodejs/docs/reference/asset/latest/asset/protos.google.cloud.asset.v1p2beta1.ilistfeedsresponse), [protos.google.cloud.asset.v1p2beta1.IListFeedsRequest](https://docs.cloud.google.com/nodejs/docs/reference/asset/latest/asset/protos.google.cloud.asset.v1p2beta1.ilistfeedsrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listFeeds(request, callback)
    
    
    listFeeds(request: protos.google.cloud.asset.v1p2beta1.IListFeedsRequest, callback: Callback<protos.google.cloud.asset.v1p2beta1.IListFeedsResponse, protos.google.cloud.asset.v1p2beta1.IListFeedsRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListFeedsRequest](https://docs.cloud.google.com/nodejs/docs/reference/asset/latest/asset/protos.google.cloud.asset.v1p2beta1.ilistfeedsrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.asset.v1p2beta1.IListFeedsResponse](https://docs.cloud.google.com/nodejs/docs/reference/asset/latest/asset/protos.google.cloud.asset.v1p2beta1.ilistfeedsresponse), [protos.google.cloud.asset.v1p2beta1.IListFeedsRequest](https://docs.cloud.google.com/nodejs/docs/reference/asset/latest/asset/protos.google.cloud.asset.v1p2beta1.ilistfeedsrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### matchAccessLevelFromAccessLevelName(accessLevelName)
    
    
    matchAccessLevelFromAccessLevelName(accessLevelName: string): string | number;

Parse the access_level from AccessLevel resource.

**Parameter**  
---  
**Name** | **Description**  
`accessLevelName` |  `string`   
A fully-qualified path representing AccessLevel resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the access_level.  
  
### matchAccessPolicyFromAccessLevelName(accessLevelName)
    
    
    matchAccessPolicyFromAccessLevelName(accessLevelName: string): string | number;

Parse the access_policy from AccessLevel resource.

**Parameter**  
---  
**Name** | **Description**  
`accessLevelName` |  `string`   
A fully-qualified path representing AccessLevel resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the access_policy.  
  
### matchAccessPolicyFromAccessPolicyName(accessPolicyName)
    
    
    matchAccessPolicyFromAccessPolicyName(accessPolicyName: string): string | number;

Parse the access_policy from AccessPolicy resource.

**Parameter**  
---  
**Name** | **Description**  
`accessPolicyName` |  `string`   
A fully-qualified path representing AccessPolicy resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the access_policy.  
  
### matchAccessPolicyFromServicePerimeterName(servicePerimeterName)
    
    
    matchAccessPolicyFromServicePerimeterName(servicePerimeterName: string): string | number;

Parse the access_policy from ServicePerimeter resource.

**Parameter**  
---  
**Name** | **Description**  
`servicePerimeterName` |  `string`   
A fully-qualified path representing ServicePerimeter resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the access_policy.  
  
### matchFeedFromFolderFeedName(folderFeedName)
    
    
    matchFeedFromFolderFeedName(folderFeedName: string): string | number;

Parse the feed from FolderFeed resource.

**Parameter**  
---  
**Name** | **Description**  
`folderFeedName` |  `string`   
A fully-qualified path representing folder_feed resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the feed.  
  
### matchFeedFromOrganizationFeedName(organizationFeedName)
    
    
    matchFeedFromOrganizationFeedName(organizationFeedName: string): string | number;

Parse the feed from OrganizationFeed resource.

**Parameter**  
---  
**Name** | **Description**  
`organizationFeedName` |  `string`   
A fully-qualified path representing organization_feed resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the feed.  
  
### matchFeedFromProjectFeedName(projectFeedName)
    
    
    matchFeedFromProjectFeedName(projectFeedName: string): string | number;

Parse the feed from ProjectFeed resource.

**Parameter**  
---  
**Name** | **Description**  
`projectFeedName` |  `string`   
A fully-qualified path representing project_feed resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the feed.  
  
### matchFolderFromFolderFeedName(folderFeedName)
    
    
    matchFolderFromFolderFeedName(folderFeedName: string): string | number;

Parse the folder from FolderFeed resource.

**Parameter**  
---  
**Name** | **Description**  
`folderFeedName` |  `string`   
A fully-qualified path representing folder_feed resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the folder.  
  
### matchOrganizationFromOrganizationFeedName(organizationFeedName)
    
    
    matchOrganizationFromOrganizationFeedName(organizationFeedName: string): string | number;

Parse the organization from OrganizationFeed resource.

**Parameter**  
---  
**Name** | **Description**  
`organizationFeedName` |  `string`   
A fully-qualified path representing organization_feed resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the organization.  
  
### matchProjectFromProjectFeedName(projectFeedName)
    
    
    matchProjectFromProjectFeedName(projectFeedName: string): string | number;

Parse the project from ProjectFeed resource.

**Parameter**  
---  
**Name** | **Description**  
`projectFeedName` |  `string`   
A fully-qualified path representing project_feed resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchServicePerimeterFromServicePerimeterName(servicePerimeterName)
    
    
    matchServicePerimeterFromServicePerimeterName(servicePerimeterName: string): string | number;

Parse the service_perimeter from ServicePerimeter resource.

**Parameter**  
---  
**Name** | **Description**  
`servicePerimeterName` |  `string`   
A fully-qualified path representing ServicePerimeter resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the service_perimeter.  
  
### organizationFeedPath(organization, feed)
    
    
    organizationFeedPath(organization: string, feed: string): string;

Return a fully-qualified organizationFeed resource name string.

**Parameters**  
---  
**Name** | **Description**  
`organization` |  `string`   
  
`feed` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### projectFeedPath(project, feed)
    
    
    projectFeedPath(project: string, feed: string): string;

Return a fully-qualified projectFeed resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`feed` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### servicePerimeterPath(accessPolicy, servicePerimeter)
    
    
    servicePerimeterPath(accessPolicy: string, servicePerimeter: string): string;

Return a fully-qualified servicePerimeter resource name string.

**Parameters**  
---  
**Name** | **Description**  
`accessPolicy` |  `string`   
  
`servicePerimeter` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### updateFeed(request, options)
    
    
    updateFeed(request?: protos.google.cloud.asset.v1p2beta1.IUpdateFeedRequest, options?: CallOptions): Promise<[
            protos.google.cloud.asset.v1p2beta1.IFeed,
            protos.google.cloud.asset.v1p2beta1.IUpdateFeedRequest | undefined,
            {} | undefined
        ]>;

Updates an asset feed configuration.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateFeedRequest](https://docs.cloud.google.com/nodejs/docs/reference/asset/latest/asset/protos.google.cloud.asset.v1p2beta1.iupdatefeedrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.asset.v1p2beta1.IFeed](https://docs.cloud.google.com/nodejs/docs/reference/asset/latest/asset/protos.google.cloud.asset.v1p2beta1.ifeed), [protos.google.cloud.asset.v1p2beta1.IUpdateFeedRequest](https://docs.cloud.google.com/nodejs/docs/reference/asset/latest/asset/protos.google.cloud.asset.v1p2beta1.iupdatefeedrequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [Feed](https://docs.cloud.google.com/nodejs/docs/reference/asset/latest/asset/protos.google.cloud.asset.v1p2beta1.feed). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The new values of feed details. It must match an existing feed
       *  and the field `name` must be in the format of:
       *  projects/project_number/feeds/feed_id or
       *  folders/folder_number/feeds/feed_id or
       *  organizations/organization_number/feeds/feed_id.
       */
      // const feed = {}
      /**
       *  Required. Only updates the `feed` fields indicated by this mask.
       *  The field mask must not be empty, and it must not contain fields that
       *  are immutable or only set by the server.
       */
      // const updateMask = {}
    
      // Imports the Asset library
      const {AssetServiceClient} = require('[@google-cloud/asset](https://docs.cloud.google.com/nodejs/docs/reference/asset/latest/overview.html)').v1p2beta1;
    
      // Instantiates a client
      const assetClient = new [AssetServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/asset/latest/overview.html)();
    
      async function callUpdateFeed() {
        // Construct request
        const request = {
          feed,
          updateMask,
        };
    
        // Run request
        const response = await assetClient.updateFeed(request);
        console.log(response);
      }
    
      callUpdateFeed();
    
    

### updateFeed(request, options, callback)
    
    
    updateFeed(request: protos.google.cloud.asset.v1p2beta1.IUpdateFeedRequest, options: CallOptions, callback: Callback<protos.google.cloud.asset.v1p2beta1.IFeed, protos.google.cloud.asset.v1p2beta1.IUpdateFeedRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateFeedRequest](https://docs.cloud.google.com/nodejs/docs/reference/asset/latest/asset/protos.google.cloud.asset.v1p2beta1.iupdatefeedrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.asset.v1p2beta1.IFeed](https://docs.cloud.google.com/nodejs/docs/reference/asset/latest/asset/protos.google.cloud.asset.v1p2beta1.ifeed), [protos.google.cloud.asset.v1p2beta1.IUpdateFeedRequest](https://docs.cloud.google.com/nodejs/docs/reference/asset/latest/asset/protos.google.cloud.asset.v1p2beta1.iupdatefeedrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateFeed(request, callback)
    
    
    updateFeed(request: protos.google.cloud.asset.v1p2beta1.IUpdateFeedRequest, callback: Callback<protos.google.cloud.asset.v1p2beta1.IFeed, protos.google.cloud.asset.v1p2beta1.IUpdateFeedRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateFeedRequest](https://docs.cloud.google.com/nodejs/docs/reference/asset/latest/asset/protos.google.cloud.asset.v1p2beta1.iupdatefeedrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.asset.v1p2beta1.IFeed](https://docs.cloud.google.com/nodejs/docs/reference/asset/latest/asset/protos.google.cloud.asset.v1p2beta1.ifeed), [protos.google.cloud.asset.v1p2beta1.IUpdateFeedRequest](https://docs.cloud.google.com/nodejs/docs/reference/asset/latest/asset/protos.google.cloud.asset.v1p2beta1.iupdatefeedrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
