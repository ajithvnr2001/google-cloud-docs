---
url: https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/v1alpha.alphaanalyticsdataclient
title: Class v1alpha.AlphaAnalyticsDataClient (7.2.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:54:39.413512+00:00
---

# Class v1alpha.AlphaAnalyticsDataClient (7.2.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/v1alpha.alphaanalyticsdataclient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class v1alpha.AlphaAnalyticsDataClient (7.2.1) Stay organized with collections  Save and categorize content based on your preferences. 

7.2.1 (latest)  7.2.0  7.1.0  6.1.0  6.0.0  4.12.0  4.11.0  4.9.0  4.8.0  4.6.0  4.5.0  3.2.1 

Google Analytics reporting data service. v1alpha

## Package

[@google-analytics/data](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/overview.html)

## Constructors 

### (constructor)(opts, gaxInstance)
    
    
    constructor(opts?: ClientOptions, gaxInstance?: typeof gax | typeof gax.fallback);

Construct an instance of AlphaAnalyticsDataClient.

**Parameters**  
---  
**Name** | **Description**  
`opts` |  `ClientOptions`   
  
`gaxInstance` |  `typeof gax | typeof fallback`   
: loaded instance of `google-gax`. Useful if you need to avoid loading the default gRPC version and want to use the fallback HTTP implementation. Load only fallback version and pass it to the constructor: ``` const gax = require('google-gax/build/src/fallback'); // avoids loading google-gax with gRPC const client = new AlphaAnalyticsDataClient({fallback: true}, gax); ```  
  
## Properties 

### alphaAnalyticsDataStub
    
    
    alphaAnalyticsDataStub?: Promise<{
            [name: string]: Function;
        }>;

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

### operationsClient
    
    
    operationsClient: gax.OperationsClient;

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

### audienceListPath(property, audienceList)
    
    
    audienceListPath(property: string, audienceList: string): string;

Return a fully-qualified audienceList resource name string.

**Parameters**  
---  
**Name** | **Description**  
`property` |  `string`   
  
`audienceList` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### cancelOperation(request, optionsOrCallback, callback)
    
    
    cancelOperation(request: protos.google.longrunning.CancelOperationRequest, optionsOrCallback?: gax.CallOptions | Callback<protos.google.longrunning.CancelOperationRequest, protos.google.protobuf.Empty, {} | undefined | null>, callback?: Callback<protos.google.longrunning.CancelOperationRequest, protos.google.protobuf.Empty, {} | undefined | null>): Promise<protos.google.protobuf.Empty>;

Starts asynchronous cancellation on a long-running operation. The server makes a best effort to cancel the operation, but success is not guaranteed. If the server doesn't support this method, it returns `google.rpc.Code.UNIMPLEMENTED`. Clients can use or other methods to check whether the cancellation succeeded or whether the operation completed despite cancellation. On successful cancellation, the operation is not deleted; instead, it becomes an operation with an value with a of 1, corresponding to `Code.CANCELLED`.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[CancelOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.longrunning.canceloperationrequest)`   
The request object that will be sent.  
`optionsOrCallback` |  `CallOptions | Callback<[protos.google.longrunning.CancelOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.longrunning.canceloperationrequest), [protos.google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.protobuf.empty), {} | undefined | null>`   
  
`callback` |  `Callback<[protos.google.longrunning.CancelOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.longrunning.canceloperationrequest), [protos.google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.protobuf.empty), {} | undefined | null>`   
The function which will be called with the result of the API call. {Promise} - The promise which resolves when API call finishes. The promise has a method named "cancel" which cancels the ongoing API call.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[protos.google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.protobuf.empty)>` |   
**Example**
    
    
    const client = longrunning.operationsClient();
    await client.cancelOperation({name: ''});
    

### chat(request, options)
    
    
    chat(request?: protos.google.analytics.data.v1alpha.IChatRequest, options?: CallOptions): Promise<[
            protos.google.analytics.data.v1alpha.IChatResponse,
            protos.google.analytics.data.v1alpha.IChatRequest | undefined,
            {} | undefined
        ]>;

Provides a chat interface for interacting with Google Analytics data through the API.

This product uses AI and may display inaccurate info. Your chat activity may be used to improve the product and your use is subject to Google's [Terms](<https://policies.google.com/terms>), [AI Use Policy](<https://policies.google.com/terms/generative-ai/use-policy>), and [Privacy Policy](<https://policies.google.com/privacy>). [Learn more about Chat AI Privacy](<https://support.google.com/helpguide/answer/14185196>).

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IChatRequest](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.analytics.data.v1alpha.ichatrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.analytics.data.v1alpha.IChatResponse](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.analytics.data.v1alpha.ichatresponse), [protos.google.analytics.data.v1alpha.IChatRequest](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.analytics.data.v1alpha.ichatrequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [ChatResponse](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.analytics.data.v1alpha.chatresponse). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The property to chat about.
       *  Format: properties/{property}
       */
      // const property = 'abc123'
      /**
       *  Required. The user's query.
       */
      // const userQuery = 'abc123'
      /**
       *  Optional. Provide this session ID to continue an existing conversation
       *  and maintain context. If this field is empty or unset, a new chat
       *  session is created. Invalid session IDs will result in an error.
       */
      // const sessionId = 'abc123'
      /**
       *  Optional. If true, the response will include the current state of this
       *  Analytics Property's quota. Quota is returned in
       *  PropertyChatQuota (#PropertyChatQuota).
       */
      // const returnPropertyQuota = true
    
      // Imports the Data library
      const {AlphaAnalyticsDataClient} = require('[@google-analytics/data](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const dataClient = new [AlphaAnalyticsDataClient](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/v1alpha.alphaanalyticsdataclient.html)();
    
      async function callChat() {
        // Construct request
        const request = {
          property,
          userQuery,
        };
    
        // Run request
        const response = await dataClient.chat(request);
        console.log(response);
      }
    
      callChat();
    
    

### chat(request, options, callback)
    
    
    chat(request: protos.google.analytics.data.v1alpha.IChatRequest, options: CallOptions, callback: Callback<protos.google.analytics.data.v1alpha.IChatResponse, protos.google.analytics.data.v1alpha.IChatRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IChatRequest](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.analytics.data.v1alpha.ichatrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.analytics.data.v1alpha.IChatResponse](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.analytics.data.v1alpha.ichatresponse), [protos.google.analytics.data.v1alpha.IChatRequest](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.analytics.data.v1alpha.ichatrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### chat(request, callback)
    
    
    chat(request: protos.google.analytics.data.v1alpha.IChatRequest, callback: Callback<protos.google.analytics.data.v1alpha.IChatResponse, protos.google.analytics.data.v1alpha.IChatRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IChatRequest](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.analytics.data.v1alpha.ichatrequest)`   
  
`callback` |  `Callback<[protos.google.analytics.data.v1alpha.IChatResponse](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.analytics.data.v1alpha.ichatresponse), [protos.google.analytics.data.v1alpha.IChatRequest](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.analytics.data.v1alpha.ichatrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### checkCreateAudienceListProgress(name)
    
    
    checkCreateAudienceListProgress(name: string): Promise<LROperation<protos.google.analytics.data.v1alpha.AudienceList, protos.google.analytics.data.v1alpha.AudienceListMetadata>>;

Check the status of the long running operation returned by `createAudienceList()`.

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
The operation name that will be passed.  
**Returns**  
---  
**Type** | **Description**  
`Promise<LROperation<[protos.google.analytics.data.v1alpha.AudienceList](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.analytics.data.v1alpha.audiencelist-class), [protos.google.analytics.data.v1alpha.AudienceListMetadata](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.analytics.data.v1alpha.audiencelistmetadata)>>` | {Promise} - The promise which resolves to an object. The decoded operation object has result and metadata field to get information from. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The parent resource where this audience list will be created.
       *  Format: `properties/{property}`
       */
      // const parent = 'abc123'
      /**
       *  Required. The audience list to create.
       */
      // const audienceList = {}
    
      // Imports the Data library
      const {AlphaAnalyticsDataClient} = require('[@google-analytics/data](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const dataClient = new [AlphaAnalyticsDataClient](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/v1alpha.alphaanalyticsdataclient.html)();
    
      async function callCreateAudienceList() {
        // Construct request
        const request = {
          parent,
          audienceList,
        };
    
        // Run request
        const [operation] = await dataClient.createAudienceList(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callCreateAudienceList();
    
    

### checkCreateReportTaskProgress(name)
    
    
    checkCreateReportTaskProgress(name: string): Promise<LROperation<protos.google.analytics.data.v1alpha.ReportTask, protos.google.analytics.data.v1alpha.ReportTaskMetadata>>;

Check the status of the long running operation returned by `createReportTask()`.

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
The operation name that will be passed.  
**Returns**  
---  
**Type** | **Description**  
`Promise<LROperation<[protos.google.analytics.data.v1alpha.ReportTask](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.analytics.data.v1alpha.reporttask-class), [protos.google.analytics.data.v1alpha.ReportTaskMetadata](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.analytics.data.v1alpha.reporttaskmetadata)>>` | {Promise} - The promise which resolves to an object. The decoded operation object has result and metadata field to get information from. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The parent resource where this report task will be created.
       *  Format: `properties/{propertyId}`
       */
      // const parent = 'abc123'
      /**
       *  Required. The report task configuration to create.
       */
      // const reportTask = {}
    
      // Imports the Data library
      const {AlphaAnalyticsDataClient} = require('[@google-analytics/data](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const dataClient = new [AlphaAnalyticsDataClient](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/v1alpha.alphaanalyticsdataclient.html)();
    
      async function callCreateReportTask() {
        // Construct request
        const request = {
          parent,
          reportTask,
        };
    
        // Run request
        const [operation] = await dataClient.createReportTask(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callCreateReportTask();
    
    

### close()
    
    
    close(): Promise<void>;

Terminate the gRPC channel and close the client.

The client will no longer be usable and all future behavior is undefined.

**Returns**  
---  
**Type** | **Description**  
`Promise<void>` | {Promise} A promise that resolves when the client is closed.  
  
### createAudienceList(request, options)
    
    
    createAudienceList(request?: protos.google.analytics.data.v1alpha.ICreateAudienceListRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.analytics.data.v1alpha.IAudienceList, protos.google.analytics.data.v1alpha.IAudienceListMetadata>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Creates an audience list for later retrieval. This method quickly returns the audience list's resource name and initiates a long running asynchronous request to form an audience list. To list the users in an audience list, first create the audience list through this method and then send the audience resource name to the `QueryAudienceList` method.

See [Creating an Audience List](<https://developers.google.com/analytics/devguides/reporting/data/v1/audience-list-basics>) for an introduction to Audience Lists with examples.

An audience list is a snapshot of the users currently in the audience at the time of audience list creation. Creating audience lists for one audience on different days will return different results as users enter and exit the audience.

Audiences in Google Analytics 4 allow you to segment your users in the ways that are important to your business. To learn more, see <https://support.google.com/analytics/answer/9267572>. Audience lists contain the users in each audience.

This method is available at beta stability at [audienceExports.create](<https://developers.google.com/analytics/devguides/reporting/data/v1/rest/v1beta/properties.audienceExports/create>). To give your feedback on this API, complete the [Google Analytics Audience Export API Feedback](<https://forms.gle/EeA5u5LW6PEggtCEA>) form.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateAudienceListRequest](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.analytics.data.v1alpha.icreateaudiencelistrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.analytics.data.v1alpha.IAudienceList](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.analytics.data.v1alpha.iaudiencelist), [protos.google.analytics.data.v1alpha.IAudienceListMetadata](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.analytics.data.v1alpha.iaudiencelistmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.longrunning.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Its `promise()` method returns a promise you can `await` for. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The parent resource where this audience list will be created.
       *  Format: `properties/{property}`
       */
      // const parent = 'abc123'
      /**
       *  Required. The audience list to create.
       */
      // const audienceList = {}
    
      // Imports the Data library
      const {AlphaAnalyticsDataClient} = require('[@google-analytics/data](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const dataClient = new [AlphaAnalyticsDataClient](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/v1alpha.alphaanalyticsdataclient.html)();
    
      async function callCreateAudienceList() {
        // Construct request
        const request = {
          parent,
          audienceList,
        };
    
        // Run request
        const [operation] = await dataClient.createAudienceList(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callCreateAudienceList();
    
    

### createAudienceList(request, options, callback)
    
    
    createAudienceList(request: protos.google.analytics.data.v1alpha.ICreateAudienceListRequest, options: CallOptions, callback: Callback<LROperation<protos.google.analytics.data.v1alpha.IAudienceList, protos.google.analytics.data.v1alpha.IAudienceListMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateAudienceListRequest](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.analytics.data.v1alpha.icreateaudiencelistrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.analytics.data.v1alpha.IAudienceList](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.analytics.data.v1alpha.iaudiencelist), [protos.google.analytics.data.v1alpha.IAudienceListMetadata](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.analytics.data.v1alpha.iaudiencelistmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createAudienceList(request, callback)
    
    
    createAudienceList(request: protos.google.analytics.data.v1alpha.ICreateAudienceListRequest, callback: Callback<LROperation<protos.google.analytics.data.v1alpha.IAudienceList, protos.google.analytics.data.v1alpha.IAudienceListMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateAudienceListRequest](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.analytics.data.v1alpha.icreateaudiencelistrequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.analytics.data.v1alpha.IAudienceList](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.analytics.data.v1alpha.iaudiencelist), [protos.google.analytics.data.v1alpha.IAudienceListMetadata](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.analytics.data.v1alpha.iaudiencelistmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createRecurringAudienceList(request, options)
    
    
    createRecurringAudienceList(request?: protos.google.analytics.data.v1alpha.ICreateRecurringAudienceListRequest, options?: CallOptions): Promise<[
            protos.google.analytics.data.v1alpha.IRecurringAudienceList,
            (protos.google.analytics.data.v1alpha.ICreateRecurringAudienceListRequest | undefined),
            {} | undefined
        ]>;

Creates a recurring audience list. Recurring audience lists produces new audience lists each day. Audience lists are users in an audience at the time of the list's creation.

A recurring audience list ensures that you have audience list based on the most recent data available for use each day. If you manually create audience list, you don't know when an audience list based on an additional day's data is available. This recurring audience list automates the creation of an audience list when an additional day's data is available. You will consume fewer quota tokens by using recurring audience list versus manually creating audience list at various times of day trying to guess when an additional day's data is ready.

This method is introduced at alpha stability with the intention of gathering feedback on syntax and capabilities before entering beta. To give your feedback on this API, complete the [Google Analytics Audience Export API Feedback](<https://forms.gle/EeA5u5LW6PEggtCEA>) form.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateRecurringAudienceListRequest](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.analytics.data.v1alpha.icreaterecurringaudiencelistrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.analytics.data.v1alpha.IRecurringAudienceList](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.analytics.data.v1alpha.irecurringaudiencelist), ([protos.google.analytics.data.v1alpha.ICreateRecurringAudienceListRequest](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.analytics.data.v1alpha.icreaterecurringaudiencelistrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [RecurringAudienceList](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.analytics.data.v1alpha.recurringaudiencelist). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The parent resource where this recurring audience list will be
       *  created. Format: `properties/{property}`
       */
      // const parent = 'abc123'
      /**
       *  Required. The recurring audience list to create.
       */
      // const recurringAudienceList = {}
    
      // Imports the Data library
      const {AlphaAnalyticsDataClient} = require('[@google-analytics/data](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const dataClient = new [AlphaAnalyticsDataClient](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/v1alpha.alphaanalyticsdataclient.html)();
    
      async function callCreateRecurringAudienceList() {
        // Construct request
        const request = {
          parent,
          recurringAudienceList,
        };
    
        // Run request
        const response = await dataClient.createRecurringAudienceList(request);
        console.log(response);
      }
    
      callCreateRecurringAudienceList();
    
    

### createRecurringAudienceList(request, options, callback)
    
    
    createRecurringAudienceList(request: protos.google.analytics.data.v1alpha.ICreateRecurringAudienceListRequest, options: CallOptions, callback: Callback<protos.google.analytics.data.v1alpha.IRecurringAudienceList, protos.google.analytics.data.v1alpha.ICreateRecurringAudienceListRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateRecurringAudienceListRequest](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.analytics.data.v1alpha.icreaterecurringaudiencelistrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.analytics.data.v1alpha.IRecurringAudienceList](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.analytics.data.v1alpha.irecurringaudiencelist), [protos.google.analytics.data.v1alpha.ICreateRecurringAudienceListRequest](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.analytics.data.v1alpha.icreaterecurringaudiencelistrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createRecurringAudienceList(request, callback)
    
    
    createRecurringAudienceList(request: protos.google.analytics.data.v1alpha.ICreateRecurringAudienceListRequest, callback: Callback<protos.google.analytics.data.v1alpha.IRecurringAudienceList, protos.google.analytics.data.v1alpha.ICreateRecurringAudienceListRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateRecurringAudienceListRequest](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.analytics.data.v1alpha.icreaterecurringaudiencelistrequest)`   
  
`callback` |  `Callback<[protos.google.analytics.data.v1alpha.IRecurringAudienceList](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.analytics.data.v1alpha.irecurringaudiencelist), [protos.google.analytics.data.v1alpha.ICreateRecurringAudienceListRequest](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.analytics.data.v1alpha.icreaterecurringaudiencelistrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createReportTask(request, options)
    
    
    createReportTask(request?: protos.google.analytics.data.v1alpha.ICreateReportTaskRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.analytics.data.v1alpha.IReportTask, protos.google.analytics.data.v1alpha.IReportTaskMetadata>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Initiates the creation of a report task. This method quickly returns a report task and initiates a long running asynchronous request to form a customized report of your Google Analytics event data.

A report task will be retained and available for querying for 72 hours after it has been created.

A report task created by one user can be listed and queried by all users who have access to the property.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateReportTaskRequest](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.analytics.data.v1alpha.icreatereporttaskrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.analytics.data.v1alpha.IReportTask](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.analytics.data.v1alpha.ireporttask), [protos.google.analytics.data.v1alpha.IReportTaskMetadata](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.analytics.data.v1alpha.ireporttaskmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.longrunning.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Its `promise()` method returns a promise you can `await` for. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The parent resource where this report task will be created.
       *  Format: `properties/{propertyId}`
       */
      // const parent = 'abc123'
      /**
       *  Required. The report task configuration to create.
       */
      // const reportTask = {}
    
      // Imports the Data library
      const {AlphaAnalyticsDataClient} = require('[@google-analytics/data](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const dataClient = new [AlphaAnalyticsDataClient](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/v1alpha.alphaanalyticsdataclient.html)();
    
      async function callCreateReportTask() {
        // Construct request
        const request = {
          parent,
          reportTask,
        };
    
        // Run request
        const [operation] = await dataClient.createReportTask(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callCreateReportTask();
    
    

### createReportTask(request, options, callback)
    
    
    createReportTask(request: protos.google.analytics.data.v1alpha.ICreateReportTaskRequest, options: CallOptions, callback: Callback<LROperation<protos.google.analytics.data.v1alpha.IReportTask, protos.google.analytics.data.v1alpha.IReportTaskMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateReportTaskRequest](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.analytics.data.v1alpha.icreatereporttaskrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.analytics.data.v1alpha.IReportTask](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.analytics.data.v1alpha.ireporttask), [protos.google.analytics.data.v1alpha.IReportTaskMetadata](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.analytics.data.v1alpha.ireporttaskmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createReportTask(request, callback)
    
    
    createReportTask(request: protos.google.analytics.data.v1alpha.ICreateReportTaskRequest, callback: Callback<LROperation<protos.google.analytics.data.v1alpha.IReportTask, protos.google.analytics.data.v1alpha.IReportTaskMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateReportTaskRequest](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.analytics.data.v1alpha.icreatereporttaskrequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.analytics.data.v1alpha.IReportTask](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.analytics.data.v1alpha.ireporttask), [protos.google.analytics.data.v1alpha.IReportTaskMetadata](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.analytics.data.v1alpha.ireporttaskmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteOperation(request, optionsOrCallback, callback)
    
    
    deleteOperation(request: protos.google.longrunning.DeleteOperationRequest, optionsOrCallback?: gax.CallOptions | Callback<protos.google.protobuf.Empty, protos.google.longrunning.DeleteOperationRequest, {} | null | undefined>, callback?: Callback<protos.google.protobuf.Empty, protos.google.longrunning.DeleteOperationRequest, {} | null | undefined>): Promise<protos.google.protobuf.Empty>;

Deletes a long-running operation. This method indicates that the client is no longer interested in the operation result. It does not cancel the operation. If the server doesn't support this method, it returns `google.rpc.Code.UNIMPLEMENTED`.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[DeleteOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.longrunning.deleteoperationrequest)`   
The request object that will be sent.  
`optionsOrCallback` |  `CallOptions | Callback<[protos.google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.protobuf.empty), [protos.google.longrunning.DeleteOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.longrunning.deleteoperationrequest), {} | null | undefined>`   
  
`callback` |  `Callback<[protos.google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.protobuf.empty), [protos.google.longrunning.DeleteOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.longrunning.deleteoperationrequest), {} | null | undefined>`   
The function which will be called with the result of the API call. {Promise} - The promise which resolves when API call finishes. The promise has a method named "cancel" which cancels the ongoing API call.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[protos.google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.protobuf.empty)>` |   
**Example**
    
    
    const client = longrunning.operationsClient();
    await client.deleteOperation({name: ''});
    

### getAudienceList(request, options)
    
    
    getAudienceList(request?: protos.google.analytics.data.v1alpha.IGetAudienceListRequest, options?: CallOptions): Promise<[
            protos.google.analytics.data.v1alpha.IAudienceList,
            protos.google.analytics.data.v1alpha.IGetAudienceListRequest | undefined,
            {} | undefined
        ]>;

Gets configuration metadata about a specific audience list. This method can be used to understand an audience list after it has been created.

See [Creating an Audience List](<https://developers.google.com/analytics/devguides/reporting/data/v1/audience-list-basics>) for an introduction to Audience Lists with examples.

This method is available at beta stability at [audienceExports.get](<https://developers.google.com/analytics/devguides/reporting/data/v1/rest/v1beta/properties.audienceExports/get>). To give your feedback on this API, complete the [Google Analytics Audience Export API Feedback](<https://forms.gle/EeA5u5LW6PEggtCEA>) form.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetAudienceListRequest](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.analytics.data.v1alpha.igetaudiencelistrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.analytics.data.v1alpha.IAudienceList](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.analytics.data.v1alpha.iaudiencelist), [protos.google.analytics.data.v1alpha.IGetAudienceListRequest](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.analytics.data.v1alpha.igetaudiencelistrequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The audience list resource name.
       *  Format: `properties/{property}/audienceLists/{audience_list}`
       */
      // const name = 'abc123'
    
      // Imports the Data library
      const {AlphaAnalyticsDataClient} = require('[@google-analytics/data](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const dataClient = new [AlphaAnalyticsDataClient](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/v1alpha.alphaanalyticsdataclient.html)();
    
      async function callGetAudienceList() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await dataClient.getAudienceList(request);
        console.log(response);
      }
    
      callGetAudienceList();
    
    

### getAudienceList(request, options, callback)
    
    
    getAudienceList(request: protos.google.analytics.data.v1alpha.IGetAudienceListRequest, options: CallOptions, callback: Callback<protos.google.analytics.data.v1alpha.IAudienceList, protos.google.analytics.data.v1alpha.IGetAudienceListRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetAudienceListRequest](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.analytics.data.v1alpha.igetaudiencelistrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.analytics.data.v1alpha.IAudienceList](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.analytics.data.v1alpha.iaudiencelist), [protos.google.analytics.data.v1alpha.IGetAudienceListRequest](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.analytics.data.v1alpha.igetaudiencelistrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getAudienceList(request, callback)
    
    
    getAudienceList(request: protos.google.analytics.data.v1alpha.IGetAudienceListRequest, callback: Callback<protos.google.analytics.data.v1alpha.IAudienceList, protos.google.analytics.data.v1alpha.IGetAudienceListRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetAudienceListRequest](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.analytics.data.v1alpha.igetaudiencelistrequest)`   
  
`callback` |  `Callback<[protos.google.analytics.data.v1alpha.IAudienceList](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.analytics.data.v1alpha.iaudiencelist), [protos.google.analytics.data.v1alpha.IGetAudienceListRequest](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.analytics.data.v1alpha.igetaudiencelistrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getMetadata(request, options)
    
    
    getMetadata(request?: protos.google.analytics.data.v1alpha.IGetMetadataRequest, options?: CallOptions): Promise<[
            protos.google.analytics.data.v1alpha.IMetadata,
            protos.google.analytics.data.v1alpha.IGetMetadataRequest | undefined,
            {} | undefined
        ]>;

Returns metadata for dimensions and metrics available in reporting methods. Used to explore the dimensions and metrics. In this method, a Google Analytics property identifier is specified in the request, and the metadata response includes Custom dimensions and metrics as well as Universal metadata.

For example if a custom metric with parameter name `levels_unlocked` is registered to a property, the Metadata response will contain `customEvent:levels_unlocked`. Universal metadata are dimensions and metrics applicable to any property such as `country` and `totalUsers`.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetMetadataRequest](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.analytics.data.v1alpha.igetmetadatarequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.analytics.data.v1alpha.IMetadata](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.analytics.data.v1alpha.imetadata), [protos.google.analytics.data.v1alpha.IGetMetadataRequest](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.analytics.data.v1alpha.igetmetadatarequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [Metadata](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.analytics.data.v1alpha.metadata). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The resource name of the metadata to retrieve. This name field is
       *  specified in the URL path and not URL parameters. Property is a numeric
       *  Google Analytics property identifier. To learn more, see where to find
       *  your Property
       *  ID (https://developers.google.com/analytics/devguides/reporting/data/v1/property-id).
       *  Example: properties/1234/metadata
       *  Set the Property ID to 0 for dimensions and metrics common to all
       *  properties. In this special mode, this method will not return custom
       *  dimensions and metrics.
       */
      // const name = 'abc123'
    
      // Imports the Data library
      const {AlphaAnalyticsDataClient} = require('[@google-analytics/data](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const dataClient = new [AlphaAnalyticsDataClient](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/v1alpha.alphaanalyticsdataclient.html)();
    
      async function callGetMetadata() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await dataClient.getMetadata(request);
        console.log(response);
      }
    
      callGetMetadata();
    
    

### getMetadata(request, options, callback)
    
    
    getMetadata(request: protos.google.analytics.data.v1alpha.IGetMetadataRequest, options: CallOptions, callback: Callback<protos.google.analytics.data.v1alpha.IMetadata, protos.google.analytics.data.v1alpha.IGetMetadataRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetMetadataRequest](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.analytics.data.v1alpha.igetmetadatarequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.analytics.data.v1alpha.IMetadata](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.analytics.data.v1alpha.imetadata), [protos.google.analytics.data.v1alpha.IGetMetadataRequest](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.analytics.data.v1alpha.igetmetadatarequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getMetadata(request, callback)
    
    
    getMetadata(request: protos.google.analytics.data.v1alpha.IGetMetadataRequest, callback: Callback<protos.google.analytics.data.v1alpha.IMetadata, protos.google.analytics.data.v1alpha.IGetMetadataRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetMetadataRequest](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.analytics.data.v1alpha.igetmetadatarequest)`   
  
`callback` |  `Callback<[protos.google.analytics.data.v1alpha.IMetadata](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.analytics.data.v1alpha.imetadata), [protos.google.analytics.data.v1alpha.IGetMetadataRequest](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.analytics.data.v1alpha.igetmetadatarequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getOperation(request, optionsOrCallback, callback)
    
    
    getOperation(request: protos.google.longrunning.GetOperationRequest, optionsOrCallback?: gax.CallOptions | Callback<protos.google.longrunning.Operation, protos.google.longrunning.GetOperationRequest, {} | null | undefined>, callback?: Callback<protos.google.longrunning.Operation, protos.google.longrunning.GetOperationRequest, {} | null | undefined>): Promise<[protos.google.longrunning.Operation]>;

Gets the latest state of a long-running operation. Clients can use this method to poll the operation result at intervals as recommended by the API service.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[GetOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.longrunning.getoperationrequest)`   
The request object that will be sent.  
`optionsOrCallback` |  `CallOptions | Callback<[protos.google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.longrunning.operation), [protos.google.longrunning.GetOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.longrunning.getoperationrequest), {} | null | undefined>`   
  
`callback` |  `Callback<[protos.google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.longrunning.operation), [protos.google.longrunning.GetOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.longrunning.getoperationrequest), {} | null | undefined>`   
The function which will be called with the result of the API call. The second parameter to the callback is an object representing . {Promise} - The promise which resolves to an array. The first element of the array is an object representing . The promise has a method named "cancel" which cancels the ongoing API call.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[[protos.google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.longrunning.operation)]>` |   
**Example**
    
    
    const client = longrunning.operationsClient();
    const name = '';
    const [response] = await client.getOperation({name});
    // doThingsWith(response)
    

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
  
### getPropertyQuotasSnapshot(request, options)
    
    
    getPropertyQuotasSnapshot(request?: protos.google.analytics.data.v1alpha.IGetPropertyQuotasSnapshotRequest, options?: CallOptions): Promise<[
            protos.google.analytics.data.v1alpha.IPropertyQuotasSnapshot,
            (protos.google.analytics.data.v1alpha.IGetPropertyQuotasSnapshotRequest | undefined),
            {} | undefined
        ]>;

Get all property quotas organized by quota category for a given property. This will charge 1 property quota from the category with the most quota.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetPropertyQuotasSnapshotRequest](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.analytics.data.v1alpha.igetpropertyquotassnapshotrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.analytics.data.v1alpha.IPropertyQuotasSnapshot](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.analytics.data.v1alpha.ipropertyquotassnapshot), ([protos.google.analytics.data.v1alpha.IGetPropertyQuotasSnapshotRequest](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.analytics.data.v1alpha.igetpropertyquotassnapshotrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [PropertyQuotasSnapshot](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.analytics.data.v1alpha.propertyquotassnapshot). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Quotas from this property will be listed in the response.
       *  Format: `properties/{property}/propertyQuotasSnapshot`
       */
      // const name = 'abc123'
    
      // Imports the Data library
      const {AlphaAnalyticsDataClient} = require('[@google-analytics/data](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const dataClient = new [AlphaAnalyticsDataClient](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/v1alpha.alphaanalyticsdataclient.html)();
    
      async function callGetPropertyQuotasSnapshot() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await dataClient.getPropertyQuotasSnapshot(request);
        console.log(response);
      }
    
      callGetPropertyQuotasSnapshot();
    
    

### getPropertyQuotasSnapshot(request, options, callback)
    
    
    getPropertyQuotasSnapshot(request: protos.google.analytics.data.v1alpha.IGetPropertyQuotasSnapshotRequest, options: CallOptions, callback: Callback<protos.google.analytics.data.v1alpha.IPropertyQuotasSnapshot, protos.google.analytics.data.v1alpha.IGetPropertyQuotasSnapshotRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetPropertyQuotasSnapshotRequest](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.analytics.data.v1alpha.igetpropertyquotassnapshotrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.analytics.data.v1alpha.IPropertyQuotasSnapshot](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.analytics.data.v1alpha.ipropertyquotassnapshot), [protos.google.analytics.data.v1alpha.IGetPropertyQuotasSnapshotRequest](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.analytics.data.v1alpha.igetpropertyquotassnapshotrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getPropertyQuotasSnapshot(request, callback)
    
    
    getPropertyQuotasSnapshot(request: protos.google.analytics.data.v1alpha.IGetPropertyQuotasSnapshotRequest, callback: Callback<protos.google.analytics.data.v1alpha.IPropertyQuotasSnapshot, protos.google.analytics.data.v1alpha.IGetPropertyQuotasSnapshotRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetPropertyQuotasSnapshotRequest](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.analytics.data.v1alpha.igetpropertyquotassnapshotrequest)`   
  
`callback` |  `Callback<[protos.google.analytics.data.v1alpha.IPropertyQuotasSnapshot](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.analytics.data.v1alpha.ipropertyquotassnapshot), [protos.google.analytics.data.v1alpha.IGetPropertyQuotasSnapshotRequest](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.analytics.data.v1alpha.igetpropertyquotassnapshotrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getRecurringAudienceList(request, options)
    
    
    getRecurringAudienceList(request?: protos.google.analytics.data.v1alpha.IGetRecurringAudienceListRequest, options?: CallOptions): Promise<[
            protos.google.analytics.data.v1alpha.IRecurringAudienceList,
            (protos.google.analytics.data.v1alpha.IGetRecurringAudienceListRequest | undefined),
            {} | undefined
        ]>;

Gets configuration metadata about a specific recurring audience list. This method can be used to understand a recurring audience list's state after it has been created. For example, a recurring audience list resource will generate audience list instances for each day, and this method can be used to get the resource name of the most recent audience list instance.

This method is introduced at alpha stability with the intention of gathering feedback on syntax and capabilities before entering beta. To give your feedback on this API, complete the [Google Analytics Audience Export API Feedback](<https://forms.gle/EeA5u5LW6PEggtCEA>) form.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetRecurringAudienceListRequest](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.analytics.data.v1alpha.igetrecurringaudiencelistrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.analytics.data.v1alpha.IRecurringAudienceList](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.analytics.data.v1alpha.irecurringaudiencelist), ([protos.google.analytics.data.v1alpha.IGetRecurringAudienceListRequest](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.analytics.data.v1alpha.igetrecurringaudiencelistrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [RecurringAudienceList](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.analytics.data.v1alpha.recurringaudiencelist). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The recurring audience list resource name.
       *  Format:
       *  `properties/{property}/recurringAudienceLists/{recurring_audience_list}`
       */
      // const name = 'abc123'
    
      // Imports the Data library
      const {AlphaAnalyticsDataClient} = require('[@google-analytics/data](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const dataClient = new [AlphaAnalyticsDataClient](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/v1alpha.alphaanalyticsdataclient.html)();
    
      async function callGetRecurringAudienceList() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await dataClient.getRecurringAudienceList(request);
        console.log(response);
      }
    
      callGetRecurringAudienceList();
    
    

### getRecurringAudienceList(request, options, callback)
    
    
    getRecurringAudienceList(request: protos.google.analytics.data.v1alpha.IGetRecurringAudienceListRequest, options: CallOptions, callback: Callback<protos.google.analytics.data.v1alpha.IRecurringAudienceList, protos.google.analytics.data.v1alpha.IGetRecurringAudienceListRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetRecurringAudienceListRequest](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.analytics.data.v1alpha.igetrecurringaudiencelistrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.analytics.data.v1alpha.IRecurringAudienceList](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.analytics.data.v1alpha.irecurringaudiencelist), [protos.google.analytics.data.v1alpha.IGetRecurringAudienceListRequest](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.analytics.data.v1alpha.igetrecurringaudiencelistrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getRecurringAudienceList(request, callback)
    
    
    getRecurringAudienceList(request: protos.google.analytics.data.v1alpha.IGetRecurringAudienceListRequest, callback: Callback<protos.google.analytics.data.v1alpha.IRecurringAudienceList, protos.google.analytics.data.v1alpha.IGetRecurringAudienceListRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetRecurringAudienceListRequest](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.analytics.data.v1alpha.igetrecurringaudiencelistrequest)`   
  
`callback` |  `Callback<[protos.google.analytics.data.v1alpha.IRecurringAudienceList](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.analytics.data.v1alpha.irecurringaudiencelist), [protos.google.analytics.data.v1alpha.IGetRecurringAudienceListRequest](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.analytics.data.v1alpha.igetrecurringaudiencelistrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getReportTask(request, options)
    
    
    getReportTask(request?: protos.google.analytics.data.v1alpha.IGetReportTaskRequest, options?: CallOptions): Promise<[
            protos.google.analytics.data.v1alpha.IReportTask,
            protos.google.analytics.data.v1alpha.IGetReportTaskRequest | undefined,
            {} | undefined
        ]>;

Gets report metadata about a specific report task. After creating a report task, use this method to check its processing state or inspect its report definition.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetReportTaskRequest](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.analytics.data.v1alpha.igetreporttaskrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.analytics.data.v1alpha.IReportTask](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.analytics.data.v1alpha.ireporttask), [protos.google.analytics.data.v1alpha.IGetReportTaskRequest](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.analytics.data.v1alpha.igetreporttaskrequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The report task resource name.
       *  Format: `properties/{property}/reportTasks/{report_task}`
       */
      // const name = 'abc123'
    
      // Imports the Data library
      const {AlphaAnalyticsDataClient} = require('[@google-analytics/data](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const dataClient = new [AlphaAnalyticsDataClient](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/v1alpha.alphaanalyticsdataclient.html)();
    
      async function callGetReportTask() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await dataClient.getReportTask(request);
        console.log(response);
      }
    
      callGetReportTask();
    
    

### getReportTask(request, options, callback)
    
    
    getReportTask(request: protos.google.analytics.data.v1alpha.IGetReportTaskRequest, options: CallOptions, callback: Callback<protos.google.analytics.data.v1alpha.IReportTask, protos.google.analytics.data.v1alpha.IGetReportTaskRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetReportTaskRequest](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.analytics.data.v1alpha.igetreporttaskrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.analytics.data.v1alpha.IReportTask](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.analytics.data.v1alpha.ireporttask), [protos.google.analytics.data.v1alpha.IGetReportTaskRequest](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.analytics.data.v1alpha.igetreporttaskrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getReportTask(request, callback)
    
    
    getReportTask(request: protos.google.analytics.data.v1alpha.IGetReportTaskRequest, callback: Callback<protos.google.analytics.data.v1alpha.IReportTask, protos.google.analytics.data.v1alpha.IGetReportTaskRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetReportTaskRequest](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.analytics.data.v1alpha.igetreporttaskrequest)`   
  
`callback` |  `Callback<[protos.google.analytics.data.v1alpha.IReportTask](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.analytics.data.v1alpha.ireporttask), [protos.google.analytics.data.v1alpha.IGetReportTaskRequest](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.analytics.data.v1alpha.igetreporttaskrequest) | null | undefined, {} | null | undefined>`   
  
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
  
### listAudienceLists(request, options)
    
    
    listAudienceLists(request?: protos.google.analytics.data.v1alpha.IListAudienceListsRequest, options?: CallOptions): Promise<[
            protos.google.analytics.data.v1alpha.IAudienceList[],
            protos.google.analytics.data.v1alpha.IListAudienceListsRequest | null,
            protos.google.analytics.data.v1alpha.IListAudienceListsResponse
        ]>;

Lists all audience lists for a property. This method can be used for you to find and reuse existing audience lists rather than creating unnecessary new audience lists. The same audience can have multiple audience lists that represent the list of users that were in an audience on different days.

See [Creating an Audience List](<https://developers.google.com/analytics/devguides/reporting/data/v1/audience-list-basics>) for an introduction to Audience Lists with examples.

This method is available at beta stability at [audienceExports.list](<https://developers.google.com/analytics/devguides/reporting/data/v1/rest/v1beta/properties.audienceExports/list>). To give your feedback on this API, complete the [Google Analytics Audience Export API Feedback](<https://forms.gle/EeA5u5LW6PEggtCEA>) form.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListAudienceListsRequest](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.analytics.data.v1alpha.ilistaudiencelistsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.analytics.data.v1alpha.IAudienceList](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.analytics.data.v1alpha.iaudiencelist)[], [protos.google.analytics.data.v1alpha.IListAudienceListsRequest](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.analytics.data.v1alpha.ilistaudiencelistsrequest) | null, [protos.google.analytics.data.v1alpha.IListAudienceListsResponse](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.analytics.data.v1alpha.ilistaudiencelistsresponse) ]>` | {Promise} - The promise which resolves to an array. The first element of the array is Array of . The client library will perform auto-pagination by default: it will call the API as many times as needed and will merge results from all the pages into this array. Note that it can affect your quota. We recommend using `listAudienceListsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listAudienceLists(request, options, callback)
    
    
    listAudienceLists(request: protos.google.analytics.data.v1alpha.IListAudienceListsRequest, options: CallOptions, callback: PaginationCallback<protos.google.analytics.data.v1alpha.IListAudienceListsRequest, protos.google.analytics.data.v1alpha.IListAudienceListsResponse | null | undefined, protos.google.analytics.data.v1alpha.IAudienceList>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListAudienceListsRequest](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.analytics.data.v1alpha.ilistaudiencelistsrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `PaginationCallback<[protos.google.analytics.data.v1alpha.IListAudienceListsRequest](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.analytics.data.v1alpha.ilistaudiencelistsrequest), [protos.google.analytics.data.v1alpha.IListAudienceListsResponse](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.analytics.data.v1alpha.ilistaudiencelistsresponse) | null | undefined, [protos.google.analytics.data.v1alpha.IAudienceList](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.analytics.data.v1alpha.iaudiencelist)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listAudienceLists(request, callback)
    
    
    listAudienceLists(request: protos.google.analytics.data.v1alpha.IListAudienceListsRequest, callback: PaginationCallback<protos.google.analytics.data.v1alpha.IListAudienceListsRequest, protos.google.analytics.data.v1alpha.IListAudienceListsResponse | null | undefined, protos.google.analytics.data.v1alpha.IAudienceList>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListAudienceListsRequest](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.analytics.data.v1alpha.ilistaudiencelistsrequest)`   
  
`callback` |  `PaginationCallback<[protos.google.analytics.data.v1alpha.IListAudienceListsRequest](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.analytics.data.v1alpha.ilistaudiencelistsrequest), [protos.google.analytics.data.v1alpha.IListAudienceListsResponse](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.analytics.data.v1alpha.ilistaudiencelistsresponse) | null | undefined, [protos.google.analytics.data.v1alpha.IAudienceList](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.analytics.data.v1alpha.iaudiencelist)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listAudienceListsAsync(request, options)
    
    
    listAudienceListsAsync(request?: protos.google.analytics.data.v1alpha.IListAudienceListsRequest, options?: CallOptions): AsyncIterable<protos.google.analytics.data.v1alpha.IAudienceList>;

Equivalent to `listAudienceLists`, but returns an iterable object.

`for`-`await`-`of` syntax is used with the iterable to get response elements on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListAudienceListsRequest](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.analytics.data.v1alpha.ilistaudiencelistsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.analytics.data.v1alpha.IAudienceList](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.analytics.data.v1alpha.iaudiencelist)>` | {Object} An iterable Object that allows [async iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols). When you iterate the returned iterable, each element will be an object representing . The API will be called under the hood as needed, once per the page, so you can stop the iteration when you don't need more results. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. All audience lists for this property will be listed in the
       *  response. Format: `properties/{property}`
       */
      // const parent = 'abc123'
      /**
       *  Optional. The maximum number of audience lists to return. The service may
       *  return fewer than this value. If unspecified, at most 200 audience lists
       *  will be returned. The maximum value is 1000 (higher values will be coerced
       *  to the maximum).
       */
      // const pageSize = 1234
      /**
       *  Optional. A page token, received from a previous `ListAudienceLists` call.
       *  Provide this to retrieve the subsequent page.
       *  When paginating, all other parameters provided to `ListAudienceLists` must
       *  match the call that provided the page token.
       */
      // const pageToken = 'abc123'
    
      // Imports the Data library
      const {AlphaAnalyticsDataClient} = require('[@google-analytics/data](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const dataClient = new [AlphaAnalyticsDataClient](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/v1alpha.alphaanalyticsdataclient.html)();
    
      async function callListAudienceLists() {
        // Construct request
        const request = {
          parent,
        };
    
        // Run request
        const iterable = dataClient.[listAudienceListsAsync](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/v1alpha.alphaanalyticsdataclient.html)(request);
        for await (const response of iterable) {
            console.log(response);
        }
      }
    
      callListAudienceLists();
    
    

### listAudienceListsStream(request, options)
    
    
    listAudienceListsStream(request?: protos.google.analytics.data.v1alpha.IListAudienceListsRequest, options?: CallOptions): Transform;

Equivalent to `listAudienceLists`, but returns a NodeJS Stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListAudienceListsRequest](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.analytics.data.v1alpha.ilistaudiencelistsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Transform` | {Stream} An object stream which emits an object representing on 'data' event. The client library will perform auto-pagination by default: it will call the API as many times as needed. Note that it can affect your quota. We recommend using `listAudienceListsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listOperationsAsync(request, options)
    
    
    listOperationsAsync(request: protos.google.longrunning.ListOperationsRequest, options?: gax.CallOptions): AsyncIterable<protos.google.longrunning.IOperation>;

Lists operations that match the specified filter in the request. If the server doesn't support this method, it returns `UNIMPLEMENTED`. Returns an iterable object.

For-await-of syntax is used with the iterable to recursively get response element on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ListOperationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.longrunning.listoperationsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Optional parameters. You can override the default settings for this call, e.g, timeout, retries, paginations, etc. See [gax.CallOptions](https://googleapis.github.io/gax-nodejs/global.html#CallOptions) for the details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.longrunning.ioperation)>` | {Object} An iterable Object that conforms to [iteration protocols](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols).  
**Example**
    
    
    const client = longrunning.operationsClient();
    for await (const response of client.listOperationsAsync(request));
    // doThingsWith(response)
    

### listRecurringAudienceLists(request, options)
    
    
    listRecurringAudienceLists(request?: protos.google.analytics.data.v1alpha.IListRecurringAudienceListsRequest, options?: CallOptions): Promise<[
            protos.google.analytics.data.v1alpha.IRecurringAudienceList[],
            protos.google.analytics.data.v1alpha.IListRecurringAudienceListsRequest | null,
            protos.google.analytics.data.v1alpha.IListRecurringAudienceListsResponse
        ]>;

Lists all recurring audience lists for a property. This method can be used for you to find and reuse existing recurring audience lists rather than creating unnecessary new recurring audience lists. The same audience can have multiple recurring audience lists that represent different dimension combinations; for example, just the dimension `deviceId` or both the dimensions `deviceId` and `userId`.

This method is introduced at alpha stability with the intention of gathering feedback on syntax and capabilities before entering beta. To give your feedback on this API, complete the [Google Analytics Audience Export API Feedback](<https://forms.gle/EeA5u5LW6PEggtCEA>) form.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListRecurringAudienceListsRequest](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.analytics.data.v1alpha.ilistrecurringaudiencelistsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.analytics.data.v1alpha.IRecurringAudienceList](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.analytics.data.v1alpha.irecurringaudiencelist)[], [protos.google.analytics.data.v1alpha.IListRecurringAudienceListsRequest](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.analytics.data.v1alpha.ilistrecurringaudiencelistsrequest) | null, [protos.google.analytics.data.v1alpha.IListRecurringAudienceListsResponse](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.analytics.data.v1alpha.ilistrecurringaudiencelistsresponse) ]>` | {Promise} - The promise which resolves to an array. The first element of the array is Array of [RecurringAudienceList](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.analytics.data.v1alpha.recurringaudiencelist). The client library will perform auto-pagination by default: it will call the API as many times as needed and will merge results from all the pages into this array. Note that it can affect your quota. We recommend using `listRecurringAudienceListsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listRecurringAudienceLists(request, options, callback)
    
    
    listRecurringAudienceLists(request: protos.google.analytics.data.v1alpha.IListRecurringAudienceListsRequest, options: CallOptions, callback: PaginationCallback<protos.google.analytics.data.v1alpha.IListRecurringAudienceListsRequest, protos.google.analytics.data.v1alpha.IListRecurringAudienceListsResponse | null | undefined, protos.google.analytics.data.v1alpha.IRecurringAudienceList>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListRecurringAudienceListsRequest](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.analytics.data.v1alpha.ilistrecurringaudiencelistsrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `PaginationCallback<[protos.google.analytics.data.v1alpha.IListRecurringAudienceListsRequest](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.analytics.data.v1alpha.ilistrecurringaudiencelistsrequest), [protos.google.analytics.data.v1alpha.IListRecurringAudienceListsResponse](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.analytics.data.v1alpha.ilistrecurringaudiencelistsresponse) | null | undefined, [protos.google.analytics.data.v1alpha.IRecurringAudienceList](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.analytics.data.v1alpha.irecurringaudiencelist)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listRecurringAudienceLists(request, callback)
    
    
    listRecurringAudienceLists(request: protos.google.analytics.data.v1alpha.IListRecurringAudienceListsRequest, callback: PaginationCallback<protos.google.analytics.data.v1alpha.IListRecurringAudienceListsRequest, protos.google.analytics.data.v1alpha.IListRecurringAudienceListsResponse | null | undefined, protos.google.analytics.data.v1alpha.IRecurringAudienceList>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListRecurringAudienceListsRequest](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.analytics.data.v1alpha.ilistrecurringaudiencelistsrequest)`   
  
`callback` |  `PaginationCallback<[protos.google.analytics.data.v1alpha.IListRecurringAudienceListsRequest](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.analytics.data.v1alpha.ilistrecurringaudiencelistsrequest), [protos.google.analytics.data.v1alpha.IListRecurringAudienceListsResponse](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.analytics.data.v1alpha.ilistrecurringaudiencelistsresponse) | null | undefined, [protos.google.analytics.data.v1alpha.IRecurringAudienceList](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.analytics.data.v1alpha.irecurringaudiencelist)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listRecurringAudienceListsAsync(request, options)
    
    
    listRecurringAudienceListsAsync(request?: protos.google.analytics.data.v1alpha.IListRecurringAudienceListsRequest, options?: CallOptions): AsyncIterable<protos.google.analytics.data.v1alpha.IRecurringAudienceList>;

Equivalent to `listRecurringAudienceLists`, but returns an iterable object.

`for`-`await`-`of` syntax is used with the iterable to get response elements on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListRecurringAudienceListsRequest](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.analytics.data.v1alpha.ilistrecurringaudiencelistsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.analytics.data.v1alpha.IRecurringAudienceList](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.analytics.data.v1alpha.irecurringaudiencelist)>` | {Object} An iterable Object that allows [async iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols). When you iterate the returned iterable, each element will be an object representing [RecurringAudienceList](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.analytics.data.v1alpha.recurringaudiencelist). The API will be called under the hood as needed, once per the page, so you can stop the iteration when you don't need more results. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. All recurring audience lists for this property will be listed in
       *  the response. Format: `properties/{property}`
       */
      // const parent = 'abc123'
      /**
       *  Optional. The maximum number of recurring audience lists to return. The
       *  service may return fewer than this value. If unspecified, at most 200
       *  recurring audience lists will be returned. The maximum value is 1000
       *  (higher values will be coerced to the maximum).
       */
      // const pageSize = 1234
      /**
       *  Optional. A page token, received from a previous
       *  `ListRecurringAudienceLists` call. Provide this to retrieve the subsequent
       *  page.
       *  When paginating, all other parameters provided to
       *  `ListRecurringAudienceLists` must match the call that provided the page
       *  token.
       */
      // const pageToken = 'abc123'
    
      // Imports the Data library
      const {AlphaAnalyticsDataClient} = require('[@google-analytics/data](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const dataClient = new [AlphaAnalyticsDataClient](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/v1alpha.alphaanalyticsdataclient.html)();
    
      async function callListRecurringAudienceLists() {
        // Construct request
        const request = {
          parent,
        };
    
        // Run request
        const iterable = dataClient.[listRecurringAudienceListsAsync](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/v1alpha.alphaanalyticsdataclient.html)(request);
        for await (const response of iterable) {
            console.log(response);
        }
      }
    
      callListRecurringAudienceLists();
    
    

### listRecurringAudienceListsStream(request, options)
    
    
    listRecurringAudienceListsStream(request?: protos.google.analytics.data.v1alpha.IListRecurringAudienceListsRequest, options?: CallOptions): Transform;

Equivalent to `listRecurringAudienceLists`, but returns a NodeJS Stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListRecurringAudienceListsRequest](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.analytics.data.v1alpha.ilistrecurringaudiencelistsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Transform` | {Stream} An object stream which emits an object representing [RecurringAudienceList](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.analytics.data.v1alpha.recurringaudiencelist) on 'data' event. The client library will perform auto-pagination by default: it will call the API as many times as needed. Note that it can affect your quota. We recommend using `listRecurringAudienceListsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listReportTasks(request, options)
    
    
    listReportTasks(request?: protos.google.analytics.data.v1alpha.IListReportTasksRequest, options?: CallOptions): Promise<[
            protos.google.analytics.data.v1alpha.IReportTask[],
            protos.google.analytics.data.v1alpha.IListReportTasksRequest | null,
            protos.google.analytics.data.v1alpha.IListReportTasksResponse
        ]>;

Lists all report tasks for a property.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListReportTasksRequest](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.analytics.data.v1alpha.ilistreporttasksrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.analytics.data.v1alpha.IReportTask](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.analytics.data.v1alpha.ireporttask)[], [protos.google.analytics.data.v1alpha.IListReportTasksRequest](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.analytics.data.v1alpha.ilistreporttasksrequest) | null, [protos.google.analytics.data.v1alpha.IListReportTasksResponse](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.analytics.data.v1alpha.ilistreporttasksresponse) ]>` | {Promise} - The promise which resolves to an array. The first element of the array is Array of . The client library will perform auto-pagination by default: it will call the API as many times as needed and will merge results from all the pages into this array. Note that it can affect your quota. We recommend using `listReportTasksAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listReportTasks(request, options, callback)
    
    
    listReportTasks(request: protos.google.analytics.data.v1alpha.IListReportTasksRequest, options: CallOptions, callback: PaginationCallback<protos.google.analytics.data.v1alpha.IListReportTasksRequest, protos.google.analytics.data.v1alpha.IListReportTasksResponse | null | undefined, protos.google.analytics.data.v1alpha.IReportTask>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListReportTasksRequest](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.analytics.data.v1alpha.ilistreporttasksrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `PaginationCallback<[protos.google.analytics.data.v1alpha.IListReportTasksRequest](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.analytics.data.v1alpha.ilistreporttasksrequest), [protos.google.analytics.data.v1alpha.IListReportTasksResponse](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.analytics.data.v1alpha.ilistreporttasksresponse) | null | undefined, [protos.google.analytics.data.v1alpha.IReportTask](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.analytics.data.v1alpha.ireporttask)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listReportTasks(request, callback)
    
    
    listReportTasks(request: protos.google.analytics.data.v1alpha.IListReportTasksRequest, callback: PaginationCallback<protos.google.analytics.data.v1alpha.IListReportTasksRequest, protos.google.analytics.data.v1alpha.IListReportTasksResponse | null | undefined, protos.google.analytics.data.v1alpha.IReportTask>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListReportTasksRequest](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.analytics.data.v1alpha.ilistreporttasksrequest)`   
  
`callback` |  `PaginationCallback<[protos.google.analytics.data.v1alpha.IListReportTasksRequest](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.analytics.data.v1alpha.ilistreporttasksrequest), [protos.google.analytics.data.v1alpha.IListReportTasksResponse](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.analytics.data.v1alpha.ilistreporttasksresponse) | null | undefined, [protos.google.analytics.data.v1alpha.IReportTask](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.analytics.data.v1alpha.ireporttask)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listReportTasksAsync(request, options)
    
    
    listReportTasksAsync(request?: protos.google.analytics.data.v1alpha.IListReportTasksRequest, options?: CallOptions): AsyncIterable<protos.google.analytics.data.v1alpha.IReportTask>;

Equivalent to `listReportTasks`, but returns an iterable object.

`for`-`await`-`of` syntax is used with the iterable to get response elements on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListReportTasksRequest](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.analytics.data.v1alpha.ilistreporttasksrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.analytics.data.v1alpha.IReportTask](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.analytics.data.v1alpha.ireporttask)>` | {Object} An iterable Object that allows [async iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols). When you iterate the returned iterable, each element will be an object representing . The API will be called under the hood as needed, once per the page, so you can stop the iteration when you don't need more results. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. All report tasks for this property will be listed in the
       *  response. Format: `properties/{property}`
       */
      // const parent = 'abc123'
      /**
       *  Optional. The maximum number of report tasks to return.
       */
      // const pageSize = 1234
      /**
       *  Optional. A page token, received from a previous `ListReportTasks` call.
       *  Provide this to retrieve the subsequent page.
       */
      // const pageToken = 'abc123'
    
      // Imports the Data library
      const {AlphaAnalyticsDataClient} = require('[@google-analytics/data](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const dataClient = new [AlphaAnalyticsDataClient](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/v1alpha.alphaanalyticsdataclient.html)();
    
      async function callListReportTasks() {
        // Construct request
        const request = {
          parent,
        };
    
        // Run request
        const iterable = dataClient.[listReportTasksAsync](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/v1alpha.alphaanalyticsdataclient.html)(request);
        for await (const response of iterable) {
            console.log(response);
        }
      }
    
      callListReportTasks();
    
    

### listReportTasksStream(request, options)
    
    
    listReportTasksStream(request?: protos.google.analytics.data.v1alpha.IListReportTasksRequest, options?: CallOptions): Transform;

Equivalent to `listReportTasks`, but returns a NodeJS Stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListReportTasksRequest](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.analytics.data.v1alpha.ilistreporttasksrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Transform` | {Stream} An object stream which emits an object representing on 'data' event. The client library will perform auto-pagination by default: it will call the API as many times as needed. Note that it can affect your quota. We recommend using `listReportTasksAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### matchAudienceListFromAudienceListName(audienceListName)
    
    
    matchAudienceListFromAudienceListName(audienceListName: string): string | number;

Parse the audience_list from AudienceList resource.

**Parameter**  
---  
**Name** | **Description**  
`audienceListName` |  `string`   
A fully-qualified path representing AudienceList resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the audience_list.  
  
### matchPropertyFromAudienceListName(audienceListName)
    
    
    matchPropertyFromAudienceListName(audienceListName: string): string | number;

Parse the property from AudienceList resource.

**Parameter**  
---  
**Name** | **Description**  
`audienceListName` |  `string`   
A fully-qualified path representing AudienceList resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the property.  
  
### matchPropertyFromMetadataName(metadataName)
    
    
    matchPropertyFromMetadataName(metadataName: string): string | number;

Parse the property from Metadata resource.

**Parameter**  
---  
**Name** | **Description**  
`metadataName` |  `string`   
A fully-qualified path representing Metadata resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the property.  
  
### matchPropertyFromPropertyName(propertyName)
    
    
    matchPropertyFromPropertyName(propertyName: string): string | number;

Parse the property from Property resource.

**Parameter**  
---  
**Name** | **Description**  
`propertyName` |  `string`   
A fully-qualified path representing Property resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the property.  
  
### matchPropertyFromPropertyQuotasSnapshotName(propertyQuotasSnapshotName)
    
    
    matchPropertyFromPropertyQuotasSnapshotName(propertyQuotasSnapshotName: string): string | number;

Parse the property from PropertyQuotasSnapshot resource.

**Parameter**  
---  
**Name** | **Description**  
`propertyQuotasSnapshotName` |  `string`   
A fully-qualified path representing PropertyQuotasSnapshot resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the property.  
  
### matchPropertyFromRecurringAudienceListName(recurringAudienceListName)
    
    
    matchPropertyFromRecurringAudienceListName(recurringAudienceListName: string): string | number;

Parse the property from RecurringAudienceList resource.

**Parameter**  
---  
**Name** | **Description**  
`recurringAudienceListName` |  `string`   
A fully-qualified path representing RecurringAudienceList resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the property.  
  
### matchPropertyFromReportTaskName(reportTaskName)
    
    
    matchPropertyFromReportTaskName(reportTaskName: string): string | number;

Parse the property from ReportTask resource.

**Parameter**  
---  
**Name** | **Description**  
`reportTaskName` |  `string`   
A fully-qualified path representing ReportTask resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the property.  
  
### matchRecurringAudienceListFromRecurringAudienceListName(recurringAudienceListName)
    
    
    matchRecurringAudienceListFromRecurringAudienceListName(recurringAudienceListName: string): string | number;

Parse the recurring_audience_list from RecurringAudienceList resource.

**Parameter**  
---  
**Name** | **Description**  
`recurringAudienceListName` |  `string`   
A fully-qualified path representing RecurringAudienceList resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the recurring_audience_list.  
  
### matchReportTaskFromReportTaskName(reportTaskName)
    
    
    matchReportTaskFromReportTaskName(reportTaskName: string): string | number;

Parse the report_task from ReportTask resource.

**Parameter**  
---  
**Name** | **Description**  
`reportTaskName` |  `string`   
A fully-qualified path representing ReportTask resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the report_task.  
  
### metadataPath(property)
    
    
    metadataPath(property: string): string;

Return a fully-qualified metadata resource name string.

**Parameter**  
---  
**Name** | **Description**  
`property` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### propertyPath(property)
    
    
    propertyPath(property: string): string;

Return a fully-qualified property resource name string.

**Parameter**  
---  
**Name** | **Description**  
`property` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### propertyQuotasSnapshotPath(property)
    
    
    propertyQuotasSnapshotPath(property: string): string;

Return a fully-qualified propertyQuotasSnapshot resource name string.

**Parameter**  
---  
**Name** | **Description**  
`property` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### queryAudienceList(request, options)
    
    
    queryAudienceList(request?: protos.google.analytics.data.v1alpha.IQueryAudienceListRequest, options?: CallOptions): Promise<[
            protos.google.analytics.data.v1alpha.IQueryAudienceListResponse,
            (protos.google.analytics.data.v1alpha.IQueryAudienceListRequest | undefined),
            {} | undefined
        ]>;

Retrieves an audience list of users. After creating an audience, the users are not immediately available for listing. First, a request to `CreateAudienceList` is necessary to create an audience list of users, and then second, this method is used to retrieve the users in the audience list.

See [Creating an Audience List](<https://developers.google.com/analytics/devguides/reporting/data/v1/audience-list-basics>) for an introduction to Audience Lists with examples.

Audiences in Google Analytics 4 allow you to segment your users in the ways that are important to your business. To learn more, see <https://support.google.com/analytics/answer/9267572>.

This method is available at beta stability at [audienceExports.query](<https://developers.google.com/analytics/devguides/reporting/data/v1/rest/v1beta/properties.audienceExports/query>). To give your feedback on this API, complete the [Google Analytics Audience Export API Feedback](<https://forms.gle/EeA5u5LW6PEggtCEA>) form.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IQueryAudienceListRequest](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.analytics.data.v1alpha.iqueryaudiencelistrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.analytics.data.v1alpha.IQueryAudienceListResponse](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.analytics.data.v1alpha.iqueryaudiencelistresponse), ([protos.google.analytics.data.v1alpha.IQueryAudienceListRequest](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.analytics.data.v1alpha.iqueryaudiencelistrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [QueryAudienceListResponse](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.analytics.data.v1alpha.queryaudiencelistresponse). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The name of the audience list to retrieve users from.
       *  Format: `properties/{property}/audienceLists/{audience_list}`
       */
      // const name = 'abc123'
      /**
       *  Optional. The row count of the start row. The first row is counted as row
       *  0.
       *  When paging, the first request does not specify offset; or equivalently,
       *  sets offset to 0; the first request returns the first `limit` of rows. The
       *  second request sets offset to the `limit` of the first request; the second
       *  request returns the second `limit` of rows.
       *  To learn more about this pagination parameter, see
       *  Pagination (https://developers.google.com/analytics/devguides/reporting/data/v1/basics#pagination).
       */
      // const offset = 1234
      /**
       *  Optional. The number of rows to return. If unspecified, 10,000 rows are
       *  returned. The API returns a maximum of 250,000 rows per request, no matter
       *  how many you ask for. `limit` must be positive.
       *  The API can also return fewer rows than the requested `limit`, if there
       *  aren't as many dimension values as the `limit`.
       *  To learn more about this pagination parameter, see
       *  Pagination (https://developers.google.com/analytics/devguides/reporting/data/v1/basics#pagination).
       */
      // const limit = 1234
    
      // Imports the Data library
      const {AlphaAnalyticsDataClient} = require('[@google-analytics/data](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const dataClient = new [AlphaAnalyticsDataClient](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/v1alpha.alphaanalyticsdataclient.html)();
    
      async function callQueryAudienceList() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await dataClient.queryAudienceList(request);
        console.log(response);
      }
    
      callQueryAudienceList();
    
    

### queryAudienceList(request, options, callback)
    
    
    queryAudienceList(request: protos.google.analytics.data.v1alpha.IQueryAudienceListRequest, options: CallOptions, callback: Callback<protos.google.analytics.data.v1alpha.IQueryAudienceListResponse, protos.google.analytics.data.v1alpha.IQueryAudienceListRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IQueryAudienceListRequest](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.analytics.data.v1alpha.iqueryaudiencelistrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.analytics.data.v1alpha.IQueryAudienceListResponse](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.analytics.data.v1alpha.iqueryaudiencelistresponse), [protos.google.analytics.data.v1alpha.IQueryAudienceListRequest](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.analytics.data.v1alpha.iqueryaudiencelistrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### queryAudienceList(request, callback)
    
    
    queryAudienceList(request: protos.google.analytics.data.v1alpha.IQueryAudienceListRequest, callback: Callback<protos.google.analytics.data.v1alpha.IQueryAudienceListResponse, protos.google.analytics.data.v1alpha.IQueryAudienceListRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IQueryAudienceListRequest](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.analytics.data.v1alpha.iqueryaudiencelistrequest)`   
  
`callback` |  `Callback<[protos.google.analytics.data.v1alpha.IQueryAudienceListResponse](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.analytics.data.v1alpha.iqueryaudiencelistresponse), [protos.google.analytics.data.v1alpha.IQueryAudienceListRequest](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.analytics.data.v1alpha.iqueryaudiencelistrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### queryReportTask(request, options)
    
    
    queryReportTask(request?: protos.google.analytics.data.v1alpha.IQueryReportTaskRequest, options?: CallOptions): Promise<[
            protos.google.analytics.data.v1alpha.IQueryReportTaskResponse,
            protos.google.analytics.data.v1alpha.IQueryReportTaskRequest | undefined,
            {} | undefined
        ]>;

Retrieves a report task's content. After requesting the `CreateReportTask`, you are able to retrieve the report content once the report is ACTIVE. This method will return an error if the report task's state is not `ACTIVE`. A query response will return the tabular row & column values of the report.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IQueryReportTaskRequest](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.analytics.data.v1alpha.iqueryreporttaskrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.analytics.data.v1alpha.IQueryReportTaskResponse](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.analytics.data.v1alpha.iqueryreporttaskresponse), [protos.google.analytics.data.v1alpha.IQueryReportTaskRequest](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.analytics.data.v1alpha.iqueryreporttaskrequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [QueryReportTaskResponse](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.analytics.data.v1alpha.queryreporttaskresponse). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The report source name.
       *  Format: `properties/{property}/reportTasks/{report}`
       */
      // const name = 'abc123'
      /**
       *  Optional. The row count of the start row in the report. The first row is
       *  counted as row 0.
       *  When paging, the first request does not specify offset; or equivalently,
       *  sets offset to 0; the first request returns the first `limit` of rows. The
       *  second request sets offset to the `limit` of the first request; the second
       *  request returns the second `limit` of rows.
       *  To learn more about this pagination parameter, see
       *  Pagination (https://developers.google.com/analytics/devguides/reporting/data/v1/basics#pagination).
       */
      // const offset = 1234
      /**
       *  Optional. The number of rows to return from the report. If unspecified,
       *  10,000 rows are returned. The API returns a maximum of 250,000 rows per
       *  request, no matter how many you ask for. `limit` must be positive.
       *  The API can also return fewer rows than the requested `limit`, if there
       *  aren't as many dimension values as the `limit`. The number of rows
       *  available to a QueryReportTaskRequest is further limited by the limit of
       *  the associated ReportTask. A query can retrieve at most ReportTask.limit
       *  rows. For example, if the ReportTask has a limit of 1,000, then a
       *  QueryReportTask request with offset=900 and limit=500 will return at most
       *  100 rows.
       *  To learn more about this pagination parameter, see
       *  Pagination (https://developers.google.com/analytics/devguides/reporting/data/v1/basics#pagination).
       */
      // const limit = 1234
    
      // Imports the Data library
      const {AlphaAnalyticsDataClient} = require('[@google-analytics/data](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const dataClient = new [AlphaAnalyticsDataClient](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/v1alpha.alphaanalyticsdataclient.html)();
    
      async function callQueryReportTask() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await dataClient.queryReportTask(request);
        console.log(response);
      }
    
      callQueryReportTask();
    
    

### queryReportTask(request, options, callback)
    
    
    queryReportTask(request: protos.google.analytics.data.v1alpha.IQueryReportTaskRequest, options: CallOptions, callback: Callback<protos.google.analytics.data.v1alpha.IQueryReportTaskResponse, protos.google.analytics.data.v1alpha.IQueryReportTaskRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IQueryReportTaskRequest](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.analytics.data.v1alpha.iqueryreporttaskrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.analytics.data.v1alpha.IQueryReportTaskResponse](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.analytics.data.v1alpha.iqueryreporttaskresponse), [protos.google.analytics.data.v1alpha.IQueryReportTaskRequest](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.analytics.data.v1alpha.iqueryreporttaskrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### queryReportTask(request, callback)
    
    
    queryReportTask(request: protos.google.analytics.data.v1alpha.IQueryReportTaskRequest, callback: Callback<protos.google.analytics.data.v1alpha.IQueryReportTaskResponse, protos.google.analytics.data.v1alpha.IQueryReportTaskRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IQueryReportTaskRequest](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.analytics.data.v1alpha.iqueryreporttaskrequest)`   
  
`callback` |  `Callback<[protos.google.analytics.data.v1alpha.IQueryReportTaskResponse](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.analytics.data.v1alpha.iqueryreporttaskresponse), [protos.google.analytics.data.v1alpha.IQueryReportTaskRequest](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.analytics.data.v1alpha.iqueryreporttaskrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### recurringAudienceListPath(property, recurringAudienceList)
    
    
    recurringAudienceListPath(property: string, recurringAudienceList: string): string;

Return a fully-qualified recurringAudienceList resource name string.

**Parameters**  
---  
**Name** | **Description**  
`property` |  `string`   
  
`recurringAudienceList` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### reportTaskPath(property, reportTask)
    
    
    reportTaskPath(property: string, reportTask: string): string;

Return a fully-qualified reportTask resource name string.

**Parameters**  
---  
**Name** | **Description**  
`property` |  `string`   
  
`reportTask` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### runFunnelReport(request, options)
    
    
    runFunnelReport(request?: protos.google.analytics.data.v1alpha.IRunFunnelReportRequest, options?: CallOptions): Promise<[
            protos.google.analytics.data.v1alpha.IRunFunnelReportResponse,
            protos.google.analytics.data.v1alpha.IRunFunnelReportRequest | undefined,
            {} | undefined
        ]>;

Returns a customized funnel report of your Google Analytics event data. The data returned from the API is as a table with columns for the requested dimensions and metrics.

Funnel exploration lets you visualize the steps your users take to complete a task and quickly see how well they are succeeding or failing at each step. For example, how do prospects become shoppers and then become buyers? How do one time buyers become repeat buyers? With this information, you can improve inefficient or abandoned customer journeys. To learn more, see [GA4 Funnel Explorations](<https://support.google.com/analytics/answer/9327974>).

This method is introduced at alpha stability with the intention of gathering feedback on syntax and capabilities before entering beta. To give your feedback on this API, complete the [Google Analytics Data API Funnel Reporting Feedback](https://docs.google.com/forms/d/e/1FAIpQLSdwOlQDJAUoBiIgUZZ3S_Lwi8gr7Bb0k1jhvc-DEg7Rol3UjA/viewform).

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IRunFunnelReportRequest](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.analytics.data.v1alpha.irunfunnelreportrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.analytics.data.v1alpha.IRunFunnelReportResponse](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.analytics.data.v1alpha.irunfunnelreportresponse), [protos.google.analytics.data.v1alpha.IRunFunnelReportRequest](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.analytics.data.v1alpha.irunfunnelreportrequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [RunFunnelReportResponse](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.analytics.data.v1alpha.runfunnelreportresponse). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Optional. A Google Analytics property identifier whose events are tracked.
       *  Specified in the URL path and not the body. To learn more, see where to
       *  find your Property
       *  ID (https://developers.google.com/analytics/devguides/reporting/data/v1/property-id).
       *  Within a batch request, this property should either be unspecified or
       *  consistent with the batch-level property.
       *  Example: properties/1234
       */
      // const property = 'abc123'
      /**
       *  Optional. Date ranges of data to read. If multiple date ranges are
       *  requested, each response row will contain a zero based date range index. If
       *  two date ranges overlap, the event data for the overlapping days is
       *  included in the response rows for both date ranges.
       */
      // const dateRanges = [1,2,3,4]
      /**
       *  Optional. The configuration of this request's funnel. This funnel
       *  configuration is required.
       */
      // const funnel = {}
      /**
       *  Optional. If specified, this breakdown adds a dimension to the funnel table
       *  sub report response. This breakdown dimension expands each funnel step to
       *  the unique values of the breakdown dimension. For example, a breakdown by
       *  the `deviceCategory` dimension will create rows for `mobile`, `tablet`,
       *  `desktop`, and the total.
       */
      // const funnelBreakdown = {}
      /**
       *  Optional. If specified, next action adds a dimension to the funnel
       *  visualization sub report response. This next action dimension expands each
       *  funnel step to the unique values of the next action. For example a next
       *  action of the `eventName` dimension will create rows for several events
       *  (for example `session_start` & `click`) and the total.
       *  Next action only supports `eventName` and most Page / Screen dimensions
       *  like `pageTitle` and `pagePath`.
       */
      // const funnelNextAction = {}
      /**
       *  Optional. The funnel visualization type controls the dimensions present in
       *  the funnel visualization sub report response. If not specified,
       *  `STANDARD_FUNNEL` is used.
       */
      // const funnelVisualizationType = {}
      /**
       *  Optional. The configurations of segments. Segments are subsets of a
       *  property's data. In a funnel report with segments, the funnel is evaluated
       *  in each segment.
       *  Each segment specified in this request
       *  produces a separate row in the response; in the response, each segment
       *  identified by its name.
       *  The segments parameter is optional. Requests are limited to 4 segments.
       */
      // const segments = [1,2,3,4]
      /**
       *  Optional. The number of rows to return. If unspecified, 10,000 rows are
       *  returned. The API returns a maximum of 250,000 rows per request, no matter
       *  how many you ask for. `limit` must be positive.
       *  The API can also return fewer rows than the requested `limit`, if there
       *  aren't as many dimension values as the `limit`.
       */
      // const limit = 1234
      /**
       *  Optional. Dimension filters allow you to ask for only specific dimension
       *  values in the report. To learn more, see Creating a Report: Dimension
       *  Filters (https://developers.google.com/analytics/devguides/reporting/data/v1/basics#dimension_filters)
       *  for examples. Metrics cannot be used in this filter.
       */
      // const dimensionFilter = {}
      /**
       *  Optional. Toggles whether to return the current state of this Analytics
       *  Property's quota. Quota is returned in PropertyQuota (#PropertyQuota).
       */
      // const returnPropertyQuota = true
    
      // Imports the Data library
      const {AlphaAnalyticsDataClient} = require('[@google-analytics/data](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const dataClient = new [AlphaAnalyticsDataClient](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/v1alpha.alphaanalyticsdataclient.html)();
    
      async function callRunFunnelReport() {
        // Construct request
        const request = {
        };
    
        // Run request
        const response = await dataClient.runFunnelReport(request);
        console.log(response);
      }
    
      callRunFunnelReport();
    
    

### runFunnelReport(request, options, callback)
    
    
    runFunnelReport(request: protos.google.analytics.data.v1alpha.IRunFunnelReportRequest, options: CallOptions, callback: Callback<protos.google.analytics.data.v1alpha.IRunFunnelReportResponse, protos.google.analytics.data.v1alpha.IRunFunnelReportRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IRunFunnelReportRequest](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.analytics.data.v1alpha.irunfunnelreportrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.analytics.data.v1alpha.IRunFunnelReportResponse](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.analytics.data.v1alpha.irunfunnelreportresponse), [protos.google.analytics.data.v1alpha.IRunFunnelReportRequest](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.analytics.data.v1alpha.irunfunnelreportrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### runFunnelReport(request, callback)
    
    
    runFunnelReport(request: protos.google.analytics.data.v1alpha.IRunFunnelReportRequest, callback: Callback<protos.google.analytics.data.v1alpha.IRunFunnelReportResponse, protos.google.analytics.data.v1alpha.IRunFunnelReportRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IRunFunnelReportRequest](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.analytics.data.v1alpha.irunfunnelreportrequest)`   
  
`callback` |  `Callback<[protos.google.analytics.data.v1alpha.IRunFunnelReportResponse](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.analytics.data.v1alpha.irunfunnelreportresponse), [protos.google.analytics.data.v1alpha.IRunFunnelReportRequest](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.analytics.data.v1alpha.irunfunnelreportrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### runReport(request, options)
    
    
    runReport(request?: protos.google.analytics.data.v1alpha.IRunReportRequest, options?: CallOptions): Promise<[
            protos.google.analytics.data.v1alpha.IRunReportResponse,
            protos.google.analytics.data.v1alpha.IRunReportRequest | undefined,
            {} | undefined
        ]>;

Returns a customized report of your Google Analytics event data. Reports contain statistics derived from data collected by the Google Analytics tracking code. The data returned from the API is as a table with columns for the requested dimensions and metrics. Metrics are individual measurements of user activity on your property, such as active users or event count. Dimensions break down metrics across some common criteria, such as country or event name.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IRunReportRequest](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.analytics.data.v1alpha.irunreportrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.analytics.data.v1alpha.IRunReportResponse](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.analytics.data.v1alpha.irunreportresponse), [protos.google.analytics.data.v1alpha.IRunReportRequest](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.analytics.data.v1alpha.irunreportrequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [RunReportResponse](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.analytics.data.v1alpha.runreportresponse). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. A Google Analytics property identifier whose events are tracked.
       *  Specified in the URL path and not the body. To learn more, see where to
       *  find your Property
       *  ID (https://developers.google.com/analytics/devguides/reporting/data/v1/property-id).
       *  Within a batch request, this property should either be unspecified or
       *  consistent with the batch-level property.
       *  Example: properties/1234
       */
      // const property = 'abc123'
      /**
       *  Optional. The dimensions requested and displayed.
       */
      // const dimensions = [1,2,3,4]
      /**
       *  Optional. The metrics requested and displayed.
       */
      // const metrics = [1,2,3,4]
      /**
       *  Optional. Date ranges of data to read. If multiple date ranges are
       *  requested, each response row will contain a zero based date range index. If
       *  two date ranges overlap, the event data for the overlapping days is
       *  included in the response rows for both date ranges. In a cohort request,
       *  this `dateRanges` must be unspecified.
       */
      // const dateRanges = [1,2,3,4]
      /**
       *  Optional. Dimension filters let you ask for only specific dimension values
       *  in the report. To learn more, see Fundamentals of Dimension
       *  Filters (https://developers.google.com/analytics/devguides/reporting/data/v1/basics#dimension_filters)
       *  for examples. Metrics cannot be used in this filter.
       */
      // const dimensionFilter = {}
      /**
       *  Optional. The filter clause of metrics. Applied after aggregating the
       *  report's rows, similar to SQL having-clause. Dimensions cannot be used in
       *  this filter.
       */
      // const metricFilter = {}
      /**
       *  Optional. The row count of the start row. The first row is counted as row
       *  0.
       *  When paging, the first request does not specify offset; or equivalently,
       *  sets offset to 0; the first request returns the first `limit` of rows. The
       *  second request sets offset to the `limit` of the first request; the second
       *  request returns the second `limit` of rows.
       *  To learn more about this pagination parameter, see
       *  Pagination (https://developers.google.com/analytics/devguides/reporting/data/v1/basics#pagination).
       */
      // const offset = 1234
      /**
       *  Optional. The maximum number of rows to return. If unspecified, 10,000 rows
       *  are returned. The API returns a maximum of 250,000 rows per request, no
       *  matter how many you ask for. `limit` must be positive.
       *  The API can also return fewer rows than the requested `limit`, if there
       *  aren't as many dimension values as the `limit`. For instance, there are
       *  fewer than 300 possible values for the dimension `country`, so when
       *  reporting on only `country`, you can't get more than 300 rows, even if you
       *  set `limit` to a higher value.
       *  To learn more about this pagination parameter, see
       *  Pagination (https://developers.google.com/analytics/devguides/reporting/data/v1/basics#pagination).
       */
      // const limit = 1234
      /**
       *  Optional. Aggregation of metrics. Aggregated metric values will be shown in
       *  rows where the dimension_values are set to "RESERVED_(MetricAggregation)".
       *  Aggregates including both comparisons and multiple date ranges will
       *  be aggregated based on the date ranges.
       */
      // const metricAggregations = [1,2,3,4]
      /**
       *  Optional. Specifies how rows are ordered in the response.
       *  Requests including both comparisons and multiple date ranges will
       *  have order bys applied on the comparisons.
       */
      // const orderBys = [1,2,3,4]
      /**
       *  Optional. A currency code in ISO4217 format, such as "AED", "USD", "JPY".
       *  If the field is empty, the report uses the property's default currency.
       */
      // const currencyCode = 'abc123'
      /**
       *  Optional. Cohort group associated with this request. If there is a cohort
       *  group in the request the 'cohort' dimension must be present.
       */
      // const cohortSpec = {}
      /**
       *  Optional. If false or unspecified, each row with all metrics equal to 0
       *  will not be returned. If true, these rows will be returned if they are not
       *  separately removed by a filter.
       *  Regardless of this `keep_empty_rows` setting, only data recorded by the
       *  Google Analytics property can be displayed in a report.
       *  For example if a property never logs a `purchase` event, then a query for
       *  the `eventName` dimension and  `eventCount` metric will not have a row
       *  eventName: "purchase" and eventCount: 0.
       */
      // const keepEmptyRows = true
      /**
       *  Optional. Toggles whether to return the current state of this Google
       *  Analytics property's quota. Quota is returned in
       *  PropertyQuota (#PropertyQuota).
       */
      // const returnPropertyQuota = true
      /**
       *  Optional. The configuration of comparisons requested and displayed. The
       *  request only requires a comparisons field in order to receive a comparison
       *  column in the response.
       */
      // const comparisons = [1,2,3,4]
      /**
       *  Optional. Controls conversion reporting. This field is optional. If this
       *  field is set or any conversion metrics are requested, the report will be a
       *  conversion report.
       */
      // const conversionSpec = {}
    
      // Imports the Data library
      const {AlphaAnalyticsDataClient} = require('[@google-analytics/data](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const dataClient = new [AlphaAnalyticsDataClient](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/v1alpha.alphaanalyticsdataclient.html)();
    
      async function callRunReport() {
        // Construct request
        const request = {
          property,
        };
    
        // Run request
        const response = await dataClient.runReport(request);
        console.log(response);
      }
    
      callRunReport();
    
    

### runReport(request, options, callback)
    
    
    runReport(request: protos.google.analytics.data.v1alpha.IRunReportRequest, options: CallOptions, callback: Callback<protos.google.analytics.data.v1alpha.IRunReportResponse, protos.google.analytics.data.v1alpha.IRunReportRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IRunReportRequest](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.analytics.data.v1alpha.irunreportrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.analytics.data.v1alpha.IRunReportResponse](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.analytics.data.v1alpha.irunreportresponse), [protos.google.analytics.data.v1alpha.IRunReportRequest](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.analytics.data.v1alpha.irunreportrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### runReport(request, callback)
    
    
    runReport(request: protos.google.analytics.data.v1alpha.IRunReportRequest, callback: Callback<protos.google.analytics.data.v1alpha.IRunReportResponse, protos.google.analytics.data.v1alpha.IRunReportRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IRunReportRequest](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.analytics.data.v1alpha.irunreportrequest)`   
  
`callback` |  `Callback<[protos.google.analytics.data.v1alpha.IRunReportResponse](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.analytics.data.v1alpha.irunreportresponse), [protos.google.analytics.data.v1alpha.IRunReportRequest](https://docs.cloud.google.com/nodejs/docs/reference/data/latest/data/protos.google.analytics.data.v1alpha.irunreportrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
