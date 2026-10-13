---
url: https://docs.cloud.google.com/nodejs/docs/reference/billing-budgets/latest/billing-budgets/v1beta1.budgetserviceclient
title: Class v1beta1.BudgetServiceClient (7.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:36:45.996191+00:00
---

# Class v1beta1.BudgetServiceClient (7.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/billing-budgets/latest/billing-budgets/v1beta1.budgetserviceclient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class v1beta1.BudgetServiceClient (7.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

7.1.1 (latest)  4.2.2  4.1.2  3.3.0  3.2.8 

BudgetService stores Cloud Billing budgets, which define a budget plan and rules to execute as we track spend against that plan. v1beta1

## Package

[@google-cloud/billing-budgets](https://docs.cloud.google.com/nodejs/docs/reference/billing-budgets/latest/overview.html)

## Constructors 

### (constructor)(opts, gaxInstance)
    
    
    constructor(opts?: ClientOptions, gaxInstance?: typeof gax | typeof gax.fallback);

Construct an instance of BudgetServiceClient.

**Parameters**  
---  
**Name** | **Description**  
`opts` |  `ClientOptions`   
  
`gaxInstance` |  `typeof gax | typeof fallback`   
: loaded instance of `google-gax`. Useful if you need to avoid loading the default gRPC version and want to use the fallback HTTP implementation. Load only fallback version and pass it to the constructor: ``` const gax = require('google-gax/build/src/fallback'); // avoids loading google-gax with gRPC const client = new BudgetServiceClient({fallback: true}, gax); ```  
  
## Properties 

### apiEndpoint
    
    
    get apiEndpoint(): string;

The DNS address for this API service.

### apiEndpoint
    
    
    static get apiEndpoint(): string;

The DNS address for this API service - same as servicePath.

### auth
    
    
    auth: gax.GoogleAuth;

### budgetServiceStub
    
    
    budgetServiceStub?: Promise<{
            [name: string]: Function;
        }>;

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

### billingAccountPath(billingAccount)
    
    
    billingAccountPath(billingAccount: string): string;

Return a fully-qualified billingAccount resource name string.

**Parameter**  
---  
**Name** | **Description**  
`billingAccount` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### budgetPath(billingAccount, budget)
    
    
    budgetPath(billingAccount: string, budget: string): string;

Return a fully-qualified budget resource name string.

**Parameters**  
---  
**Name** | **Description**  
`billingAccount` |  `string`   
  
`budget` |  `string`   
  
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
  
### createBudget(request, options)
    
    
    createBudget(request?: protos.google.cloud.billing.budgets.v1beta1.ICreateBudgetRequest, options?: CallOptions): Promise<[
            protos.google.cloud.billing.budgets.v1beta1.IBudget,
            (protos.google.cloud.billing.budgets.v1beta1.ICreateBudgetRequest | undefined),
            {} | undefined
        ]>;

Creates a new budget. See [Quotas and limits](<https://cloud.google.com/billing/quotas>) for more information on the limits of the number of budgets you can create.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateBudgetRequest](https://docs.cloud.google.com/nodejs/docs/reference/billing-budgets/latest/billing-budgets/protos.google.cloud.billing.budgets.v1beta1.icreatebudgetrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.billing.budgets.v1beta1.IBudget](https://docs.cloud.google.com/nodejs/docs/reference/billing-budgets/latest/billing-budgets/protos.google.cloud.billing.budgets.v1beta1.ibudget), ([protos.google.cloud.billing.budgets.v1beta1.ICreateBudgetRequest](https://docs.cloud.google.com/nodejs/docs/reference/billing-budgets/latest/billing-budgets/protos.google.cloud.billing.budgets.v1beta1.icreatebudgetrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [Budget](https://docs.cloud.google.com/nodejs/docs/reference/billing-budgets/latest/billing-budgets/protos.google.cloud.billing.budgets.v1beta1.budget). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The name of the billing account to create the budget in. Values
       *  are of the form `billingAccounts/{billingAccountId}`.
       */
      // const parent = 'abc123'
      /**
       *  Required. Budget to create.
       */
      // const budget = {}
    
      // Imports the Budgets library
      const {BudgetServiceClient} = require('[@google-cloud/billing-budgets](https://docs.cloud.google.com/nodejs/docs/reference/billing-budgets/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const budgetsClient = new [BudgetServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/billing-budgets/latest/overview.html)();
    
      async function callCreateBudget() {
        // Construct request
        const request = {
          parent,
          budget,
        };
    
        // Run request
        const response = await budgetsClient.createBudget(request);
        console.log(response);
      }
    
      callCreateBudget();
    
    

### createBudget(request, options, callback)
    
    
    createBudget(request: protos.google.cloud.billing.budgets.v1beta1.ICreateBudgetRequest, options: CallOptions, callback: Callback<protos.google.cloud.billing.budgets.v1beta1.IBudget, protos.google.cloud.billing.budgets.v1beta1.ICreateBudgetRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateBudgetRequest](https://docs.cloud.google.com/nodejs/docs/reference/billing-budgets/latest/billing-budgets/protos.google.cloud.billing.budgets.v1beta1.icreatebudgetrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.billing.budgets.v1beta1.IBudget](https://docs.cloud.google.com/nodejs/docs/reference/billing-budgets/latest/billing-budgets/protos.google.cloud.billing.budgets.v1beta1.ibudget), [protos.google.cloud.billing.budgets.v1beta1.ICreateBudgetRequest](https://docs.cloud.google.com/nodejs/docs/reference/billing-budgets/latest/billing-budgets/protos.google.cloud.billing.budgets.v1beta1.icreatebudgetrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createBudget(request, callback)
    
    
    createBudget(request: protos.google.cloud.billing.budgets.v1beta1.ICreateBudgetRequest, callback: Callback<protos.google.cloud.billing.budgets.v1beta1.IBudget, protos.google.cloud.billing.budgets.v1beta1.ICreateBudgetRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateBudgetRequest](https://docs.cloud.google.com/nodejs/docs/reference/billing-budgets/latest/billing-budgets/protos.google.cloud.billing.budgets.v1beta1.icreatebudgetrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.billing.budgets.v1beta1.IBudget](https://docs.cloud.google.com/nodejs/docs/reference/billing-budgets/latest/billing-budgets/protos.google.cloud.billing.budgets.v1beta1.ibudget), [protos.google.cloud.billing.budgets.v1beta1.ICreateBudgetRequest](https://docs.cloud.google.com/nodejs/docs/reference/billing-budgets/latest/billing-budgets/protos.google.cloud.billing.budgets.v1beta1.icreatebudgetrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteBudget(request, options)
    
    
    deleteBudget(request?: protos.google.cloud.billing.budgets.v1beta1.IDeleteBudgetRequest, options?: CallOptions): Promise<[
            protos.google.protobuf.IEmpty,
            (protos.google.cloud.billing.budgets.v1beta1.IDeleteBudgetRequest | undefined),
            {} | undefined
        ]>;

Deletes a budget. Returns successfully if already deleted.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteBudgetRequest](https://docs.cloud.google.com/nodejs/docs/reference/billing-budgets/latest/billing-budgets/protos.google.cloud.billing.budgets.v1beta1.ideletebudgetrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/billing-budgets/latest/billing-budgets/protos.google.protobuf.iempty), ([protos.google.cloud.billing.budgets.v1beta1.IDeleteBudgetRequest](https://docs.cloud.google.com/nodejs/docs/reference/billing-budgets/latest/billing-budgets/protos.google.cloud.billing.budgets.v1beta1.ideletebudgetrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [Empty](https://docs.cloud.google.com/nodejs/docs/reference/billing-budgets/latest/billing-budgets/protos.google.protobuf.empty). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Name of the budget to delete. Values are of the form
       *  `billingAccounts/{billingAccountId}/budgets/{budgetId}`.
       */
      // const name = 'abc123'
    
      // Imports the Budgets library
      const {BudgetServiceClient} = require('[@google-cloud/billing-budgets](https://docs.cloud.google.com/nodejs/docs/reference/billing-budgets/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const budgetsClient = new [BudgetServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/billing-budgets/latest/overview.html)();
    
      async function callDeleteBudget() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await budgetsClient.deleteBudget(request);
        console.log(response);
      }
    
      callDeleteBudget();
    
    

### deleteBudget(request, options, callback)
    
    
    deleteBudget(request: protos.google.cloud.billing.budgets.v1beta1.IDeleteBudgetRequest, options: CallOptions, callback: Callback<protos.google.protobuf.IEmpty, protos.google.cloud.billing.budgets.v1beta1.IDeleteBudgetRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteBudgetRequest](https://docs.cloud.google.com/nodejs/docs/reference/billing-budgets/latest/billing-budgets/protos.google.cloud.billing.budgets.v1beta1.ideletebudgetrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/billing-budgets/latest/billing-budgets/protos.google.protobuf.iempty), [protos.google.cloud.billing.budgets.v1beta1.IDeleteBudgetRequest](https://docs.cloud.google.com/nodejs/docs/reference/billing-budgets/latest/billing-budgets/protos.google.cloud.billing.budgets.v1beta1.ideletebudgetrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteBudget(request, callback)
    
    
    deleteBudget(request: protos.google.cloud.billing.budgets.v1beta1.IDeleteBudgetRequest, callback: Callback<protos.google.protobuf.IEmpty, protos.google.cloud.billing.budgets.v1beta1.IDeleteBudgetRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteBudgetRequest](https://docs.cloud.google.com/nodejs/docs/reference/billing-budgets/latest/billing-budgets/protos.google.cloud.billing.budgets.v1beta1.ideletebudgetrequest)`   
  
`callback` |  `Callback<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/billing-budgets/latest/billing-budgets/protos.google.protobuf.iempty), [protos.google.cloud.billing.budgets.v1beta1.IDeleteBudgetRequest](https://docs.cloud.google.com/nodejs/docs/reference/billing-budgets/latest/billing-budgets/protos.google.cloud.billing.budgets.v1beta1.ideletebudgetrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getBudget(request, options)
    
    
    getBudget(request?: protos.google.cloud.billing.budgets.v1beta1.IGetBudgetRequest, options?: CallOptions): Promise<[
            protos.google.cloud.billing.budgets.v1beta1.IBudget,
            protos.google.cloud.billing.budgets.v1beta1.IGetBudgetRequest | undefined,
            {} | undefined
        ]>;

Returns a budget.

WARNING: There are some fields exposed on the Google Cloud Console that aren't available on this API. When reading from the API, you will not see these fields in the return value, though they may have been set in the Cloud Console.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetBudgetRequest](https://docs.cloud.google.com/nodejs/docs/reference/billing-budgets/latest/billing-budgets/protos.google.cloud.billing.budgets.v1beta1.igetbudgetrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.billing.budgets.v1beta1.IBudget](https://docs.cloud.google.com/nodejs/docs/reference/billing-budgets/latest/billing-budgets/protos.google.cloud.billing.budgets.v1beta1.ibudget), [protos.google.cloud.billing.budgets.v1beta1.IGetBudgetRequest](https://docs.cloud.google.com/nodejs/docs/reference/billing-budgets/latest/billing-budgets/protos.google.cloud.billing.budgets.v1beta1.igetbudgetrequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [Budget](https://docs.cloud.google.com/nodejs/docs/reference/billing-budgets/latest/billing-budgets/protos.google.cloud.billing.budgets.v1beta1.budget). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Name of budget to get. Values are of the form
       *  `billingAccounts/{billingAccountId}/budgets/{budgetId}`.
       */
      // const name = 'abc123'
    
      // Imports the Budgets library
      const {BudgetServiceClient} = require('[@google-cloud/billing-budgets](https://docs.cloud.google.com/nodejs/docs/reference/billing-budgets/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const budgetsClient = new [BudgetServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/billing-budgets/latest/overview.html)();
    
      async function callGetBudget() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await budgetsClient.getBudget(request);
        console.log(response);
      }
    
      callGetBudget();
    
    

### getBudget(request, options, callback)
    
    
    getBudget(request: protos.google.cloud.billing.budgets.v1beta1.IGetBudgetRequest, options: CallOptions, callback: Callback<protos.google.cloud.billing.budgets.v1beta1.IBudget, protos.google.cloud.billing.budgets.v1beta1.IGetBudgetRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetBudgetRequest](https://docs.cloud.google.com/nodejs/docs/reference/billing-budgets/latest/billing-budgets/protos.google.cloud.billing.budgets.v1beta1.igetbudgetrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.billing.budgets.v1beta1.IBudget](https://docs.cloud.google.com/nodejs/docs/reference/billing-budgets/latest/billing-budgets/protos.google.cloud.billing.budgets.v1beta1.ibudget), [protos.google.cloud.billing.budgets.v1beta1.IGetBudgetRequest](https://docs.cloud.google.com/nodejs/docs/reference/billing-budgets/latest/billing-budgets/protos.google.cloud.billing.budgets.v1beta1.igetbudgetrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getBudget(request, callback)
    
    
    getBudget(request: protos.google.cloud.billing.budgets.v1beta1.IGetBudgetRequest, callback: Callback<protos.google.cloud.billing.budgets.v1beta1.IBudget, protos.google.cloud.billing.budgets.v1beta1.IGetBudgetRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetBudgetRequest](https://docs.cloud.google.com/nodejs/docs/reference/billing-budgets/latest/billing-budgets/protos.google.cloud.billing.budgets.v1beta1.igetbudgetrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.billing.budgets.v1beta1.IBudget](https://docs.cloud.google.com/nodejs/docs/reference/billing-budgets/latest/billing-budgets/protos.google.cloud.billing.budgets.v1beta1.ibudget), [protos.google.cloud.billing.budgets.v1beta1.IGetBudgetRequest](https://docs.cloud.google.com/nodejs/docs/reference/billing-budgets/latest/billing-budgets/protos.google.cloud.billing.budgets.v1beta1.igetbudgetrequest) | null | undefined, {} | null | undefined>`   
  
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
  
### listBudgets(request, options)
    
    
    listBudgets(request?: protos.google.cloud.billing.budgets.v1beta1.IListBudgetsRequest, options?: CallOptions): Promise<[
            protos.google.cloud.billing.budgets.v1beta1.IBudget[],
            protos.google.cloud.billing.budgets.v1beta1.IListBudgetsRequest | null,
            protos.google.cloud.billing.budgets.v1beta1.IListBudgetsResponse
        ]>;

Returns a list of budgets for a billing account.

WARNING: There are some fields exposed on the Google Cloud Console that aren't available on this API. When reading from the API, you will not see these fields in the return value, though they may have been set in the Cloud Console.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListBudgetsRequest](https://docs.cloud.google.com/nodejs/docs/reference/billing-budgets/latest/billing-budgets/protos.google.cloud.billing.budgets.v1beta1.ilistbudgetsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.billing.budgets.v1beta1.IBudget](https://docs.cloud.google.com/nodejs/docs/reference/billing-budgets/latest/billing-budgets/protos.google.cloud.billing.budgets.v1beta1.ibudget)[], [protos.google.cloud.billing.budgets.v1beta1.IListBudgetsRequest](https://docs.cloud.google.com/nodejs/docs/reference/billing-budgets/latest/billing-budgets/protos.google.cloud.billing.budgets.v1beta1.ilistbudgetsrequest) | null, [protos.google.cloud.billing.budgets.v1beta1.IListBudgetsResponse](https://docs.cloud.google.com/nodejs/docs/reference/billing-budgets/latest/billing-budgets/protos.google.cloud.billing.budgets.v1beta1.ilistbudgetsresponse) ]>` | {Promise} - The promise which resolves to an array. The first element of the array is Array of [Budget](https://docs.cloud.google.com/nodejs/docs/reference/billing-budgets/latest/billing-budgets/protos.google.cloud.billing.budgets.v1beta1.budget). The client library will perform auto-pagination by default: it will call the API as many times as needed and will merge results from all the pages into this array. Note that it can affect your quota. We recommend using `listBudgetsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listBudgets(request, options, callback)
    
    
    listBudgets(request: protos.google.cloud.billing.budgets.v1beta1.IListBudgetsRequest, options: CallOptions, callback: PaginationCallback<protos.google.cloud.billing.budgets.v1beta1.IListBudgetsRequest, protos.google.cloud.billing.budgets.v1beta1.IListBudgetsResponse | null | undefined, protos.google.cloud.billing.budgets.v1beta1.IBudget>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListBudgetsRequest](https://docs.cloud.google.com/nodejs/docs/reference/billing-budgets/latest/billing-budgets/protos.google.cloud.billing.budgets.v1beta1.ilistbudgetsrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.billing.budgets.v1beta1.IListBudgetsRequest](https://docs.cloud.google.com/nodejs/docs/reference/billing-budgets/latest/billing-budgets/protos.google.cloud.billing.budgets.v1beta1.ilistbudgetsrequest), [protos.google.cloud.billing.budgets.v1beta1.IListBudgetsResponse](https://docs.cloud.google.com/nodejs/docs/reference/billing-budgets/latest/billing-budgets/protos.google.cloud.billing.budgets.v1beta1.ilistbudgetsresponse) | null | undefined, [protos.google.cloud.billing.budgets.v1beta1.IBudget](https://docs.cloud.google.com/nodejs/docs/reference/billing-budgets/latest/billing-budgets/protos.google.cloud.billing.budgets.v1beta1.ibudget)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listBudgets(request, callback)
    
    
    listBudgets(request: protos.google.cloud.billing.budgets.v1beta1.IListBudgetsRequest, callback: PaginationCallback<protos.google.cloud.billing.budgets.v1beta1.IListBudgetsRequest, protos.google.cloud.billing.budgets.v1beta1.IListBudgetsResponse | null | undefined, protos.google.cloud.billing.budgets.v1beta1.IBudget>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListBudgetsRequest](https://docs.cloud.google.com/nodejs/docs/reference/billing-budgets/latest/billing-budgets/protos.google.cloud.billing.budgets.v1beta1.ilistbudgetsrequest)`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.billing.budgets.v1beta1.IListBudgetsRequest](https://docs.cloud.google.com/nodejs/docs/reference/billing-budgets/latest/billing-budgets/protos.google.cloud.billing.budgets.v1beta1.ilistbudgetsrequest), [protos.google.cloud.billing.budgets.v1beta1.IListBudgetsResponse](https://docs.cloud.google.com/nodejs/docs/reference/billing-budgets/latest/billing-budgets/protos.google.cloud.billing.budgets.v1beta1.ilistbudgetsresponse) | null | undefined, [protos.google.cloud.billing.budgets.v1beta1.IBudget](https://docs.cloud.google.com/nodejs/docs/reference/billing-budgets/latest/billing-budgets/protos.google.cloud.billing.budgets.v1beta1.ibudget)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listBudgetsAsync(request, options)
    
    
    listBudgetsAsync(request?: protos.google.cloud.billing.budgets.v1beta1.IListBudgetsRequest, options?: CallOptions): AsyncIterable<protos.google.cloud.billing.budgets.v1beta1.IBudget>;

Equivalent to `listBudgets`, but returns an iterable object.

`for`-`await`-`of` syntax is used with the iterable to get response elements on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListBudgetsRequest](https://docs.cloud.google.com/nodejs/docs/reference/billing-budgets/latest/billing-budgets/protos.google.cloud.billing.budgets.v1beta1.ilistbudgetsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.cloud.billing.budgets.v1beta1.IBudget](https://docs.cloud.google.com/nodejs/docs/reference/billing-budgets/latest/billing-budgets/protos.google.cloud.billing.budgets.v1beta1.ibudget)>` | {Object} An iterable Object that allows [async iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols). When you iterate the returned iterable, each element will be an object representing [Budget](https://docs.cloud.google.com/nodejs/docs/reference/billing-budgets/latest/billing-budgets/protos.google.cloud.billing.budgets.v1beta1.budget). The API will be called under the hood as needed, once per the page, so you can stop the iteration when you don't need more results. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Name of billing account to list budgets under. Values
       *  are of the form `billingAccounts/{billingAccountId}`.
       */
      // const parent = 'abc123'
      /**
       *  Optional. Set the scope of the budgets to be returned, in the format of the
       *  resource name. The scope of a budget is the cost that it tracks, such as
       *  costs for a single project, or the costs for all projects in a folder. Only
       *  project scope (in the format of "projects/project-id" or "projects/123") is
       *  supported in this field. When this field is set to a project's resource
       *  name, the budgets returned are tracking the costs for that project.
       */
      // const scope = 'abc123'
      /**
       *  Optional. The maximum number of budgets to return per page.
       *  The default and maximum value are 100.
       */
      // const pageSize = 1234
      /**
       *  Optional. The value returned by the last `ListBudgetsResponse` which
       *  indicates that this is a continuation of a prior `ListBudgets` call,
       *  and that the system should return the next page of data.
       */
      // const pageToken = 'abc123'
    
      // Imports the Budgets library
      const {BudgetServiceClient} = require('[@google-cloud/billing-budgets](https://docs.cloud.google.com/nodejs/docs/reference/billing-budgets/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const budgetsClient = new [BudgetServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/billing-budgets/latest/overview.html)();
    
      async function callListBudgets() {
        // Construct request
        const request = {
          parent,
        };
    
        // Run request
        const iterable = budgetsClient.listBudgetsAsync(request);
        for await (const response of iterable) {
            console.log(response);
        }
      }
    
      callListBudgets();
    
    

### listBudgetsStream(request, options)
    
    
    listBudgetsStream(request?: protos.google.cloud.billing.budgets.v1beta1.IListBudgetsRequest, options?: CallOptions): Transform;

Equivalent to `listBudgets`, but returns a NodeJS Stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListBudgetsRequest](https://docs.cloud.google.com/nodejs/docs/reference/billing-budgets/latest/billing-budgets/protos.google.cloud.billing.budgets.v1beta1.ilistbudgetsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Transform` | {Stream} An object stream which emits an object representing [Budget](https://docs.cloud.google.com/nodejs/docs/reference/billing-budgets/latest/billing-budgets/protos.google.cloud.billing.budgets.v1beta1.budget) on 'data' event. The client library will perform auto-pagination by default: it will call the API as many times as needed. Note that it can affect your quota. We recommend using `listBudgetsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### matchBillingAccountFromBillingAccountName(billingAccountName)
    
    
    matchBillingAccountFromBillingAccountName(billingAccountName: string): string | number;

Parse the billing_account from BillingAccount resource.

**Parameter**  
---  
**Name** | **Description**  
`billingAccountName` |  `string`   
A fully-qualified path representing BillingAccount resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the billing_account.  
  
### matchBillingAccountFromBudgetName(budgetName)
    
    
    matchBillingAccountFromBudgetName(budgetName: string): string | number;

Parse the billing_account from Budget resource.

**Parameter**  
---  
**Name** | **Description**  
`budgetName` |  `string`   
A fully-qualified path representing Budget resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the billing_account.  
  
### matchBudgetFromBudgetName(budgetName)
    
    
    matchBudgetFromBudgetName(budgetName: string): string | number;

Parse the budget from Budget resource.

**Parameter**  
---  
**Name** | **Description**  
`budgetName` |  `string`   
A fully-qualified path representing Budget resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the budget.  
  
### updateBudget(request, options)
    
    
    updateBudget(request?: protos.google.cloud.billing.budgets.v1beta1.IUpdateBudgetRequest, options?: CallOptions): Promise<[
            protos.google.cloud.billing.budgets.v1beta1.IBudget,
            (protos.google.cloud.billing.budgets.v1beta1.IUpdateBudgetRequest | undefined),
            {} | undefined
        ]>;

Updates a budget and returns the updated budget.

WARNING: There are some fields exposed on the Google Cloud Console that aren't available on this API. Budget fields that are not exposed in this API will not be changed by this method.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateBudgetRequest](https://docs.cloud.google.com/nodejs/docs/reference/billing-budgets/latest/billing-budgets/protos.google.cloud.billing.budgets.v1beta1.iupdatebudgetrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.billing.budgets.v1beta1.IBudget](https://docs.cloud.google.com/nodejs/docs/reference/billing-budgets/latest/billing-budgets/protos.google.cloud.billing.budgets.v1beta1.ibudget), ([protos.google.cloud.billing.budgets.v1beta1.IUpdateBudgetRequest](https://docs.cloud.google.com/nodejs/docs/reference/billing-budgets/latest/billing-budgets/protos.google.cloud.billing.budgets.v1beta1.iupdatebudgetrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [Budget](https://docs.cloud.google.com/nodejs/docs/reference/billing-budgets/latest/billing-budgets/protos.google.cloud.billing.budgets.v1beta1.budget). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The updated budget object.
       *  The budget to update is specified by the budget name in the budget.
       */
      // const budget = {}
      /**
       *  Optional. Indicates which fields in the provided budget to update.
       *  Read-only fields (such as `name`) cannot be changed. If this is not
       *  provided, then only fields with non-default values from the request are
       *  updated. See
       *  https://developers.google.com/protocol-buffers/docs/proto3#default for more
       *  details about default values.
       */
      // const updateMask = {}
    
      // Imports the Budgets library
      const {BudgetServiceClient} = require('[@google-cloud/billing-budgets](https://docs.cloud.google.com/nodejs/docs/reference/billing-budgets/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const budgetsClient = new [BudgetServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/billing-budgets/latest/overview.html)();
    
      async function callUpdateBudget() {
        // Construct request
        const request = {
          budget,
        };
    
        // Run request
        const response = await budgetsClient.updateBudget(request);
        console.log(response);
      }
    
      callUpdateBudget();
    
    

### updateBudget(request, options, callback)
    
    
    updateBudget(request: protos.google.cloud.billing.budgets.v1beta1.IUpdateBudgetRequest, options: CallOptions, callback: Callback<protos.google.cloud.billing.budgets.v1beta1.IBudget, protos.google.cloud.billing.budgets.v1beta1.IUpdateBudgetRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateBudgetRequest](https://docs.cloud.google.com/nodejs/docs/reference/billing-budgets/latest/billing-budgets/protos.google.cloud.billing.budgets.v1beta1.iupdatebudgetrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.billing.budgets.v1beta1.IBudget](https://docs.cloud.google.com/nodejs/docs/reference/billing-budgets/latest/billing-budgets/protos.google.cloud.billing.budgets.v1beta1.ibudget), [protos.google.cloud.billing.budgets.v1beta1.IUpdateBudgetRequest](https://docs.cloud.google.com/nodejs/docs/reference/billing-budgets/latest/billing-budgets/protos.google.cloud.billing.budgets.v1beta1.iupdatebudgetrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateBudget(request, callback)
    
    
    updateBudget(request: protos.google.cloud.billing.budgets.v1beta1.IUpdateBudgetRequest, callback: Callback<protos.google.cloud.billing.budgets.v1beta1.IBudget, protos.google.cloud.billing.budgets.v1beta1.IUpdateBudgetRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateBudgetRequest](https://docs.cloud.google.com/nodejs/docs/reference/billing-budgets/latest/billing-budgets/protos.google.cloud.billing.budgets.v1beta1.iupdatebudgetrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.billing.budgets.v1beta1.IBudget](https://docs.cloud.google.com/nodejs/docs/reference/billing-budgets/latest/billing-budgets/protos.google.cloud.billing.budgets.v1beta1.ibudget), [protos.google.cloud.billing.budgets.v1beta1.IUpdateBudgetRequest](https://docs.cloud.google.com/nodejs/docs/reference/billing-budgets/latest/billing-budgets/protos.google.cloud.billing.budgets.v1beta1.iupdatebudgetrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
