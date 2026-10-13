---
url: https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/v1beta1.clustermanagerclient
title: Class v1beta1.ClusterManagerClient (7.2.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:04:22.886279+00:00
---

# Class v1beta1.ClusterManagerClient (7.2.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/v1beta1.clustermanagerclient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class v1beta1.ClusterManagerClient (7.2.1) Stay organized with collections  Save and categorize content based on your preferences. 

7.2.1 (latest)  7.1.0  6.8.0  6.7.0  6.1.0  5.19.0  5.17.0  5.15.1  5.14.0  5.10.0  5.9.0  5.8.0  5.6.0  5.5.0  5.4.1  5.1.0  4.11.0  4.10.0  4.9.0  4.7.1  4.4.0  4.3.0  4.2.0  4.1.3  3.0.0  2.6.0  2.5.0  2.4.4  2.3.2 

Google Kubernetes Engine Cluster Manager v1beta1 v1beta1

## Package

[@google-cloud/container](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/overview.html)

## Constructors 

### (constructor)(opts, gaxInstance)
    
    
    constructor(opts?: ClientOptions, gaxInstance?: typeof gax | typeof gax.fallback);

Construct an instance of ClusterManagerClient.

**Parameters**  
---  
**Name** | **Description**  
`opts` |  `ClientOptions`   
  
`gaxInstance` |  `typeof gax | typeof fallback`   
: loaded instance of `google-gax`. Useful if you need to avoid loading the default gRPC version and want to use the fallback HTTP implementation. Load only fallback version and pass it to the constructor: ``` const gax = require('google-gax/build/src/fallback'); // avoids loading google-gax with gRPC const client = new ClusterManagerClient({fallback: true}, gax); ```  
  
## Properties 

### apiEndpoint
    
    
    get apiEndpoint(): string;

The DNS address for this API service.

### apiEndpoint
    
    
    static get apiEndpoint(): string;

The DNS address for this API service - same as servicePath.

### auth
    
    
    auth: gax.GoogleAuth;

### clusterManagerStub
    
    
    clusterManagerStub?: Promise<{
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

### cancelOperation(request, options)
    
    
    cancelOperation(request?: protos.google.container.v1beta1.ICancelOperationRequest, options?: CallOptions): Promise<[
            protos.google.protobuf.IEmpty,
            protos.google.container.v1beta1.ICancelOperationRequest | undefined,
            {} | undefined
        ]>;

Cancels the specified operation.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICancelOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.icanceloperationrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.protobuf.iempty), [protos.google.container.v1beta1.ICancelOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.icanceloperationrequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [Empty](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.protobuf.empty). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  The name (project, location, operation id) of the operation to cancel.
       *  Specified in the format `projects/* /locations/* /operations/*`.
       */
      // const name = 'abc123'
    
      // Imports the Container library
      const {ClusterManagerClient} = require('[@google-cloud/container](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const containerClient = new [ClusterManagerClient](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/overview.html)();
    
      async function callCancelOperation() {
        // Construct request
        const request = {
        };
    
        // Run request
        const response = await containerClient.cancelOperation(request);
        console.log(response);
      }
    
      callCancelOperation();
    
    

### cancelOperation(request, options, callback)
    
    
    cancelOperation(request: protos.google.container.v1beta1.ICancelOperationRequest, options: CallOptions, callback: Callback<protos.google.protobuf.IEmpty, protos.google.container.v1beta1.ICancelOperationRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICancelOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.icanceloperationrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.protobuf.iempty), [protos.google.container.v1beta1.ICancelOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.icanceloperationrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### cancelOperation(request, callback)
    
    
    cancelOperation(request: protos.google.container.v1beta1.ICancelOperationRequest, callback: Callback<protos.google.protobuf.IEmpty, protos.google.container.v1beta1.ICancelOperationRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICancelOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.icanceloperationrequest)`   
  
`callback` |  `Callback<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.protobuf.iempty), [protos.google.container.v1beta1.ICancelOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.icanceloperationrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### caPoolPath(project, location, caPool)
    
    
    caPoolPath(project: string, location: string, caPool: string): string;

Return a fully-qualified caPool resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`caPool` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### checkAutopilotCompatibility(request, options)
    
    
    checkAutopilotCompatibility(request?: protos.google.container.v1beta1.ICheckAutopilotCompatibilityRequest, options?: CallOptions): Promise<[
            protos.google.container.v1beta1.ICheckAutopilotCompatibilityResponse,
            (protos.google.container.v1beta1.ICheckAutopilotCompatibilityRequest | undefined),
            {} | undefined
        ]>;

Checks the cluster compatibility with Autopilot mode, and returns a list of compatibility issues.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICheckAutopilotCompatibilityRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.icheckautopilotcompatibilityrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.container.v1beta1.ICheckAutopilotCompatibilityResponse](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.icheckautopilotcompatibilityresponse), ([protos.google.container.v1beta1.ICheckAutopilotCompatibilityRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.icheckautopilotcompatibilityrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [CheckAutopilotCompatibilityResponse](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.checkautopilotcompatibilityresponse). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  The name (project, location, cluster) of the cluster to retrieve.
       *  Specified in the format `projects/* /locations/* /clusters/*`.
       */
      // const name = 'abc123'
    
      // Imports the Container library
      const {ClusterManagerClient} = require('[@google-cloud/container](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const containerClient = new [ClusterManagerClient](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/overview.html)();
    
      async function callCheckAutopilotCompatibility() {
        // Construct request
        const request = {
        };
    
        // Run request
        const response = await containerClient.checkAutopilotCompatibility(request);
        console.log(response);
      }
    
      callCheckAutopilotCompatibility();
    
    

### checkAutopilotCompatibility(request, options, callback)
    
    
    checkAutopilotCompatibility(request: protos.google.container.v1beta1.ICheckAutopilotCompatibilityRequest, options: CallOptions, callback: Callback<protos.google.container.v1beta1.ICheckAutopilotCompatibilityResponse, protos.google.container.v1beta1.ICheckAutopilotCompatibilityRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICheckAutopilotCompatibilityRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.icheckautopilotcompatibilityrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.container.v1beta1.ICheckAutopilotCompatibilityResponse](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.icheckautopilotcompatibilityresponse), [protos.google.container.v1beta1.ICheckAutopilotCompatibilityRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.icheckautopilotcompatibilityrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### checkAutopilotCompatibility(request, callback)
    
    
    checkAutopilotCompatibility(request: protos.google.container.v1beta1.ICheckAutopilotCompatibilityRequest, callback: Callback<protos.google.container.v1beta1.ICheckAutopilotCompatibilityResponse, protos.google.container.v1beta1.ICheckAutopilotCompatibilityRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICheckAutopilotCompatibilityRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.icheckautopilotcompatibilityrequest)`   
  
`callback` |  `Callback<[protos.google.container.v1beta1.ICheckAutopilotCompatibilityResponse](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.icheckautopilotcompatibilityresponse), [protos.google.container.v1beta1.ICheckAutopilotCompatibilityRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.icheckautopilotcompatibilityrequest) | null | undefined, {} | null | undefined>`   
  
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
  
### completeControlPlaneUpgrade(request, options)
    
    
    completeControlPlaneUpgrade(request?: protos.google.container.v1beta1.ICompleteControlPlaneUpgradeRequest, options?: CallOptions): Promise<[
            protos.google.container.v1beta1.IOperation,
            (protos.google.container.v1beta1.ICompleteControlPlaneUpgradeRequest | undefined),
            {} | undefined
        ]>;

CompleteControlPlaneUpgrade completes the rollback-safe upgrade by performing the step two upgrade for a specific cluster.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICompleteControlPlaneUpgradeRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.icompletecontrolplaneupgraderequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.container.v1beta1.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.ioperation), ([protos.google.container.v1beta1.ICompleteControlPlaneUpgradeRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.icompletecontrolplaneupgraderequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  The name (project, location, cluster) of the cluster to complete upgrade.
       *  Specified in the format `projects/* /locations/* /clusters/*`.
       */
      // const name = 'abc123'
      /**
       *  API request version that initiates this operation.
       */
      // const version = 'abc123'
    
      // Imports the Container library
      const {ClusterManagerClient} = require('[@google-cloud/container](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const containerClient = new [ClusterManagerClient](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/overview.html)();
    
      async function callCompleteControlPlaneUpgrade() {
        // Construct request
        const request = {
        };
    
        // Run request
        const response = await containerClient.completeControlPlaneUpgrade(request);
        console.log(response);
      }
    
      callCompleteControlPlaneUpgrade();
    
    

### completeControlPlaneUpgrade(request, options, callback)
    
    
    completeControlPlaneUpgrade(request: protos.google.container.v1beta1.ICompleteControlPlaneUpgradeRequest, options: CallOptions, callback: Callback<protos.google.container.v1beta1.IOperation, protos.google.container.v1beta1.ICompleteControlPlaneUpgradeRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICompleteControlPlaneUpgradeRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.icompletecontrolplaneupgraderequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.container.v1beta1.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.ioperation), [protos.google.container.v1beta1.ICompleteControlPlaneUpgradeRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.icompletecontrolplaneupgraderequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### completeControlPlaneUpgrade(request, callback)
    
    
    completeControlPlaneUpgrade(request: protos.google.container.v1beta1.ICompleteControlPlaneUpgradeRequest, callback: Callback<protos.google.container.v1beta1.IOperation, protos.google.container.v1beta1.ICompleteControlPlaneUpgradeRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICompleteControlPlaneUpgradeRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.icompletecontrolplaneupgraderequest)`   
  
`callback` |  `Callback<[protos.google.container.v1beta1.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.ioperation), [protos.google.container.v1beta1.ICompleteControlPlaneUpgradeRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.icompletecontrolplaneupgraderequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### completeIPRotation(request, options)
    
    
    completeIPRotation(request?: protos.google.container.v1beta1.ICompleteIPRotationRequest, options?: CallOptions): Promise<[
            protos.google.container.v1beta1.IOperation,
            protos.google.container.v1beta1.ICompleteIPRotationRequest | undefined,
            {} | undefined
        ]>;

Completes master IP rotation.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICompleteIPRotationRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.icompleteiprotationrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.container.v1beta1.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.ioperation), [protos.google.container.v1beta1.ICompleteIPRotationRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.icompleteiprotationrequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  The name (project, location, cluster name) of the cluster to complete IP
       *  rotation. Specified in the format `projects/* /locations/* /clusters/*`.
       */
      // const name = 'abc123'
    
      // Imports the Container library
      const {ClusterManagerClient} = require('[@google-cloud/container](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const containerClient = new [ClusterManagerClient](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/overview.html)();
    
      async function callCompleteIPRotation() {
        // Construct request
        const request = {
        };
    
        // Run request
        const response = await containerClient.completeIPRotation(request);
        console.log(response);
      }
    
      callCompleteIPRotation();
    
    

### completeIPRotation(request, options, callback)
    
    
    completeIPRotation(request: protos.google.container.v1beta1.ICompleteIPRotationRequest, options: CallOptions, callback: Callback<protos.google.container.v1beta1.IOperation, protos.google.container.v1beta1.ICompleteIPRotationRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICompleteIPRotationRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.icompleteiprotationrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.container.v1beta1.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.ioperation), [protos.google.container.v1beta1.ICompleteIPRotationRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.icompleteiprotationrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### completeIPRotation(request, callback)
    
    
    completeIPRotation(request: protos.google.container.v1beta1.ICompleteIPRotationRequest, callback: Callback<protos.google.container.v1beta1.IOperation, protos.google.container.v1beta1.ICompleteIPRotationRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICompleteIPRotationRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.icompleteiprotationrequest)`   
  
`callback` |  `Callback<[protos.google.container.v1beta1.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.ioperation), [protos.google.container.v1beta1.ICompleteIPRotationRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.icompleteiprotationrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### completeNodePoolUpgrade(request, options)
    
    
    completeNodePoolUpgrade(request?: protos.google.container.v1beta1.ICompleteNodePoolUpgradeRequest, options?: CallOptions): Promise<[
            protos.google.protobuf.IEmpty,
            (protos.google.container.v1beta1.ICompleteNodePoolUpgradeRequest | undefined),
            {} | undefined
        ]>;

CompleteNodePoolUpgrade will signal an on-going node pool upgrade to complete.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICompleteNodePoolUpgradeRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.icompletenodepoolupgraderequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.protobuf.iempty), ([protos.google.container.v1beta1.ICompleteNodePoolUpgradeRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.icompletenodepoolupgraderequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [Empty](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.protobuf.empty). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  The name (project, location, cluster, node pool id) of the node pool to
       *  complete upgrade.
       *  Specified in the format `projects/* /locations/* /clusters/* /nodePools/*`.
       */
      // const name = 'abc123'
    
      // Imports the Container library
      const {ClusterManagerClient} = require('[@google-cloud/container](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const containerClient = new [ClusterManagerClient](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/overview.html)();
    
      async function callCompleteNodePoolUpgrade() {
        // Construct request
        const request = {
        };
    
        // Run request
        const response = await containerClient.completeNodePoolUpgrade(request);
        console.log(response);
      }
    
      callCompleteNodePoolUpgrade();
    
    

### completeNodePoolUpgrade(request, options, callback)
    
    
    completeNodePoolUpgrade(request: protos.google.container.v1beta1.ICompleteNodePoolUpgradeRequest, options: CallOptions, callback: Callback<protos.google.protobuf.IEmpty, protos.google.container.v1beta1.ICompleteNodePoolUpgradeRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICompleteNodePoolUpgradeRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.icompletenodepoolupgraderequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.protobuf.iempty), [protos.google.container.v1beta1.ICompleteNodePoolUpgradeRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.icompletenodepoolupgraderequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### completeNodePoolUpgrade(request, callback)
    
    
    completeNodePoolUpgrade(request: protos.google.container.v1beta1.ICompleteNodePoolUpgradeRequest, callback: Callback<protos.google.protobuf.IEmpty, protos.google.container.v1beta1.ICompleteNodePoolUpgradeRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICompleteNodePoolUpgradeRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.icompletenodepoolupgraderequest)`   
  
`callback` |  `Callback<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.protobuf.iempty), [protos.google.container.v1beta1.ICompleteNodePoolUpgradeRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.icompletenodepoolupgraderequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createCluster(request, options)
    
    
    createCluster(request?: protos.google.container.v1beta1.ICreateClusterRequest, options?: CallOptions): Promise<[
            protos.google.container.v1beta1.IOperation,
            protos.google.container.v1beta1.ICreateClusterRequest | undefined,
            {} | undefined
        ]>;

Creates a cluster, consisting of the specified number and type of Google Compute Engine instances.

By default, the cluster is created in the project's [default network](https://cloud.google.com/compute/docs/networks-and-firewalls#networks).

One firewall is added for the cluster. After cluster creation, the kubelet creates routes for each node to allow the containers on that node to communicate with all other instances in the cluster.

Finally, an entry is added to the project's global metadata indicating which CIDR range the cluster is using.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateClusterRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.icreateclusterrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.container.v1beta1.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.ioperation), [protos.google.container.v1beta1.ICreateClusterRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.icreateclusterrequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. A cluster
       *  resource (https://cloud.google.com/container-engine/reference/rest/v1beta1/projects.locations.clusters)
       */
      // const cluster = {}
      /**
       *  The parent (project and location) where the cluster will be created.
       *  Specified in the format `projects/* /locations/*`.
       */
      // const parent = 'abc123'
    
      // Imports the Container library
      const {ClusterManagerClient} = require('[@google-cloud/container](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const containerClient = new [ClusterManagerClient](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/overview.html)();
    
      async function callCreateCluster() {
        // Construct request
        const request = {
          cluster,
        };
    
        // Run request
        const response = await containerClient.createCluster(request);
        console.log(response);
      }
    
      callCreateCluster();
    
    

### createCluster(request, options, callback)
    
    
    createCluster(request: protos.google.container.v1beta1.ICreateClusterRequest, options: CallOptions, callback: Callback<protos.google.container.v1beta1.IOperation, protos.google.container.v1beta1.ICreateClusterRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateClusterRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.icreateclusterrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.container.v1beta1.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.ioperation), [protos.google.container.v1beta1.ICreateClusterRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.icreateclusterrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createCluster(request, callback)
    
    
    createCluster(request: protos.google.container.v1beta1.ICreateClusterRequest, callback: Callback<protos.google.container.v1beta1.IOperation, protos.google.container.v1beta1.ICreateClusterRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateClusterRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.icreateclusterrequest)`   
  
`callback` |  `Callback<[protos.google.container.v1beta1.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.ioperation), [protos.google.container.v1beta1.ICreateClusterRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.icreateclusterrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createNodePool(request, options)
    
    
    createNodePool(request?: protos.google.container.v1beta1.ICreateNodePoolRequest, options?: CallOptions): Promise<[
            protos.google.container.v1beta1.IOperation,
            protos.google.container.v1beta1.ICreateNodePoolRequest | undefined,
            {} | undefined
        ]>;

Creates a node pool for a cluster.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateNodePoolRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.icreatenodepoolrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.container.v1beta1.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.ioperation), [protos.google.container.v1beta1.ICreateNodePoolRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.icreatenodepoolrequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The node pool to create.
       */
      // const nodePool = {}
      /**
       *  The parent (project, location, cluster name) where the node pool will be
       *  created. Specified in the format
       *  `projects/* /locations/* /clusters/*`.
       */
      // const parent = 'abc123'
    
      // Imports the Container library
      const {ClusterManagerClient} = require('[@google-cloud/container](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const containerClient = new [ClusterManagerClient](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/overview.html)();
    
      async function callCreateNodePool() {
        // Construct request
        const request = {
          nodePool,
        };
    
        // Run request
        const response = await containerClient.createNodePool(request);
        console.log(response);
      }
    
      callCreateNodePool();
    
    

### createNodePool(request, options, callback)
    
    
    createNodePool(request: protos.google.container.v1beta1.ICreateNodePoolRequest, options: CallOptions, callback: Callback<protos.google.container.v1beta1.IOperation, protos.google.container.v1beta1.ICreateNodePoolRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateNodePoolRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.icreatenodepoolrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.container.v1beta1.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.ioperation), [protos.google.container.v1beta1.ICreateNodePoolRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.icreatenodepoolrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createNodePool(request, callback)
    
    
    createNodePool(request: protos.google.container.v1beta1.ICreateNodePoolRequest, callback: Callback<protos.google.container.v1beta1.IOperation, protos.google.container.v1beta1.ICreateNodePoolRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateNodePoolRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.icreatenodepoolrequest)`   
  
`callback` |  `Callback<[protos.google.container.v1beta1.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.ioperation), [protos.google.container.v1beta1.ICreateNodePoolRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.icreatenodepoolrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### cryptoKeyVersionPath(project, location, keyRing, cryptoKey, cryptoKeyVersion)
    
    
    cryptoKeyVersionPath(project: string, location: string, keyRing: string, cryptoKey: string, cryptoKeyVersion: string): string;

Return a fully-qualified cryptoKeyVersion resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`keyRing` |  `string`   
  
`cryptoKey` |  `string`   
  
`cryptoKeyVersion` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### deleteCluster(request, options)
    
    
    deleteCluster(request?: protos.google.container.v1beta1.IDeleteClusterRequest, options?: CallOptions): Promise<[
            protos.google.container.v1beta1.IOperation,
            protos.google.container.v1beta1.IDeleteClusterRequest | undefined,
            {} | undefined
        ]>;

Deletes the cluster, including the Kubernetes endpoint and all worker nodes.

Firewalls and routes that were configured during cluster creation are also deleted.

Other Google Compute Engine resources that might be in use by the cluster, such as load balancer resources, are not deleted if they weren't present when the cluster was initially created.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteClusterRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.ideleteclusterrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.container.v1beta1.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.ioperation), [protos.google.container.v1beta1.IDeleteClusterRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.ideleteclusterrequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  The name (project, location, cluster) of the cluster to delete.
       *  Specified in the format `projects/* /locations/* /clusters/*`.
       */
      // const name = 'abc123'
    
      // Imports the Container library
      const {ClusterManagerClient} = require('[@google-cloud/container](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const containerClient = new [ClusterManagerClient](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/overview.html)();
    
      async function callDeleteCluster() {
        // Construct request
        const request = {
        };
    
        // Run request
        const response = await containerClient.deleteCluster(request);
        console.log(response);
      }
    
      callDeleteCluster();
    
    

### deleteCluster(request, options, callback)
    
    
    deleteCluster(request: protos.google.container.v1beta1.IDeleteClusterRequest, options: CallOptions, callback: Callback<protos.google.container.v1beta1.IOperation, protos.google.container.v1beta1.IDeleteClusterRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteClusterRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.ideleteclusterrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.container.v1beta1.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.ioperation), [protos.google.container.v1beta1.IDeleteClusterRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.ideleteclusterrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteCluster(request, callback)
    
    
    deleteCluster(request: protos.google.container.v1beta1.IDeleteClusterRequest, callback: Callback<protos.google.container.v1beta1.IOperation, protos.google.container.v1beta1.IDeleteClusterRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteClusterRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.ideleteclusterrequest)`   
  
`callback` |  `Callback<[protos.google.container.v1beta1.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.ioperation), [protos.google.container.v1beta1.IDeleteClusterRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.ideleteclusterrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteNodePool(request, options)
    
    
    deleteNodePool(request?: protos.google.container.v1beta1.IDeleteNodePoolRequest, options?: CallOptions): Promise<[
            protos.google.container.v1beta1.IOperation,
            protos.google.container.v1beta1.IDeleteNodePoolRequest | undefined,
            {} | undefined
        ]>;

Deletes a node pool from a cluster.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteNodePoolRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.ideletenodepoolrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.container.v1beta1.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.ioperation), [protos.google.container.v1beta1.IDeleteNodePoolRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.ideletenodepoolrequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  The name (project, location, cluster, node pool id) of the node pool to
       *  delete. Specified in the format
       *  `projects/* /locations/* /clusters/* /nodePools/*`.
       */
      // const name = 'abc123'
    
      // Imports the Container library
      const {ClusterManagerClient} = require('[@google-cloud/container](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const containerClient = new [ClusterManagerClient](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/overview.html)();
    
      async function callDeleteNodePool() {
        // Construct request
        const request = {
        };
    
        // Run request
        const response = await containerClient.deleteNodePool(request);
        console.log(response);
      }
    
      callDeleteNodePool();
    
    

### deleteNodePool(request, options, callback)
    
    
    deleteNodePool(request: protos.google.container.v1beta1.IDeleteNodePoolRequest, options: CallOptions, callback: Callback<protos.google.container.v1beta1.IOperation, protos.google.container.v1beta1.IDeleteNodePoolRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteNodePoolRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.ideletenodepoolrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.container.v1beta1.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.ioperation), [protos.google.container.v1beta1.IDeleteNodePoolRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.ideletenodepoolrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteNodePool(request, callback)
    
    
    deleteNodePool(request: protos.google.container.v1beta1.IDeleteNodePoolRequest, callback: Callback<protos.google.container.v1beta1.IOperation, protos.google.container.v1beta1.IDeleteNodePoolRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteNodePoolRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.ideletenodepoolrequest)`   
  
`callback` |  `Callback<[protos.google.container.v1beta1.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.ioperation), [protos.google.container.v1beta1.IDeleteNodePoolRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.ideletenodepoolrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### fetchClusterUpgradeInfo(request, options)
    
    
    fetchClusterUpgradeInfo(request?: protos.google.container.v1beta1.IFetchClusterUpgradeInfoRequest, options?: CallOptions): Promise<[
            protos.google.container.v1beta1.IClusterUpgradeInfo,
            (protos.google.container.v1beta1.IFetchClusterUpgradeInfoRequest | undefined),
            {} | undefined
        ]>;

Fetch upgrade information of a specific cluster.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IFetchClusterUpgradeInfoRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.ifetchclusterupgradeinforequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.container.v1beta1.IClusterUpgradeInfo](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.iclusterupgradeinfo), ([protos.google.container.v1beta1.IFetchClusterUpgradeInfoRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.ifetchclusterupgradeinforequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The name (project, location, cluster) of the cluster to get.
       *  Specified in the format `projects/* /locations/* /clusters/*` or
       *  `projects/* /zones/* /clusters/*`.
       */
      // const name = 'abc123'
      /**
       *  API request version that initiates this operation.
       */
      // const version = 'abc123'
    
      // Imports the Container library
      const {ClusterManagerClient} = require('[@google-cloud/container](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const containerClient = new [ClusterManagerClient](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/overview.html)();
    
      async function callFetchClusterUpgradeInfo() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await containerClient.fetchClusterUpgradeInfo(request);
        console.log(response);
      }
    
      callFetchClusterUpgradeInfo();
    
    

### fetchClusterUpgradeInfo(request, options, callback)
    
    
    fetchClusterUpgradeInfo(request: protos.google.container.v1beta1.IFetchClusterUpgradeInfoRequest, options: CallOptions, callback: Callback<protos.google.container.v1beta1.IClusterUpgradeInfo, protos.google.container.v1beta1.IFetchClusterUpgradeInfoRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IFetchClusterUpgradeInfoRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.ifetchclusterupgradeinforequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.container.v1beta1.IClusterUpgradeInfo](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.iclusterupgradeinfo), [protos.google.container.v1beta1.IFetchClusterUpgradeInfoRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.ifetchclusterupgradeinforequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### fetchClusterUpgradeInfo(request, callback)
    
    
    fetchClusterUpgradeInfo(request: protos.google.container.v1beta1.IFetchClusterUpgradeInfoRequest, callback: Callback<protos.google.container.v1beta1.IClusterUpgradeInfo, protos.google.container.v1beta1.IFetchClusterUpgradeInfoRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IFetchClusterUpgradeInfoRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.ifetchclusterupgradeinforequest)`   
  
`callback` |  `Callback<[protos.google.container.v1beta1.IClusterUpgradeInfo](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.iclusterupgradeinfo), [protos.google.container.v1beta1.IFetchClusterUpgradeInfoRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.ifetchclusterupgradeinforequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### fetchNodePoolUpgradeInfo(request, options)
    
    
    fetchNodePoolUpgradeInfo(request?: protos.google.container.v1beta1.IFetchNodePoolUpgradeInfoRequest, options?: CallOptions): Promise<[
            protos.google.container.v1beta1.INodePoolUpgradeInfo,
            (protos.google.container.v1beta1.IFetchNodePoolUpgradeInfoRequest | undefined),
            {} | undefined
        ]>;

Fetch upgrade information of a specific node pool.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IFetchNodePoolUpgradeInfoRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.ifetchnodepoolupgradeinforequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.container.v1beta1.INodePoolUpgradeInfo](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.inodepoolupgradeinfo), ([protos.google.container.v1beta1.IFetchNodePoolUpgradeInfoRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.ifetchnodepoolupgradeinforequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The name (project, location, cluster, node pool) of the node pool
       *  to get. Specified in the format
       *  `projects/* /locations/* /clusters/* /nodePools/*` or
       *  `projects/* /zones/* /clusters/* /nodePools/*`.
       */
      // const name = 'abc123'
      /**
       *  API request version that initiates this operation.
       */
      // const version = 'abc123'
    
      // Imports the Container library
      const {ClusterManagerClient} = require('[@google-cloud/container](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const containerClient = new [ClusterManagerClient](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/overview.html)();
    
      async function callFetchNodePoolUpgradeInfo() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await containerClient.fetchNodePoolUpgradeInfo(request);
        console.log(response);
      }
    
      callFetchNodePoolUpgradeInfo();
    
    

### fetchNodePoolUpgradeInfo(request, options, callback)
    
    
    fetchNodePoolUpgradeInfo(request: protos.google.container.v1beta1.IFetchNodePoolUpgradeInfoRequest, options: CallOptions, callback: Callback<protos.google.container.v1beta1.INodePoolUpgradeInfo, protos.google.container.v1beta1.IFetchNodePoolUpgradeInfoRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IFetchNodePoolUpgradeInfoRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.ifetchnodepoolupgradeinforequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.container.v1beta1.INodePoolUpgradeInfo](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.inodepoolupgradeinfo), [protos.google.container.v1beta1.IFetchNodePoolUpgradeInfoRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.ifetchnodepoolupgradeinforequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### fetchNodePoolUpgradeInfo(request, callback)
    
    
    fetchNodePoolUpgradeInfo(request: protos.google.container.v1beta1.IFetchNodePoolUpgradeInfoRequest, callback: Callback<protos.google.container.v1beta1.INodePoolUpgradeInfo, protos.google.container.v1beta1.IFetchNodePoolUpgradeInfoRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IFetchNodePoolUpgradeInfoRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.ifetchnodepoolupgradeinforequest)`   
  
`callback` |  `Callback<[protos.google.container.v1beta1.INodePoolUpgradeInfo](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.inodepoolupgradeinfo), [protos.google.container.v1beta1.IFetchNodePoolUpgradeInfoRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.ifetchnodepoolupgradeinforequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getCluster(request, options)
    
    
    getCluster(request?: protos.google.container.v1beta1.IGetClusterRequest, options?: CallOptions): Promise<[
            protos.google.container.v1beta1.ICluster,
            protos.google.container.v1beta1.IGetClusterRequest | undefined,
            {} | undefined
        ]>;

Gets the details for a specific cluster.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetClusterRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.igetclusterrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.container.v1beta1.ICluster](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.icluster), [protos.google.container.v1beta1.IGetClusterRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.igetclusterrequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  The name (project, location, cluster) of the cluster to retrieve.
       *  Specified in the format `projects/* /locations/* /clusters/*`.
       */
      // const name = 'abc123'
    
      // Imports the Container library
      const {ClusterManagerClient} = require('[@google-cloud/container](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const containerClient = new [ClusterManagerClient](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/overview.html)();
    
      async function callGetCluster() {
        // Construct request
        const request = {
        };
    
        // Run request
        const response = await containerClient.getCluster(request);
        console.log(response);
      }
    
      callGetCluster();
    
    

### getCluster(request, options, callback)
    
    
    getCluster(request: protos.google.container.v1beta1.IGetClusterRequest, options: CallOptions, callback: Callback<protos.google.container.v1beta1.ICluster, protos.google.container.v1beta1.IGetClusterRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetClusterRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.igetclusterrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.container.v1beta1.ICluster](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.icluster), [protos.google.container.v1beta1.IGetClusterRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.igetclusterrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getCluster(request, callback)
    
    
    getCluster(request: protos.google.container.v1beta1.IGetClusterRequest, callback: Callback<protos.google.container.v1beta1.ICluster, protos.google.container.v1beta1.IGetClusterRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetClusterRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.igetclusterrequest)`   
  
`callback` |  `Callback<[protos.google.container.v1beta1.ICluster](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.icluster), [protos.google.container.v1beta1.IGetClusterRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.igetclusterrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getJSONWebKeys(request, options)
    
    
    getJSONWebKeys(request?: protos.google.container.v1beta1.IGetJSONWebKeysRequest, options?: CallOptions): Promise<[
            protos.google.container.v1beta1.IGetJSONWebKeysResponse,
            protos.google.container.v1beta1.IGetJSONWebKeysRequest | undefined,
            {} | undefined
        ]>;

Gets the public component of the cluster signing keys in JSON Web Key format.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetJSONWebKeysRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.igetjsonwebkeysrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.container.v1beta1.IGetJSONWebKeysResponse](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.igetjsonwebkeysresponse), [protos.google.container.v1beta1.IGetJSONWebKeysRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.igetjsonwebkeysrequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [GetJSONWebKeysResponse](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.getjsonwebkeysresponse). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  The cluster (project, location, cluster name) to get keys for. Specified in
       *  the format `projects/* /locations/* /clusters/*`.
       */
      // const parent = 'abc123'
    
      // Imports the Container library
      const {ClusterManagerClient} = require('[@google-cloud/container](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const containerClient = new [ClusterManagerClient](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/overview.html)();
    
      async function callGetJSONWebKeys() {
        // Construct request
        const request = {
        };
    
        // Run request
        const response = await containerClient.getJSONWebKeys(request);
        console.log(response);
      }
    
      callGetJSONWebKeys();
    
    

### getJSONWebKeys(request, options, callback)
    
    
    getJSONWebKeys(request: protos.google.container.v1beta1.IGetJSONWebKeysRequest, options: CallOptions, callback: Callback<protos.google.container.v1beta1.IGetJSONWebKeysResponse, protos.google.container.v1beta1.IGetJSONWebKeysRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetJSONWebKeysRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.igetjsonwebkeysrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.container.v1beta1.IGetJSONWebKeysResponse](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.igetjsonwebkeysresponse), [protos.google.container.v1beta1.IGetJSONWebKeysRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.igetjsonwebkeysrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getJSONWebKeys(request, callback)
    
    
    getJSONWebKeys(request: protos.google.container.v1beta1.IGetJSONWebKeysRequest, callback: Callback<protos.google.container.v1beta1.IGetJSONWebKeysResponse, protos.google.container.v1beta1.IGetJSONWebKeysRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetJSONWebKeysRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.igetjsonwebkeysrequest)`   
  
`callback` |  `Callback<[protos.google.container.v1beta1.IGetJSONWebKeysResponse](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.igetjsonwebkeysresponse), [protos.google.container.v1beta1.IGetJSONWebKeysRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.igetjsonwebkeysrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getNodePool(request, options)
    
    
    getNodePool(request?: protos.google.container.v1beta1.IGetNodePoolRequest, options?: CallOptions): Promise<[
            protos.google.container.v1beta1.INodePool,
            protos.google.container.v1beta1.IGetNodePoolRequest | undefined,
            {} | undefined
        ]>;

Retrieves the requested node pool.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetNodePoolRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.igetnodepoolrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.container.v1beta1.INodePool](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.inodepool), [protos.google.container.v1beta1.IGetNodePoolRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.igetnodepoolrequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  The name (project, location, cluster, node pool id) of the node pool to
       *  get. Specified in the format
       *  `projects/* /locations/* /clusters/* /nodePools/*`.
       */
      // const name = 'abc123'
    
      // Imports the Container library
      const {ClusterManagerClient} = require('[@google-cloud/container](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const containerClient = new [ClusterManagerClient](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/overview.html)();
    
      async function callGetNodePool() {
        // Construct request
        const request = {
        };
    
        // Run request
        const response = await containerClient.getNodePool(request);
        console.log(response);
      }
    
      callGetNodePool();
    
    

### getNodePool(request, options, callback)
    
    
    getNodePool(request: protos.google.container.v1beta1.IGetNodePoolRequest, options: CallOptions, callback: Callback<protos.google.container.v1beta1.INodePool, protos.google.container.v1beta1.IGetNodePoolRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetNodePoolRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.igetnodepoolrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.container.v1beta1.INodePool](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.inodepool), [protos.google.container.v1beta1.IGetNodePoolRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.igetnodepoolrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getNodePool(request, callback)
    
    
    getNodePool(request: protos.google.container.v1beta1.IGetNodePoolRequest, callback: Callback<protos.google.container.v1beta1.INodePool, protos.google.container.v1beta1.IGetNodePoolRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetNodePoolRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.igetnodepoolrequest)`   
  
`callback` |  `Callback<[protos.google.container.v1beta1.INodePool](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.inodepool), [protos.google.container.v1beta1.IGetNodePoolRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.igetnodepoolrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getOperation(request, options)
    
    
    getOperation(request?: protos.google.container.v1beta1.IGetOperationRequest, options?: CallOptions): Promise<[
            protos.google.container.v1beta1.IOperation,
            protos.google.container.v1beta1.IGetOperationRequest | undefined,
            {} | undefined
        ]>;

Gets the specified operation.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.igetoperationrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.container.v1beta1.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.ioperation), [protos.google.container.v1beta1.IGetOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.igetoperationrequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  The name (project, location, operation id) of the operation to get.
       *  Specified in the format `projects/* /locations/* /operations/*`.
       */
      // const name = 'abc123'
    
      // Imports the Container library
      const {ClusterManagerClient} = require('[@google-cloud/container](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const containerClient = new [ClusterManagerClient](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/overview.html)();
    
      async function callGetOperation() {
        // Construct request
        const request = {
        };
    
        // Run request
        const response = await containerClient.getOperation(request);
        console.log(response);
      }
    
      callGetOperation();
    
    

### getOperation(request, options, callback)
    
    
    getOperation(request: protos.google.container.v1beta1.IGetOperationRequest, options: CallOptions, callback: Callback<protos.google.container.v1beta1.IOperation, protos.google.container.v1beta1.IGetOperationRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.igetoperationrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.container.v1beta1.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.ioperation), [protos.google.container.v1beta1.IGetOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.igetoperationrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getOperation(request, callback)
    
    
    getOperation(request: protos.google.container.v1beta1.IGetOperationRequest, callback: Callback<protos.google.container.v1beta1.IOperation, protos.google.container.v1beta1.IGetOperationRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.igetoperationrequest)`   
  
`callback` |  `Callback<[protos.google.container.v1beta1.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.ioperation), [protos.google.container.v1beta1.IGetOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.igetoperationrequest) | null | undefined, {} | null | undefined>`   
  
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
  
### getServerConfig(request, options)
    
    
    getServerConfig(request?: protos.google.container.v1beta1.IGetServerConfigRequest, options?: CallOptions): Promise<[
            protos.google.container.v1beta1.IServerConfig,
            protos.google.container.v1beta1.IGetServerConfigRequest | undefined,
            {} | undefined
        ]>;

Returns configuration info about the Google Kubernetes Engine service.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetServerConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.igetserverconfigrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.container.v1beta1.IServerConfig](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.iserverconfig), [protos.google.container.v1beta1.IGetServerConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.igetserverconfigrequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  The name (project and location) of the server config to get,
       *  specified in the format `projects/* /locations/*`.
       */
      // const name = 'abc123'
    
      // Imports the Container library
      const {ClusterManagerClient} = require('[@google-cloud/container](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const containerClient = new [ClusterManagerClient](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/overview.html)();
    
      async function callGetServerConfig() {
        // Construct request
        const request = {
        };
    
        // Run request
        const response = await containerClient.getServerConfig(request);
        console.log(response);
      }
    
      callGetServerConfig();
    
    

### getServerConfig(request, options, callback)
    
    
    getServerConfig(request: protos.google.container.v1beta1.IGetServerConfigRequest, options: CallOptions, callback: Callback<protos.google.container.v1beta1.IServerConfig, protos.google.container.v1beta1.IGetServerConfigRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetServerConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.igetserverconfigrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.container.v1beta1.IServerConfig](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.iserverconfig), [protos.google.container.v1beta1.IGetServerConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.igetserverconfigrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getServerConfig(request, callback)
    
    
    getServerConfig(request: protos.google.container.v1beta1.IGetServerConfigRequest, callback: Callback<protos.google.container.v1beta1.IServerConfig, protos.google.container.v1beta1.IGetServerConfigRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetServerConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.igetserverconfigrequest)`   
  
`callback` |  `Callback<[protos.google.container.v1beta1.IServerConfig](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.iserverconfig), [protos.google.container.v1beta1.IGetServerConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.igetserverconfigrequest) | null | undefined, {} | null | undefined>`   
  
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
  
### listClusters(request, options)
    
    
    listClusters(request?: protos.google.container.v1beta1.IListClustersRequest, options?: CallOptions): Promise<[
            protos.google.container.v1beta1.IListClustersResponse,
            protos.google.container.v1beta1.IListClustersRequest | undefined,
            {} | undefined
        ]>;

Lists all clusters owned by a project in either the specified zone or all zones.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListClustersRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.ilistclustersrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.container.v1beta1.IListClustersResponse](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.ilistclustersresponse), [protos.google.container.v1beta1.IListClustersRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.ilistclustersrequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [ListClustersResponse](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.listclustersresponse). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  The parent (project and location) where the clusters will be listed.
       *  Specified in the format `projects/* /locations/*`.
       *  Location "-" matches all zones and all regions.
       */
      // const parent = 'abc123'
    
      // Imports the Container library
      const {ClusterManagerClient} = require('[@google-cloud/container](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const containerClient = new [ClusterManagerClient](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/overview.html)();
    
      async function callListClusters() {
        // Construct request
        const request = {
        };
    
        // Run request
        const response = await containerClient.listClusters(request);
        console.log(response);
      }
    
      callListClusters();
    
    

### listClusters(request, options, callback)
    
    
    listClusters(request: protos.google.container.v1beta1.IListClustersRequest, options: CallOptions, callback: Callback<protos.google.container.v1beta1.IListClustersResponse, protos.google.container.v1beta1.IListClustersRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListClustersRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.ilistclustersrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.container.v1beta1.IListClustersResponse](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.ilistclustersresponse), [protos.google.container.v1beta1.IListClustersRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.ilistclustersrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listClusters(request, callback)
    
    
    listClusters(request: protos.google.container.v1beta1.IListClustersRequest, callback: Callback<protos.google.container.v1beta1.IListClustersResponse, protos.google.container.v1beta1.IListClustersRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListClustersRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.ilistclustersrequest)`   
  
`callback` |  `Callback<[protos.google.container.v1beta1.IListClustersResponse](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.ilistclustersresponse), [protos.google.container.v1beta1.IListClustersRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.ilistclustersrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listLocations(request, options)
    
    
    listLocations(request?: protos.google.container.v1beta1.IListLocationsRequest, options?: CallOptions): Promise<[
            protos.google.container.v1beta1.IListLocationsResponse,
            protos.google.container.v1beta1.IListLocationsRequest | undefined,
            {} | undefined
        ]>;

Fetches locations that offer Google Kubernetes Engine.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListLocationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.ilistlocationsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.container.v1beta1.IListLocationsResponse](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.ilistlocationsresponse), [protos.google.container.v1beta1.IListLocationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.ilistlocationsrequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [ListLocationsResponse](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.listlocationsresponse). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Contains the name of the resource requested.
       *  Specified in the format `projects/*`.
       */
      // const parent = 'abc123'
    
      // Imports the Container library
      const {ClusterManagerClient} = require('[@google-cloud/container](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const containerClient = new [ClusterManagerClient](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/overview.html)();
    
      async function callListLocations() {
        // Construct request
        const request = {
          parent,
        };
    
        // Run request
        const response = await containerClient.listLocations(request);
        console.log(response);
      }
    
      callListLocations();
    
    

### listLocations(request, options, callback)
    
    
    listLocations(request: protos.google.container.v1beta1.IListLocationsRequest, options: CallOptions, callback: Callback<protos.google.container.v1beta1.IListLocationsResponse, protos.google.container.v1beta1.IListLocationsRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListLocationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.ilistlocationsrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.container.v1beta1.IListLocationsResponse](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.ilistlocationsresponse), [protos.google.container.v1beta1.IListLocationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.ilistlocationsrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listLocations(request, callback)
    
    
    listLocations(request: protos.google.container.v1beta1.IListLocationsRequest, callback: Callback<protos.google.container.v1beta1.IListLocationsResponse, protos.google.container.v1beta1.IListLocationsRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListLocationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.ilistlocationsrequest)`   
  
`callback` |  `Callback<[protos.google.container.v1beta1.IListLocationsResponse](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.ilistlocationsresponse), [protos.google.container.v1beta1.IListLocationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.ilistlocationsrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listNodePools(request, options)
    
    
    listNodePools(request?: protos.google.container.v1beta1.IListNodePoolsRequest, options?: CallOptions): Promise<[
            protos.google.container.v1beta1.IListNodePoolsResponse,
            protos.google.container.v1beta1.IListNodePoolsRequest | undefined,
            {} | undefined
        ]>;

Lists the node pools for a cluster.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListNodePoolsRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.ilistnodepoolsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.container.v1beta1.IListNodePoolsResponse](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.ilistnodepoolsresponse), [protos.google.container.v1beta1.IListNodePoolsRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.ilistnodepoolsrequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [ListNodePoolsResponse](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.listnodepoolsresponse). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  The parent (project, location, cluster name) where the node pools will be
       *  listed. Specified in the format `projects/* /locations/* /clusters/*`.
       */
      // const parent = 'abc123'
    
      // Imports the Container library
      const {ClusterManagerClient} = require('[@google-cloud/container](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const containerClient = new [ClusterManagerClient](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/overview.html)();
    
      async function callListNodePools() {
        // Construct request
        const request = {
        };
    
        // Run request
        const response = await containerClient.listNodePools(request);
        console.log(response);
      }
    
      callListNodePools();
    
    

### listNodePools(request, options, callback)
    
    
    listNodePools(request: protos.google.container.v1beta1.IListNodePoolsRequest, options: CallOptions, callback: Callback<protos.google.container.v1beta1.IListNodePoolsResponse, protos.google.container.v1beta1.IListNodePoolsRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListNodePoolsRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.ilistnodepoolsrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.container.v1beta1.IListNodePoolsResponse](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.ilistnodepoolsresponse), [protos.google.container.v1beta1.IListNodePoolsRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.ilistnodepoolsrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listNodePools(request, callback)
    
    
    listNodePools(request: protos.google.container.v1beta1.IListNodePoolsRequest, callback: Callback<protos.google.container.v1beta1.IListNodePoolsResponse, protos.google.container.v1beta1.IListNodePoolsRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListNodePoolsRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.ilistnodepoolsrequest)`   
  
`callback` |  `Callback<[protos.google.container.v1beta1.IListNodePoolsResponse](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.ilistnodepoolsresponse), [protos.google.container.v1beta1.IListNodePoolsRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.ilistnodepoolsrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listOperations(request, options)
    
    
    listOperations(request?: protos.google.container.v1beta1.IListOperationsRequest, options?: CallOptions): Promise<[
            protos.google.container.v1beta1.IListOperationsResponse,
            protos.google.container.v1beta1.IListOperationsRequest | undefined,
            {} | undefined
        ]>;

Lists all operations in a project in the specified zone or all zones.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListOperationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.ilistoperationsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.container.v1beta1.IListOperationsResponse](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.ilistoperationsresponse), [protos.google.container.v1beta1.IListOperationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.ilistoperationsrequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [ListOperationsResponse](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.listoperationsresponse). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  The parent (project and location) where the operations will be listed.
       *  Specified in the format `projects/* /locations/*`.
       *  Location "-" matches all zones and all regions.
       */
      // const parent = 'abc123'
    
      // Imports the Container library
      const {ClusterManagerClient} = require('[@google-cloud/container](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const containerClient = new [ClusterManagerClient](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/overview.html)();
    
      async function callListOperations() {
        // Construct request
        const request = {
        };
    
        // Run request
        const response = await containerClient.listOperations(request);
        console.log(response);
      }
    
      callListOperations();
    
    

### listOperations(request, options, callback)
    
    
    listOperations(request: protos.google.container.v1beta1.IListOperationsRequest, options: CallOptions, callback: Callback<protos.google.container.v1beta1.IListOperationsResponse, protos.google.container.v1beta1.IListOperationsRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListOperationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.ilistoperationsrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.container.v1beta1.IListOperationsResponse](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.ilistoperationsresponse), [protos.google.container.v1beta1.IListOperationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.ilistoperationsrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listOperations(request, callback)
    
    
    listOperations(request: protos.google.container.v1beta1.IListOperationsRequest, callback: Callback<protos.google.container.v1beta1.IListOperationsResponse, protos.google.container.v1beta1.IListOperationsRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListOperationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.ilistoperationsrequest)`   
  
`callback` |  `Callback<[protos.google.container.v1beta1.IListOperationsResponse](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.ilistoperationsresponse), [protos.google.container.v1beta1.IListOperationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.ilistoperationsrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listUsableSubnetworks(request, options)
    
    
    listUsableSubnetworks(request?: protos.google.container.v1beta1.IListUsableSubnetworksRequest, options?: CallOptions): Promise<[
            protos.google.container.v1beta1.IUsableSubnetwork[],
            protos.google.container.v1beta1.IListUsableSubnetworksRequest | null,
            protos.google.container.v1beta1.IListUsableSubnetworksResponse
        ]>;

Lists subnetworks that can be used for creating clusters in a project.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListUsableSubnetworksRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.ilistusablesubnetworksrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.container.v1beta1.IUsableSubnetwork](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.iusablesubnetwork)[], [protos.google.container.v1beta1.IListUsableSubnetworksRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.ilistusablesubnetworksrequest) | null, [protos.google.container.v1beta1.IListUsableSubnetworksResponse](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.ilistusablesubnetworksresponse) ]>` | {Promise} - The promise which resolves to an array. The first element of the array is Array of [UsableSubnetwork](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.usablesubnetwork). The client library will perform auto-pagination by default: it will call the API as many times as needed and will merge results from all the pages into this array. Note that it can affect your quota. We recommend using `listUsableSubnetworksAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listUsableSubnetworks(request, options, callback)
    
    
    listUsableSubnetworks(request: protos.google.container.v1beta1.IListUsableSubnetworksRequest, options: CallOptions, callback: PaginationCallback<protos.google.container.v1beta1.IListUsableSubnetworksRequest, protos.google.container.v1beta1.IListUsableSubnetworksResponse | null | undefined, protos.google.container.v1beta1.IUsableSubnetwork>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListUsableSubnetworksRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.ilistusablesubnetworksrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `PaginationCallback<[protos.google.container.v1beta1.IListUsableSubnetworksRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.ilistusablesubnetworksrequest), [protos.google.container.v1beta1.IListUsableSubnetworksResponse](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.ilistusablesubnetworksresponse) | null | undefined, [protos.google.container.v1beta1.IUsableSubnetwork](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.iusablesubnetwork)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listUsableSubnetworks(request, callback)
    
    
    listUsableSubnetworks(request: protos.google.container.v1beta1.IListUsableSubnetworksRequest, callback: PaginationCallback<protos.google.container.v1beta1.IListUsableSubnetworksRequest, protos.google.container.v1beta1.IListUsableSubnetworksResponse | null | undefined, protos.google.container.v1beta1.IUsableSubnetwork>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListUsableSubnetworksRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.ilistusablesubnetworksrequest)`   
  
`callback` |  `PaginationCallback<[protos.google.container.v1beta1.IListUsableSubnetworksRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.ilistusablesubnetworksrequest), [protos.google.container.v1beta1.IListUsableSubnetworksResponse](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.ilistusablesubnetworksresponse) | null | undefined, [protos.google.container.v1beta1.IUsableSubnetwork](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.iusablesubnetwork)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listUsableSubnetworksAsync(request, options)
    
    
    listUsableSubnetworksAsync(request?: protos.google.container.v1beta1.IListUsableSubnetworksRequest, options?: CallOptions): AsyncIterable<protos.google.container.v1beta1.IUsableSubnetwork>;

Equivalent to `listUsableSubnetworks`, but returns an iterable object.

`for`-`await`-`of` syntax is used with the iterable to get response elements on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListUsableSubnetworksRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.ilistusablesubnetworksrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.container.v1beta1.IUsableSubnetwork](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.iusablesubnetwork)>` | {Object} An iterable Object that allows [async iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols). When you iterate the returned iterable, each element will be an object representing [UsableSubnetwork](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.usablesubnetwork). The API will be called under the hood as needed, once per the page, so you can stop the iteration when you don't need more results. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The parent project where subnetworks are usable.
       *  Specified in the format `projects/*`.
       */
      // const parent = 'abc123'
      /**
       *  Filtering currently only supports equality on the networkProjectId and must
       *  be in the form: "networkProjectId=[PROJECTID]", where `networkProjectId`
       *  is the project which owns the listed subnetworks. This defaults to the
       *  parent project ID.
       */
      // const filter = 'abc123'
      /**
       *  The max number of results per page that should be returned. If the number
       *  of available results is larger than `page_size`, a `next_page_token` is
       *  returned which can be used to get the next page of results in subsequent
       *  requests. Acceptable values are 0 to 500, inclusive. (Default: 500)
       */
      // const pageSize = 1234
      /**
       *  Specifies a page token to use. Set this to the nextPageToken returned by
       *  previous list requests to get the next page of results.
       */
      // const pageToken = 'abc123'
    
      // Imports the Container library
      const {ClusterManagerClient} = require('[@google-cloud/container](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const containerClient = new [ClusterManagerClient](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/overview.html)();
    
      async function callListUsableSubnetworks() {
        // Construct request
        const request = {
          parent,
        };
    
        // Run request
        const iterable = containerClient.listUsableSubnetworksAsync(request);
        for await (const response of iterable) {
            console.log(response);
        }
      }
    
      callListUsableSubnetworks();
    
    

### listUsableSubnetworksStream(request, options)
    
    
    listUsableSubnetworksStream(request?: protos.google.container.v1beta1.IListUsableSubnetworksRequest, options?: CallOptions): Transform;

Equivalent to `listUsableSubnetworks`, but returns a NodeJS Stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListUsableSubnetworksRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.ilistusablesubnetworksrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Transform` | {Stream} An object stream which emits an object representing [UsableSubnetwork](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.usablesubnetwork) on 'data' event. The client library will perform auto-pagination by default: it will call the API as many times as needed. Note that it can affect your quota. We recommend using `listUsableSubnetworksAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### matchCaPoolFromCaPoolName(caPoolName)
    
    
    matchCaPoolFromCaPoolName(caPoolName: string): string | number;

Parse the ca_pool from CaPool resource.

**Parameter**  
---  
**Name** | **Description**  
`caPoolName` |  `string`   
A fully-qualified path representing CaPool resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the ca_pool.  
  
### matchCryptoKeyFromCryptoKeyVersionName(cryptoKeyVersionName)
    
    
    matchCryptoKeyFromCryptoKeyVersionName(cryptoKeyVersionName: string): string | number;

Parse the crypto_key from CryptoKeyVersion resource.

**Parameter**  
---  
**Name** | **Description**  
`cryptoKeyVersionName` |  `string`   
A fully-qualified path representing CryptoKeyVersion resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the crypto_key.  
  
### matchCryptoKeyVersionFromCryptoKeyVersionName(cryptoKeyVersionName)
    
    
    matchCryptoKeyVersionFromCryptoKeyVersionName(cryptoKeyVersionName: string): string | number;

Parse the crypto_key_version from CryptoKeyVersion resource.

**Parameter**  
---  
**Name** | **Description**  
`cryptoKeyVersionName` |  `string`   
A fully-qualified path representing CryptoKeyVersion resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the crypto_key_version.  
  
### matchKeyRingFromCryptoKeyVersionName(cryptoKeyVersionName)
    
    
    matchKeyRingFromCryptoKeyVersionName(cryptoKeyVersionName: string): string | number;

Parse the key_ring from CryptoKeyVersion resource.

**Parameter**  
---  
**Name** | **Description**  
`cryptoKeyVersionName` |  `string`   
A fully-qualified path representing CryptoKeyVersion resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the key_ring.  
  
### matchLocationFromCaPoolName(caPoolName)
    
    
    matchLocationFromCaPoolName(caPoolName: string): string | number;

Parse the location from CaPool resource.

**Parameter**  
---  
**Name** | **Description**  
`caPoolName` |  `string`   
A fully-qualified path representing CaPool resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromCryptoKeyVersionName(cryptoKeyVersionName)
    
    
    matchLocationFromCryptoKeyVersionName(cryptoKeyVersionName: string): string | number;

Parse the location from CryptoKeyVersion resource.

**Parameter**  
---  
**Name** | **Description**  
`cryptoKeyVersionName` |  `string`   
A fully-qualified path representing CryptoKeyVersion resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchProjectFromCaPoolName(caPoolName)
    
    
    matchProjectFromCaPoolName(caPoolName: string): string | number;

Parse the project from CaPool resource.

**Parameter**  
---  
**Name** | **Description**  
`caPoolName` |  `string`   
A fully-qualified path representing CaPool resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromCryptoKeyVersionName(cryptoKeyVersionName)
    
    
    matchProjectFromCryptoKeyVersionName(cryptoKeyVersionName: string): string | number;

Parse the project from CryptoKeyVersion resource.

**Parameter**  
---  
**Name** | **Description**  
`cryptoKeyVersionName` |  `string`   
A fully-qualified path representing CryptoKeyVersion resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromSubnetworkName(subnetworkName)
    
    
    matchProjectFromSubnetworkName(subnetworkName: string): string | number;

Parse the project from Subnetwork resource.

**Parameter**  
---  
**Name** | **Description**  
`subnetworkName` |  `string`   
A fully-qualified path representing Subnetwork resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchRegionFromSubnetworkName(subnetworkName)
    
    
    matchRegionFromSubnetworkName(subnetworkName: string): string | number;

Parse the region from Subnetwork resource.

**Parameter**  
---  
**Name** | **Description**  
`subnetworkName` |  `string`   
A fully-qualified path representing Subnetwork resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the region.  
  
### matchSubnetworkFromSubnetworkName(subnetworkName)
    
    
    matchSubnetworkFromSubnetworkName(subnetworkName: string): string | number;

Parse the subnetwork from Subnetwork resource.

**Parameter**  
---  
**Name** | **Description**  
`subnetworkName` |  `string`   
A fully-qualified path representing Subnetwork resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the subnetwork.  
  
### rollbackNodePoolUpgrade(request, options)
    
    
    rollbackNodePoolUpgrade(request?: protos.google.container.v1beta1.IRollbackNodePoolUpgradeRequest, options?: CallOptions): Promise<[
            protos.google.container.v1beta1.IOperation,
            (protos.google.container.v1beta1.IRollbackNodePoolUpgradeRequest | undefined),
            {} | undefined
        ]>;

Rolls back a previously Aborted or Failed NodePool upgrade. This makes no changes if the last upgrade successfully completed.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IRollbackNodePoolUpgradeRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.irollbacknodepoolupgraderequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.container.v1beta1.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.ioperation), ([protos.google.container.v1beta1.IRollbackNodePoolUpgradeRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.irollbacknodepoolupgraderequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  The name (project, location, cluster, node pool id) of the node poll to
       *  rollback upgrade.
       *  Specified in the format `projects/* /locations/* /clusters/* /nodePools/*`.
       */
      // const name = 'abc123'
      /**
       *  Option for rollback to ignore the PodDisruptionBudget.
       *  Default value is false.
       */
      // const respectPdb = true
    
      // Imports the Container library
      const {ClusterManagerClient} = require('[@google-cloud/container](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const containerClient = new [ClusterManagerClient](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/overview.html)();
    
      async function callRollbackNodePoolUpgrade() {
        // Construct request
        const request = {
        };
    
        // Run request
        const response = await containerClient.rollbackNodePoolUpgrade(request);
        console.log(response);
      }
    
      callRollbackNodePoolUpgrade();
    
    

### rollbackNodePoolUpgrade(request, options, callback)
    
    
    rollbackNodePoolUpgrade(request: protos.google.container.v1beta1.IRollbackNodePoolUpgradeRequest, options: CallOptions, callback: Callback<protos.google.container.v1beta1.IOperation, protos.google.container.v1beta1.IRollbackNodePoolUpgradeRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IRollbackNodePoolUpgradeRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.irollbacknodepoolupgraderequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.container.v1beta1.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.ioperation), [protos.google.container.v1beta1.IRollbackNodePoolUpgradeRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.irollbacknodepoolupgraderequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### rollbackNodePoolUpgrade(request, callback)
    
    
    rollbackNodePoolUpgrade(request: protos.google.container.v1beta1.IRollbackNodePoolUpgradeRequest, callback: Callback<protos.google.container.v1beta1.IOperation, protos.google.container.v1beta1.IRollbackNodePoolUpgradeRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IRollbackNodePoolUpgradeRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.irollbacknodepoolupgraderequest)`   
  
`callback` |  `Callback<[protos.google.container.v1beta1.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.ioperation), [protos.google.container.v1beta1.IRollbackNodePoolUpgradeRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.irollbacknodepoolupgraderequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### setAddonsConfig(request, options)
    
    
    setAddonsConfig(request?: protos.google.container.v1beta1.ISetAddonsConfigRequest, options?: CallOptions): Promise<[
            protos.google.container.v1beta1.IOperation,
            protos.google.container.v1beta1.ISetAddonsConfigRequest | undefined,
            {} | undefined
        ]>;

Sets the addons for a specific cluster.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISetAddonsConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.isetaddonsconfigrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.container.v1beta1.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.ioperation), [protos.google.container.v1beta1.ISetAddonsConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.isetaddonsconfigrequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The desired configurations for the various addons available to
       *  run in the cluster.
       */
      // const addonsConfig = {}
      /**
       *  The name (project, location, cluster) of the cluster to set addons.
       *  Specified in the format `projects/* /locations/* /clusters/*`.
       */
      // const name = 'abc123'
    
      // Imports the Container library
      const {ClusterManagerClient} = require('[@google-cloud/container](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const containerClient = new [ClusterManagerClient](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/overview.html)();
    
      async function callSetAddonsConfig() {
        // Construct request
        const request = {
          addonsConfig,
        };
    
        // Run request
        const response = await containerClient.setAddonsConfig(request);
        console.log(response);
      }
    
      callSetAddonsConfig();
    
    

### setAddonsConfig(request, options, callback)
    
    
    setAddonsConfig(request: protos.google.container.v1beta1.ISetAddonsConfigRequest, options: CallOptions, callback: Callback<protos.google.container.v1beta1.IOperation, protos.google.container.v1beta1.ISetAddonsConfigRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISetAddonsConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.isetaddonsconfigrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.container.v1beta1.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.ioperation), [protos.google.container.v1beta1.ISetAddonsConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.isetaddonsconfigrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### setAddonsConfig(request, callback)
    
    
    setAddonsConfig(request: protos.google.container.v1beta1.ISetAddonsConfigRequest, callback: Callback<protos.google.container.v1beta1.IOperation, protos.google.container.v1beta1.ISetAddonsConfigRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISetAddonsConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.isetaddonsconfigrequest)`   
  
`callback` |  `Callback<[protos.google.container.v1beta1.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.ioperation), [protos.google.container.v1beta1.ISetAddonsConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.isetaddonsconfigrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### setLabels(request, options)
    
    
    setLabels(request?: protos.google.container.v1beta1.ISetLabelsRequest, options?: CallOptions): Promise<[
            protos.google.container.v1beta1.IOperation,
            protos.google.container.v1beta1.ISetLabelsRequest | undefined,
            {} | undefined
        ]>;

Sets labels on a cluster.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISetLabelsRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.isetlabelsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.container.v1beta1.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.ioperation), [protos.google.container.v1beta1.ISetLabelsRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.isetlabelsrequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The labels to set for that cluster.
       */
      // const resourceLabels = [1,2,3,4]
      /**
       *  Required. The fingerprint of the previous set of labels for this resource,
       *  used to detect conflicts. The fingerprint is initially generated by
       *  Kubernetes Engine and changes after every request to modify or update
       *  labels. You must always provide an up-to-date fingerprint hash when
       *  updating or changing labels. Make a `get()` request to the
       *  resource to get the latest fingerprint.
       */
      // const labelFingerprint = 'abc123'
      /**
       *  The name (project, location, cluster name) of the cluster to set labels.
       *  Specified in the format `projects/* /locations/* /clusters/*`.
       */
      // const name = 'abc123'
    
      // Imports the Container library
      const {ClusterManagerClient} = require('[@google-cloud/container](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const containerClient = new [ClusterManagerClient](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/overview.html)();
    
      async function callSetLabels() {
        // Construct request
        const request = {
          resourceLabels,
          labelFingerprint,
        };
    
        // Run request
        const response = await containerClient.setLabels(request);
        console.log(response);
      }
    
      callSetLabels();
    
    

### setLabels(request, options, callback)
    
    
    setLabels(request: protos.google.container.v1beta1.ISetLabelsRequest, options: CallOptions, callback: Callback<protos.google.container.v1beta1.IOperation, protos.google.container.v1beta1.ISetLabelsRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISetLabelsRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.isetlabelsrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.container.v1beta1.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.ioperation), [protos.google.container.v1beta1.ISetLabelsRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.isetlabelsrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### setLabels(request, callback)
    
    
    setLabels(request: protos.google.container.v1beta1.ISetLabelsRequest, callback: Callback<protos.google.container.v1beta1.IOperation, protos.google.container.v1beta1.ISetLabelsRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISetLabelsRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.isetlabelsrequest)`   
  
`callback` |  `Callback<[protos.google.container.v1beta1.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.ioperation), [protos.google.container.v1beta1.ISetLabelsRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.isetlabelsrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### setLegacyAbac(request, options)
    
    
    setLegacyAbac(request?: protos.google.container.v1beta1.ISetLegacyAbacRequest, options?: CallOptions): Promise<[
            protos.google.container.v1beta1.IOperation,
            protos.google.container.v1beta1.ISetLegacyAbacRequest | undefined,
            {} | undefined
        ]>;

Enables or disables the ABAC authorization mechanism on a cluster.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISetLegacyAbacRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.isetlegacyabacrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.container.v1beta1.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.ioperation), [protos.google.container.v1beta1.ISetLegacyAbacRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.isetlegacyabacrequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Whether ABAC authorization will be enabled in the cluster.
       */
      // const enabled = true
      /**
       *  The name (project, location, cluster name) of the cluster to set legacy
       *  abac. Specified in the format `projects/* /locations/* /clusters/*`.
       */
      // const name = 'abc123'
    
      // Imports the Container library
      const {ClusterManagerClient} = require('[@google-cloud/container](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const containerClient = new [ClusterManagerClient](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/overview.html)();
    
      async function callSetLegacyAbac() {
        // Construct request
        const request = {
          enabled,
        };
    
        // Run request
        const response = await containerClient.setLegacyAbac(request);
        console.log(response);
      }
    
      callSetLegacyAbac();
    
    

### setLegacyAbac(request, options, callback)
    
    
    setLegacyAbac(request: protos.google.container.v1beta1.ISetLegacyAbacRequest, options: CallOptions, callback: Callback<protos.google.container.v1beta1.IOperation, protos.google.container.v1beta1.ISetLegacyAbacRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISetLegacyAbacRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.isetlegacyabacrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.container.v1beta1.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.ioperation), [protos.google.container.v1beta1.ISetLegacyAbacRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.isetlegacyabacrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### setLegacyAbac(request, callback)
    
    
    setLegacyAbac(request: protos.google.container.v1beta1.ISetLegacyAbacRequest, callback: Callback<protos.google.container.v1beta1.IOperation, protos.google.container.v1beta1.ISetLegacyAbacRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISetLegacyAbacRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.isetlegacyabacrequest)`   
  
`callback` |  `Callback<[protos.google.container.v1beta1.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.ioperation), [protos.google.container.v1beta1.ISetLegacyAbacRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.isetlegacyabacrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### setLocations(request, options)
    
    
    setLocations(request?: protos.google.container.v1beta1.ISetLocationsRequest, options?: CallOptions): Promise<[
            protos.google.container.v1beta1.IOperation,
            protos.google.container.v1beta1.ISetLocationsRequest | undefined,
            {} | undefined
        ]>;

Sets the locations for a specific cluster. Deprecated. Use [projects.locations.clusters.update](<https://cloud.google.com/kubernetes-engine/docs/reference/rest/v1beta1/projects.locations.clusters/update>) instead.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISetLocationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.isetlocationsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.container.v1beta1.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.ioperation), [protos.google.container.v1beta1.ISetLocationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.isetlocationsrequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The desired list of Google Compute Engine
       *  zones (https://cloud.google.com/compute/docs/zones#available)
       *  in which the cluster's nodes should be located. Changing the locations a
       *  cluster is in will result in nodes being either created or removed from the
       *  cluster, depending on whether locations are being added or removed.
       *  This list must always include the cluster's primary zone.
       */
      // const locations = ['abc','def']
      /**
       *  The name (project, location, cluster) of the cluster to set locations.
       *  Specified in the format `projects/* /locations/* /clusters/*`.
       */
      // const name = 'abc123'
    
      // Imports the Container library
      const {ClusterManagerClient} = require('[@google-cloud/container](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const containerClient = new [ClusterManagerClient](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/overview.html)();
    
      async function callSetLocations() {
        // Construct request
        const request = {
          locations,
        };
    
        // Run request
        const response = await containerClient.setLocations(request);
        console.log(response);
      }
    
      callSetLocations();
    
    

### setLocations(request, options, callback)
    
    
    setLocations(request: protos.google.container.v1beta1.ISetLocationsRequest, options: CallOptions, callback: Callback<protos.google.container.v1beta1.IOperation, protos.google.container.v1beta1.ISetLocationsRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISetLocationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.isetlocationsrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.container.v1beta1.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.ioperation), [protos.google.container.v1beta1.ISetLocationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.isetlocationsrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### setLocations(request, callback)
    
    
    setLocations(request: protos.google.container.v1beta1.ISetLocationsRequest, callback: Callback<protos.google.container.v1beta1.IOperation, protos.google.container.v1beta1.ISetLocationsRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISetLocationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.isetlocationsrequest)`   
  
`callback` |  `Callback<[protos.google.container.v1beta1.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.ioperation), [protos.google.container.v1beta1.ISetLocationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.isetlocationsrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### setLoggingService(request, options)
    
    
    setLoggingService(request?: protos.google.container.v1beta1.ISetLoggingServiceRequest, options?: CallOptions): Promise<[
            protos.google.container.v1beta1.IOperation,
            protos.google.container.v1beta1.ISetLoggingServiceRequest | undefined,
            {} | undefined
        ]>;

Sets the logging service for a specific cluster.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISetLoggingServiceRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.isetloggingservicerequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.container.v1beta1.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.ioperation), [protos.google.container.v1beta1.ISetLoggingServiceRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.isetloggingservicerequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The logging service the cluster should use to write logs.
       *  Currently available options:
       *  * `logging.googleapis.com/kubernetes` - The Cloud Logging
       *  service with a Kubernetes-native resource model
       *  * `logging.googleapis.com` - The legacy Cloud Logging service (no longer
       *    available as of GKE 1.15).
       *  * `none` - no logs will be exported from the cluster.
       *  If left as an empty string,`logging.googleapis.com/kubernetes` will be
       *  used for GKE 1.14+ or `logging.googleapis.com` for earlier versions.
       */
      // const loggingService = 'abc123'
      /**
       *  The name (project, location, cluster) of the cluster to set logging.
       *  Specified in the format `projects/* /locations/* /clusters/*`.
       */
      // const name = 'abc123'
    
      // Imports the Container library
      const {ClusterManagerClient} = require('[@google-cloud/container](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const containerClient = new [ClusterManagerClient](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/overview.html)();
    
      async function callSetLoggingService() {
        // Construct request
        const request = {
          loggingService,
        };
    
        // Run request
        const response = await containerClient.setLoggingService(request);
        console.log(response);
      }
    
      callSetLoggingService();
    
    

### setLoggingService(request, options, callback)
    
    
    setLoggingService(request: protos.google.container.v1beta1.ISetLoggingServiceRequest, options: CallOptions, callback: Callback<protos.google.container.v1beta1.IOperation, protos.google.container.v1beta1.ISetLoggingServiceRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISetLoggingServiceRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.isetloggingservicerequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.container.v1beta1.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.ioperation), [protos.google.container.v1beta1.ISetLoggingServiceRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.isetloggingservicerequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### setLoggingService(request, callback)
    
    
    setLoggingService(request: protos.google.container.v1beta1.ISetLoggingServiceRequest, callback: Callback<protos.google.container.v1beta1.IOperation, protos.google.container.v1beta1.ISetLoggingServiceRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISetLoggingServiceRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.isetloggingservicerequest)`   
  
`callback` |  `Callback<[protos.google.container.v1beta1.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.ioperation), [protos.google.container.v1beta1.ISetLoggingServiceRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.isetloggingservicerequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### setMaintenancePolicy(request, options)
    
    
    setMaintenancePolicy(request?: protos.google.container.v1beta1.ISetMaintenancePolicyRequest, options?: CallOptions): Promise<[
            protos.google.container.v1beta1.IOperation,
            protos.google.container.v1beta1.ISetMaintenancePolicyRequest | undefined,
            {} | undefined
        ]>;

Sets the maintenance policy for a cluster.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISetMaintenancePolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.isetmaintenancepolicyrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.container.v1beta1.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.ioperation), [protos.google.container.v1beta1.ISetMaintenancePolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.isetmaintenancepolicyrequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The Google Developers Console project ID or project
       *  number (https://cloud.google.com/resource-manager/docs/creating-managing-projects).
       */
      // const projectId = 'abc123'
      /**
       *  Required. The name of the Google Compute Engine
       *  zone (https://cloud.google.com/compute/docs/zones#available)
       *  in which the cluster resides.
       */
      // const zone = 'abc123'
      /**
       *  Required. The name of the cluster to update.
       */
      // const clusterId = 'abc123'
      /**
       *  Required. The maintenance policy to be set for the cluster. An empty field
       *  clears the existing maintenance policy.
       */
      // const maintenancePolicy = {}
      /**
       *  The name (project, location, cluster name) of the cluster to set
       *  maintenance policy.
       *  Specified in the format `projects/* /locations/* /clusters/*`.
       */
      // const name = 'abc123'
    
      // Imports the Container library
      const {ClusterManagerClient} = require('[@google-cloud/container](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const containerClient = new [ClusterManagerClient](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/overview.html)();
    
      async function callSetMaintenancePolicy() {
        // Construct request
        const request = {
          projectId,
          zone,
          clusterId,
          maintenancePolicy,
        };
    
        // Run request
        const response = await containerClient.setMaintenancePolicy(request);
        console.log(response);
      }
    
      callSetMaintenancePolicy();
    
    

### setMaintenancePolicy(request, options, callback)
    
    
    setMaintenancePolicy(request: protos.google.container.v1beta1.ISetMaintenancePolicyRequest, options: CallOptions, callback: Callback<protos.google.container.v1beta1.IOperation, protos.google.container.v1beta1.ISetMaintenancePolicyRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISetMaintenancePolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.isetmaintenancepolicyrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.container.v1beta1.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.ioperation), [protos.google.container.v1beta1.ISetMaintenancePolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.isetmaintenancepolicyrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### setMaintenancePolicy(request, callback)
    
    
    setMaintenancePolicy(request: protos.google.container.v1beta1.ISetMaintenancePolicyRequest, callback: Callback<protos.google.container.v1beta1.IOperation, protos.google.container.v1beta1.ISetMaintenancePolicyRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISetMaintenancePolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.isetmaintenancepolicyrequest)`   
  
`callback` |  `Callback<[protos.google.container.v1beta1.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.ioperation), [protos.google.container.v1beta1.ISetMaintenancePolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.isetmaintenancepolicyrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### setMasterAuth(request, options)
    
    
    setMasterAuth(request?: protos.google.container.v1beta1.ISetMasterAuthRequest, options?: CallOptions): Promise<[
            protos.google.container.v1beta1.IOperation,
            protos.google.container.v1beta1.ISetMasterAuthRequest | undefined,
            {} | undefined
        ]>;

Sets master auth materials. Currently supports changing the admin password or a specific cluster, either via password generation or explicitly setting the password.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISetMasterAuthRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.isetmasterauthrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.container.v1beta1.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.ioperation), [protos.google.container.v1beta1.ISetMasterAuthRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.isetmasterauthrequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The exact form of action to be taken on the master auth.
       */
      // const action = {}
      /**
       *  Required. A description of the update.
       */
      // const update = {}
      /**
       *  The name (project, location, cluster) of the cluster to set auth.
       *  Specified in the format `projects/* /locations/* /clusters/*`.
       */
      // const name = 'abc123'
    
      // Imports the Container library
      const {ClusterManagerClient} = require('[@google-cloud/container](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const containerClient = new [ClusterManagerClient](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/overview.html)();
    
      async function callSetMasterAuth() {
        // Construct request
        const request = {
          action,
          update,
        };
    
        // Run request
        const response = await containerClient.setMasterAuth(request);
        console.log(response);
      }
    
      callSetMasterAuth();
    
    

### setMasterAuth(request, options, callback)
    
    
    setMasterAuth(request: protos.google.container.v1beta1.ISetMasterAuthRequest, options: CallOptions, callback: Callback<protos.google.container.v1beta1.IOperation, protos.google.container.v1beta1.ISetMasterAuthRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISetMasterAuthRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.isetmasterauthrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.container.v1beta1.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.ioperation), [protos.google.container.v1beta1.ISetMasterAuthRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.isetmasterauthrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### setMasterAuth(request, callback)
    
    
    setMasterAuth(request: protos.google.container.v1beta1.ISetMasterAuthRequest, callback: Callback<protos.google.container.v1beta1.IOperation, protos.google.container.v1beta1.ISetMasterAuthRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISetMasterAuthRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.isetmasterauthrequest)`   
  
`callback` |  `Callback<[protos.google.container.v1beta1.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.ioperation), [protos.google.container.v1beta1.ISetMasterAuthRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.isetmasterauthrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### setMonitoringService(request, options)
    
    
    setMonitoringService(request?: protos.google.container.v1beta1.ISetMonitoringServiceRequest, options?: CallOptions): Promise<[
            protos.google.container.v1beta1.IOperation,
            protos.google.container.v1beta1.ISetMonitoringServiceRequest | undefined,
            {} | undefined
        ]>;

Sets the monitoring service for a specific cluster.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISetMonitoringServiceRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.isetmonitoringservicerequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.container.v1beta1.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.ioperation), [protos.google.container.v1beta1.ISetMonitoringServiceRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.isetmonitoringservicerequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The monitoring service the cluster should use to write metrics.
       *  Currently available options:
       *  * `monitoring.googleapis.com/kubernetes` - The Cloud Monitoring
       *  service with a Kubernetes-native resource model
       *  * `monitoring.googleapis.com` - The legacy Cloud Monitoring service (no
       *    longer available as of GKE 1.15).
       *  * `none` - No metrics will be exported from the cluster.
       *  If left as an empty string,`monitoring.googleapis.com/kubernetes` will be
       *  used for GKE 1.14+ or `monitoring.googleapis.com` for earlier versions.
       */
      // const monitoringService = 'abc123'
      /**
       *  The name (project, location, cluster) of the cluster to set monitoring.
       *  Specified in the format `projects/* /locations/* /clusters/*`.
       */
      // const name = 'abc123'
    
      // Imports the Container library
      const {ClusterManagerClient} = require('[@google-cloud/container](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const containerClient = new [ClusterManagerClient](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/overview.html)();
    
      async function callSetMonitoringService() {
        // Construct request
        const request = {
          monitoringService,
        };
    
        // Run request
        const response = await containerClient.setMonitoringService(request);
        console.log(response);
      }
    
      callSetMonitoringService();
    
    

### setMonitoringService(request, options, callback)
    
    
    setMonitoringService(request: protos.google.container.v1beta1.ISetMonitoringServiceRequest, options: CallOptions, callback: Callback<protos.google.container.v1beta1.IOperation, protos.google.container.v1beta1.ISetMonitoringServiceRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISetMonitoringServiceRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.isetmonitoringservicerequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.container.v1beta1.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.ioperation), [protos.google.container.v1beta1.ISetMonitoringServiceRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.isetmonitoringservicerequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### setMonitoringService(request, callback)
    
    
    setMonitoringService(request: protos.google.container.v1beta1.ISetMonitoringServiceRequest, callback: Callback<protos.google.container.v1beta1.IOperation, protos.google.container.v1beta1.ISetMonitoringServiceRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISetMonitoringServiceRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.isetmonitoringservicerequest)`   
  
`callback` |  `Callback<[protos.google.container.v1beta1.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.ioperation), [protos.google.container.v1beta1.ISetMonitoringServiceRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.isetmonitoringservicerequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### setNetworkPolicy(request, options)
    
    
    setNetworkPolicy(request?: protos.google.container.v1beta1.ISetNetworkPolicyRequest, options?: CallOptions): Promise<[
            protos.google.container.v1beta1.IOperation,
            protos.google.container.v1beta1.ISetNetworkPolicyRequest | undefined,
            {} | undefined
        ]>;

Enables or disables Network Policy for a cluster.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISetNetworkPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.isetnetworkpolicyrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.container.v1beta1.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.ioperation), [protos.google.container.v1beta1.ISetNetworkPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.isetnetworkpolicyrequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Configuration options for the NetworkPolicy feature.
       */
      // const networkPolicy = {}
      /**
       *  The name (project, location, cluster name) of the cluster to set networking
       *  policy. Specified in the format `projects/* /locations/* /clusters/*`.
       */
      // const name = 'abc123'
    
      // Imports the Container library
      const {ClusterManagerClient} = require('[@google-cloud/container](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const containerClient = new [ClusterManagerClient](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/overview.html)();
    
      async function callSetNetworkPolicy() {
        // Construct request
        const request = {
          networkPolicy,
        };
    
        // Run request
        const response = await containerClient.setNetworkPolicy(request);
        console.log(response);
      }
    
      callSetNetworkPolicy();
    
    

### setNetworkPolicy(request, options, callback)
    
    
    setNetworkPolicy(request: protos.google.container.v1beta1.ISetNetworkPolicyRequest, options: CallOptions, callback: Callback<protos.google.container.v1beta1.IOperation, protos.google.container.v1beta1.ISetNetworkPolicyRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISetNetworkPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.isetnetworkpolicyrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.container.v1beta1.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.ioperation), [protos.google.container.v1beta1.ISetNetworkPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.isetnetworkpolicyrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### setNetworkPolicy(request, callback)
    
    
    setNetworkPolicy(request: protos.google.container.v1beta1.ISetNetworkPolicyRequest, callback: Callback<protos.google.container.v1beta1.IOperation, protos.google.container.v1beta1.ISetNetworkPolicyRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISetNetworkPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.isetnetworkpolicyrequest)`   
  
`callback` |  `Callback<[protos.google.container.v1beta1.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.ioperation), [protos.google.container.v1beta1.ISetNetworkPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.isetnetworkpolicyrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### setNodePoolAutoscaling(request, options)
    
    
    setNodePoolAutoscaling(request?: protos.google.container.v1beta1.ISetNodePoolAutoscalingRequest, options?: CallOptions): Promise<[
            protos.google.container.v1beta1.IOperation,
            (protos.google.container.v1beta1.ISetNodePoolAutoscalingRequest | undefined),
            {} | undefined
        ]>;

Sets the autoscaling settings of a specific node pool.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISetNodePoolAutoscalingRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.isetnodepoolautoscalingrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.container.v1beta1.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.ioperation), ([protos.google.container.v1beta1.ISetNodePoolAutoscalingRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.isetnodepoolautoscalingrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Autoscaling configuration for the node pool.
       */
      // const autoscaling = {}
      /**
       *  The name (project, location, cluster, node pool) of the node pool to set
       *  autoscaler settings. Specified in the format
       *  `projects/* /locations/* /clusters/* /nodePools/*`.
       */
      // const name = 'abc123'
    
      // Imports the Container library
      const {ClusterManagerClient} = require('[@google-cloud/container](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const containerClient = new [ClusterManagerClient](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/overview.html)();
    
      async function callSetNodePoolAutoscaling() {
        // Construct request
        const request = {
          autoscaling,
        };
    
        // Run request
        const response = await containerClient.setNodePoolAutoscaling(request);
        console.log(response);
      }
    
      callSetNodePoolAutoscaling();
    
    

### setNodePoolAutoscaling(request, options, callback)
    
    
    setNodePoolAutoscaling(request: protos.google.container.v1beta1.ISetNodePoolAutoscalingRequest, options: CallOptions, callback: Callback<protos.google.container.v1beta1.IOperation, protos.google.container.v1beta1.ISetNodePoolAutoscalingRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISetNodePoolAutoscalingRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.isetnodepoolautoscalingrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.container.v1beta1.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.ioperation), [protos.google.container.v1beta1.ISetNodePoolAutoscalingRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.isetnodepoolautoscalingrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### setNodePoolAutoscaling(request, callback)
    
    
    setNodePoolAutoscaling(request: protos.google.container.v1beta1.ISetNodePoolAutoscalingRequest, callback: Callback<protos.google.container.v1beta1.IOperation, protos.google.container.v1beta1.ISetNodePoolAutoscalingRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISetNodePoolAutoscalingRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.isetnodepoolautoscalingrequest)`   
  
`callback` |  `Callback<[protos.google.container.v1beta1.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.ioperation), [protos.google.container.v1beta1.ISetNodePoolAutoscalingRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.isetnodepoolautoscalingrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### setNodePoolManagement(request, options)
    
    
    setNodePoolManagement(request?: protos.google.container.v1beta1.ISetNodePoolManagementRequest, options?: CallOptions): Promise<[
            protos.google.container.v1beta1.IOperation,
            protos.google.container.v1beta1.ISetNodePoolManagementRequest | undefined,
            {} | undefined
        ]>;

Sets the NodeManagement options for a node pool.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISetNodePoolManagementRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.isetnodepoolmanagementrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.container.v1beta1.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.ioperation), [protos.google.container.v1beta1.ISetNodePoolManagementRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.isetnodepoolmanagementrequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. NodeManagement configuration for the node pool.
       */
      // const management = {}
      /**
       *  The name (project, location, cluster, node pool id) of the node pool to set
       *  management properties. Specified in the format
       *  `projects/* /locations/* /clusters/* /nodePools/*`.
       */
      // const name = 'abc123'
    
      // Imports the Container library
      const {ClusterManagerClient} = require('[@google-cloud/container](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const containerClient = new [ClusterManagerClient](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/overview.html)();
    
      async function callSetNodePoolManagement() {
        // Construct request
        const request = {
          management,
        };
    
        // Run request
        const response = await containerClient.setNodePoolManagement(request);
        console.log(response);
      }
    
      callSetNodePoolManagement();
    
    

### setNodePoolManagement(request, options, callback)
    
    
    setNodePoolManagement(request: protos.google.container.v1beta1.ISetNodePoolManagementRequest, options: CallOptions, callback: Callback<protos.google.container.v1beta1.IOperation, protos.google.container.v1beta1.ISetNodePoolManagementRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISetNodePoolManagementRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.isetnodepoolmanagementrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.container.v1beta1.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.ioperation), [protos.google.container.v1beta1.ISetNodePoolManagementRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.isetnodepoolmanagementrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### setNodePoolManagement(request, callback)
    
    
    setNodePoolManagement(request: protos.google.container.v1beta1.ISetNodePoolManagementRequest, callback: Callback<protos.google.container.v1beta1.IOperation, protos.google.container.v1beta1.ISetNodePoolManagementRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISetNodePoolManagementRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.isetnodepoolmanagementrequest)`   
  
`callback` |  `Callback<[protos.google.container.v1beta1.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.ioperation), [protos.google.container.v1beta1.ISetNodePoolManagementRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.isetnodepoolmanagementrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### setNodePoolSize(request, options)
    
    
    setNodePoolSize(request?: protos.google.container.v1beta1.ISetNodePoolSizeRequest, options?: CallOptions): Promise<[
            protos.google.container.v1beta1.IOperation,
            protos.google.container.v1beta1.ISetNodePoolSizeRequest | undefined,
            {} | undefined
        ]>;

SetNodePoolSizeRequest sets the size of a node pool. The new size will be used for all replicas, including future replicas created by modifying .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISetNodePoolSizeRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.isetnodepoolsizerequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.container.v1beta1.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.ioperation), [protos.google.container.v1beta1.ISetNodePoolSizeRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.isetnodepoolsizerequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The desired node count for the pool.
       */
      // const nodeCount = 1234
      /**
       *  The name (project, location, cluster, node pool id) of the node pool to set
       *  size.
       *  Specified in the format `projects/* /locations/* /clusters/* /nodePools/*`.
       */
      // const name = 'abc123'
    
      // Imports the Container library
      const {ClusterManagerClient} = require('[@google-cloud/container](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const containerClient = new [ClusterManagerClient](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/overview.html)();
    
      async function callSetNodePoolSize() {
        // Construct request
        const request = {
          nodeCount,
        };
    
        // Run request
        const response = await containerClient.setNodePoolSize(request);
        console.log(response);
      }
    
      callSetNodePoolSize();
    
    

### setNodePoolSize(request, options, callback)
    
    
    setNodePoolSize(request: protos.google.container.v1beta1.ISetNodePoolSizeRequest, options: CallOptions, callback: Callback<protos.google.container.v1beta1.IOperation, protos.google.container.v1beta1.ISetNodePoolSizeRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISetNodePoolSizeRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.isetnodepoolsizerequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.container.v1beta1.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.ioperation), [protos.google.container.v1beta1.ISetNodePoolSizeRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.isetnodepoolsizerequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### setNodePoolSize(request, callback)
    
    
    setNodePoolSize(request: protos.google.container.v1beta1.ISetNodePoolSizeRequest, callback: Callback<protos.google.container.v1beta1.IOperation, protos.google.container.v1beta1.ISetNodePoolSizeRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISetNodePoolSizeRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.isetnodepoolsizerequest)`   
  
`callback` |  `Callback<[protos.google.container.v1beta1.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.ioperation), [protos.google.container.v1beta1.ISetNodePoolSizeRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.isetnodepoolsizerequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### startIPRotation(request, options)
    
    
    startIPRotation(request?: protos.google.container.v1beta1.IStartIPRotationRequest, options?: CallOptions): Promise<[
            protos.google.container.v1beta1.IOperation,
            protos.google.container.v1beta1.IStartIPRotationRequest | undefined,
            {} | undefined
        ]>;

Starts master IP rotation.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IStartIPRotationRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.istartiprotationrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.container.v1beta1.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.ioperation), [protos.google.container.v1beta1.IStartIPRotationRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.istartiprotationrequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  The name (project, location, cluster name) of the cluster to start IP
       *  rotation. Specified in the format `projects/* /locations/* /clusters/*`.
       */
      // const name = 'abc123'
      /**
       *  Whether to rotate credentials during IP rotation.
       */
      // const rotateCredentials = true
    
      // Imports the Container library
      const {ClusterManagerClient} = require('[@google-cloud/container](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const containerClient = new [ClusterManagerClient](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/overview.html)();
    
      async function callStartIPRotation() {
        // Construct request
        const request = {
        };
    
        // Run request
        const response = await containerClient.startIPRotation(request);
        console.log(response);
      }
    
      callStartIPRotation();
    
    

### startIPRotation(request, options, callback)
    
    
    startIPRotation(request: protos.google.container.v1beta1.IStartIPRotationRequest, options: CallOptions, callback: Callback<protos.google.container.v1beta1.IOperation, protos.google.container.v1beta1.IStartIPRotationRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IStartIPRotationRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.istartiprotationrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.container.v1beta1.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.ioperation), [protos.google.container.v1beta1.IStartIPRotationRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.istartiprotationrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### startIPRotation(request, callback)
    
    
    startIPRotation(request: protos.google.container.v1beta1.IStartIPRotationRequest, callback: Callback<protos.google.container.v1beta1.IOperation, protos.google.container.v1beta1.IStartIPRotationRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IStartIPRotationRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.istartiprotationrequest)`   
  
`callback` |  `Callback<[protos.google.container.v1beta1.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.ioperation), [protos.google.container.v1beta1.IStartIPRotationRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.istartiprotationrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### subnetworkPath(project, region, subnetwork)
    
    
    subnetworkPath(project: string, region: string, subnetwork: string): string;

Return a fully-qualified subnetwork resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`region` |  `string`   
  
`subnetwork` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### updateCluster(request, options)
    
    
    updateCluster(request?: protos.google.container.v1beta1.IUpdateClusterRequest, options?: CallOptions): Promise<[
            protos.google.container.v1beta1.IOperation,
            protos.google.container.v1beta1.IUpdateClusterRequest | undefined,
            {} | undefined
        ]>;

Updates the settings for a specific cluster.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateClusterRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.iupdateclusterrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.container.v1beta1.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.ioperation), [protos.google.container.v1beta1.IUpdateClusterRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.iupdateclusterrequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. A description of the update.
       */
      // const update = {}
      /**
       *  The name (project, location, cluster) of the cluster to update.
       *  Specified in the format `projects/* /locations/* /clusters/*`.
       */
      // const name = 'abc123'
    
      // Imports the Container library
      const {ClusterManagerClient} = require('[@google-cloud/container](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const containerClient = new [ClusterManagerClient](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/overview.html)();
    
      async function callUpdateCluster() {
        // Construct request
        const request = {
          update,
        };
    
        // Run request
        const response = await containerClient.updateCluster(request);
        console.log(response);
      }
    
      callUpdateCluster();
    
    

### updateCluster(request, options, callback)
    
    
    updateCluster(request: protos.google.container.v1beta1.IUpdateClusterRequest, options: CallOptions, callback: Callback<protos.google.container.v1beta1.IOperation, protos.google.container.v1beta1.IUpdateClusterRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateClusterRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.iupdateclusterrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.container.v1beta1.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.ioperation), [protos.google.container.v1beta1.IUpdateClusterRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.iupdateclusterrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateCluster(request, callback)
    
    
    updateCluster(request: protos.google.container.v1beta1.IUpdateClusterRequest, callback: Callback<protos.google.container.v1beta1.IOperation, protos.google.container.v1beta1.IUpdateClusterRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateClusterRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.iupdateclusterrequest)`   
  
`callback` |  `Callback<[protos.google.container.v1beta1.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.ioperation), [protos.google.container.v1beta1.IUpdateClusterRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.iupdateclusterrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateMaster(request, options)
    
    
    updateMaster(request?: protos.google.container.v1beta1.IUpdateMasterRequest, options?: CallOptions): Promise<[
            protos.google.container.v1beta1.IOperation,
            protos.google.container.v1beta1.IUpdateMasterRequest | undefined,
            {} | undefined
        ]>;

Updates the master for a specific cluster.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateMasterRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.iupdatemasterrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.container.v1beta1.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.ioperation), [protos.google.container.v1beta1.IUpdateMasterRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.iupdatemasterrequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The Kubernetes version to change the master to.
       *  Users may specify either explicit versions offered by
       *  Kubernetes Engine or version aliases, which have the following behavior:
       *  - "latest": picks the highest valid Kubernetes version
       *  - "1.X": picks the highest valid patch+gke.N patch in the 1.X version
       *  - "1.X.Y": picks the highest valid gke.N patch in the 1.X.Y version
       *  - "1.X.Y-gke.N": picks an explicit Kubernetes version
       *  - "-": picks the default Kubernetes version
       */
      // const masterVersion = 'abc123'
      /**
       *  The name (project, location, cluster) of the cluster to update.
       *  Specified in the format `projects/* /locations/* /clusters/*`.
       */
      // const name = 'abc123'
    
      // Imports the Container library
      const {ClusterManagerClient} = require('[@google-cloud/container](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const containerClient = new [ClusterManagerClient](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/overview.html)();
    
      async function callUpdateMaster() {
        // Construct request
        const request = {
          masterVersion,
        };
    
        // Run request
        const response = await containerClient.updateMaster(request);
        console.log(response);
      }
    
      callUpdateMaster();
    
    

### updateMaster(request, options, callback)
    
    
    updateMaster(request: protos.google.container.v1beta1.IUpdateMasterRequest, options: CallOptions, callback: Callback<protos.google.container.v1beta1.IOperation, protos.google.container.v1beta1.IUpdateMasterRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateMasterRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.iupdatemasterrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.container.v1beta1.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.ioperation), [protos.google.container.v1beta1.IUpdateMasterRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.iupdatemasterrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateMaster(request, callback)
    
    
    updateMaster(request: protos.google.container.v1beta1.IUpdateMasterRequest, callback: Callback<protos.google.container.v1beta1.IOperation, protos.google.container.v1beta1.IUpdateMasterRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateMasterRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.iupdatemasterrequest)`   
  
`callback` |  `Callback<[protos.google.container.v1beta1.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.ioperation), [protos.google.container.v1beta1.IUpdateMasterRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.iupdatemasterrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateNodePool(request, options)
    
    
    updateNodePool(request?: protos.google.container.v1beta1.IUpdateNodePoolRequest, options?: CallOptions): Promise<[
            protos.google.container.v1beta1.IOperation,
            protos.google.container.v1beta1.IUpdateNodePoolRequest | undefined,
            {} | undefined
        ]>;

Updates the version and/or image type of a specific node pool.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateNodePoolRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.iupdatenodepoolrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.container.v1beta1.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.ioperation), [protos.google.container.v1beta1.IUpdateNodePoolRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.iupdatenodepoolrequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The Kubernetes version to change the nodes to (typically an
       *  upgrade).
       *  Users may specify either explicit versions offered by Kubernetes Engine or
       *  version aliases, which have the following behavior:
       *  - "latest": picks the highest valid Kubernetes version
       *  - "1.X": picks the highest valid patch+gke.N patch in the 1.X version
       *  - "1.X.Y": picks the highest valid gke.N patch in the 1.X.Y version
       *  - "1.X.Y-gke.N": picks an explicit Kubernetes version
       *  - "-": picks the Kubernetes master version
       */
      // const nodeVersion = 'abc123'
      /**
       *  Required. The desired image type for the node pool. Please see
       *  https://cloud.google.com/kubernetes-engine/docs/concepts/node-images
       *  for available image types.
       */
      // const imageType = 'abc123'
      /**
       *  The desired name of the image name to use for this node.
       *  This is used to create clusters using a custom image.
       */
      // const image = 'abc123'
      /**
       *  The project containing the desired image to use for this node pool.
       *  This is used to create clusters using a custom image.
       */
      // const imageProject = 'abc123'
      /**
       *  The desired list of Google Compute Engine
       *  zones (https://cloud.google.com/compute/docs/zones#available)
       *  in which the node pool's nodes should be located. Changing the locations
       *  for a node pool will result in nodes being either created or removed from
       *  the node pool, depending on whether locations are being added or removed.
       *  Warning: It is recommended to update node pool locations in a standalone
       *  API call. Do not combine a location update with changes to other fields
       *  (such as `tags`, `labels`, `taints`, etc.) in the same request.
       *  Otherwise, the API performs a structural modification where changes to
       *  other fields will only apply to newly created nodes and will not be
       *  applied to existing nodes in the node pool. To ensure all nodes are updated
       *  consistently, use a separate API call for location changes.
       */
      // const locations = ['abc','def']
      /**
       *  The desired workload metadata config for the node pool.
       */
      // const workloadMetadataConfig = {}
      /**
       *  The name (project, location, cluster, node pool) of the node pool to
       *  update. Specified in the format
       *  `projects/* /locations/* /clusters/* /nodePools/*`.
       */
      // const name = 'abc123'
      /**
       *  Upgrade settings control disruption and speed of the upgrade.
       */
      // const upgradeSettings = {}
      /**
       *  The desired network tags to be applied to all nodes in the node pool.
       *  If this field is not present, the tags will not be changed. Otherwise,
       *  the existing network tags will be *replaced* with the provided tags.
       */
      // const tags = {}
      /**
       *  The desired node taints to be applied to all nodes in the node pool.
       *  If this field is not present, the taints will not be changed. Otherwise,
       *  the existing node taints will be *replaced* with the provided taints.
       */
      // const taints = {}
      /**
       *  The desired node labels to be applied to all nodes in the node pool.
       *  If this field is not present, the labels will not be changed. Otherwise,
       *  the existing node labels will be *replaced* with the provided labels.
       */
      // const labels = {}
      /**
       *  Parameters that can be configured on Linux nodes.
       */
      // const linuxNodeConfig = {}
      /**
       *  Node kubelet configs.
       */
      // const kubeletConfig = {}
      /**
       *  Node network config.
       */
      // const nodeNetworkConfig = {}
      /**
       *  GCFS config.
       */
      // const gcfsConfig = {}
      /**
       *  Confidential nodes config.
       *  All the nodes in the node pool will be Confidential VM once enabled.
       */
      // const confidentialNodes = {}
      /**
       *  Enable or disable gvnic on the node pool.
       */
      // const gvnic = {}
      /**
       *  The current etag of the node pool.
       *  If an etag is provided and does not match the current etag of the node
       *  pool, update will be blocked and an ABORTED error will be returned.
       */
      // const etag = 'abc123'
      /**
       *  Enable or disable NCCL fast socket for the node pool.
       */
      // const fastSocket = {}
      /**
       *  Logging configuration.
       */
      // const loggingConfig = {}
      /**
       *  The resource labels for the node pool to use to annotate any related
       *  Google Compute Engine resources.
       */
      // const resourceLabels = {}
      /**
       *  Parameters that can be configured on Windows nodes.
       */
      // const windowsNodeConfig = {}
      /**
       *  A list of hardware accelerators to be attached to each node.
       *  See
       *  https://cloud.google.com/compute/docs/gpus
       *  for more information about support for GPUs.
       */
      // const accelerators = [1,2,3,4]
      /**
       *  Optional. The desired machine type for nodes in the node pool.
       *  Initiates an upgrade operation that migrates the nodes in the
       *  node pool to the specified machine type.
       */
      // const machineType = 'abc123'
      /**
       *  Optional. The desired disk type for nodes in the node pool.
       *  Initiates an upgrade operation that migrates the nodes in the
       *  node pool to the specified disk type.
       */
      // const diskType = 'abc123'
      /**
       *  Optional. The desired disk size for nodes in the node pool.
       *  Initiates an upgrade operation that migrates the nodes in the
       *  node pool to the specified disk size.
       */
      // const diskSizeGb = 1234
      /**
       *  Desired resource manager tag keys and values to be attached to the nodes
       *  for managing Compute Engine firewalls using Network Firewall Policies.
       *  Existing tags will be replaced with new values.
       */
      // const resourceManagerTags = {}
      /**
       *  The desired containerd config for nodes in the node pool.
       *  Initiates an upgrade operation that recreates the nodes with the new
       *  config.
       */
      // const containerdConfig = {}
      /**
       *  Specifies the configuration of queued provisioning.
       */
      // const queuedProvisioning = {}
      /**
       *  List of Storage Pools where boot disks are provisioned.
       *  Existing Storage Pools will be replaced with storage-pools.
       */
      // const storagePools = ['abc','def']
      /**
       *  The maximum duration for the nodes to exist.
       *  If unspecified, the nodes can exist indefinitely.
       */
      // const maxRunDuration = {}
      /**
       *  Flex Start flag for enabling Flex Start VM.
       */
      // const flexStart = true
      /**
       *  The desired boot disk config for nodes in the node pool.
       *  Initiates an upgrade operation that migrates the nodes in the
       *  node pool to the specified boot disk config.
       */
      // const bootDisk = {}
      /**
       *  The desired node drain configuration for nodes in the node pool.
       */
      // const nodeDrainConfig = {}
      /**
       *  Consolidation delay defines duration after which the Cluster Autoscaler can
       *  scale down underutilized nodes. If not set, nodes are scaled down by
       *  default behavior, i.e. according to the chosen autoscaling profile.
       */
      // const consolidationDelay = {}
      /**
       *  The taint configuration for the node pool.
       */
      // const taintConfig = {}
    
      // Imports the Container library
      const {ClusterManagerClient} = require('[@google-cloud/container](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const containerClient = new [ClusterManagerClient](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/overview.html)();
    
      async function callUpdateNodePool() {
        // Construct request
        const request = {
          nodeVersion,
          imageType,
        };
    
        // Run request
        const response = await containerClient.updateNodePool(request);
        console.log(response);
      }
    
      callUpdateNodePool();
    
    

### updateNodePool(request, options, callback)
    
    
    updateNodePool(request: protos.google.container.v1beta1.IUpdateNodePoolRequest, options: CallOptions, callback: Callback<protos.google.container.v1beta1.IOperation, protos.google.container.v1beta1.IUpdateNodePoolRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateNodePoolRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.iupdatenodepoolrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.container.v1beta1.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.ioperation), [protos.google.container.v1beta1.IUpdateNodePoolRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.iupdatenodepoolrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateNodePool(request, callback)
    
    
    updateNodePool(request: protos.google.container.v1beta1.IUpdateNodePoolRequest, callback: Callback<protos.google.container.v1beta1.IOperation, protos.google.container.v1beta1.IUpdateNodePoolRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateNodePoolRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.iupdatenodepoolrequest)`   
  
`callback` |  `Callback<[protos.google.container.v1beta1.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.ioperation), [protos.google.container.v1beta1.IUpdateNodePoolRequest](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1beta1.iupdatenodepoolrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
