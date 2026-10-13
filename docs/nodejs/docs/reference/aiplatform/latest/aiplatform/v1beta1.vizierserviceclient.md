---
url: https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/v1beta1.vizierserviceclient
title: Class v1beta1.VizierServiceClient (7.4.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:14:46.255753+00:00
---

# Class v1beta1.VizierServiceClient (7.4.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/v1beta1.vizierserviceclient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class v1beta1.VizierServiceClient (7.4.1) Stay organized with collections  Save and categorize content based on your preferences. 

7.4.1 (latest)  7.3.0  6.10.0  6.9.0  6.8.1  6.6.0  6.4.0  6.3.0  6.2.0  6.1.0  6.0.0  5.14.0  5.13.0  3.15.0  3.13.0  3.11.0  3.10.1  3.9.0  3.7.0  3.6.0  3.4.0  3.3.0  3.0.0  2.12.0  2.11.0  2.10.0  2.7.0  2.6.1  2.5.0  2.3.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.1  1.13.0  1.11.0  1.7.2 

Vertex AI Vizier API.

Vertex AI Vizier is a service to solve blackbox optimization problems, such as tuning machine learning hyperparameters and searching over deep learning architectures. v1beta1

## Package

[@google-cloud/aiplatform](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)

## Constructors 

### (constructor)(opts, gaxInstance)
    
    
    constructor(opts?: ClientOptions, gaxInstance?: typeof gax | typeof gax.fallback);

Construct an instance of VizierServiceClient.

**Parameters**  
---  
**Name** | **Description**  
`opts` |  `ClientOptions`   
  
`gaxInstance` |  `typeof gax | typeof fallback`   
: loaded instance of `google-gax`. Useful if you need to avoid loading the default gRPC version and want to use the fallback HTTP implementation. Load only fallback version and pass it to the constructor: ``` const gax = require('google-gax/build/src/fallback'); // avoids loading google-gax with gRPC const client = new VizierServiceClient({fallback: true}, gax); ```  
  
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

### iamClient
    
    
    iamClient: IamClient;

### innerApiCalls
    
    
    innerApiCalls: {
            [name: string]: Function;
        };

### locationsClient
    
    
    locationsClient: LocationsClient;

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

### vizierServiceStub
    
    
    vizierServiceStub?: Promise<{
            [name: string]: Function;
        }>;

### warn
    
    
    warn: (code: string, message: string, warnType?: string) => void;

## Methods 

### addTrialMeasurement(request, options)
    
    
    addTrialMeasurement(request?: protos.google.cloud.aiplatform.v1beta1.IAddTrialMeasurementRequest, options?: CallOptions): Promise<[
            protos.google.cloud.aiplatform.v1beta1.ITrial,
            (protos.google.cloud.aiplatform.v1beta1.IAddTrialMeasurementRequest | undefined),
            {} | undefined
        ]>;

Adds a measurement of the objective metrics to a Trial. This measurement is assumed to have been taken before the Trial is complete.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IAddTrialMeasurementRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.iaddtrialmeasurementrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.aiplatform.v1beta1.ITrial](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.itrial), ([protos.google.cloud.aiplatform.v1beta1.IAddTrialMeasurementRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.iaddtrialmeasurementrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The name of the trial to add measurement.
       *  Format:
       *  `projects/{project}/locations/{location}/studies/{study}/trials/{trial}`
       */
      // const trialName = 'abc123'
      /**
       *  Required. The measurement to be added to a Trial.
       */
      // const measurement = {}
    
      // Imports the Aiplatform library
      const {VizierServiceClient} = require('[@google-cloud/aiplatform](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const aiplatformClient = new [VizierServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)();
    
      async function callAddTrialMeasurement() {
        // Construct request
        const request = {
          trialName,
          measurement,
        };
    
        // Run request
        const response = await aiplatformClient.addTrialMeasurement(request);
        console.log(response);
      }
    
      callAddTrialMeasurement();
    
    

### addTrialMeasurement(request, options, callback)
    
    
    addTrialMeasurement(request: protos.google.cloud.aiplatform.v1beta1.IAddTrialMeasurementRequest, options: CallOptions, callback: Callback<protos.google.cloud.aiplatform.v1beta1.ITrial, protos.google.cloud.aiplatform.v1beta1.IAddTrialMeasurementRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IAddTrialMeasurementRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.iaddtrialmeasurementrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.aiplatform.v1beta1.ITrial](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.itrial), [protos.google.cloud.aiplatform.v1beta1.IAddTrialMeasurementRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.iaddtrialmeasurementrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### addTrialMeasurement(request, callback)
    
    
    addTrialMeasurement(request: protos.google.cloud.aiplatform.v1beta1.IAddTrialMeasurementRequest, callback: Callback<protos.google.cloud.aiplatform.v1beta1.ITrial, protos.google.cloud.aiplatform.v1beta1.IAddTrialMeasurementRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IAddTrialMeasurementRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.iaddtrialmeasurementrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.aiplatform.v1beta1.ITrial](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.itrial), [protos.google.cloud.aiplatform.v1beta1.IAddTrialMeasurementRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.iaddtrialmeasurementrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### annotationPath(project, location, dataset, dataItem, annotation)
    
    
    annotationPath(project: string, location: string, dataset: string, dataItem: string, annotation: string): string;

Return a fully-qualified annotation resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`dataset` |  `string`   
  
`dataItem` |  `string`   
  
`annotation` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### annotationSpecPath(project, location, dataset, annotationSpec)
    
    
    annotationSpecPath(project: string, location: string, dataset: string, annotationSpec: string): string;

Return a fully-qualified annotationSpec resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`dataset` |  `string`   
  
`annotationSpec` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### artifactPath(project, location, metadataStore, artifact)
    
    
    artifactPath(project: string, location: string, metadataStore: string, artifact: string): string;

Return a fully-qualified artifact resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`metadataStore` |  `string`   
  
`artifact` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### batchPredictionJobPath(project, location, batchPredictionJob)
    
    
    batchPredictionJobPath(project: string, location: string, batchPredictionJob: string): string;

Return a fully-qualified batchPredictionJob resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`batchPredictionJob` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### cachedContentPath(project, location, cachedContent)
    
    
    cachedContentPath(project: string, location: string, cachedContent: string): string;

Return a fully-qualified cachedContent resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`cachedContent` |  `string`   
  
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
`request` |  `[CancelOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.longrunning.canceloperationrequest)`   
The request object that will be sent.  
`optionsOrCallback` |  `CallOptions | Callback<[protos.google.longrunning.CancelOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.longrunning.canceloperationrequest), [protos.google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.protobuf.empty), {} | undefined | null>`   
  
`callback` |  `Callback<[protos.google.longrunning.CancelOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.longrunning.canceloperationrequest), [protos.google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.protobuf.empty), {} | undefined | null>`   
The function which will be called with the result of the API call. {Promise} - The promise which resolves when API call finishes. The promise has a method named "cancel" which cancels the ongoing API call.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[protos.google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.protobuf.empty)>` |   
**Example**
    
    
    const client = longrunning.operationsClient();
    await client.cancelOperation({name: ''});
    

### checkCheckTrialEarlyStoppingStateProgress(name)
    
    
    checkCheckTrialEarlyStoppingStateProgress(name: string): Promise<LROperation<protos.google.cloud.aiplatform.v1beta1.CheckTrialEarlyStoppingStateResponse, protos.google.cloud.aiplatform.v1beta1.CheckTrialEarlyStoppingStateMetatdata>>;

Check the status of the long running operation returned by `checkTrialEarlyStoppingState()`.

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
The operation name that will be passed.  
**Returns**  
---  
**Type** | **Description**  
`Promise<LROperation<[protos.google.cloud.aiplatform.v1beta1.CheckTrialEarlyStoppingStateResponse](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.checktrialearlystoppingstateresponse), [protos.google.cloud.aiplatform.v1beta1.CheckTrialEarlyStoppingStateMetatdata](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.checktrialearlystoppingstatemetatdata)>>` | {Promise} - The promise which resolves to an object. The decoded operation object has result and metadata field to get information from. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The Trial's name.
       *  Format:
       *  `projects/{project}/locations/{location}/studies/{study}/trials/{trial}`
       */
      // const trialName = 'abc123'
    
      // Imports the Aiplatform library
      const {VizierServiceClient} = require('[@google-cloud/aiplatform](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const aiplatformClient = new [VizierServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)();
    
      async function callCheckTrialEarlyStoppingState() {
        // Construct request
        const request = {
          trialName,
        };
    
        // Run request
        const [operation] = await aiplatformClient.checkTrialEarlyStoppingState(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callCheckTrialEarlyStoppingState();
    
    

### checkSuggestTrialsProgress(name)
    
    
    checkSuggestTrialsProgress(name: string): Promise<LROperation<protos.google.cloud.aiplatform.v1beta1.SuggestTrialsResponse, protos.google.cloud.aiplatform.v1beta1.SuggestTrialsMetadata>>;

Check the status of the long running operation returned by `suggestTrials()`.

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
The operation name that will be passed.  
**Returns**  
---  
**Type** | **Description**  
`Promise<LROperation<[protos.google.cloud.aiplatform.v1beta1.SuggestTrialsResponse](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.suggesttrialsresponse), [protos.google.cloud.aiplatform.v1beta1.SuggestTrialsMetadata](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.suggesttrialsmetadata)>>` | {Promise} - The promise which resolves to an object. The decoded operation object has result and metadata field to get information from. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The project and location that the Study belongs to.
       *  Format: `projects/{project}/locations/{location}/studies/{study}`
       */
      // const parent = 'abc123'
      /**
       *  Required. The number of suggestions requested. It must be positive.
       */
      // const suggestionCount = 1234
      /**
       *  Required. The identifier of the client that is requesting the suggestion.
       *  If multiple SuggestTrialsRequests have the same `client_id`,
       *  the service will return the identical suggested Trial if the Trial is
       *  pending, and provide a new Trial if the last suggested Trial was completed.
       */
      // const clientId = 'abc123'
      /**
       *  Optional. This allows you to specify the "context" for a Trial; a context
       *  is a slice (a subspace) of the search space.
       *  Typical uses for contexts:
       *  1) You are using Vizier to tune a server for best performance, but there's
       *    a strong weekly cycle.  The context specifies the day-of-week.
       *    This allows Tuesday to generalize from Wednesday without assuming that
       *    everything is identical.
       *  2) Imagine you're optimizing some medical treatment for people.
       *    As they walk in the door, you know certain facts about them
       *    (e.g. sex, weight, height, blood-pressure).  Put that information in the
       *    context, and Vizier will adapt its suggestions to the patient.
       *  3) You want to do a fair A/B test efficiently.  Specify the "A" and "B"
       *    conditions as contexts, and Vizier will generalize between "A" and "B"
       *    conditions.  If they are similar, this will allow Vizier to converge
       *    to the optimum faster than if "A" and "B" were separate Studies.
       *    NOTE: You can also enter contexts as REQUESTED Trials, e.g. via the
       *    CreateTrial() RPC; that's the asynchronous option where you don't need a
       *    close association between contexts and suggestions.
       *  NOTE: All the Parameters you set in a context MUST be defined in the
       *    Study.
       *  NOTE: You must supply 0 or $suggestion_count contexts.
       *    If you don't supply any contexts, Vizier will make suggestions
       *    from the full search space specified in the StudySpec; if you supply
       *    a full set of context, each suggestion will match the corresponding
       *    context.
       *  NOTE: A Context with no features set matches anything, and allows
       *    suggestions from the full search space.
       *  NOTE: Contexts MUST lie within the search space specified in the
       *    StudySpec.  It's an error if they don't.
       *  NOTE: Contexts preferentially match ACTIVE then REQUESTED trials before
       *    new suggestions are generated.
       *  NOTE: Generation of suggestions involves a match between a Context and
       *    (optionally) a REQUESTED trial; if that match is not fully specified, a
       *    suggestion will be geneated in the merged subspace.
       */
      // const contexts = [1,2,3,4]
    
      // Imports the Aiplatform library
      const {VizierServiceClient} = require('[@google-cloud/aiplatform](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const aiplatformClient = new [VizierServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)();
    
      async function callSuggestTrials() {
        // Construct request
        const request = {
          parent,
          suggestionCount,
          clientId,
        };
    
        // Run request
        const [operation] = await aiplatformClient.suggestTrials(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callSuggestTrials();
    
    

### checkTrialEarlyStoppingState(request, options)
    
    
    checkTrialEarlyStoppingState(request?: protos.google.cloud.aiplatform.v1beta1.ICheckTrialEarlyStoppingStateRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.cloud.aiplatform.v1beta1.ICheckTrialEarlyStoppingStateResponse, protos.google.cloud.aiplatform.v1beta1.ICheckTrialEarlyStoppingStateMetatdata>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Checks whether a Trial should stop or not. Returns a long-running operation. When the operation is successful, it will contain a [CheckTrialEarlyStoppingStateResponse](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.checktrialearlystoppingstateresponse).

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICheckTrialEarlyStoppingStateRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ichecktrialearlystoppingstaterequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.cloud.aiplatform.v1beta1.ICheckTrialEarlyStoppingStateResponse](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ichecktrialearlystoppingstateresponse), [protos.google.cloud.aiplatform.v1beta1.ICheckTrialEarlyStoppingStateMetatdata](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ichecktrialearlystoppingstatemetatdata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.longrunning.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Its `promise()` method returns a promise you can `await` for. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The Trial's name.
       *  Format:
       *  `projects/{project}/locations/{location}/studies/{study}/trials/{trial}`
       */
      // const trialName = 'abc123'
    
      // Imports the Aiplatform library
      const {VizierServiceClient} = require('[@google-cloud/aiplatform](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const aiplatformClient = new [VizierServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)();
    
      async function callCheckTrialEarlyStoppingState() {
        // Construct request
        const request = {
          trialName,
        };
    
        // Run request
        const [operation] = await aiplatformClient.checkTrialEarlyStoppingState(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callCheckTrialEarlyStoppingState();
    
    

### checkTrialEarlyStoppingState(request, options, callback)
    
    
    checkTrialEarlyStoppingState(request: protos.google.cloud.aiplatform.v1beta1.ICheckTrialEarlyStoppingStateRequest, options: CallOptions, callback: Callback<LROperation<protos.google.cloud.aiplatform.v1beta1.ICheckTrialEarlyStoppingStateResponse, protos.google.cloud.aiplatform.v1beta1.ICheckTrialEarlyStoppingStateMetatdata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICheckTrialEarlyStoppingStateRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ichecktrialearlystoppingstaterequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.aiplatform.v1beta1.ICheckTrialEarlyStoppingStateResponse](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ichecktrialearlystoppingstateresponse), [protos.google.cloud.aiplatform.v1beta1.ICheckTrialEarlyStoppingStateMetatdata](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ichecktrialearlystoppingstatemetatdata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### checkTrialEarlyStoppingState(request, callback)
    
    
    checkTrialEarlyStoppingState(request: protos.google.cloud.aiplatform.v1beta1.ICheckTrialEarlyStoppingStateRequest, callback: Callback<LROperation<protos.google.cloud.aiplatform.v1beta1.ICheckTrialEarlyStoppingStateResponse, protos.google.cloud.aiplatform.v1beta1.ICheckTrialEarlyStoppingStateMetatdata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICheckTrialEarlyStoppingStateRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ichecktrialearlystoppingstaterequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.aiplatform.v1beta1.ICheckTrialEarlyStoppingStateResponse](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ichecktrialearlystoppingstateresponse), [protos.google.cloud.aiplatform.v1beta1.ICheckTrialEarlyStoppingStateMetatdata](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ichecktrialearlystoppingstatemetatdata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### close()
    
    
    close(): Promise<void>;

Terminate the gRPC channel and close the client.

The client will no longer be usable and all future behavior is undefined.

**Returns**  
---  
**Type** | **Description**  
`Promise<void>` | {Promise} A promise that resolves when the client is closed.  
  
### completeTrial(request, options)
    
    
    completeTrial(request?: protos.google.cloud.aiplatform.v1beta1.ICompleteTrialRequest, options?: CallOptions): Promise<[
            protos.google.cloud.aiplatform.v1beta1.ITrial,
            protos.google.cloud.aiplatform.v1beta1.ICompleteTrialRequest | undefined,
            {} | undefined
        ]>;

Marks a Trial as complete.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICompleteTrialRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.icompletetrialrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.aiplatform.v1beta1.ITrial](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.itrial), [protos.google.cloud.aiplatform.v1beta1.ICompleteTrialRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.icompletetrialrequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The Trial's name.
       *  Format:
       *  `projects/{project}/locations/{location}/studies/{study}/trials/{trial}`
       */
      // const name = 'abc123'
      /**
       *  Optional. If provided, it will be used as the completed Trial's
       *  final_measurement; Otherwise, the service will auto-select a
       *  previously reported measurement as the final-measurement
       */
      // const finalMeasurement = {}
      /**
       *  Optional. True if the Trial cannot be run with the given Parameter, and
       *  final_measurement will be ignored.
       */
      // const trialInfeasible = true
      /**
       *  Optional. A human readable reason why the trial was infeasible. This should
       *  only be provided if `trial_infeasible` is true.
       */
      // const infeasibleReason = 'abc123'
    
      // Imports the Aiplatform library
      const {VizierServiceClient} = require('[@google-cloud/aiplatform](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const aiplatformClient = new [VizierServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)();
    
      async function callCompleteTrial() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await aiplatformClient.completeTrial(request);
        console.log(response);
      }
    
      callCompleteTrial();
    
    

### completeTrial(request, options, callback)
    
    
    completeTrial(request: protos.google.cloud.aiplatform.v1beta1.ICompleteTrialRequest, options: CallOptions, callback: Callback<protos.google.cloud.aiplatform.v1beta1.ITrial, protos.google.cloud.aiplatform.v1beta1.ICompleteTrialRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICompleteTrialRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.icompletetrialrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.aiplatform.v1beta1.ITrial](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.itrial), [protos.google.cloud.aiplatform.v1beta1.ICompleteTrialRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.icompletetrialrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### completeTrial(request, callback)
    
    
    completeTrial(request: protos.google.cloud.aiplatform.v1beta1.ICompleteTrialRequest, callback: Callback<protos.google.cloud.aiplatform.v1beta1.ITrial, protos.google.cloud.aiplatform.v1beta1.ICompleteTrialRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICompleteTrialRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.icompletetrialrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.aiplatform.v1beta1.ITrial](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.itrial), [protos.google.cloud.aiplatform.v1beta1.ICompleteTrialRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.icompletetrialrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### contextPath(project, location, metadataStore, context)
    
    
    contextPath(project: string, location: string, metadataStore: string, context: string): string;

Return a fully-qualified context resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`metadataStore` |  `string`   
  
`context` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### createStudy(request, options)
    
    
    createStudy(request?: protos.google.cloud.aiplatform.v1beta1.ICreateStudyRequest, options?: CallOptions): Promise<[
            protos.google.cloud.aiplatform.v1beta1.IStudy,
            protos.google.cloud.aiplatform.v1beta1.ICreateStudyRequest | undefined,
            {} | undefined
        ]>;

Creates a Study. A resource name will be generated after creation of the Study.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateStudyRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.icreatestudyrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.aiplatform.v1beta1.IStudy](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.istudy), [protos.google.cloud.aiplatform.v1beta1.ICreateStudyRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.icreatestudyrequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The resource name of the Location to create the CustomJob in.
       *  Format: `projects/{project}/locations/{location}`
       */
      // const parent = 'abc123'
      /**
       *  Required. The Study configuration used to create the Study.
       */
      // const study = {}
    
      // Imports the Aiplatform library
      const {VizierServiceClient} = require('[@google-cloud/aiplatform](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const aiplatformClient = new [VizierServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)();
    
      async function callCreateStudy() {
        // Construct request
        const request = {
          parent,
          study,
        };
    
        // Run request
        const response = await aiplatformClient.createStudy(request);
        console.log(response);
      }
    
      callCreateStudy();
    
    

### createStudy(request, options, callback)
    
    
    createStudy(request: protos.google.cloud.aiplatform.v1beta1.ICreateStudyRequest, options: CallOptions, callback: Callback<protos.google.cloud.aiplatform.v1beta1.IStudy, protos.google.cloud.aiplatform.v1beta1.ICreateStudyRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateStudyRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.icreatestudyrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.aiplatform.v1beta1.IStudy](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.istudy), [protos.google.cloud.aiplatform.v1beta1.ICreateStudyRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.icreatestudyrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createStudy(request, callback)
    
    
    createStudy(request: protos.google.cloud.aiplatform.v1beta1.ICreateStudyRequest, callback: Callback<protos.google.cloud.aiplatform.v1beta1.IStudy, protos.google.cloud.aiplatform.v1beta1.ICreateStudyRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateStudyRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.icreatestudyrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.aiplatform.v1beta1.IStudy](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.istudy), [protos.google.cloud.aiplatform.v1beta1.ICreateStudyRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.icreatestudyrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createTrial(request, options)
    
    
    createTrial(request?: protos.google.cloud.aiplatform.v1beta1.ICreateTrialRequest, options?: CallOptions): Promise<[
            protos.google.cloud.aiplatform.v1beta1.ITrial,
            protos.google.cloud.aiplatform.v1beta1.ICreateTrialRequest | undefined,
            {} | undefined
        ]>;

Adds a user provided Trial to a Study.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateTrialRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.icreatetrialrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.aiplatform.v1beta1.ITrial](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.itrial), [protos.google.cloud.aiplatform.v1beta1.ICreateTrialRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.icreatetrialrequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The resource name of the Study to create the Trial in.
       *  Format: `projects/{project}/locations/{location}/studies/{study}`
       */
      // const parent = 'abc123'
      /**
       *  Required. The Trial to create.
       */
      // const trial = {}
    
      // Imports the Aiplatform library
      const {VizierServiceClient} = require('[@google-cloud/aiplatform](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const aiplatformClient = new [VizierServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)();
    
      async function callCreateTrial() {
        // Construct request
        const request = {
          parent,
          trial,
        };
    
        // Run request
        const response = await aiplatformClient.createTrial(request);
        console.log(response);
      }
    
      callCreateTrial();
    
    

### createTrial(request, options, callback)
    
    
    createTrial(request: protos.google.cloud.aiplatform.v1beta1.ICreateTrialRequest, options: CallOptions, callback: Callback<protos.google.cloud.aiplatform.v1beta1.ITrial, protos.google.cloud.aiplatform.v1beta1.ICreateTrialRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateTrialRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.icreatetrialrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.aiplatform.v1beta1.ITrial](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.itrial), [protos.google.cloud.aiplatform.v1beta1.ICreateTrialRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.icreatetrialrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createTrial(request, callback)
    
    
    createTrial(request: protos.google.cloud.aiplatform.v1beta1.ICreateTrialRequest, callback: Callback<protos.google.cloud.aiplatform.v1beta1.ITrial, protos.google.cloud.aiplatform.v1beta1.ICreateTrialRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateTrialRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.icreatetrialrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.aiplatform.v1beta1.ITrial](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.itrial), [protos.google.cloud.aiplatform.v1beta1.ICreateTrialRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.icreatetrialrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### customJobPath(project, location, customJob)
    
    
    customJobPath(project: string, location: string, customJob: string): string;

Return a fully-qualified customJob resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`customJob` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### dataItemPath(project, location, dataset, dataItem)
    
    
    dataItemPath(project: string, location: string, dataset: string, dataItem: string): string;

Return a fully-qualified dataItem resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`dataset` |  `string`   
  
`dataItem` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### dataLabelingJobPath(project, location, dataLabelingJob)
    
    
    dataLabelingJobPath(project: string, location: string, dataLabelingJob: string): string;

Return a fully-qualified dataLabelingJob resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`dataLabelingJob` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### datasetPath(project, location, dataset)
    
    
    datasetPath(project: string, location: string, dataset: string): string;

Return a fully-qualified dataset resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`dataset` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### datasetVersionPath(project, location, dataset, datasetVersion)
    
    
    datasetVersionPath(project: string, location: string, dataset: string, datasetVersion: string): string;

Return a fully-qualified datasetVersion resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`dataset` |  `string`   
  
`datasetVersion` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### deleteOperation(request, optionsOrCallback, callback)
    
    
    deleteOperation(request: protos.google.longrunning.DeleteOperationRequest, optionsOrCallback?: gax.CallOptions | Callback<protos.google.protobuf.Empty, protos.google.longrunning.DeleteOperationRequest, {} | null | undefined>, callback?: Callback<protos.google.protobuf.Empty, protos.google.longrunning.DeleteOperationRequest, {} | null | undefined>): Promise<protos.google.protobuf.Empty>;

Deletes a long-running operation. This method indicates that the client is no longer interested in the operation result. It does not cancel the operation. If the server doesn't support this method, it returns `google.rpc.Code.UNIMPLEMENTED`.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[DeleteOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.longrunning.deleteoperationrequest)`   
The request object that will be sent.  
`optionsOrCallback` |  `CallOptions | Callback<[protos.google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.protobuf.empty), [protos.google.longrunning.DeleteOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.longrunning.deleteoperationrequest), {} | null | undefined>`   
  
`callback` |  `Callback<[protos.google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.protobuf.empty), [protos.google.longrunning.DeleteOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.longrunning.deleteoperationrequest), {} | null | undefined>`   
The function which will be called with the result of the API call. {Promise} - The promise which resolves when API call finishes. The promise has a method named "cancel" which cancels the ongoing API call.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[protos.google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.protobuf.empty)>` |   
**Example**
    
    
    const client = longrunning.operationsClient();
    await client.deleteOperation({name: ''});
    

### deleteStudy(request, options)
    
    
    deleteStudy(request?: protos.google.cloud.aiplatform.v1beta1.IDeleteStudyRequest, options?: CallOptions): Promise<[
            protos.google.protobuf.IEmpty,
            protos.google.cloud.aiplatform.v1beta1.IDeleteStudyRequest | undefined,
            {} | undefined
        ]>;

Deletes a Study.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteStudyRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ideletestudyrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.protobuf.iempty), [protos.google.cloud.aiplatform.v1beta1.IDeleteStudyRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ideletestudyrequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [Empty](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.protobuf.empty). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The name of the Study resource to be deleted.
       *  Format: `projects/{project}/locations/{location}/studies/{study}`
       */
      // const name = 'abc123'
    
      // Imports the Aiplatform library
      const {VizierServiceClient} = require('[@google-cloud/aiplatform](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const aiplatformClient = new [VizierServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)();
    
      async function callDeleteStudy() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await aiplatformClient.deleteStudy(request);
        console.log(response);
      }
    
      callDeleteStudy();
    
    

### deleteStudy(request, options, callback)
    
    
    deleteStudy(request: protos.google.cloud.aiplatform.v1beta1.IDeleteStudyRequest, options: CallOptions, callback: Callback<protos.google.protobuf.IEmpty, protos.google.cloud.aiplatform.v1beta1.IDeleteStudyRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteStudyRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ideletestudyrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.protobuf.iempty), [protos.google.cloud.aiplatform.v1beta1.IDeleteStudyRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ideletestudyrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteStudy(request, callback)
    
    
    deleteStudy(request: protos.google.cloud.aiplatform.v1beta1.IDeleteStudyRequest, callback: Callback<protos.google.protobuf.IEmpty, protos.google.cloud.aiplatform.v1beta1.IDeleteStudyRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteStudyRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ideletestudyrequest)`   
  
`callback` |  `Callback<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.protobuf.iempty), [protos.google.cloud.aiplatform.v1beta1.IDeleteStudyRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ideletestudyrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteTrial(request, options)
    
    
    deleteTrial(request?: protos.google.cloud.aiplatform.v1beta1.IDeleteTrialRequest, options?: CallOptions): Promise<[
            protos.google.protobuf.IEmpty,
            protos.google.cloud.aiplatform.v1beta1.IDeleteTrialRequest | undefined,
            {} | undefined
        ]>;

Deletes a Trial.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteTrialRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ideletetrialrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.protobuf.iempty), [protos.google.cloud.aiplatform.v1beta1.IDeleteTrialRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ideletetrialrequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [Empty](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.protobuf.empty). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The Trial's name.
       *  Format:
       *  `projects/{project}/locations/{location}/studies/{study}/trials/{trial}`
       */
      // const name = 'abc123'
    
      // Imports the Aiplatform library
      const {VizierServiceClient} = require('[@google-cloud/aiplatform](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const aiplatformClient = new [VizierServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)();
    
      async function callDeleteTrial() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await aiplatformClient.deleteTrial(request);
        console.log(response);
      }
    
      callDeleteTrial();
    
    

### deleteTrial(request, options, callback)
    
    
    deleteTrial(request: protos.google.cloud.aiplatform.v1beta1.IDeleteTrialRequest, options: CallOptions, callback: Callback<protos.google.protobuf.IEmpty, protos.google.cloud.aiplatform.v1beta1.IDeleteTrialRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteTrialRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ideletetrialrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.protobuf.iempty), [protos.google.cloud.aiplatform.v1beta1.IDeleteTrialRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ideletetrialrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteTrial(request, callback)
    
    
    deleteTrial(request: protos.google.cloud.aiplatform.v1beta1.IDeleteTrialRequest, callback: Callback<protos.google.protobuf.IEmpty, protos.google.cloud.aiplatform.v1beta1.IDeleteTrialRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteTrialRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ideletetrialrequest)`   
  
`callback` |  `Callback<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.protobuf.iempty), [protos.google.cloud.aiplatform.v1beta1.IDeleteTrialRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ideletetrialrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deploymentResourcePoolPath(project, location, deploymentResourcePool)
    
    
    deploymentResourcePoolPath(project: string, location: string, deploymentResourcePool: string): string;

Return a fully-qualified deploymentResourcePool resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`deploymentResourcePool` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### entityTypePath(project, location, featurestore, entityType)
    
    
    entityTypePath(project: string, location: string, featurestore: string, entityType: string): string;

Return a fully-qualified entityType resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`featurestore` |  `string`   
  
`entityType` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### exampleStorePath(project, location, exampleStore)
    
    
    exampleStorePath(project: string, location: string, exampleStore: string): string;

Return a fully-qualified exampleStore resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`exampleStore` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### executionPath(project, location, metadataStore, execution)
    
    
    executionPath(project: string, location: string, metadataStore: string, execution: string): string;

Return a fully-qualified execution resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`metadataStore` |  `string`   
  
`execution` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### extensionPath(project, location, extension)
    
    
    extensionPath(project: string, location: string, extension: string): string;

Return a fully-qualified extension resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`extension` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### featureGroupPath(project, location, featureGroup)
    
    
    featureGroupPath(project: string, location: string, featureGroup: string): string;

Return a fully-qualified featureGroup resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`featureGroup` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### featureMonitorJobPath(project, location, featureGroup, featureMonitor, featureMonitorJob)
    
    
    featureMonitorJobPath(project: string, location: string, featureGroup: string, featureMonitor: string, featureMonitorJob: string): string;

Return a fully-qualified featureMonitorJob resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`featureGroup` |  `string`   
  
`featureMonitor` |  `string`   
  
`featureMonitorJob` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### featureMonitorPath(project, location, featureGroup, featureMonitor)
    
    
    featureMonitorPath(project: string, location: string, featureGroup: string, featureMonitor: string): string;

Return a fully-qualified featureMonitor resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`featureGroup` |  `string`   
  
`featureMonitor` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### featureOnlineStorePath(project, location, featureOnlineStore)
    
    
    featureOnlineStorePath(project: string, location: string, featureOnlineStore: string): string;

Return a fully-qualified featureOnlineStore resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`featureOnlineStore` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### featurestorePath(project, location, featurestore)
    
    
    featurestorePath(project: string, location: string, featurestore: string): string;

Return a fully-qualified featurestore resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`featurestore` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### featureViewPath(project, location, featureOnlineStore, featureView)
    
    
    featureViewPath(project: string, location: string, featureOnlineStore: string, featureView: string): string;

Return a fully-qualified featureView resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`featureOnlineStore` |  `string`   
  
`featureView` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### featureViewSyncPath(project, location, featureOnlineStore, featureView)
    
    
    featureViewSyncPath(project: string, location: string, featureOnlineStore: string, featureView: string): string;

Return a fully-qualified featureViewSync resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`featureOnlineStore` |  `string`   
  
`featureView` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### getIamPolicy(request, options, callback)
    
    
    getIamPolicy(request: IamProtos.google.iam.v1.GetIamPolicyRequest, options?: gax.CallOptions | Callback<IamProtos.google.iam.v1.Policy, IamProtos.google.iam.v1.GetIamPolicyRequest | null | undefined, {} | null | undefined>, callback?: Callback<IamProtos.google.iam.v1.Policy, IamProtos.google.iam.v1.GetIamPolicyRequest | null | undefined, {} | null | undefined>): Promise<[IamProtos.google.iam.v1.Policy]>;

Gets the access control policy for a resource. Returns an empty policy if the resource exists and does not have a policy set.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `IamProtos.google.iam.v1.GetIamPolicyRequest`   
The request object that will be sent.  
`options` |  `CallOptions | Callback<google.iam.v1.Policy, google.iam.v1.GetIamPolicyRequest | null | undefined, {} | null | undefined>`   
Optional parameters. You can override the default settings for this call, e.g, timeout, retries, paginations, etc. See [gax.CallOptions](https://googleapis.github.io/gax-nodejs/interfaces/CallOptions.html) for the details.  
`callback` |  `Callback<google.iam.v1.Policy, google.iam.v1.GetIamPolicyRequest | null | undefined, {} | null | undefined>`   
The function which will be called with the result of the API call. The second parameter to the callback is an object representing .  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.iam.v1.Policy]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . The promise has a method named "cancel" which cancels the ongoing API call.  
  
### getLocation(request, options, callback)
    
    
    getLocation(request: LocationProtos.google.cloud.location.IGetLocationRequest, options?: gax.CallOptions | Callback<LocationProtos.google.cloud.location.ILocation, LocationProtos.google.cloud.location.IGetLocationRequest | null | undefined, {} | null | undefined>, callback?: Callback<LocationProtos.google.cloud.location.ILocation, LocationProtos.google.cloud.location.IGetLocationRequest | null | undefined, {} | null | undefined>): Promise<LocationProtos.google.cloud.location.ILocation>;

Gets information about a location.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `LocationProtos.google.cloud.location.IGetLocationRequest`   
The request object that will be sent.  
`options` |  `CallOptions | Callback<google.cloud.location.ILocation, google.cloud.location.IGetLocationRequest | null | undefined, {} | null | undefined>`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
`callback` |  `Callback<google.cloud.location.ILocation, google.cloud.location.IGetLocationRequest | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`Promise<google.cloud.location.ILocation>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
    const [response] = await client.getLocation(request);
    

### getOperation(request, optionsOrCallback, callback)
    
    
    getOperation(request: protos.google.longrunning.GetOperationRequest, optionsOrCallback?: gax.CallOptions | Callback<protos.google.longrunning.Operation, protos.google.longrunning.GetOperationRequest, {} | null | undefined>, callback?: Callback<protos.google.longrunning.Operation, protos.google.longrunning.GetOperationRequest, {} | null | undefined>): Promise<[protos.google.longrunning.Operation]>;

Gets the latest state of a long-running operation. Clients can use this method to poll the operation result at intervals as recommended by the API service.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[GetOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.longrunning.getoperationrequest)`   
The request object that will be sent.  
`optionsOrCallback` |  `CallOptions | Callback<[protos.google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.longrunning.operation), [protos.google.longrunning.GetOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.longrunning.getoperationrequest), {} | null | undefined>`   
  
`callback` |  `Callback<[protos.google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.longrunning.operation), [protos.google.longrunning.GetOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.longrunning.getoperationrequest), {} | null | undefined>`   
The function which will be called with the result of the API call. The second parameter to the callback is an object representing . {Promise} - The promise which resolves to an array. The first element of the array is an object representing . The promise has a method named "cancel" which cancels the ongoing API call.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[[protos.google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.longrunning.operation)]>` |   
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
  
### getStudy(request, options)
    
    
    getStudy(request?: protos.google.cloud.aiplatform.v1beta1.IGetStudyRequest, options?: CallOptions): Promise<[
            protos.google.cloud.aiplatform.v1beta1.IStudy,
            protos.google.cloud.aiplatform.v1beta1.IGetStudyRequest | undefined,
            {} | undefined
        ]>;

Gets a Study by name.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetStudyRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.igetstudyrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.aiplatform.v1beta1.IStudy](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.istudy), [protos.google.cloud.aiplatform.v1beta1.IGetStudyRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.igetstudyrequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The name of the Study resource.
       *  Format: `projects/{project}/locations/{location}/studies/{study}`
       */
      // const name = 'abc123'
    
      // Imports the Aiplatform library
      const {VizierServiceClient} = require('[@google-cloud/aiplatform](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const aiplatformClient = new [VizierServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)();
    
      async function callGetStudy() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await aiplatformClient.getStudy(request);
        console.log(response);
      }
    
      callGetStudy();
    
    

### getStudy(request, options, callback)
    
    
    getStudy(request: protos.google.cloud.aiplatform.v1beta1.IGetStudyRequest, options: CallOptions, callback: Callback<protos.google.cloud.aiplatform.v1beta1.IStudy, protos.google.cloud.aiplatform.v1beta1.IGetStudyRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetStudyRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.igetstudyrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.aiplatform.v1beta1.IStudy](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.istudy), [protos.google.cloud.aiplatform.v1beta1.IGetStudyRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.igetstudyrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getStudy(request, callback)
    
    
    getStudy(request: protos.google.cloud.aiplatform.v1beta1.IGetStudyRequest, callback: Callback<protos.google.cloud.aiplatform.v1beta1.IStudy, protos.google.cloud.aiplatform.v1beta1.IGetStudyRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetStudyRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.igetstudyrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.aiplatform.v1beta1.IStudy](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.istudy), [protos.google.cloud.aiplatform.v1beta1.IGetStudyRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.igetstudyrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getTrial(request, options)
    
    
    getTrial(request?: protos.google.cloud.aiplatform.v1beta1.IGetTrialRequest, options?: CallOptions): Promise<[
            protos.google.cloud.aiplatform.v1beta1.ITrial,
            protos.google.cloud.aiplatform.v1beta1.IGetTrialRequest | undefined,
            {} | undefined
        ]>;

Gets a Trial.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetTrialRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.igettrialrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.aiplatform.v1beta1.ITrial](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.itrial), [protos.google.cloud.aiplatform.v1beta1.IGetTrialRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.igettrialrequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The name of the Trial resource.
       *  Format:
       *  `projects/{project}/locations/{location}/studies/{study}/trials/{trial}`
       */
      // const name = 'abc123'
    
      // Imports the Aiplatform library
      const {VizierServiceClient} = require('[@google-cloud/aiplatform](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const aiplatformClient = new [VizierServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)();
    
      async function callGetTrial() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await aiplatformClient.getTrial(request);
        console.log(response);
      }
    
      callGetTrial();
    
    

### getTrial(request, options, callback)
    
    
    getTrial(request: protos.google.cloud.aiplatform.v1beta1.IGetTrialRequest, options: CallOptions, callback: Callback<protos.google.cloud.aiplatform.v1beta1.ITrial, protos.google.cloud.aiplatform.v1beta1.IGetTrialRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetTrialRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.igettrialrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.aiplatform.v1beta1.ITrial](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.itrial), [protos.google.cloud.aiplatform.v1beta1.IGetTrialRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.igettrialrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getTrial(request, callback)
    
    
    getTrial(request: protos.google.cloud.aiplatform.v1beta1.IGetTrialRequest, callback: Callback<protos.google.cloud.aiplatform.v1beta1.ITrial, protos.google.cloud.aiplatform.v1beta1.IGetTrialRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetTrialRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.igettrialrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.aiplatform.v1beta1.ITrial](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.itrial), [protos.google.cloud.aiplatform.v1beta1.IGetTrialRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.igettrialrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### hyperparameterTuningJobPath(project, location, hyperparameterTuningJob)
    
    
    hyperparameterTuningJobPath(project: string, location: string, hyperparameterTuningJob: string): string;

Return a fully-qualified hyperparameterTuningJob resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`hyperparameterTuningJob` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### indexEndpointPath(project, location, indexEndpoint)
    
    
    indexEndpointPath(project: string, location: string, indexEndpoint: string): string;

Return a fully-qualified indexEndpoint resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`indexEndpoint` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### indexPath(project, location, index)
    
    
    indexPath(project: string, location: string, index: string): string;

Return a fully-qualified index resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`index` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
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
  
### listLocationsAsync(request, options)
    
    
    listLocationsAsync(request: LocationProtos.google.cloud.location.IListLocationsRequest, options?: CallOptions): AsyncIterable<LocationProtos.google.cloud.location.ILocation>;

Lists information about the supported locations for this service. Returns an iterable object.

`for`-`await`-`of` syntax is used with the iterable to get response elements on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `LocationProtos.google.cloud.location.IListLocationsRequest`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<google.cloud.location.ILocation>` | {Object} An iterable Object that allows [async iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols). When you iterate the returned iterable, each element will be an object representing . The API will be called under the hood as needed, once per the page, so you can stop the iteration when you don't need more results. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
**Example**
    
    
    const iterable = client.listLocationsAsync(request);
    for await (const response of iterable) {
      // process response
    }
    

### listOperationsAsync(request, options)
    
    
    listOperationsAsync(request: protos.google.longrunning.ListOperationsRequest, options?: gax.CallOptions): AsyncIterable<protos.google.longrunning.IOperation>;

Lists operations that match the specified filter in the request. If the server doesn't support this method, it returns `UNIMPLEMENTED`. Returns an iterable object.

For-await-of syntax is used with the iterable to recursively get response element on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ListOperationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.longrunning.listoperationsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Optional parameters. You can override the default settings for this call, e.g, timeout, retries, paginations, etc. See [gax.CallOptions](https://googleapis.github.io/gax-nodejs/global.html#CallOptions) for the details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.longrunning.ioperation)>` | {Object} An iterable Object that conforms to [iteration protocols](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols).  
**Example**
    
    
    const client = longrunning.operationsClient();
    for await (const response of client.listOperationsAsync(request));
    // doThingsWith(response)
    

### listOptimalTrials(request, options)
    
    
    listOptimalTrials(request?: protos.google.cloud.aiplatform.v1beta1.IListOptimalTrialsRequest, options?: CallOptions): Promise<[
            protos.google.cloud.aiplatform.v1beta1.IListOptimalTrialsResponse,
            (protos.google.cloud.aiplatform.v1beta1.IListOptimalTrialsRequest | undefined),
            {} | undefined
        ]>;

Lists the pareto-optimal Trials for multi-objective Study or the optimal Trials for single-objective Study. The definition of pareto-optimal can be checked in wiki page. https://en.wikipedia.org/wiki/Pareto_efficiency

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListOptimalTrialsRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ilistoptimaltrialsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.aiplatform.v1beta1.IListOptimalTrialsResponse](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ilistoptimaltrialsresponse), ([protos.google.cloud.aiplatform.v1beta1.IListOptimalTrialsRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ilistoptimaltrialsrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [ListOptimalTrialsResponse](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.listoptimaltrialsresponse). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The name of the Study that the optimal Trial belongs to.
       */
      // const parent = 'abc123'
    
      // Imports the Aiplatform library
      const {VizierServiceClient} = require('[@google-cloud/aiplatform](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const aiplatformClient = new [VizierServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)();
    
      async function callListOptimalTrials() {
        // Construct request
        const request = {
          parent,
        };
    
        // Run request
        const response = await aiplatformClient.listOptimalTrials(request);
        console.log(response);
      }
    
      callListOptimalTrials();
    
    

### listOptimalTrials(request, options, callback)
    
    
    listOptimalTrials(request: protos.google.cloud.aiplatform.v1beta1.IListOptimalTrialsRequest, options: CallOptions, callback: Callback<protos.google.cloud.aiplatform.v1beta1.IListOptimalTrialsResponse, protos.google.cloud.aiplatform.v1beta1.IListOptimalTrialsRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListOptimalTrialsRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ilistoptimaltrialsrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.aiplatform.v1beta1.IListOptimalTrialsResponse](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ilistoptimaltrialsresponse), [protos.google.cloud.aiplatform.v1beta1.IListOptimalTrialsRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ilistoptimaltrialsrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listOptimalTrials(request, callback)
    
    
    listOptimalTrials(request: protos.google.cloud.aiplatform.v1beta1.IListOptimalTrialsRequest, callback: Callback<protos.google.cloud.aiplatform.v1beta1.IListOptimalTrialsResponse, protos.google.cloud.aiplatform.v1beta1.IListOptimalTrialsRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListOptimalTrialsRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ilistoptimaltrialsrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.aiplatform.v1beta1.IListOptimalTrialsResponse](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ilistoptimaltrialsresponse), [protos.google.cloud.aiplatform.v1beta1.IListOptimalTrialsRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ilistoptimaltrialsrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listStudies(request, options)
    
    
    listStudies(request?: protos.google.cloud.aiplatform.v1beta1.IListStudiesRequest, options?: CallOptions): Promise<[
            protos.google.cloud.aiplatform.v1beta1.IStudy[],
            protos.google.cloud.aiplatform.v1beta1.IListStudiesRequest | null,
            protos.google.cloud.aiplatform.v1beta1.IListStudiesResponse
        ]>;

Lists all the studies in a region for an associated project.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListStudiesRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.iliststudiesrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.aiplatform.v1beta1.IStudy](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.istudy)[], [protos.google.cloud.aiplatform.v1beta1.IListStudiesRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.iliststudiesrequest) | null, [protos.google.cloud.aiplatform.v1beta1.IListStudiesResponse](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.iliststudiesresponse) ]>` | {Promise} - The promise which resolves to an array. The first element of the array is Array of . The client library will perform auto-pagination by default: it will call the API as many times as needed and will merge results from all the pages into this array. Note that it can affect your quota. We recommend using `listStudiesAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listStudies(request, options, callback)
    
    
    listStudies(request: protos.google.cloud.aiplatform.v1beta1.IListStudiesRequest, options: CallOptions, callback: PaginationCallback<protos.google.cloud.aiplatform.v1beta1.IListStudiesRequest, protos.google.cloud.aiplatform.v1beta1.IListStudiesResponse | null | undefined, protos.google.cloud.aiplatform.v1beta1.IStudy>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListStudiesRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.iliststudiesrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.aiplatform.v1beta1.IListStudiesRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.iliststudiesrequest), [protos.google.cloud.aiplatform.v1beta1.IListStudiesResponse](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.iliststudiesresponse) | null | undefined, [protos.google.cloud.aiplatform.v1beta1.IStudy](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.istudy)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listStudies(request, callback)
    
    
    listStudies(request: protos.google.cloud.aiplatform.v1beta1.IListStudiesRequest, callback: PaginationCallback<protos.google.cloud.aiplatform.v1beta1.IListStudiesRequest, protos.google.cloud.aiplatform.v1beta1.IListStudiesResponse | null | undefined, protos.google.cloud.aiplatform.v1beta1.IStudy>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListStudiesRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.iliststudiesrequest)`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.aiplatform.v1beta1.IListStudiesRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.iliststudiesrequest), [protos.google.cloud.aiplatform.v1beta1.IListStudiesResponse](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.iliststudiesresponse) | null | undefined, [protos.google.cloud.aiplatform.v1beta1.IStudy](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.istudy)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listStudiesAsync(request, options)
    
    
    listStudiesAsync(request?: protos.google.cloud.aiplatform.v1beta1.IListStudiesRequest, options?: CallOptions): AsyncIterable<protos.google.cloud.aiplatform.v1beta1.IStudy>;

Equivalent to `listStudies`, but returns an iterable object.

`for`-`await`-`of` syntax is used with the iterable to get response elements on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListStudiesRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.iliststudiesrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.cloud.aiplatform.v1beta1.IStudy](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.istudy)>` | {Object} An iterable Object that allows [async iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols). When you iterate the returned iterable, each element will be an object representing . The API will be called under the hood as needed, once per the page, so you can stop the iteration when you don't need more results. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The resource name of the Location to list the Study from.
       *  Format: `projects/{project}/locations/{location}`
       */
      // const parent = 'abc123'
      /**
       *  Optional. A page token to request the next page of results.
       *  If unspecified, there are no subsequent pages.
       */
      // const pageToken = 'abc123'
      /**
       *  Optional. The maximum number of studies to return per "page" of results.
       *  If unspecified, service will pick an appropriate default.
       */
      // const pageSize = 1234
    
      // Imports the Aiplatform library
      const {VizierServiceClient} = require('[@google-cloud/aiplatform](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const aiplatformClient = new [VizierServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)();
    
      async function callListStudies() {
        // Construct request
        const request = {
          parent,
        };
    
        // Run request
        const iterable = aiplatformClient.listStudiesAsync(request);
        for await (const response of iterable) {
            console.log(response);
        }
      }
    
      callListStudies();
    
    

### listStudiesStream(request, options)
    
    
    listStudiesStream(request?: protos.google.cloud.aiplatform.v1beta1.IListStudiesRequest, options?: CallOptions): Transform;

Equivalent to `listStudies`, but returns a NodeJS Stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListStudiesRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.iliststudiesrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Transform` | {Stream} An object stream which emits an object representing on 'data' event. The client library will perform auto-pagination by default: it will call the API as many times as needed. Note that it can affect your quota. We recommend using `listStudiesAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listTrials(request, options)
    
    
    listTrials(request?: protos.google.cloud.aiplatform.v1beta1.IListTrialsRequest, options?: CallOptions): Promise<[
            protos.google.cloud.aiplatform.v1beta1.ITrial[],
            protos.google.cloud.aiplatform.v1beta1.IListTrialsRequest | null,
            protos.google.cloud.aiplatform.v1beta1.IListTrialsResponse
        ]>;

Lists the Trials associated with a Study.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListTrialsRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ilisttrialsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.aiplatform.v1beta1.ITrial](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.itrial)[], [protos.google.cloud.aiplatform.v1beta1.IListTrialsRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ilisttrialsrequest) | null, [protos.google.cloud.aiplatform.v1beta1.IListTrialsResponse](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ilisttrialsresponse) ]>` | {Promise} - The promise which resolves to an array. The first element of the array is Array of . The client library will perform auto-pagination by default: it will call the API as many times as needed and will merge results from all the pages into this array. Note that it can affect your quota. We recommend using `listTrialsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listTrials(request, options, callback)
    
    
    listTrials(request: protos.google.cloud.aiplatform.v1beta1.IListTrialsRequest, options: CallOptions, callback: PaginationCallback<protos.google.cloud.aiplatform.v1beta1.IListTrialsRequest, protos.google.cloud.aiplatform.v1beta1.IListTrialsResponse | null | undefined, protos.google.cloud.aiplatform.v1beta1.ITrial>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListTrialsRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ilisttrialsrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.aiplatform.v1beta1.IListTrialsRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ilisttrialsrequest), [protos.google.cloud.aiplatform.v1beta1.IListTrialsResponse](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ilisttrialsresponse) | null | undefined, [protos.google.cloud.aiplatform.v1beta1.ITrial](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.itrial)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listTrials(request, callback)
    
    
    listTrials(request: protos.google.cloud.aiplatform.v1beta1.IListTrialsRequest, callback: PaginationCallback<protos.google.cloud.aiplatform.v1beta1.IListTrialsRequest, protos.google.cloud.aiplatform.v1beta1.IListTrialsResponse | null | undefined, protos.google.cloud.aiplatform.v1beta1.ITrial>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListTrialsRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ilisttrialsrequest)`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.aiplatform.v1beta1.IListTrialsRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ilisttrialsrequest), [protos.google.cloud.aiplatform.v1beta1.IListTrialsResponse](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ilisttrialsresponse) | null | undefined, [protos.google.cloud.aiplatform.v1beta1.ITrial](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.itrial)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listTrialsAsync(request, options)
    
    
    listTrialsAsync(request?: protos.google.cloud.aiplatform.v1beta1.IListTrialsRequest, options?: CallOptions): AsyncIterable<protos.google.cloud.aiplatform.v1beta1.ITrial>;

Equivalent to `listTrials`, but returns an iterable object.

`for`-`await`-`of` syntax is used with the iterable to get response elements on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListTrialsRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ilisttrialsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.cloud.aiplatform.v1beta1.ITrial](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.itrial)>` | {Object} An iterable Object that allows [async iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols). When you iterate the returned iterable, each element will be an object representing . The API will be called under the hood as needed, once per the page, so you can stop the iteration when you don't need more results. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The resource name of the Study to list the Trial from.
       *  Format: `projects/{project}/locations/{location}/studies/{study}`
       */
      // const parent = 'abc123'
      /**
       *  Optional. A page token to request the next page of results.
       *  If unspecified, there are no subsequent pages.
       */
      // const pageToken = 'abc123'
      /**
       *  Optional. The number of Trials to retrieve per "page" of results.
       *  If unspecified, the service will pick an appropriate default.
       */
      // const pageSize = 1234
    
      // Imports the Aiplatform library
      const {VizierServiceClient} = require('[@google-cloud/aiplatform](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const aiplatformClient = new [VizierServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)();
    
      async function callListTrials() {
        // Construct request
        const request = {
          parent,
        };
    
        // Run request
        const iterable = aiplatformClient.listTrialsAsync(request);
        for await (const response of iterable) {
            console.log(response);
        }
      }
    
      callListTrials();
    
    

### listTrialsStream(request, options)
    
    
    listTrialsStream(request?: protos.google.cloud.aiplatform.v1beta1.IListTrialsRequest, options?: CallOptions): Transform;

Equivalent to `listTrials`, but returns a NodeJS Stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListTrialsRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ilisttrialsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Transform` | {Stream} An object stream which emits an object representing on 'data' event. The client library will perform auto-pagination by default: it will call the API as many times as needed. Note that it can affect your quota. We recommend using `listTrialsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### locationPath(project, location)
    
    
    locationPath(project: string, location: string): string;

Return a fully-qualified location resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### lookupStudy(request, options)
    
    
    lookupStudy(request?: protos.google.cloud.aiplatform.v1beta1.ILookupStudyRequest, options?: CallOptions): Promise<[
            protos.google.cloud.aiplatform.v1beta1.IStudy,
            protos.google.cloud.aiplatform.v1beta1.ILookupStudyRequest | undefined,
            {} | undefined
        ]>;

Looks a study up using the user-defined display_name field instead of the fully qualified resource name.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ILookupStudyRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ilookupstudyrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.aiplatform.v1beta1.IStudy](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.istudy), [protos.google.cloud.aiplatform.v1beta1.ILookupStudyRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ilookupstudyrequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The resource name of the Location to get the Study from.
       *  Format: `projects/{project}/locations/{location}`
       */
      // const parent = 'abc123'
      /**
       *  Required. The user-defined display name of the Study
       */
      // const displayName = 'abc123'
    
      // Imports the Aiplatform library
      const {VizierServiceClient} = require('[@google-cloud/aiplatform](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const aiplatformClient = new [VizierServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)();
    
      async function callLookupStudy() {
        // Construct request
        const request = {
          parent,
          displayName,
        };
    
        // Run request
        const response = await aiplatformClient.lookupStudy(request);
        console.log(response);
      }
    
      callLookupStudy();
    
    

### lookupStudy(request, options, callback)
    
    
    lookupStudy(request: protos.google.cloud.aiplatform.v1beta1.ILookupStudyRequest, options: CallOptions, callback: Callback<protos.google.cloud.aiplatform.v1beta1.IStudy, protos.google.cloud.aiplatform.v1beta1.ILookupStudyRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ILookupStudyRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ilookupstudyrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.aiplatform.v1beta1.IStudy](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.istudy), [protos.google.cloud.aiplatform.v1beta1.ILookupStudyRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ilookupstudyrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### lookupStudy(request, callback)
    
    
    lookupStudy(request: protos.google.cloud.aiplatform.v1beta1.ILookupStudyRequest, callback: Callback<protos.google.cloud.aiplatform.v1beta1.IStudy, protos.google.cloud.aiplatform.v1beta1.ILookupStudyRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ILookupStudyRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ilookupstudyrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.aiplatform.v1beta1.IStudy](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.istudy), [protos.google.cloud.aiplatform.v1beta1.ILookupStudyRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ilookupstudyrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### matchAnnotationFromAnnotationName(annotationName)
    
    
    matchAnnotationFromAnnotationName(annotationName: string): string | number;

Parse the annotation from Annotation resource.

**Parameter**  
---  
**Name** | **Description**  
`annotationName` |  `string`   
A fully-qualified path representing Annotation resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the annotation.  
  
### matchAnnotationSpecFromAnnotationSpecName(annotationSpecName)
    
    
    matchAnnotationSpecFromAnnotationSpecName(annotationSpecName: string): string | number;

Parse the annotation_spec from AnnotationSpec resource.

**Parameter**  
---  
**Name** | **Description**  
`annotationSpecName` |  `string`   
A fully-qualified path representing AnnotationSpec resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the annotation_spec.  
  
### matchArtifactFromArtifactName(artifactName)
    
    
    matchArtifactFromArtifactName(artifactName: string): string | number;

Parse the artifact from Artifact resource.

**Parameter**  
---  
**Name** | **Description**  
`artifactName` |  `string`   
A fully-qualified path representing Artifact resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the artifact.  
  
### matchBatchPredictionJobFromBatchPredictionJobName(batchPredictionJobName)
    
    
    matchBatchPredictionJobFromBatchPredictionJobName(batchPredictionJobName: string): string | number;

Parse the batch_prediction_job from BatchPredictionJob resource.

**Parameter**  
---  
**Name** | **Description**  
`batchPredictionJobName` |  `string`   
A fully-qualified path representing BatchPredictionJob resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the batch_prediction_job.  
  
### matchCachedContentFromCachedContentName(cachedContentName)
    
    
    matchCachedContentFromCachedContentName(cachedContentName: string): string | number;

Parse the cached_content from CachedContent resource.

**Parameter**  
---  
**Name** | **Description**  
`cachedContentName` |  `string`   
A fully-qualified path representing CachedContent resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the cached_content.  
  
### matchContextFromContextName(contextName)
    
    
    matchContextFromContextName(contextName: string): string | number;

Parse the context from Context resource.

**Parameter**  
---  
**Name** | **Description**  
`contextName` |  `string`   
A fully-qualified path representing Context resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the context.  
  
### matchCustomJobFromCustomJobName(customJobName)
    
    
    matchCustomJobFromCustomJobName(customJobName: string): string | number;

Parse the custom_job from CustomJob resource.

**Parameter**  
---  
**Name** | **Description**  
`customJobName` |  `string`   
A fully-qualified path representing CustomJob resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the custom_job.  
  
### matchDataItemFromAnnotationName(annotationName)
    
    
    matchDataItemFromAnnotationName(annotationName: string): string | number;

Parse the data_item from Annotation resource.

**Parameter**  
---  
**Name** | **Description**  
`annotationName` |  `string`   
A fully-qualified path representing Annotation resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the data_item.  
  
### matchDataItemFromDataItemName(dataItemName)
    
    
    matchDataItemFromDataItemName(dataItemName: string): string | number;

Parse the data_item from DataItem resource.

**Parameter**  
---  
**Name** | **Description**  
`dataItemName` |  `string`   
A fully-qualified path representing DataItem resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the data_item.  
  
### matchDataLabelingJobFromDataLabelingJobName(dataLabelingJobName)
    
    
    matchDataLabelingJobFromDataLabelingJobName(dataLabelingJobName: string): string | number;

Parse the data_labeling_job from DataLabelingJob resource.

**Parameter**  
---  
**Name** | **Description**  
`dataLabelingJobName` |  `string`   
A fully-qualified path representing DataLabelingJob resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the data_labeling_job.  
  
### matchDatasetFromAnnotationName(annotationName)
    
    
    matchDatasetFromAnnotationName(annotationName: string): string | number;

Parse the dataset from Annotation resource.

**Parameter**  
---  
**Name** | **Description**  
`annotationName` |  `string`   
A fully-qualified path representing Annotation resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the dataset.  
  
### matchDatasetFromAnnotationSpecName(annotationSpecName)
    
    
    matchDatasetFromAnnotationSpecName(annotationSpecName: string): string | number;

Parse the dataset from AnnotationSpec resource.

**Parameter**  
---  
**Name** | **Description**  
`annotationSpecName` |  `string`   
A fully-qualified path representing AnnotationSpec resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the dataset.  
  
### matchDatasetFromDataItemName(dataItemName)
    
    
    matchDatasetFromDataItemName(dataItemName: string): string | number;

Parse the dataset from DataItem resource.

**Parameter**  
---  
**Name** | **Description**  
`dataItemName` |  `string`   
A fully-qualified path representing DataItem resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the dataset.  
  
### matchDatasetFromDatasetName(datasetName)
    
    
    matchDatasetFromDatasetName(datasetName: string): string | number;

Parse the dataset from Dataset resource.

**Parameter**  
---  
**Name** | **Description**  
`datasetName` |  `string`   
A fully-qualified path representing Dataset resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the dataset.  
  
### matchDatasetFromDatasetVersionName(datasetVersionName)
    
    
    matchDatasetFromDatasetVersionName(datasetVersionName: string): string | number;

Parse the dataset from DatasetVersion resource.

**Parameter**  
---  
**Name** | **Description**  
`datasetVersionName` |  `string`   
A fully-qualified path representing DatasetVersion resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the dataset.  
  
### matchDatasetFromSavedQueryName(savedQueryName)
    
    
    matchDatasetFromSavedQueryName(savedQueryName: string): string | number;

Parse the dataset from SavedQuery resource.

**Parameter**  
---  
**Name** | **Description**  
`savedQueryName` |  `string`   
A fully-qualified path representing SavedQuery resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the dataset.  
  
### matchDatasetVersionFromDatasetVersionName(datasetVersionName)
    
    
    matchDatasetVersionFromDatasetVersionName(datasetVersionName: string): string | number;

Parse the dataset_version from DatasetVersion resource.

**Parameter**  
---  
**Name** | **Description**  
`datasetVersionName` |  `string`   
A fully-qualified path representing DatasetVersion resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the dataset_version.  
  
### matchDeploymentResourcePoolFromDeploymentResourcePoolName(deploymentResourcePoolName)
    
    
    matchDeploymentResourcePoolFromDeploymentResourcePoolName(deploymentResourcePoolName: string): string | number;

Parse the deployment_resource_pool from DeploymentResourcePool resource.

**Parameter**  
---  
**Name** | **Description**  
`deploymentResourcePoolName` |  `string`   
A fully-qualified path representing DeploymentResourcePool resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the deployment_resource_pool.  
  
### matchEndpointFromProjectLocationEndpointName(projectLocationEndpointName)
    
    
    matchEndpointFromProjectLocationEndpointName(projectLocationEndpointName: string): string | number;

Parse the endpoint from ProjectLocationEndpoint resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationEndpointName` |  `string`   
A fully-qualified path representing project_location_endpoint resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the endpoint.  
  
### matchEntityTypeFromEntityTypeName(entityTypeName)
    
    
    matchEntityTypeFromEntityTypeName(entityTypeName: string): string | number;

Parse the entity_type from EntityType resource.

**Parameter**  
---  
**Name** | **Description**  
`entityTypeName` |  `string`   
A fully-qualified path representing EntityType resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the entity_type.  
  
### matchEntityTypeFromProjectLocationFeaturestoreEntityTypeFeaturesName(projectLocationFeaturestoreEntityTypeFeaturesName)
    
    
    matchEntityTypeFromProjectLocationFeaturestoreEntityTypeFeaturesName(projectLocationFeaturestoreEntityTypeFeaturesName: string): string | number;

Parse the entity_type from ProjectLocationFeaturestoreEntityTypeFeatures resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationFeaturestoreEntityTypeFeaturesName` |  `string`   
A fully-qualified path representing project_location_featurestore_entity_type_features resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the entity_type.  
  
### matchEvaluationFromModelEvaluationName(modelEvaluationName)
    
    
    matchEvaluationFromModelEvaluationName(modelEvaluationName: string): string | number;

Parse the evaluation from ModelEvaluation resource.

**Parameter**  
---  
**Name** | **Description**  
`modelEvaluationName` |  `string`   
A fully-qualified path representing ModelEvaluation resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the evaluation.  
  
### matchEvaluationFromModelEvaluationSliceName(modelEvaluationSliceName)
    
    
    matchEvaluationFromModelEvaluationSliceName(modelEvaluationSliceName: string): string | number;

Parse the evaluation from ModelEvaluationSlice resource.

**Parameter**  
---  
**Name** | **Description**  
`modelEvaluationSliceName` |  `string`   
A fully-qualified path representing ModelEvaluationSlice resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the evaluation.  
  
### matchEventFromSessionEventName(sessionEventName)
    
    
    matchEventFromSessionEventName(sessionEventName: string): string | number;

Parse the event from SessionEvent resource.

**Parameter**  
---  
**Name** | **Description**  
`sessionEventName` |  `string`   
A fully-qualified path representing SessionEvent resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the event.  
  
### matchExampleStoreFromExampleStoreName(exampleStoreName)
    
    
    matchExampleStoreFromExampleStoreName(exampleStoreName: string): string | number;

Parse the example_store from ExampleStore resource.

**Parameter**  
---  
**Name** | **Description**  
`exampleStoreName` |  `string`   
A fully-qualified path representing ExampleStore resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the example_store.  
  
### matchExecutionFromExecutionName(executionName)
    
    
    matchExecutionFromExecutionName(executionName: string): string | number;

Parse the execution from Execution resource.

**Parameter**  
---  
**Name** | **Description**  
`executionName` |  `string`   
A fully-qualified path representing Execution resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the execution.  
  
### matchExperimentFromTensorboardExperimentName(tensorboardExperimentName)
    
    
    matchExperimentFromTensorboardExperimentName(tensorboardExperimentName: string): string | number;

Parse the experiment from TensorboardExperiment resource.

**Parameter**  
---  
**Name** | **Description**  
`tensorboardExperimentName` |  `string`   
A fully-qualified path representing TensorboardExperiment resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the experiment.  
  
### matchExperimentFromTensorboardRunName(tensorboardRunName)
    
    
    matchExperimentFromTensorboardRunName(tensorboardRunName: string): string | number;

Parse the experiment from TensorboardRun resource.

**Parameter**  
---  
**Name** | **Description**  
`tensorboardRunName` |  `string`   
A fully-qualified path representing TensorboardRun resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the experiment.  
  
### matchExperimentFromTensorboardTimeSeriesName(tensorboardTimeSeriesName)
    
    
    matchExperimentFromTensorboardTimeSeriesName(tensorboardTimeSeriesName: string): string | number;

Parse the experiment from TensorboardTimeSeries resource.

**Parameter**  
---  
**Name** | **Description**  
`tensorboardTimeSeriesName` |  `string`   
A fully-qualified path representing TensorboardTimeSeries resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the experiment.  
  
### matchExtensionFromExtensionName(extensionName)
    
    
    matchExtensionFromExtensionName(extensionName: string): string | number;

Parse the extension from Extension resource.

**Parameter**  
---  
**Name** | **Description**  
`extensionName` |  `string`   
A fully-qualified path representing Extension resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the extension.  
  
### matchFeatureFromProjectLocationFeatureGroupFeaturesName(projectLocationFeatureGroupFeaturesName)
    
    
    matchFeatureFromProjectLocationFeatureGroupFeaturesName(projectLocationFeatureGroupFeaturesName: string): string | number;

Parse the feature from ProjectLocationFeatureGroupFeatures resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationFeatureGroupFeaturesName` |  `string`   
A fully-qualified path representing project_location_feature_group_features resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the feature.  
  
### matchFeatureFromProjectLocationFeaturestoreEntityTypeFeaturesName(projectLocationFeaturestoreEntityTypeFeaturesName)
    
    
    matchFeatureFromProjectLocationFeaturestoreEntityTypeFeaturesName(projectLocationFeaturestoreEntityTypeFeaturesName: string): string | number;

Parse the feature from ProjectLocationFeaturestoreEntityTypeFeatures resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationFeaturestoreEntityTypeFeaturesName` |  `string`   
A fully-qualified path representing project_location_featurestore_entity_type_features resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the feature.  
  
### matchFeatureGroupFromFeatureGroupName(featureGroupName)
    
    
    matchFeatureGroupFromFeatureGroupName(featureGroupName: string): string | number;

Parse the feature_group from FeatureGroup resource.

**Parameter**  
---  
**Name** | **Description**  
`featureGroupName` |  `string`   
A fully-qualified path representing FeatureGroup resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the feature_group.  
  
### matchFeatureGroupFromFeatureMonitorJobName(featureMonitorJobName)
    
    
    matchFeatureGroupFromFeatureMonitorJobName(featureMonitorJobName: string): string | number;

Parse the feature_group from FeatureMonitorJob resource.

**Parameter**  
---  
**Name** | **Description**  
`featureMonitorJobName` |  `string`   
A fully-qualified path representing FeatureMonitorJob resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the feature_group.  
  
### matchFeatureGroupFromFeatureMonitorName(featureMonitorName)
    
    
    matchFeatureGroupFromFeatureMonitorName(featureMonitorName: string): string | number;

Parse the feature_group from FeatureMonitor resource.

**Parameter**  
---  
**Name** | **Description**  
`featureMonitorName` |  `string`   
A fully-qualified path representing FeatureMonitor resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the feature_group.  
  
### matchFeatureGroupFromProjectLocationFeatureGroupFeaturesName(projectLocationFeatureGroupFeaturesName)
    
    
    matchFeatureGroupFromProjectLocationFeatureGroupFeaturesName(projectLocationFeatureGroupFeaturesName: string): string | number;

Parse the feature_group from ProjectLocationFeatureGroupFeatures resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationFeatureGroupFeaturesName` |  `string`   
A fully-qualified path representing project_location_feature_group_features resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the feature_group.  
  
### matchFeatureMonitorFromFeatureMonitorJobName(featureMonitorJobName)
    
    
    matchFeatureMonitorFromFeatureMonitorJobName(featureMonitorJobName: string): string | number;

Parse the feature_monitor from FeatureMonitorJob resource.

**Parameter**  
---  
**Name** | **Description**  
`featureMonitorJobName` |  `string`   
A fully-qualified path representing FeatureMonitorJob resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the feature_monitor.  
  
### matchFeatureMonitorFromFeatureMonitorName(featureMonitorName)
    
    
    matchFeatureMonitorFromFeatureMonitorName(featureMonitorName: string): string | number;

Parse the feature_monitor from FeatureMonitor resource.

**Parameter**  
---  
**Name** | **Description**  
`featureMonitorName` |  `string`   
A fully-qualified path representing FeatureMonitor resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the feature_monitor.  
  
### matchFeatureMonitorJobFromFeatureMonitorJobName(featureMonitorJobName)
    
    
    matchFeatureMonitorJobFromFeatureMonitorJobName(featureMonitorJobName: string): string | number;

Parse the feature_monitor_job from FeatureMonitorJob resource.

**Parameter**  
---  
**Name** | **Description**  
`featureMonitorJobName` |  `string`   
A fully-qualified path representing FeatureMonitorJob resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the feature_monitor_job.  
  
### matchFeatureOnlineStoreFromFeatureOnlineStoreName(featureOnlineStoreName)
    
    
    matchFeatureOnlineStoreFromFeatureOnlineStoreName(featureOnlineStoreName: string): string | number;

Parse the feature_online_store from FeatureOnlineStore resource.

**Parameter**  
---  
**Name** | **Description**  
`featureOnlineStoreName` |  `string`   
A fully-qualified path representing FeatureOnlineStore resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the feature_online_store.  
  
### matchFeatureOnlineStoreFromFeatureViewName(featureViewName)
    
    
    matchFeatureOnlineStoreFromFeatureViewName(featureViewName: string): string | number;

Parse the feature_online_store from FeatureView resource.

**Parameter**  
---  
**Name** | **Description**  
`featureViewName` |  `string`   
A fully-qualified path representing FeatureView resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the feature_online_store.  
  
### matchFeatureOnlineStoreFromFeatureViewSyncName(featureViewSyncName)
    
    
    matchFeatureOnlineStoreFromFeatureViewSyncName(featureViewSyncName: string): string | number;

Parse the feature_online_store from FeatureViewSync resource.

**Parameter**  
---  
**Name** | **Description**  
`featureViewSyncName` |  `string`   
A fully-qualified path representing FeatureViewSync resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the feature_online_store.  
  
### matchFeaturestoreFromEntityTypeName(entityTypeName)
    
    
    matchFeaturestoreFromEntityTypeName(entityTypeName: string): string | number;

Parse the featurestore from EntityType resource.

**Parameter**  
---  
**Name** | **Description**  
`entityTypeName` |  `string`   
A fully-qualified path representing EntityType resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the featurestore.  
  
### matchFeaturestoreFromFeaturestoreName(featurestoreName)
    
    
    matchFeaturestoreFromFeaturestoreName(featurestoreName: string): string | number;

Parse the featurestore from Featurestore resource.

**Parameter**  
---  
**Name** | **Description**  
`featurestoreName` |  `string`   
A fully-qualified path representing Featurestore resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the featurestore.  
  
### matchFeaturestoreFromProjectLocationFeaturestoreEntityTypeFeaturesName(projectLocationFeaturestoreEntityTypeFeaturesName)
    
    
    matchFeaturestoreFromProjectLocationFeaturestoreEntityTypeFeaturesName(projectLocationFeaturestoreEntityTypeFeaturesName: string): string | number;

Parse the featurestore from ProjectLocationFeaturestoreEntityTypeFeatures resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationFeaturestoreEntityTypeFeaturesName` |  `string`   
A fully-qualified path representing project_location_featurestore_entity_type_features resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the featurestore.  
  
### matchFeatureViewFromFeatureViewName(featureViewName)
    
    
    matchFeatureViewFromFeatureViewName(featureViewName: string): string | number;

Parse the feature_view from FeatureView resource.

**Parameter**  
---  
**Name** | **Description**  
`featureViewName` |  `string`   
A fully-qualified path representing FeatureView resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the feature_view.  
  
### matchFeatureViewFromFeatureViewSyncName(featureViewSyncName)
    
    
    matchFeatureViewFromFeatureViewSyncName(featureViewSyncName: string): string | number;

Parse the feature_view from FeatureViewSync resource.

**Parameter**  
---  
**Name** | **Description**  
`featureViewSyncName` |  `string`   
A fully-qualified path representing FeatureViewSync resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the feature_view.  
  
### matchHyperparameterTuningJobFromHyperparameterTuningJobName(hyperparameterTuningJobName)
    
    
    matchHyperparameterTuningJobFromHyperparameterTuningJobName(hyperparameterTuningJobName: string): string | number;

Parse the hyperparameter_tuning_job from HyperparameterTuningJob resource.

**Parameter**  
---  
**Name** | **Description**  
`hyperparameterTuningJobName` |  `string`   
A fully-qualified path representing HyperparameterTuningJob resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the hyperparameter_tuning_job.  
  
### matchIndexEndpointFromIndexEndpointName(indexEndpointName)
    
    
    matchIndexEndpointFromIndexEndpointName(indexEndpointName: string): string | number;

Parse the index_endpoint from IndexEndpoint resource.

**Parameter**  
---  
**Name** | **Description**  
`indexEndpointName` |  `string`   
A fully-qualified path representing IndexEndpoint resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the index_endpoint.  
  
### matchIndexFromIndexName(indexName)
    
    
    matchIndexFromIndexName(indexName: string): string | number;

Parse the index from Index resource.

**Parameter**  
---  
**Name** | **Description**  
`indexName` |  `string`   
A fully-qualified path representing Index resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the index.  
  
### matchLocationFromAnnotationName(annotationName)
    
    
    matchLocationFromAnnotationName(annotationName: string): string | number;

Parse the location from Annotation resource.

**Parameter**  
---  
**Name** | **Description**  
`annotationName` |  `string`   
A fully-qualified path representing Annotation resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromAnnotationSpecName(annotationSpecName)
    
    
    matchLocationFromAnnotationSpecName(annotationSpecName: string): string | number;

Parse the location from AnnotationSpec resource.

**Parameter**  
---  
**Name** | **Description**  
`annotationSpecName` |  `string`   
A fully-qualified path representing AnnotationSpec resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromArtifactName(artifactName)
    
    
    matchLocationFromArtifactName(artifactName: string): string | number;

Parse the location from Artifact resource.

**Parameter**  
---  
**Name** | **Description**  
`artifactName` |  `string`   
A fully-qualified path representing Artifact resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromBatchPredictionJobName(batchPredictionJobName)
    
    
    matchLocationFromBatchPredictionJobName(batchPredictionJobName: string): string | number;

Parse the location from BatchPredictionJob resource.

**Parameter**  
---  
**Name** | **Description**  
`batchPredictionJobName` |  `string`   
A fully-qualified path representing BatchPredictionJob resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromCachedContentName(cachedContentName)
    
    
    matchLocationFromCachedContentName(cachedContentName: string): string | number;

Parse the location from CachedContent resource.

**Parameter**  
---  
**Name** | **Description**  
`cachedContentName` |  `string`   
A fully-qualified path representing CachedContent resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromContextName(contextName)
    
    
    matchLocationFromContextName(contextName: string): string | number;

Parse the location from Context resource.

**Parameter**  
---  
**Name** | **Description**  
`contextName` |  `string`   
A fully-qualified path representing Context resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromCustomJobName(customJobName)
    
    
    matchLocationFromCustomJobName(customJobName: string): string | number;

Parse the location from CustomJob resource.

**Parameter**  
---  
**Name** | **Description**  
`customJobName` |  `string`   
A fully-qualified path representing CustomJob resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromDataItemName(dataItemName)
    
    
    matchLocationFromDataItemName(dataItemName: string): string | number;

Parse the location from DataItem resource.

**Parameter**  
---  
**Name** | **Description**  
`dataItemName` |  `string`   
A fully-qualified path representing DataItem resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromDataLabelingJobName(dataLabelingJobName)
    
    
    matchLocationFromDataLabelingJobName(dataLabelingJobName: string): string | number;

Parse the location from DataLabelingJob resource.

**Parameter**  
---  
**Name** | **Description**  
`dataLabelingJobName` |  `string`   
A fully-qualified path representing DataLabelingJob resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromDatasetName(datasetName)
    
    
    matchLocationFromDatasetName(datasetName: string): string | number;

Parse the location from Dataset resource.

**Parameter**  
---  
**Name** | **Description**  
`datasetName` |  `string`   
A fully-qualified path representing Dataset resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromDatasetVersionName(datasetVersionName)
    
    
    matchLocationFromDatasetVersionName(datasetVersionName: string): string | number;

Parse the location from DatasetVersion resource.

**Parameter**  
---  
**Name** | **Description**  
`datasetVersionName` |  `string`   
A fully-qualified path representing DatasetVersion resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromDeploymentResourcePoolName(deploymentResourcePoolName)
    
    
    matchLocationFromDeploymentResourcePoolName(deploymentResourcePoolName: string): string | number;

Parse the location from DeploymentResourcePool resource.

**Parameter**  
---  
**Name** | **Description**  
`deploymentResourcePoolName` |  `string`   
A fully-qualified path representing DeploymentResourcePool resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromEntityTypeName(entityTypeName)
    
    
    matchLocationFromEntityTypeName(entityTypeName: string): string | number;

Parse the location from EntityType resource.

**Parameter**  
---  
**Name** | **Description**  
`entityTypeName` |  `string`   
A fully-qualified path representing EntityType resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromExampleStoreName(exampleStoreName)
    
    
    matchLocationFromExampleStoreName(exampleStoreName: string): string | number;

Parse the location from ExampleStore resource.

**Parameter**  
---  
**Name** | **Description**  
`exampleStoreName` |  `string`   
A fully-qualified path representing ExampleStore resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromExecutionName(executionName)
    
    
    matchLocationFromExecutionName(executionName: string): string | number;

Parse the location from Execution resource.

**Parameter**  
---  
**Name** | **Description**  
`executionName` |  `string`   
A fully-qualified path representing Execution resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromExtensionName(extensionName)
    
    
    matchLocationFromExtensionName(extensionName: string): string | number;

Parse the location from Extension resource.

**Parameter**  
---  
**Name** | **Description**  
`extensionName` |  `string`   
A fully-qualified path representing Extension resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromFeatureGroupName(featureGroupName)
    
    
    matchLocationFromFeatureGroupName(featureGroupName: string): string | number;

Parse the location from FeatureGroup resource.

**Parameter**  
---  
**Name** | **Description**  
`featureGroupName` |  `string`   
A fully-qualified path representing FeatureGroup resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromFeatureMonitorJobName(featureMonitorJobName)
    
    
    matchLocationFromFeatureMonitorJobName(featureMonitorJobName: string): string | number;

Parse the location from FeatureMonitorJob resource.

**Parameter**  
---  
**Name** | **Description**  
`featureMonitorJobName` |  `string`   
A fully-qualified path representing FeatureMonitorJob resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromFeatureMonitorName(featureMonitorName)
    
    
    matchLocationFromFeatureMonitorName(featureMonitorName: string): string | number;

Parse the location from FeatureMonitor resource.

**Parameter**  
---  
**Name** | **Description**  
`featureMonitorName` |  `string`   
A fully-qualified path representing FeatureMonitor resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromFeatureOnlineStoreName(featureOnlineStoreName)
    
    
    matchLocationFromFeatureOnlineStoreName(featureOnlineStoreName: string): string | number;

Parse the location from FeatureOnlineStore resource.

**Parameter**  
---  
**Name** | **Description**  
`featureOnlineStoreName` |  `string`   
A fully-qualified path representing FeatureOnlineStore resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromFeaturestoreName(featurestoreName)
    
    
    matchLocationFromFeaturestoreName(featurestoreName: string): string | number;

Parse the location from Featurestore resource.

**Parameter**  
---  
**Name** | **Description**  
`featurestoreName` |  `string`   
A fully-qualified path representing Featurestore resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromFeatureViewName(featureViewName)
    
    
    matchLocationFromFeatureViewName(featureViewName: string): string | number;

Parse the location from FeatureView resource.

**Parameter**  
---  
**Name** | **Description**  
`featureViewName` |  `string`   
A fully-qualified path representing FeatureView resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromFeatureViewSyncName(featureViewSyncName)
    
    
    matchLocationFromFeatureViewSyncName(featureViewSyncName: string): string | number;

Parse the location from FeatureViewSync resource.

**Parameter**  
---  
**Name** | **Description**  
`featureViewSyncName` |  `string`   
A fully-qualified path representing FeatureViewSync resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromHyperparameterTuningJobName(hyperparameterTuningJobName)
    
    
    matchLocationFromHyperparameterTuningJobName(hyperparameterTuningJobName: string): string | number;

Parse the location from HyperparameterTuningJob resource.

**Parameter**  
---  
**Name** | **Description**  
`hyperparameterTuningJobName` |  `string`   
A fully-qualified path representing HyperparameterTuningJob resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromIndexEndpointName(indexEndpointName)
    
    
    matchLocationFromIndexEndpointName(indexEndpointName: string): string | number;

Parse the location from IndexEndpoint resource.

**Parameter**  
---  
**Name** | **Description**  
`indexEndpointName` |  `string`   
A fully-qualified path representing IndexEndpoint resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromIndexName(indexName)
    
    
    matchLocationFromIndexName(indexName: string): string | number;

Parse the location from Index resource.

**Parameter**  
---  
**Name** | **Description**  
`indexName` |  `string`   
A fully-qualified path representing Index resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromLocationName(locationName)
    
    
    matchLocationFromLocationName(locationName: string): string | number;

Parse the location from Location resource.

**Parameter**  
---  
**Name** | **Description**  
`locationName` |  `string`   
A fully-qualified path representing Location resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromMemoryName(memoryName)
    
    
    matchLocationFromMemoryName(memoryName: string): string | number;

Parse the location from Memory resource.

**Parameter**  
---  
**Name** | **Description**  
`memoryName` |  `string`   
A fully-qualified path representing Memory resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromMetadataSchemaName(metadataSchemaName)
    
    
    matchLocationFromMetadataSchemaName(metadataSchemaName: string): string | number;

Parse the location from MetadataSchema resource.

**Parameter**  
---  
**Name** | **Description**  
`metadataSchemaName` |  `string`   
A fully-qualified path representing MetadataSchema resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromMetadataStoreName(metadataStoreName)
    
    
    matchLocationFromMetadataStoreName(metadataStoreName: string): string | number;

Parse the location from MetadataStore resource.

**Parameter**  
---  
**Name** | **Description**  
`metadataStoreName` |  `string`   
A fully-qualified path representing MetadataStore resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromModelDeploymentMonitoringJobName(modelDeploymentMonitoringJobName)
    
    
    matchLocationFromModelDeploymentMonitoringJobName(modelDeploymentMonitoringJobName: string): string | number;

Parse the location from ModelDeploymentMonitoringJob resource.

**Parameter**  
---  
**Name** | **Description**  
`modelDeploymentMonitoringJobName` |  `string`   
A fully-qualified path representing ModelDeploymentMonitoringJob resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromModelEvaluationName(modelEvaluationName)
    
    
    matchLocationFromModelEvaluationName(modelEvaluationName: string): string | number;

Parse the location from ModelEvaluation resource.

**Parameter**  
---  
**Name** | **Description**  
`modelEvaluationName` |  `string`   
A fully-qualified path representing ModelEvaluation resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromModelEvaluationSliceName(modelEvaluationSliceName)
    
    
    matchLocationFromModelEvaluationSliceName(modelEvaluationSliceName: string): string | number;

Parse the location from ModelEvaluationSlice resource.

**Parameter**  
---  
**Name** | **Description**  
`modelEvaluationSliceName` |  `string`   
A fully-qualified path representing ModelEvaluationSlice resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromModelMonitoringJobName(modelMonitoringJobName)
    
    
    matchLocationFromModelMonitoringJobName(modelMonitoringJobName: string): string | number;

Parse the location from ModelMonitoringJob resource.

**Parameter**  
---  
**Name** | **Description**  
`modelMonitoringJobName` |  `string`   
A fully-qualified path representing ModelMonitoringJob resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromModelMonitorName(modelMonitorName)
    
    
    matchLocationFromModelMonitorName(modelMonitorName: string): string | number;

Parse the location from ModelMonitor resource.

**Parameter**  
---  
**Name** | **Description**  
`modelMonitorName` |  `string`   
A fully-qualified path representing ModelMonitor resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromModelName(modelName)
    
    
    matchLocationFromModelName(modelName: string): string | number;

Parse the location from Model resource.

**Parameter**  
---  
**Name** | **Description**  
`modelName` |  `string`   
A fully-qualified path representing Model resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromNasJobName(nasJobName)
    
    
    matchLocationFromNasJobName(nasJobName: string): string | number;

Parse the location from NasJob resource.

**Parameter**  
---  
**Name** | **Description**  
`nasJobName` |  `string`   
A fully-qualified path representing NasJob resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromNasTrialDetailName(nasTrialDetailName)
    
    
    matchLocationFromNasTrialDetailName(nasTrialDetailName: string): string | number;

Parse the location from NasTrialDetail resource.

**Parameter**  
---  
**Name** | **Description**  
`nasTrialDetailName` |  `string`   
A fully-qualified path representing NasTrialDetail resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromNotebookExecutionJobName(notebookExecutionJobName)
    
    
    matchLocationFromNotebookExecutionJobName(notebookExecutionJobName: string): string | number;

Parse the location from NotebookExecutionJob resource.

**Parameter**  
---  
**Name** | **Description**  
`notebookExecutionJobName` |  `string`   
A fully-qualified path representing NotebookExecutionJob resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromNotebookRuntimeName(notebookRuntimeName)
    
    
    matchLocationFromNotebookRuntimeName(notebookRuntimeName: string): string | number;

Parse the location from NotebookRuntime resource.

**Parameter**  
---  
**Name** | **Description**  
`notebookRuntimeName` |  `string`   
A fully-qualified path representing NotebookRuntime resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromNotebookRuntimeTemplateName(notebookRuntimeTemplateName)
    
    
    matchLocationFromNotebookRuntimeTemplateName(notebookRuntimeTemplateName: string): string | number;

Parse the location from NotebookRuntimeTemplate resource.

**Parameter**  
---  
**Name** | **Description**  
`notebookRuntimeTemplateName` |  `string`   
A fully-qualified path representing NotebookRuntimeTemplate resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromOnlineEvaluatorName(onlineEvaluatorName)
    
    
    matchLocationFromOnlineEvaluatorName(onlineEvaluatorName: string): string | number;

Parse the location from OnlineEvaluator resource.

**Parameter**  
---  
**Name** | **Description**  
`onlineEvaluatorName` |  `string`   
A fully-qualified path representing OnlineEvaluator resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromPersistentResourceName(persistentResourceName)
    
    
    matchLocationFromPersistentResourceName(persistentResourceName: string): string | number;

Parse the location from PersistentResource resource.

**Parameter**  
---  
**Name** | **Description**  
`persistentResourceName` |  `string`   
A fully-qualified path representing PersistentResource resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromPipelineJobName(pipelineJobName)
    
    
    matchLocationFromPipelineJobName(pipelineJobName: string): string | number;

Parse the location from PipelineJob resource.

**Parameter**  
---  
**Name** | **Description**  
`pipelineJobName` |  `string`   
A fully-qualified path representing PipelineJob resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromProjectLocationEndpointName(projectLocationEndpointName)
    
    
    matchLocationFromProjectLocationEndpointName(projectLocationEndpointName: string): string | number;

Parse the location from ProjectLocationEndpoint resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationEndpointName` |  `string`   
A fully-qualified path representing project_location_endpoint resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromProjectLocationFeatureGroupFeaturesName(projectLocationFeatureGroupFeaturesName)
    
    
    matchLocationFromProjectLocationFeatureGroupFeaturesName(projectLocationFeatureGroupFeaturesName: string): string | number;

Parse the location from ProjectLocationFeatureGroupFeatures resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationFeatureGroupFeaturesName` |  `string`   
A fully-qualified path representing project_location_feature_group_features resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromProjectLocationFeaturestoreEntityTypeFeaturesName(projectLocationFeaturestoreEntityTypeFeaturesName)
    
    
    matchLocationFromProjectLocationFeaturestoreEntityTypeFeaturesName(projectLocationFeaturestoreEntityTypeFeaturesName: string): string | number;

Parse the location from ProjectLocationFeaturestoreEntityTypeFeatures resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationFeaturestoreEntityTypeFeaturesName` |  `string`   
A fully-qualified path representing project_location_featurestore_entity_type_features resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromProjectLocationPublisherModelName(projectLocationPublisherModelName)
    
    
    matchLocationFromProjectLocationPublisherModelName(projectLocationPublisherModelName: string): string | number;

Parse the location from ProjectLocationPublisherModel resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationPublisherModelName` |  `string`   
A fully-qualified path representing project_location_publisher_model resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromRagCorpusName(ragCorpusName)
    
    
    matchLocationFromRagCorpusName(ragCorpusName: string): string | number;

Parse the location from RagCorpus resource.

**Parameter**  
---  
**Name** | **Description**  
`ragCorpusName` |  `string`   
A fully-qualified path representing RagCorpus resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromRagDataSchemaName(ragDataSchemaName)
    
    
    matchLocationFromRagDataSchemaName(ragDataSchemaName: string): string | number;

Parse the location from RagDataSchema resource.

**Parameter**  
---  
**Name** | **Description**  
`ragDataSchemaName` |  `string`   
A fully-qualified path representing RagDataSchema resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromRagEngineConfigName(ragEngineConfigName)
    
    
    matchLocationFromRagEngineConfigName(ragEngineConfigName: string): string | number;

Parse the location from RagEngineConfig resource.

**Parameter**  
---  
**Name** | **Description**  
`ragEngineConfigName` |  `string`   
A fully-qualified path representing RagEngineConfig resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromRagFileName(ragFileName)
    
    
    matchLocationFromRagFileName(ragFileName: string): string | number;

Parse the location from RagFile resource.

**Parameter**  
---  
**Name** | **Description**  
`ragFileName` |  `string`   
A fully-qualified path representing RagFile resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromRagMetadataName(ragMetadataName)
    
    
    matchLocationFromRagMetadataName(ragMetadataName: string): string | number;

Parse the location from RagMetadata resource.

**Parameter**  
---  
**Name** | **Description**  
`ragMetadataName` |  `string`   
A fully-qualified path representing RagMetadata resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromReasoningEngineName(reasoningEngineName)
    
    
    matchLocationFromReasoningEngineName(reasoningEngineName: string): string | number;

Parse the location from ReasoningEngine resource.

**Parameter**  
---  
**Name** | **Description**  
`reasoningEngineName` |  `string`   
A fully-qualified path representing ReasoningEngine resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromReasoningEngineRuntimeRevisionName(reasoningEngineRuntimeRevisionName)
    
    
    matchLocationFromReasoningEngineRuntimeRevisionName(reasoningEngineRuntimeRevisionName: string): string | number;

Parse the location from ReasoningEngineRuntimeRevision resource.

**Parameter**  
---  
**Name** | **Description**  
`reasoningEngineRuntimeRevisionName` |  `string`   
A fully-qualified path representing ReasoningEngineRuntimeRevision resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromSavedQueryName(savedQueryName)
    
    
    matchLocationFromSavedQueryName(savedQueryName: string): string | number;

Parse the location from SavedQuery resource.

**Parameter**  
---  
**Name** | **Description**  
`savedQueryName` |  `string`   
A fully-qualified path representing SavedQuery resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromScheduleName(scheduleName)
    
    
    matchLocationFromScheduleName(scheduleName: string): string | number;

Parse the location from Schedule resource.

**Parameter**  
---  
**Name** | **Description**  
`scheduleName` |  `string`   
A fully-qualified path representing Schedule resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromSessionEventName(sessionEventName)
    
    
    matchLocationFromSessionEventName(sessionEventName: string): string | number;

Parse the location from SessionEvent resource.

**Parameter**  
---  
**Name** | **Description**  
`sessionEventName` |  `string`   
A fully-qualified path representing SessionEvent resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromSessionName(sessionName)
    
    
    matchLocationFromSessionName(sessionName: string): string | number;

Parse the location from Session resource.

**Parameter**  
---  
**Name** | **Description**  
`sessionName` |  `string`   
A fully-qualified path representing Session resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromSpecialistPoolName(specialistPoolName)
    
    
    matchLocationFromSpecialistPoolName(specialistPoolName: string): string | number;

Parse the location from SpecialistPool resource.

**Parameter**  
---  
**Name** | **Description**  
`specialistPoolName` |  `string`   
A fully-qualified path representing SpecialistPool resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromStudyName(studyName)
    
    
    matchLocationFromStudyName(studyName: string): string | number;

Parse the location from Study resource.

**Parameter**  
---  
**Name** | **Description**  
`studyName` |  `string`   
A fully-qualified path representing Study resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromTensorboardExperimentName(tensorboardExperimentName)
    
    
    matchLocationFromTensorboardExperimentName(tensorboardExperimentName: string): string | number;

Parse the location from TensorboardExperiment resource.

**Parameter**  
---  
**Name** | **Description**  
`tensorboardExperimentName` |  `string`   
A fully-qualified path representing TensorboardExperiment resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromTensorboardName(tensorboardName)
    
    
    matchLocationFromTensorboardName(tensorboardName: string): string | number;

Parse the location from Tensorboard resource.

**Parameter**  
---  
**Name** | **Description**  
`tensorboardName` |  `string`   
A fully-qualified path representing Tensorboard resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromTensorboardRunName(tensorboardRunName)
    
    
    matchLocationFromTensorboardRunName(tensorboardRunName: string): string | number;

Parse the location from TensorboardRun resource.

**Parameter**  
---  
**Name** | **Description**  
`tensorboardRunName` |  `string`   
A fully-qualified path representing TensorboardRun resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromTensorboardTimeSeriesName(tensorboardTimeSeriesName)
    
    
    matchLocationFromTensorboardTimeSeriesName(tensorboardTimeSeriesName: string): string | number;

Parse the location from TensorboardTimeSeries resource.

**Parameter**  
---  
**Name** | **Description**  
`tensorboardTimeSeriesName` |  `string`   
A fully-qualified path representing TensorboardTimeSeries resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromTrainingPipelineName(trainingPipelineName)
    
    
    matchLocationFromTrainingPipelineName(trainingPipelineName: string): string | number;

Parse the location from TrainingPipeline resource.

**Parameter**  
---  
**Name** | **Description**  
`trainingPipelineName` |  `string`   
A fully-qualified path representing TrainingPipeline resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromTrialName(trialName)
    
    
    matchLocationFromTrialName(trialName: string): string | number;

Parse the location from Trial resource.

**Parameter**  
---  
**Name** | **Description**  
`trialName` |  `string`   
A fully-qualified path representing Trial resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromTuningJobName(tuningJobName)
    
    
    matchLocationFromTuningJobName(tuningJobName: string): string | number;

Parse the location from TuningJob resource.

**Parameter**  
---  
**Name** | **Description**  
`tuningJobName` |  `string`   
A fully-qualified path representing TuningJob resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchMemoryFromMemoryName(memoryName)
    
    
    matchMemoryFromMemoryName(memoryName: string): string | number;

Parse the memory from Memory resource.

**Parameter**  
---  
**Name** | **Description**  
`memoryName` |  `string`   
A fully-qualified path representing Memory resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the memory.  
  
### matchMetadataSchemaFromMetadataSchemaName(metadataSchemaName)
    
    
    matchMetadataSchemaFromMetadataSchemaName(metadataSchemaName: string): string | number;

Parse the metadata_schema from MetadataSchema resource.

**Parameter**  
---  
**Name** | **Description**  
`metadataSchemaName` |  `string`   
A fully-qualified path representing MetadataSchema resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the metadata_schema.  
  
### matchMetadataStoreFromArtifactName(artifactName)
    
    
    matchMetadataStoreFromArtifactName(artifactName: string): string | number;

Parse the metadata_store from Artifact resource.

**Parameter**  
---  
**Name** | **Description**  
`artifactName` |  `string`   
A fully-qualified path representing Artifact resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the metadata_store.  
  
### matchMetadataStoreFromContextName(contextName)
    
    
    matchMetadataStoreFromContextName(contextName: string): string | number;

Parse the metadata_store from Context resource.

**Parameter**  
---  
**Name** | **Description**  
`contextName` |  `string`   
A fully-qualified path representing Context resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the metadata_store.  
  
### matchMetadataStoreFromExecutionName(executionName)
    
    
    matchMetadataStoreFromExecutionName(executionName: string): string | number;

Parse the metadata_store from Execution resource.

**Parameter**  
---  
**Name** | **Description**  
`executionName` |  `string`   
A fully-qualified path representing Execution resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the metadata_store.  
  
### matchMetadataStoreFromMetadataSchemaName(metadataSchemaName)
    
    
    matchMetadataStoreFromMetadataSchemaName(metadataSchemaName: string): string | number;

Parse the metadata_store from MetadataSchema resource.

**Parameter**  
---  
**Name** | **Description**  
`metadataSchemaName` |  `string`   
A fully-qualified path representing MetadataSchema resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the metadata_store.  
  
### matchMetadataStoreFromMetadataStoreName(metadataStoreName)
    
    
    matchMetadataStoreFromMetadataStoreName(metadataStoreName: string): string | number;

Parse the metadata_store from MetadataStore resource.

**Parameter**  
---  
**Name** | **Description**  
`metadataStoreName` |  `string`   
A fully-qualified path representing MetadataStore resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the metadata_store.  
  
### matchModelDeploymentMonitoringJobFromModelDeploymentMonitoringJobName(modelDeploymentMonitoringJobName)
    
    
    matchModelDeploymentMonitoringJobFromModelDeploymentMonitoringJobName(modelDeploymentMonitoringJobName: string): string | number;

Parse the model_deployment_monitoring_job from ModelDeploymentMonitoringJob resource.

**Parameter**  
---  
**Name** | **Description**  
`modelDeploymentMonitoringJobName` |  `string`   
A fully-qualified path representing ModelDeploymentMonitoringJob resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the model_deployment_monitoring_job.  
  
### matchModelFromModelEvaluationName(modelEvaluationName)
    
    
    matchModelFromModelEvaluationName(modelEvaluationName: string): string | number;

Parse the model from ModelEvaluation resource.

**Parameter**  
---  
**Name** | **Description**  
`modelEvaluationName` |  `string`   
A fully-qualified path representing ModelEvaluation resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the model.  
  
### matchModelFromModelEvaluationSliceName(modelEvaluationSliceName)
    
    
    matchModelFromModelEvaluationSliceName(modelEvaluationSliceName: string): string | number;

Parse the model from ModelEvaluationSlice resource.

**Parameter**  
---  
**Name** | **Description**  
`modelEvaluationSliceName` |  `string`   
A fully-qualified path representing ModelEvaluationSlice resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the model.  
  
### matchModelFromModelName(modelName)
    
    
    matchModelFromModelName(modelName: string): string | number;

Parse the model from Model resource.

**Parameter**  
---  
**Name** | **Description**  
`modelName` |  `string`   
A fully-qualified path representing Model resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the model.  
  
### matchModelFromProjectLocationPublisherModelName(projectLocationPublisherModelName)
    
    
    matchModelFromProjectLocationPublisherModelName(projectLocationPublisherModelName: string): string | number;

Parse the model from ProjectLocationPublisherModel resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationPublisherModelName` |  `string`   
A fully-qualified path representing project_location_publisher_model resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the model.  
  
### matchModelFromPublisherModelName(publisherModelName)
    
    
    matchModelFromPublisherModelName(publisherModelName: string): string | number;

Parse the model from PublisherModel resource.

**Parameter**  
---  
**Name** | **Description**  
`publisherModelName` |  `string`   
A fully-qualified path representing PublisherModel resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the model.  
  
### matchModelMonitorFromModelMonitoringJobName(modelMonitoringJobName)
    
    
    matchModelMonitorFromModelMonitoringJobName(modelMonitoringJobName: string): string | number;

Parse the model_monitor from ModelMonitoringJob resource.

**Parameter**  
---  
**Name** | **Description**  
`modelMonitoringJobName` |  `string`   
A fully-qualified path representing ModelMonitoringJob resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the model_monitor.  
  
### matchModelMonitorFromModelMonitorName(modelMonitorName)
    
    
    matchModelMonitorFromModelMonitorName(modelMonitorName: string): string | number;

Parse the model_monitor from ModelMonitor resource.

**Parameter**  
---  
**Name** | **Description**  
`modelMonitorName` |  `string`   
A fully-qualified path representing ModelMonitor resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the model_monitor.  
  
### matchModelMonitoringJobFromModelMonitoringJobName(modelMonitoringJobName)
    
    
    matchModelMonitoringJobFromModelMonitoringJobName(modelMonitoringJobName: string): string | number;

Parse the model_monitoring_job from ModelMonitoringJob resource.

**Parameter**  
---  
**Name** | **Description**  
`modelMonitoringJobName` |  `string`   
A fully-qualified path representing ModelMonitoringJob resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the model_monitoring_job.  
  
### matchNasJobFromNasJobName(nasJobName)
    
    
    matchNasJobFromNasJobName(nasJobName: string): string | number;

Parse the nas_job from NasJob resource.

**Parameter**  
---  
**Name** | **Description**  
`nasJobName` |  `string`   
A fully-qualified path representing NasJob resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the nas_job.  
  
### matchNasJobFromNasTrialDetailName(nasTrialDetailName)
    
    
    matchNasJobFromNasTrialDetailName(nasTrialDetailName: string): string | number;

Parse the nas_job from NasTrialDetail resource.

**Parameter**  
---  
**Name** | **Description**  
`nasTrialDetailName` |  `string`   
A fully-qualified path representing NasTrialDetail resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the nas_job.  
  
### matchNasTrialDetailFromNasTrialDetailName(nasTrialDetailName)
    
    
    matchNasTrialDetailFromNasTrialDetailName(nasTrialDetailName: string): string | number;

Parse the nas_trial_detail from NasTrialDetail resource.

**Parameter**  
---  
**Name** | **Description**  
`nasTrialDetailName` |  `string`   
A fully-qualified path representing NasTrialDetail resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the nas_trial_detail.  
  
### matchNotebookExecutionJobFromNotebookExecutionJobName(notebookExecutionJobName)
    
    
    matchNotebookExecutionJobFromNotebookExecutionJobName(notebookExecutionJobName: string): string | number;

Parse the notebook_execution_job from NotebookExecutionJob resource.

**Parameter**  
---  
**Name** | **Description**  
`notebookExecutionJobName` |  `string`   
A fully-qualified path representing NotebookExecutionJob resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the notebook_execution_job.  
  
### matchNotebookRuntimeFromNotebookRuntimeName(notebookRuntimeName)
    
    
    matchNotebookRuntimeFromNotebookRuntimeName(notebookRuntimeName: string): string | number;

Parse the notebook_runtime from NotebookRuntime resource.

**Parameter**  
---  
**Name** | **Description**  
`notebookRuntimeName` |  `string`   
A fully-qualified path representing NotebookRuntime resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the notebook_runtime.  
  
### matchNotebookRuntimeTemplateFromNotebookRuntimeTemplateName(notebookRuntimeTemplateName)
    
    
    matchNotebookRuntimeTemplateFromNotebookRuntimeTemplateName(notebookRuntimeTemplateName: string): string | number;

Parse the notebook_runtime_template from NotebookRuntimeTemplate resource.

**Parameter**  
---  
**Name** | **Description**  
`notebookRuntimeTemplateName` |  `string`   
A fully-qualified path representing NotebookRuntimeTemplate resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the notebook_runtime_template.  
  
### matchOnlineEvaluatorFromOnlineEvaluatorName(onlineEvaluatorName)
    
    
    matchOnlineEvaluatorFromOnlineEvaluatorName(onlineEvaluatorName: string): string | number;

Parse the online_evaluator from OnlineEvaluator resource.

**Parameter**  
---  
**Name** | **Description**  
`onlineEvaluatorName` |  `string`   
A fully-qualified path representing OnlineEvaluator resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the online_evaluator.  
  
### matchPersistentResourceFromPersistentResourceName(persistentResourceName)
    
    
    matchPersistentResourceFromPersistentResourceName(persistentResourceName: string): string | number;

Parse the persistent_resource from PersistentResource resource.

**Parameter**  
---  
**Name** | **Description**  
`persistentResourceName` |  `string`   
A fully-qualified path representing PersistentResource resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the persistent_resource.  
  
### matchPipelineJobFromPipelineJobName(pipelineJobName)
    
    
    matchPipelineJobFromPipelineJobName(pipelineJobName: string): string | number;

Parse the pipeline_job from PipelineJob resource.

**Parameter**  
---  
**Name** | **Description**  
`pipelineJobName` |  `string`   
A fully-qualified path representing PipelineJob resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the pipeline_job.  
  
### matchProjectFromAnnotationName(annotationName)
    
    
    matchProjectFromAnnotationName(annotationName: string): string | number;

Parse the project from Annotation resource.

**Parameter**  
---  
**Name** | **Description**  
`annotationName` |  `string`   
A fully-qualified path representing Annotation resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromAnnotationSpecName(annotationSpecName)
    
    
    matchProjectFromAnnotationSpecName(annotationSpecName: string): string | number;

Parse the project from AnnotationSpec resource.

**Parameter**  
---  
**Name** | **Description**  
`annotationSpecName` |  `string`   
A fully-qualified path representing AnnotationSpec resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromArtifactName(artifactName)
    
    
    matchProjectFromArtifactName(artifactName: string): string | number;

Parse the project from Artifact resource.

**Parameter**  
---  
**Name** | **Description**  
`artifactName` |  `string`   
A fully-qualified path representing Artifact resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromBatchPredictionJobName(batchPredictionJobName)
    
    
    matchProjectFromBatchPredictionJobName(batchPredictionJobName: string): string | number;

Parse the project from BatchPredictionJob resource.

**Parameter**  
---  
**Name** | **Description**  
`batchPredictionJobName` |  `string`   
A fully-qualified path representing BatchPredictionJob resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromCachedContentName(cachedContentName)
    
    
    matchProjectFromCachedContentName(cachedContentName: string): string | number;

Parse the project from CachedContent resource.

**Parameter**  
---  
**Name** | **Description**  
`cachedContentName` |  `string`   
A fully-qualified path representing CachedContent resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromContextName(contextName)
    
    
    matchProjectFromContextName(contextName: string): string | number;

Parse the project from Context resource.

**Parameter**  
---  
**Name** | **Description**  
`contextName` |  `string`   
A fully-qualified path representing Context resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromCustomJobName(customJobName)
    
    
    matchProjectFromCustomJobName(customJobName: string): string | number;

Parse the project from CustomJob resource.

**Parameter**  
---  
**Name** | **Description**  
`customJobName` |  `string`   
A fully-qualified path representing CustomJob resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromDataItemName(dataItemName)
    
    
    matchProjectFromDataItemName(dataItemName: string): string | number;

Parse the project from DataItem resource.

**Parameter**  
---  
**Name** | **Description**  
`dataItemName` |  `string`   
A fully-qualified path representing DataItem resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromDataLabelingJobName(dataLabelingJobName)
    
    
    matchProjectFromDataLabelingJobName(dataLabelingJobName: string): string | number;

Parse the project from DataLabelingJob resource.

**Parameter**  
---  
**Name** | **Description**  
`dataLabelingJobName` |  `string`   
A fully-qualified path representing DataLabelingJob resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromDatasetName(datasetName)
    
    
    matchProjectFromDatasetName(datasetName: string): string | number;

Parse the project from Dataset resource.

**Parameter**  
---  
**Name** | **Description**  
`datasetName` |  `string`   
A fully-qualified path representing Dataset resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromDatasetVersionName(datasetVersionName)
    
    
    matchProjectFromDatasetVersionName(datasetVersionName: string): string | number;

Parse the project from DatasetVersion resource.

**Parameter**  
---  
**Name** | **Description**  
`datasetVersionName` |  `string`   
A fully-qualified path representing DatasetVersion resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromDeploymentResourcePoolName(deploymentResourcePoolName)
    
    
    matchProjectFromDeploymentResourcePoolName(deploymentResourcePoolName: string): string | number;

Parse the project from DeploymentResourcePool resource.

**Parameter**  
---  
**Name** | **Description**  
`deploymentResourcePoolName` |  `string`   
A fully-qualified path representing DeploymentResourcePool resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromEntityTypeName(entityTypeName)
    
    
    matchProjectFromEntityTypeName(entityTypeName: string): string | number;

Parse the project from EntityType resource.

**Parameter**  
---  
**Name** | **Description**  
`entityTypeName` |  `string`   
A fully-qualified path representing EntityType resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromExampleStoreName(exampleStoreName)
    
    
    matchProjectFromExampleStoreName(exampleStoreName: string): string | number;

Parse the project from ExampleStore resource.

**Parameter**  
---  
**Name** | **Description**  
`exampleStoreName` |  `string`   
A fully-qualified path representing ExampleStore resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromExecutionName(executionName)
    
    
    matchProjectFromExecutionName(executionName: string): string | number;

Parse the project from Execution resource.

**Parameter**  
---  
**Name** | **Description**  
`executionName` |  `string`   
A fully-qualified path representing Execution resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromExtensionName(extensionName)
    
    
    matchProjectFromExtensionName(extensionName: string): string | number;

Parse the project from Extension resource.

**Parameter**  
---  
**Name** | **Description**  
`extensionName` |  `string`   
A fully-qualified path representing Extension resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromFeatureGroupName(featureGroupName)
    
    
    matchProjectFromFeatureGroupName(featureGroupName: string): string | number;

Parse the project from FeatureGroup resource.

**Parameter**  
---  
**Name** | **Description**  
`featureGroupName` |  `string`   
A fully-qualified path representing FeatureGroup resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromFeatureMonitorJobName(featureMonitorJobName)
    
    
    matchProjectFromFeatureMonitorJobName(featureMonitorJobName: string): string | number;

Parse the project from FeatureMonitorJob resource.

**Parameter**  
---  
**Name** | **Description**  
`featureMonitorJobName` |  `string`   
A fully-qualified path representing FeatureMonitorJob resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromFeatureMonitorName(featureMonitorName)
    
    
    matchProjectFromFeatureMonitorName(featureMonitorName: string): string | number;

Parse the project from FeatureMonitor resource.

**Parameter**  
---  
**Name** | **Description**  
`featureMonitorName` |  `string`   
A fully-qualified path representing FeatureMonitor resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromFeatureOnlineStoreName(featureOnlineStoreName)
    
    
    matchProjectFromFeatureOnlineStoreName(featureOnlineStoreName: string): string | number;

Parse the project from FeatureOnlineStore resource.

**Parameter**  
---  
**Name** | **Description**  
`featureOnlineStoreName` |  `string`   
A fully-qualified path representing FeatureOnlineStore resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromFeaturestoreName(featurestoreName)
    
    
    matchProjectFromFeaturestoreName(featurestoreName: string): string | number;

Parse the project from Featurestore resource.

**Parameter**  
---  
**Name** | **Description**  
`featurestoreName` |  `string`   
A fully-qualified path representing Featurestore resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromFeatureViewName(featureViewName)
    
    
    matchProjectFromFeatureViewName(featureViewName: string): string | number;

Parse the project from FeatureView resource.

**Parameter**  
---  
**Name** | **Description**  
`featureViewName` |  `string`   
A fully-qualified path representing FeatureView resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromFeatureViewSyncName(featureViewSyncName)
    
    
    matchProjectFromFeatureViewSyncName(featureViewSyncName: string): string | number;

Parse the project from FeatureViewSync resource.

**Parameter**  
---  
**Name** | **Description**  
`featureViewSyncName` |  `string`   
A fully-qualified path representing FeatureViewSync resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromHyperparameterTuningJobName(hyperparameterTuningJobName)
    
    
    matchProjectFromHyperparameterTuningJobName(hyperparameterTuningJobName: string): string | number;

Parse the project from HyperparameterTuningJob resource.

**Parameter**  
---  
**Name** | **Description**  
`hyperparameterTuningJobName` |  `string`   
A fully-qualified path representing HyperparameterTuningJob resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromIndexEndpointName(indexEndpointName)
    
    
    matchProjectFromIndexEndpointName(indexEndpointName: string): string | number;

Parse the project from IndexEndpoint resource.

**Parameter**  
---  
**Name** | **Description**  
`indexEndpointName` |  `string`   
A fully-qualified path representing IndexEndpoint resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromIndexName(indexName)
    
    
    matchProjectFromIndexName(indexName: string): string | number;

Parse the project from Index resource.

**Parameter**  
---  
**Name** | **Description**  
`indexName` |  `string`   
A fully-qualified path representing Index resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromLocationName(locationName)
    
    
    matchProjectFromLocationName(locationName: string): string | number;

Parse the project from Location resource.

**Parameter**  
---  
**Name** | **Description**  
`locationName` |  `string`   
A fully-qualified path representing Location resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromMemoryName(memoryName)
    
    
    matchProjectFromMemoryName(memoryName: string): string | number;

Parse the project from Memory resource.

**Parameter**  
---  
**Name** | **Description**  
`memoryName` |  `string`   
A fully-qualified path representing Memory resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromMetadataSchemaName(metadataSchemaName)
    
    
    matchProjectFromMetadataSchemaName(metadataSchemaName: string): string | number;

Parse the project from MetadataSchema resource.

**Parameter**  
---  
**Name** | **Description**  
`metadataSchemaName` |  `string`   
A fully-qualified path representing MetadataSchema resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromMetadataStoreName(metadataStoreName)
    
    
    matchProjectFromMetadataStoreName(metadataStoreName: string): string | number;

Parse the project from MetadataStore resource.

**Parameter**  
---  
**Name** | **Description**  
`metadataStoreName` |  `string`   
A fully-qualified path representing MetadataStore resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromModelDeploymentMonitoringJobName(modelDeploymentMonitoringJobName)
    
    
    matchProjectFromModelDeploymentMonitoringJobName(modelDeploymentMonitoringJobName: string): string | number;

Parse the project from ModelDeploymentMonitoringJob resource.

**Parameter**  
---  
**Name** | **Description**  
`modelDeploymentMonitoringJobName` |  `string`   
A fully-qualified path representing ModelDeploymentMonitoringJob resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromModelEvaluationName(modelEvaluationName)
    
    
    matchProjectFromModelEvaluationName(modelEvaluationName: string): string | number;

Parse the project from ModelEvaluation resource.

**Parameter**  
---  
**Name** | **Description**  
`modelEvaluationName` |  `string`   
A fully-qualified path representing ModelEvaluation resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromModelEvaluationSliceName(modelEvaluationSliceName)
    
    
    matchProjectFromModelEvaluationSliceName(modelEvaluationSliceName: string): string | number;

Parse the project from ModelEvaluationSlice resource.

**Parameter**  
---  
**Name** | **Description**  
`modelEvaluationSliceName` |  `string`   
A fully-qualified path representing ModelEvaluationSlice resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromModelMonitoringJobName(modelMonitoringJobName)
    
    
    matchProjectFromModelMonitoringJobName(modelMonitoringJobName: string): string | number;

Parse the project from ModelMonitoringJob resource.

**Parameter**  
---  
**Name** | **Description**  
`modelMonitoringJobName` |  `string`   
A fully-qualified path representing ModelMonitoringJob resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromModelMonitorName(modelMonitorName)
    
    
    matchProjectFromModelMonitorName(modelMonitorName: string): string | number;

Parse the project from ModelMonitor resource.

**Parameter**  
---  
**Name** | **Description**  
`modelMonitorName` |  `string`   
A fully-qualified path representing ModelMonitor resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromModelName(modelName)
    
    
    matchProjectFromModelName(modelName: string): string | number;

Parse the project from Model resource.

**Parameter**  
---  
**Name** | **Description**  
`modelName` |  `string`   
A fully-qualified path representing Model resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromNasJobName(nasJobName)
    
    
    matchProjectFromNasJobName(nasJobName: string): string | number;

Parse the project from NasJob resource.

**Parameter**  
---  
**Name** | **Description**  
`nasJobName` |  `string`   
A fully-qualified path representing NasJob resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromNasTrialDetailName(nasTrialDetailName)
    
    
    matchProjectFromNasTrialDetailName(nasTrialDetailName: string): string | number;

Parse the project from NasTrialDetail resource.

**Parameter**  
---  
**Name** | **Description**  
`nasTrialDetailName` |  `string`   
A fully-qualified path representing NasTrialDetail resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromNotebookExecutionJobName(notebookExecutionJobName)
    
    
    matchProjectFromNotebookExecutionJobName(notebookExecutionJobName: string): string | number;

Parse the project from NotebookExecutionJob resource.

**Parameter**  
---  
**Name** | **Description**  
`notebookExecutionJobName` |  `string`   
A fully-qualified path representing NotebookExecutionJob resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromNotebookRuntimeName(notebookRuntimeName)
    
    
    matchProjectFromNotebookRuntimeName(notebookRuntimeName: string): string | number;

Parse the project from NotebookRuntime resource.

**Parameter**  
---  
**Name** | **Description**  
`notebookRuntimeName` |  `string`   
A fully-qualified path representing NotebookRuntime resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromNotebookRuntimeTemplateName(notebookRuntimeTemplateName)
    
    
    matchProjectFromNotebookRuntimeTemplateName(notebookRuntimeTemplateName: string): string | number;

Parse the project from NotebookRuntimeTemplate resource.

**Parameter**  
---  
**Name** | **Description**  
`notebookRuntimeTemplateName` |  `string`   
A fully-qualified path representing NotebookRuntimeTemplate resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromOnlineEvaluatorName(onlineEvaluatorName)
    
    
    matchProjectFromOnlineEvaluatorName(onlineEvaluatorName: string): string | number;

Parse the project from OnlineEvaluator resource.

**Parameter**  
---  
**Name** | **Description**  
`onlineEvaluatorName` |  `string`   
A fully-qualified path representing OnlineEvaluator resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromPersistentResourceName(persistentResourceName)
    
    
    matchProjectFromPersistentResourceName(persistentResourceName: string): string | number;

Parse the project from PersistentResource resource.

**Parameter**  
---  
**Name** | **Description**  
`persistentResourceName` |  `string`   
A fully-qualified path representing PersistentResource resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromPipelineJobName(pipelineJobName)
    
    
    matchProjectFromPipelineJobName(pipelineJobName: string): string | number;

Parse the project from PipelineJob resource.

**Parameter**  
---  
**Name** | **Description**  
`pipelineJobName` |  `string`   
A fully-qualified path representing PipelineJob resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromProjectLocationEndpointName(projectLocationEndpointName)
    
    
    matchProjectFromProjectLocationEndpointName(projectLocationEndpointName: string): string | number;

Parse the project from ProjectLocationEndpoint resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationEndpointName` |  `string`   
A fully-qualified path representing project_location_endpoint resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromProjectLocationFeatureGroupFeaturesName(projectLocationFeatureGroupFeaturesName)
    
    
    matchProjectFromProjectLocationFeatureGroupFeaturesName(projectLocationFeatureGroupFeaturesName: string): string | number;

Parse the project from ProjectLocationFeatureGroupFeatures resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationFeatureGroupFeaturesName` |  `string`   
A fully-qualified path representing project_location_feature_group_features resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromProjectLocationFeaturestoreEntityTypeFeaturesName(projectLocationFeaturestoreEntityTypeFeaturesName)
    
    
    matchProjectFromProjectLocationFeaturestoreEntityTypeFeaturesName(projectLocationFeaturestoreEntityTypeFeaturesName: string): string | number;

Parse the project from ProjectLocationFeaturestoreEntityTypeFeatures resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationFeaturestoreEntityTypeFeaturesName` |  `string`   
A fully-qualified path representing project_location_featurestore_entity_type_features resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromProjectLocationPublisherModelName(projectLocationPublisherModelName)
    
    
    matchProjectFromProjectLocationPublisherModelName(projectLocationPublisherModelName: string): string | number;

Parse the project from ProjectLocationPublisherModel resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationPublisherModelName` |  `string`   
A fully-qualified path representing project_location_publisher_model resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromRagCorpusName(ragCorpusName)
    
    
    matchProjectFromRagCorpusName(ragCorpusName: string): string | number;

Parse the project from RagCorpus resource.

**Parameter**  
---  
**Name** | **Description**  
`ragCorpusName` |  `string`   
A fully-qualified path representing RagCorpus resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromRagDataSchemaName(ragDataSchemaName)
    
    
    matchProjectFromRagDataSchemaName(ragDataSchemaName: string): string | number;

Parse the project from RagDataSchema resource.

**Parameter**  
---  
**Name** | **Description**  
`ragDataSchemaName` |  `string`   
A fully-qualified path representing RagDataSchema resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromRagEngineConfigName(ragEngineConfigName)
    
    
    matchProjectFromRagEngineConfigName(ragEngineConfigName: string): string | number;

Parse the project from RagEngineConfig resource.

**Parameter**  
---  
**Name** | **Description**  
`ragEngineConfigName` |  `string`   
A fully-qualified path representing RagEngineConfig resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromRagFileName(ragFileName)
    
    
    matchProjectFromRagFileName(ragFileName: string): string | number;

Parse the project from RagFile resource.

**Parameter**  
---  
**Name** | **Description**  
`ragFileName` |  `string`   
A fully-qualified path representing RagFile resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromRagMetadataName(ragMetadataName)
    
    
    matchProjectFromRagMetadataName(ragMetadataName: string): string | number;

Parse the project from RagMetadata resource.

**Parameter**  
---  
**Name** | **Description**  
`ragMetadataName` |  `string`   
A fully-qualified path representing RagMetadata resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromReasoningEngineName(reasoningEngineName)
    
    
    matchProjectFromReasoningEngineName(reasoningEngineName: string): string | number;

Parse the project from ReasoningEngine resource.

**Parameter**  
---  
**Name** | **Description**  
`reasoningEngineName` |  `string`   
A fully-qualified path representing ReasoningEngine resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromReasoningEngineRuntimeRevisionName(reasoningEngineRuntimeRevisionName)
    
    
    matchProjectFromReasoningEngineRuntimeRevisionName(reasoningEngineRuntimeRevisionName: string): string | number;

Parse the project from ReasoningEngineRuntimeRevision resource.

**Parameter**  
---  
**Name** | **Description**  
`reasoningEngineRuntimeRevisionName` |  `string`   
A fully-qualified path representing ReasoningEngineRuntimeRevision resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromSavedQueryName(savedQueryName)
    
    
    matchProjectFromSavedQueryName(savedQueryName: string): string | number;

Parse the project from SavedQuery resource.

**Parameter**  
---  
**Name** | **Description**  
`savedQueryName` |  `string`   
A fully-qualified path representing SavedQuery resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromScheduleName(scheduleName)
    
    
    matchProjectFromScheduleName(scheduleName: string): string | number;

Parse the project from Schedule resource.

**Parameter**  
---  
**Name** | **Description**  
`scheduleName` |  `string`   
A fully-qualified path representing Schedule resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromSessionEventName(sessionEventName)
    
    
    matchProjectFromSessionEventName(sessionEventName: string): string | number;

Parse the project from SessionEvent resource.

**Parameter**  
---  
**Name** | **Description**  
`sessionEventName` |  `string`   
A fully-qualified path representing SessionEvent resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromSessionName(sessionName)
    
    
    matchProjectFromSessionName(sessionName: string): string | number;

Parse the project from Session resource.

**Parameter**  
---  
**Name** | **Description**  
`sessionName` |  `string`   
A fully-qualified path representing Session resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromSpecialistPoolName(specialistPoolName)
    
    
    matchProjectFromSpecialistPoolName(specialistPoolName: string): string | number;

Parse the project from SpecialistPool resource.

**Parameter**  
---  
**Name** | **Description**  
`specialistPoolName` |  `string`   
A fully-qualified path representing SpecialistPool resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromStudyName(studyName)
    
    
    matchProjectFromStudyName(studyName: string): string | number;

Parse the project from Study resource.

**Parameter**  
---  
**Name** | **Description**  
`studyName` |  `string`   
A fully-qualified path representing Study resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromTensorboardExperimentName(tensorboardExperimentName)
    
    
    matchProjectFromTensorboardExperimentName(tensorboardExperimentName: string): string | number;

Parse the project from TensorboardExperiment resource.

**Parameter**  
---  
**Name** | **Description**  
`tensorboardExperimentName` |  `string`   
A fully-qualified path representing TensorboardExperiment resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromTensorboardName(tensorboardName)
    
    
    matchProjectFromTensorboardName(tensorboardName: string): string | number;

Parse the project from Tensorboard resource.

**Parameter**  
---  
**Name** | **Description**  
`tensorboardName` |  `string`   
A fully-qualified path representing Tensorboard resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromTensorboardRunName(tensorboardRunName)
    
    
    matchProjectFromTensorboardRunName(tensorboardRunName: string): string | number;

Parse the project from TensorboardRun resource.

**Parameter**  
---  
**Name** | **Description**  
`tensorboardRunName` |  `string`   
A fully-qualified path representing TensorboardRun resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromTensorboardTimeSeriesName(tensorboardTimeSeriesName)
    
    
    matchProjectFromTensorboardTimeSeriesName(tensorboardTimeSeriesName: string): string | number;

Parse the project from TensorboardTimeSeries resource.

**Parameter**  
---  
**Name** | **Description**  
`tensorboardTimeSeriesName` |  `string`   
A fully-qualified path representing TensorboardTimeSeries resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromTrainingPipelineName(trainingPipelineName)
    
    
    matchProjectFromTrainingPipelineName(trainingPipelineName: string): string | number;

Parse the project from TrainingPipeline resource.

**Parameter**  
---  
**Name** | **Description**  
`trainingPipelineName` |  `string`   
A fully-qualified path representing TrainingPipeline resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromTrialName(trialName)
    
    
    matchProjectFromTrialName(trialName: string): string | number;

Parse the project from Trial resource.

**Parameter**  
---  
**Name** | **Description**  
`trialName` |  `string`   
A fully-qualified path representing Trial resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromTuningJobName(tuningJobName)
    
    
    matchProjectFromTuningJobName(tuningJobName: string): string | number;

Parse the project from TuningJob resource.

**Parameter**  
---  
**Name** | **Description**  
`tuningJobName` |  `string`   
A fully-qualified path representing TuningJob resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchPublisherFromProjectLocationPublisherModelName(projectLocationPublisherModelName)
    
    
    matchPublisherFromProjectLocationPublisherModelName(projectLocationPublisherModelName: string): string | number;

Parse the publisher from ProjectLocationPublisherModel resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationPublisherModelName` |  `string`   
A fully-qualified path representing project_location_publisher_model resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the publisher.  
  
### matchPublisherFromPublisherModelName(publisherModelName)
    
    
    matchPublisherFromPublisherModelName(publisherModelName: string): string | number;

Parse the publisher from PublisherModel resource.

**Parameter**  
---  
**Name** | **Description**  
`publisherModelName` |  `string`   
A fully-qualified path representing PublisherModel resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the publisher.  
  
### matchRagCorpusFromRagCorpusName(ragCorpusName)
    
    
    matchRagCorpusFromRagCorpusName(ragCorpusName: string): string | number;

Parse the rag_corpus from RagCorpus resource.

**Parameter**  
---  
**Name** | **Description**  
`ragCorpusName` |  `string`   
A fully-qualified path representing RagCorpus resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the rag_corpus.  
  
### matchRagCorpusFromRagDataSchemaName(ragDataSchemaName)
    
    
    matchRagCorpusFromRagDataSchemaName(ragDataSchemaName: string): string | number;

Parse the rag_corpus from RagDataSchema resource.

**Parameter**  
---  
**Name** | **Description**  
`ragDataSchemaName` |  `string`   
A fully-qualified path representing RagDataSchema resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the rag_corpus.  
  
### matchRagCorpusFromRagFileName(ragFileName)
    
    
    matchRagCorpusFromRagFileName(ragFileName: string): string | number;

Parse the rag_corpus from RagFile resource.

**Parameter**  
---  
**Name** | **Description**  
`ragFileName` |  `string`   
A fully-qualified path representing RagFile resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the rag_corpus.  
  
### matchRagCorpusFromRagMetadataName(ragMetadataName)
    
    
    matchRagCorpusFromRagMetadataName(ragMetadataName: string): string | number;

Parse the rag_corpus from RagMetadata resource.

**Parameter**  
---  
**Name** | **Description**  
`ragMetadataName` |  `string`   
A fully-qualified path representing RagMetadata resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the rag_corpus.  
  
### matchRagDataSchemaFromRagDataSchemaName(ragDataSchemaName)
    
    
    matchRagDataSchemaFromRagDataSchemaName(ragDataSchemaName: string): string | number;

Parse the rag_data_schema from RagDataSchema resource.

**Parameter**  
---  
**Name** | **Description**  
`ragDataSchemaName` |  `string`   
A fully-qualified path representing RagDataSchema resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the rag_data_schema.  
  
### matchRagFileFromRagFileName(ragFileName)
    
    
    matchRagFileFromRagFileName(ragFileName: string): string | number;

Parse the rag_file from RagFile resource.

**Parameter**  
---  
**Name** | **Description**  
`ragFileName` |  `string`   
A fully-qualified path representing RagFile resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the rag_file.  
  
### matchRagFileFromRagMetadataName(ragMetadataName)
    
    
    matchRagFileFromRagMetadataName(ragMetadataName: string): string | number;

Parse the rag_file from RagMetadata resource.

**Parameter**  
---  
**Name** | **Description**  
`ragMetadataName` |  `string`   
A fully-qualified path representing RagMetadata resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the rag_file.  
  
### matchRagMetadataFromRagMetadataName(ragMetadataName)
    
    
    matchRagMetadataFromRagMetadataName(ragMetadataName: string): string | number;

Parse the rag_metadata from RagMetadata resource.

**Parameter**  
---  
**Name** | **Description**  
`ragMetadataName` |  `string`   
A fully-qualified path representing RagMetadata resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the rag_metadata.  
  
### matchReasoningEngineFromMemoryName(memoryName)
    
    
    matchReasoningEngineFromMemoryName(memoryName: string): string | number;

Parse the reasoning_engine from Memory resource.

**Parameter**  
---  
**Name** | **Description**  
`memoryName` |  `string`   
A fully-qualified path representing Memory resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the reasoning_engine.  
  
### matchReasoningEngineFromReasoningEngineName(reasoningEngineName)
    
    
    matchReasoningEngineFromReasoningEngineName(reasoningEngineName: string): string | number;

Parse the reasoning_engine from ReasoningEngine resource.

**Parameter**  
---  
**Name** | **Description**  
`reasoningEngineName` |  `string`   
A fully-qualified path representing ReasoningEngine resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the reasoning_engine.  
  
### matchReasoningEngineFromReasoningEngineRuntimeRevisionName(reasoningEngineRuntimeRevisionName)
    
    
    matchReasoningEngineFromReasoningEngineRuntimeRevisionName(reasoningEngineRuntimeRevisionName: string): string | number;

Parse the reasoning_engine from ReasoningEngineRuntimeRevision resource.

**Parameter**  
---  
**Name** | **Description**  
`reasoningEngineRuntimeRevisionName` |  `string`   
A fully-qualified path representing ReasoningEngineRuntimeRevision resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the reasoning_engine.  
  
### matchReasoningEngineFromSessionEventName(sessionEventName)
    
    
    matchReasoningEngineFromSessionEventName(sessionEventName: string): string | number;

Parse the reasoning_engine from SessionEvent resource.

**Parameter**  
---  
**Name** | **Description**  
`sessionEventName` |  `string`   
A fully-qualified path representing SessionEvent resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the reasoning_engine.  
  
### matchReasoningEngineFromSessionName(sessionName)
    
    
    matchReasoningEngineFromSessionName(sessionName: string): string | number;

Parse the reasoning_engine from Session resource.

**Parameter**  
---  
**Name** | **Description**  
`sessionName` |  `string`   
A fully-qualified path representing Session resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the reasoning_engine.  
  
### matchRunFromTensorboardRunName(tensorboardRunName)
    
    
    matchRunFromTensorboardRunName(tensorboardRunName: string): string | number;

Parse the run from TensorboardRun resource.

**Parameter**  
---  
**Name** | **Description**  
`tensorboardRunName` |  `string`   
A fully-qualified path representing TensorboardRun resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the run.  
  
### matchRunFromTensorboardTimeSeriesName(tensorboardTimeSeriesName)
    
    
    matchRunFromTensorboardTimeSeriesName(tensorboardTimeSeriesName: string): string | number;

Parse the run from TensorboardTimeSeries resource.

**Parameter**  
---  
**Name** | **Description**  
`tensorboardTimeSeriesName` |  `string`   
A fully-qualified path representing TensorboardTimeSeries resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the run.  
  
### matchRuntimeRevisionFromReasoningEngineRuntimeRevisionName(reasoningEngineRuntimeRevisionName)
    
    
    matchRuntimeRevisionFromReasoningEngineRuntimeRevisionName(reasoningEngineRuntimeRevisionName: string): string | number;

Parse the runtime_revision from ReasoningEngineRuntimeRevision resource.

**Parameter**  
---  
**Name** | **Description**  
`reasoningEngineRuntimeRevisionName` |  `string`   
A fully-qualified path representing ReasoningEngineRuntimeRevision resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the runtime_revision.  
  
### matchSavedQueryFromSavedQueryName(savedQueryName)
    
    
    matchSavedQueryFromSavedQueryName(savedQueryName: string): string | number;

Parse the saved_query from SavedQuery resource.

**Parameter**  
---  
**Name** | **Description**  
`savedQueryName` |  `string`   
A fully-qualified path representing SavedQuery resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the saved_query.  
  
### matchScheduleFromScheduleName(scheduleName)
    
    
    matchScheduleFromScheduleName(scheduleName: string): string | number;

Parse the schedule from Schedule resource.

**Parameter**  
---  
**Name** | **Description**  
`scheduleName` |  `string`   
A fully-qualified path representing Schedule resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the schedule.  
  
### matchSessionFromSessionEventName(sessionEventName)
    
    
    matchSessionFromSessionEventName(sessionEventName: string): string | number;

Parse the session from SessionEvent resource.

**Parameter**  
---  
**Name** | **Description**  
`sessionEventName` |  `string`   
A fully-qualified path representing SessionEvent resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the session.  
  
### matchSessionFromSessionName(sessionName)
    
    
    matchSessionFromSessionName(sessionName: string): string | number;

Parse the session from Session resource.

**Parameter**  
---  
**Name** | **Description**  
`sessionName` |  `string`   
A fully-qualified path representing Session resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the session.  
  
### matchSliceFromModelEvaluationSliceName(modelEvaluationSliceName)
    
    
    matchSliceFromModelEvaluationSliceName(modelEvaluationSliceName: string): string | number;

Parse the slice from ModelEvaluationSlice resource.

**Parameter**  
---  
**Name** | **Description**  
`modelEvaluationSliceName` |  `string`   
A fully-qualified path representing ModelEvaluationSlice resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the slice.  
  
### matchSpecialistPoolFromSpecialistPoolName(specialistPoolName)
    
    
    matchSpecialistPoolFromSpecialistPoolName(specialistPoolName: string): string | number;

Parse the specialist_pool from SpecialistPool resource.

**Parameter**  
---  
**Name** | **Description**  
`specialistPoolName` |  `string`   
A fully-qualified path representing SpecialistPool resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the specialist_pool.  
  
### matchStudyFromStudyName(studyName)
    
    
    matchStudyFromStudyName(studyName: string): string | number;

Parse the study from Study resource.

**Parameter**  
---  
**Name** | **Description**  
`studyName` |  `string`   
A fully-qualified path representing Study resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the study.  
  
### matchStudyFromTrialName(trialName)
    
    
    matchStudyFromTrialName(trialName: string): string | number;

Parse the study from Trial resource.

**Parameter**  
---  
**Name** | **Description**  
`trialName` |  `string`   
A fully-qualified path representing Trial resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the study.  
  
### matchTensorboardFromTensorboardExperimentName(tensorboardExperimentName)
    
    
    matchTensorboardFromTensorboardExperimentName(tensorboardExperimentName: string): string | number;

Parse the tensorboard from TensorboardExperiment resource.

**Parameter**  
---  
**Name** | **Description**  
`tensorboardExperimentName` |  `string`   
A fully-qualified path representing TensorboardExperiment resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the tensorboard.  
  
### matchTensorboardFromTensorboardName(tensorboardName)
    
    
    matchTensorboardFromTensorboardName(tensorboardName: string): string | number;

Parse the tensorboard from Tensorboard resource.

**Parameter**  
---  
**Name** | **Description**  
`tensorboardName` |  `string`   
A fully-qualified path representing Tensorboard resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the tensorboard.  
  
### matchTensorboardFromTensorboardRunName(tensorboardRunName)
    
    
    matchTensorboardFromTensorboardRunName(tensorboardRunName: string): string | number;

Parse the tensorboard from TensorboardRun resource.

**Parameter**  
---  
**Name** | **Description**  
`tensorboardRunName` |  `string`   
A fully-qualified path representing TensorboardRun resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the tensorboard.  
  
### matchTensorboardFromTensorboardTimeSeriesName(tensorboardTimeSeriesName)
    
    
    matchTensorboardFromTensorboardTimeSeriesName(tensorboardTimeSeriesName: string): string | number;

Parse the tensorboard from TensorboardTimeSeries resource.

**Parameter**  
---  
**Name** | **Description**  
`tensorboardTimeSeriesName` |  `string`   
A fully-qualified path representing TensorboardTimeSeries resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the tensorboard.  
  
### matchTimeSeriesFromTensorboardTimeSeriesName(tensorboardTimeSeriesName)
    
    
    matchTimeSeriesFromTensorboardTimeSeriesName(tensorboardTimeSeriesName: string): string | number;

Parse the time_series from TensorboardTimeSeries resource.

**Parameter**  
---  
**Name** | **Description**  
`tensorboardTimeSeriesName` |  `string`   
A fully-qualified path representing TensorboardTimeSeries resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the time_series.  
  
### matchTrainingPipelineFromTrainingPipelineName(trainingPipelineName)
    
    
    matchTrainingPipelineFromTrainingPipelineName(trainingPipelineName: string): string | number;

Parse the training_pipeline from TrainingPipeline resource.

**Parameter**  
---  
**Name** | **Description**  
`trainingPipelineName` |  `string`   
A fully-qualified path representing TrainingPipeline resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the training_pipeline.  
  
### matchTrialFromTrialName(trialName)
    
    
    matchTrialFromTrialName(trialName: string): string | number;

Parse the trial from Trial resource.

**Parameter**  
---  
**Name** | **Description**  
`trialName` |  `string`   
A fully-qualified path representing Trial resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the trial.  
  
### matchTuningJobFromTuningJobName(tuningJobName)
    
    
    matchTuningJobFromTuningJobName(tuningJobName: string): string | number;

Parse the tuning_job from TuningJob resource.

**Parameter**  
---  
**Name** | **Description**  
`tuningJobName` |  `string`   
A fully-qualified path representing TuningJob resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the tuning_job.  
  
### memoryPath(project, location, reasoningEngine, memory)
    
    
    memoryPath(project: string, location: string, reasoningEngine: string, memory: string): string;

Return a fully-qualified memory resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`reasoningEngine` |  `string`   
  
`memory` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### metadataSchemaPath(project, location, metadataStore, metadataSchema)
    
    
    metadataSchemaPath(project: string, location: string, metadataStore: string, metadataSchema: string): string;

Return a fully-qualified metadataSchema resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`metadataStore` |  `string`   
  
`metadataSchema` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### metadataStorePath(project, location, metadataStore)
    
    
    metadataStorePath(project: string, location: string, metadataStore: string): string;

Return a fully-qualified metadataStore resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`metadataStore` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### modelDeploymentMonitoringJobPath(project, location, modelDeploymentMonitoringJob)
    
    
    modelDeploymentMonitoringJobPath(project: string, location: string, modelDeploymentMonitoringJob: string): string;

Return a fully-qualified modelDeploymentMonitoringJob resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`modelDeploymentMonitoringJob` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### modelEvaluationPath(project, location, model, evaluation)
    
    
    modelEvaluationPath(project: string, location: string, model: string, evaluation: string): string;

Return a fully-qualified modelEvaluation resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`model` |  `string`   
  
`evaluation` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### modelEvaluationSlicePath(project, location, model, evaluation, slice)
    
    
    modelEvaluationSlicePath(project: string, location: string, model: string, evaluation: string, slice: string): string;

Return a fully-qualified modelEvaluationSlice resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`model` |  `string`   
  
`evaluation` |  `string`   
  
`slice` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### modelMonitoringJobPath(project, location, modelMonitor, modelMonitoringJob)
    
    
    modelMonitoringJobPath(project: string, location: string, modelMonitor: string, modelMonitoringJob: string): string;

Return a fully-qualified modelMonitoringJob resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`modelMonitor` |  `string`   
  
`modelMonitoringJob` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### modelMonitorPath(project, location, modelMonitor)
    
    
    modelMonitorPath(project: string, location: string, modelMonitor: string): string;

Return a fully-qualified modelMonitor resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`modelMonitor` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### modelPath(project, location, model)
    
    
    modelPath(project: string, location: string, model: string): string;

Return a fully-qualified model resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`model` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### nasJobPath(project, location, nasJob)
    
    
    nasJobPath(project: string, location: string, nasJob: string): string;

Return a fully-qualified nasJob resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`nasJob` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### nasTrialDetailPath(project, location, nasJob, nasTrialDetail)
    
    
    nasTrialDetailPath(project: string, location: string, nasJob: string, nasTrialDetail: string): string;

Return a fully-qualified nasTrialDetail resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`nasJob` |  `string`   
  
`nasTrialDetail` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### notebookExecutionJobPath(project, location, notebookExecutionJob)
    
    
    notebookExecutionJobPath(project: string, location: string, notebookExecutionJob: string): string;

Return a fully-qualified notebookExecutionJob resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`notebookExecutionJob` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### notebookRuntimePath(project, location, notebookRuntime)
    
    
    notebookRuntimePath(project: string, location: string, notebookRuntime: string): string;

Return a fully-qualified notebookRuntime resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`notebookRuntime` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### notebookRuntimeTemplatePath(project, location, notebookRuntimeTemplate)
    
    
    notebookRuntimeTemplatePath(project: string, location: string, notebookRuntimeTemplate: string): string;

Return a fully-qualified notebookRuntimeTemplate resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`notebookRuntimeTemplate` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### onlineEvaluatorPath(project, location, onlineEvaluator)
    
    
    onlineEvaluatorPath(project: string, location: string, onlineEvaluator: string): string;

Return a fully-qualified onlineEvaluator resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`onlineEvaluator` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### persistentResourcePath(project, location, persistentResource)
    
    
    persistentResourcePath(project: string, location: string, persistentResource: string): string;

Return a fully-qualified persistentResource resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`persistentResource` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### pipelineJobPath(project, location, pipelineJob)
    
    
    pipelineJobPath(project: string, location: string, pipelineJob: string): string;

Return a fully-qualified pipelineJob resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`pipelineJob` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### projectLocationEndpointPath(project, location, endpoint)
    
    
    projectLocationEndpointPath(project: string, location: string, endpoint: string): string;

Return a fully-qualified projectLocationEndpoint resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`endpoint` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### projectLocationFeatureGroupFeaturesPath(project, location, featureGroup, feature)
    
    
    projectLocationFeatureGroupFeaturesPath(project: string, location: string, featureGroup: string, feature: string): string;

Return a fully-qualified projectLocationFeatureGroupFeatures resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`featureGroup` |  `string`   
  
`feature` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### projectLocationFeaturestoreEntityTypeFeaturesPath(project, location, featurestore, entityType, feature)
    
    
    projectLocationFeaturestoreEntityTypeFeaturesPath(project: string, location: string, featurestore: string, entityType: string, feature: string): string;

Return a fully-qualified projectLocationFeaturestoreEntityTypeFeatures resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`featurestore` |  `string`   
  
`entityType` |  `string`   
  
`feature` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### projectLocationPublisherModelPath(project, location, publisher, model)
    
    
    projectLocationPublisherModelPath(project: string, location: string, publisher: string, model: string): string;

Return a fully-qualified projectLocationPublisherModel resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`publisher` |  `string`   
  
`model` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### publisherModelPath(publisher, model)
    
    
    publisherModelPath(publisher: string, model: string): string;

Return a fully-qualified publisherModel resource name string.

**Parameters**  
---  
**Name** | **Description**  
`publisher` |  `string`   
  
`model` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### ragCorpusPath(project, location, ragCorpus)
    
    
    ragCorpusPath(project: string, location: string, ragCorpus: string): string;

Return a fully-qualified ragCorpus resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`ragCorpus` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### ragDataSchemaPath(project, location, ragCorpus, ragDataSchema)
    
    
    ragDataSchemaPath(project: string, location: string, ragCorpus: string, ragDataSchema: string): string;

Return a fully-qualified ragDataSchema resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`ragCorpus` |  `string`   
  
`ragDataSchema` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### ragEngineConfigPath(project, location)
    
    
    ragEngineConfigPath(project: string, location: string): string;

Return a fully-qualified ragEngineConfig resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### ragFilePath(project, location, ragCorpus, ragFile)
    
    
    ragFilePath(project: string, location: string, ragCorpus: string, ragFile: string): string;

Return a fully-qualified ragFile resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`ragCorpus` |  `string`   
  
`ragFile` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### ragMetadataPath(project, location, ragCorpus, ragFile, ragMetadata)
    
    
    ragMetadataPath(project: string, location: string, ragCorpus: string, ragFile: string, ragMetadata: string): string;

Return a fully-qualified ragMetadata resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`ragCorpus` |  `string`   
  
`ragFile` |  `string`   
  
`ragMetadata` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### reasoningEnginePath(project, location, reasoningEngine)
    
    
    reasoningEnginePath(project: string, location: string, reasoningEngine: string): string;

Return a fully-qualified reasoningEngine resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`reasoningEngine` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### reasoningEngineRuntimeRevisionPath(project, location, reasoningEngine, runtimeRevision)
    
    
    reasoningEngineRuntimeRevisionPath(project: string, location: string, reasoningEngine: string, runtimeRevision: string): string;

Return a fully-qualified reasoningEngineRuntimeRevision resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`reasoningEngine` |  `string`   
  
`runtimeRevision` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### savedQueryPath(project, location, dataset, savedQuery)
    
    
    savedQueryPath(project: string, location: string, dataset: string, savedQuery: string): string;

Return a fully-qualified savedQuery resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`dataset` |  `string`   
  
`savedQuery` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### schedulePath(project, location, schedule)
    
    
    schedulePath(project: string, location: string, schedule: string): string;

Return a fully-qualified schedule resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`schedule` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### sessionEventPath(project, location, reasoningEngine, session, event)
    
    
    sessionEventPath(project: string, location: string, reasoningEngine: string, session: string, event: string): string;

Return a fully-qualified sessionEvent resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`reasoningEngine` |  `string`   
  
`session` |  `string`   
  
`event` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### sessionPath(project, location, reasoningEngine, session)
    
    
    sessionPath(project: string, location: string, reasoningEngine: string, session: string): string;

Return a fully-qualified session resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`reasoningEngine` |  `string`   
  
`session` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### setIamPolicy(request, options, callback)
    
    
    setIamPolicy(request: IamProtos.google.iam.v1.SetIamPolicyRequest, options?: gax.CallOptions | Callback<IamProtos.google.iam.v1.Policy, IamProtos.google.iam.v1.SetIamPolicyRequest | null | undefined, {} | null | undefined>, callback?: Callback<IamProtos.google.iam.v1.Policy, IamProtos.google.iam.v1.SetIamPolicyRequest | null | undefined, {} | null | undefined>): Promise<[IamProtos.google.iam.v1.Policy]>;

Returns permissions that a caller has on the specified resource. If the resource does not exist, this will return an empty set of permissions, not a NOT_FOUND error.

Note: This operation is designed to be used for building permission-aware UIs and command-line tools, not for authorization checking. This operation may "fail open" without warning.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `IamProtos.google.iam.v1.SetIamPolicyRequest`   
The request object that will be sent.  
`options` |  `CallOptions | Callback<google.iam.v1.Policy, google.iam.v1.SetIamPolicyRequest | null | undefined, {} | null | undefined>`   
Optional parameters. You can override the default settings for this call, e.g, timeout, retries, paginations, etc. See [gax.CallOptions](https://googleapis.github.io/gax-nodejs/interfaces/CallOptions.html) for the details.  
`callback` |  `Callback<google.iam.v1.Policy, google.iam.v1.SetIamPolicyRequest | null | undefined, {} | null | undefined>`   
The function which will be called with the result of the API call. The second parameter to the callback is an object representing .  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.iam.v1.Policy]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . The promise has a method named "cancel" which cancels the ongoing API call.  
  
### specialistPoolPath(project, location, specialistPool)
    
    
    specialistPoolPath(project: string, location: string, specialistPool: string): string;

Return a fully-qualified specialistPool resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`specialistPool` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### stopTrial(request, options)
    
    
    stopTrial(request?: protos.google.cloud.aiplatform.v1beta1.IStopTrialRequest, options?: CallOptions): Promise<[
            protos.google.cloud.aiplatform.v1beta1.ITrial,
            protos.google.cloud.aiplatform.v1beta1.IStopTrialRequest | undefined,
            {} | undefined
        ]>;

Stops a Trial.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IStopTrialRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.istoptrialrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.aiplatform.v1beta1.ITrial](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.itrial), [protos.google.cloud.aiplatform.v1beta1.IStopTrialRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.istoptrialrequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The Trial's name.
       *  Format:
       *  `projects/{project}/locations/{location}/studies/{study}/trials/{trial}`
       */
      // const name = 'abc123'
    
      // Imports the Aiplatform library
      const {VizierServiceClient} = require('[@google-cloud/aiplatform](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const aiplatformClient = new [VizierServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)();
    
      async function callStopTrial() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await aiplatformClient.stopTrial(request);
        console.log(response);
      }
    
      callStopTrial();
    
    

### stopTrial(request, options, callback)
    
    
    stopTrial(request: protos.google.cloud.aiplatform.v1beta1.IStopTrialRequest, options: CallOptions, callback: Callback<protos.google.cloud.aiplatform.v1beta1.ITrial, protos.google.cloud.aiplatform.v1beta1.IStopTrialRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IStopTrialRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.istoptrialrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.aiplatform.v1beta1.ITrial](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.itrial), [protos.google.cloud.aiplatform.v1beta1.IStopTrialRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.istoptrialrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### stopTrial(request, callback)
    
    
    stopTrial(request: protos.google.cloud.aiplatform.v1beta1.IStopTrialRequest, callback: Callback<protos.google.cloud.aiplatform.v1beta1.ITrial, protos.google.cloud.aiplatform.v1beta1.IStopTrialRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IStopTrialRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.istoptrialrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.aiplatform.v1beta1.ITrial](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.itrial), [protos.google.cloud.aiplatform.v1beta1.IStopTrialRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.istoptrialrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### studyPath(project, location, study)
    
    
    studyPath(project: string, location: string, study: string): string;

Return a fully-qualified study resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`study` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### suggestTrials(request, options)
    
    
    suggestTrials(request?: protos.google.cloud.aiplatform.v1beta1.ISuggestTrialsRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.cloud.aiplatform.v1beta1.ISuggestTrialsResponse, protos.google.cloud.aiplatform.v1beta1.ISuggestTrialsMetadata>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Adds one or more Trials to a Study, with parameter values suggested by Vertex AI Vizier. Returns a long-running operation associated with the generation of Trial suggestions. When this long-running operation succeeds, it will contain a [SuggestTrialsResponse](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.suggesttrialsresponse).

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISuggestTrialsRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.isuggesttrialsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.cloud.aiplatform.v1beta1.ISuggestTrialsResponse](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.isuggesttrialsresponse), [protos.google.cloud.aiplatform.v1beta1.ISuggestTrialsMetadata](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.isuggesttrialsmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.longrunning.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Its `promise()` method returns a promise you can `await` for. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The project and location that the Study belongs to.
       *  Format: `projects/{project}/locations/{location}/studies/{study}`
       */
      // const parent = 'abc123'
      /**
       *  Required. The number of suggestions requested. It must be positive.
       */
      // const suggestionCount = 1234
      /**
       *  Required. The identifier of the client that is requesting the suggestion.
       *  If multiple SuggestTrialsRequests have the same `client_id`,
       *  the service will return the identical suggested Trial if the Trial is
       *  pending, and provide a new Trial if the last suggested Trial was completed.
       */
      // const clientId = 'abc123'
      /**
       *  Optional. This allows you to specify the "context" for a Trial; a context
       *  is a slice (a subspace) of the search space.
       *  Typical uses for contexts:
       *  1) You are using Vizier to tune a server for best performance, but there's
       *    a strong weekly cycle.  The context specifies the day-of-week.
       *    This allows Tuesday to generalize from Wednesday without assuming that
       *    everything is identical.
       *  2) Imagine you're optimizing some medical treatment for people.
       *    As they walk in the door, you know certain facts about them
       *    (e.g. sex, weight, height, blood-pressure).  Put that information in the
       *    context, and Vizier will adapt its suggestions to the patient.
       *  3) You want to do a fair A/B test efficiently.  Specify the "A" and "B"
       *    conditions as contexts, and Vizier will generalize between "A" and "B"
       *    conditions.  If they are similar, this will allow Vizier to converge
       *    to the optimum faster than if "A" and "B" were separate Studies.
       *    NOTE: You can also enter contexts as REQUESTED Trials, e.g. via the
       *    CreateTrial() RPC; that's the asynchronous option where you don't need a
       *    close association between contexts and suggestions.
       *  NOTE: All the Parameters you set in a context MUST be defined in the
       *    Study.
       *  NOTE: You must supply 0 or $suggestion_count contexts.
       *    If you don't supply any contexts, Vizier will make suggestions
       *    from the full search space specified in the StudySpec; if you supply
       *    a full set of context, each suggestion will match the corresponding
       *    context.
       *  NOTE: A Context with no features set matches anything, and allows
       *    suggestions from the full search space.
       *  NOTE: Contexts MUST lie within the search space specified in the
       *    StudySpec.  It's an error if they don't.
       *  NOTE: Contexts preferentially match ACTIVE then REQUESTED trials before
       *    new suggestions are generated.
       *  NOTE: Generation of suggestions involves a match between a Context and
       *    (optionally) a REQUESTED trial; if that match is not fully specified, a
       *    suggestion will be geneated in the merged subspace.
       */
      // const contexts = [1,2,3,4]
    
      // Imports the Aiplatform library
      const {VizierServiceClient} = require('[@google-cloud/aiplatform](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const aiplatformClient = new [VizierServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)();
    
      async function callSuggestTrials() {
        // Construct request
        const request = {
          parent,
          suggestionCount,
          clientId,
        };
    
        // Run request
        const [operation] = await aiplatformClient.suggestTrials(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callSuggestTrials();
    
    

### suggestTrials(request, options, callback)
    
    
    suggestTrials(request: protos.google.cloud.aiplatform.v1beta1.ISuggestTrialsRequest, options: CallOptions, callback: Callback<LROperation<protos.google.cloud.aiplatform.v1beta1.ISuggestTrialsResponse, protos.google.cloud.aiplatform.v1beta1.ISuggestTrialsMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISuggestTrialsRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.isuggesttrialsrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.aiplatform.v1beta1.ISuggestTrialsResponse](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.isuggesttrialsresponse), [protos.google.cloud.aiplatform.v1beta1.ISuggestTrialsMetadata](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.isuggesttrialsmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### suggestTrials(request, callback)
    
    
    suggestTrials(request: protos.google.cloud.aiplatform.v1beta1.ISuggestTrialsRequest, callback: Callback<LROperation<protos.google.cloud.aiplatform.v1beta1.ISuggestTrialsResponse, protos.google.cloud.aiplatform.v1beta1.ISuggestTrialsMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISuggestTrialsRequest](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.isuggesttrialsrequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.aiplatform.v1beta1.ISuggestTrialsResponse](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.isuggesttrialsresponse), [protos.google.cloud.aiplatform.v1beta1.ISuggestTrialsMetadata](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.isuggesttrialsmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### tensorboardExperimentPath(project, location, tensorboard, experiment)
    
    
    tensorboardExperimentPath(project: string, location: string, tensorboard: string, experiment: string): string;

Return a fully-qualified tensorboardExperiment resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`tensorboard` |  `string`   
  
`experiment` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### tensorboardPath(project, location, tensorboard)
    
    
    tensorboardPath(project: string, location: string, tensorboard: string): string;

Return a fully-qualified tensorboard resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`tensorboard` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### tensorboardRunPath(project, location, tensorboard, experiment, run)
    
    
    tensorboardRunPath(project: string, location: string, tensorboard: string, experiment: string, run: string): string;

Return a fully-qualified tensorboardRun resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`tensorboard` |  `string`   
  
`experiment` |  `string`   
  
`run` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### tensorboardTimeSeriesPath(project, location, tensorboard, experiment, run, timeSeries)
    
    
    tensorboardTimeSeriesPath(project: string, location: string, tensorboard: string, experiment: string, run: string, timeSeries: string): string;

Return a fully-qualified tensorboardTimeSeries resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`tensorboard` |  `string`   
  
`experiment` |  `string`   
  
`run` |  `string`   
  
`timeSeries` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### testIamPermissions(request, options, callback)
    
    
    testIamPermissions(request: IamProtos.google.iam.v1.TestIamPermissionsRequest, options?: gax.CallOptions | Callback<IamProtos.google.iam.v1.TestIamPermissionsResponse, IamProtos.google.iam.v1.TestIamPermissionsRequest | null | undefined, {} | null | undefined>, callback?: Callback<IamProtos.google.iam.v1.TestIamPermissionsResponse, IamProtos.google.iam.v1.TestIamPermissionsRequest | null | undefined, {} | null | undefined>): Promise<[IamProtos.google.iam.v1.TestIamPermissionsResponse]>;

Returns permissions that a caller has on the specified resource. If the resource does not exist, this will return an empty set of permissions, not a NOT_FOUND error.

Note: This operation is designed to be used for building permission-aware UIs and command-line tools, not for authorization checking. This operation may "fail open" without warning.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `IamProtos.google.iam.v1.TestIamPermissionsRequest`   
The request object that will be sent.  
`options` |  `CallOptions | Callback<google.iam.v1.TestIamPermissionsResponse, google.iam.v1.TestIamPermissionsRequest | null | undefined, {} | null | undefined>`   
Optional parameters. You can override the default settings for this call, e.g, timeout, retries, paginations, etc. See [gax.CallOptions](https://googleapis.github.io/gax-nodejs/interfaces/CallOptions.html) for the details.  
`callback` |  `Callback<google.iam.v1.TestIamPermissionsResponse, google.iam.v1.TestIamPermissionsRequest | null | undefined, {} | null | undefined>`   
The function which will be called with the result of the API call. The second parameter to the callback is an object representing .  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.iam.v1.TestIamPermissionsResponse]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . The promise has a method named "cancel" which cancels the ongoing API call.  
  
### trainingPipelinePath(project, location, trainingPipeline)
    
    
    trainingPipelinePath(project: string, location: string, trainingPipeline: string): string;

Return a fully-qualified trainingPipeline resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`trainingPipeline` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### trialPath(project, location, study, trial)
    
    
    trialPath(project: string, location: string, study: string, trial: string): string;

Return a fully-qualified trial resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`study` |  `string`   
  
`trial` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### tuningJobPath(project, location, tuningJob)
    
    
    tuningJobPath(project: string, location: string, tuningJob: string): string;

Return a fully-qualified tuningJob resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`tuningJob` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
