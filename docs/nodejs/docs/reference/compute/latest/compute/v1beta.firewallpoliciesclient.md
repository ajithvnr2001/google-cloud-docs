---
url: https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/v1beta.firewallpoliciesclient
title: Class v1beta.FirewallPoliciesClient (7.6.0) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:12:32.651268+00:00
---

# Class v1beta.FirewallPoliciesClient (7.6.0)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/v1beta.firewallpoliciesclient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class v1beta.FirewallPoliciesClient (7.6.0) Stay organized with collections  Save and categorize content based on your preferences. 

7.6.0 (latest)  7.5.1  7.2.0  6.14.0  6.13.0  6.12.0  6.11.0  6.9.0  6.7.0  6.5.0  4.11.0  4.10.0  4.9.0  4.8.0  4.6.0  4.5.0  4.3.0  4.1.0  3.9.1  3.8.1  3.6.0  3.5.1  3.1.2  3.0.0 

The FirewallPolicies API. v1beta

## Package

[@google-cloud/compute](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)

## Constructors 

### (constructor)(opts, gaxInstance)
    
    
    constructor(opts?: ClientOptions, gaxInstance?: typeof gax | typeof gax.fallback);

Construct an instance of FirewallPoliciesClient.

**Parameters**  
---  
**Name** | **Description**  
`opts` |  `ClientOptions`   
  
`gaxInstance` |  `typeof gax | typeof fallback`   
: loaded instance of `google-gax`. Useful if you need to avoid loading the default gRPC version and want to use the fallback HTTP implementation. Load only fallback version and pass it to the constructor: ``` const gax = require('google-gax/build/src/fallback'); // avoids loading google-gax with gRPC const client = new FirewallPoliciesClient({fallback: true}, gax); ```  
  
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

### firewallPoliciesStub
    
    
    firewallPoliciesStub?: Promise<{
            [name: string]: Function;
        }>;

### innerApiCalls
    
    
    innerApiCalls: {
            [name: string]: Function;
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

### addAssociation(request, options)
    
    
    addAssociation(request?: protos.google.cloud.compute.v1beta.IAddAssociationFirewallPolicyRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.cloud.compute.v1beta.IOperation, null>,
            protos.google.cloud.compute.v1beta.IOperation | undefined,
            {} | undefined
        ]>;

Inserts an association for the specified firewall policy.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IAddAssociationFirewallPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.iaddassociationfirewallpolicyrequest)`   
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
       *  Indicates whether or not to replace it if an association of the attachment
       *  already exists. This is false by default, in which case an error will be
       *  returned if an association already exists.
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
      const {FirewallPoliciesClient} = require('[@google-cloud/compute](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const computeClient = new [FirewallPoliciesClient](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)();
    
      async function callAddAssociation() {
        // Construct request
        const request = {
          firewallPolicy,
          firewallPolicyAssociationResource,
        };
    
        // Run request
        const response = await computeClient.addAssociation(request);
        console.log(response);
      }
    
      callAddAssociation();
    
    

### addAssociation(request, options, callback)
    
    
    addAssociation(request: protos.google.cloud.compute.v1beta.IAddAssociationFirewallPolicyRequest, options: CallOptions, callback: Callback<protos.google.cloud.compute.v1beta.IOperation, protos.google.cloud.compute.v1beta.IAddAssociationFirewallPolicyRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IAddAssociationFirewallPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.iaddassociationfirewallpolicyrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.compute.v1beta.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ioperation), [protos.google.cloud.compute.v1beta.IAddAssociationFirewallPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.iaddassociationfirewallpolicyrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### addAssociation(request, callback)
    
    
    addAssociation(request: protos.google.cloud.compute.v1beta.IAddAssociationFirewallPolicyRequest, callback: Callback<protos.google.cloud.compute.v1beta.IOperation, protos.google.cloud.compute.v1beta.IAddAssociationFirewallPolicyRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IAddAssociationFirewallPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.iaddassociationfirewallpolicyrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.compute.v1beta.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ioperation), [protos.google.cloud.compute.v1beta.IAddAssociationFirewallPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.iaddassociationfirewallpolicyrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### addPacketMirroringRule(request, options)
    
    
    addPacketMirroringRule(request?: protos.google.cloud.compute.v1beta.IAddPacketMirroringRuleFirewallPolicyRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.cloud.compute.v1beta.IOperation, null>,
            protos.google.cloud.compute.v1beta.IOperation | undefined,
            {} | undefined
        ]>;

Inserts a packet mirroring rule into a firewall policy.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IAddPacketMirroringRuleFirewallPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.iaddpacketmirroringrulefirewallpolicyrequest)`   
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
      const {FirewallPoliciesClient} = require('[@google-cloud/compute](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const computeClient = new [FirewallPoliciesClient](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)();
    
      async function callAddPacketMirroringRule() {
        // Construct request
        const request = {
          firewallPolicy,
          firewallPolicyRuleResource,
        };
    
        // Run request
        const response = await computeClient.addPacketMirroringRule(request);
        console.log(response);
      }
    
      callAddPacketMirroringRule();
    
    

### addPacketMirroringRule(request, options, callback)
    
    
    addPacketMirroringRule(request: protos.google.cloud.compute.v1beta.IAddPacketMirroringRuleFirewallPolicyRequest, options: CallOptions, callback: Callback<protos.google.cloud.compute.v1beta.IOperation, protos.google.cloud.compute.v1beta.IAddPacketMirroringRuleFirewallPolicyRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IAddPacketMirroringRuleFirewallPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.iaddpacketmirroringrulefirewallpolicyrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.compute.v1beta.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ioperation), [protos.google.cloud.compute.v1beta.IAddPacketMirroringRuleFirewallPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.iaddpacketmirroringrulefirewallpolicyrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### addPacketMirroringRule(request, callback)
    
    
    addPacketMirroringRule(request: protos.google.cloud.compute.v1beta.IAddPacketMirroringRuleFirewallPolicyRequest, callback: Callback<protos.google.cloud.compute.v1beta.IOperation, protos.google.cloud.compute.v1beta.IAddPacketMirroringRuleFirewallPolicyRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IAddPacketMirroringRuleFirewallPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.iaddpacketmirroringrulefirewallpolicyrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.compute.v1beta.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ioperation), [protos.google.cloud.compute.v1beta.IAddPacketMirroringRuleFirewallPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.iaddpacketmirroringrulefirewallpolicyrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### addRule(request, options)
    
    
    addRule(request?: protos.google.cloud.compute.v1beta.IAddRuleFirewallPolicyRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.cloud.compute.v1beta.IOperation, null>,
            protos.google.cloud.compute.v1beta.IOperation | undefined,
            {} | undefined
        ]>;

Inserts a rule into a firewall policy.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IAddRuleFirewallPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.iaddrulefirewallpolicyrequest)`   
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
      const {FirewallPoliciesClient} = require('[@google-cloud/compute](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const computeClient = new [FirewallPoliciesClient](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)();
    
      async function callAddRule() {
        // Construct request
        const request = {
          firewallPolicy,
          firewallPolicyRuleResource,
        };
    
        // Run request
        const response = await computeClient.addRule(request);
        console.log(response);
      }
    
      callAddRule();
    
    

### addRule(request, options, callback)
    
    
    addRule(request: protos.google.cloud.compute.v1beta.IAddRuleFirewallPolicyRequest, options: CallOptions, callback: Callback<protos.google.cloud.compute.v1beta.IOperation, protos.google.cloud.compute.v1beta.IAddRuleFirewallPolicyRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IAddRuleFirewallPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.iaddrulefirewallpolicyrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.compute.v1beta.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ioperation), [protos.google.cloud.compute.v1beta.IAddRuleFirewallPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.iaddrulefirewallpolicyrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### addRule(request, callback)
    
    
    addRule(request: protos.google.cloud.compute.v1beta.IAddRuleFirewallPolicyRequest, callback: Callback<protos.google.cloud.compute.v1beta.IOperation, protos.google.cloud.compute.v1beta.IAddRuleFirewallPolicyRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IAddRuleFirewallPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.iaddrulefirewallpolicyrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.compute.v1beta.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ioperation), [protos.google.cloud.compute.v1beta.IAddRuleFirewallPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.iaddrulefirewallpolicyrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### cloneRules(request, options)
    
    
    cloneRules(request?: protos.google.cloud.compute.v1beta.ICloneRulesFirewallPolicyRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.cloud.compute.v1beta.IOperation, null>,
            protos.google.cloud.compute.v1beta.IOperation | undefined,
            {} | undefined
        ]>;

Copies rules to the specified firewall policy.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICloneRulesFirewallPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.iclonerulesfirewallpolicyrequest)`   
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
      const {FirewallPoliciesClient} = require('[@google-cloud/compute](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const computeClient = new [FirewallPoliciesClient](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)();
    
      async function callCloneRules() {
        // Construct request
        const request = {
          firewallPolicy,
        };
    
        // Run request
        const response = await computeClient.cloneRules(request);
        console.log(response);
      }
    
      callCloneRules();
    
    

### cloneRules(request, options, callback)
    
    
    cloneRules(request: protos.google.cloud.compute.v1beta.ICloneRulesFirewallPolicyRequest, options: CallOptions, callback: Callback<protos.google.cloud.compute.v1beta.IOperation, protos.google.cloud.compute.v1beta.ICloneRulesFirewallPolicyRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICloneRulesFirewallPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.iclonerulesfirewallpolicyrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.compute.v1beta.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ioperation), [protos.google.cloud.compute.v1beta.ICloneRulesFirewallPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.iclonerulesfirewallpolicyrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### cloneRules(request, callback)
    
    
    cloneRules(request: protos.google.cloud.compute.v1beta.ICloneRulesFirewallPolicyRequest, callback: Callback<protos.google.cloud.compute.v1beta.IOperation, protos.google.cloud.compute.v1beta.ICloneRulesFirewallPolicyRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICloneRulesFirewallPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.iclonerulesfirewallpolicyrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.compute.v1beta.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ioperation), [protos.google.cloud.compute.v1beta.ICloneRulesFirewallPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.iclonerulesfirewallpolicyrequest) | null | undefined, {} | null | undefined>`   
  
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
    
    
    delete(request?: protos.google.cloud.compute.v1beta.IDeleteFirewallPolicyRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.cloud.compute.v1beta.IOperation, null>,
            protos.google.cloud.compute.v1beta.IOperation | undefined,
            {} | undefined
        ]>;

Deletes the specified policy.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteFirewallPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ideletefirewallpolicyrequest)`   
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
      const {FirewallPoliciesClient} = require('[@google-cloud/compute](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const computeClient = new [FirewallPoliciesClient](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)();
    
      async function callDelete() {
        // Construct request
        const request = {
          firewallPolicy,
        };
    
        // Run request
        const response = await computeClient.delete(request);
        console.log(response);
      }
    
      callDelete();
    
    

### delete(request, options, callback)
    
    
    delete(request: protos.google.cloud.compute.v1beta.IDeleteFirewallPolicyRequest, options: CallOptions, callback: Callback<protos.google.cloud.compute.v1beta.IOperation, protos.google.cloud.compute.v1beta.IDeleteFirewallPolicyRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteFirewallPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ideletefirewallpolicyrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.compute.v1beta.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ioperation), [protos.google.cloud.compute.v1beta.IDeleteFirewallPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ideletefirewallpolicyrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### delete(request, callback)
    
    
    delete(request: protos.google.cloud.compute.v1beta.IDeleteFirewallPolicyRequest, callback: Callback<protos.google.cloud.compute.v1beta.IOperation, protos.google.cloud.compute.v1beta.IDeleteFirewallPolicyRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteFirewallPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ideletefirewallpolicyrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.compute.v1beta.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ioperation), [protos.google.cloud.compute.v1beta.IDeleteFirewallPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ideletefirewallpolicyrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### get(request, options)
    
    
    get(request?: protos.google.cloud.compute.v1beta.IGetFirewallPolicyRequest, options?: CallOptions): Promise<[
            protos.google.cloud.compute.v1beta.IFirewallPolicy,
            protos.google.cloud.compute.v1beta.IGetFirewallPolicyRequest | undefined,
            {} | undefined
        ]>;

Returns the specified firewall policy.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetFirewallPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.igetfirewallpolicyrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.compute.v1beta.IFirewallPolicy](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ifirewallpolicy), [protos.google.cloud.compute.v1beta.IGetFirewallPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.igetfirewallpolicyrequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
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
    
      // Imports the Compute library
      const {FirewallPoliciesClient} = require('[@google-cloud/compute](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const computeClient = new [FirewallPoliciesClient](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)();
    
      async function callGet() {
        // Construct request
        const request = {
          firewallPolicy,
        };
    
        // Run request
        const response = await computeClient.get(request);
        console.log(response);
      }
    
      callGet();
    
    

### get(request, options, callback)
    
    
    get(request: protos.google.cloud.compute.v1beta.IGetFirewallPolicyRequest, options: CallOptions, callback: Callback<protos.google.cloud.compute.v1beta.IFirewallPolicy, protos.google.cloud.compute.v1beta.IGetFirewallPolicyRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetFirewallPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.igetfirewallpolicyrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.compute.v1beta.IFirewallPolicy](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ifirewallpolicy), [protos.google.cloud.compute.v1beta.IGetFirewallPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.igetfirewallpolicyrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### get(request, callback)
    
    
    get(request: protos.google.cloud.compute.v1beta.IGetFirewallPolicyRequest, callback: Callback<protos.google.cloud.compute.v1beta.IFirewallPolicy, protos.google.cloud.compute.v1beta.IGetFirewallPolicyRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetFirewallPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.igetfirewallpolicyrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.compute.v1beta.IFirewallPolicy](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ifirewallpolicy), [protos.google.cloud.compute.v1beta.IGetFirewallPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.igetfirewallpolicyrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getAssociation(request, options)
    
    
    getAssociation(request?: protos.google.cloud.compute.v1beta.IGetAssociationFirewallPolicyRequest, options?: CallOptions): Promise<[
            protos.google.cloud.compute.v1beta.IFirewallPolicyAssociation,
            (protos.google.cloud.compute.v1beta.IGetAssociationFirewallPolicyRequest | undefined),
            {} | undefined
        ]>;

Gets an association with the specified name.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetAssociationFirewallPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.igetassociationfirewallpolicyrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.compute.v1beta.IFirewallPolicyAssociation](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ifirewallpolicyassociation), ([protos.google.cloud.compute.v1beta.IGetAssociationFirewallPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.igetassociationfirewallpolicyrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [FirewallPolicyAssociation](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.firewallpolicyassociation). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
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
       *  The name of the association to get from the firewall policy.
       */
      // const name = 'abc123'
    
      // Imports the Compute library
      const {FirewallPoliciesClient} = require('[@google-cloud/compute](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const computeClient = new [FirewallPoliciesClient](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)();
    
      async function callGetAssociation() {
        // Construct request
        const request = {
          firewallPolicy,
        };
    
        // Run request
        const response = await computeClient.getAssociation(request);
        console.log(response);
      }
    
      callGetAssociation();
    
    

### getAssociation(request, options, callback)
    
    
    getAssociation(request: protos.google.cloud.compute.v1beta.IGetAssociationFirewallPolicyRequest, options: CallOptions, callback: Callback<protos.google.cloud.compute.v1beta.IFirewallPolicyAssociation, protos.google.cloud.compute.v1beta.IGetAssociationFirewallPolicyRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetAssociationFirewallPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.igetassociationfirewallpolicyrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.compute.v1beta.IFirewallPolicyAssociation](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ifirewallpolicyassociation), [protos.google.cloud.compute.v1beta.IGetAssociationFirewallPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.igetassociationfirewallpolicyrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getAssociation(request, callback)
    
    
    getAssociation(request: protos.google.cloud.compute.v1beta.IGetAssociationFirewallPolicyRequest, callback: Callback<protos.google.cloud.compute.v1beta.IFirewallPolicyAssociation, protos.google.cloud.compute.v1beta.IGetAssociationFirewallPolicyRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetAssociationFirewallPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.igetassociationfirewallpolicyrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.compute.v1beta.IFirewallPolicyAssociation](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ifirewallpolicyassociation), [protos.google.cloud.compute.v1beta.IGetAssociationFirewallPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.igetassociationfirewallpolicyrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getIamPolicy(request, options)
    
    
    getIamPolicy(request?: protos.google.cloud.compute.v1beta.IGetIamPolicyFirewallPolicyRequest, options?: CallOptions): Promise<[
            protos.google.cloud.compute.v1beta.IPolicy,
            (protos.google.cloud.compute.v1beta.IGetIamPolicyFirewallPolicyRequest | undefined),
            {} | undefined
        ]>;

Gets the access control policy for a resource. May be empty if no such policy or resource exists.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetIamPolicyFirewallPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.igetiampolicyfirewallpolicyrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.compute.v1beta.IPolicy](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ipolicy), ([protos.google.cloud.compute.v1beta.IGetIamPolicyFirewallPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.igetiampolicyfirewallpolicyrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [Policy](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.policy). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
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
       *  Name or id of the resource for this request.
       */
      // const resource = 'abc123'
    
      // Imports the Compute library
      const {FirewallPoliciesClient} = require('[@google-cloud/compute](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const computeClient = new [FirewallPoliciesClient](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)();
    
      async function callGetIamPolicy() {
        // Construct request
        const request = {
          resource,
        };
    
        // Run request
        const response = await computeClient.getIamPolicy(request);
        console.log(response);
      }
    
      callGetIamPolicy();
    
    

### getIamPolicy(request, options, callback)
    
    
    getIamPolicy(request: protos.google.cloud.compute.v1beta.IGetIamPolicyFirewallPolicyRequest, options: CallOptions, callback: Callback<protos.google.cloud.compute.v1beta.IPolicy, protos.google.cloud.compute.v1beta.IGetIamPolicyFirewallPolicyRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetIamPolicyFirewallPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.igetiampolicyfirewallpolicyrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.compute.v1beta.IPolicy](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ipolicy), [protos.google.cloud.compute.v1beta.IGetIamPolicyFirewallPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.igetiampolicyfirewallpolicyrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getIamPolicy(request, callback)
    
    
    getIamPolicy(request: protos.google.cloud.compute.v1beta.IGetIamPolicyFirewallPolicyRequest, callback: Callback<protos.google.cloud.compute.v1beta.IPolicy, protos.google.cloud.compute.v1beta.IGetIamPolicyFirewallPolicyRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetIamPolicyFirewallPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.igetiampolicyfirewallpolicyrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.compute.v1beta.IPolicy](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ipolicy), [protos.google.cloud.compute.v1beta.IGetIamPolicyFirewallPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.igetiampolicyfirewallpolicyrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getPacketMirroringRule(request, options)
    
    
    getPacketMirroringRule(request?: protos.google.cloud.compute.v1beta.IGetPacketMirroringRuleFirewallPolicyRequest, options?: CallOptions): Promise<[
            protos.google.cloud.compute.v1beta.IFirewallPolicyRule,
            (protos.google.cloud.compute.v1beta.IGetPacketMirroringRuleFirewallPolicyRequest | undefined),
            {} | undefined
        ]>;

Gets a packet mirroring rule of the specified priority.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetPacketMirroringRuleFirewallPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.igetpacketmirroringrulefirewallpolicyrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.compute.v1beta.IFirewallPolicyRule](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ifirewallpolicyrule), ([protos.google.cloud.compute.v1beta.IGetPacketMirroringRuleFirewallPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.igetpacketmirroringrulefirewallpolicyrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
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
    
      // Imports the Compute library
      const {FirewallPoliciesClient} = require('[@google-cloud/compute](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const computeClient = new [FirewallPoliciesClient](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)();
    
      async function callGetPacketMirroringRule() {
        // Construct request
        const request = {
          firewallPolicy,
        };
    
        // Run request
        const response = await computeClient.getPacketMirroringRule(request);
        console.log(response);
      }
    
      callGetPacketMirroringRule();
    
    

### getPacketMirroringRule(request, options, callback)
    
    
    getPacketMirroringRule(request: protos.google.cloud.compute.v1beta.IGetPacketMirroringRuleFirewallPolicyRequest, options: CallOptions, callback: Callback<protos.google.cloud.compute.v1beta.IFirewallPolicyRule, protos.google.cloud.compute.v1beta.IGetPacketMirroringRuleFirewallPolicyRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetPacketMirroringRuleFirewallPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.igetpacketmirroringrulefirewallpolicyrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.compute.v1beta.IFirewallPolicyRule](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ifirewallpolicyrule), [protos.google.cloud.compute.v1beta.IGetPacketMirroringRuleFirewallPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.igetpacketmirroringrulefirewallpolicyrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getPacketMirroringRule(request, callback)
    
    
    getPacketMirroringRule(request: protos.google.cloud.compute.v1beta.IGetPacketMirroringRuleFirewallPolicyRequest, callback: Callback<protos.google.cloud.compute.v1beta.IFirewallPolicyRule, protos.google.cloud.compute.v1beta.IGetPacketMirroringRuleFirewallPolicyRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetPacketMirroringRuleFirewallPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.igetpacketmirroringrulefirewallpolicyrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.compute.v1beta.IFirewallPolicyRule](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ifirewallpolicyrule), [protos.google.cloud.compute.v1beta.IGetPacketMirroringRuleFirewallPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.igetpacketmirroringrulefirewallpolicyrequest) | null | undefined, {} | null | undefined>`   
  
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
    
    
    getRule(request?: protos.google.cloud.compute.v1beta.IGetRuleFirewallPolicyRequest, options?: CallOptions): Promise<[
            protos.google.cloud.compute.v1beta.IFirewallPolicyRule,
            (protos.google.cloud.compute.v1beta.IGetRuleFirewallPolicyRequest | undefined),
            {} | undefined
        ]>;

Gets a rule of the specified priority.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetRuleFirewallPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.igetrulefirewallpolicyrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.compute.v1beta.IFirewallPolicyRule](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ifirewallpolicyrule), ([protos.google.cloud.compute.v1beta.IGetRuleFirewallPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.igetrulefirewallpolicyrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
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
    
      // Imports the Compute library
      const {FirewallPoliciesClient} = require('[@google-cloud/compute](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const computeClient = new [FirewallPoliciesClient](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)();
    
      async function callGetRule() {
        // Construct request
        const request = {
          firewallPolicy,
        };
    
        // Run request
        const response = await computeClient.getRule(request);
        console.log(response);
      }
    
      callGetRule();
    
    

### getRule(request, options, callback)
    
    
    getRule(request: protos.google.cloud.compute.v1beta.IGetRuleFirewallPolicyRequest, options: CallOptions, callback: Callback<protos.google.cloud.compute.v1beta.IFirewallPolicyRule, protos.google.cloud.compute.v1beta.IGetRuleFirewallPolicyRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetRuleFirewallPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.igetrulefirewallpolicyrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.compute.v1beta.IFirewallPolicyRule](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ifirewallpolicyrule), [protos.google.cloud.compute.v1beta.IGetRuleFirewallPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.igetrulefirewallpolicyrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getRule(request, callback)
    
    
    getRule(request: protos.google.cloud.compute.v1beta.IGetRuleFirewallPolicyRequest, callback: Callback<protos.google.cloud.compute.v1beta.IFirewallPolicyRule, protos.google.cloud.compute.v1beta.IGetRuleFirewallPolicyRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetRuleFirewallPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.igetrulefirewallpolicyrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.compute.v1beta.IFirewallPolicyRule](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ifirewallpolicyrule), [protos.google.cloud.compute.v1beta.IGetRuleFirewallPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.igetrulefirewallpolicyrequest) | null | undefined, {} | null | undefined>`   
  
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
    
    
    insert(request?: protos.google.cloud.compute.v1beta.IInsertFirewallPolicyRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.cloud.compute.v1beta.IOperation, null>,
            protos.google.cloud.compute.v1beta.IOperation | undefined,
            {} | undefined
        ]>;

Creates a new policy in the specified project using the data included in the request.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IInsertFirewallPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.iinsertfirewallpolicyrequest)`   
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
       *  Parent ID for this request. The ID can be either be "folders/[FOLDER_ID]"
       *  if the parent is a folder or "organizations/[ORGANIZATION_ID]" if the
       *  parent is an organization.
       */
      // const parentId = 'abc123'
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
      const {FirewallPoliciesClient} = require('[@google-cloud/compute](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const computeClient = new [FirewallPoliciesClient](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)();
    
      async function callInsert() {
        // Construct request
        const request = {
          firewallPolicyResource,
          parentId,
        };
    
        // Run request
        const response = await computeClient.insert(request);
        console.log(response);
      }
    
      callInsert();
    
    

### insert(request, options, callback)
    
    
    insert(request: protos.google.cloud.compute.v1beta.IInsertFirewallPolicyRequest, options: CallOptions, callback: Callback<protos.google.cloud.compute.v1beta.IOperation, protos.google.cloud.compute.v1beta.IInsertFirewallPolicyRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IInsertFirewallPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.iinsertfirewallpolicyrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.compute.v1beta.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ioperation), [protos.google.cloud.compute.v1beta.IInsertFirewallPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.iinsertfirewallpolicyrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### insert(request, callback)
    
    
    insert(request: protos.google.cloud.compute.v1beta.IInsertFirewallPolicyRequest, callback: Callback<protos.google.cloud.compute.v1beta.IOperation, protos.google.cloud.compute.v1beta.IInsertFirewallPolicyRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IInsertFirewallPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.iinsertfirewallpolicyrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.compute.v1beta.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ioperation), [protos.google.cloud.compute.v1beta.IInsertFirewallPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.iinsertfirewallpolicyrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### list(request, options)
    
    
    list(request?: protos.google.cloud.compute.v1beta.IListFirewallPoliciesRequest, options?: CallOptions): Promise<[
            protos.google.cloud.compute.v1beta.IFirewallPolicy[],
            protos.google.cloud.compute.v1beta.IListFirewallPoliciesRequest | null,
            protos.google.cloud.compute.v1beta.IFirewallPolicyList
        ]>;

Lists all the policies that have been configured for the specified folder or organization.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListFirewallPoliciesRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ilistfirewallpoliciesrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.compute.v1beta.IFirewallPolicy](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ifirewallpolicy)[], [protos.google.cloud.compute.v1beta.IListFirewallPoliciesRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ilistfirewallpoliciesrequest) | null, [protos.google.cloud.compute.v1beta.IFirewallPolicyList](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ifirewallpolicylist) ]>` | {Promise} - The promise which resolves to an array. The first element of the array is Array of . The client library will perform auto-pagination by default: it will call the API as many times as needed and will merge results from all the pages into this array. Note that it can affect your quota. We recommend using `listAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### list(request, options, callback)
    
    
    list(request: protos.google.cloud.compute.v1beta.IListFirewallPoliciesRequest, options: CallOptions, callback: PaginationCallback<protos.google.cloud.compute.v1beta.IListFirewallPoliciesRequest, protos.google.cloud.compute.v1beta.IFirewallPolicyList | null | undefined, protos.google.cloud.compute.v1beta.IFirewallPolicy>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListFirewallPoliciesRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ilistfirewallpoliciesrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.compute.v1beta.IListFirewallPoliciesRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ilistfirewallpoliciesrequest), [protos.google.cloud.compute.v1beta.IFirewallPolicyList](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ifirewallpolicylist) | null | undefined, [protos.google.cloud.compute.v1beta.IFirewallPolicy](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ifirewallpolicy)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### list(request, callback)
    
    
    list(request: protos.google.cloud.compute.v1beta.IListFirewallPoliciesRequest, callback: PaginationCallback<protos.google.cloud.compute.v1beta.IListFirewallPoliciesRequest, protos.google.cloud.compute.v1beta.IFirewallPolicyList | null | undefined, protos.google.cloud.compute.v1beta.IFirewallPolicy>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListFirewallPoliciesRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ilistfirewallpoliciesrequest)`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.compute.v1beta.IListFirewallPoliciesRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ilistfirewallpoliciesrequest), [protos.google.cloud.compute.v1beta.IFirewallPolicyList](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ifirewallpolicylist) | null | undefined, [protos.google.cloud.compute.v1beta.IFirewallPolicy](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ifirewallpolicy)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listAssociations(request, options)
    
    
    listAssociations(request?: protos.google.cloud.compute.v1beta.IListAssociationsFirewallPolicyRequest, options?: CallOptions): Promise<[
            protos.google.cloud.compute.v1beta.IFirewallPoliciesListAssociationsResponse,
            (protos.google.cloud.compute.v1beta.IListAssociationsFirewallPolicyRequest | undefined),
            {} | undefined
        ]>;

Lists associations of a specified target, i.e., organization or folder.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListAssociationsFirewallPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ilistassociationsfirewallpolicyrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.compute.v1beta.IFirewallPoliciesListAssociationsResponse](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ifirewallpolicieslistassociationsresponse), ([protos.google.cloud.compute.v1beta.IListAssociationsFirewallPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ilistassociationsfirewallpolicyrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [FirewallPoliciesListAssociationsResponse](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.firewallpolicieslistassociationsresponse). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  If set to "true", the response will contain a list of all associations for
       *  the containing folders and the containing organization of the target. The
       *  parameter has no effect if the target is an organization.
       */
      // const includeInheritedPolicies = true
      /**
       *  The target resource to list associations. It is an organization, or a
       *  folder.
       */
      // const targetResource = 'abc123'
    
      // Imports the Compute library
      const {FirewallPoliciesClient} = require('[@google-cloud/compute](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const computeClient = new [FirewallPoliciesClient](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)();
    
      async function callListAssociations() {
        // Construct request
        const request = {
        };
    
        // Run request
        const response = await computeClient.listAssociations(request);
        console.log(response);
      }
    
      callListAssociations();
    
    

### listAssociations(request, options, callback)
    
    
    listAssociations(request: protos.google.cloud.compute.v1beta.IListAssociationsFirewallPolicyRequest, options: CallOptions, callback: Callback<protos.google.cloud.compute.v1beta.IFirewallPoliciesListAssociationsResponse, protos.google.cloud.compute.v1beta.IListAssociationsFirewallPolicyRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListAssociationsFirewallPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ilistassociationsfirewallpolicyrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.compute.v1beta.IFirewallPoliciesListAssociationsResponse](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ifirewallpolicieslistassociationsresponse), [protos.google.cloud.compute.v1beta.IListAssociationsFirewallPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ilistassociationsfirewallpolicyrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listAssociations(request, callback)
    
    
    listAssociations(request: protos.google.cloud.compute.v1beta.IListAssociationsFirewallPolicyRequest, callback: Callback<protos.google.cloud.compute.v1beta.IFirewallPoliciesListAssociationsResponse, protos.google.cloud.compute.v1beta.IListAssociationsFirewallPolicyRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListAssociationsFirewallPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ilistassociationsfirewallpolicyrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.compute.v1beta.IFirewallPoliciesListAssociationsResponse](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ifirewallpolicieslistassociationsresponse), [protos.google.cloud.compute.v1beta.IListAssociationsFirewallPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ilistassociationsfirewallpolicyrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listAsync(request, options)
    
    
    listAsync(request?: protos.google.cloud.compute.v1beta.IListFirewallPoliciesRequest, options?: CallOptions): AsyncIterable<protos.google.cloud.compute.v1beta.IFirewallPolicy>;

Equivalent to `list`, but returns an iterable object.

`for`-`await`-`of` syntax is used with the iterable to get response elements on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListFirewallPoliciesRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ilistfirewallpoliciesrequest)`   
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
  * Parent ID for this request. The ID can be either be "folders/[FOLDER_ID]"
  * if the parent is a folder or "organizations/[ORGANIZATION_ID]" if the
  * parent is an organization. _/ // const parentId = 'abc123' /_ *
  * Opt-in for partial success behavior which provides partial results in case
  * of failure. The default value is false.
  * For example, when partial success behavior is enabled, aggregatedList for a
  * single zone scope either returns all resources in the zone or no resources,
  * with an error code. */ // const returnPartialSuccess = true

// Imports the Compute library const {FirewallPoliciesClient} = require('@google-cloud/compute').v1beta;

// Instantiates a client const computeClient = new FirewallPoliciesClient();

async function callList() { // Construct request const request = { };

// Run request const iterable = computeClient.listAsync(request); for await (const response of iterable) { console.log(response); } }

callList();




` `

### listStream(request, options)
    
    
    listStream(request?: protos.google.cloud.compute.v1beta.IListFirewallPoliciesRequest, options?: CallOptions): Transform;

Equivalent to `list`, but returns a NodeJS Stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListFirewallPoliciesRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ilistfirewallpoliciesrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Transform` | {Stream} An object stream which emits an object representing on 'data' event. The client library will perform auto-pagination by default: it will call the API as many times as needed. Note that it can affect your quota. We recommend using `listAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### move(request, options)
    
    
    move(request?: protos.google.cloud.compute.v1beta.IMoveFirewallPolicyRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.cloud.compute.v1beta.IOperation, null>,
            protos.google.cloud.compute.v1beta.IOperation | undefined,
            {} | undefined
        ]>;

Moves the specified firewall policy.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IMoveFirewallPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.imovefirewallpolicyrequest)`   
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
       *  The new parent of the firewall policy. The ID can be either be
       *  "folders/[FOLDER_ID]" if the parent is a folder or
       *  "organizations/[ORGANIZATION_ID]" if the parent is an organization.
       */
      // const parentId = 'abc123'
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
      const {FirewallPoliciesClient} = require('[@google-cloud/compute](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const computeClient = new [FirewallPoliciesClient](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)();
    
      async function callMove() {
        // Construct request
        const request = {
          firewallPolicy,
          parentId,
        };
    
        // Run request
        const response = await computeClient.move(request);
        console.log(response);
      }
    
      callMove();
    
    

### move(request, options, callback)
    
    
    move(request: protos.google.cloud.compute.v1beta.IMoveFirewallPolicyRequest, options: CallOptions, callback: Callback<protos.google.cloud.compute.v1beta.IOperation, protos.google.cloud.compute.v1beta.IMoveFirewallPolicyRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IMoveFirewallPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.imovefirewallpolicyrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.compute.v1beta.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ioperation), [protos.google.cloud.compute.v1beta.IMoveFirewallPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.imovefirewallpolicyrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### move(request, callback)
    
    
    move(request: protos.google.cloud.compute.v1beta.IMoveFirewallPolicyRequest, callback: Callback<protos.google.cloud.compute.v1beta.IOperation, protos.google.cloud.compute.v1beta.IMoveFirewallPolicyRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IMoveFirewallPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.imovefirewallpolicyrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.compute.v1beta.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ioperation), [protos.google.cloud.compute.v1beta.IMoveFirewallPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.imovefirewallpolicyrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### patch(request, options)
    
    
    patch(request?: protos.google.cloud.compute.v1beta.IPatchFirewallPolicyRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.cloud.compute.v1beta.IOperation, null>,
            protos.google.cloud.compute.v1beta.IOperation | undefined,
            {} | undefined
        ]>;

Patches the specified policy with the data included in the request.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IPatchFirewallPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ipatchfirewallpolicyrequest)`   
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
      const {FirewallPoliciesClient} = require('[@google-cloud/compute](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const computeClient = new [FirewallPoliciesClient](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)();
    
      async function callPatch() {
        // Construct request
        const request = {
          firewallPolicy,
          firewallPolicyResource,
        };
    
        // Run request
        const response = await computeClient.patch(request);
        console.log(response);
      }
    
      callPatch();
    
    

### patch(request, options, callback)
    
    
    patch(request: protos.google.cloud.compute.v1beta.IPatchFirewallPolicyRequest, options: CallOptions, callback: Callback<protos.google.cloud.compute.v1beta.IOperation, protos.google.cloud.compute.v1beta.IPatchFirewallPolicyRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IPatchFirewallPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ipatchfirewallpolicyrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.compute.v1beta.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ioperation), [protos.google.cloud.compute.v1beta.IPatchFirewallPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ipatchfirewallpolicyrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### patch(request, callback)
    
    
    patch(request: protos.google.cloud.compute.v1beta.IPatchFirewallPolicyRequest, callback: Callback<protos.google.cloud.compute.v1beta.IOperation, protos.google.cloud.compute.v1beta.IPatchFirewallPolicyRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IPatchFirewallPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ipatchfirewallpolicyrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.compute.v1beta.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ioperation), [protos.google.cloud.compute.v1beta.IPatchFirewallPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ipatchfirewallpolicyrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### patchPacketMirroringRule(request, options)
    
    
    patchPacketMirroringRule(request?: protos.google.cloud.compute.v1beta.IPatchPacketMirroringRuleFirewallPolicyRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.cloud.compute.v1beta.IOperation, null>,
            protos.google.cloud.compute.v1beta.IOperation | undefined,
            {} | undefined
        ]>;

Patches a packet mirroring rule of the specified priority.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IPatchPacketMirroringRuleFirewallPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ipatchpacketmirroringrulefirewallpolicyrequest)`   
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
      const {FirewallPoliciesClient} = require('[@google-cloud/compute](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const computeClient = new [FirewallPoliciesClient](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)();
    
      async function callPatchPacketMirroringRule() {
        // Construct request
        const request = {
          firewallPolicy,
          firewallPolicyRuleResource,
        };
    
        // Run request
        const response = await computeClient.patchPacketMirroringRule(request);
        console.log(response);
      }
    
      callPatchPacketMirroringRule();
    
    

### patchPacketMirroringRule(request, options, callback)
    
    
    patchPacketMirroringRule(request: protos.google.cloud.compute.v1beta.IPatchPacketMirroringRuleFirewallPolicyRequest, options: CallOptions, callback: Callback<protos.google.cloud.compute.v1beta.IOperation, protos.google.cloud.compute.v1beta.IPatchPacketMirroringRuleFirewallPolicyRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IPatchPacketMirroringRuleFirewallPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ipatchpacketmirroringrulefirewallpolicyrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.compute.v1beta.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ioperation), [protos.google.cloud.compute.v1beta.IPatchPacketMirroringRuleFirewallPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ipatchpacketmirroringrulefirewallpolicyrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### patchPacketMirroringRule(request, callback)
    
    
    patchPacketMirroringRule(request: protos.google.cloud.compute.v1beta.IPatchPacketMirroringRuleFirewallPolicyRequest, callback: Callback<protos.google.cloud.compute.v1beta.IOperation, protos.google.cloud.compute.v1beta.IPatchPacketMirroringRuleFirewallPolicyRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IPatchPacketMirroringRuleFirewallPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ipatchpacketmirroringrulefirewallpolicyrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.compute.v1beta.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ioperation), [protos.google.cloud.compute.v1beta.IPatchPacketMirroringRuleFirewallPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ipatchpacketmirroringrulefirewallpolicyrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### patchRule(request, options)
    
    
    patchRule(request?: protos.google.cloud.compute.v1beta.IPatchRuleFirewallPolicyRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.cloud.compute.v1beta.IOperation, null>,
            protos.google.cloud.compute.v1beta.IOperation | undefined,
            {} | undefined
        ]>;

Patches a rule of the specified priority.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IPatchRuleFirewallPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ipatchrulefirewallpolicyrequest)`   
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
      const {FirewallPoliciesClient} = require('[@google-cloud/compute](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const computeClient = new [FirewallPoliciesClient](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)();
    
      async function callPatchRule() {
        // Construct request
        const request = {
          firewallPolicy,
          firewallPolicyRuleResource,
        };
    
        // Run request
        const response = await computeClient.patchRule(request);
        console.log(response);
      }
    
      callPatchRule();
    
    

### patchRule(request, options, callback)
    
    
    patchRule(request: protos.google.cloud.compute.v1beta.IPatchRuleFirewallPolicyRequest, options: CallOptions, callback: Callback<protos.google.cloud.compute.v1beta.IOperation, protos.google.cloud.compute.v1beta.IPatchRuleFirewallPolicyRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IPatchRuleFirewallPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ipatchrulefirewallpolicyrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.compute.v1beta.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ioperation), [protos.google.cloud.compute.v1beta.IPatchRuleFirewallPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ipatchrulefirewallpolicyrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### patchRule(request, callback)
    
    
    patchRule(request: protos.google.cloud.compute.v1beta.IPatchRuleFirewallPolicyRequest, callback: Callback<protos.google.cloud.compute.v1beta.IOperation, protos.google.cloud.compute.v1beta.IPatchRuleFirewallPolicyRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IPatchRuleFirewallPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ipatchrulefirewallpolicyrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.compute.v1beta.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ioperation), [protos.google.cloud.compute.v1beta.IPatchRuleFirewallPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ipatchrulefirewallpolicyrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### removeAssociation(request, options)
    
    
    removeAssociation(request?: protos.google.cloud.compute.v1beta.IRemoveAssociationFirewallPolicyRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.cloud.compute.v1beta.IOperation, null>,
            protos.google.cloud.compute.v1beta.IOperation | undefined,
            {} | undefined
        ]>;

Removes an association for the specified firewall policy.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IRemoveAssociationFirewallPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.iremoveassociationfirewallpolicyrequest)`   
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
       *  Name for the attachment that will be removed.
       */
      // const name = 'abc123'
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
      const {FirewallPoliciesClient} = require('[@google-cloud/compute](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const computeClient = new [FirewallPoliciesClient](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)();
    
      async function callRemoveAssociation() {
        // Construct request
        const request = {
          firewallPolicy,
        };
    
        // Run request
        const response = await computeClient.removeAssociation(request);
        console.log(response);
      }
    
      callRemoveAssociation();
    
    

### removeAssociation(request, options, callback)
    
    
    removeAssociation(request: protos.google.cloud.compute.v1beta.IRemoveAssociationFirewallPolicyRequest, options: CallOptions, callback: Callback<protos.google.cloud.compute.v1beta.IOperation, protos.google.cloud.compute.v1beta.IRemoveAssociationFirewallPolicyRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IRemoveAssociationFirewallPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.iremoveassociationfirewallpolicyrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.compute.v1beta.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ioperation), [protos.google.cloud.compute.v1beta.IRemoveAssociationFirewallPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.iremoveassociationfirewallpolicyrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### removeAssociation(request, callback)
    
    
    removeAssociation(request: protos.google.cloud.compute.v1beta.IRemoveAssociationFirewallPolicyRequest, callback: Callback<protos.google.cloud.compute.v1beta.IOperation, protos.google.cloud.compute.v1beta.IRemoveAssociationFirewallPolicyRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IRemoveAssociationFirewallPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.iremoveassociationfirewallpolicyrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.compute.v1beta.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ioperation), [protos.google.cloud.compute.v1beta.IRemoveAssociationFirewallPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.iremoveassociationfirewallpolicyrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### removePacketMirroringRule(request, options)
    
    
    removePacketMirroringRule(request?: protos.google.cloud.compute.v1beta.IRemovePacketMirroringRuleFirewallPolicyRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.cloud.compute.v1beta.IOperation, null>,
            protos.google.cloud.compute.v1beta.IOperation | undefined,
            {} | undefined
        ]>;

Deletes a packet mirroring rule of the specified priority.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IRemovePacketMirroringRuleFirewallPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.iremovepacketmirroringrulefirewallpolicyrequest)`   
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
      const {FirewallPoliciesClient} = require('[@google-cloud/compute](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const computeClient = new [FirewallPoliciesClient](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)();
    
      async function callRemovePacketMirroringRule() {
        // Construct request
        const request = {
          firewallPolicy,
        };
    
        // Run request
        const response = await computeClient.removePacketMirroringRule(request);
        console.log(response);
      }
    
      callRemovePacketMirroringRule();
    
    

### removePacketMirroringRule(request, options, callback)
    
    
    removePacketMirroringRule(request: protos.google.cloud.compute.v1beta.IRemovePacketMirroringRuleFirewallPolicyRequest, options: CallOptions, callback: Callback<protos.google.cloud.compute.v1beta.IOperation, protos.google.cloud.compute.v1beta.IRemovePacketMirroringRuleFirewallPolicyRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IRemovePacketMirroringRuleFirewallPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.iremovepacketmirroringrulefirewallpolicyrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.compute.v1beta.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ioperation), [protos.google.cloud.compute.v1beta.IRemovePacketMirroringRuleFirewallPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.iremovepacketmirroringrulefirewallpolicyrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### removePacketMirroringRule(request, callback)
    
    
    removePacketMirroringRule(request: protos.google.cloud.compute.v1beta.IRemovePacketMirroringRuleFirewallPolicyRequest, callback: Callback<protos.google.cloud.compute.v1beta.IOperation, protos.google.cloud.compute.v1beta.IRemovePacketMirroringRuleFirewallPolicyRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IRemovePacketMirroringRuleFirewallPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.iremovepacketmirroringrulefirewallpolicyrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.compute.v1beta.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ioperation), [protos.google.cloud.compute.v1beta.IRemovePacketMirroringRuleFirewallPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.iremovepacketmirroringrulefirewallpolicyrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### removeRule(request, options)
    
    
    removeRule(request?: protos.google.cloud.compute.v1beta.IRemoveRuleFirewallPolicyRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.cloud.compute.v1beta.IOperation, null>,
            protos.google.cloud.compute.v1beta.IOperation | undefined,
            {} | undefined
        ]>;

Deletes a rule of the specified priority.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IRemoveRuleFirewallPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.iremoverulefirewallpolicyrequest)`   
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
      const {FirewallPoliciesClient} = require('[@google-cloud/compute](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const computeClient = new [FirewallPoliciesClient](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)();
    
      async function callRemoveRule() {
        // Construct request
        const request = {
          firewallPolicy,
        };
    
        // Run request
        const response = await computeClient.removeRule(request);
        console.log(response);
      }
    
      callRemoveRule();
    
    

### removeRule(request, options, callback)
    
    
    removeRule(request: protos.google.cloud.compute.v1beta.IRemoveRuleFirewallPolicyRequest, options: CallOptions, callback: Callback<protos.google.cloud.compute.v1beta.IOperation, protos.google.cloud.compute.v1beta.IRemoveRuleFirewallPolicyRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IRemoveRuleFirewallPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.iremoverulefirewallpolicyrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.compute.v1beta.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ioperation), [protos.google.cloud.compute.v1beta.IRemoveRuleFirewallPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.iremoverulefirewallpolicyrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### removeRule(request, callback)
    
    
    removeRule(request: protos.google.cloud.compute.v1beta.IRemoveRuleFirewallPolicyRequest, callback: Callback<protos.google.cloud.compute.v1beta.IOperation, protos.google.cloud.compute.v1beta.IRemoveRuleFirewallPolicyRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IRemoveRuleFirewallPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.iremoverulefirewallpolicyrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.compute.v1beta.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ioperation), [protos.google.cloud.compute.v1beta.IRemoveRuleFirewallPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.iremoverulefirewallpolicyrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### setIamPolicy(request, options)
    
    
    setIamPolicy(request?: protos.google.cloud.compute.v1beta.ISetIamPolicyFirewallPolicyRequest, options?: CallOptions): Promise<[
            protos.google.cloud.compute.v1beta.IPolicy,
            (protos.google.cloud.compute.v1beta.ISetIamPolicyFirewallPolicyRequest | undefined),
            {} | undefined
        ]>;

Sets the access control policy on the specified resource. Replaces any existing policy.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISetIamPolicyFirewallPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.isetiampolicyfirewallpolicyrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.compute.v1beta.IPolicy](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ipolicy), ([protos.google.cloud.compute.v1beta.ISetIamPolicyFirewallPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.isetiampolicyfirewallpolicyrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [Policy](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.policy). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
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
      // const globalOrganizationSetPolicyRequestResource = {}
      /**
       *  Name or id of the resource for this request.
       */
      // const resource = 'abc123'
    
      // Imports the Compute library
      const {FirewallPoliciesClient} = require('[@google-cloud/compute](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const computeClient = new [FirewallPoliciesClient](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)();
    
      async function callSetIamPolicy() {
        // Construct request
        const request = {
          globalOrganizationSetPolicyRequestResource,
          resource,
        };
    
        // Run request
        const response = await computeClient.setIamPolicy(request);
        console.log(response);
      }
    
      callSetIamPolicy();
    
    

### setIamPolicy(request, options, callback)
    
    
    setIamPolicy(request: protos.google.cloud.compute.v1beta.ISetIamPolicyFirewallPolicyRequest, options: CallOptions, callback: Callback<protos.google.cloud.compute.v1beta.IPolicy, protos.google.cloud.compute.v1beta.ISetIamPolicyFirewallPolicyRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISetIamPolicyFirewallPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.isetiampolicyfirewallpolicyrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.compute.v1beta.IPolicy](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ipolicy), [protos.google.cloud.compute.v1beta.ISetIamPolicyFirewallPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.isetiampolicyfirewallpolicyrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### setIamPolicy(request, callback)
    
    
    setIamPolicy(request: protos.google.cloud.compute.v1beta.ISetIamPolicyFirewallPolicyRequest, callback: Callback<protos.google.cloud.compute.v1beta.IPolicy, protos.google.cloud.compute.v1beta.ISetIamPolicyFirewallPolicyRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISetIamPolicyFirewallPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.isetiampolicyfirewallpolicyrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.compute.v1beta.IPolicy](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ipolicy), [protos.google.cloud.compute.v1beta.ISetIamPolicyFirewallPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.isetiampolicyfirewallpolicyrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### testIamPermissions(request, options)
    
    
    testIamPermissions(request?: protos.google.cloud.compute.v1beta.ITestIamPermissionsFirewallPolicyRequest, options?: CallOptions): Promise<[
            protos.google.cloud.compute.v1beta.ITestPermissionsResponse,
            (protos.google.cloud.compute.v1beta.ITestIamPermissionsFirewallPolicyRequest | undefined),
            {} | undefined
        ]>;

Returns permissions that a caller has on the specified resource.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ITestIamPermissionsFirewallPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.itestiampermissionsfirewallpolicyrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.compute.v1beta.ITestPermissionsResponse](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.itestpermissionsresponse), ([protos.google.cloud.compute.v1beta.ITestIamPermissionsFirewallPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.itestiampermissionsfirewallpolicyrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [TestPermissionsResponse](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.testpermissionsresponse). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Name or id of the resource for this request.
       */
      // const resource = 'abc123'
      /**
       *  The body resource for this request
       */
      // const testPermissionsRequestResource = {}
    
      // Imports the Compute library
      const {FirewallPoliciesClient} = require('[@google-cloud/compute](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const computeClient = new [FirewallPoliciesClient](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)();
    
      async function callTestIamPermissions() {
        // Construct request
        const request = {
          resource,
          testPermissionsRequestResource,
        };
    
        // Run request
        const response = await computeClient.testIamPermissions(request);
        console.log(response);
      }
    
      callTestIamPermissions();
    
    

### testIamPermissions(request, options, callback)
    
    
    testIamPermissions(request: protos.google.cloud.compute.v1beta.ITestIamPermissionsFirewallPolicyRequest, options: CallOptions, callback: Callback<protos.google.cloud.compute.v1beta.ITestPermissionsResponse, protos.google.cloud.compute.v1beta.ITestIamPermissionsFirewallPolicyRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ITestIamPermissionsFirewallPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.itestiampermissionsfirewallpolicyrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.compute.v1beta.ITestPermissionsResponse](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.itestpermissionsresponse), [protos.google.cloud.compute.v1beta.ITestIamPermissionsFirewallPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.itestiampermissionsfirewallpolicyrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### testIamPermissions(request, callback)
    
    
    testIamPermissions(request: protos.google.cloud.compute.v1beta.ITestIamPermissionsFirewallPolicyRequest, callback: Callback<protos.google.cloud.compute.v1beta.ITestPermissionsResponse, protos.google.cloud.compute.v1beta.ITestIamPermissionsFirewallPolicyRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ITestIamPermissionsFirewallPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.itestiampermissionsfirewallpolicyrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.compute.v1beta.ITestPermissionsResponse](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.itestpermissionsresponse), [protos.google.cloud.compute.v1beta.ITestIamPermissionsFirewallPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.itestiampermissionsfirewallpolicyrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
