---
url: https://docs.cloud.google.com/nodejs/docs/reference/gcs-resumable-upload/latest/gcs-resumable-upload/upload/
title: Class Upload (6.0.0) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:54:47.452257+00:00
---

# Class Upload (6.0.0)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/gcs-resumable-upload/latest/gcs-resumable-upload/upload/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class Upload (6.0.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 6.0.0 (latest) ](https://docs.cloud.google.com/nodejs/docs/reference/gcs-resumable-upload/latest/gcs-resumable-upload/upload/)
  * [ 5.0.1 ](https://docs.cloud.google.com/nodejs/docs/reference/gcs-resumable-upload/5.0.1/gcs-resumable-upload/upload/)
  * [ 4.0.2 ](https://docs.cloud.google.com/nodejs/docs/reference/gcs-resumable-upload/4.0.2/gcs-resumable-upload/upload/)
  * [ 3.6.0 ](https://docs.cloud.google.com/nodejs/docs/reference/gcs-resumable-upload/3.6.0/gcs-resumable-upload/upload/)
  * [ 3.5.1 ](https://docs.cloud.google.com/nodejs/docs/reference/gcs-resumable-upload/3.5.1/gcs-resumable-upload/upload/)
  * [ 3.4.0 ](https://docs.cloud.google.com/nodejs/docs/reference/gcs-resumable-upload/3.4.0/gcs-resumable-upload/upload/)
  * [ 3.3.1 ](https://docs.cloud.google.com/nodejs/docs/reference/gcs-resumable-upload/3.3.1/gcs-resumable-upload/upload/)
  * [ 3.2.1 ](https://docs.cloud.google.com/nodejs/docs/reference/gcs-resumable-upload/3.2.1/gcs-resumable-upload/upload/)



## Inheritance

Pumpify > Upload

## Package

[gcs-resumable-upload](https://docs.cloud.google.com/nodejs/docs/reference/gcs-resumable-upload/latest/overview.html)

## Constructors 

### (constructor)(cfg)
    
    
    constructor(cfg: UploadConfig);

Constructs a new instance of the `Upload` class

**Parameter**  
---  
**Name** | **Description**  
`cfg` |  `[UploadConfig](https://docs.cloud.google.com/nodejs/docs/reference/gcs-resumable-upload/latest/gcs-resumable-upload/uploadconfig)`   
  
  
## Properties 

### apiEndpoint
    
    
    apiEndpoint: string;

### authClient
    
    
    authClient: {
            request: <T>(opts: GaxiosOptions) => Promise<GaxiosResponse<T>> | GaxiosPromise<T>;
        };

### authConfig
    
    
    authConfig?: {
            scopes?: string[];
        };

### baseURI
    
    
    baseURI: string;

### bucket
    
    
    bucket: string;

### cacheKey
    
    
    cacheKey: string;

### chunkSize
    
    
    chunkSize?: number;

### configStore
    
    
    configStore: ConfigStore;

### contentLength
    
    
    contentLength: number | '*';

### customRequestOptions
    
    
    customRequestOptions: GaxiosOptions;

### encryption
    
    
    encryption?: Encryption;

### file
    
    
    file: string;

### generation
    
    
    generation?: number;

### key
    
    
    key?: string | Buffer;

### kmsKeyName
    
    
    kmsKeyName?: string;

### maxRetryDelay
    
    
    maxRetryDelay: number;

### maxRetryTotalTimeout
    
    
    maxRetryTotalTimeout: number;

### metadata
    
    
    metadata: ConfigMetadata;

### numBytesWritten
    
    
    numBytesWritten: number;

### numRetries
    
    
    numRetries: number;

### offset
    
    
    offset?: number;

### origin
    
    
    origin?: string;

### params
    
    
    params: QueryParameters;

### predefinedAcl
    
    
    predefinedAcl?: PredefinedAcl;

### private
    
    
    private?: boolean;

### public
    
    
    public?: boolean;

### retryableErrorFn
    
    
    retryableErrorFn?: (err: ApiError) => boolean;

### retryDelayMultiplier
    
    
    retryDelayMultiplier: number;

### retryLimit
    
    
    retryLimit: number;

### timeOfFirstRequest
    
    
    timeOfFirstRequest: number;

### uri
    
    
    uri?: string;

### uriProvidedManually
    
    
    uriProvidedManually: boolean;

### userProject
    
    
    userProject?: string;

## Methods 

### createURI()
    
    
    createURI(): Promise<string>;

**Returns**  
---  
**Type** | **Description**  
`Promise<string>` |   
  
### createURI(callback)
    
    
    createURI(callback: CreateUriCallback): void;

**Parameter**  
---  
**Name** | **Description**  
`callback` |  `[CreateUriCallback](https://docs.cloud.google.com/nodejs/docs/reference/gcs-resumable-upload/latest/overview.html)`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createURIAsync()
    
    
    protected createURIAsync(): Promise<string>;

**Returns**  
---  
**Type** | **Description**  
`Promise<string>` |   
  
### deleteConfig()
    
    
    deleteConfig(): void;

**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### isServerErrorResponse(status)
    
    
    isServerErrorResponse(status: number): boolean;

Check if a given status code is 5xx

**Parameter**  
---  
**Name** | **Description**  
`status` |  `number`   
The status code to check  
**Returns**  
---  
**Type** | **Description**  
`boolean` | if the status is 5xx  
  
### isSuccessfulResponse(status)
    
    
    isSuccessfulResponse(status: number): boolean;

Check if a given status code is 2xx

**Parameter**  
---  
**Name** | **Description**  
`status` |  `number`   
The status code to check  
**Returns**  
---  
**Type** | **Description**  
`boolean` | if the status is 2xx  
  
### startUploading()
    
    
    startUploading(): Promise<void>;

**Returns**  
---  
**Type** | **Description**  
`Promise<void>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
