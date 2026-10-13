---
url: https://docs.cloud.google.com/nodejs/docs/reference/reviews/latest/reviews/v1beta.merchantreviewsserviceclient
title: Class v1beta.MerchantReviewsServiceClient (0.7.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:08:11.910702+00:00
---

# Class v1beta.MerchantReviewsServiceClient (0.7.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/reviews/latest/reviews/v1beta.merchantreviewsserviceclient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class v1beta.MerchantReviewsServiceClient (0.7.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.7.1 (latest)  0.6.0  0.3.0  0.2.1  0.1.0 

Service to manage merchant reviews. v1beta

## Package

[@google-shopping/reviews](https://docs.cloud.google.com/nodejs/docs/reference/reviews/latest/overview.html)

## Constructors 

### (constructor)(opts, gaxInstance)
    
    
    constructor(opts?: ClientOptions, gaxInstance?: typeof gax | typeof gax.fallback);

Construct an instance of MerchantReviewsServiceClient.

**Parameters**  
---  
**Name** | **Description**  
`opts` |  `ClientOptions`   
  
`gaxInstance` |  `typeof gax | typeof fallback`   
: loaded instance of `google-gax`. Useful if you need to avoid loading the default gRPC version and want to use the fallback HTTP implementation. Load only fallback version and pass it to the constructor: ``` const gax = require('google-gax/build/src/fallback'); // avoids loading google-gax with gRPC const client = new MerchantReviewsServiceClient({fallback: true}, gax); ```  
  
## Properties 

### apiEndpoint
    
    
    get apiEndpoint(): string;

The DNS address for this API service.

### apiEndpoint
    
    
    static get apiEndpoint(): string;

The DNS address for this API service - same as servicePath.

### auth
    
    
    auth: gax.GoogleAuth;

### descriptors
    
    
    descriptors: Descriptors;

### innerApiCalls
    
    
    innerApiCalls: {
            [name: string]: Function;
        };

### merchantReviewsServiceStub
    
    
    merchantReviewsServiceStub?: Promise<{
            [name: string]: Function;
        }>;

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

### accountPath(account)
    
    
    accountPath(account: string): string;

Return a fully-qualified account resource name string.

**Parameter**  
---  
**Name** | **Description**  
`account` |  `string`   
  
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
  
### deleteMerchantReview(request, options)
    
    
    deleteMerchantReview(request?: protos.google.shopping.merchant.reviews.v1beta.IDeleteMerchantReviewRequest, options?: CallOptions): Promise<[
            protos.google.protobuf.IEmpty,
            (protos.google.shopping.merchant.reviews.v1beta.IDeleteMerchantReviewRequest | undefined),
            {} | undefined
        ]>;

Deletes merchant review.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteMerchantReviewRequest](https://docs.cloud.google.com/nodejs/docs/reference/reviews/latest/reviews/protos.google.shopping.merchant.reviews.v1beta.ideletemerchantreviewrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/reviews/latest/reviews/protos.google.protobuf.iempty), ([protos.google.shopping.merchant.reviews.v1beta.IDeleteMerchantReviewRequest](https://docs.cloud.google.com/nodejs/docs/reference/reviews/latest/reviews/protos.google.shopping.merchant.reviews.v1beta.ideletemerchantreviewrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [Empty](https://docs.cloud.google.com/nodejs/docs/reference/reviews/latest/reviews/protos.google.protobuf.empty). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The ID of the merchant review.
       *  Format: accounts/{account}/merchantReviews/{merchantReview}
       */
      // const name = 'abc123'
    
      // Imports the Reviews library
      const {MerchantReviewsServiceClient} = require('[@google-shopping/reviews](https://docs.cloud.google.com/nodejs/docs/reference/reviews/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const reviewsClient = new [MerchantReviewsServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/reviews/latest/overview.html)();
    
      async function callDeleteMerchantReview() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await reviewsClient.deleteMerchantReview(request);
        console.log(response);
      }
    
      callDeleteMerchantReview();
    
    

### deleteMerchantReview(request, options, callback)
    
    
    deleteMerchantReview(request: protos.google.shopping.merchant.reviews.v1beta.IDeleteMerchantReviewRequest, options: CallOptions, callback: Callback<protos.google.protobuf.IEmpty, protos.google.shopping.merchant.reviews.v1beta.IDeleteMerchantReviewRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteMerchantReviewRequest](https://docs.cloud.google.com/nodejs/docs/reference/reviews/latest/reviews/protos.google.shopping.merchant.reviews.v1beta.ideletemerchantreviewrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/reviews/latest/reviews/protos.google.protobuf.iempty), [protos.google.shopping.merchant.reviews.v1beta.IDeleteMerchantReviewRequest](https://docs.cloud.google.com/nodejs/docs/reference/reviews/latest/reviews/protos.google.shopping.merchant.reviews.v1beta.ideletemerchantreviewrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteMerchantReview(request, callback)
    
    
    deleteMerchantReview(request: protos.google.shopping.merchant.reviews.v1beta.IDeleteMerchantReviewRequest, callback: Callback<protos.google.protobuf.IEmpty, protos.google.shopping.merchant.reviews.v1beta.IDeleteMerchantReviewRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteMerchantReviewRequest](https://docs.cloud.google.com/nodejs/docs/reference/reviews/latest/reviews/protos.google.shopping.merchant.reviews.v1beta.ideletemerchantreviewrequest)`   
  
`callback` |  `Callback<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/reviews/latest/reviews/protos.google.protobuf.iempty), [protos.google.shopping.merchant.reviews.v1beta.IDeleteMerchantReviewRequest](https://docs.cloud.google.com/nodejs/docs/reference/reviews/latest/reviews/protos.google.shopping.merchant.reviews.v1beta.ideletemerchantreviewrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getMerchantReview(request, options)
    
    
    getMerchantReview(request?: protos.google.shopping.merchant.reviews.v1beta.IGetMerchantReviewRequest, options?: CallOptions): Promise<[
            protos.google.shopping.merchant.reviews.v1beta.IMerchantReview,
            (protos.google.shopping.merchant.reviews.v1beta.IGetMerchantReviewRequest | undefined),
            {} | undefined
        ]>;

Gets a merchant review.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetMerchantReviewRequest](https://docs.cloud.google.com/nodejs/docs/reference/reviews/latest/reviews/protos.google.shopping.merchant.reviews.v1beta.igetmerchantreviewrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.shopping.merchant.reviews.v1beta.IMerchantReview](https://docs.cloud.google.com/nodejs/docs/reference/reviews/latest/reviews/protos.google.shopping.merchant.reviews.v1beta.imerchantreview), ([protos.google.shopping.merchant.reviews.v1beta.IGetMerchantReviewRequest](https://docs.cloud.google.com/nodejs/docs/reference/reviews/latest/reviews/protos.google.shopping.merchant.reviews.v1beta.igetmerchantreviewrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [MerchantReview](https://docs.cloud.google.com/nodejs/docs/reference/reviews/latest/reviews/protos.google.shopping.merchant.reviews.v1beta.merchantreview). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The ID of the merchant review.
       *  Format: accounts/{account}/merchantReviews/{merchantReview}
       */
      // const name = 'abc123'
    
      // Imports the Reviews library
      const {MerchantReviewsServiceClient} = require('[@google-shopping/reviews](https://docs.cloud.google.com/nodejs/docs/reference/reviews/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const reviewsClient = new [MerchantReviewsServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/reviews/latest/overview.html)();
    
      async function callGetMerchantReview() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await reviewsClient.getMerchantReview(request);
        console.log(response);
      }
    
      callGetMerchantReview();
    
    

### getMerchantReview(request, options, callback)
    
    
    getMerchantReview(request: protos.google.shopping.merchant.reviews.v1beta.IGetMerchantReviewRequest, options: CallOptions, callback: Callback<protos.google.shopping.merchant.reviews.v1beta.IMerchantReview, protos.google.shopping.merchant.reviews.v1beta.IGetMerchantReviewRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetMerchantReviewRequest](https://docs.cloud.google.com/nodejs/docs/reference/reviews/latest/reviews/protos.google.shopping.merchant.reviews.v1beta.igetmerchantreviewrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.shopping.merchant.reviews.v1beta.IMerchantReview](https://docs.cloud.google.com/nodejs/docs/reference/reviews/latest/reviews/protos.google.shopping.merchant.reviews.v1beta.imerchantreview), [protos.google.shopping.merchant.reviews.v1beta.IGetMerchantReviewRequest](https://docs.cloud.google.com/nodejs/docs/reference/reviews/latest/reviews/protos.google.shopping.merchant.reviews.v1beta.igetmerchantreviewrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getMerchantReview(request, callback)
    
    
    getMerchantReview(request: protos.google.shopping.merchant.reviews.v1beta.IGetMerchantReviewRequest, callback: Callback<protos.google.shopping.merchant.reviews.v1beta.IMerchantReview, protos.google.shopping.merchant.reviews.v1beta.IGetMerchantReviewRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetMerchantReviewRequest](https://docs.cloud.google.com/nodejs/docs/reference/reviews/latest/reviews/protos.google.shopping.merchant.reviews.v1beta.igetmerchantreviewrequest)`   
  
`callback` |  `Callback<[protos.google.shopping.merchant.reviews.v1beta.IMerchantReview](https://docs.cloud.google.com/nodejs/docs/reference/reviews/latest/reviews/protos.google.shopping.merchant.reviews.v1beta.imerchantreview), [protos.google.shopping.merchant.reviews.v1beta.IGetMerchantReviewRequest](https://docs.cloud.google.com/nodejs/docs/reference/reviews/latest/reviews/protos.google.shopping.merchant.reviews.v1beta.igetmerchantreviewrequest) | null | undefined, {} | null | undefined>`   
  
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
  
### insertMerchantReview(request, options)
    
    
    insertMerchantReview(request?: protos.google.shopping.merchant.reviews.v1beta.IInsertMerchantReviewRequest, options?: CallOptions): Promise<[
            protos.google.shopping.merchant.reviews.v1beta.IMerchantReview,
            (protos.google.shopping.merchant.reviews.v1beta.IInsertMerchantReviewRequest | undefined),
            {} | undefined
        ]>;

Inserts a review for your Merchant Center account. If the review already exists, then the review is replaced with the new instance.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IInsertMerchantReviewRequest](https://docs.cloud.google.com/nodejs/docs/reference/reviews/latest/reviews/protos.google.shopping.merchant.reviews.v1beta.iinsertmerchantreviewrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.shopping.merchant.reviews.v1beta.IMerchantReview](https://docs.cloud.google.com/nodejs/docs/reference/reviews/latest/reviews/protos.google.shopping.merchant.reviews.v1beta.imerchantreview), ([protos.google.shopping.merchant.reviews.v1beta.IInsertMerchantReviewRequest](https://docs.cloud.google.com/nodejs/docs/reference/reviews/latest/reviews/protos.google.shopping.merchant.reviews.v1beta.iinsertmerchantreviewrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [MerchantReview](https://docs.cloud.google.com/nodejs/docs/reference/reviews/latest/reviews/protos.google.shopping.merchant.reviews.v1beta.merchantreview). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The account where the merchant review will be inserted.
       *  Format: accounts/{account}
       */
      // const parent = 'abc123'
      /**
       *  Required. The merchant review to insert.
       */
      // const merchantReview = {}
      /**
       *  Required. The data source of the
       *  merchantreview (https://support.google.com/merchants/answer/7045996?sjid=5253581244217581976-EU)
       *  Format:
       *  `accounts/{account}/dataSources/{datasource}`.
       */
      // const dataSource = 'abc123'
    
      // Imports the Reviews library
      const {MerchantReviewsServiceClient} = require('[@google-shopping/reviews](https://docs.cloud.google.com/nodejs/docs/reference/reviews/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const reviewsClient = new [MerchantReviewsServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/reviews/latest/overview.html)();
    
      async function callInsertMerchantReview() {
        // Construct request
        const request = {
          parent,
          merchantReview,
          dataSource,
        };
    
        // Run request
        const response = await reviewsClient.insertMerchantReview(request);
        console.log(response);
      }
    
      callInsertMerchantReview();
    
    

### insertMerchantReview(request, options, callback)
    
    
    insertMerchantReview(request: protos.google.shopping.merchant.reviews.v1beta.IInsertMerchantReviewRequest, options: CallOptions, callback: Callback<protos.google.shopping.merchant.reviews.v1beta.IMerchantReview, protos.google.shopping.merchant.reviews.v1beta.IInsertMerchantReviewRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IInsertMerchantReviewRequest](https://docs.cloud.google.com/nodejs/docs/reference/reviews/latest/reviews/protos.google.shopping.merchant.reviews.v1beta.iinsertmerchantreviewrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.shopping.merchant.reviews.v1beta.IMerchantReview](https://docs.cloud.google.com/nodejs/docs/reference/reviews/latest/reviews/protos.google.shopping.merchant.reviews.v1beta.imerchantreview), [protos.google.shopping.merchant.reviews.v1beta.IInsertMerchantReviewRequest](https://docs.cloud.google.com/nodejs/docs/reference/reviews/latest/reviews/protos.google.shopping.merchant.reviews.v1beta.iinsertmerchantreviewrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### insertMerchantReview(request, callback)
    
    
    insertMerchantReview(request: protos.google.shopping.merchant.reviews.v1beta.IInsertMerchantReviewRequest, callback: Callback<protos.google.shopping.merchant.reviews.v1beta.IMerchantReview, protos.google.shopping.merchant.reviews.v1beta.IInsertMerchantReviewRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IInsertMerchantReviewRequest](https://docs.cloud.google.com/nodejs/docs/reference/reviews/latest/reviews/protos.google.shopping.merchant.reviews.v1beta.iinsertmerchantreviewrequest)`   
  
`callback` |  `Callback<[protos.google.shopping.merchant.reviews.v1beta.IMerchantReview](https://docs.cloud.google.com/nodejs/docs/reference/reviews/latest/reviews/protos.google.shopping.merchant.reviews.v1beta.imerchantreview), [protos.google.shopping.merchant.reviews.v1beta.IInsertMerchantReviewRequest](https://docs.cloud.google.com/nodejs/docs/reference/reviews/latest/reviews/protos.google.shopping.merchant.reviews.v1beta.iinsertmerchantreviewrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listMerchantReviews(request, options)
    
    
    listMerchantReviews(request?: protos.google.shopping.merchant.reviews.v1beta.IListMerchantReviewsRequest, options?: CallOptions): Promise<[
            protos.google.shopping.merchant.reviews.v1beta.IMerchantReview[],
            protos.google.shopping.merchant.reviews.v1beta.IListMerchantReviewsRequest | null,
            protos.google.shopping.merchant.reviews.v1beta.IListMerchantReviewsResponse
        ]>;

Lists merchant reviews.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListMerchantReviewsRequest](https://docs.cloud.google.com/nodejs/docs/reference/reviews/latest/reviews/protos.google.shopping.merchant.reviews.v1beta.ilistmerchantreviewsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.shopping.merchant.reviews.v1beta.IMerchantReview](https://docs.cloud.google.com/nodejs/docs/reference/reviews/latest/reviews/protos.google.shopping.merchant.reviews.v1beta.imerchantreview)[], [protos.google.shopping.merchant.reviews.v1beta.IListMerchantReviewsRequest](https://docs.cloud.google.com/nodejs/docs/reference/reviews/latest/reviews/protos.google.shopping.merchant.reviews.v1beta.ilistmerchantreviewsrequest) | null, [protos.google.shopping.merchant.reviews.v1beta.IListMerchantReviewsResponse](https://docs.cloud.google.com/nodejs/docs/reference/reviews/latest/reviews/protos.google.shopping.merchant.reviews.v1beta.ilistmerchantreviewsresponse) ]>` | {Promise} - The promise which resolves to an array. The first element of the array is Array of [MerchantReview](https://docs.cloud.google.com/nodejs/docs/reference/reviews/latest/reviews/protos.google.shopping.merchant.reviews.v1beta.merchantreview). The client library will perform auto-pagination by default: it will call the API as many times as needed and will merge results from all the pages into this array. Note that it can affect your quota. We recommend using `listMerchantReviewsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listMerchantReviews(request, options, callback)
    
    
    listMerchantReviews(request: protos.google.shopping.merchant.reviews.v1beta.IListMerchantReviewsRequest, options: CallOptions, callback: PaginationCallback<protos.google.shopping.merchant.reviews.v1beta.IListMerchantReviewsRequest, protos.google.shopping.merchant.reviews.v1beta.IListMerchantReviewsResponse | null | undefined, protos.google.shopping.merchant.reviews.v1beta.IMerchantReview>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListMerchantReviewsRequest](https://docs.cloud.google.com/nodejs/docs/reference/reviews/latest/reviews/protos.google.shopping.merchant.reviews.v1beta.ilistmerchantreviewsrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `PaginationCallback<[protos.google.shopping.merchant.reviews.v1beta.IListMerchantReviewsRequest](https://docs.cloud.google.com/nodejs/docs/reference/reviews/latest/reviews/protos.google.shopping.merchant.reviews.v1beta.ilistmerchantreviewsrequest), [protos.google.shopping.merchant.reviews.v1beta.IListMerchantReviewsResponse](https://docs.cloud.google.com/nodejs/docs/reference/reviews/latest/reviews/protos.google.shopping.merchant.reviews.v1beta.ilistmerchantreviewsresponse) | null | undefined, [protos.google.shopping.merchant.reviews.v1beta.IMerchantReview](https://docs.cloud.google.com/nodejs/docs/reference/reviews/latest/reviews/protos.google.shopping.merchant.reviews.v1beta.imerchantreview)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listMerchantReviews(request, callback)
    
    
    listMerchantReviews(request: protos.google.shopping.merchant.reviews.v1beta.IListMerchantReviewsRequest, callback: PaginationCallback<protos.google.shopping.merchant.reviews.v1beta.IListMerchantReviewsRequest, protos.google.shopping.merchant.reviews.v1beta.IListMerchantReviewsResponse | null | undefined, protos.google.shopping.merchant.reviews.v1beta.IMerchantReview>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListMerchantReviewsRequest](https://docs.cloud.google.com/nodejs/docs/reference/reviews/latest/reviews/protos.google.shopping.merchant.reviews.v1beta.ilistmerchantreviewsrequest)`   
  
`callback` |  `PaginationCallback<[protos.google.shopping.merchant.reviews.v1beta.IListMerchantReviewsRequest](https://docs.cloud.google.com/nodejs/docs/reference/reviews/latest/reviews/protos.google.shopping.merchant.reviews.v1beta.ilistmerchantreviewsrequest), [protos.google.shopping.merchant.reviews.v1beta.IListMerchantReviewsResponse](https://docs.cloud.google.com/nodejs/docs/reference/reviews/latest/reviews/protos.google.shopping.merchant.reviews.v1beta.ilistmerchantreviewsresponse) | null | undefined, [protos.google.shopping.merchant.reviews.v1beta.IMerchantReview](https://docs.cloud.google.com/nodejs/docs/reference/reviews/latest/reviews/protos.google.shopping.merchant.reviews.v1beta.imerchantreview)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listMerchantReviewsAsync(request, options)
    
    
    listMerchantReviewsAsync(request?: protos.google.shopping.merchant.reviews.v1beta.IListMerchantReviewsRequest, options?: CallOptions): AsyncIterable<protos.google.shopping.merchant.reviews.v1beta.IMerchantReview>;

Equivalent to `listMerchantReviews`, but returns an iterable object.

`for`-`await`-`of` syntax is used with the iterable to get response elements on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListMerchantReviewsRequest](https://docs.cloud.google.com/nodejs/docs/reference/reviews/latest/reviews/protos.google.shopping.merchant.reviews.v1beta.ilistmerchantreviewsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.shopping.merchant.reviews.v1beta.IMerchantReview](https://docs.cloud.google.com/nodejs/docs/reference/reviews/latest/reviews/protos.google.shopping.merchant.reviews.v1beta.imerchantreview)>` | {Object} An iterable Object that allows [async iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols). When you iterate the returned iterable, each element will be an object representing [MerchantReview](https://docs.cloud.google.com/nodejs/docs/reference/reviews/latest/reviews/protos.google.shopping.merchant.reviews.v1beta.merchantreview). The API will be called under the hood as needed, once per the page, so you can stop the iteration when you don't need more results. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The account to list merchant reviews for.
       *  Format: accounts/{account}
       */
      // const parent = 'abc123'
      /**
       *  Optional. The maximum number of merchant reviews to return. The service can
       *  return fewer than this value. The maximum value is 1000; values above 1000
       *  are coerced to 1000. If unspecified, the maximum number of reviews is
       *  returned.
       */
      // const pageSize = 1234
      /**
       *  Optional. A page token, received from a previous `ListMerchantReviews`
       *  call. Provide this to retrieve the subsequent page.
       *  When paginating, all other parameters provided to `ListMerchantReviews`
       *  must match the call that provided the page token.
       */
      // const pageToken = 'abc123'
    
      // Imports the Reviews library
      const {MerchantReviewsServiceClient} = require('[@google-shopping/reviews](https://docs.cloud.google.com/nodejs/docs/reference/reviews/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const reviewsClient = new [MerchantReviewsServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/reviews/latest/overview.html)();
    
      async function callListMerchantReviews() {
        // Construct request
        const request = {
          parent,
        };
    
        // Run request
        const iterable = reviewsClient.[listMerchantReviewsAsync](https://docs.cloud.google.com/nodejs/docs/reference/reviews/latest/reviews/v1beta.merchantreviewsserviceclient.html)(request);
        for await (const response of iterable) {
            console.log(response);
        }
      }
    
      callListMerchantReviews();
    
    

### listMerchantReviewsStream(request, options)
    
    
    listMerchantReviewsStream(request?: protos.google.shopping.merchant.reviews.v1beta.IListMerchantReviewsRequest, options?: CallOptions): Transform;

Equivalent to `listMerchantReviews`, but returns a NodeJS Stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListMerchantReviewsRequest](https://docs.cloud.google.com/nodejs/docs/reference/reviews/latest/reviews/protos.google.shopping.merchant.reviews.v1beta.ilistmerchantreviewsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Transform` | {Stream} An object stream which emits an object representing [MerchantReview](https://docs.cloud.google.com/nodejs/docs/reference/reviews/latest/reviews/protos.google.shopping.merchant.reviews.v1beta.merchantreview) on 'data' event. The client library will perform auto-pagination by default: it will call the API as many times as needed. Note that it can affect your quota. We recommend using `listMerchantReviewsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### matchAccountFromAccountName(accountName)
    
    
    matchAccountFromAccountName(accountName: string): string | number;

Parse the account from Account resource.

**Parameter**  
---  
**Name** | **Description**  
`accountName` |  `string`   
A fully-qualified path representing Account resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the account.  
  
### matchAccountFromMerchantReviewName(merchantReviewName)
    
    
    matchAccountFromMerchantReviewName(merchantReviewName: string): string | number;

Parse the account from MerchantReview resource.

**Parameter**  
---  
**Name** | **Description**  
`merchantReviewName` |  `string`   
A fully-qualified path representing MerchantReview resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the account.  
  
### matchAccountFromProductReviewName(productReviewName)
    
    
    matchAccountFromProductReviewName(productReviewName: string): string | number;

Parse the account from ProductReview resource.

**Parameter**  
---  
**Name** | **Description**  
`productReviewName` |  `string`   
A fully-qualified path representing ProductReview resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the account.  
  
### matchNameFromMerchantReviewName(merchantReviewName)
    
    
    matchNameFromMerchantReviewName(merchantReviewName: string): string | number;

Parse the name from MerchantReview resource.

**Parameter**  
---  
**Name** | **Description**  
`merchantReviewName` |  `string`   
A fully-qualified path representing MerchantReview resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the name.  
  
### matchProductreviewFromProductReviewName(productReviewName)
    
    
    matchProductreviewFromProductReviewName(productReviewName: string): string | number;

Parse the productreview from ProductReview resource.

**Parameter**  
---  
**Name** | **Description**  
`productReviewName` |  `string`   
A fully-qualified path representing ProductReview resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the productreview.  
  
### merchantReviewPath(account, name)
    
    
    merchantReviewPath(account: string, name: string): string;

Return a fully-qualified merchantReview resource name string.

**Parameters**  
---  
**Name** | **Description**  
`account` |  `string`   
  
`name` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### productReviewPath(account, productreview)
    
    
    productReviewPath(account: string, productreview: string): string;

Return a fully-qualified productReview resource name string.

**Parameters**  
---  
**Name** | **Description**  
`account` |  `string`   
  
`productreview` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
