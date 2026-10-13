---
url: https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/v1beta.regionnetworkfirewallpoliciesclient
title: Class v1beta.RegionNetworkFirewallPoliciesClient (7.6.0) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:16:25.509961+00:00
---

# Class v1beta.RegionNetworkFirewallPoliciesClient (7.6.0)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/v1beta.regionnetworkfirewallpoliciesclient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class v1beta.RegionNetworkFirewallPoliciesClient (7.6.0) Stay organized with collections  Save and categorize content based on your preferences. 

7.6.0 (latest)  7.5.1  7.2.0  6.14.0  6.13.0  6.12.0  6.11.0  6.9.0  6.7.0  6.5.0  4.11.0  4.10.0  4.9.0  4.8.0  4.6.0  4.5.0  4.3.0  4.1.0  3.9.1  3.8.1  3.6.0  3.5.1  3.1.2  3.0.0 

The RegionNetworkFirewallPolicies API. v1beta

## Package

[@google-cloud/compute](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)

## Constructors 

### (constructor)(opts, gaxInstance)
    
    
    constructor(opts?: ClientOptions, gaxInstance?: typeof gax | typeof gax.fallback);

Construct an instance of RegionNetworkFirewallPoliciesClient.

**Parameters**  
---  
**Name** | **Description**  
`opts` |  `ClientOptions`   
  
`gaxInstance` |  `typeof gax | typeof fallback`   
: loaded instance of `google-gax`. Useful if you need to avoid loading the default gRPC version and want to use the fallback HTTP implementation. Load only fallback version and pass it to the constructor: ``` const gax = require('google-gax/build/src/fallback'); // avoids loading google-gax with gRPC const client = new RegionNetworkFirewallPoliciesClient({fallback: true}, gax); ```  
  
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

### port
    
    
    static get port(): number;

The port for this API service.

### regionNetworkFirewallPoliciesStub
    
    
    regionNetworkFirewallPoliciesStub?: Promise<{
            [name: string]: Function;
        }>;

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

### addAssociation(request, options)
    
    
    addAssociation(request?: protos.google.cloud.compute.v1beta.IAddAssociationRegionNetworkFirewallPolicyRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.cloud.compute.v1beta.IOperation, null>,
            protos.google.cloud.compute.v1beta.IOperation | undefined,
            {} | undefined
        ]>;

Inserts an association for the specified network firewall policy.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IAddAssociationRegionNetworkFirewallPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.iaddassociationregionnetworkfirewallpolicyrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.cloud.compute.v1beta.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ioperation), null>, [protos.google.cloud.compute.v1beta.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples. This method is considered to be in beta. This means while stable it is still a work-in-progress and under active development, and might get backwards-incompatible changes at any time. `.promise()` is not supported yet.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Name of the firewall policy associated with the target network to swap
       *  association with. This field is mutually exclusive with
       *  'replace_existing_association'.
       */
      // const associatedPolicyToBeReplaced = 'abc123'
      /**
       *  Name of the firewall policy to update.
       */
      // const firewallPolicy = 'abc123'
      /**
       *  The body resource for this request
       */
      // const firewallPolicyAssociationResource = {}
      /**
       *  Project ID for this request.
       */
      // const project = 'my-project'
      /**
       *  Name of the region scoping this request.
       */
      // const region = 'us-central1'
      /**
       *  Indicates whether or not to replace it if an association already exists.
       *  This is false by default, in which case an error will be returned if an
       *  association already exists.
       */
      // const replaceExistingAssociation = true
      /**
       *  An optional request ID to identify requests. Specify a unique request ID so
       *  that if you must retry your request, the server will know to ignore the
       *  request if it has already been completed.
       *  For example, consider a situation where you make an initial request and
       *  the request times out. If you make the request again with the same
       *  request ID, the server can check if original operation with the same
       *  request ID was received, and if so, will ignore the second request. This
       *  prevents clients from accidentally creating duplicate commitments.
       *  The request ID must be
       *  a valid UUID with the exception that zero UUID is not supported
       *  (00000000-0000-0000-0000-000000000000).
       */
      // const requestId = 'abc123'
    
      // Imports the Compute library
      const {RegionNetworkFirewallPoliciesClient} = require('[@google-cloud/compute](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const computeClient = new [RegionNetworkFirewallPoliciesClient](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)();
    
      async function callAddAssociation() {
        // Construct request
        const request = {
          firewallPolicy,
          firewallPolicyAssociationResource,
          project,
          region,
        };
    
        // Run request
        const response = await computeClient.addAssociation(request);
        console.log(response);
      }
    
      callAddAssociation();
    
    

### addAssociation(request, options, callback)
    
    
    addAssociation(request: protos.google.cloud.compute.v1beta.IAddAssociationRegionNetworkFirewallPolicyRequest, options: CallOptions, callback: Callback<protos.google.cloud.compute.v1beta.IOperation, protos.google.cloud.compute.v1beta.IAddAssociationRegionNetworkFirewallPolicyRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IAddAssociationRegionNetworkFirewallPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.iaddassociationregionnetworkfirewallpolicyrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.compute.v1beta.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ioperation), [protos.google.cloud.compute.v1beta.IAddAssociationRegionNetworkFirewallPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.iaddassociationregionnetworkfirewallpolicyrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### addAssociation(request, callback)
    
    
    addAssociation(request: protos.google.cloud.compute.v1beta.IAddAssociationRegionNetworkFirewallPolicyRequest, callback: Callback<protos.google.cloud.compute.v1beta.IOperation, protos.google.cloud.compute.v1beta.IAddAssociationRegionNetworkFirewallPolicyRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IAddAssociationRegionNetworkFirewallPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.iaddassociationregionnetworkfirewallpolicyrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.compute.v1beta.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ioperation), [protos.google.cloud.compute.v1beta.IAddAssociationRegionNetworkFirewallPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.iaddassociationregionnetworkfirewallpolicyrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### addRule(request, options)
    
    
    addRule(request?: protos.google.cloud.compute.v1beta.IAddRuleRegionNetworkFirewallPolicyRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.cloud.compute.v1beta.IOperation, null>,
            protos.google.cloud.compute.v1beta.IOperation | undefined,
            {} | undefined
        ]>;

Inserts a rule into a network firewall policy.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IAddRuleRegionNetworkFirewallPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.iaddruleregionnetworkfirewallpolicyrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.cloud.compute.v1beta.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ioperation), null>, [protos.google.cloud.compute.v1beta.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples. This method is considered to be in beta. This means while stable it is still a work-in-progress and under active development, and might get backwards-incompatible changes at any time. `.promise()` is not supported yet.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Name of the firewall policy to update.
       */
      // const firewallPolicy = 'abc123'
      /**
       *  The body resource for this request
       */
      // const firewallPolicyRuleResource = {}
      /**
       *  When rule.priority is not specified, auto choose a unused priority betweenminPriority and maxPriority>.
       *  This field is exclusive with rule.priority.
       */
      // const maxPriority = 1234
      /**
       *  When rule.priority is not specified, auto choose a unused priority betweenminPriority and maxPriority>.
       *  This field is exclusive with rule.priority.
       */
      // const minPriority = 1234
      /**
       *  Project ID for this request.
       */
      // const project = 'my-project'
      /**
       *  Name of the region scoping this request.
       */
      // const region = 'us-central1'
      /**
       *  An optional request ID to identify requests. Specify a unique request ID so
       *  that if you must retry your request, the server will know to ignore the
       *  request if it has already been completed.
       *  For example, consider a situation where you make an initial request and
       *  the request times out. If you make the request again with the same
       *  request ID, the server can check if original operation with the same
       *  request ID was received, and if so, will ignore the second request. This
       *  prevents clients from accidentally creating duplicate commitments.
       *  The request ID must be
       *  a valid UUID with the exception that zero UUID is not supported
       *  (00000000-0000-0000-0000-000000000000).
       */
      // const requestId = 'abc123'
    
      // Imports the Compute library
      const {RegionNetworkFirewallPoliciesClient} = require('[@google-cloud/compute](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const computeClient = new [RegionNetworkFirewallPoliciesClient](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)();
    
      async function callAddRule() {
        // Construct request
        const request = {
          firewallPolicy,
          firewallPolicyRuleResource,
          project,
          region,
        };
    
        // Run request
        const response = await computeClient.addRule(request);
        console.log(response);
      }
    
      callAddRule();
    
    

### addRule(request, options, callback)
    
    
    addRule(request: protos.google.cloud.compute.v1beta.IAddRuleRegionNetworkFirewallPolicyRequest, options: CallOptions, callback: Callback<protos.google.cloud.compute.v1beta.IOperation, protos.google.cloud.compute.v1beta.IAddRuleRegionNetworkFirewallPolicyRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IAddRuleRegionNetworkFirewallPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.iaddruleregionnetworkfirewallpolicyrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.compute.v1beta.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ioperation), [protos.google.cloud.compute.v1beta.IAddRuleRegionNetworkFirewallPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.iaddruleregionnetworkfirewallpolicyrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### addRule(request, callback)
    
    
    addRule(request: protos.google.cloud.compute.v1beta.IAddRuleRegionNetworkFirewallPolicyRequest, callback: Callback<protos.google.cloud.compute.v1beta.IOperation, protos.google.cloud.compute.v1beta.IAddRuleRegionNetworkFirewallPolicyRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IAddRuleRegionNetworkFirewallPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.iaddruleregionnetworkfirewallpolicyrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.compute.v1beta.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ioperation), [protos.google.cloud.compute.v1beta.IAddRuleRegionNetworkFirewallPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.iaddruleregionnetworkfirewallpolicyrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### cloneRules(request, options)
    
    
    cloneRules(request?: protos.google.cloud.compute.v1beta.ICloneRulesRegionNetworkFirewallPolicyRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.cloud.compute.v1beta.IOperation, null>,
            protos.google.cloud.compute.v1beta.IOperation | undefined,
            {} | undefined
        ]>;

Copies rules to the specified network firewall policy.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICloneRulesRegionNetworkFirewallPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.iclonerulesregionnetworkfirewallpolicyrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.cloud.compute.v1beta.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ioperation), null>, [protos.google.cloud.compute.v1beta.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples. This method is considered to be in beta. This means while stable it is still a work-in-progress and under active development, and might get backwards-incompatible changes at any time. `.promise()` is not supported yet.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Name of the firewall policy to update.
       */
      // const firewallPolicy = 'abc123'
      /**
       *  Project ID for this request.
       */
      // const project = 'my-project'
      /**
       *  Name of the region scoping this request.
       */
      // const region = 'us-central1'
      /**
       *  An optional request ID to identify requests. Specify a unique request ID so
       *  that if you must retry your request, the server will know to ignore the
       *  request if it has already been completed.
       *  For example, consider a situation where you make an initial request and
       *  the request times out. If you make the request again with the same
       *  request ID, the server can check if original operation with the same
       *  request ID was received, and if so, will ignore the second request. This
       *  prevents clients from accidentally creating duplicate commitments.
       *  The request ID must be
       *  a valid UUID with the exception that zero UUID is not supported
       *  (00000000-0000-0000-0000-000000000000).
       */
      // const requestId = 'abc123'
      /**
       *  The firewall policy from which to copy rules.
       */
      // const sourceFirewallPolicy = 'abc123'
    
      // Imports the Compute library
      const {RegionNetworkFirewallPoliciesClient} = require('[@google-cloud/compute](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const computeClient = new [RegionNetworkFirewallPoliciesClient](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)();
    
      async function callCloneRules() {
        // Construct request
        const request = {
          firewallPolicy,
          project,
          region,
        };
    
        // Run request
        const response = await computeClient.cloneRules(request);
        console.log(response);
      }
    
      callCloneRules();
    
    

### cloneRules(request, options, callback)
    
    
    cloneRules(request: protos.google.cloud.compute.v1beta.ICloneRulesRegionNetworkFirewallPolicyRequest, options: CallOptions, callback: Callback<protos.google.cloud.compute.v1beta.IOperation, protos.google.cloud.compute.v1beta.ICloneRulesRegionNetworkFirewallPolicyRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICloneRulesRegionNetworkFirewallPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.iclonerulesregionnetworkfirewallpolicyrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.compute.v1beta.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ioperation), [protos.google.cloud.compute.v1beta.ICloneRulesRegionNetworkFirewallPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.iclonerulesregionnetworkfirewallpolicyrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### cloneRules(request, callback)
    
    
    cloneRules(request: protos.google.cloud.compute.v1beta.ICloneRulesRegionNetworkFirewallPolicyRequest, callback: Callback<protos.google.cloud.compute.v1beta.IOperation, protos.google.cloud.compute.v1beta.ICloneRulesRegionNetworkFirewallPolicyRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICloneRulesRegionNetworkFirewallPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.iclonerulesregionnetworkfirewallpolicyrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.compute.v1beta.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ioperation), [protos.google.cloud.compute.v1beta.ICloneRulesRegionNetworkFirewallPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.iclonerulesregionnetworkfirewallpolicyrequest) | null | undefined, {} | null | undefined>`   
  
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
  
### delete(request, options)
    
    
    delete(request?: protos.google.cloud.compute.v1beta.IDeleteRegionNetworkFirewallPolicyRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.cloud.compute.v1beta.IOperation, null>,
            protos.google.cloud.compute.v1beta.IOperation | undefined,
            {} | undefined
        ]>;

Deletes the specified network firewall policy.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteRegionNetworkFirewallPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ideleteregionnetworkfirewallpolicyrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.cloud.compute.v1beta.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ioperation), null>, [protos.google.cloud.compute.v1beta.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples. This method is considered to be in beta. This means while stable it is still a work-in-progress and under active development, and might get backwards-incompatible changes at any time. `.promise()` is not supported yet.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Name of the firewall policy to delete.
       */
      // const firewallPolicy = 'abc123'
      /**
       *  Project ID for this request.
       */
      // const project = 'my-project'
      /**
       *  Name of the region scoping this request.
       */
      // const region = 'us-central1'
      /**
       *  An optional request ID to identify requests. Specify a unique request ID so
       *  that if you must retry your request, the server will know to ignore the
       *  request if it has already been completed.
       *  For example, consider a situation where you make an initial request and
       *  the request times out. If you make the request again with the same
       *  request ID, the server can check if original operation with the same
       *  request ID was received, and if so, will ignore the second request. This
       *  prevents clients from accidentally creating duplicate commitments.
       *  The request ID must be
       *  a valid UUID with the exception that zero UUID is not supported
       *  (00000000-0000-0000-0000-000000000000).
       */
      // const requestId = 'abc123'
    
      // Imports the Compute library
      const {RegionNetworkFirewallPoliciesClient} = require('[@google-cloud/compute](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const computeClient = new [RegionNetworkFirewallPoliciesClient](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)();
    
      async function callDelete() {
        // Construct request
        const request = {
          firewallPolicy,
          project,
          region,
        };
    
        // Run request
        const response = await computeClient.delete(request);
        console.log(response);
      }
    
      callDelete();
    
    

### delete(request, options, callback)
    
    
    delete(request: protos.google.cloud.compute.v1beta.IDeleteRegionNetworkFirewallPolicyRequest, options: CallOptions, callback: Callback<protos.google.cloud.compute.v1beta.IOperation, protos.google.cloud.compute.v1beta.IDeleteRegionNetworkFirewallPolicyRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteRegionNetworkFirewallPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ideleteregionnetworkfirewallpolicyrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.compute.v1beta.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ioperation), [protos.google.cloud.compute.v1beta.IDeleteRegionNetworkFirewallPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ideleteregionnetworkfirewallpolicyrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### delete(request, callback)
    
    
    delete(request: protos.google.cloud.compute.v1beta.IDeleteRegionNetworkFirewallPolicyRequest, callback: Callback<protos.google.cloud.compute.v1beta.IOperation, protos.google.cloud.compute.v1beta.IDeleteRegionNetworkFirewallPolicyRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteRegionNetworkFirewallPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ideleteregionnetworkfirewallpolicyrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.compute.v1beta.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ioperation), [protos.google.cloud.compute.v1beta.IDeleteRegionNetworkFirewallPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ideleteregionnetworkfirewallpolicyrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### get(request, options)
    
    
    get(request?: protos.google.cloud.compute.v1beta.IGetRegionNetworkFirewallPolicyRequest, options?: CallOptions): Promise<[
            protos.google.cloud.compute.v1beta.IFirewallPolicy,
            (protos.google.cloud.compute.v1beta.IGetRegionNetworkFirewallPolicyRequest | undefined),
            {} | undefined
        ]>;

Returns the specified network firewall policy.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetRegionNetworkFirewallPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.igetregionnetworkfirewallpolicyrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.compute.v1beta.IFirewallPolicy](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ifirewallpolicy), ([protos.google.cloud.compute.v1beta.IGetRegionNetworkFirewallPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.igetregionnetworkfirewallpolicyrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Name of the firewall policy to get.
       */
      // const firewallPolicy = 'abc123'
      /**
       *  Project ID for this request.
       */
      // const project = 'my-project'
      /**
       *  Name of the region scoping this request.
       */
      // const region = 'us-central1'
    
      // Imports the Compute library
      const {RegionNetworkFirewallPoliciesClient} = require('[@google-cloud/compute](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const computeClient = new [RegionNetworkFirewallPoliciesClient](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)();
    
      async function callGet() {
        // Construct request
        const request = {
          firewallPolicy,
          project,
          region,
        };
    
        // Run request
        const response = await computeClient.get(request);
        console.log(response);
      }
    
      callGet();
    
    

### get(request, options, callback)
    
    
    get(request: protos.google.cloud.compute.v1beta.IGetRegionNetworkFirewallPolicyRequest, options: CallOptions, callback: Callback<protos.google.cloud.compute.v1beta.IFirewallPolicy, protos.google.cloud.compute.v1beta.IGetRegionNetworkFirewallPolicyRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetRegionNetworkFirewallPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.igetregionnetworkfirewallpolicyrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.compute.v1beta.IFirewallPolicy](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ifirewallpolicy), [protos.google.cloud.compute.v1beta.IGetRegionNetworkFirewallPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.igetregionnetworkfirewallpolicyrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### get(request, callback)
    
    
    get(request: protos.google.cloud.compute.v1beta.IGetRegionNetworkFirewallPolicyRequest, callback: Callback<protos.google.cloud.compute.v1beta.IFirewallPolicy, protos.google.cloud.compute.v1beta.IGetRegionNetworkFirewallPolicyRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetRegionNetworkFirewallPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.igetregionnetworkfirewallpolicyrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.compute.v1beta.IFirewallPolicy](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ifirewallpolicy), [protos.google.cloud.compute.v1beta.IGetRegionNetworkFirewallPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.igetregionnetworkfirewallpolicyrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getAssociation(request, options)
    
    
    getAssociation(request?: protos.google.cloud.compute.v1beta.IGetAssociationRegionNetworkFirewallPolicyRequest, options?: CallOptions): Promise<[
            protos.google.cloud.compute.v1beta.IFirewallPolicyAssociation,
            (protos.google.cloud.compute.v1beta.IGetAssociationRegionNetworkFirewallPolicyRequest | undefined),
            {} | undefined
        ]>;

Gets an association with the specified name.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetAssociationRegionNetworkFirewallPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.igetassociationregionnetworkfirewallpolicyrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.compute.v1beta.IFirewallPolicyAssociation](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ifirewallpolicyassociation), ([protos.google.cloud.compute.v1beta.IGetAssociationRegionNetworkFirewallPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.igetassociationregionnetworkfirewallpolicyrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [FirewallPolicyAssociation](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.firewallpolicyassociation). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Name of the firewall policy to which the queried association belongs.
       */
      // const firewallPolicy = 'abc123'
      /**
       *  The name of the association to get from the firewall policy.
       */
      // const name = 'abc123'
      /**
       *  Project ID for this request.
       */
      // const project = 'my-project'
      /**
       *  Name of the region scoping this request.
       */
      // const region = 'us-central1'
    
      // Imports the Compute library
      const {RegionNetworkFirewallPoliciesClient} = require('[@google-cloud/compute](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const computeClient = new [RegionNetworkFirewallPoliciesClient](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)();
    
      async function callGetAssociation() {
        // Construct request
        const request = {
          firewallPolicy,
          project,
          region,
        };
    
        // Run request
        const response = await computeClient.getAssociation(request);
        console.log(response);
      }
    
      callGetAssociation();
    
    

### getAssociation(request, options, callback)
    
    
    getAssociation(request: protos.google.cloud.compute.v1beta.IGetAssociationRegionNetworkFirewallPolicyRequest, options: CallOptions, callback: Callback<protos.google.cloud.compute.v1beta.IFirewallPolicyAssociation, protos.google.cloud.compute.v1beta.IGetAssociationRegionNetworkFirewallPolicyRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetAssociationRegionNetworkFirewallPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.igetassociationregionnetworkfirewallpolicyrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.compute.v1beta.IFirewallPolicyAssociation](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ifirewallpolicyassociation), [protos.google.cloud.compute.v1beta.IGetAssociationRegionNetworkFirewallPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.igetassociationregionnetworkfirewallpolicyrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getAssociation(request, callback)
    
    
    getAssociation(request: protos.google.cloud.compute.v1beta.IGetAssociationRegionNetworkFirewallPolicyRequest, callback: Callback<protos.google.cloud.compute.v1beta.IFirewallPolicyAssociation, protos.google.cloud.compute.v1beta.IGetAssociationRegionNetworkFirewallPolicyRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetAssociationRegionNetworkFirewallPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.igetassociationregionnetworkfirewallpolicyrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.compute.v1beta.IFirewallPolicyAssociation](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ifirewallpolicyassociation), [protos.google.cloud.compute.v1beta.IGetAssociationRegionNetworkFirewallPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.igetassociationregionnetworkfirewallpolicyrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getEffectiveFirewalls(request, options)
    
    
    getEffectiveFirewalls(request?: protos.google.cloud.compute.v1beta.IGetEffectiveFirewallsRegionNetworkFirewallPolicyRequest, options?: CallOptions): Promise<[
            protos.google.cloud.compute.v1beta.IRegionNetworkFirewallPoliciesGetEffectiveFirewallsResponse,
            (protos.google.cloud.compute.v1beta.IGetEffectiveFirewallsRegionNetworkFirewallPolicyRequest | undefined),
            {} | undefined
        ]>;

Returns the effective firewalls on a given network.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetEffectiveFirewallsRegionNetworkFirewallPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.igeteffectivefirewallsregionnetworkfirewallpolicyrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.compute.v1beta.IRegionNetworkFirewallPoliciesGetEffectiveFirewallsResponse](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.iregionnetworkfirewallpoliciesgeteffectivefirewallsresponse), ([protos.google.cloud.compute.v1beta.IGetEffectiveFirewallsRegionNetworkFirewallPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.igeteffectivefirewallsregionnetworkfirewallpolicyrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [RegionNetworkFirewallPoliciesGetEffectiveFirewallsResponse](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.regionnetworkfirewallpoliciesgeteffectivefirewallsresponse). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Network reference
       */
      // const network = 'abc123'
      /**
       *  Project ID for this request.
       */
      // const project = 'my-project'
      /**
       *  Name of the region scoping this request.
       */
      // const region = 'us-central1'
    
      // Imports the Compute library
      const {RegionNetworkFirewallPoliciesClient} = require('[@google-cloud/compute](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const computeClient = new [RegionNetworkFirewallPoliciesClient](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)();
    
      async function callGetEffectiveFirewalls() {
        // Construct request
        const request = {
          network,
          project,
          region,
        };
    
        // Run request
        const response = await computeClient.getEffectiveFirewalls(request);
        console.log(response);
      }
    
      callGetEffectiveFirewalls();
    
    

### getEffectiveFirewalls(request, options, callback)
    
    
    getEffectiveFirewalls(request: protos.google.cloud.compute.v1beta.IGetEffectiveFirewallsRegionNetworkFirewallPolicyRequest, options: CallOptions, callback: Callback<protos.google.cloud.compute.v1beta.IRegionNetworkFirewallPoliciesGetEffectiveFirewallsResponse, protos.google.cloud.compute.v1beta.IGetEffectiveFirewallsRegionNetworkFirewallPolicyRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetEffectiveFirewallsRegionNetworkFirewallPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.igeteffectivefirewallsregionnetworkfirewallpolicyrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.compute.v1beta.IRegionNetworkFirewallPoliciesGetEffectiveFirewallsResponse](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.iregionnetworkfirewallpoliciesgeteffectivefirewallsresponse), [protos.google.cloud.compute.v1beta.IGetEffectiveFirewallsRegionNetworkFirewallPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.igeteffectivefirewallsregionnetworkfirewallpolicyrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getEffectiveFirewalls(request, callback)
    
    
    getEffectiveFirewalls(request: protos.google.cloud.compute.v1beta.IGetEffectiveFirewallsRegionNetworkFirewallPolicyRequest, callback: Callback<protos.google.cloud.compute.v1beta.IRegionNetworkFirewallPoliciesGetEffectiveFirewallsResponse, protos.google.cloud.compute.v1beta.IGetEffectiveFirewallsRegionNetworkFirewallPolicyRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetEffectiveFirewallsRegionNetworkFirewallPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.igeteffectivefirewallsregionnetworkfirewallpolicyrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.compute.v1beta.IRegionNetworkFirewallPoliciesGetEffectiveFirewallsResponse](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.iregionnetworkfirewallpoliciesgeteffectivefirewallsresponse), [protos.google.cloud.compute.v1beta.IGetEffectiveFirewallsRegionNetworkFirewallPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.igeteffectivefirewallsregionnetworkfirewallpolicyrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getIamPolicy(request, options)
    
    
    getIamPolicy(request?: protos.google.cloud.compute.v1beta.IGetIamPolicyRegionNetworkFirewallPolicyRequest, options?: CallOptions): Promise<[
            protos.google.cloud.compute.v1beta.IPolicy,
            (protos.google.cloud.compute.v1beta.IGetIamPolicyRegionNetworkFirewallPolicyRequest | undefined),
            {} | undefined
        ]>;

Gets the access control policy for a resource. May be empty if no such policy or resource exists.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetIamPolicyRegionNetworkFirewallPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.igetiampolicyregionnetworkfirewallpolicyrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.compute.v1beta.IPolicy](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ipolicy), ([protos.google.cloud.compute.v1beta.IGetIamPolicyRegionNetworkFirewallPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.igetiampolicyregionnetworkfirewallpolicyrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [Policy](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.policy). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Requested IAM Policy version.
       */
      // const optionsRequestedPolicyVersion = 1234
      /**
       *  Project ID for this request.
       */
      // const project = 'my-project'
      /**
       *  The name of the region for this request.
       */
      // const region = 'us-central1'
      /**
       *  Name or id of the resource for this request.
       */
      // const resource = 'abc123'
    
      // Imports the Compute library
      const {RegionNetworkFirewallPoliciesClient} = require('[@google-cloud/compute](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const computeClient = new [RegionNetworkFirewallPoliciesClient](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)();
    
      async function callGetIamPolicy() {
        // Construct request
        const request = {
          project,
          region,
          resource,
        };
    
        // Run request
        const response = await computeClient.getIamPolicy(request);
        console.log(response);
      }
    
      callGetIamPolicy();
    
    

### getIamPolicy(request, options, callback)
    
    
    getIamPolicy(request: protos.google.cloud.compute.v1beta.IGetIamPolicyRegionNetworkFirewallPolicyRequest, options: CallOptions, callback: Callback<protos.google.cloud.compute.v1beta.IPolicy, protos.google.cloud.compute.v1beta.IGetIamPolicyRegionNetworkFirewallPolicyRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetIamPolicyRegionNetworkFirewallPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.igetiampolicyregionnetworkfirewallpolicyrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.compute.v1beta.IPolicy](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ipolicy), [protos.google.cloud.compute.v1beta.IGetIamPolicyRegionNetworkFirewallPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.igetiampolicyregionnetworkfirewallpolicyrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getIamPolicy(request, callback)
    
    
    getIamPolicy(request: protos.google.cloud.compute.v1beta.IGetIamPolicyRegionNetworkFirewallPolicyRequest, callback: Callback<protos.google.cloud.compute.v1beta.IPolicy, protos.google.cloud.compute.v1beta.IGetIamPolicyRegionNetworkFirewallPolicyRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetIamPolicyRegionNetworkFirewallPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.igetiampolicyregionnetworkfirewallpolicyrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.compute.v1beta.IPolicy](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ipolicy), [protos.google.cloud.compute.v1beta.IGetIamPolicyRegionNetworkFirewallPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.igetiampolicyregionnetworkfirewallpolicyrequest) | null | undefined, {} | null | undefined>`   
  
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
  
### getRule(request, options)
    
    
    getRule(request?: protos.google.cloud.compute.v1beta.IGetRuleRegionNetworkFirewallPolicyRequest, options?: CallOptions): Promise<[
            protos.google.cloud.compute.v1beta.IFirewallPolicyRule,
            (protos.google.cloud.compute.v1beta.IGetRuleRegionNetworkFirewallPolicyRequest | undefined),
            {} | undefined
        ]>;

Gets a rule of the specified priority.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetRuleRegionNetworkFirewallPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.igetruleregionnetworkfirewallpolicyrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.compute.v1beta.IFirewallPolicyRule](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ifirewallpolicyrule), ([protos.google.cloud.compute.v1beta.IGetRuleRegionNetworkFirewallPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.igetruleregionnetworkfirewallpolicyrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Name of the firewall policy to which the queried rule belongs.
       */
      // const firewallPolicy = 'abc123'
      /**
       *  The priority of the rule to get from the firewall policy.
       */
      // const priority = 1234
      /**
       *  Project ID for this request.
       */
      // const project = 'my-project'
      /**
       *  Name of the region scoping this request.
       */
      // const region = 'us-central1'
    
      // Imports the Compute library
      const {RegionNetworkFirewallPoliciesClient} = require('[@google-cloud/compute](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const computeClient = new [RegionNetworkFirewallPoliciesClient](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)();
    
      async function callGetRule() {
        // Construct request
        const request = {
          firewallPolicy,
          project,
          region,
        };
    
        // Run request
        const response = await computeClient.getRule(request);
        console.log(response);
      }
    
      callGetRule();
    
    

### getRule(request, options, callback)
    
    
    getRule(request: protos.google.cloud.compute.v1beta.IGetRuleRegionNetworkFirewallPolicyRequest, options: CallOptions, callback: Callback<protos.google.cloud.compute.v1beta.IFirewallPolicyRule, protos.google.cloud.compute.v1beta.IGetRuleRegionNetworkFirewallPolicyRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetRuleRegionNetworkFirewallPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.igetruleregionnetworkfirewallpolicyrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.compute.v1beta.IFirewallPolicyRule](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ifirewallpolicyrule), [protos.google.cloud.compute.v1beta.IGetRuleRegionNetworkFirewallPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.igetruleregionnetworkfirewallpolicyrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getRule(request, callback)
    
    
    getRule(request: protos.google.cloud.compute.v1beta.IGetRuleRegionNetworkFirewallPolicyRequest, callback: Callback<protos.google.cloud.compute.v1beta.IFirewallPolicyRule, protos.google.cloud.compute.v1beta.IGetRuleRegionNetworkFirewallPolicyRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetRuleRegionNetworkFirewallPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.igetruleregionnetworkfirewallpolicyrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.compute.v1beta.IFirewallPolicyRule](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ifirewallpolicyrule), [protos.google.cloud.compute.v1beta.IGetRuleRegionNetworkFirewallPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.igetruleregionnetworkfirewallpolicyrequest) | null | undefined, {} | null | undefined>`   
  
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
  
### insert(request, options)
    
    
    insert(request?: protos.google.cloud.compute.v1beta.IInsertRegionNetworkFirewallPolicyRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.cloud.compute.v1beta.IOperation, null>,
            protos.google.cloud.compute.v1beta.IOperation | undefined,
            {} | undefined
        ]>;

Creates a new network firewall policy in the specified project and region.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IInsertRegionNetworkFirewallPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.iinsertregionnetworkfirewallpolicyrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.cloud.compute.v1beta.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ioperation), null>, [protos.google.cloud.compute.v1beta.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples. This method is considered to be in beta. This means while stable it is still a work-in-progress and under active development, and might get backwards-incompatible changes at any time. `.promise()` is not supported yet.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  The body resource for this request
       */
      // const firewallPolicyResource = {}
      /**
       *  Project ID for this request.
       */
      // const project = 'my-project'
      /**
       *  Name of the region scoping this request.
       */
      // const region = 'us-central1'
      /**
       *  An optional request ID to identify requests. Specify a unique request ID
       *  so that if you must retry your request, the server will know to ignore the
       *  request if it has already been completed.
       *  For example, consider a situation where you make an initial request and
       *  the request times out. If you make the request again with the same
       *  request ID, the server can check if original operation with the same
       *  request ID was received, and if so, will ignore the second request. This
       *  prevents clients from accidentally creating duplicate commitments.
       *  The request ID must be
       *  a valid UUID with the exception that zero UUID is not supported
       *  (00000000-0000-0000-0000-000000000000).
       */
      // const requestId = 'abc123'
    
      // Imports the Compute library
      const {RegionNetworkFirewallPoliciesClient} = require('[@google-cloud/compute](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const computeClient = new [RegionNetworkFirewallPoliciesClient](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)();
    
      async function callInsert() {
        // Construct request
        const request = {
          firewallPolicyResource,
          project,
          region,
        };
    
        // Run request
        const response = await computeClient.insert(request);
        console.log(response);
      }
    
      callInsert();
    
    

### insert(request, options, callback)
    
    
    insert(request: protos.google.cloud.compute.v1beta.IInsertRegionNetworkFirewallPolicyRequest, options: CallOptions, callback: Callback<protos.google.cloud.compute.v1beta.IOperation, protos.google.cloud.compute.v1beta.IInsertRegionNetworkFirewallPolicyRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IInsertRegionNetworkFirewallPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.iinsertregionnetworkfirewallpolicyrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.compute.v1beta.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ioperation), [protos.google.cloud.compute.v1beta.IInsertRegionNetworkFirewallPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.iinsertregionnetworkfirewallpolicyrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### insert(request, callback)
    
    
    insert(request: protos.google.cloud.compute.v1beta.IInsertRegionNetworkFirewallPolicyRequest, callback: Callback<protos.google.cloud.compute.v1beta.IOperation, protos.google.cloud.compute.v1beta.IInsertRegionNetworkFirewallPolicyRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IInsertRegionNetworkFirewallPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.iinsertregionnetworkfirewallpolicyrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.compute.v1beta.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ioperation), [protos.google.cloud.compute.v1beta.IInsertRegionNetworkFirewallPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.iinsertregionnetworkfirewallpolicyrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### list(request, options)
    
    
    list(request?: protos.google.cloud.compute.v1beta.IListRegionNetworkFirewallPoliciesRequest, options?: CallOptions): Promise<[
            protos.google.cloud.compute.v1beta.IFirewallPolicy[],
            protos.google.cloud.compute.v1beta.IListRegionNetworkFirewallPoliciesRequest | null,
            protos.google.cloud.compute.v1beta.IFirewallPolicyList
        ]>;

Lists all the network firewall policies that have been configured for the specified project in the given region.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListRegionNetworkFirewallPoliciesRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ilistregionnetworkfirewallpoliciesrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.compute.v1beta.IFirewallPolicy](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ifirewallpolicy)[], [protos.google.cloud.compute.v1beta.IListRegionNetworkFirewallPoliciesRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ilistregionnetworkfirewallpoliciesrequest) | null, [protos.google.cloud.compute.v1beta.IFirewallPolicyList](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ifirewallpolicylist) ]>` | {Promise} - The promise which resolves to an array. The first element of the array is Array of . The client library will perform auto-pagination by default: it will call the API as many times as needed and will merge results from all the pages into this array. Note that it can affect your quota. We recommend using `listAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### list(request, options, callback)
    
    
    list(request: protos.google.cloud.compute.v1beta.IListRegionNetworkFirewallPoliciesRequest, options: CallOptions, callback: PaginationCallback<protos.google.cloud.compute.v1beta.IListRegionNetworkFirewallPoliciesRequest, protos.google.cloud.compute.v1beta.IFirewallPolicyList | null | undefined, protos.google.cloud.compute.v1beta.IFirewallPolicy>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListRegionNetworkFirewallPoliciesRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ilistregionnetworkfirewallpoliciesrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.compute.v1beta.IListRegionNetworkFirewallPoliciesRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ilistregionnetworkfirewallpoliciesrequest), [protos.google.cloud.compute.v1beta.IFirewallPolicyList](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ifirewallpolicylist) | null | undefined, [protos.google.cloud.compute.v1beta.IFirewallPolicy](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ifirewallpolicy)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### list(request, callback)
    
    
    list(request: protos.google.cloud.compute.v1beta.IListRegionNetworkFirewallPoliciesRequest, callback: PaginationCallback<protos.google.cloud.compute.v1beta.IListRegionNetworkFirewallPoliciesRequest, protos.google.cloud.compute.v1beta.IFirewallPolicyList | null | undefined, protos.google.cloud.compute.v1beta.IFirewallPolicy>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListRegionNetworkFirewallPoliciesRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ilistregionnetworkfirewallpoliciesrequest)`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.compute.v1beta.IListRegionNetworkFirewallPoliciesRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ilistregionnetworkfirewallpoliciesrequest), [protos.google.cloud.compute.v1beta.IFirewallPolicyList](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ifirewallpolicylist) | null | undefined, [protos.google.cloud.compute.v1beta.IFirewallPolicy](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ifirewallpolicy)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listAsync(request, options)
    
    
    listAsync(request?: protos.google.cloud.compute.v1beta.IListRegionNetworkFirewallPoliciesRequest, options?: CallOptions): AsyncIterable<protos.google.cloud.compute.v1beta.IFirewallPolicy>;

Equivalent to `list`, but returns an iterable object.

`for`-`await`-`of` syntax is used with the iterable to get response elements on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListRegionNetworkFirewallPoliciesRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ilistregionnetworkfirewallpoliciesrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.cloud.compute.v1beta.IFirewallPolicy](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ifirewallpolicy)>` | {Object} An iterable Object that allows [async iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols). When you iterate the returned iterable, each element will be an object representing . The API will be called under the hood as needed, once per the page, so you can stop the iteration when you don't need more results. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  A filter expression that filters resources listed in the response. Most
       *  Compute resources support two types of filter expressions:
       *  expressions that support regular expressions and expressions that follow
       *  API improvement proposal AIP-160.
       *  These two types of filter expressions cannot be mixed in one request.
       *  If you want to use AIP-160, your expression must specify the field name, an
       *  operator, and the value that you want to use for filtering. The value
       *  must be a string, a number, or a boolean. The operator
       *  must be either `=`, `!=`, `>`, `<`,><=`, `="">=` or `:`.
       *  For example, if you are filtering Compute Engine instances, you can
       *  exclude instances named `example-instance` by specifying
       *  `name != example-instance`.
       *  The `:*` comparison can be used to test whether a key has been defined.
       *  For example, to find all objects with `owner` label use:
       *  
    
    
       *  labels.owner:*
       *  

`

  * You can also filter nested fields. For example, you could specify
  * `scheduling.automaticRestart = false` to include instances only
  * if they are not scheduled for automatic restarts. You can use filtering
  * on nested fields to filter based onresource labels.
  * To filter on multiple expressions, provide each separate expression within
  * parentheses. For example:
  *   * (scheduling.automaticRestart = true)
  * (cpuPlatform = "Intel Skylake")
  *   * By default, each expression is an `AND` expression. However, you
  * can include `AND` and `OR` expressions explicitly.
  * For example:
  *   * (cpuPlatform = "Intel Skylake") OR
  * (cpuPlatform = "Intel Broadwell") AND
  * (scheduling.automaticRestart = true)
  *   * If you want to use a regular expression, use the `eq` (equal) or `ne`
  * (not equal) operator against a single un-parenthesized expression with or
  * without quotes or against multiple parenthesized expressions. Examples:
  * `fieldname eq unquoted literal`
  * `fieldname eq 'single quoted literal'`
  * `fieldname eq "double quoted literal"`
  * `(fieldname1 eq literal) (fieldname2 ne "literal")`
  * The literal value is interpreted as a regular expression using GoogleRE2 library syntax.
  * The literal value must match the entire field.
  * For example, to filter for instances that do not end with name "instance",
  * you would use `name ne .*instance`.
  * You cannot combine constraints on multiple fields using regular
  * expressions. _/ // const filter = 'abc123' /_ *
  * The maximum number of results per page that should be returned.
  * If the number of available results is larger than `maxResults`,
  * Compute Engine returns a `nextPageToken` that can be used to get
  * the next page of results in subsequent list requests. Acceptable values are
  * `0` to `500`, inclusive. (Default: `500`) _/ // const maxResults = 1234 /_ *
  * Sorts list results by a certain order. By default, results
  * are returned in alphanumerical order based on the resource name.
  * You can also sort results in descending order based on the creation
  * timestamp using `orderBy="creationTimestamp desc"`. This sorts
  * results based on the `creationTimestamp` field in
  * reverse chronological order (newest result first). Use this to sort
  * resources like operations so that the newest operation is returned first.
  * Currently, only sorting by `name` or
  * `creationTimestamp desc` is supported. _/ // const orderBy = 'abc123' /_ *
  * Specifies a page token to use. Set `pageToken` to the
  * `nextPageToken` returned by a previous list request to get
  * the next page of results. _/ // const pageToken = 'abc123' /_ *
  * Project ID for this request. _/ // const project = 'my-project' /_ *
  * Name of the region scoping this request. _/ // const region = 'us-central1' /_ *
  * Opt-in for partial success behavior which provides partial results in case
  * of failure. The default value is false.
  * For example, when partial success behavior is enabled, aggregatedList for a
  * single zone scope either returns all resources in the zone or no resources,
  * with an error code. */ // const returnPartialSuccess = true

// Imports the Compute library const {RegionNetworkFirewallPoliciesClient} = require('@google-cloud/compute').v1beta;

// Instantiates a client const computeClient = new RegionNetworkFirewallPoliciesClient();

async function callList() { // Construct request const request = { project, region, };

// Run request const iterable = computeClient.listAsync(request); for await (const response of iterable) { console.log(response); } }

callList();




` `

### listStream(request, options)
    
    
    listStream(request?: protos.google.cloud.compute.v1beta.IListRegionNetworkFirewallPoliciesRequest, options?: CallOptions): Transform;

Equivalent to `list`, but returns a NodeJS Stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListRegionNetworkFirewallPoliciesRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ilistregionnetworkfirewallpoliciesrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Transform` | {Stream} An object stream which emits an object representing on 'data' event. The client library will perform auto-pagination by default: it will call the API as many times as needed. Note that it can affect your quota. We recommend using `listAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### patch(request, options)
    
    
    patch(request?: protos.google.cloud.compute.v1beta.IPatchRegionNetworkFirewallPolicyRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.cloud.compute.v1beta.IOperation, null>,
            protos.google.cloud.compute.v1beta.IOperation | undefined,
            {} | undefined
        ]>;

Patches the specified network firewall policy.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IPatchRegionNetworkFirewallPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ipatchregionnetworkfirewallpolicyrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.cloud.compute.v1beta.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ioperation), null>, [protos.google.cloud.compute.v1beta.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples. This method is considered to be in beta. This means while stable it is still a work-in-progress and under active development, and might get backwards-incompatible changes at any time. `.promise()` is not supported yet.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Name of the firewall policy to update.
       */
      // const firewallPolicy = 'abc123'
      /**
       *  The body resource for this request
       */
      // const firewallPolicyResource = {}
      /**
       *  Project ID for this request.
       */
      // const project = 'my-project'
      /**
       *  Name of the region scoping this request.
       */
      // const region = 'us-central1'
      /**
       *  An optional request ID to identify requests. Specify a unique request ID so
       *  that if you must retry your request, the server will know to ignore the
       *  request if it has already been completed.
       *  For example, consider a situation where you make an initial request and
       *  the request times out. If you make the request again with the same
       *  request ID, the server can check if original operation with the same
       *  request ID was received, and if so, will ignore the second request. This
       *  prevents clients from accidentally creating duplicate commitments.
       *  The request ID must be
       *  a valid UUID with the exception that zero UUID is not supported
       *  (00000000-0000-0000-0000-000000000000).
       */
      // const requestId = 'abc123'
    
      // Imports the Compute library
      const {RegionNetworkFirewallPoliciesClient} = require('[@google-cloud/compute](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const computeClient = new [RegionNetworkFirewallPoliciesClient](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)();
    
      async function callPatch() {
        // Construct request
        const request = {
          firewallPolicy,
          firewallPolicyResource,
          project,
          region,
        };
    
        // Run request
        const response = await computeClient.patch(request);
        console.log(response);
      }
    
      callPatch();
    
    

### patch(request, options, callback)
    
    
    patch(request: protos.google.cloud.compute.v1beta.IPatchRegionNetworkFirewallPolicyRequest, options: CallOptions, callback: Callback<protos.google.cloud.compute.v1beta.IOperation, protos.google.cloud.compute.v1beta.IPatchRegionNetworkFirewallPolicyRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IPatchRegionNetworkFirewallPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ipatchregionnetworkfirewallpolicyrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.compute.v1beta.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ioperation), [protos.google.cloud.compute.v1beta.IPatchRegionNetworkFirewallPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ipatchregionnetworkfirewallpolicyrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### patch(request, callback)
    
    
    patch(request: protos.google.cloud.compute.v1beta.IPatchRegionNetworkFirewallPolicyRequest, callback: Callback<protos.google.cloud.compute.v1beta.IOperation, protos.google.cloud.compute.v1beta.IPatchRegionNetworkFirewallPolicyRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IPatchRegionNetworkFirewallPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ipatchregionnetworkfirewallpolicyrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.compute.v1beta.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ioperation), [protos.google.cloud.compute.v1beta.IPatchRegionNetworkFirewallPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ipatchregionnetworkfirewallpolicyrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### patchAssociation(request, options)
    
    
    patchAssociation(request?: protos.google.cloud.compute.v1beta.IPatchAssociationRegionNetworkFirewallPolicyRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.cloud.compute.v1beta.IOperation, null>,
            protos.google.cloud.compute.v1beta.IOperation | undefined,
            {} | undefined
        ]>;

Updates an association for the specified network firewall policy.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IPatchAssociationRegionNetworkFirewallPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ipatchassociationregionnetworkfirewallpolicyrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.cloud.compute.v1beta.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ioperation), null>, [protos.google.cloud.compute.v1beta.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples. This method is considered to be in beta. This means while stable it is still a work-in-progress and under active development, and might get backwards-incompatible changes at any time. `.promise()` is not supported yet.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Name of the firewall policy to update.
       */
      // const firewallPolicy = 'abc123'
      /**
       *  The body resource for this request
       */
      // const firewallPolicyAssociationResource = {}
      /**
       *  Project ID for this request.
       */
      // const project = 'my-project'
      /**
       *  Name of the region scoping this request.
       */
      // const region = 'us-central1'
      /**
       *  An optional request ID to identify requests. Specify a unique request ID so
       *  that if you must retry your request, the server will know to ignore the
       *  request if it has already been completed.
       *  For example, consider a situation where you make an initial request and
       *  the request times out. If you make the request again with the same
       *  request ID, the server can check if original operation with the same
       *  request ID was received, and if so, will ignore the second request. This
       *  prevents clients from accidentally creating duplicate commitments.
       *  The request ID must be
       *  a valid UUID with the exception that zero UUID is not supported
       *  (00000000-0000-0000-0000-000000000000).
       */
      // const requestId = 'abc123'
    
      // Imports the Compute library
      const {RegionNetworkFirewallPoliciesClient} = require('[@google-cloud/compute](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const computeClient = new [RegionNetworkFirewallPoliciesClient](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)();
    
      async function callPatchAssociation() {
        // Construct request
        const request = {
          firewallPolicy,
          firewallPolicyAssociationResource,
          project,
          region,
        };
    
        // Run request
        const response = await computeClient.patchAssociation(request);
        console.log(response);
      }
    
      callPatchAssociation();
    
    

### patchAssociation(request, options, callback)
    
    
    patchAssociation(request: protos.google.cloud.compute.v1beta.IPatchAssociationRegionNetworkFirewallPolicyRequest, options: CallOptions, callback: Callback<protos.google.cloud.compute.v1beta.IOperation, protos.google.cloud.compute.v1beta.IPatchAssociationRegionNetworkFirewallPolicyRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IPatchAssociationRegionNetworkFirewallPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ipatchassociationregionnetworkfirewallpolicyrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.compute.v1beta.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ioperation), [protos.google.cloud.compute.v1beta.IPatchAssociationRegionNetworkFirewallPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ipatchassociationregionnetworkfirewallpolicyrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### patchAssociation(request, callback)
    
    
    patchAssociation(request: protos.google.cloud.compute.v1beta.IPatchAssociationRegionNetworkFirewallPolicyRequest, callback: Callback<protos.google.cloud.compute.v1beta.IOperation, protos.google.cloud.compute.v1beta.IPatchAssociationRegionNetworkFirewallPolicyRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IPatchAssociationRegionNetworkFirewallPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ipatchassociationregionnetworkfirewallpolicyrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.compute.v1beta.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ioperation), [protos.google.cloud.compute.v1beta.IPatchAssociationRegionNetworkFirewallPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ipatchassociationregionnetworkfirewallpolicyrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### patchRule(request, options)
    
    
    patchRule(request?: protos.google.cloud.compute.v1beta.IPatchRuleRegionNetworkFirewallPolicyRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.cloud.compute.v1beta.IOperation, null>,
            protos.google.cloud.compute.v1beta.IOperation | undefined,
            {} | undefined
        ]>;

Patches a rule of the specified priority.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IPatchRuleRegionNetworkFirewallPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ipatchruleregionnetworkfirewallpolicyrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.cloud.compute.v1beta.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ioperation), null>, [protos.google.cloud.compute.v1beta.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples. This method is considered to be in beta. This means while stable it is still a work-in-progress and under active development, and might get backwards-incompatible changes at any time. `.promise()` is not supported yet.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Name of the firewall policy to update.
       */
      // const firewallPolicy = 'abc123'
      /**
       *  The body resource for this request
       */
      // const firewallPolicyRuleResource = {}
      /**
       *  The priority of the rule to patch.
       */
      // const priority = 1234
      /**
       *  Project ID for this request.
       */
      // const project = 'my-project'
      /**
       *  Name of the region scoping this request.
       */
      // const region = 'us-central1'
      /**
       *  An optional request ID to identify requests. Specify a unique request ID so
       *  that if you must retry your request, the server will know to ignore the
       *  request if it has already been completed.
       *  For example, consider a situation where you make an initial request and
       *  the request times out. If you make the request again with the same
       *  request ID, the server can check if original operation with the same
       *  request ID was received, and if so, will ignore the second request. This
       *  prevents clients from accidentally creating duplicate commitments.
       *  The request ID must be
       *  a valid UUID with the exception that zero UUID is not supported
       *  (00000000-0000-0000-0000-000000000000).
       */
      // const requestId = 'abc123'
    
      // Imports the Compute library
      const {RegionNetworkFirewallPoliciesClient} = require('[@google-cloud/compute](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const computeClient = new [RegionNetworkFirewallPoliciesClient](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)();
    
      async function callPatchRule() {
        // Construct request
        const request = {
          firewallPolicy,
          firewallPolicyRuleResource,
          project,
          region,
        };
    
        // Run request
        const response = await computeClient.patchRule(request);
        console.log(response);
      }
    
      callPatchRule();
    
    

### patchRule(request, options, callback)
    
    
    patchRule(request: protos.google.cloud.compute.v1beta.IPatchRuleRegionNetworkFirewallPolicyRequest, options: CallOptions, callback: Callback<protos.google.cloud.compute.v1beta.IOperation, protos.google.cloud.compute.v1beta.IPatchRuleRegionNetworkFirewallPolicyRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IPatchRuleRegionNetworkFirewallPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ipatchruleregionnetworkfirewallpolicyrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.compute.v1beta.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ioperation), [protos.google.cloud.compute.v1beta.IPatchRuleRegionNetworkFirewallPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ipatchruleregionnetworkfirewallpolicyrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### patchRule(request, callback)
    
    
    patchRule(request: protos.google.cloud.compute.v1beta.IPatchRuleRegionNetworkFirewallPolicyRequest, callback: Callback<protos.google.cloud.compute.v1beta.IOperation, protos.google.cloud.compute.v1beta.IPatchRuleRegionNetworkFirewallPolicyRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IPatchRuleRegionNetworkFirewallPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ipatchruleregionnetworkfirewallpolicyrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.compute.v1beta.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ioperation), [protos.google.cloud.compute.v1beta.IPatchRuleRegionNetworkFirewallPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ipatchruleregionnetworkfirewallpolicyrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### removeAssociation(request, options)
    
    
    removeAssociation(request?: protos.google.cloud.compute.v1beta.IRemoveAssociationRegionNetworkFirewallPolicyRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.cloud.compute.v1beta.IOperation, null>,
            protos.google.cloud.compute.v1beta.IOperation | undefined,
            {} | undefined
        ]>;

Removes an association for the specified network firewall policy.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IRemoveAssociationRegionNetworkFirewallPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.iremoveassociationregionnetworkfirewallpolicyrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.cloud.compute.v1beta.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ioperation), null>, [protos.google.cloud.compute.v1beta.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples. This method is considered to be in beta. This means while stable it is still a work-in-progress and under active development, and might get backwards-incompatible changes at any time. `.promise()` is not supported yet.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Name of the firewall policy to update.
       */
      // const firewallPolicy = 'abc123'
      /**
       *  Name for the association that will be removed.
       */
      // const name = 'abc123'
      /**
       *  Project ID for this request.
       */
      // const project = 'my-project'
      /**
       *  Name of the region scoping this request.
       */
      // const region = 'us-central1'
      /**
       *  An optional request ID to identify requests. Specify a unique request ID so
       *  that if you must retry your request, the server will know to ignore the
       *  request if it has already been completed.
       *  For example, consider a situation where you make an initial request and
       *  the request times out. If you make the request again with the same
       *  request ID, the server can check if original operation with the same
       *  request ID was received, and if so, will ignore the second request. This
       *  prevents clients from accidentally creating duplicate commitments.
       *  The request ID must be
       *  a valid UUID with the exception that zero UUID is not supported
       *  (00000000-0000-0000-0000-000000000000).
       */
      // const requestId = 'abc123'
    
      // Imports the Compute library
      const {RegionNetworkFirewallPoliciesClient} = require('[@google-cloud/compute](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const computeClient = new [RegionNetworkFirewallPoliciesClient](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)();
    
      async function callRemoveAssociation() {
        // Construct request
        const request = {
          firewallPolicy,
          project,
          region,
        };
    
        // Run request
        const response = await computeClient.removeAssociation(request);
        console.log(response);
      }
    
      callRemoveAssociation();
    
    

### removeAssociation(request, options, callback)
    
    
    removeAssociation(request: protos.google.cloud.compute.v1beta.IRemoveAssociationRegionNetworkFirewallPolicyRequest, options: CallOptions, callback: Callback<protos.google.cloud.compute.v1beta.IOperation, protos.google.cloud.compute.v1beta.IRemoveAssociationRegionNetworkFirewallPolicyRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IRemoveAssociationRegionNetworkFirewallPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.iremoveassociationregionnetworkfirewallpolicyrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.compute.v1beta.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ioperation), [protos.google.cloud.compute.v1beta.IRemoveAssociationRegionNetworkFirewallPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.iremoveassociationregionnetworkfirewallpolicyrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### removeAssociation(request, callback)
    
    
    removeAssociation(request: protos.google.cloud.compute.v1beta.IRemoveAssociationRegionNetworkFirewallPolicyRequest, callback: Callback<protos.google.cloud.compute.v1beta.IOperation, protos.google.cloud.compute.v1beta.IRemoveAssociationRegionNetworkFirewallPolicyRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IRemoveAssociationRegionNetworkFirewallPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.iremoveassociationregionnetworkfirewallpolicyrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.compute.v1beta.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ioperation), [protos.google.cloud.compute.v1beta.IRemoveAssociationRegionNetworkFirewallPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.iremoveassociationregionnetworkfirewallpolicyrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### removeRule(request, options)
    
    
    removeRule(request?: protos.google.cloud.compute.v1beta.IRemoveRuleRegionNetworkFirewallPolicyRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.cloud.compute.v1beta.IOperation, null>,
            protos.google.cloud.compute.v1beta.IOperation | undefined,
            {} | undefined
        ]>;

Deletes a rule of the specified priority.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IRemoveRuleRegionNetworkFirewallPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.iremoveruleregionnetworkfirewallpolicyrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.cloud.compute.v1beta.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ioperation), null>, [protos.google.cloud.compute.v1beta.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples. This method is considered to be in beta. This means while stable it is still a work-in-progress and under active development, and might get backwards-incompatible changes at any time. `.promise()` is not supported yet.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Name of the firewall policy to update.
       */
      // const firewallPolicy = 'abc123'
      /**
       *  The priority of the rule to remove from the firewall policy.
       */
      // const priority = 1234
      /**
       *  Project ID for this request.
       */
      // const project = 'my-project'
      /**
       *  Name of the region scoping this request.
       */
      // const region = 'us-central1'
      /**
       *  An optional request ID to identify requests. Specify a unique request ID so
       *  that if you must retry your request, the server will know to ignore the
       *  request if it has already been completed.
       *  For example, consider a situation where you make an initial request and
       *  the request times out. If you make the request again with the same
       *  request ID, the server can check if original operation with the same
       *  request ID was received, and if so, will ignore the second request. This
       *  prevents clients from accidentally creating duplicate commitments.
       *  The request ID must be
       *  a valid UUID with the exception that zero UUID is not supported
       *  (00000000-0000-0000-0000-000000000000).
       */
      // const requestId = 'abc123'
    
      // Imports the Compute library
      const {RegionNetworkFirewallPoliciesClient} = require('[@google-cloud/compute](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const computeClient = new [RegionNetworkFirewallPoliciesClient](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)();
    
      async function callRemoveRule() {
        // Construct request
        const request = {
          firewallPolicy,
          project,
          region,
        };
    
        // Run request
        const response = await computeClient.removeRule(request);
        console.log(response);
      }
    
      callRemoveRule();
    
    

### removeRule(request, options, callback)
    
    
    removeRule(request: protos.google.cloud.compute.v1beta.IRemoveRuleRegionNetworkFirewallPolicyRequest, options: CallOptions, callback: Callback<protos.google.cloud.compute.v1beta.IOperation, protos.google.cloud.compute.v1beta.IRemoveRuleRegionNetworkFirewallPolicyRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IRemoveRuleRegionNetworkFirewallPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.iremoveruleregionnetworkfirewallpolicyrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.compute.v1beta.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ioperation), [protos.google.cloud.compute.v1beta.IRemoveRuleRegionNetworkFirewallPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.iremoveruleregionnetworkfirewallpolicyrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### removeRule(request, callback)
    
    
    removeRule(request: protos.google.cloud.compute.v1beta.IRemoveRuleRegionNetworkFirewallPolicyRequest, callback: Callback<protos.google.cloud.compute.v1beta.IOperation, protos.google.cloud.compute.v1beta.IRemoveRuleRegionNetworkFirewallPolicyRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IRemoveRuleRegionNetworkFirewallPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.iremoveruleregionnetworkfirewallpolicyrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.compute.v1beta.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ioperation), [protos.google.cloud.compute.v1beta.IRemoveRuleRegionNetworkFirewallPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.iremoveruleregionnetworkfirewallpolicyrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### setIamPolicy(request, options)
    
    
    setIamPolicy(request?: protos.google.cloud.compute.v1beta.ISetIamPolicyRegionNetworkFirewallPolicyRequest, options?: CallOptions): Promise<[
            protos.google.cloud.compute.v1beta.IPolicy,
            (protos.google.cloud.compute.v1beta.ISetIamPolicyRegionNetworkFirewallPolicyRequest | undefined),
            {} | undefined
        ]>;

Sets the access control policy on the specified resource. Replaces any existing policy.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISetIamPolicyRegionNetworkFirewallPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.isetiampolicyregionnetworkfirewallpolicyrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.compute.v1beta.IPolicy](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ipolicy), ([protos.google.cloud.compute.v1beta.ISetIamPolicyRegionNetworkFirewallPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.isetiampolicyregionnetworkfirewallpolicyrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [Policy](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.policy). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Project ID for this request.
       */
      // const project = 'my-project'
      /**
       *  The name of the region for this request.
       */
      // const region = 'us-central1'
      /**
       *  The body resource for this request
       */
      // const regionSetPolicyRequestResource = {}
      /**
       *  Name or id of the resource for this request.
       */
      // const resource = 'abc123'
    
      // Imports the Compute library
      const {RegionNetworkFirewallPoliciesClient} = require('[@google-cloud/compute](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const computeClient = new [RegionNetworkFirewallPoliciesClient](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)();
    
      async function callSetIamPolicy() {
        // Construct request
        const request = {
          project,
          region,
          regionSetPolicyRequestResource,
          resource,
        };
    
        // Run request
        const response = await computeClient.setIamPolicy(request);
        console.log(response);
      }
    
      callSetIamPolicy();
    
    

### setIamPolicy(request, options, callback)
    
    
    setIamPolicy(request: protos.google.cloud.compute.v1beta.ISetIamPolicyRegionNetworkFirewallPolicyRequest, options: CallOptions, callback: Callback<protos.google.cloud.compute.v1beta.IPolicy, protos.google.cloud.compute.v1beta.ISetIamPolicyRegionNetworkFirewallPolicyRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISetIamPolicyRegionNetworkFirewallPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.isetiampolicyregionnetworkfirewallpolicyrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.compute.v1beta.IPolicy](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ipolicy), [protos.google.cloud.compute.v1beta.ISetIamPolicyRegionNetworkFirewallPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.isetiampolicyregionnetworkfirewallpolicyrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### setIamPolicy(request, callback)
    
    
    setIamPolicy(request: protos.google.cloud.compute.v1beta.ISetIamPolicyRegionNetworkFirewallPolicyRequest, callback: Callback<protos.google.cloud.compute.v1beta.IPolicy, protos.google.cloud.compute.v1beta.ISetIamPolicyRegionNetworkFirewallPolicyRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISetIamPolicyRegionNetworkFirewallPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.isetiampolicyregionnetworkfirewallpolicyrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.compute.v1beta.IPolicy](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ipolicy), [protos.google.cloud.compute.v1beta.ISetIamPolicyRegionNetworkFirewallPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.isetiampolicyregionnetworkfirewallpolicyrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### testIamPermissions(request, options)
    
    
    testIamPermissions(request?: protos.google.cloud.compute.v1beta.ITestIamPermissionsRegionNetworkFirewallPolicyRequest, options?: CallOptions): Promise<[
            protos.google.cloud.compute.v1beta.ITestPermissionsResponse,
            (protos.google.cloud.compute.v1beta.ITestIamPermissionsRegionNetworkFirewallPolicyRequest | undefined),
            {} | undefined
        ]>;

Returns permissions that a caller has on the specified resource.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ITestIamPermissionsRegionNetworkFirewallPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.itestiampermissionsregionnetworkfirewallpolicyrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.compute.v1beta.ITestPermissionsResponse](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.itestpermissionsresponse), ([protos.google.cloud.compute.v1beta.ITestIamPermissionsRegionNetworkFirewallPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.itestiampermissionsregionnetworkfirewallpolicyrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [TestPermissionsResponse](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.testpermissionsresponse). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Project ID for this request.
       */
      // const project = 'my-project'
      /**
       *  The name of the region for this request.
       */
      // const region = 'us-central1'
      /**
       *  Name or id of the resource for this request.
       */
      // const resource = 'abc123'
      /**
       *  The body resource for this request
       */
      // const testPermissionsRequestResource = {}
    
      // Imports the Compute library
      const {RegionNetworkFirewallPoliciesClient} = require('[@google-cloud/compute](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const computeClient = new [RegionNetworkFirewallPoliciesClient](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)();
    
      async function callTestIamPermissions() {
        // Construct request
        const request = {
          project,
          region,
          resource,
          testPermissionsRequestResource,
        };
    
        // Run request
        const response = await computeClient.testIamPermissions(request);
        console.log(response);
      }
    
      callTestIamPermissions();
    
    

### testIamPermissions(request, options, callback)
    
    
    testIamPermissions(request: protos.google.cloud.compute.v1beta.ITestIamPermissionsRegionNetworkFirewallPolicyRequest, options: CallOptions, callback: Callback<protos.google.cloud.compute.v1beta.ITestPermissionsResponse, protos.google.cloud.compute.v1beta.ITestIamPermissionsRegionNetworkFirewallPolicyRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ITestIamPermissionsRegionNetworkFirewallPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.itestiampermissionsregionnetworkfirewallpolicyrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.compute.v1beta.ITestPermissionsResponse](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.itestpermissionsresponse), [protos.google.cloud.compute.v1beta.ITestIamPermissionsRegionNetworkFirewallPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.itestiampermissionsregionnetworkfirewallpolicyrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### testIamPermissions(request, callback)
    
    
    testIamPermissions(request: protos.google.cloud.compute.v1beta.ITestIamPermissionsRegionNetworkFirewallPolicyRequest, callback: Callback<protos.google.cloud.compute.v1beta.ITestPermissionsResponse, protos.google.cloud.compute.v1beta.ITestIamPermissionsRegionNetworkFirewallPolicyRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ITestIamPermissionsRegionNetworkFirewallPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.itestiampermissionsregionnetworkfirewallpolicyrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.compute.v1beta.ITestPermissionsResponse](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.itestpermissionsresponse), [protos.google.cloud.compute.v1beta.ITestIamPermissionsRegionNetworkFirewallPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.itestiampermissionsregionnetworkfirewallpolicyrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
