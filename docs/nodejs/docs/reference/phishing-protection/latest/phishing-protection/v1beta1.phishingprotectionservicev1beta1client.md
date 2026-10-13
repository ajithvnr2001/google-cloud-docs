---
url: https://docs.cloud.google.com/nodejs/docs/reference/phishing-protection/latest/phishing-protection/v1beta1.phishingprotectionservicev1beta1client
title: Class v1beta1.PhishingProtectionServiceV1Beta1Client (6.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:51:43.354939+00:00
---

# Class v1beta1.PhishingProtectionServiceV1Beta1Client (6.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/phishing-protection/latest/phishing-protection/v1beta1.phishingprotectionservicev1beta1client

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class v1beta1.PhishingProtectionServiceV1Beta1Client (6.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

6.1.1 (latest)  5.1.0  5.0.1  3.0.8  2.5.0  2.4.7 

Service to report phishing URIs. v1beta1

## Package

[@google-cloud/phishing-protection](https://docs.cloud.google.com/nodejs/docs/reference/phishing-protection/latest/overview.html)

## Constructors 

### (constructor)(opts, gaxInstance)
    
    
    constructor(opts?: ClientOptions, gaxInstance?: typeof gax | typeof gax.fallback);

Construct an instance of PhishingProtectionServiceV1Beta1Client.

**Parameters**  
---  
**Name** | **Description**  
`opts` |  `ClientOptions`   
  
`gaxInstance` |  `typeof gax | typeof fallback`   
: loaded instance of `google-gax`. Useful if you need to avoid loading the default gRPC version and want to use the fallback HTTP implementation. Load only fallback version and pass it to the constructor: ``` const gax = require('google-gax/build/src/fallback'); // avoids loading google-gax with gRPC const client = new PhishingProtectionServiceV1Beta1Client({fallback: true}, gax); ```  
  
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

### pathTemplates
    
    
    pathTemplates: {
            [name: string]: gax.PathTemplate;
        };

### phishingProtectionServiceV1Beta1Stub
    
    
    phishingProtectionServiceV1Beta1Stub?: Promise<{
            [name: string]: Function;
        }>;

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

### close()
    
    
    close(): Promise<void>;

Terminate the gRPC channel and close the client.

The client will no longer be usable and all future behavior is undefined.

**Returns**  
---  
**Type** | **Description**  
`Promise<void>` | {Promise} A promise that resolves when the client is closed.  
  
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
  
### matchProjectFromProjectName(projectName)
    
    
    matchProjectFromProjectName(projectName: string): string | number;

Parse the project from Project resource.

**Parameter**  
---  
**Name** | **Description**  
`projectName` |  `string`   
A fully-qualified path representing Project resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### projectPath(project)
    
    
    projectPath(project: string): string;

Return a fully-qualified project resource name string.

**Parameter**  
---  
**Name** | **Description**  
`project` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### reportPhishing(request, options)
    
    
    reportPhishing(request?: protos.google.cloud.phishingprotection.v1beta1.IReportPhishingRequest, options?: CallOptions): Promise<[
            protos.google.cloud.phishingprotection.v1beta1.IReportPhishingResponse,
            (protos.google.cloud.phishingprotection.v1beta1.IReportPhishingRequest | undefined),
            {} | undefined
        ]>;

Reports a URI suspected of containing phishing content to be reviewed. Once the report review is complete, its result can be found in the Cloud Security Command Center findings dashboard for Phishing Protection. If the result verifies the existence of malicious phishing content, the site will be added the to [Google's Social Engineering lists](<https://support.google.com/webmasters/answer/6350487/>) in order to protect users that could get exposed to this threat in the future.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IReportPhishingRequest](https://docs.cloud.google.com/nodejs/docs/reference/phishing-protection/latest/phishing-protection/protos.google.cloud.phishingprotection.v1beta1.ireportphishingrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.phishingprotection.v1beta1.IReportPhishingResponse](https://docs.cloud.google.com/nodejs/docs/reference/phishing-protection/latest/phishing-protection/protos.google.cloud.phishingprotection.v1beta1.ireportphishingresponse), ([protos.google.cloud.phishingprotection.v1beta1.IReportPhishingRequest](https://docs.cloud.google.com/nodejs/docs/reference/phishing-protection/latest/phishing-protection/protos.google.cloud.phishingprotection.v1beta1.ireportphishingrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [ReportPhishingResponse](https://docs.cloud.google.com/nodejs/docs/reference/phishing-protection/latest/phishing-protection/protos.google.cloud.phishingprotection.v1beta1.reportphishingresponse). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The name of the project for which the report will be created,
       *  in the format "projects/{project_number}".
       */
      // const parent = 'abc123'
      /**
       *  Required. The URI that is being reported for phishing content to be analyzed.
       */
      // const uri = 'abc123'
    
      // Imports the Phishingprotection library
      const {PhishingProtectionServiceV1Beta1Client} = require('[@google-cloud/phishing-protection](https://docs.cloud.google.com/nodejs/docs/reference/phishing-protection/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const phishingprotectionClient = new [PhishingProtectionServiceV1Beta1Client](https://docs.cloud.google.com/nodejs/docs/reference/phishing-protection/latest/overview.html)();
    
      async function callReportPhishing() {
        // Construct request
        const request = {
          parent,
          uri,
        };
    
        // Run request
        const response = await phishingprotectionClient.reportPhishing(request);
        console.log(response);
      }
    
      callReportPhishing();
    
    

### reportPhishing(request, options, callback)
    
    
    reportPhishing(request: protos.google.cloud.phishingprotection.v1beta1.IReportPhishingRequest, options: CallOptions, callback: Callback<protos.google.cloud.phishingprotection.v1beta1.IReportPhishingResponse, protos.google.cloud.phishingprotection.v1beta1.IReportPhishingRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IReportPhishingRequest](https://docs.cloud.google.com/nodejs/docs/reference/phishing-protection/latest/phishing-protection/protos.google.cloud.phishingprotection.v1beta1.ireportphishingrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.phishingprotection.v1beta1.IReportPhishingResponse](https://docs.cloud.google.com/nodejs/docs/reference/phishing-protection/latest/phishing-protection/protos.google.cloud.phishingprotection.v1beta1.ireportphishingresponse), [protos.google.cloud.phishingprotection.v1beta1.IReportPhishingRequest](https://docs.cloud.google.com/nodejs/docs/reference/phishing-protection/latest/phishing-protection/protos.google.cloud.phishingprotection.v1beta1.ireportphishingrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### reportPhishing(request, callback)
    
    
    reportPhishing(request: protos.google.cloud.phishingprotection.v1beta1.IReportPhishingRequest, callback: Callback<protos.google.cloud.phishingprotection.v1beta1.IReportPhishingResponse, protos.google.cloud.phishingprotection.v1beta1.IReportPhishingRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IReportPhishingRequest](https://docs.cloud.google.com/nodejs/docs/reference/phishing-protection/latest/phishing-protection/protos.google.cloud.phishingprotection.v1beta1.ireportphishingrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.phishingprotection.v1beta1.IReportPhishingResponse](https://docs.cloud.google.com/nodejs/docs/reference/phishing-protection/latest/phishing-protection/protos.google.cloud.phishingprotection.v1beta1.ireportphishingresponse), [protos.google.cloud.phishingprotection.v1beta1.IReportPhishingRequest](https://docs.cloud.google.com/nodejs/docs/reference/phishing-protection/latest/phishing-protection/protos.google.cloud.phishingprotection.v1beta1.ireportphishingrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
