---
url: https://docs.cloud.google.com/nodejs/docs/reference/recaptcha-enterprise/latest/recaptcha-enterprise/v1beta1.recaptchaenterpriseservicev1beta1client
title: Class v1beta1.RecaptchaEnterpriseServiceV1Beta1Client (7.2.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:22:13.685898+00:00
---

# Class v1beta1.RecaptchaEnterpriseServiceV1Beta1Client (7.2.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/recaptcha-enterprise/latest/recaptcha-enterprise/v1beta1.recaptchaenterpriseservicev1beta1client

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class v1beta1.RecaptchaEnterpriseServiceV1Beta1Client (7.2.1) Stay organized with collections  Save and categorize content based on your preferences. 

7.2.1 (latest)  6.2.0  6.0.1  5.13.0  5.11.0  5.10.0  5.8.0  5.5.0  5.4.0  5.2.0  5.1.1  5.0.0  4.1.0  3.4.1  3.3.1  3.1.1  3.0.4  2.5.0  2.4.0  2.3.0  2.2.1  2.1.7 

Service to determine the likelihood an event is legitimate. v1beta1

## Package

[@google-cloud/recaptcha-enterprise](https://docs.cloud.google.com/nodejs/docs/reference/recaptcha-enterprise/latest/overview.html)

## Constructors 

### (constructor)(opts, gaxInstance)
    
    
    constructor(opts?: ClientOptions, gaxInstance?: typeof gax | typeof gax.fallback);

Construct an instance of RecaptchaEnterpriseServiceV1Beta1Client.

**Parameters**  
---  
**Name** | **Description**  
`opts` |  `ClientOptions`   
  
`gaxInstance` |  `typeof gax | typeof fallback`   
: loaded instance of `google-gax`. Useful if you need to avoid loading the default gRPC version and want to use the fallback HTTP implementation. Load only fallback version and pass it to the constructor: ``` const gax = require('google-gax/build/src/fallback'); // avoids loading google-gax with gRPC const client = new RecaptchaEnterpriseServiceV1Beta1Client({fallback: true}, gax); ```  
  
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

### port
    
    
    static get port(): number;

The port for this API service.

### recaptchaEnterpriseServiceV1Beta1Stub
    
    
    recaptchaEnterpriseServiceV1Beta1Stub?: Promise<{
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

### annotateAssessment(request, options)
    
    
    annotateAssessment(request?: protos.google.cloud.recaptchaenterprise.v1beta1.IAnnotateAssessmentRequest, options?: CallOptions): Promise<[
            protos.google.cloud.recaptchaenterprise.v1beta1.IAnnotateAssessmentResponse,
            (protos.google.cloud.recaptchaenterprise.v1beta1.IAnnotateAssessmentRequest | undefined),
            {} | undefined
        ]>;

Annotates a previously created Assessment to provide additional information on whether the event turned out to be authentic or fradulent.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IAnnotateAssessmentRequest](https://docs.cloud.google.com/nodejs/docs/reference/recaptcha-enterprise/latest/recaptcha-enterprise/protos.google.cloud.recaptchaenterprise.v1beta1.iannotateassessmentrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.recaptchaenterprise.v1beta1.IAnnotateAssessmentResponse](https://docs.cloud.google.com/nodejs/docs/reference/recaptcha-enterprise/latest/recaptcha-enterprise/protos.google.cloud.recaptchaenterprise.v1beta1.iannotateassessmentresponse), ([protos.google.cloud.recaptchaenterprise.v1beta1.IAnnotateAssessmentRequest](https://docs.cloud.google.com/nodejs/docs/reference/recaptcha-enterprise/latest/recaptcha-enterprise/protos.google.cloud.recaptchaenterprise.v1beta1.iannotateassessmentrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [AnnotateAssessmentResponse](https://docs.cloud.google.com/nodejs/docs/reference/recaptcha-enterprise/latest/recaptcha-enterprise/protos.google.cloud.recaptchaenterprise.v1beta1.annotateassessmentresponse). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The resource name of the Assessment, in the format
       *  `projects/{project_number}/assessments/{assessment_id}`.
       */
      // const name = 'abc123'
      /**
       *  Optional. The annotation that is assigned to the Event. This field can be
       *  left empty to provide reasons that apply to an event without concluding
       *  whether the event is legitimate or fraudulent.
       */
      // const annotation = {}
      /**
       *  Optional. Reasons for the annotation that are assigned to the event.
       */
      // const reasons = [1,2,3,4]
      /**
       *  Optional. Unique stable hashed user identifier to apply to the assessment.
       *  This is an alternative to setting the `hashed_account_id` in
       *  `CreateAssessment`, for example, when the account identifier is not yet
       *  known in the initial request. It is recommended that the identifier is
       *  hashed using hmac-sha256 with stable secret.
       */
      // const hashedAccountId = Buffer.from('string')
      /**
       *  Optional. If the assessment is part of a payment transaction, provide
       *  details on payment lifecycle events that occur in the transaction.
       */
      // const transactionEvent = {}
    
      // Imports the Recaptchaenterprise library
      const {RecaptchaEnterpriseServiceV1Beta1Client} = require('[@google-cloud/recaptcha-enterprise](https://docs.cloud.google.com/nodejs/docs/reference/recaptcha-enterprise/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const recaptchaenterpriseClient = new [RecaptchaEnterpriseServiceV1Beta1Client](https://docs.cloud.google.com/nodejs/docs/reference/recaptcha-enterprise/latest/recaptcha-enterprise/v1beta1.recaptchaenterpriseservicev1beta1client.html)();
    
      async function callAnnotateAssessment() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await recaptchaenterpriseClient.annotateAssessment(request);
        console.log(response);
      }
    
      callAnnotateAssessment();
    
    

### annotateAssessment(request, options, callback)
    
    
    annotateAssessment(request: protos.google.cloud.recaptchaenterprise.v1beta1.IAnnotateAssessmentRequest, options: CallOptions, callback: Callback<protos.google.cloud.recaptchaenterprise.v1beta1.IAnnotateAssessmentResponse, protos.google.cloud.recaptchaenterprise.v1beta1.IAnnotateAssessmentRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IAnnotateAssessmentRequest](https://docs.cloud.google.com/nodejs/docs/reference/recaptcha-enterprise/latest/recaptcha-enterprise/protos.google.cloud.recaptchaenterprise.v1beta1.iannotateassessmentrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.recaptchaenterprise.v1beta1.IAnnotateAssessmentResponse](https://docs.cloud.google.com/nodejs/docs/reference/recaptcha-enterprise/latest/recaptcha-enterprise/protos.google.cloud.recaptchaenterprise.v1beta1.iannotateassessmentresponse), [protos.google.cloud.recaptchaenterprise.v1beta1.IAnnotateAssessmentRequest](https://docs.cloud.google.com/nodejs/docs/reference/recaptcha-enterprise/latest/recaptcha-enterprise/protos.google.cloud.recaptchaenterprise.v1beta1.iannotateassessmentrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### annotateAssessment(request, callback)
    
    
    annotateAssessment(request: protos.google.cloud.recaptchaenterprise.v1beta1.IAnnotateAssessmentRequest, callback: Callback<protos.google.cloud.recaptchaenterprise.v1beta1.IAnnotateAssessmentResponse, protos.google.cloud.recaptchaenterprise.v1beta1.IAnnotateAssessmentRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IAnnotateAssessmentRequest](https://docs.cloud.google.com/nodejs/docs/reference/recaptcha-enterprise/latest/recaptcha-enterprise/protos.google.cloud.recaptchaenterprise.v1beta1.iannotateassessmentrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.recaptchaenterprise.v1beta1.IAnnotateAssessmentResponse](https://docs.cloud.google.com/nodejs/docs/reference/recaptcha-enterprise/latest/recaptcha-enterprise/protos.google.cloud.recaptchaenterprise.v1beta1.iannotateassessmentresponse), [protos.google.cloud.recaptchaenterprise.v1beta1.IAnnotateAssessmentRequest](https://docs.cloud.google.com/nodejs/docs/reference/recaptcha-enterprise/latest/recaptcha-enterprise/protos.google.cloud.recaptchaenterprise.v1beta1.iannotateassessmentrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### assessmentPath(project, assessment)
    
    
    assessmentPath(project: string, assessment: string): string;

Return a fully-qualified assessment resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`assessment` |  `string`   
  
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
  
### createAssessment(request, options)
    
    
    createAssessment(request?: protos.google.cloud.recaptchaenterprise.v1beta1.ICreateAssessmentRequest, options?: CallOptions): Promise<[
            protos.google.cloud.recaptchaenterprise.v1beta1.IAssessment,
            (protos.google.cloud.recaptchaenterprise.v1beta1.ICreateAssessmentRequest | undefined),
            {} | undefined
        ]>;

Creates an Assessment of the likelihood an event is legitimate.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateAssessmentRequest](https://docs.cloud.google.com/nodejs/docs/reference/recaptcha-enterprise/latest/recaptcha-enterprise/protos.google.cloud.recaptchaenterprise.v1beta1.icreateassessmentrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.recaptchaenterprise.v1beta1.IAssessment](https://docs.cloud.google.com/nodejs/docs/reference/recaptcha-enterprise/latest/recaptcha-enterprise/protos.google.cloud.recaptchaenterprise.v1beta1.iassessment), ([protos.google.cloud.recaptchaenterprise.v1beta1.ICreateAssessmentRequest](https://docs.cloud.google.com/nodejs/docs/reference/recaptcha-enterprise/latest/recaptcha-enterprise/protos.google.cloud.recaptchaenterprise.v1beta1.icreateassessmentrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The name of the project in which the assessment is created,
       *  in the format `projects/{project_number}`.
       */
      // const parent = 'abc123'
      /**
       *  Required. The assessment details.
       */
      // const assessment = {}
    
      // Imports the Recaptchaenterprise library
      const {RecaptchaEnterpriseServiceV1Beta1Client} = require('[@google-cloud/recaptcha-enterprise](https://docs.cloud.google.com/nodejs/docs/reference/recaptcha-enterprise/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const recaptchaenterpriseClient = new [RecaptchaEnterpriseServiceV1Beta1Client](https://docs.cloud.google.com/nodejs/docs/reference/recaptcha-enterprise/latest/recaptcha-enterprise/v1beta1.recaptchaenterpriseservicev1beta1client.html)();
    
      async function callCreateAssessment() {
        // Construct request
        const request = {
          parent,
          assessment,
        };
    
        // Run request
        const response = await recaptchaenterpriseClient.createAssessment(request);
        console.log(response);
      }
    
      callCreateAssessment();
    
    

### createAssessment(request, options, callback)
    
    
    createAssessment(request: protos.google.cloud.recaptchaenterprise.v1beta1.ICreateAssessmentRequest, options: CallOptions, callback: Callback<protos.google.cloud.recaptchaenterprise.v1beta1.IAssessment, protos.google.cloud.recaptchaenterprise.v1beta1.ICreateAssessmentRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateAssessmentRequest](https://docs.cloud.google.com/nodejs/docs/reference/recaptcha-enterprise/latest/recaptcha-enterprise/protos.google.cloud.recaptchaenterprise.v1beta1.icreateassessmentrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.recaptchaenterprise.v1beta1.IAssessment](https://docs.cloud.google.com/nodejs/docs/reference/recaptcha-enterprise/latest/recaptcha-enterprise/protos.google.cloud.recaptchaenterprise.v1beta1.iassessment), [protos.google.cloud.recaptchaenterprise.v1beta1.ICreateAssessmentRequest](https://docs.cloud.google.com/nodejs/docs/reference/recaptcha-enterprise/latest/recaptcha-enterprise/protos.google.cloud.recaptchaenterprise.v1beta1.icreateassessmentrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createAssessment(request, callback)
    
    
    createAssessment(request: protos.google.cloud.recaptchaenterprise.v1beta1.ICreateAssessmentRequest, callback: Callback<protos.google.cloud.recaptchaenterprise.v1beta1.IAssessment, protos.google.cloud.recaptchaenterprise.v1beta1.ICreateAssessmentRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateAssessmentRequest](https://docs.cloud.google.com/nodejs/docs/reference/recaptcha-enterprise/latest/recaptcha-enterprise/protos.google.cloud.recaptchaenterprise.v1beta1.icreateassessmentrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.recaptchaenterprise.v1beta1.IAssessment](https://docs.cloud.google.com/nodejs/docs/reference/recaptcha-enterprise/latest/recaptcha-enterprise/protos.google.cloud.recaptchaenterprise.v1beta1.iassessment), [protos.google.cloud.recaptchaenterprise.v1beta1.ICreateAssessmentRequest](https://docs.cloud.google.com/nodejs/docs/reference/recaptcha-enterprise/latest/recaptcha-enterprise/protos.google.cloud.recaptchaenterprise.v1beta1.icreateassessmentrequest) | null | undefined, {} | null | undefined>`   
  
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
  
### matchAssessmentFromAssessmentName(assessmentName)
    
    
    matchAssessmentFromAssessmentName(assessmentName: string): string | number;

Parse the assessment from Assessment resource.

**Parameter**  
---  
**Name** | **Description**  
`assessmentName` |  `string`   
A fully-qualified path representing Assessment resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the assessment.  
  
### matchProjectFromAssessmentName(assessmentName)
    
    
    matchProjectFromAssessmentName(assessmentName: string): string | number;

Parse the project from Assessment resource.

**Parameter**  
---  
**Name** | **Description**  
`assessmentName` |  `string`   
A fully-qualified path representing Assessment resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
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
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
