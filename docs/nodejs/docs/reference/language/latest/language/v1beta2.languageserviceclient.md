---
url: https://docs.cloud.google.com/nodejs/docs/reference/language/latest/language/v1beta2.languageserviceclient
title: Class v1beta2.LanguageServiceClient (8.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:41:52.969544+00:00
---

# Class v1beta2.LanguageServiceClient (8.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/language/latest/language/v1beta2.languageserviceclient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class v1beta2.LanguageServiceClient (8.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

8.1.1 (latest)  8.0.1  7.1.0  6.5.0  5.2.2  5.1.2  5.0.2  4.3.2  4.2.9 

Provides text analysis operations such as sentiment analysis and entity recognition. v1beta2

## Package

[@google-cloud/language](https://docs.cloud.google.com/nodejs/docs/reference/language/latest/overview.html)

## Constructors 

### (constructor)(opts, gaxInstance)
    
    
    constructor(opts?: ClientOptions, gaxInstance?: typeof gax | typeof gax.fallback);

Construct an instance of LanguageServiceClient.

**Parameters**  
---  
**Name** | **Description**  
`opts` |  `ClientOptions`   
  
`gaxInstance` |  `typeof gax | typeof fallback`   
: loaded instance of `google-gax`. Useful if you need to avoid loading the default gRPC version and want to use the fallback HTTP implementation. Load only fallback version and pass it to the constructor: ``` const gax = require('google-gax/build/src/fallback'); // avoids loading google-gax with gRPC const client = new LanguageServiceClient({fallback: true}, gax); ```  
  
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

### languageServiceStub
    
    
    languageServiceStub?: Promise<{
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

### analyzeEntities(request, options)
    
    
    analyzeEntities(request?: protos.google.cloud.language.v1beta2.IAnalyzeEntitiesRequest, options?: CallOptions): Promise<[
            protos.google.cloud.language.v1beta2.IAnalyzeEntitiesResponse,
            protos.google.cloud.language.v1beta2.IAnalyzeEntitiesRequest | undefined,
            {} | undefined
        ]>;

Finds named entities (currently proper names and common nouns) in the text along with entity types, salience, mentions for each entity, and other properties.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IAnalyzeEntitiesRequest](https://docs.cloud.google.com/nodejs/docs/reference/language/latest/language/protos.google.cloud.language.v1beta2.ianalyzeentitiesrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.language.v1beta2.IAnalyzeEntitiesResponse](https://docs.cloud.google.com/nodejs/docs/reference/language/latest/language/protos.google.cloud.language.v1beta2.ianalyzeentitiesresponse), [protos.google.cloud.language.v1beta2.IAnalyzeEntitiesRequest](https://docs.cloud.google.com/nodejs/docs/reference/language/latest/language/protos.google.cloud.language.v1beta2.ianalyzeentitiesrequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [AnalyzeEntitiesResponse](https://docs.cloud.google.com/nodejs/docs/reference/language/latest/language/protos.google.cloud.language.v1beta2.analyzeentitiesresponse). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Input document.
       */
      // const document = {}
      /**
       *  The encoding type used by the API to calculate offsets.
       */
      // const encodingType = {}
    
      // Imports the Language library
      const {LanguageServiceClient} = require('[@google-cloud/language](https://docs.cloud.google.com/nodejs/docs/reference/language/latest/overview.html)').v1beta2;
    
      // Instantiates a client
      const languageClient = new [LanguageServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/language/latest/overview.html)();
    
      async function callAnalyzeEntities() {
        // Construct request
        const request = {
          document,
        };
    
        // Run request
        const response = await languageClient.analyzeEntities(request);
        console.log(response);
      }
    
      callAnalyzeEntities();
    
    

### analyzeEntities(request, options, callback)
    
    
    analyzeEntities(request: protos.google.cloud.language.v1beta2.IAnalyzeEntitiesRequest, options: CallOptions, callback: Callback<protos.google.cloud.language.v1beta2.IAnalyzeEntitiesResponse, protos.google.cloud.language.v1beta2.IAnalyzeEntitiesRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IAnalyzeEntitiesRequest](https://docs.cloud.google.com/nodejs/docs/reference/language/latest/language/protos.google.cloud.language.v1beta2.ianalyzeentitiesrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.language.v1beta2.IAnalyzeEntitiesResponse](https://docs.cloud.google.com/nodejs/docs/reference/language/latest/language/protos.google.cloud.language.v1beta2.ianalyzeentitiesresponse), [protos.google.cloud.language.v1beta2.IAnalyzeEntitiesRequest](https://docs.cloud.google.com/nodejs/docs/reference/language/latest/language/protos.google.cloud.language.v1beta2.ianalyzeentitiesrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### analyzeEntities(request, callback)
    
    
    analyzeEntities(request: protos.google.cloud.language.v1beta2.IAnalyzeEntitiesRequest, callback: Callback<protos.google.cloud.language.v1beta2.IAnalyzeEntitiesResponse, protos.google.cloud.language.v1beta2.IAnalyzeEntitiesRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IAnalyzeEntitiesRequest](https://docs.cloud.google.com/nodejs/docs/reference/language/latest/language/protos.google.cloud.language.v1beta2.ianalyzeentitiesrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.language.v1beta2.IAnalyzeEntitiesResponse](https://docs.cloud.google.com/nodejs/docs/reference/language/latest/language/protos.google.cloud.language.v1beta2.ianalyzeentitiesresponse), [protos.google.cloud.language.v1beta2.IAnalyzeEntitiesRequest](https://docs.cloud.google.com/nodejs/docs/reference/language/latest/language/protos.google.cloud.language.v1beta2.ianalyzeentitiesrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### analyzeEntitySentiment(request, options)
    
    
    analyzeEntitySentiment(request?: protos.google.cloud.language.v1beta2.IAnalyzeEntitySentimentRequest, options?: CallOptions): Promise<[
            protos.google.cloud.language.v1beta2.IAnalyzeEntitySentimentResponse,
            (protos.google.cloud.language.v1beta2.IAnalyzeEntitySentimentRequest | undefined),
            {} | undefined
        ]>;

Finds entities, similar to in the text and analyzes sentiment associated with each entity and its mentions.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IAnalyzeEntitySentimentRequest](https://docs.cloud.google.com/nodejs/docs/reference/language/latest/language/protos.google.cloud.language.v1beta2.ianalyzeentitysentimentrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.language.v1beta2.IAnalyzeEntitySentimentResponse](https://docs.cloud.google.com/nodejs/docs/reference/language/latest/language/protos.google.cloud.language.v1beta2.ianalyzeentitysentimentresponse), ([protos.google.cloud.language.v1beta2.IAnalyzeEntitySentimentRequest](https://docs.cloud.google.com/nodejs/docs/reference/language/latest/language/protos.google.cloud.language.v1beta2.ianalyzeentitysentimentrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [AnalyzeEntitySentimentResponse](https://docs.cloud.google.com/nodejs/docs/reference/language/latest/language/protos.google.cloud.language.v1beta2.analyzeentitysentimentresponse). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Input document.
       */
      // const document = {}
      /**
       *  The encoding type used by the API to calculate offsets.
       */
      // const encodingType = {}
    
      // Imports the Language library
      const {LanguageServiceClient} = require('[@google-cloud/language](https://docs.cloud.google.com/nodejs/docs/reference/language/latest/overview.html)').v1beta2;
    
      // Instantiates a client
      const languageClient = new [LanguageServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/language/latest/overview.html)();
    
      async function callAnalyzeEntitySentiment() {
        // Construct request
        const request = {
          document,
        };
    
        // Run request
        const response = await languageClient.analyzeEntitySentiment(request);
        console.log(response);
      }
    
      callAnalyzeEntitySentiment();
    
    

### analyzeEntitySentiment(request, options, callback)
    
    
    analyzeEntitySentiment(request: protos.google.cloud.language.v1beta2.IAnalyzeEntitySentimentRequest, options: CallOptions, callback: Callback<protos.google.cloud.language.v1beta2.IAnalyzeEntitySentimentResponse, protos.google.cloud.language.v1beta2.IAnalyzeEntitySentimentRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IAnalyzeEntitySentimentRequest](https://docs.cloud.google.com/nodejs/docs/reference/language/latest/language/protos.google.cloud.language.v1beta2.ianalyzeentitysentimentrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.language.v1beta2.IAnalyzeEntitySentimentResponse](https://docs.cloud.google.com/nodejs/docs/reference/language/latest/language/protos.google.cloud.language.v1beta2.ianalyzeentitysentimentresponse), [protos.google.cloud.language.v1beta2.IAnalyzeEntitySentimentRequest](https://docs.cloud.google.com/nodejs/docs/reference/language/latest/language/protos.google.cloud.language.v1beta2.ianalyzeentitysentimentrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### analyzeEntitySentiment(request, callback)
    
    
    analyzeEntitySentiment(request: protos.google.cloud.language.v1beta2.IAnalyzeEntitySentimentRequest, callback: Callback<protos.google.cloud.language.v1beta2.IAnalyzeEntitySentimentResponse, protos.google.cloud.language.v1beta2.IAnalyzeEntitySentimentRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IAnalyzeEntitySentimentRequest](https://docs.cloud.google.com/nodejs/docs/reference/language/latest/language/protos.google.cloud.language.v1beta2.ianalyzeentitysentimentrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.language.v1beta2.IAnalyzeEntitySentimentResponse](https://docs.cloud.google.com/nodejs/docs/reference/language/latest/language/protos.google.cloud.language.v1beta2.ianalyzeentitysentimentresponse), [protos.google.cloud.language.v1beta2.IAnalyzeEntitySentimentRequest](https://docs.cloud.google.com/nodejs/docs/reference/language/latest/language/protos.google.cloud.language.v1beta2.ianalyzeentitysentimentrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### analyzeSentiment(request, options)
    
    
    analyzeSentiment(request?: protos.google.cloud.language.v1beta2.IAnalyzeSentimentRequest, options?: CallOptions): Promise<[
            protos.google.cloud.language.v1beta2.IAnalyzeSentimentResponse,
            protos.google.cloud.language.v1beta2.IAnalyzeSentimentRequest | undefined,
            {} | undefined
        ]>;

Analyzes the sentiment of the provided text.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IAnalyzeSentimentRequest](https://docs.cloud.google.com/nodejs/docs/reference/language/latest/language/protos.google.cloud.language.v1beta2.ianalyzesentimentrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.language.v1beta2.IAnalyzeSentimentResponse](https://docs.cloud.google.com/nodejs/docs/reference/language/latest/language/protos.google.cloud.language.v1beta2.ianalyzesentimentresponse), [protos.google.cloud.language.v1beta2.IAnalyzeSentimentRequest](https://docs.cloud.google.com/nodejs/docs/reference/language/latest/language/protos.google.cloud.language.v1beta2.ianalyzesentimentrequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [AnalyzeSentimentResponse](https://docs.cloud.google.com/nodejs/docs/reference/language/latest/language/protos.google.cloud.language.v1beta2.analyzesentimentresponse). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Input document.
       */
      // const document = {}
      /**
       *  The encoding type used by the API to calculate sentence offsets for the
       *  sentence sentiment.
       */
      // const encodingType = {}
    
      // Imports the Language library
      const {LanguageServiceClient} = require('[@google-cloud/language](https://docs.cloud.google.com/nodejs/docs/reference/language/latest/overview.html)').v1beta2;
    
      // Instantiates a client
      const languageClient = new [LanguageServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/language/latest/overview.html)();
    
      async function callAnalyzeSentiment() {
        // Construct request
        const request = {
          document,
        };
    
        // Run request
        const response = await languageClient.analyzeSentiment(request);
        console.log(response);
      }
    
      callAnalyzeSentiment();
    
    

### analyzeSentiment(request, options, callback)
    
    
    analyzeSentiment(request: protos.google.cloud.language.v1beta2.IAnalyzeSentimentRequest, options: CallOptions, callback: Callback<protos.google.cloud.language.v1beta2.IAnalyzeSentimentResponse, protos.google.cloud.language.v1beta2.IAnalyzeSentimentRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IAnalyzeSentimentRequest](https://docs.cloud.google.com/nodejs/docs/reference/language/latest/language/protos.google.cloud.language.v1beta2.ianalyzesentimentrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.language.v1beta2.IAnalyzeSentimentResponse](https://docs.cloud.google.com/nodejs/docs/reference/language/latest/language/protos.google.cloud.language.v1beta2.ianalyzesentimentresponse), [protos.google.cloud.language.v1beta2.IAnalyzeSentimentRequest](https://docs.cloud.google.com/nodejs/docs/reference/language/latest/language/protos.google.cloud.language.v1beta2.ianalyzesentimentrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### analyzeSentiment(request, callback)
    
    
    analyzeSentiment(request: protos.google.cloud.language.v1beta2.IAnalyzeSentimentRequest, callback: Callback<protos.google.cloud.language.v1beta2.IAnalyzeSentimentResponse, protos.google.cloud.language.v1beta2.IAnalyzeSentimentRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IAnalyzeSentimentRequest](https://docs.cloud.google.com/nodejs/docs/reference/language/latest/language/protos.google.cloud.language.v1beta2.ianalyzesentimentrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.language.v1beta2.IAnalyzeSentimentResponse](https://docs.cloud.google.com/nodejs/docs/reference/language/latest/language/protos.google.cloud.language.v1beta2.ianalyzesentimentresponse), [protos.google.cloud.language.v1beta2.IAnalyzeSentimentRequest](https://docs.cloud.google.com/nodejs/docs/reference/language/latest/language/protos.google.cloud.language.v1beta2.ianalyzesentimentrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### analyzeSyntax(request, options)
    
    
    analyzeSyntax(request?: protos.google.cloud.language.v1beta2.IAnalyzeSyntaxRequest, options?: CallOptions): Promise<[
            protos.google.cloud.language.v1beta2.IAnalyzeSyntaxResponse,
            protos.google.cloud.language.v1beta2.IAnalyzeSyntaxRequest | undefined,
            {} | undefined
        ]>;

Analyzes the syntax of the text and provides sentence boundaries and tokenization along with part of speech tags, dependency trees, and other properties.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IAnalyzeSyntaxRequest](https://docs.cloud.google.com/nodejs/docs/reference/language/latest/language/protos.google.cloud.language.v1beta2.ianalyzesyntaxrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.language.v1beta2.IAnalyzeSyntaxResponse](https://docs.cloud.google.com/nodejs/docs/reference/language/latest/language/protos.google.cloud.language.v1beta2.ianalyzesyntaxresponse), [protos.google.cloud.language.v1beta2.IAnalyzeSyntaxRequest](https://docs.cloud.google.com/nodejs/docs/reference/language/latest/language/protos.google.cloud.language.v1beta2.ianalyzesyntaxrequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [AnalyzeSyntaxResponse](https://docs.cloud.google.com/nodejs/docs/reference/language/latest/language/protos.google.cloud.language.v1beta2.analyzesyntaxresponse). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Input document.
       */
      // const document = {}
      /**
       *  The encoding type used by the API to calculate offsets.
       */
      // const encodingType = {}
    
      // Imports the Language library
      const {LanguageServiceClient} = require('[@google-cloud/language](https://docs.cloud.google.com/nodejs/docs/reference/language/latest/overview.html)').v1beta2;
    
      // Instantiates a client
      const languageClient = new [LanguageServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/language/latest/overview.html)();
    
      async function callAnalyzeSyntax() {
        // Construct request
        const request = {
          document,
        };
    
        // Run request
        const response = await languageClient.analyzeSyntax(request);
        console.log(response);
      }
    
      callAnalyzeSyntax();
    
    

### analyzeSyntax(request, options, callback)
    
    
    analyzeSyntax(request: protos.google.cloud.language.v1beta2.IAnalyzeSyntaxRequest, options: CallOptions, callback: Callback<protos.google.cloud.language.v1beta2.IAnalyzeSyntaxResponse, protos.google.cloud.language.v1beta2.IAnalyzeSyntaxRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IAnalyzeSyntaxRequest](https://docs.cloud.google.com/nodejs/docs/reference/language/latest/language/protos.google.cloud.language.v1beta2.ianalyzesyntaxrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.language.v1beta2.IAnalyzeSyntaxResponse](https://docs.cloud.google.com/nodejs/docs/reference/language/latest/language/protos.google.cloud.language.v1beta2.ianalyzesyntaxresponse), [protos.google.cloud.language.v1beta2.IAnalyzeSyntaxRequest](https://docs.cloud.google.com/nodejs/docs/reference/language/latest/language/protos.google.cloud.language.v1beta2.ianalyzesyntaxrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### analyzeSyntax(request, callback)
    
    
    analyzeSyntax(request: protos.google.cloud.language.v1beta2.IAnalyzeSyntaxRequest, callback: Callback<protos.google.cloud.language.v1beta2.IAnalyzeSyntaxResponse, protos.google.cloud.language.v1beta2.IAnalyzeSyntaxRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IAnalyzeSyntaxRequest](https://docs.cloud.google.com/nodejs/docs/reference/language/latest/language/protos.google.cloud.language.v1beta2.ianalyzesyntaxrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.language.v1beta2.IAnalyzeSyntaxResponse](https://docs.cloud.google.com/nodejs/docs/reference/language/latest/language/protos.google.cloud.language.v1beta2.ianalyzesyntaxresponse), [protos.google.cloud.language.v1beta2.IAnalyzeSyntaxRequest](https://docs.cloud.google.com/nodejs/docs/reference/language/latest/language/protos.google.cloud.language.v1beta2.ianalyzesyntaxrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### annotateText(request, options)
    
    
    annotateText(request?: protos.google.cloud.language.v1beta2.IAnnotateTextRequest, options?: CallOptions): Promise<[
            protos.google.cloud.language.v1beta2.IAnnotateTextResponse,
            protos.google.cloud.language.v1beta2.IAnnotateTextRequest | undefined,
            {} | undefined
        ]>;

A convenience method that provides all syntax, sentiment, entity, and classification features in one call.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IAnnotateTextRequest](https://docs.cloud.google.com/nodejs/docs/reference/language/latest/language/protos.google.cloud.language.v1beta2.iannotatetextrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.language.v1beta2.IAnnotateTextResponse](https://docs.cloud.google.com/nodejs/docs/reference/language/latest/language/protos.google.cloud.language.v1beta2.iannotatetextresponse), [protos.google.cloud.language.v1beta2.IAnnotateTextRequest](https://docs.cloud.google.com/nodejs/docs/reference/language/latest/language/protos.google.cloud.language.v1beta2.iannotatetextrequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [AnnotateTextResponse](https://docs.cloud.google.com/nodejs/docs/reference/language/latest/language/protos.google.cloud.language.v1beta2.annotatetextresponse). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Input document.
       */
      // const document = {}
      /**
       *  Required. The enabled features.
       */
      // const features = {}
      /**
       *  The encoding type used by the API to calculate offsets.
       */
      // const encodingType = {}
    
      // Imports the Language library
      const {LanguageServiceClient} = require('[@google-cloud/language](https://docs.cloud.google.com/nodejs/docs/reference/language/latest/overview.html)').v1beta2;
    
      // Instantiates a client
      const languageClient = new [LanguageServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/language/latest/overview.html)();
    
      async function callAnnotateText() {
        // Construct request
        const request = {
          document,
          features,
        };
    
        // Run request
        const response = await languageClient.annotateText(request);
        console.log(response);
      }
    
      callAnnotateText();
    
    

### annotateText(request, options, callback)
    
    
    annotateText(request: protos.google.cloud.language.v1beta2.IAnnotateTextRequest, options: CallOptions, callback: Callback<protos.google.cloud.language.v1beta2.IAnnotateTextResponse, protos.google.cloud.language.v1beta2.IAnnotateTextRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IAnnotateTextRequest](https://docs.cloud.google.com/nodejs/docs/reference/language/latest/language/protos.google.cloud.language.v1beta2.iannotatetextrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.language.v1beta2.IAnnotateTextResponse](https://docs.cloud.google.com/nodejs/docs/reference/language/latest/language/protos.google.cloud.language.v1beta2.iannotatetextresponse), [protos.google.cloud.language.v1beta2.IAnnotateTextRequest](https://docs.cloud.google.com/nodejs/docs/reference/language/latest/language/protos.google.cloud.language.v1beta2.iannotatetextrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### annotateText(request, callback)
    
    
    annotateText(request: protos.google.cloud.language.v1beta2.IAnnotateTextRequest, callback: Callback<protos.google.cloud.language.v1beta2.IAnnotateTextResponse, protos.google.cloud.language.v1beta2.IAnnotateTextRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IAnnotateTextRequest](https://docs.cloud.google.com/nodejs/docs/reference/language/latest/language/protos.google.cloud.language.v1beta2.iannotatetextrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.language.v1beta2.IAnnotateTextResponse](https://docs.cloud.google.com/nodejs/docs/reference/language/latest/language/protos.google.cloud.language.v1beta2.iannotatetextresponse), [protos.google.cloud.language.v1beta2.IAnnotateTextRequest](https://docs.cloud.google.com/nodejs/docs/reference/language/latest/language/protos.google.cloud.language.v1beta2.iannotatetextrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### classifyText(request, options)
    
    
    classifyText(request?: protos.google.cloud.language.v1beta2.IClassifyTextRequest, options?: CallOptions): Promise<[
            protos.google.cloud.language.v1beta2.IClassifyTextResponse,
            protos.google.cloud.language.v1beta2.IClassifyTextRequest | undefined,
            {} | undefined
        ]>;

Classifies a document into categories.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IClassifyTextRequest](https://docs.cloud.google.com/nodejs/docs/reference/language/latest/language/protos.google.cloud.language.v1beta2.iclassifytextrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.language.v1beta2.IClassifyTextResponse](https://docs.cloud.google.com/nodejs/docs/reference/language/latest/language/protos.google.cloud.language.v1beta2.iclassifytextresponse), [protos.google.cloud.language.v1beta2.IClassifyTextRequest](https://docs.cloud.google.com/nodejs/docs/reference/language/latest/language/protos.google.cloud.language.v1beta2.iclassifytextrequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [ClassifyTextResponse](https://docs.cloud.google.com/nodejs/docs/reference/language/latest/language/protos.google.cloud.language.v1beta2.classifytextresponse). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Input document.
       */
      // const document = {}
      /**
       *  Model options to use for classification. Defaults to v1 options if not
       *  specified.
       */
      // const classificationModelOptions = {}
    
      // Imports the Language library
      const {LanguageServiceClient} = require('[@google-cloud/language](https://docs.cloud.google.com/nodejs/docs/reference/language/latest/overview.html)').v1beta2;
    
      // Instantiates a client
      const languageClient = new [LanguageServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/language/latest/overview.html)();
    
      async function callClassifyText() {
        // Construct request
        const request = {
          document,
        };
    
        // Run request
        const response = await languageClient.classifyText(request);
        console.log(response);
      }
    
      callClassifyText();
    
    

### classifyText(request, options, callback)
    
    
    classifyText(request: protos.google.cloud.language.v1beta2.IClassifyTextRequest, options: CallOptions, callback: Callback<protos.google.cloud.language.v1beta2.IClassifyTextResponse, protos.google.cloud.language.v1beta2.IClassifyTextRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IClassifyTextRequest](https://docs.cloud.google.com/nodejs/docs/reference/language/latest/language/protos.google.cloud.language.v1beta2.iclassifytextrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.language.v1beta2.IClassifyTextResponse](https://docs.cloud.google.com/nodejs/docs/reference/language/latest/language/protos.google.cloud.language.v1beta2.iclassifytextresponse), [protos.google.cloud.language.v1beta2.IClassifyTextRequest](https://docs.cloud.google.com/nodejs/docs/reference/language/latest/language/protos.google.cloud.language.v1beta2.iclassifytextrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### classifyText(request, callback)
    
    
    classifyText(request: protos.google.cloud.language.v1beta2.IClassifyTextRequest, callback: Callback<protos.google.cloud.language.v1beta2.IClassifyTextResponse, protos.google.cloud.language.v1beta2.IClassifyTextRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IClassifyTextRequest](https://docs.cloud.google.com/nodejs/docs/reference/language/latest/language/protos.google.cloud.language.v1beta2.iclassifytextrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.language.v1beta2.IClassifyTextResponse](https://docs.cloud.google.com/nodejs/docs/reference/language/latest/language/protos.google.cloud.language.v1beta2.iclassifytextresponse), [protos.google.cloud.language.v1beta2.IClassifyTextRequest](https://docs.cloud.google.com/nodejs/docs/reference/language/latest/language/protos.google.cloud.language.v1beta2.iclassifytextrequest) | null | undefined, {} | null | undefined>`   
  
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
  
### moderateText(request, options)
    
    
    moderateText(request?: protos.google.cloud.language.v1beta2.IModerateTextRequest, options?: CallOptions): Promise<[
            protos.google.cloud.language.v1beta2.IModerateTextResponse,
            protos.google.cloud.language.v1beta2.IModerateTextRequest | undefined,
            {} | undefined
        ]>;

Moderates a document for harmful and sensitive categories.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IModerateTextRequest](https://docs.cloud.google.com/nodejs/docs/reference/language/latest/language/protos.google.cloud.language.v1beta2.imoderatetextrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.language.v1beta2.IModerateTextResponse](https://docs.cloud.google.com/nodejs/docs/reference/language/latest/language/protos.google.cloud.language.v1beta2.imoderatetextresponse), [protos.google.cloud.language.v1beta2.IModerateTextRequest](https://docs.cloud.google.com/nodejs/docs/reference/language/latest/language/protos.google.cloud.language.v1beta2.imoderatetextrequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [ModerateTextResponse](https://docs.cloud.google.com/nodejs/docs/reference/language/latest/language/protos.google.cloud.language.v1beta2.moderatetextresponse). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Input document.
       */
      // const document = {}
    
      // Imports the Language library
      const {LanguageServiceClient} = require('[@google-cloud/language](https://docs.cloud.google.com/nodejs/docs/reference/language/latest/overview.html)').v1beta2;
    
      // Instantiates a client
      const languageClient = new [LanguageServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/language/latest/overview.html)();
    
      async function callModerateText() {
        // Construct request
        const request = {
          document,
        };
    
        // Run request
        const response = await languageClient.moderateText(request);
        console.log(response);
      }
    
      callModerateText();
    
    

### moderateText(request, options, callback)
    
    
    moderateText(request: protos.google.cloud.language.v1beta2.IModerateTextRequest, options: CallOptions, callback: Callback<protos.google.cloud.language.v1beta2.IModerateTextResponse, protos.google.cloud.language.v1beta2.IModerateTextRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IModerateTextRequest](https://docs.cloud.google.com/nodejs/docs/reference/language/latest/language/protos.google.cloud.language.v1beta2.imoderatetextrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.language.v1beta2.IModerateTextResponse](https://docs.cloud.google.com/nodejs/docs/reference/language/latest/language/protos.google.cloud.language.v1beta2.imoderatetextresponse), [protos.google.cloud.language.v1beta2.IModerateTextRequest](https://docs.cloud.google.com/nodejs/docs/reference/language/latest/language/protos.google.cloud.language.v1beta2.imoderatetextrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### moderateText(request, callback)
    
    
    moderateText(request: protos.google.cloud.language.v1beta2.IModerateTextRequest, callback: Callback<protos.google.cloud.language.v1beta2.IModerateTextResponse, protos.google.cloud.language.v1beta2.IModerateTextRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IModerateTextRequest](https://docs.cloud.google.com/nodejs/docs/reference/language/latest/language/protos.google.cloud.language.v1beta2.imoderatetextrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.language.v1beta2.IModerateTextResponse](https://docs.cloud.google.com/nodejs/docs/reference/language/latest/language/protos.google.cloud.language.v1beta2.imoderatetextresponse), [protos.google.cloud.language.v1beta2.IModerateTextRequest](https://docs.cloud.google.com/nodejs/docs/reference/language/latest/language/protos.google.cloud.language.v1beta2.imoderatetextrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
