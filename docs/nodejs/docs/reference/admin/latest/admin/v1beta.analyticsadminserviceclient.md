---
url: https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/v1beta.analyticsadminserviceclient
title: Class v1beta.AnalyticsAdminServiceClient (10.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:55:00.437877+00:00
---

# Class v1beta.AnalyticsAdminServiceClient (10.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/v1beta.analyticsadminserviceclient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class v1beta.AnalyticsAdminServiceClient (10.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

10.1.1 (latest)  10.1.0  9.2.0  7.6.0  7.3.0  4.6.0  4.5.1  4.4.0 

Service Interface for the Google Analytics Admin API. v1beta

## Package

[@google-analytics/admin](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)

## Constructors 

### (constructor)(opts, gaxInstance)
    
    
    constructor(opts?: ClientOptions, gaxInstance?: typeof gax | typeof gax.fallback);

Construct an instance of AnalyticsAdminServiceClient.

**Parameters**  
---  
**Name** | **Description**  
`opts` |  `ClientOptions`   
  
`gaxInstance` |  `typeof gax | typeof fallback`   
: loaded instance of `google-gax`. Useful if you need to avoid loading the default gRPC version and want to use the fallback HTTP implementation. Load only fallback version and pass it to the constructor: ``` const gax = require('google-gax/build/src/fallback'); // avoids loading google-gax with gRPC const client = new AnalyticsAdminServiceClient({fallback: true}, gax); ```  
  
## Properties 

### analyticsAdminServiceStub
    
    
    analyticsAdminServiceStub?: Promise<{
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

### accountPath(account)
    
    
    accountPath(account: string): string;

Return a fully-qualified account resource name string.

**Parameter**  
---  
**Name** | **Description**  
`account` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### accountSummaryPath(accountSummary)
    
    
    accountSummaryPath(accountSummary: string): string;

Return a fully-qualified accountSummary resource name string.

**Parameter**  
---  
**Name** | **Description**  
`accountSummary` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### acknowledgeUserDataCollection(request, options)
    
    
    acknowledgeUserDataCollection(request?: protos.google.analytics.admin.v1beta.IAcknowledgeUserDataCollectionRequest, options?: CallOptions): Promise<[
            protos.google.analytics.admin.v1beta.IAcknowledgeUserDataCollectionResponse,
            (protos.google.analytics.admin.v1beta.IAcknowledgeUserDataCollectionRequest | undefined),
            {} | undefined
        ]>;

Acknowledges the terms of user data collection for the specified property.

This acknowledgement must be completed (either in the Google Analytics UI or through this API) before MeasurementProtocolSecret resources may be created.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IAcknowledgeUserDataCollectionRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.iacknowledgeuserdatacollectionrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.analytics.admin.v1beta.IAcknowledgeUserDataCollectionResponse](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.iacknowledgeuserdatacollectionresponse), ([protos.google.analytics.admin.v1beta.IAcknowledgeUserDataCollectionRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.iacknowledgeuserdatacollectionrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [AcknowledgeUserDataCollectionResponse](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.acknowledgeuserdatacollectionresponse). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The property for which to acknowledge user data collection.
       */
      // const property = 'abc123'
      /**
       *  Required. An acknowledgement that the caller of this method understands the
       *  terms of user data collection.
       *  This field must contain the exact value:
       *  "I acknowledge that I have the necessary privacy disclosures and rights
       *  from my end users for the collection and processing of their data,
       *  including the association of such data with the visitation information
       *  Google Analytics collects from my site and/or app property."
       */
      // const acknowledgement = 'abc123'
    
      // Imports the Admin library
      const {AnalyticsAdminServiceClient} = require('[@google-analytics/admin](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const adminClient = new [AnalyticsAdminServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)();
    
      async function callAcknowledgeUserDataCollection() {
        // Construct request
        const request = {
          property,
          acknowledgement,
        };
    
        // Run request
        const response = await adminClient.acknowledgeUserDataCollection(request);
        console.log(response);
      }
    
      callAcknowledgeUserDataCollection();
    
    

### acknowledgeUserDataCollection(request, options, callback)
    
    
    acknowledgeUserDataCollection(request: protos.google.analytics.admin.v1beta.IAcknowledgeUserDataCollectionRequest, options: CallOptions, callback: Callback<protos.google.analytics.admin.v1beta.IAcknowledgeUserDataCollectionResponse, protos.google.analytics.admin.v1beta.IAcknowledgeUserDataCollectionRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IAcknowledgeUserDataCollectionRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.iacknowledgeuserdatacollectionrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.analytics.admin.v1beta.IAcknowledgeUserDataCollectionResponse](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.iacknowledgeuserdatacollectionresponse), [protos.google.analytics.admin.v1beta.IAcknowledgeUserDataCollectionRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.iacknowledgeuserdatacollectionrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### acknowledgeUserDataCollection(request, callback)
    
    
    acknowledgeUserDataCollection(request: protos.google.analytics.admin.v1beta.IAcknowledgeUserDataCollectionRequest, callback: Callback<protos.google.analytics.admin.v1beta.IAcknowledgeUserDataCollectionResponse, protos.google.analytics.admin.v1beta.IAcknowledgeUserDataCollectionRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IAcknowledgeUserDataCollectionRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.iacknowledgeuserdatacollectionrequest)`   
  
`callback` |  `Callback<[protos.google.analytics.admin.v1beta.IAcknowledgeUserDataCollectionResponse](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.iacknowledgeuserdatacollectionresponse), [protos.google.analytics.admin.v1beta.IAcknowledgeUserDataCollectionRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.iacknowledgeuserdatacollectionrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### archiveCustomDimension(request, options)
    
    
    archiveCustomDimension(request?: protos.google.analytics.admin.v1beta.IArchiveCustomDimensionRequest, options?: CallOptions): Promise<[
            protos.google.protobuf.IEmpty,
            (protos.google.analytics.admin.v1beta.IArchiveCustomDimensionRequest | undefined),
            {} | undefined
        ]>;

Archives a CustomDimension on a property.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IArchiveCustomDimensionRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.iarchivecustomdimensionrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.protobuf.iempty), ([protos.google.analytics.admin.v1beta.IArchiveCustomDimensionRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.iarchivecustomdimensionrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [Empty](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.protobuf.empty). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The name of the CustomDimension to archive.
       *  Example format: properties/1234/customDimensions/5678
       */
      // const name = 'abc123'
    
      // Imports the Admin library
      const {AnalyticsAdminServiceClient} = require('[@google-analytics/admin](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const adminClient = new [AnalyticsAdminServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)();
    
      async function callArchiveCustomDimension() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await adminClient.archiveCustomDimension(request);
        console.log(response);
      }
    
      callArchiveCustomDimension();
    
    

### archiveCustomDimension(request, options, callback)
    
    
    archiveCustomDimension(request: protos.google.analytics.admin.v1beta.IArchiveCustomDimensionRequest, options: CallOptions, callback: Callback<protos.google.protobuf.IEmpty, protos.google.analytics.admin.v1beta.IArchiveCustomDimensionRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IArchiveCustomDimensionRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.iarchivecustomdimensionrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.protobuf.iempty), [protos.google.analytics.admin.v1beta.IArchiveCustomDimensionRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.iarchivecustomdimensionrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### archiveCustomDimension(request, callback)
    
    
    archiveCustomDimension(request: protos.google.analytics.admin.v1beta.IArchiveCustomDimensionRequest, callback: Callback<protos.google.protobuf.IEmpty, protos.google.analytics.admin.v1beta.IArchiveCustomDimensionRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IArchiveCustomDimensionRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.iarchivecustomdimensionrequest)`   
  
`callback` |  `Callback<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.protobuf.iempty), [protos.google.analytics.admin.v1beta.IArchiveCustomDimensionRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.iarchivecustomdimensionrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### archiveCustomMetric(request, options)
    
    
    archiveCustomMetric(request?: protos.google.analytics.admin.v1beta.IArchiveCustomMetricRequest, options?: CallOptions): Promise<[
            protos.google.protobuf.IEmpty,
            (protos.google.analytics.admin.v1beta.IArchiveCustomMetricRequest | undefined),
            {} | undefined
        ]>;

Archives a CustomMetric on a property.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IArchiveCustomMetricRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.iarchivecustommetricrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.protobuf.iempty), ([protos.google.analytics.admin.v1beta.IArchiveCustomMetricRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.iarchivecustommetricrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [Empty](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.protobuf.empty). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The name of the CustomMetric to archive.
       *  Example format: properties/1234/customMetrics/5678
       */
      // const name = 'abc123'
    
      // Imports the Admin library
      const {AnalyticsAdminServiceClient} = require('[@google-analytics/admin](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const adminClient = new [AnalyticsAdminServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)();
    
      async function callArchiveCustomMetric() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await adminClient.archiveCustomMetric(request);
        console.log(response);
      }
    
      callArchiveCustomMetric();
    
    

### archiveCustomMetric(request, options, callback)
    
    
    archiveCustomMetric(request: protos.google.analytics.admin.v1beta.IArchiveCustomMetricRequest, options: CallOptions, callback: Callback<protos.google.protobuf.IEmpty, protos.google.analytics.admin.v1beta.IArchiveCustomMetricRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IArchiveCustomMetricRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.iarchivecustommetricrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.protobuf.iempty), [protos.google.analytics.admin.v1beta.IArchiveCustomMetricRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.iarchivecustommetricrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### archiveCustomMetric(request, callback)
    
    
    archiveCustomMetric(request: protos.google.analytics.admin.v1beta.IArchiveCustomMetricRequest, callback: Callback<protos.google.protobuf.IEmpty, protos.google.analytics.admin.v1beta.IArchiveCustomMetricRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IArchiveCustomMetricRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.iarchivecustommetricrequest)`   
  
`callback` |  `Callback<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.protobuf.iempty), [protos.google.analytics.admin.v1beta.IArchiveCustomMetricRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.iarchivecustommetricrequest) | null | undefined, {} | null | undefined>`   
  
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
  
### conversionEventPath(property, conversionEvent)
    
    
    conversionEventPath(property: string, conversionEvent: string): string;

Return a fully-qualified conversionEvent resource name string.

**Parameters**  
---  
**Name** | **Description**  
`property` |  `string`   
  
`conversionEvent` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### createConversionEvent(request, options)
    
    
    createConversionEvent(request?: protos.google.analytics.admin.v1beta.ICreateConversionEventRequest, options?: CallOptions): Promise<[
            protos.google.analytics.admin.v1beta.IConversionEvent,
            (protos.google.analytics.admin.v1beta.ICreateConversionEventRequest | undefined),
            {} | undefined
        ]>;

Deprecated: Use `CreateKeyEvent` instead. Creates a conversion event with the specified attributes.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateConversionEventRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.icreateconversioneventrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.analytics.admin.v1beta.IConversionEvent](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.iconversionevent), ([protos.google.analytics.admin.v1beta.ICreateConversionEventRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.icreateconversioneventrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The conversion event to create.
       */
      // const conversionEvent = {}
      /**
       *  Required. The resource name of the parent property where this conversion
       *  event will be created. Format: properties/123
       */
      // const parent = 'abc123'
    
      // Imports the Admin library
      const {AnalyticsAdminServiceClient} = require('[@google-analytics/admin](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const adminClient = new [AnalyticsAdminServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)();
    
      async function callCreateConversionEvent() {
        // Construct request
        const request = {
          conversionEvent,
          parent,
        };
    
        // Run request
        const response = await adminClient.createConversionEvent(request);
        console.log(response);
      }
    
      callCreateConversionEvent();
    
    

### createConversionEvent(request, options, callback)
    
    
    createConversionEvent(request: protos.google.analytics.admin.v1beta.ICreateConversionEventRequest, options: CallOptions, callback: Callback<protos.google.analytics.admin.v1beta.IConversionEvent, protos.google.analytics.admin.v1beta.ICreateConversionEventRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateConversionEventRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.icreateconversioneventrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.analytics.admin.v1beta.IConversionEvent](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.iconversionevent), [protos.google.analytics.admin.v1beta.ICreateConversionEventRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.icreateconversioneventrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createConversionEvent(request, callback)
    
    
    createConversionEvent(request: protos.google.analytics.admin.v1beta.ICreateConversionEventRequest, callback: Callback<protos.google.analytics.admin.v1beta.IConversionEvent, protos.google.analytics.admin.v1beta.ICreateConversionEventRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateConversionEventRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.icreateconversioneventrequest)`   
  
`callback` |  `Callback<[protos.google.analytics.admin.v1beta.IConversionEvent](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.iconversionevent), [protos.google.analytics.admin.v1beta.ICreateConversionEventRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.icreateconversioneventrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createCustomDimension(request, options)
    
    
    createCustomDimension(request?: protos.google.analytics.admin.v1beta.ICreateCustomDimensionRequest, options?: CallOptions): Promise<[
            protos.google.analytics.admin.v1beta.ICustomDimension,
            (protos.google.analytics.admin.v1beta.ICreateCustomDimensionRequest | undefined),
            {} | undefined
        ]>;

Creates a CustomDimension.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateCustomDimensionRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.icreatecustomdimensionrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.analytics.admin.v1beta.ICustomDimension](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.icustomdimension), ([protos.google.analytics.admin.v1beta.ICreateCustomDimensionRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.icreatecustomdimensionrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Example format: properties/1234
       */
      // const parent = 'abc123'
      /**
       *  Required. The CustomDimension to create.
       */
      // const customDimension = {}
    
      // Imports the Admin library
      const {AnalyticsAdminServiceClient} = require('[@google-analytics/admin](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const adminClient = new [AnalyticsAdminServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)();
    
      async function callCreateCustomDimension() {
        // Construct request
        const request = {
          parent,
          customDimension,
        };
    
        // Run request
        const response = await adminClient.createCustomDimension(request);
        console.log(response);
      }
    
      callCreateCustomDimension();
    
    

### createCustomDimension(request, options, callback)
    
    
    createCustomDimension(request: protos.google.analytics.admin.v1beta.ICreateCustomDimensionRequest, options: CallOptions, callback: Callback<protos.google.analytics.admin.v1beta.ICustomDimension, protos.google.analytics.admin.v1beta.ICreateCustomDimensionRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateCustomDimensionRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.icreatecustomdimensionrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.analytics.admin.v1beta.ICustomDimension](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.icustomdimension), [protos.google.analytics.admin.v1beta.ICreateCustomDimensionRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.icreatecustomdimensionrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createCustomDimension(request, callback)
    
    
    createCustomDimension(request: protos.google.analytics.admin.v1beta.ICreateCustomDimensionRequest, callback: Callback<protos.google.analytics.admin.v1beta.ICustomDimension, protos.google.analytics.admin.v1beta.ICreateCustomDimensionRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateCustomDimensionRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.icreatecustomdimensionrequest)`   
  
`callback` |  `Callback<[protos.google.analytics.admin.v1beta.ICustomDimension](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.icustomdimension), [protos.google.analytics.admin.v1beta.ICreateCustomDimensionRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.icreatecustomdimensionrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createCustomMetric(request, options)
    
    
    createCustomMetric(request?: protos.google.analytics.admin.v1beta.ICreateCustomMetricRequest, options?: CallOptions): Promise<[
            protos.google.analytics.admin.v1beta.ICustomMetric,
            (protos.google.analytics.admin.v1beta.ICreateCustomMetricRequest | undefined),
            {} | undefined
        ]>;

Creates a CustomMetric.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateCustomMetricRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.icreatecustommetricrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.analytics.admin.v1beta.ICustomMetric](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.icustommetric), ([protos.google.analytics.admin.v1beta.ICreateCustomMetricRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.icreatecustommetricrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Example format: properties/1234
       */
      // const parent = 'abc123'
      /**
       *  Required. The CustomMetric to create.
       */
      // const customMetric = {}
    
      // Imports the Admin library
      const {AnalyticsAdminServiceClient} = require('[@google-analytics/admin](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const adminClient = new [AnalyticsAdminServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)();
    
      async function callCreateCustomMetric() {
        // Construct request
        const request = {
          parent,
          customMetric,
        };
    
        // Run request
        const response = await adminClient.createCustomMetric(request);
        console.log(response);
      }
    
      callCreateCustomMetric();
    
    

### createCustomMetric(request, options, callback)
    
    
    createCustomMetric(request: protos.google.analytics.admin.v1beta.ICreateCustomMetricRequest, options: CallOptions, callback: Callback<protos.google.analytics.admin.v1beta.ICustomMetric, protos.google.analytics.admin.v1beta.ICreateCustomMetricRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateCustomMetricRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.icreatecustommetricrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.analytics.admin.v1beta.ICustomMetric](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.icustommetric), [protos.google.analytics.admin.v1beta.ICreateCustomMetricRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.icreatecustommetricrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createCustomMetric(request, callback)
    
    
    createCustomMetric(request: protos.google.analytics.admin.v1beta.ICreateCustomMetricRequest, callback: Callback<protos.google.analytics.admin.v1beta.ICustomMetric, protos.google.analytics.admin.v1beta.ICreateCustomMetricRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateCustomMetricRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.icreatecustommetricrequest)`   
  
`callback` |  `Callback<[protos.google.analytics.admin.v1beta.ICustomMetric](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.icustommetric), [protos.google.analytics.admin.v1beta.ICreateCustomMetricRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.icreatecustommetricrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createDataStream(request, options)
    
    
    createDataStream(request?: protos.google.analytics.admin.v1beta.ICreateDataStreamRequest, options?: CallOptions): Promise<[
            protos.google.analytics.admin.v1beta.IDataStream,
            protos.google.analytics.admin.v1beta.ICreateDataStreamRequest | undefined,
            {} | undefined
        ]>;

Creates a DataStream.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateDataStreamRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.icreatedatastreamrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.analytics.admin.v1beta.IDataStream](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.idatastream), [protos.google.analytics.admin.v1beta.ICreateDataStreamRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.icreatedatastreamrequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Example format: properties/1234
       */
      // const parent = 'abc123'
      /**
       *  Required. The DataStream to create.
       */
      // const dataStream = {}
    
      // Imports the Admin library
      const {AnalyticsAdminServiceClient} = require('[@google-analytics/admin](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const adminClient = new [AnalyticsAdminServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)();
    
      async function callCreateDataStream() {
        // Construct request
        const request = {
          parent,
          dataStream,
        };
    
        // Run request
        const response = await adminClient.createDataStream(request);
        console.log(response);
      }
    
      callCreateDataStream();
    
    

### createDataStream(request, options, callback)
    
    
    createDataStream(request: protos.google.analytics.admin.v1beta.ICreateDataStreamRequest, options: CallOptions, callback: Callback<protos.google.analytics.admin.v1beta.IDataStream, protos.google.analytics.admin.v1beta.ICreateDataStreamRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateDataStreamRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.icreatedatastreamrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.analytics.admin.v1beta.IDataStream](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.idatastream), [protos.google.analytics.admin.v1beta.ICreateDataStreamRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.icreatedatastreamrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createDataStream(request, callback)
    
    
    createDataStream(request: protos.google.analytics.admin.v1beta.ICreateDataStreamRequest, callback: Callback<protos.google.analytics.admin.v1beta.IDataStream, protos.google.analytics.admin.v1beta.ICreateDataStreamRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateDataStreamRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.icreatedatastreamrequest)`   
  
`callback` |  `Callback<[protos.google.analytics.admin.v1beta.IDataStream](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.idatastream), [protos.google.analytics.admin.v1beta.ICreateDataStreamRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.icreatedatastreamrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createFirebaseLink(request, options)
    
    
    createFirebaseLink(request?: protos.google.analytics.admin.v1beta.ICreateFirebaseLinkRequest, options?: CallOptions): Promise<[
            protos.google.analytics.admin.v1beta.IFirebaseLink,
            (protos.google.analytics.admin.v1beta.ICreateFirebaseLinkRequest | undefined),
            {} | undefined
        ]>;

Creates a FirebaseLink.

Properties can have at most one FirebaseLink.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateFirebaseLinkRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.icreatefirebaselinkrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.analytics.admin.v1beta.IFirebaseLink](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ifirebaselink), ([protos.google.analytics.admin.v1beta.ICreateFirebaseLinkRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.icreatefirebaselinkrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [FirebaseLink](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.firebaselink). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Format: properties/{property_id}
       *  Example: `properties/1234`
       */
      // const parent = 'abc123'
      /**
       *  Required. The Firebase link to create.
       */
      // const firebaseLink = {}
    
      // Imports the Admin library
      const {AnalyticsAdminServiceClient} = require('[@google-analytics/admin](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const adminClient = new [AnalyticsAdminServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)();
    
      async function callCreateFirebaseLink() {
        // Construct request
        const request = {
          parent,
          firebaseLink,
        };
    
        // Run request
        const response = await adminClient.createFirebaseLink(request);
        console.log(response);
      }
    
      callCreateFirebaseLink();
    
    

### createFirebaseLink(request, options, callback)
    
    
    createFirebaseLink(request: protos.google.analytics.admin.v1beta.ICreateFirebaseLinkRequest, options: CallOptions, callback: Callback<protos.google.analytics.admin.v1beta.IFirebaseLink, protos.google.analytics.admin.v1beta.ICreateFirebaseLinkRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateFirebaseLinkRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.icreatefirebaselinkrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.analytics.admin.v1beta.IFirebaseLink](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ifirebaselink), [protos.google.analytics.admin.v1beta.ICreateFirebaseLinkRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.icreatefirebaselinkrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createFirebaseLink(request, callback)
    
    
    createFirebaseLink(request: protos.google.analytics.admin.v1beta.ICreateFirebaseLinkRequest, callback: Callback<protos.google.analytics.admin.v1beta.IFirebaseLink, protos.google.analytics.admin.v1beta.ICreateFirebaseLinkRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateFirebaseLinkRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.icreatefirebaselinkrequest)`   
  
`callback` |  `Callback<[protos.google.analytics.admin.v1beta.IFirebaseLink](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ifirebaselink), [protos.google.analytics.admin.v1beta.ICreateFirebaseLinkRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.icreatefirebaselinkrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createGoogleAdsLink(request, options)
    
    
    createGoogleAdsLink(request?: protos.google.analytics.admin.v1beta.ICreateGoogleAdsLinkRequest, options?: CallOptions): Promise<[
            protos.google.analytics.admin.v1beta.IGoogleAdsLink,
            (protos.google.analytics.admin.v1beta.ICreateGoogleAdsLinkRequest | undefined),
            {} | undefined
        ]>;

Creates a GoogleAdsLink.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateGoogleAdsLinkRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.icreategoogleadslinkrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.analytics.admin.v1beta.IGoogleAdsLink](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.igoogleadslink), ([protos.google.analytics.admin.v1beta.ICreateGoogleAdsLinkRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.icreategoogleadslinkrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [GoogleAdsLink](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.googleadslink). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Example format: properties/1234
       */
      // const parent = 'abc123'
      /**
       *  Required. The GoogleAdsLink to create.
       */
      // const googleAdsLink = {}
    
      // Imports the Admin library
      const {AnalyticsAdminServiceClient} = require('[@google-analytics/admin](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const adminClient = new [AnalyticsAdminServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)();
    
      async function callCreateGoogleAdsLink() {
        // Construct request
        const request = {
          parent,
          googleAdsLink,
        };
    
        // Run request
        const response = await adminClient.createGoogleAdsLink(request);
        console.log(response);
      }
    
      callCreateGoogleAdsLink();
    
    

### createGoogleAdsLink(request, options, callback)
    
    
    createGoogleAdsLink(request: protos.google.analytics.admin.v1beta.ICreateGoogleAdsLinkRequest, options: CallOptions, callback: Callback<protos.google.analytics.admin.v1beta.IGoogleAdsLink, protos.google.analytics.admin.v1beta.ICreateGoogleAdsLinkRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateGoogleAdsLinkRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.icreategoogleadslinkrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.analytics.admin.v1beta.IGoogleAdsLink](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.igoogleadslink), [protos.google.analytics.admin.v1beta.ICreateGoogleAdsLinkRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.icreategoogleadslinkrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createGoogleAdsLink(request, callback)
    
    
    createGoogleAdsLink(request: protos.google.analytics.admin.v1beta.ICreateGoogleAdsLinkRequest, callback: Callback<protos.google.analytics.admin.v1beta.IGoogleAdsLink, protos.google.analytics.admin.v1beta.ICreateGoogleAdsLinkRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateGoogleAdsLinkRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.icreategoogleadslinkrequest)`   
  
`callback` |  `Callback<[protos.google.analytics.admin.v1beta.IGoogleAdsLink](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.igoogleadslink), [protos.google.analytics.admin.v1beta.ICreateGoogleAdsLinkRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.icreategoogleadslinkrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createKeyEvent(request, options)
    
    
    createKeyEvent(request?: protos.google.analytics.admin.v1beta.ICreateKeyEventRequest, options?: CallOptions): Promise<[
            protos.google.analytics.admin.v1beta.IKeyEvent,
            protos.google.analytics.admin.v1beta.ICreateKeyEventRequest | undefined,
            {} | undefined
        ]>;

Creates a Key Event.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateKeyEventRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.icreatekeyeventrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.analytics.admin.v1beta.IKeyEvent](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ikeyevent), [protos.google.analytics.admin.v1beta.ICreateKeyEventRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.icreatekeyeventrequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The Key Event to create.
       */
      // const keyEvent = {}
      /**
       *  Required. The resource name of the parent property where this Key Event
       *  will be created. Format: properties/123
       */
      // const parent = 'abc123'
    
      // Imports the Admin library
      const {AnalyticsAdminServiceClient} = require('[@google-analytics/admin](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const adminClient = new [AnalyticsAdminServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)();
    
      async function callCreateKeyEvent() {
        // Construct request
        const request = {
          keyEvent,
          parent,
        };
    
        // Run request
        const response = await adminClient.createKeyEvent(request);
        console.log(response);
      }
    
      callCreateKeyEvent();
    
    

### createKeyEvent(request, options, callback)
    
    
    createKeyEvent(request: protos.google.analytics.admin.v1beta.ICreateKeyEventRequest, options: CallOptions, callback: Callback<protos.google.analytics.admin.v1beta.IKeyEvent, protos.google.analytics.admin.v1beta.ICreateKeyEventRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateKeyEventRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.icreatekeyeventrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.analytics.admin.v1beta.IKeyEvent](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ikeyevent), [protos.google.analytics.admin.v1beta.ICreateKeyEventRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.icreatekeyeventrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createKeyEvent(request, callback)
    
    
    createKeyEvent(request: protos.google.analytics.admin.v1beta.ICreateKeyEventRequest, callback: Callback<protos.google.analytics.admin.v1beta.IKeyEvent, protos.google.analytics.admin.v1beta.ICreateKeyEventRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateKeyEventRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.icreatekeyeventrequest)`   
  
`callback` |  `Callback<[protos.google.analytics.admin.v1beta.IKeyEvent](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ikeyevent), [protos.google.analytics.admin.v1beta.ICreateKeyEventRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.icreatekeyeventrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createMeasurementProtocolSecret(request, options)
    
    
    createMeasurementProtocolSecret(request?: protos.google.analytics.admin.v1beta.ICreateMeasurementProtocolSecretRequest, options?: CallOptions): Promise<[
            protos.google.analytics.admin.v1beta.IMeasurementProtocolSecret,
            (protos.google.analytics.admin.v1beta.ICreateMeasurementProtocolSecretRequest | undefined),
            {} | undefined
        ]>;

Creates a measurement protocol secret.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateMeasurementProtocolSecretRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.icreatemeasurementprotocolsecretrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.analytics.admin.v1beta.IMeasurementProtocolSecret](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.imeasurementprotocolsecret), ([protos.google.analytics.admin.v1beta.ICreateMeasurementProtocolSecretRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.icreatemeasurementprotocolsecretrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [MeasurementProtocolSecret](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.measurementprotocolsecret). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The parent resource where this secret will be created.
       *  Format: properties/{property}/dataStreams/{dataStream}
       */
      // const parent = 'abc123'
      /**
       *  Required. The measurement protocol secret to create.
       */
      // const measurementProtocolSecret = {}
    
      // Imports the Admin library
      const {AnalyticsAdminServiceClient} = require('[@google-analytics/admin](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const adminClient = new [AnalyticsAdminServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)();
    
      async function callCreateMeasurementProtocolSecret() {
        // Construct request
        const request = {
          parent,
          measurementProtocolSecret,
        };
    
        // Run request
        const response = await adminClient.createMeasurementProtocolSecret(request);
        console.log(response);
      }
    
      callCreateMeasurementProtocolSecret();
    
    

### createMeasurementProtocolSecret(request, options, callback)
    
    
    createMeasurementProtocolSecret(request: protos.google.analytics.admin.v1beta.ICreateMeasurementProtocolSecretRequest, options: CallOptions, callback: Callback<protos.google.analytics.admin.v1beta.IMeasurementProtocolSecret, protos.google.analytics.admin.v1beta.ICreateMeasurementProtocolSecretRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateMeasurementProtocolSecretRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.icreatemeasurementprotocolsecretrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.analytics.admin.v1beta.IMeasurementProtocolSecret](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.imeasurementprotocolsecret), [protos.google.analytics.admin.v1beta.ICreateMeasurementProtocolSecretRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.icreatemeasurementprotocolsecretrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createMeasurementProtocolSecret(request, callback)
    
    
    createMeasurementProtocolSecret(request: protos.google.analytics.admin.v1beta.ICreateMeasurementProtocolSecretRequest, callback: Callback<protos.google.analytics.admin.v1beta.IMeasurementProtocolSecret, protos.google.analytics.admin.v1beta.ICreateMeasurementProtocolSecretRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateMeasurementProtocolSecretRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.icreatemeasurementprotocolsecretrequest)`   
  
`callback` |  `Callback<[protos.google.analytics.admin.v1beta.IMeasurementProtocolSecret](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.imeasurementprotocolsecret), [protos.google.analytics.admin.v1beta.ICreateMeasurementProtocolSecretRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.icreatemeasurementprotocolsecretrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createProperty(request, options)
    
    
    createProperty(request?: protos.google.analytics.admin.v1beta.ICreatePropertyRequest, options?: CallOptions): Promise<[
            protos.google.analytics.admin.v1beta.IProperty,
            protos.google.analytics.admin.v1beta.ICreatePropertyRequest | undefined,
            {} | undefined
        ]>;

Creates a Google Analytics property with the specified location and attributes.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreatePropertyRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.icreatepropertyrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.analytics.admin.v1beta.IProperty](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.iproperty), [protos.google.analytics.admin.v1beta.ICreatePropertyRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.icreatepropertyrequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [Property](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.property). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The property to create.
       *  Note: the supplied property must specify its parent.
       */
      // const property = {}
    
      // Imports the Admin library
      const {AnalyticsAdminServiceClient} = require('[@google-analytics/admin](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const adminClient = new [AnalyticsAdminServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)();
    
      async function callCreateProperty() {
        // Construct request
        const request = {
          property,
        };
    
        // Run request
        const response = await adminClient.createProperty(request);
        console.log(response);
      }
    
      callCreateProperty();
    
    

### createProperty(request, options, callback)
    
    
    createProperty(request: protos.google.analytics.admin.v1beta.ICreatePropertyRequest, options: CallOptions, callback: Callback<protos.google.analytics.admin.v1beta.IProperty, protos.google.analytics.admin.v1beta.ICreatePropertyRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreatePropertyRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.icreatepropertyrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.analytics.admin.v1beta.IProperty](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.iproperty), [protos.google.analytics.admin.v1beta.ICreatePropertyRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.icreatepropertyrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createProperty(request, callback)
    
    
    createProperty(request: protos.google.analytics.admin.v1beta.ICreatePropertyRequest, callback: Callback<protos.google.analytics.admin.v1beta.IProperty, protos.google.analytics.admin.v1beta.ICreatePropertyRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreatePropertyRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.icreatepropertyrequest)`   
  
`callback` |  `Callback<[protos.google.analytics.admin.v1beta.IProperty](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.iproperty), [protos.google.analytics.admin.v1beta.ICreatePropertyRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.icreatepropertyrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### customDimensionPath(property, customDimension)
    
    
    customDimensionPath(property: string, customDimension: string): string;

Return a fully-qualified customDimension resource name string.

**Parameters**  
---  
**Name** | **Description**  
`property` |  `string`   
  
`customDimension` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### customMetricPath(property, customMetric)
    
    
    customMetricPath(property: string, customMetric: string): string;

Return a fully-qualified customMetric resource name string.

**Parameters**  
---  
**Name** | **Description**  
`property` |  `string`   
  
`customMetric` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### dataRetentionSettingsPath(property)
    
    
    dataRetentionSettingsPath(property: string): string;

Return a fully-qualified dataRetentionSettings resource name string.

**Parameter**  
---  
**Name** | **Description**  
`property` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### dataSharingSettingsPath(account)
    
    
    dataSharingSettingsPath(account: string): string;

Return a fully-qualified dataSharingSettings resource name string.

**Parameter**  
---  
**Name** | **Description**  
`account` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### dataStreamPath(property, dataStream)
    
    
    dataStreamPath(property: string, dataStream: string): string;

Return a fully-qualified dataStream resource name string.

**Parameters**  
---  
**Name** | **Description**  
`property` |  `string`   
  
`dataStream` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### deleteAccount(request, options)
    
    
    deleteAccount(request?: protos.google.analytics.admin.v1beta.IDeleteAccountRequest, options?: CallOptions): Promise<[
            protos.google.protobuf.IEmpty,
            protos.google.analytics.admin.v1beta.IDeleteAccountRequest | undefined,
            {} | undefined
        ]>;

Marks target Account as soft-deleted (ie: "trashed") and returns it.

This API does not have a method to restore soft-deleted accounts. However, they can be restored using the Trash Can UI.

If the accounts are not restored before the expiration time, the account and all child resources (eg: Properties, GoogleAdsLinks, Streams, AccessBindings) will be permanently purged. <https://support.google.com/analytics/answer/6154772>

Returns an error if the target is not found.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteAccountRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ideleteaccountrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.protobuf.iempty), [protos.google.analytics.admin.v1beta.IDeleteAccountRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ideleteaccountrequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [Empty](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.protobuf.empty). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The name of the Account to soft-delete.
       *  Format: accounts/{account}
       *  Example: "accounts/100"
       */
      // const name = 'abc123'
    
      // Imports the Admin library
      const {AnalyticsAdminServiceClient} = require('[@google-analytics/admin](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const adminClient = new [AnalyticsAdminServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)();
    
      async function callDeleteAccount() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await adminClient.deleteAccount(request);
        console.log(response);
      }
    
      callDeleteAccount();
    
    

### deleteAccount(request, options, callback)
    
    
    deleteAccount(request: protos.google.analytics.admin.v1beta.IDeleteAccountRequest, options: CallOptions, callback: Callback<protos.google.protobuf.IEmpty, protos.google.analytics.admin.v1beta.IDeleteAccountRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteAccountRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ideleteaccountrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.protobuf.iempty), [protos.google.analytics.admin.v1beta.IDeleteAccountRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ideleteaccountrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteAccount(request, callback)
    
    
    deleteAccount(request: protos.google.analytics.admin.v1beta.IDeleteAccountRequest, callback: Callback<protos.google.protobuf.IEmpty, protos.google.analytics.admin.v1beta.IDeleteAccountRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteAccountRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ideleteaccountrequest)`   
  
`callback` |  `Callback<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.protobuf.iempty), [protos.google.analytics.admin.v1beta.IDeleteAccountRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ideleteaccountrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteConversionEvent(request, options)
    
    
    deleteConversionEvent(request?: protos.google.analytics.admin.v1beta.IDeleteConversionEventRequest, options?: CallOptions): Promise<[
            protos.google.protobuf.IEmpty,
            (protos.google.analytics.admin.v1beta.IDeleteConversionEventRequest | undefined),
            {} | undefined
        ]>;

Deprecated: Use `DeleteKeyEvent` instead. Deletes a conversion event in a property.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteConversionEventRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ideleteconversioneventrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.protobuf.iempty), ([protos.google.analytics.admin.v1beta.IDeleteConversionEventRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ideleteconversioneventrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [Empty](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.protobuf.empty). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The resource name of the conversion event to delete.
       *  Format: properties/{property}/conversionEvents/{conversion_event}
       *  Example: "properties/123/conversionEvents/456"
       */
      // const name = 'abc123'
    
      // Imports the Admin library
      const {AnalyticsAdminServiceClient} = require('[@google-analytics/admin](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const adminClient = new [AnalyticsAdminServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)();
    
      async function callDeleteConversionEvent() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await adminClient.deleteConversionEvent(request);
        console.log(response);
      }
    
      callDeleteConversionEvent();
    
    

### deleteConversionEvent(request, options, callback)
    
    
    deleteConversionEvent(request: protos.google.analytics.admin.v1beta.IDeleteConversionEventRequest, options: CallOptions, callback: Callback<protos.google.protobuf.IEmpty, protos.google.analytics.admin.v1beta.IDeleteConversionEventRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteConversionEventRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ideleteconversioneventrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.protobuf.iempty), [protos.google.analytics.admin.v1beta.IDeleteConversionEventRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ideleteconversioneventrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteConversionEvent(request, callback)
    
    
    deleteConversionEvent(request: protos.google.analytics.admin.v1beta.IDeleteConversionEventRequest, callback: Callback<protos.google.protobuf.IEmpty, protos.google.analytics.admin.v1beta.IDeleteConversionEventRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteConversionEventRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ideleteconversioneventrequest)`   
  
`callback` |  `Callback<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.protobuf.iempty), [protos.google.analytics.admin.v1beta.IDeleteConversionEventRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ideleteconversioneventrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteDataStream(request, options)
    
    
    deleteDataStream(request?: protos.google.analytics.admin.v1beta.IDeleteDataStreamRequest, options?: CallOptions): Promise<[
            protos.google.protobuf.IEmpty,
            protos.google.analytics.admin.v1beta.IDeleteDataStreamRequest | undefined,
            {} | undefined
        ]>;

Deletes a DataStream on a property.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteDataStreamRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ideletedatastreamrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.protobuf.iempty), [protos.google.analytics.admin.v1beta.IDeleteDataStreamRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ideletedatastreamrequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [Empty](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.protobuf.empty). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The name of the DataStream to delete.
       *  Example format: properties/1234/dataStreams/5678
       */
      // const name = 'abc123'
    
      // Imports the Admin library
      const {AnalyticsAdminServiceClient} = require('[@google-analytics/admin](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const adminClient = new [AnalyticsAdminServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)();
    
      async function callDeleteDataStream() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await adminClient.deleteDataStream(request);
        console.log(response);
      }
    
      callDeleteDataStream();
    
    

### deleteDataStream(request, options, callback)
    
    
    deleteDataStream(request: protos.google.analytics.admin.v1beta.IDeleteDataStreamRequest, options: CallOptions, callback: Callback<protos.google.protobuf.IEmpty, protos.google.analytics.admin.v1beta.IDeleteDataStreamRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteDataStreamRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ideletedatastreamrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.protobuf.iempty), [protos.google.analytics.admin.v1beta.IDeleteDataStreamRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ideletedatastreamrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteDataStream(request, callback)
    
    
    deleteDataStream(request: protos.google.analytics.admin.v1beta.IDeleteDataStreamRequest, callback: Callback<protos.google.protobuf.IEmpty, protos.google.analytics.admin.v1beta.IDeleteDataStreamRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteDataStreamRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ideletedatastreamrequest)`   
  
`callback` |  `Callback<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.protobuf.iempty), [protos.google.analytics.admin.v1beta.IDeleteDataStreamRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ideletedatastreamrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteFirebaseLink(request, options)
    
    
    deleteFirebaseLink(request?: protos.google.analytics.admin.v1beta.IDeleteFirebaseLinkRequest, options?: CallOptions): Promise<[
            protos.google.protobuf.IEmpty,
            (protos.google.analytics.admin.v1beta.IDeleteFirebaseLinkRequest | undefined),
            {} | undefined
        ]>;

Deletes a FirebaseLink on a property

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteFirebaseLinkRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ideletefirebaselinkrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.protobuf.iempty), ([protos.google.analytics.admin.v1beta.IDeleteFirebaseLinkRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ideletefirebaselinkrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [Empty](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.protobuf.empty). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Format: properties/{property_id}/firebaseLinks/{firebase_link_id}
       *  Example: `properties/1234/firebaseLinks/5678`
       */
      // const name = 'abc123'
    
      // Imports the Admin library
      const {AnalyticsAdminServiceClient} = require('[@google-analytics/admin](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const adminClient = new [AnalyticsAdminServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)();
    
      async function callDeleteFirebaseLink() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await adminClient.deleteFirebaseLink(request);
        console.log(response);
      }
    
      callDeleteFirebaseLink();
    
    

### deleteFirebaseLink(request, options, callback)
    
    
    deleteFirebaseLink(request: protos.google.analytics.admin.v1beta.IDeleteFirebaseLinkRequest, options: CallOptions, callback: Callback<protos.google.protobuf.IEmpty, protos.google.analytics.admin.v1beta.IDeleteFirebaseLinkRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteFirebaseLinkRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ideletefirebaselinkrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.protobuf.iempty), [protos.google.analytics.admin.v1beta.IDeleteFirebaseLinkRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ideletefirebaselinkrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteFirebaseLink(request, callback)
    
    
    deleteFirebaseLink(request: protos.google.analytics.admin.v1beta.IDeleteFirebaseLinkRequest, callback: Callback<protos.google.protobuf.IEmpty, protos.google.analytics.admin.v1beta.IDeleteFirebaseLinkRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteFirebaseLinkRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ideletefirebaselinkrequest)`   
  
`callback` |  `Callback<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.protobuf.iempty), [protos.google.analytics.admin.v1beta.IDeleteFirebaseLinkRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ideletefirebaselinkrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteGoogleAdsLink(request, options)
    
    
    deleteGoogleAdsLink(request?: protos.google.analytics.admin.v1beta.IDeleteGoogleAdsLinkRequest, options?: CallOptions): Promise<[
            protos.google.protobuf.IEmpty,
            (protos.google.analytics.admin.v1beta.IDeleteGoogleAdsLinkRequest | undefined),
            {} | undefined
        ]>;

Deletes a GoogleAdsLink on a property

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteGoogleAdsLinkRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ideletegoogleadslinkrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.protobuf.iempty), ([protos.google.analytics.admin.v1beta.IDeleteGoogleAdsLinkRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ideletegoogleadslinkrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [Empty](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.protobuf.empty). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Example format: properties/1234/googleAdsLinks/5678
       */
      // const name = 'abc123'
    
      // Imports the Admin library
      const {AnalyticsAdminServiceClient} = require('[@google-analytics/admin](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const adminClient = new [AnalyticsAdminServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)();
    
      async function callDeleteGoogleAdsLink() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await adminClient.deleteGoogleAdsLink(request);
        console.log(response);
      }
    
      callDeleteGoogleAdsLink();
    
    

### deleteGoogleAdsLink(request, options, callback)
    
    
    deleteGoogleAdsLink(request: protos.google.analytics.admin.v1beta.IDeleteGoogleAdsLinkRequest, options: CallOptions, callback: Callback<protos.google.protobuf.IEmpty, protos.google.analytics.admin.v1beta.IDeleteGoogleAdsLinkRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteGoogleAdsLinkRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ideletegoogleadslinkrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.protobuf.iempty), [protos.google.analytics.admin.v1beta.IDeleteGoogleAdsLinkRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ideletegoogleadslinkrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteGoogleAdsLink(request, callback)
    
    
    deleteGoogleAdsLink(request: protos.google.analytics.admin.v1beta.IDeleteGoogleAdsLinkRequest, callback: Callback<protos.google.protobuf.IEmpty, protos.google.analytics.admin.v1beta.IDeleteGoogleAdsLinkRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteGoogleAdsLinkRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ideletegoogleadslinkrequest)`   
  
`callback` |  `Callback<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.protobuf.iempty), [protos.google.analytics.admin.v1beta.IDeleteGoogleAdsLinkRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ideletegoogleadslinkrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteKeyEvent(request, options)
    
    
    deleteKeyEvent(request?: protos.google.analytics.admin.v1beta.IDeleteKeyEventRequest, options?: CallOptions): Promise<[
            protos.google.protobuf.IEmpty,
            protos.google.analytics.admin.v1beta.IDeleteKeyEventRequest | undefined,
            {} | undefined
        ]>;

Deletes a Key Event.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteKeyEventRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ideletekeyeventrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.protobuf.iempty), [protos.google.analytics.admin.v1beta.IDeleteKeyEventRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ideletekeyeventrequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [Empty](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.protobuf.empty). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The resource name of the Key Event to delete.
       *  Format: properties/{property}/keyEvents/{key_event}
       *  Example: "properties/123/keyEvents/456"
       */
      // const name = 'abc123'
    
      // Imports the Admin library
      const {AnalyticsAdminServiceClient} = require('[@google-analytics/admin](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const adminClient = new [AnalyticsAdminServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)();
    
      async function callDeleteKeyEvent() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await adminClient.deleteKeyEvent(request);
        console.log(response);
      }
    
      callDeleteKeyEvent();
    
    

### deleteKeyEvent(request, options, callback)
    
    
    deleteKeyEvent(request: protos.google.analytics.admin.v1beta.IDeleteKeyEventRequest, options: CallOptions, callback: Callback<protos.google.protobuf.IEmpty, protos.google.analytics.admin.v1beta.IDeleteKeyEventRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteKeyEventRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ideletekeyeventrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.protobuf.iempty), [protos.google.analytics.admin.v1beta.IDeleteKeyEventRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ideletekeyeventrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteKeyEvent(request, callback)
    
    
    deleteKeyEvent(request: protos.google.analytics.admin.v1beta.IDeleteKeyEventRequest, callback: Callback<protos.google.protobuf.IEmpty, protos.google.analytics.admin.v1beta.IDeleteKeyEventRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteKeyEventRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ideletekeyeventrequest)`   
  
`callback` |  `Callback<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.protobuf.iempty), [protos.google.analytics.admin.v1beta.IDeleteKeyEventRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ideletekeyeventrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteMeasurementProtocolSecret(request, options)
    
    
    deleteMeasurementProtocolSecret(request?: protos.google.analytics.admin.v1beta.IDeleteMeasurementProtocolSecretRequest, options?: CallOptions): Promise<[
            protos.google.protobuf.IEmpty,
            (protos.google.analytics.admin.v1beta.IDeleteMeasurementProtocolSecretRequest | undefined),
            {} | undefined
        ]>;

Deletes target MeasurementProtocolSecret.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteMeasurementProtocolSecretRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ideletemeasurementprotocolsecretrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.protobuf.iempty), ([protos.google.analytics.admin.v1beta.IDeleteMeasurementProtocolSecretRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ideletemeasurementprotocolsecretrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [Empty](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.protobuf.empty). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The name of the MeasurementProtocolSecret to delete.
       *  Format:
       *  properties/{property}/dataStreams/{dataStream}/measurementProtocolSecrets/{measurementProtocolSecret}
       */
      // const name = 'abc123'
    
      // Imports the Admin library
      const {AnalyticsAdminServiceClient} = require('[@google-analytics/admin](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const adminClient = new [AnalyticsAdminServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)();
    
      async function callDeleteMeasurementProtocolSecret() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await adminClient.deleteMeasurementProtocolSecret(request);
        console.log(response);
      }
    
      callDeleteMeasurementProtocolSecret();
    
    

### deleteMeasurementProtocolSecret(request, options, callback)
    
    
    deleteMeasurementProtocolSecret(request: protos.google.analytics.admin.v1beta.IDeleteMeasurementProtocolSecretRequest, options: CallOptions, callback: Callback<protos.google.protobuf.IEmpty, protos.google.analytics.admin.v1beta.IDeleteMeasurementProtocolSecretRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteMeasurementProtocolSecretRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ideletemeasurementprotocolsecretrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.protobuf.iempty), [protos.google.analytics.admin.v1beta.IDeleteMeasurementProtocolSecretRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ideletemeasurementprotocolsecretrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteMeasurementProtocolSecret(request, callback)
    
    
    deleteMeasurementProtocolSecret(request: protos.google.analytics.admin.v1beta.IDeleteMeasurementProtocolSecretRequest, callback: Callback<protos.google.protobuf.IEmpty, protos.google.analytics.admin.v1beta.IDeleteMeasurementProtocolSecretRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteMeasurementProtocolSecretRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ideletemeasurementprotocolsecretrequest)`   
  
`callback` |  `Callback<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.protobuf.iempty), [protos.google.analytics.admin.v1beta.IDeleteMeasurementProtocolSecretRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ideletemeasurementprotocolsecretrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteProperty(request, options)
    
    
    deleteProperty(request?: protos.google.analytics.admin.v1beta.IDeletePropertyRequest, options?: CallOptions): Promise<[
            protos.google.analytics.admin.v1beta.IProperty,
            protos.google.analytics.admin.v1beta.IDeletePropertyRequest | undefined,
            {} | undefined
        ]>;

Marks target Property as soft-deleted (ie: "trashed") and returns it.

This API does not have a method to restore soft-deleted properties. However, they can be restored using the Trash Can UI.

If the properties are not restored before the expiration time, the Property and all child resources (eg: GoogleAdsLinks, Streams, AccessBindings) will be permanently purged. <https://support.google.com/analytics/answer/6154772>

Returns an error if the target is not found.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeletePropertyRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ideletepropertyrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.analytics.admin.v1beta.IProperty](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.iproperty), [protos.google.analytics.admin.v1beta.IDeletePropertyRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ideletepropertyrequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [Property](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.property). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The name of the Property to soft-delete.
       *  Format: properties/{property_id}
       *  Example: "properties/1000"
       */
      // const name = 'abc123'
    
      // Imports the Admin library
      const {AnalyticsAdminServiceClient} = require('[@google-analytics/admin](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const adminClient = new [AnalyticsAdminServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)();
    
      async function callDeleteProperty() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await adminClient.deleteProperty(request);
        console.log(response);
      }
    
      callDeleteProperty();
    
    

### deleteProperty(request, options, callback)
    
    
    deleteProperty(request: protos.google.analytics.admin.v1beta.IDeletePropertyRequest, options: CallOptions, callback: Callback<protos.google.analytics.admin.v1beta.IProperty, protos.google.analytics.admin.v1beta.IDeletePropertyRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeletePropertyRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ideletepropertyrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.analytics.admin.v1beta.IProperty](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.iproperty), [protos.google.analytics.admin.v1beta.IDeletePropertyRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ideletepropertyrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteProperty(request, callback)
    
    
    deleteProperty(request: protos.google.analytics.admin.v1beta.IDeletePropertyRequest, callback: Callback<protos.google.analytics.admin.v1beta.IProperty, protos.google.analytics.admin.v1beta.IDeletePropertyRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeletePropertyRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ideletepropertyrequest)`   
  
`callback` |  `Callback<[protos.google.analytics.admin.v1beta.IProperty](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.iproperty), [protos.google.analytics.admin.v1beta.IDeletePropertyRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ideletepropertyrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### firebaseLinkPath(property, firebaseLink)
    
    
    firebaseLinkPath(property: string, firebaseLink: string): string;

Return a fully-qualified firebaseLink resource name string.

**Parameters**  
---  
**Name** | **Description**  
`property` |  `string`   
  
`firebaseLink` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### getAccount(request, options)
    
    
    getAccount(request?: protos.google.analytics.admin.v1beta.IGetAccountRequest, options?: CallOptions): Promise<[
            protos.google.analytics.admin.v1beta.IAccount,
            protos.google.analytics.admin.v1beta.IGetAccountRequest | undefined,
            {} | undefined
        ]>;

Lookup for a single Account.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetAccountRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.igetaccountrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.analytics.admin.v1beta.IAccount](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.iaccount), [protos.google.analytics.admin.v1beta.IGetAccountRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.igetaccountrequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [Account](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.account). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The name of the account to lookup.
       *  Format: accounts/{account}
       *  Example: "accounts/100"
       */
      // const name = 'abc123'
    
      // Imports the Admin library
      const {AnalyticsAdminServiceClient} = require('[@google-analytics/admin](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const adminClient = new [AnalyticsAdminServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)();
    
      async function callGetAccount() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await adminClient.getAccount(request);
        console.log(response);
      }
    
      callGetAccount();
    
    

### getAccount(request, options, callback)
    
    
    getAccount(request: protos.google.analytics.admin.v1beta.IGetAccountRequest, options: CallOptions, callback: Callback<protos.google.analytics.admin.v1beta.IAccount, protos.google.analytics.admin.v1beta.IGetAccountRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetAccountRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.igetaccountrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.analytics.admin.v1beta.IAccount](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.iaccount), [protos.google.analytics.admin.v1beta.IGetAccountRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.igetaccountrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getAccount(request, callback)
    
    
    getAccount(request: protos.google.analytics.admin.v1beta.IGetAccountRequest, callback: Callback<protos.google.analytics.admin.v1beta.IAccount, protos.google.analytics.admin.v1beta.IGetAccountRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetAccountRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.igetaccountrequest)`   
  
`callback` |  `Callback<[protos.google.analytics.admin.v1beta.IAccount](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.iaccount), [protos.google.analytics.admin.v1beta.IGetAccountRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.igetaccountrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getConversionEvent(request, options)
    
    
    getConversionEvent(request?: protos.google.analytics.admin.v1beta.IGetConversionEventRequest, options?: CallOptions): Promise<[
            protos.google.analytics.admin.v1beta.IConversionEvent,
            (protos.google.analytics.admin.v1beta.IGetConversionEventRequest | undefined),
            {} | undefined
        ]>;

Deprecated: Use `GetKeyEvent` instead. Retrieve a single conversion event.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetConversionEventRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.igetconversioneventrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.analytics.admin.v1beta.IConversionEvent](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.iconversionevent), ([protos.google.analytics.admin.v1beta.IGetConversionEventRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.igetconversioneventrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The resource name of the conversion event to retrieve.
       *  Format: properties/{property}/conversionEvents/{conversion_event}
       *  Example: "properties/123/conversionEvents/456"
       */
      // const name = 'abc123'
    
      // Imports the Admin library
      const {AnalyticsAdminServiceClient} = require('[@google-analytics/admin](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const adminClient = new [AnalyticsAdminServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)();
    
      async function callGetConversionEvent() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await adminClient.getConversionEvent(request);
        console.log(response);
      }
    
      callGetConversionEvent();
    
    

### getConversionEvent(request, options, callback)
    
    
    getConversionEvent(request: protos.google.analytics.admin.v1beta.IGetConversionEventRequest, options: CallOptions, callback: Callback<protos.google.analytics.admin.v1beta.IConversionEvent, protos.google.analytics.admin.v1beta.IGetConversionEventRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetConversionEventRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.igetconversioneventrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.analytics.admin.v1beta.IConversionEvent](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.iconversionevent), [protos.google.analytics.admin.v1beta.IGetConversionEventRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.igetconversioneventrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getConversionEvent(request, callback)
    
    
    getConversionEvent(request: protos.google.analytics.admin.v1beta.IGetConversionEventRequest, callback: Callback<protos.google.analytics.admin.v1beta.IConversionEvent, protos.google.analytics.admin.v1beta.IGetConversionEventRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetConversionEventRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.igetconversioneventrequest)`   
  
`callback` |  `Callback<[protos.google.analytics.admin.v1beta.IConversionEvent](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.iconversionevent), [protos.google.analytics.admin.v1beta.IGetConversionEventRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.igetconversioneventrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getCustomDimension(request, options)
    
    
    getCustomDimension(request?: protos.google.analytics.admin.v1beta.IGetCustomDimensionRequest, options?: CallOptions): Promise<[
            protos.google.analytics.admin.v1beta.ICustomDimension,
            (protos.google.analytics.admin.v1beta.IGetCustomDimensionRequest | undefined),
            {} | undefined
        ]>;

Lookup for a single CustomDimension.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetCustomDimensionRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.igetcustomdimensionrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.analytics.admin.v1beta.ICustomDimension](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.icustomdimension), ([protos.google.analytics.admin.v1beta.IGetCustomDimensionRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.igetcustomdimensionrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The name of the CustomDimension to get.
       *  Example format: properties/1234/customDimensions/5678
       */
      // const name = 'abc123'
    
      // Imports the Admin library
      const {AnalyticsAdminServiceClient} = require('[@google-analytics/admin](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const adminClient = new [AnalyticsAdminServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)();
    
      async function callGetCustomDimension() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await adminClient.getCustomDimension(request);
        console.log(response);
      }
    
      callGetCustomDimension();
    
    

### getCustomDimension(request, options, callback)
    
    
    getCustomDimension(request: protos.google.analytics.admin.v1beta.IGetCustomDimensionRequest, options: CallOptions, callback: Callback<protos.google.analytics.admin.v1beta.ICustomDimension, protos.google.analytics.admin.v1beta.IGetCustomDimensionRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetCustomDimensionRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.igetcustomdimensionrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.analytics.admin.v1beta.ICustomDimension](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.icustomdimension), [protos.google.analytics.admin.v1beta.IGetCustomDimensionRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.igetcustomdimensionrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getCustomDimension(request, callback)
    
    
    getCustomDimension(request: protos.google.analytics.admin.v1beta.IGetCustomDimensionRequest, callback: Callback<protos.google.analytics.admin.v1beta.ICustomDimension, protos.google.analytics.admin.v1beta.IGetCustomDimensionRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetCustomDimensionRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.igetcustomdimensionrequest)`   
  
`callback` |  `Callback<[protos.google.analytics.admin.v1beta.ICustomDimension](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.icustomdimension), [protos.google.analytics.admin.v1beta.IGetCustomDimensionRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.igetcustomdimensionrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getCustomMetric(request, options)
    
    
    getCustomMetric(request?: protos.google.analytics.admin.v1beta.IGetCustomMetricRequest, options?: CallOptions): Promise<[
            protos.google.analytics.admin.v1beta.ICustomMetric,
            protos.google.analytics.admin.v1beta.IGetCustomMetricRequest | undefined,
            {} | undefined
        ]>;

Lookup for a single CustomMetric.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetCustomMetricRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.igetcustommetricrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.analytics.admin.v1beta.ICustomMetric](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.icustommetric), [protos.google.analytics.admin.v1beta.IGetCustomMetricRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.igetcustommetricrequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The name of the CustomMetric to get.
       *  Example format: properties/1234/customMetrics/5678
       */
      // const name = 'abc123'
    
      // Imports the Admin library
      const {AnalyticsAdminServiceClient} = require('[@google-analytics/admin](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const adminClient = new [AnalyticsAdminServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)();
    
      async function callGetCustomMetric() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await adminClient.getCustomMetric(request);
        console.log(response);
      }
    
      callGetCustomMetric();
    
    

### getCustomMetric(request, options, callback)
    
    
    getCustomMetric(request: protos.google.analytics.admin.v1beta.IGetCustomMetricRequest, options: CallOptions, callback: Callback<protos.google.analytics.admin.v1beta.ICustomMetric, protos.google.analytics.admin.v1beta.IGetCustomMetricRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetCustomMetricRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.igetcustommetricrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.analytics.admin.v1beta.ICustomMetric](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.icustommetric), [protos.google.analytics.admin.v1beta.IGetCustomMetricRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.igetcustommetricrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getCustomMetric(request, callback)
    
    
    getCustomMetric(request: protos.google.analytics.admin.v1beta.IGetCustomMetricRequest, callback: Callback<protos.google.analytics.admin.v1beta.ICustomMetric, protos.google.analytics.admin.v1beta.IGetCustomMetricRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetCustomMetricRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.igetcustommetricrequest)`   
  
`callback` |  `Callback<[protos.google.analytics.admin.v1beta.ICustomMetric](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.icustommetric), [protos.google.analytics.admin.v1beta.IGetCustomMetricRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.igetcustommetricrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getDataRetentionSettings(request, options)
    
    
    getDataRetentionSettings(request?: protos.google.analytics.admin.v1beta.IGetDataRetentionSettingsRequest, options?: CallOptions): Promise<[
            protos.google.analytics.admin.v1beta.IDataRetentionSettings,
            (protos.google.analytics.admin.v1beta.IGetDataRetentionSettingsRequest | undefined),
            {} | undefined
        ]>;

Returns the singleton data retention settings for this property.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetDataRetentionSettingsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.igetdataretentionsettingsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.analytics.admin.v1beta.IDataRetentionSettings](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.idataretentionsettings), ([protos.google.analytics.admin.v1beta.IGetDataRetentionSettingsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.igetdataretentionsettingsrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The name of the settings to lookup.
       *  Format:
       *  properties/{property}/dataRetentionSettings
       *  Example: "properties/1000/dataRetentionSettings"
       */
      // const name = 'abc123'
    
      // Imports the Admin library
      const {AnalyticsAdminServiceClient} = require('[@google-analytics/admin](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const adminClient = new [AnalyticsAdminServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)();
    
      async function callGetDataRetentionSettings() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await adminClient.getDataRetentionSettings(request);
        console.log(response);
      }
    
      callGetDataRetentionSettings();
    
    

### getDataRetentionSettings(request, options, callback)
    
    
    getDataRetentionSettings(request: protos.google.analytics.admin.v1beta.IGetDataRetentionSettingsRequest, options: CallOptions, callback: Callback<protos.google.analytics.admin.v1beta.IDataRetentionSettings, protos.google.analytics.admin.v1beta.IGetDataRetentionSettingsRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetDataRetentionSettingsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.igetdataretentionsettingsrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.analytics.admin.v1beta.IDataRetentionSettings](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.idataretentionsettings), [protos.google.analytics.admin.v1beta.IGetDataRetentionSettingsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.igetdataretentionsettingsrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getDataRetentionSettings(request, callback)
    
    
    getDataRetentionSettings(request: protos.google.analytics.admin.v1beta.IGetDataRetentionSettingsRequest, callback: Callback<protos.google.analytics.admin.v1beta.IDataRetentionSettings, protos.google.analytics.admin.v1beta.IGetDataRetentionSettingsRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetDataRetentionSettingsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.igetdataretentionsettingsrequest)`   
  
`callback` |  `Callback<[protos.google.analytics.admin.v1beta.IDataRetentionSettings](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.idataretentionsettings), [protos.google.analytics.admin.v1beta.IGetDataRetentionSettingsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.igetdataretentionsettingsrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getDataSharingSettings(request, options)
    
    
    getDataSharingSettings(request?: protos.google.analytics.admin.v1beta.IGetDataSharingSettingsRequest, options?: CallOptions): Promise<[
            protos.google.analytics.admin.v1beta.IDataSharingSettings,
            (protos.google.analytics.admin.v1beta.IGetDataSharingSettingsRequest | undefined),
            {} | undefined
        ]>;

Get data sharing settings on an account. Data sharing settings are singletons.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetDataSharingSettingsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.igetdatasharingsettingsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.analytics.admin.v1beta.IDataSharingSettings](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.idatasharingsettings), ([protos.google.analytics.admin.v1beta.IGetDataSharingSettingsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.igetdatasharingsettingsrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [DataSharingSettings](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.datasharingsettings). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The name of the settings to lookup.
       *  Format: accounts/{account}/dataSharingSettings
       *  Example: `accounts/1000/dataSharingSettings`
       */
      // const name = 'abc123'
    
      // Imports the Admin library
      const {AnalyticsAdminServiceClient} = require('[@google-analytics/admin](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const adminClient = new [AnalyticsAdminServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)();
    
      async function callGetDataSharingSettings() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await adminClient.getDataSharingSettings(request);
        console.log(response);
      }
    
      callGetDataSharingSettings();
    
    

### getDataSharingSettings(request, options, callback)
    
    
    getDataSharingSettings(request: protos.google.analytics.admin.v1beta.IGetDataSharingSettingsRequest, options: CallOptions, callback: Callback<protos.google.analytics.admin.v1beta.IDataSharingSettings, protos.google.analytics.admin.v1beta.IGetDataSharingSettingsRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetDataSharingSettingsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.igetdatasharingsettingsrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.analytics.admin.v1beta.IDataSharingSettings](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.idatasharingsettings), [protos.google.analytics.admin.v1beta.IGetDataSharingSettingsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.igetdatasharingsettingsrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getDataSharingSettings(request, callback)
    
    
    getDataSharingSettings(request: protos.google.analytics.admin.v1beta.IGetDataSharingSettingsRequest, callback: Callback<protos.google.analytics.admin.v1beta.IDataSharingSettings, protos.google.analytics.admin.v1beta.IGetDataSharingSettingsRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetDataSharingSettingsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.igetdatasharingsettingsrequest)`   
  
`callback` |  `Callback<[protos.google.analytics.admin.v1beta.IDataSharingSettings](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.idatasharingsettings), [protos.google.analytics.admin.v1beta.IGetDataSharingSettingsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.igetdatasharingsettingsrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getDataStream(request, options)
    
    
    getDataStream(request?: protos.google.analytics.admin.v1beta.IGetDataStreamRequest, options?: CallOptions): Promise<[
            protos.google.analytics.admin.v1beta.IDataStream,
            protos.google.analytics.admin.v1beta.IGetDataStreamRequest | undefined,
            {} | undefined
        ]>;

Lookup for a single DataStream.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetDataStreamRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.igetdatastreamrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.analytics.admin.v1beta.IDataStream](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.idatastream), [protos.google.analytics.admin.v1beta.IGetDataStreamRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.igetdatastreamrequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The name of the DataStream to get.
       *  Example format: properties/1234/dataStreams/5678
       */
      // const name = 'abc123'
    
      // Imports the Admin library
      const {AnalyticsAdminServiceClient} = require('[@google-analytics/admin](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const adminClient = new [AnalyticsAdminServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)();
    
      async function callGetDataStream() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await adminClient.getDataStream(request);
        console.log(response);
      }
    
      callGetDataStream();
    
    

### getDataStream(request, options, callback)
    
    
    getDataStream(request: protos.google.analytics.admin.v1beta.IGetDataStreamRequest, options: CallOptions, callback: Callback<protos.google.analytics.admin.v1beta.IDataStream, protos.google.analytics.admin.v1beta.IGetDataStreamRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetDataStreamRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.igetdatastreamrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.analytics.admin.v1beta.IDataStream](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.idatastream), [protos.google.analytics.admin.v1beta.IGetDataStreamRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.igetdatastreamrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getDataStream(request, callback)
    
    
    getDataStream(request: protos.google.analytics.admin.v1beta.IGetDataStreamRequest, callback: Callback<protos.google.analytics.admin.v1beta.IDataStream, protos.google.analytics.admin.v1beta.IGetDataStreamRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetDataStreamRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.igetdatastreamrequest)`   
  
`callback` |  `Callback<[protos.google.analytics.admin.v1beta.IDataStream](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.idatastream), [protos.google.analytics.admin.v1beta.IGetDataStreamRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.igetdatastreamrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getKeyEvent(request, options)
    
    
    getKeyEvent(request?: protos.google.analytics.admin.v1beta.IGetKeyEventRequest, options?: CallOptions): Promise<[
            protos.google.analytics.admin.v1beta.IKeyEvent,
            protos.google.analytics.admin.v1beta.IGetKeyEventRequest | undefined,
            {} | undefined
        ]>;

Retrieve a single Key Event.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetKeyEventRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.igetkeyeventrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.analytics.admin.v1beta.IKeyEvent](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ikeyevent), [protos.google.analytics.admin.v1beta.IGetKeyEventRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.igetkeyeventrequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The resource name of the Key Event to retrieve.
       *  Format: properties/{property}/keyEvents/{key_event}
       *  Example: "properties/123/keyEvents/456"
       */
      // const name = 'abc123'
    
      // Imports the Admin library
      const {AnalyticsAdminServiceClient} = require('[@google-analytics/admin](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const adminClient = new [AnalyticsAdminServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)();
    
      async function callGetKeyEvent() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await adminClient.getKeyEvent(request);
        console.log(response);
      }
    
      callGetKeyEvent();
    
    

### getKeyEvent(request, options, callback)
    
    
    getKeyEvent(request: protos.google.analytics.admin.v1beta.IGetKeyEventRequest, options: CallOptions, callback: Callback<protos.google.analytics.admin.v1beta.IKeyEvent, protos.google.analytics.admin.v1beta.IGetKeyEventRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetKeyEventRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.igetkeyeventrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.analytics.admin.v1beta.IKeyEvent](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ikeyevent), [protos.google.analytics.admin.v1beta.IGetKeyEventRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.igetkeyeventrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getKeyEvent(request, callback)
    
    
    getKeyEvent(request: protos.google.analytics.admin.v1beta.IGetKeyEventRequest, callback: Callback<protos.google.analytics.admin.v1beta.IKeyEvent, protos.google.analytics.admin.v1beta.IGetKeyEventRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetKeyEventRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.igetkeyeventrequest)`   
  
`callback` |  `Callback<[protos.google.analytics.admin.v1beta.IKeyEvent](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ikeyevent), [protos.google.analytics.admin.v1beta.IGetKeyEventRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.igetkeyeventrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getMeasurementProtocolSecret(request, options)
    
    
    getMeasurementProtocolSecret(request?: protos.google.analytics.admin.v1beta.IGetMeasurementProtocolSecretRequest, options?: CallOptions): Promise<[
            protos.google.analytics.admin.v1beta.IMeasurementProtocolSecret,
            (protos.google.analytics.admin.v1beta.IGetMeasurementProtocolSecretRequest | undefined),
            {} | undefined
        ]>;

Lookup for a single MeasurementProtocolSecret.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetMeasurementProtocolSecretRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.igetmeasurementprotocolsecretrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.analytics.admin.v1beta.IMeasurementProtocolSecret](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.imeasurementprotocolsecret), ([protos.google.analytics.admin.v1beta.IGetMeasurementProtocolSecretRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.igetmeasurementprotocolsecretrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [MeasurementProtocolSecret](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.measurementprotocolsecret). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The name of the measurement protocol secret to lookup.
       *  Format:
       *  properties/{property}/dataStreams/{dataStream}/measurementProtocolSecrets/{measurementProtocolSecret}
       */
      // const name = 'abc123'
    
      // Imports the Admin library
      const {AnalyticsAdminServiceClient} = require('[@google-analytics/admin](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const adminClient = new [AnalyticsAdminServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)();
    
      async function callGetMeasurementProtocolSecret() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await adminClient.getMeasurementProtocolSecret(request);
        console.log(response);
      }
    
      callGetMeasurementProtocolSecret();
    
    

### getMeasurementProtocolSecret(request, options, callback)
    
    
    getMeasurementProtocolSecret(request: protos.google.analytics.admin.v1beta.IGetMeasurementProtocolSecretRequest, options: CallOptions, callback: Callback<protos.google.analytics.admin.v1beta.IMeasurementProtocolSecret, protos.google.analytics.admin.v1beta.IGetMeasurementProtocolSecretRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetMeasurementProtocolSecretRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.igetmeasurementprotocolsecretrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.analytics.admin.v1beta.IMeasurementProtocolSecret](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.imeasurementprotocolsecret), [protos.google.analytics.admin.v1beta.IGetMeasurementProtocolSecretRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.igetmeasurementprotocolsecretrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getMeasurementProtocolSecret(request, callback)
    
    
    getMeasurementProtocolSecret(request: protos.google.analytics.admin.v1beta.IGetMeasurementProtocolSecretRequest, callback: Callback<protos.google.analytics.admin.v1beta.IMeasurementProtocolSecret, protos.google.analytics.admin.v1beta.IGetMeasurementProtocolSecretRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetMeasurementProtocolSecretRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.igetmeasurementprotocolsecretrequest)`   
  
`callback` |  `Callback<[protos.google.analytics.admin.v1beta.IMeasurementProtocolSecret](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.imeasurementprotocolsecret), [protos.google.analytics.admin.v1beta.IGetMeasurementProtocolSecretRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.igetmeasurementprotocolsecretrequest) | null | undefined, {} | null | undefined>`   
  
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
  
### getProperty(request, options)
    
    
    getProperty(request?: protos.google.analytics.admin.v1beta.IGetPropertyRequest, options?: CallOptions): Promise<[
            protos.google.analytics.admin.v1beta.IProperty,
            protos.google.analytics.admin.v1beta.IGetPropertyRequest | undefined,
            {} | undefined
        ]>;

Lookup for a single GA Property.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetPropertyRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.igetpropertyrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.analytics.admin.v1beta.IProperty](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.iproperty), [protos.google.analytics.admin.v1beta.IGetPropertyRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.igetpropertyrequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [Property](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.property). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The name of the property to lookup.
       *  Format: properties/{property_id}
       *  Example: "properties/1000"
       */
      // const name = 'abc123'
    
      // Imports the Admin library
      const {AnalyticsAdminServiceClient} = require('[@google-analytics/admin](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const adminClient = new [AnalyticsAdminServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)();
    
      async function callGetProperty() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await adminClient.getProperty(request);
        console.log(response);
      }
    
      callGetProperty();
    
    

### getProperty(request, options, callback)
    
    
    getProperty(request: protos.google.analytics.admin.v1beta.IGetPropertyRequest, options: CallOptions, callback: Callback<protos.google.analytics.admin.v1beta.IProperty, protos.google.analytics.admin.v1beta.IGetPropertyRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetPropertyRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.igetpropertyrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.analytics.admin.v1beta.IProperty](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.iproperty), [protos.google.analytics.admin.v1beta.IGetPropertyRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.igetpropertyrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getProperty(request, callback)
    
    
    getProperty(request: protos.google.analytics.admin.v1beta.IGetPropertyRequest, callback: Callback<protos.google.analytics.admin.v1beta.IProperty, protos.google.analytics.admin.v1beta.IGetPropertyRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetPropertyRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.igetpropertyrequest)`   
  
`callback` |  `Callback<[protos.google.analytics.admin.v1beta.IProperty](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.iproperty), [protos.google.analytics.admin.v1beta.IGetPropertyRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.igetpropertyrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### googleAdsLinkPath(property, googleAdsLink)
    
    
    googleAdsLinkPath(property: string, googleAdsLink: string): string;

Return a fully-qualified googleAdsLink resource name string.

**Parameters**  
---  
**Name** | **Description**  
`property` |  `string`   
  
`googleAdsLink` |  `string`   
  
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
  
### keyEventPath(property, keyEvent)
    
    
    keyEventPath(property: string, keyEvent: string): string;

Return a fully-qualified keyEvent resource name string.

**Parameters**  
---  
**Name** | **Description**  
`property` |  `string`   
  
`keyEvent` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### listAccounts(request, options)
    
    
    listAccounts(request?: protos.google.analytics.admin.v1beta.IListAccountsRequest, options?: CallOptions): Promise<[
            protos.google.analytics.admin.v1beta.IAccount[],
            protos.google.analytics.admin.v1beta.IListAccountsRequest | null,
            protos.google.analytics.admin.v1beta.IListAccountsResponse
        ]>;

Returns all accounts accessible by the caller.

Note that these accounts might not currently have GA properties. Soft-deleted (ie: "trashed") accounts are excluded by default. Returns an empty list if no relevant accounts are found.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListAccountsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ilistaccountsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.analytics.admin.v1beta.IAccount](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.iaccount)[], [protos.google.analytics.admin.v1beta.IListAccountsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ilistaccountsrequest) | null, [protos.google.analytics.admin.v1beta.IListAccountsResponse](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ilistaccountsresponse) ]>` | {Promise} - The promise which resolves to an array. The first element of the array is Array of [Account](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.account). The client library will perform auto-pagination by default: it will call the API as many times as needed and will merge results from all the pages into this array. Note that it can affect your quota. We recommend using `listAccountsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listAccounts(request, options, callback)
    
    
    listAccounts(request: protos.google.analytics.admin.v1beta.IListAccountsRequest, options: CallOptions, callback: PaginationCallback<protos.google.analytics.admin.v1beta.IListAccountsRequest, protos.google.analytics.admin.v1beta.IListAccountsResponse | null | undefined, protos.google.analytics.admin.v1beta.IAccount>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListAccountsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ilistaccountsrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `PaginationCallback<[protos.google.analytics.admin.v1beta.IListAccountsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ilistaccountsrequest), [protos.google.analytics.admin.v1beta.IListAccountsResponse](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ilistaccountsresponse) | null | undefined, [protos.google.analytics.admin.v1beta.IAccount](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.iaccount)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listAccounts(request, callback)
    
    
    listAccounts(request: protos.google.analytics.admin.v1beta.IListAccountsRequest, callback: PaginationCallback<protos.google.analytics.admin.v1beta.IListAccountsRequest, protos.google.analytics.admin.v1beta.IListAccountsResponse | null | undefined, protos.google.analytics.admin.v1beta.IAccount>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListAccountsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ilistaccountsrequest)`   
  
`callback` |  `PaginationCallback<[protos.google.analytics.admin.v1beta.IListAccountsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ilistaccountsrequest), [protos.google.analytics.admin.v1beta.IListAccountsResponse](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ilistaccountsresponse) | null | undefined, [protos.google.analytics.admin.v1beta.IAccount](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.iaccount)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listAccountsAsync(request, options)
    
    
    listAccountsAsync(request?: protos.google.analytics.admin.v1beta.IListAccountsRequest, options?: CallOptions): AsyncIterable<protos.google.analytics.admin.v1beta.IAccount>;

Equivalent to `listAccounts`, but returns an iterable object.

`for`-`await`-`of` syntax is used with the iterable to get response elements on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListAccountsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ilistaccountsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.analytics.admin.v1beta.IAccount](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.iaccount)>` | {Object} An iterable Object that allows [async iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols). When you iterate the returned iterable, each element will be an object representing [Account](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.account). The API will be called under the hood as needed, once per the page, so you can stop the iteration when you don't need more results. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Optional. The maximum number of resources to return. The service may return
       *  fewer than this value, even if there are additional pages.
       *  If unspecified, at most 50 resources will be returned.
       *  The maximum value is 200; (higher values will be coerced to the maximum)
       */
      // const pageSize = 1234
      /**
       *  Optional. A page token, received from a previous `ListAccounts` call.
       *  Provide this to retrieve the subsequent page.
       *  When paginating, all other parameters provided to `ListAccounts` must
       *  match the call that provided the page token.
       */
      // const pageToken = 'abc123'
      /**
       *  Whether to include soft-deleted (ie: "trashed") Accounts in the
       *  results. Accounts can be inspected to determine whether they are deleted or
       *  not.
       */
      // const showDeleted = true
    
      // Imports the Admin library
      const {AnalyticsAdminServiceClient} = require('[@google-analytics/admin](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const adminClient = new [AnalyticsAdminServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)();
    
      async function callListAccounts() {
        // Construct request
        const request = {
        };
    
        // Run request
        const iterable = adminClient.listAccountsAsync(request);
        for await (const response of iterable) {
            console.log(response);
        }
      }
    
      callListAccounts();
    
    

### listAccountsStream(request, options)
    
    
    listAccountsStream(request?: protos.google.analytics.admin.v1beta.IListAccountsRequest, options?: CallOptions): Transform;

Equivalent to `listAccounts`, but returns a NodeJS Stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListAccountsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ilistaccountsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Transform` | {Stream} An object stream which emits an object representing [Account](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.account) on 'data' event. The client library will perform auto-pagination by default: it will call the API as many times as needed. Note that it can affect your quota. We recommend using `listAccountsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listAccountSummaries(request, options)
    
    
    listAccountSummaries(request?: protos.google.analytics.admin.v1beta.IListAccountSummariesRequest, options?: CallOptions): Promise<[
            protos.google.analytics.admin.v1beta.IAccountSummary[],
            protos.google.analytics.admin.v1beta.IListAccountSummariesRequest | null,
            protos.google.analytics.admin.v1beta.IListAccountSummariesResponse
        ]>;

Returns summaries of all accounts accessible by the caller.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListAccountSummariesRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ilistaccountsummariesrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.analytics.admin.v1beta.IAccountSummary](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.iaccountsummary)[], [protos.google.analytics.admin.v1beta.IListAccountSummariesRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ilistaccountsummariesrequest) | null, [protos.google.analytics.admin.v1beta.IListAccountSummariesResponse](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ilistaccountsummariesresponse) ]>` | {Promise} - The promise which resolves to an array. The first element of the array is Array of [AccountSummary](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.accountsummary). The client library will perform auto-pagination by default: it will call the API as many times as needed and will merge results from all the pages into this array. Note that it can affect your quota. We recommend using `listAccountSummariesAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listAccountSummaries(request, options, callback)
    
    
    listAccountSummaries(request: protos.google.analytics.admin.v1beta.IListAccountSummariesRequest, options: CallOptions, callback: PaginationCallback<protos.google.analytics.admin.v1beta.IListAccountSummariesRequest, protos.google.analytics.admin.v1beta.IListAccountSummariesResponse | null | undefined, protos.google.analytics.admin.v1beta.IAccountSummary>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListAccountSummariesRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ilistaccountsummariesrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `PaginationCallback<[protos.google.analytics.admin.v1beta.IListAccountSummariesRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ilistaccountsummariesrequest), [protos.google.analytics.admin.v1beta.IListAccountSummariesResponse](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ilistaccountsummariesresponse) | null | undefined, [protos.google.analytics.admin.v1beta.IAccountSummary](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.iaccountsummary)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listAccountSummaries(request, callback)
    
    
    listAccountSummaries(request: protos.google.analytics.admin.v1beta.IListAccountSummariesRequest, callback: PaginationCallback<protos.google.analytics.admin.v1beta.IListAccountSummariesRequest, protos.google.analytics.admin.v1beta.IListAccountSummariesResponse | null | undefined, protos.google.analytics.admin.v1beta.IAccountSummary>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListAccountSummariesRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ilistaccountsummariesrequest)`   
  
`callback` |  `PaginationCallback<[protos.google.analytics.admin.v1beta.IListAccountSummariesRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ilistaccountsummariesrequest), [protos.google.analytics.admin.v1beta.IListAccountSummariesResponse](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ilistaccountsummariesresponse) | null | undefined, [protos.google.analytics.admin.v1beta.IAccountSummary](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.iaccountsummary)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listAccountSummariesAsync(request, options)
    
    
    listAccountSummariesAsync(request?: protos.google.analytics.admin.v1beta.IListAccountSummariesRequest, options?: CallOptions): AsyncIterable<protos.google.analytics.admin.v1beta.IAccountSummary>;

Equivalent to `listAccountSummaries`, but returns an iterable object.

`for`-`await`-`of` syntax is used with the iterable to get response elements on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListAccountSummariesRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ilistaccountsummariesrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.analytics.admin.v1beta.IAccountSummary](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.iaccountsummary)>` | {Object} An iterable Object that allows [async iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols). When you iterate the returned iterable, each element will be an object representing [AccountSummary](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.accountsummary). The API will be called under the hood as needed, once per the page, so you can stop the iteration when you don't need more results. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Optional. The maximum number of AccountSummary resources to return. The
       *  service may return fewer than this value, even if there are additional
       *  pages. If unspecified, at most 50 resources will be returned. The maximum
       *  value is 200; (higher values will be coerced to the maximum)
       */
      // const pageSize = 1234
      /**
       *  Optional. A page token, received from a previous `ListAccountSummaries`
       *  call. Provide this to retrieve the subsequent page. When paginating, all
       *  other parameters provided to `ListAccountSummaries` must match the call
       *  that provided the page token.
       */
      // const pageToken = 'abc123'
    
      // Imports the Admin library
      const {AnalyticsAdminServiceClient} = require('[@google-analytics/admin](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const adminClient = new [AnalyticsAdminServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)();
    
      async function callListAccountSummaries() {
        // Construct request
        const request = {
        };
    
        // Run request
        const iterable = adminClient.listAccountSummariesAsync(request);
        for await (const response of iterable) {
            console.log(response);
        }
      }
    
      callListAccountSummaries();
    
    

### listAccountSummariesStream(request, options)
    
    
    listAccountSummariesStream(request?: protos.google.analytics.admin.v1beta.IListAccountSummariesRequest, options?: CallOptions): Transform;

Equivalent to `listAccountSummaries`, but returns a NodeJS Stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListAccountSummariesRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ilistaccountsummariesrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Transform` | {Stream} An object stream which emits an object representing [AccountSummary](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.accountsummary) on 'data' event. The client library will perform auto-pagination by default: it will call the API as many times as needed. Note that it can affect your quota. We recommend using `listAccountSummariesAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listConversionEvents(request, options)
    
    
    listConversionEvents(request?: protos.google.analytics.admin.v1beta.IListConversionEventsRequest, options?: CallOptions): Promise<[
            protos.google.analytics.admin.v1beta.IConversionEvent[],
            protos.google.analytics.admin.v1beta.IListConversionEventsRequest | null,
            protos.google.analytics.admin.v1beta.IListConversionEventsResponse
        ]>;

Deprecated: Use `ListKeyEvents` instead. Returns a list of conversion events in the specified parent property.

Returns an empty list if no conversion events are found.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListConversionEventsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ilistconversioneventsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.analytics.admin.v1beta.IConversionEvent](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.iconversionevent)[], [protos.google.analytics.admin.v1beta.IListConversionEventsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ilistconversioneventsrequest) | null, [protos.google.analytics.admin.v1beta.IListConversionEventsResponse](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ilistconversioneventsresponse) ]>` | {Promise} - The promise which resolves to an array. The first element of the array is Array of . The client library will perform auto-pagination by default: it will call the API as many times as needed and will merge results from all the pages into this array. Note that it can affect your quota. We recommend using `listConversionEventsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listConversionEvents(request, options, callback)
    
    
    listConversionEvents(request: protos.google.analytics.admin.v1beta.IListConversionEventsRequest, options: CallOptions, callback: PaginationCallback<protos.google.analytics.admin.v1beta.IListConversionEventsRequest, protos.google.analytics.admin.v1beta.IListConversionEventsResponse | null | undefined, protos.google.analytics.admin.v1beta.IConversionEvent>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListConversionEventsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ilistconversioneventsrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `PaginationCallback<[protos.google.analytics.admin.v1beta.IListConversionEventsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ilistconversioneventsrequest), [protos.google.analytics.admin.v1beta.IListConversionEventsResponse](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ilistconversioneventsresponse) | null | undefined, [protos.google.analytics.admin.v1beta.IConversionEvent](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.iconversionevent)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listConversionEvents(request, callback)
    
    
    listConversionEvents(request: protos.google.analytics.admin.v1beta.IListConversionEventsRequest, callback: PaginationCallback<protos.google.analytics.admin.v1beta.IListConversionEventsRequest, protos.google.analytics.admin.v1beta.IListConversionEventsResponse | null | undefined, protos.google.analytics.admin.v1beta.IConversionEvent>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListConversionEventsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ilistconversioneventsrequest)`   
  
`callback` |  `PaginationCallback<[protos.google.analytics.admin.v1beta.IListConversionEventsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ilistconversioneventsrequest), [protos.google.analytics.admin.v1beta.IListConversionEventsResponse](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ilistconversioneventsresponse) | null | undefined, [protos.google.analytics.admin.v1beta.IConversionEvent](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.iconversionevent)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listConversionEventsAsync(request, options)
    
    
    listConversionEventsAsync(request?: protos.google.analytics.admin.v1beta.IListConversionEventsRequest, options?: CallOptions): AsyncIterable<protos.google.analytics.admin.v1beta.IConversionEvent>;

Equivalent to `listConversionEvents`, but returns an iterable object.

`for`-`await`-`of` syntax is used with the iterable to get response elements on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListConversionEventsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ilistconversioneventsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.analytics.admin.v1beta.IConversionEvent](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.iconversionevent)>` | {Object} An iterable Object that allows [async iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols). When you iterate the returned iterable, each element will be an object representing . The API will be called under the hood as needed, once per the page, so you can stop the iteration when you don't need more results. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The resource name of the parent property.
       *  Example: 'properties/123'
       */
      // const parent = 'abc123'
      /**
       *  Optional. The maximum number of resources to return.
       *  If unspecified, at most 50 resources will be returned.
       *  The maximum value is 200; (higher values will be coerced to the maximum)
       */
      // const pageSize = 1234
      /**
       *  Optional. A page token, received from a previous `ListConversionEvents`
       *  call. Provide this to retrieve the subsequent page. When paginating, all
       *  other parameters provided to `ListConversionEvents` must match the call
       *  that provided the page token.
       */
      // const pageToken = 'abc123'
    
      // Imports the Admin library
      const {AnalyticsAdminServiceClient} = require('[@google-analytics/admin](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const adminClient = new [AnalyticsAdminServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)();
    
      async function callListConversionEvents() {
        // Construct request
        const request = {
          parent,
        };
    
        // Run request
        const iterable = adminClient.listConversionEventsAsync(request);
        for await (const response of iterable) {
            console.log(response);
        }
      }
    
      callListConversionEvents();
    
    

### listConversionEventsStream(request, options)
    
    
    listConversionEventsStream(request?: protos.google.analytics.admin.v1beta.IListConversionEventsRequest, options?: CallOptions): Transform;

Equivalent to `listConversionEvents`, but returns a NodeJS Stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListConversionEventsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ilistconversioneventsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Transform` | {Stream} An object stream which emits an object representing on 'data' event. The client library will perform auto-pagination by default: it will call the API as many times as needed. Note that it can affect your quota. We recommend using `listConversionEventsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listCustomDimensions(request, options)
    
    
    listCustomDimensions(request?: protos.google.analytics.admin.v1beta.IListCustomDimensionsRequest, options?: CallOptions): Promise<[
            protos.google.analytics.admin.v1beta.ICustomDimension[],
            protos.google.analytics.admin.v1beta.IListCustomDimensionsRequest | null,
            protos.google.analytics.admin.v1beta.IListCustomDimensionsResponse
        ]>;

Lists CustomDimensions on a property.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListCustomDimensionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ilistcustomdimensionsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.analytics.admin.v1beta.ICustomDimension](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.icustomdimension)[], [protos.google.analytics.admin.v1beta.IListCustomDimensionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ilistcustomdimensionsrequest) | null, [protos.google.analytics.admin.v1beta.IListCustomDimensionsResponse](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ilistcustomdimensionsresponse) ]>` | {Promise} - The promise which resolves to an array. The first element of the array is Array of . The client library will perform auto-pagination by default: it will call the API as many times as needed and will merge results from all the pages into this array. Note that it can affect your quota. We recommend using `listCustomDimensionsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listCustomDimensions(request, options, callback)
    
    
    listCustomDimensions(request: protos.google.analytics.admin.v1beta.IListCustomDimensionsRequest, options: CallOptions, callback: PaginationCallback<protos.google.analytics.admin.v1beta.IListCustomDimensionsRequest, protos.google.analytics.admin.v1beta.IListCustomDimensionsResponse | null | undefined, protos.google.analytics.admin.v1beta.ICustomDimension>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListCustomDimensionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ilistcustomdimensionsrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `PaginationCallback<[protos.google.analytics.admin.v1beta.IListCustomDimensionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ilistcustomdimensionsrequest), [protos.google.analytics.admin.v1beta.IListCustomDimensionsResponse](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ilistcustomdimensionsresponse) | null | undefined, [protos.google.analytics.admin.v1beta.ICustomDimension](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.icustomdimension)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listCustomDimensions(request, callback)
    
    
    listCustomDimensions(request: protos.google.analytics.admin.v1beta.IListCustomDimensionsRequest, callback: PaginationCallback<protos.google.analytics.admin.v1beta.IListCustomDimensionsRequest, protos.google.analytics.admin.v1beta.IListCustomDimensionsResponse | null | undefined, protos.google.analytics.admin.v1beta.ICustomDimension>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListCustomDimensionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ilistcustomdimensionsrequest)`   
  
`callback` |  `PaginationCallback<[protos.google.analytics.admin.v1beta.IListCustomDimensionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ilistcustomdimensionsrequest), [protos.google.analytics.admin.v1beta.IListCustomDimensionsResponse](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ilistcustomdimensionsresponse) | null | undefined, [protos.google.analytics.admin.v1beta.ICustomDimension](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.icustomdimension)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listCustomDimensionsAsync(request, options)
    
    
    listCustomDimensionsAsync(request?: protos.google.analytics.admin.v1beta.IListCustomDimensionsRequest, options?: CallOptions): AsyncIterable<protos.google.analytics.admin.v1beta.ICustomDimension>;

Equivalent to `listCustomDimensions`, but returns an iterable object.

`for`-`await`-`of` syntax is used with the iterable to get response elements on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListCustomDimensionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ilistcustomdimensionsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.analytics.admin.v1beta.ICustomDimension](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.icustomdimension)>` | {Object} An iterable Object that allows [async iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols). When you iterate the returned iterable, each element will be an object representing . The API will be called under the hood as needed, once per the page, so you can stop the iteration when you don't need more results. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Example format: properties/1234
       */
      // const parent = 'abc123'
      /**
       *  Optional. The maximum number of resources to return.
       *  If unspecified, at most 50 resources will be returned.
       *  The maximum value is 200 (higher values will be coerced to the maximum).
       */
      // const pageSize = 1234
      /**
       *  Optional. A page token, received from a previous `ListCustomDimensions`
       *  call. Provide this to retrieve the subsequent page.
       *  When paginating, all other parameters provided to `ListCustomDimensions`
       *  must match the call that provided the page token.
       */
      // const pageToken = 'abc123'
    
      // Imports the Admin library
      const {AnalyticsAdminServiceClient} = require('[@google-analytics/admin](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const adminClient = new [AnalyticsAdminServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)();
    
      async function callListCustomDimensions() {
        // Construct request
        const request = {
          parent,
        };
    
        // Run request
        const iterable = adminClient.listCustomDimensionsAsync(request);
        for await (const response of iterable) {
            console.log(response);
        }
      }
    
      callListCustomDimensions();
    
    

### listCustomDimensionsStream(request, options)
    
    
    listCustomDimensionsStream(request?: protos.google.analytics.admin.v1beta.IListCustomDimensionsRequest, options?: CallOptions): Transform;

Equivalent to `listCustomDimensions`, but returns a NodeJS Stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListCustomDimensionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ilistcustomdimensionsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Transform` | {Stream} An object stream which emits an object representing on 'data' event. The client library will perform auto-pagination by default: it will call the API as many times as needed. Note that it can affect your quota. We recommend using `listCustomDimensionsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listCustomMetrics(request, options)
    
    
    listCustomMetrics(request?: protos.google.analytics.admin.v1beta.IListCustomMetricsRequest, options?: CallOptions): Promise<[
            protos.google.analytics.admin.v1beta.ICustomMetric[],
            protos.google.analytics.admin.v1beta.IListCustomMetricsRequest | null,
            protos.google.analytics.admin.v1beta.IListCustomMetricsResponse
        ]>;

Lists CustomMetrics on a property.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListCustomMetricsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ilistcustommetricsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.analytics.admin.v1beta.ICustomMetric](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.icustommetric)[], [protos.google.analytics.admin.v1beta.IListCustomMetricsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ilistcustommetricsrequest) | null, [protos.google.analytics.admin.v1beta.IListCustomMetricsResponse](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ilistcustommetricsresponse) ]>` | {Promise} - The promise which resolves to an array. The first element of the array is Array of . The client library will perform auto-pagination by default: it will call the API as many times as needed and will merge results from all the pages into this array. Note that it can affect your quota. We recommend using `listCustomMetricsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listCustomMetrics(request, options, callback)
    
    
    listCustomMetrics(request: protos.google.analytics.admin.v1beta.IListCustomMetricsRequest, options: CallOptions, callback: PaginationCallback<protos.google.analytics.admin.v1beta.IListCustomMetricsRequest, protos.google.analytics.admin.v1beta.IListCustomMetricsResponse | null | undefined, protos.google.analytics.admin.v1beta.ICustomMetric>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListCustomMetricsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ilistcustommetricsrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `PaginationCallback<[protos.google.analytics.admin.v1beta.IListCustomMetricsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ilistcustommetricsrequest), [protos.google.analytics.admin.v1beta.IListCustomMetricsResponse](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ilistcustommetricsresponse) | null | undefined, [protos.google.analytics.admin.v1beta.ICustomMetric](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.icustommetric)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listCustomMetrics(request, callback)
    
    
    listCustomMetrics(request: protos.google.analytics.admin.v1beta.IListCustomMetricsRequest, callback: PaginationCallback<protos.google.analytics.admin.v1beta.IListCustomMetricsRequest, protos.google.analytics.admin.v1beta.IListCustomMetricsResponse | null | undefined, protos.google.analytics.admin.v1beta.ICustomMetric>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListCustomMetricsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ilistcustommetricsrequest)`   
  
`callback` |  `PaginationCallback<[protos.google.analytics.admin.v1beta.IListCustomMetricsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ilistcustommetricsrequest), [protos.google.analytics.admin.v1beta.IListCustomMetricsResponse](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ilistcustommetricsresponse) | null | undefined, [protos.google.analytics.admin.v1beta.ICustomMetric](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.icustommetric)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listCustomMetricsAsync(request, options)
    
    
    listCustomMetricsAsync(request?: protos.google.analytics.admin.v1beta.IListCustomMetricsRequest, options?: CallOptions): AsyncIterable<protos.google.analytics.admin.v1beta.ICustomMetric>;

Equivalent to `listCustomMetrics`, but returns an iterable object.

`for`-`await`-`of` syntax is used with the iterable to get response elements on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListCustomMetricsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ilistcustommetricsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.analytics.admin.v1beta.ICustomMetric](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.icustommetric)>` | {Object} An iterable Object that allows [async iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols). When you iterate the returned iterable, each element will be an object representing . The API will be called under the hood as needed, once per the page, so you can stop the iteration when you don't need more results. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Example format: properties/1234
       */
      // const parent = 'abc123'
      /**
       *  The maximum number of resources to return.
       *  If unspecified, at most 50 resources will be returned.
       *  The maximum value is 200 (higher values will be coerced to the maximum).
       */
      // const pageSize = 1234
      /**
       *  A page token, received from a previous `ListCustomMetrics` call.
       *  Provide this to retrieve the subsequent page.
       *  When paginating, all other parameters provided to `ListCustomMetrics` must
       *  match the call that provided the page token.
       */
      // const pageToken = 'abc123'
    
      // Imports the Admin library
      const {AnalyticsAdminServiceClient} = require('[@google-analytics/admin](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const adminClient = new [AnalyticsAdminServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)();
    
      async function callListCustomMetrics() {
        // Construct request
        const request = {
          parent,
        };
    
        // Run request
        const iterable = adminClient.listCustomMetricsAsync(request);
        for await (const response of iterable) {
            console.log(response);
        }
      }
    
      callListCustomMetrics();
    
    

### listCustomMetricsStream(request, options)
    
    
    listCustomMetricsStream(request?: protos.google.analytics.admin.v1beta.IListCustomMetricsRequest, options?: CallOptions): Transform;

Equivalent to `listCustomMetrics`, but returns a NodeJS Stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListCustomMetricsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ilistcustommetricsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Transform` | {Stream} An object stream which emits an object representing on 'data' event. The client library will perform auto-pagination by default: it will call the API as many times as needed. Note that it can affect your quota. We recommend using `listCustomMetricsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listDataStreams(request, options)
    
    
    listDataStreams(request?: protos.google.analytics.admin.v1beta.IListDataStreamsRequest, options?: CallOptions): Promise<[
            protos.google.analytics.admin.v1beta.IDataStream[],
            protos.google.analytics.admin.v1beta.IListDataStreamsRequest | null,
            protos.google.analytics.admin.v1beta.IListDataStreamsResponse
        ]>;

Lists DataStreams on a property.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListDataStreamsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ilistdatastreamsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.analytics.admin.v1beta.IDataStream](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.idatastream)[], [protos.google.analytics.admin.v1beta.IListDataStreamsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ilistdatastreamsrequest) | null, [protos.google.analytics.admin.v1beta.IListDataStreamsResponse](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ilistdatastreamsresponse) ]>` | {Promise} - The promise which resolves to an array. The first element of the array is Array of . The client library will perform auto-pagination by default: it will call the API as many times as needed and will merge results from all the pages into this array. Note that it can affect your quota. We recommend using `listDataStreamsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listDataStreams(request, options, callback)
    
    
    listDataStreams(request: protos.google.analytics.admin.v1beta.IListDataStreamsRequest, options: CallOptions, callback: PaginationCallback<protos.google.analytics.admin.v1beta.IListDataStreamsRequest, protos.google.analytics.admin.v1beta.IListDataStreamsResponse | null | undefined, protos.google.analytics.admin.v1beta.IDataStream>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListDataStreamsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ilistdatastreamsrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `PaginationCallback<[protos.google.analytics.admin.v1beta.IListDataStreamsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ilistdatastreamsrequest), [protos.google.analytics.admin.v1beta.IListDataStreamsResponse](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ilistdatastreamsresponse) | null | undefined, [protos.google.analytics.admin.v1beta.IDataStream](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.idatastream)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listDataStreams(request, callback)
    
    
    listDataStreams(request: protos.google.analytics.admin.v1beta.IListDataStreamsRequest, callback: PaginationCallback<protos.google.analytics.admin.v1beta.IListDataStreamsRequest, protos.google.analytics.admin.v1beta.IListDataStreamsResponse | null | undefined, protos.google.analytics.admin.v1beta.IDataStream>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListDataStreamsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ilistdatastreamsrequest)`   
  
`callback` |  `PaginationCallback<[protos.google.analytics.admin.v1beta.IListDataStreamsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ilistdatastreamsrequest), [protos.google.analytics.admin.v1beta.IListDataStreamsResponse](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ilistdatastreamsresponse) | null | undefined, [protos.google.analytics.admin.v1beta.IDataStream](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.idatastream)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listDataStreamsAsync(request, options)
    
    
    listDataStreamsAsync(request?: protos.google.analytics.admin.v1beta.IListDataStreamsRequest, options?: CallOptions): AsyncIterable<protos.google.analytics.admin.v1beta.IDataStream>;

Equivalent to `listDataStreams`, but returns an iterable object.

`for`-`await`-`of` syntax is used with the iterable to get response elements on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListDataStreamsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ilistdatastreamsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.analytics.admin.v1beta.IDataStream](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.idatastream)>` | {Object} An iterable Object that allows [async iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols). When you iterate the returned iterable, each element will be an object representing . The API will be called under the hood as needed, once per the page, so you can stop the iteration when you don't need more results. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Example format: properties/1234
       */
      // const parent = 'abc123'
      /**
       *  The maximum number of resources to return.
       *  If unspecified, at most 50 resources will be returned.
       *  The maximum value is 200 (higher values will be coerced to the maximum).
       */
      // const pageSize = 1234
      /**
       *  A page token, received from a previous `ListDataStreams` call.
       *  Provide this to retrieve the subsequent page.
       *  When paginating, all other parameters provided to `ListDataStreams` must
       *  match the call that provided the page token.
       */
      // const pageToken = 'abc123'
    
      // Imports the Admin library
      const {AnalyticsAdminServiceClient} = require('[@google-analytics/admin](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const adminClient = new [AnalyticsAdminServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)();
    
      async function callListDataStreams() {
        // Construct request
        const request = {
          parent,
        };
    
        // Run request
        const iterable = adminClient.listDataStreamsAsync(request);
        for await (const response of iterable) {
            console.log(response);
        }
      }
    
      callListDataStreams();
    
    

### listDataStreamsStream(request, options)
    
    
    listDataStreamsStream(request?: protos.google.analytics.admin.v1beta.IListDataStreamsRequest, options?: CallOptions): Transform;

Equivalent to `listDataStreams`, but returns a NodeJS Stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListDataStreamsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ilistdatastreamsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Transform` | {Stream} An object stream which emits an object representing on 'data' event. The client library will perform auto-pagination by default: it will call the API as many times as needed. Note that it can affect your quota. We recommend using `listDataStreamsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listFirebaseLinks(request, options)
    
    
    listFirebaseLinks(request?: protos.google.analytics.admin.v1beta.IListFirebaseLinksRequest, options?: CallOptions): Promise<[
            protos.google.analytics.admin.v1beta.IFirebaseLink[],
            protos.google.analytics.admin.v1beta.IListFirebaseLinksRequest | null,
            protos.google.analytics.admin.v1beta.IListFirebaseLinksResponse
        ]>;

Lists FirebaseLinks on a property. Properties can have at most one FirebaseLink.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListFirebaseLinksRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ilistfirebaselinksrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.analytics.admin.v1beta.IFirebaseLink](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ifirebaselink)[], [protos.google.analytics.admin.v1beta.IListFirebaseLinksRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ilistfirebaselinksrequest) | null, [protos.google.analytics.admin.v1beta.IListFirebaseLinksResponse](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ilistfirebaselinksresponse) ]>` | {Promise} - The promise which resolves to an array. The first element of the array is Array of [FirebaseLink](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.firebaselink). The client library will perform auto-pagination by default: it will call the API as many times as needed and will merge results from all the pages into this array. Note that it can affect your quota. We recommend using `listFirebaseLinksAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listFirebaseLinks(request, options, callback)
    
    
    listFirebaseLinks(request: protos.google.analytics.admin.v1beta.IListFirebaseLinksRequest, options: CallOptions, callback: PaginationCallback<protos.google.analytics.admin.v1beta.IListFirebaseLinksRequest, protos.google.analytics.admin.v1beta.IListFirebaseLinksResponse | null | undefined, protos.google.analytics.admin.v1beta.IFirebaseLink>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListFirebaseLinksRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ilistfirebaselinksrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `PaginationCallback<[protos.google.analytics.admin.v1beta.IListFirebaseLinksRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ilistfirebaselinksrequest), [protos.google.analytics.admin.v1beta.IListFirebaseLinksResponse](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ilistfirebaselinksresponse) | null | undefined, [protos.google.analytics.admin.v1beta.IFirebaseLink](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ifirebaselink)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listFirebaseLinks(request, callback)
    
    
    listFirebaseLinks(request: protos.google.analytics.admin.v1beta.IListFirebaseLinksRequest, callback: PaginationCallback<protos.google.analytics.admin.v1beta.IListFirebaseLinksRequest, protos.google.analytics.admin.v1beta.IListFirebaseLinksResponse | null | undefined, protos.google.analytics.admin.v1beta.IFirebaseLink>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListFirebaseLinksRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ilistfirebaselinksrequest)`   
  
`callback` |  `PaginationCallback<[protos.google.analytics.admin.v1beta.IListFirebaseLinksRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ilistfirebaselinksrequest), [protos.google.analytics.admin.v1beta.IListFirebaseLinksResponse](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ilistfirebaselinksresponse) | null | undefined, [protos.google.analytics.admin.v1beta.IFirebaseLink](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ifirebaselink)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listFirebaseLinksAsync(request, options)
    
    
    listFirebaseLinksAsync(request?: protos.google.analytics.admin.v1beta.IListFirebaseLinksRequest, options?: CallOptions): AsyncIterable<protos.google.analytics.admin.v1beta.IFirebaseLink>;

Equivalent to `listFirebaseLinks`, but returns an iterable object.

`for`-`await`-`of` syntax is used with the iterable to get response elements on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListFirebaseLinksRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ilistfirebaselinksrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.analytics.admin.v1beta.IFirebaseLink](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ifirebaselink)>` | {Object} An iterable Object that allows [async iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols). When you iterate the returned iterable, each element will be an object representing [FirebaseLink](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.firebaselink). The API will be called under the hood as needed, once per the page, so you can stop the iteration when you don't need more results. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Format: properties/{property_id}
       *  Example: `properties/1234`
       */
      // const parent = 'abc123'
      /**
       *  Optional. The maximum number of resources to return. The service may return
       *  fewer than this value, even if there are additional pages.
       *  If unspecified, at most 50 resources will be returned.
       *  The maximum value is 200; (higher values will be coerced to the maximum)
       */
      // const pageSize = 1234
      /**
       *  Optional. A page token, received from a previous `ListFirebaseLinks` call.
       *  Provide this to retrieve the subsequent page.
       *  When paginating, all other parameters provided to `ListFirebaseLinks` must
       *  match the call that provided the page token.
       */
      // const pageToken = 'abc123'
    
      // Imports the Admin library
      const {AnalyticsAdminServiceClient} = require('[@google-analytics/admin](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const adminClient = new [AnalyticsAdminServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)();
    
      async function callListFirebaseLinks() {
        // Construct request
        const request = {
          parent,
        };
    
        // Run request
        const iterable = adminClient.listFirebaseLinksAsync(request);
        for await (const response of iterable) {
            console.log(response);
        }
      }
    
      callListFirebaseLinks();
    
    

### listFirebaseLinksStream(request, options)
    
    
    listFirebaseLinksStream(request?: protos.google.analytics.admin.v1beta.IListFirebaseLinksRequest, options?: CallOptions): Transform;

Equivalent to `listFirebaseLinks`, but returns a NodeJS Stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListFirebaseLinksRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ilistfirebaselinksrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Transform` | {Stream} An object stream which emits an object representing [FirebaseLink](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.firebaselink) on 'data' event. The client library will perform auto-pagination by default: it will call the API as many times as needed. Note that it can affect your quota. We recommend using `listFirebaseLinksAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listGoogleAdsLinks(request, options)
    
    
    listGoogleAdsLinks(request?: protos.google.analytics.admin.v1beta.IListGoogleAdsLinksRequest, options?: CallOptions): Promise<[
            protos.google.analytics.admin.v1beta.IGoogleAdsLink[],
            protos.google.analytics.admin.v1beta.IListGoogleAdsLinksRequest | null,
            protos.google.analytics.admin.v1beta.IListGoogleAdsLinksResponse
        ]>;

Lists GoogleAdsLinks on a property.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListGoogleAdsLinksRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ilistgoogleadslinksrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.analytics.admin.v1beta.IGoogleAdsLink](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.igoogleadslink)[], [protos.google.analytics.admin.v1beta.IListGoogleAdsLinksRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ilistgoogleadslinksrequest) | null, [protos.google.analytics.admin.v1beta.IListGoogleAdsLinksResponse](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ilistgoogleadslinksresponse) ]>` | {Promise} - The promise which resolves to an array. The first element of the array is Array of [GoogleAdsLink](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.googleadslink). The client library will perform auto-pagination by default: it will call the API as many times as needed and will merge results from all the pages into this array. Note that it can affect your quota. We recommend using `listGoogleAdsLinksAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listGoogleAdsLinks(request, options, callback)
    
    
    listGoogleAdsLinks(request: protos.google.analytics.admin.v1beta.IListGoogleAdsLinksRequest, options: CallOptions, callback: PaginationCallback<protos.google.analytics.admin.v1beta.IListGoogleAdsLinksRequest, protos.google.analytics.admin.v1beta.IListGoogleAdsLinksResponse | null | undefined, protos.google.analytics.admin.v1beta.IGoogleAdsLink>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListGoogleAdsLinksRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ilistgoogleadslinksrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `PaginationCallback<[protos.google.analytics.admin.v1beta.IListGoogleAdsLinksRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ilistgoogleadslinksrequest), [protos.google.analytics.admin.v1beta.IListGoogleAdsLinksResponse](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ilistgoogleadslinksresponse) | null | undefined, [protos.google.analytics.admin.v1beta.IGoogleAdsLink](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.igoogleadslink)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listGoogleAdsLinks(request, callback)
    
    
    listGoogleAdsLinks(request: protos.google.analytics.admin.v1beta.IListGoogleAdsLinksRequest, callback: PaginationCallback<protos.google.analytics.admin.v1beta.IListGoogleAdsLinksRequest, protos.google.analytics.admin.v1beta.IListGoogleAdsLinksResponse | null | undefined, protos.google.analytics.admin.v1beta.IGoogleAdsLink>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListGoogleAdsLinksRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ilistgoogleadslinksrequest)`   
  
`callback` |  `PaginationCallback<[protos.google.analytics.admin.v1beta.IListGoogleAdsLinksRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ilistgoogleadslinksrequest), [protos.google.analytics.admin.v1beta.IListGoogleAdsLinksResponse](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ilistgoogleadslinksresponse) | null | undefined, [protos.google.analytics.admin.v1beta.IGoogleAdsLink](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.igoogleadslink)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listGoogleAdsLinksAsync(request, options)
    
    
    listGoogleAdsLinksAsync(request?: protos.google.analytics.admin.v1beta.IListGoogleAdsLinksRequest, options?: CallOptions): AsyncIterable<protos.google.analytics.admin.v1beta.IGoogleAdsLink>;

Equivalent to `listGoogleAdsLinks`, but returns an iterable object.

`for`-`await`-`of` syntax is used with the iterable to get response elements on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListGoogleAdsLinksRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ilistgoogleadslinksrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.analytics.admin.v1beta.IGoogleAdsLink](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.igoogleadslink)>` | {Object} An iterable Object that allows [async iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols). When you iterate the returned iterable, each element will be an object representing [GoogleAdsLink](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.googleadslink). The API will be called under the hood as needed, once per the page, so you can stop the iteration when you don't need more results. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Example format: properties/1234
       */
      // const parent = 'abc123'
      /**
       *  Optional. The maximum number of resources to return.
       *  If unspecified, at most 50 resources will be returned.
       *  The maximum value is 200 (higher values will be coerced to the maximum).
       */
      // const pageSize = 1234
      /**
       *  Optional. A page token, received from a previous `ListGoogleAdsLinks` call.
       *  Provide this to retrieve the subsequent page.
       *  When paginating, all other parameters provided to `ListGoogleAdsLinks` must
       *  match the call that provided the page token.
       */
      // const pageToken = 'abc123'
    
      // Imports the Admin library
      const {AnalyticsAdminServiceClient} = require('[@google-analytics/admin](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const adminClient = new [AnalyticsAdminServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)();
    
      async function callListGoogleAdsLinks() {
        // Construct request
        const request = {
          parent,
        };
    
        // Run request
        const iterable = adminClient.listGoogleAdsLinksAsync(request);
        for await (const response of iterable) {
            console.log(response);
        }
      }
    
      callListGoogleAdsLinks();
    
    

### listGoogleAdsLinksStream(request, options)
    
    
    listGoogleAdsLinksStream(request?: protos.google.analytics.admin.v1beta.IListGoogleAdsLinksRequest, options?: CallOptions): Transform;

Equivalent to `listGoogleAdsLinks`, but returns a NodeJS Stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListGoogleAdsLinksRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ilistgoogleadslinksrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Transform` | {Stream} An object stream which emits an object representing [GoogleAdsLink](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.googleadslink) on 'data' event. The client library will perform auto-pagination by default: it will call the API as many times as needed. Note that it can affect your quota. We recommend using `listGoogleAdsLinksAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listKeyEvents(request, options)
    
    
    listKeyEvents(request?: protos.google.analytics.admin.v1beta.IListKeyEventsRequest, options?: CallOptions): Promise<[
            protos.google.analytics.admin.v1beta.IKeyEvent[],
            protos.google.analytics.admin.v1beta.IListKeyEventsRequest | null,
            protos.google.analytics.admin.v1beta.IListKeyEventsResponse
        ]>;

Returns a list of Key Events in the specified parent property. Returns an empty list if no Key Events are found.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListKeyEventsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ilistkeyeventsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.analytics.admin.v1beta.IKeyEvent](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ikeyevent)[], [protos.google.analytics.admin.v1beta.IListKeyEventsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ilistkeyeventsrequest) | null, [protos.google.analytics.admin.v1beta.IListKeyEventsResponse](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ilistkeyeventsresponse) ]>` | {Promise} - The promise which resolves to an array. The first element of the array is Array of . The client library will perform auto-pagination by default: it will call the API as many times as needed and will merge results from all the pages into this array. Note that it can affect your quota. We recommend using `listKeyEventsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listKeyEvents(request, options, callback)
    
    
    listKeyEvents(request: protos.google.analytics.admin.v1beta.IListKeyEventsRequest, options: CallOptions, callback: PaginationCallback<protos.google.analytics.admin.v1beta.IListKeyEventsRequest, protos.google.analytics.admin.v1beta.IListKeyEventsResponse | null | undefined, protos.google.analytics.admin.v1beta.IKeyEvent>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListKeyEventsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ilistkeyeventsrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `PaginationCallback<[protos.google.analytics.admin.v1beta.IListKeyEventsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ilistkeyeventsrequest), [protos.google.analytics.admin.v1beta.IListKeyEventsResponse](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ilistkeyeventsresponse) | null | undefined, [protos.google.analytics.admin.v1beta.IKeyEvent](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ikeyevent)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listKeyEvents(request, callback)
    
    
    listKeyEvents(request: protos.google.analytics.admin.v1beta.IListKeyEventsRequest, callback: PaginationCallback<protos.google.analytics.admin.v1beta.IListKeyEventsRequest, protos.google.analytics.admin.v1beta.IListKeyEventsResponse | null | undefined, protos.google.analytics.admin.v1beta.IKeyEvent>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListKeyEventsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ilistkeyeventsrequest)`   
  
`callback` |  `PaginationCallback<[protos.google.analytics.admin.v1beta.IListKeyEventsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ilistkeyeventsrequest), [protos.google.analytics.admin.v1beta.IListKeyEventsResponse](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ilistkeyeventsresponse) | null | undefined, [protos.google.analytics.admin.v1beta.IKeyEvent](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ikeyevent)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listKeyEventsAsync(request, options)
    
    
    listKeyEventsAsync(request?: protos.google.analytics.admin.v1beta.IListKeyEventsRequest, options?: CallOptions): AsyncIterable<protos.google.analytics.admin.v1beta.IKeyEvent>;

Equivalent to `listKeyEvents`, but returns an iterable object.

`for`-`await`-`of` syntax is used with the iterable to get response elements on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListKeyEventsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ilistkeyeventsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.analytics.admin.v1beta.IKeyEvent](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ikeyevent)>` | {Object} An iterable Object that allows [async iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols). When you iterate the returned iterable, each element will be an object representing . The API will be called under the hood as needed, once per the page, so you can stop the iteration when you don't need more results. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The resource name of the parent property.
       *  Example: 'properties/123'
       */
      // const parent = 'abc123'
      /**
       *  Optional. The maximum number of resources to return.
       *  If unspecified, at most 50 resources will be returned.
       *  The maximum value is 200; (higher values will be coerced to the maximum)
       */
      // const pageSize = 1234
      /**
       *  Optional. A page token, received from a previous `ListKeyEvents` call.
       *  Provide this to retrieve the subsequent page.
       *  When paginating, all other parameters provided to `ListKeyEvents`
       *  must match the call that provided the page token.
       */
      // const pageToken = 'abc123'
    
      // Imports the Admin library
      const {AnalyticsAdminServiceClient} = require('[@google-analytics/admin](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const adminClient = new [AnalyticsAdminServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)();
    
      async function callListKeyEvents() {
        // Construct request
        const request = {
          parent,
        };
    
        // Run request
        const iterable = adminClient.listKeyEventsAsync(request);
        for await (const response of iterable) {
            console.log(response);
        }
      }
    
      callListKeyEvents();
    
    

### listKeyEventsStream(request, options)
    
    
    listKeyEventsStream(request?: protos.google.analytics.admin.v1beta.IListKeyEventsRequest, options?: CallOptions): Transform;

Equivalent to `listKeyEvents`, but returns a NodeJS Stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListKeyEventsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ilistkeyeventsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Transform` | {Stream} An object stream which emits an object representing on 'data' event. The client library will perform auto-pagination by default: it will call the API as many times as needed. Note that it can affect your quota. We recommend using `listKeyEventsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listMeasurementProtocolSecrets(request, options)
    
    
    listMeasurementProtocolSecrets(request?: protos.google.analytics.admin.v1beta.IListMeasurementProtocolSecretsRequest, options?: CallOptions): Promise<[
            protos.google.analytics.admin.v1beta.IMeasurementProtocolSecret[],
            protos.google.analytics.admin.v1beta.IListMeasurementProtocolSecretsRequest | null,
            protos.google.analytics.admin.v1beta.IListMeasurementProtocolSecretsResponse
        ]>;

Returns child MeasurementProtocolSecrets under the specified parent Property.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListMeasurementProtocolSecretsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ilistmeasurementprotocolsecretsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.analytics.admin.v1beta.IMeasurementProtocolSecret](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.imeasurementprotocolsecret)[], [protos.google.analytics.admin.v1beta.IListMeasurementProtocolSecretsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ilistmeasurementprotocolsecretsrequest) | null, [protos.google.analytics.admin.v1beta.IListMeasurementProtocolSecretsResponse](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ilistmeasurementprotocolsecretsresponse) ]>` | {Promise} - The promise which resolves to an array. The first element of the array is Array of [MeasurementProtocolSecret](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.measurementprotocolsecret). The client library will perform auto-pagination by default: it will call the API as many times as needed and will merge results from all the pages into this array. Note that it can affect your quota. We recommend using `listMeasurementProtocolSecretsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listMeasurementProtocolSecrets(request, options, callback)
    
    
    listMeasurementProtocolSecrets(request: protos.google.analytics.admin.v1beta.IListMeasurementProtocolSecretsRequest, options: CallOptions, callback: PaginationCallback<protos.google.analytics.admin.v1beta.IListMeasurementProtocolSecretsRequest, protos.google.analytics.admin.v1beta.IListMeasurementProtocolSecretsResponse | null | undefined, protos.google.analytics.admin.v1beta.IMeasurementProtocolSecret>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListMeasurementProtocolSecretsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ilistmeasurementprotocolsecretsrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `PaginationCallback<[protos.google.analytics.admin.v1beta.IListMeasurementProtocolSecretsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ilistmeasurementprotocolsecretsrequest), [protos.google.analytics.admin.v1beta.IListMeasurementProtocolSecretsResponse](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ilistmeasurementprotocolsecretsresponse) | null | undefined, [protos.google.analytics.admin.v1beta.IMeasurementProtocolSecret](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.imeasurementprotocolsecret)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listMeasurementProtocolSecrets(request, callback)
    
    
    listMeasurementProtocolSecrets(request: protos.google.analytics.admin.v1beta.IListMeasurementProtocolSecretsRequest, callback: PaginationCallback<protos.google.analytics.admin.v1beta.IListMeasurementProtocolSecretsRequest, protos.google.analytics.admin.v1beta.IListMeasurementProtocolSecretsResponse | null | undefined, protos.google.analytics.admin.v1beta.IMeasurementProtocolSecret>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListMeasurementProtocolSecretsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ilistmeasurementprotocolsecretsrequest)`   
  
`callback` |  `PaginationCallback<[protos.google.analytics.admin.v1beta.IListMeasurementProtocolSecretsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ilistmeasurementprotocolsecretsrequest), [protos.google.analytics.admin.v1beta.IListMeasurementProtocolSecretsResponse](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ilistmeasurementprotocolsecretsresponse) | null | undefined, [protos.google.analytics.admin.v1beta.IMeasurementProtocolSecret](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.imeasurementprotocolsecret)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listMeasurementProtocolSecretsAsync(request, options)
    
    
    listMeasurementProtocolSecretsAsync(request?: protos.google.analytics.admin.v1beta.IListMeasurementProtocolSecretsRequest, options?: CallOptions): AsyncIterable<protos.google.analytics.admin.v1beta.IMeasurementProtocolSecret>;

Equivalent to `listMeasurementProtocolSecrets`, but returns an iterable object.

`for`-`await`-`of` syntax is used with the iterable to get response elements on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListMeasurementProtocolSecretsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ilistmeasurementprotocolsecretsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.analytics.admin.v1beta.IMeasurementProtocolSecret](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.imeasurementprotocolsecret)>` | {Object} An iterable Object that allows [async iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols). When you iterate the returned iterable, each element will be an object representing [MeasurementProtocolSecret](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.measurementprotocolsecret). The API will be called under the hood as needed, once per the page, so you can stop the iteration when you don't need more results. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The resource name of the parent stream.
       *  Format:
       *  properties/{property}/dataStreams/{dataStream}/measurementProtocolSecrets
       */
      // const parent = 'abc123'
      /**
       *  Optional. The maximum number of resources to return.
       *  If unspecified, at most 10 resources will be returned.
       *  The maximum value is 10. Higher values will be coerced to the maximum.
       */
      // const pageSize = 1234
      /**
       *  Optional. A page token, received from a previous
       *  `ListMeasurementProtocolSecrets` call. Provide this to retrieve the
       *  subsequent page. When paginating, all other parameters provided to
       *  `ListMeasurementProtocolSecrets` must match the call that provided the page
       *  token.
       */
      // const pageToken = 'abc123'
    
      // Imports the Admin library
      const {AnalyticsAdminServiceClient} = require('[@google-analytics/admin](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const adminClient = new [AnalyticsAdminServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)();
    
      async function callListMeasurementProtocolSecrets() {
        // Construct request
        const request = {
          parent,
        };
    
        // Run request
        const iterable = adminClient.listMeasurementProtocolSecretsAsync(request);
        for await (const response of iterable) {
            console.log(response);
        }
      }
    
      callListMeasurementProtocolSecrets();
    
    

### listMeasurementProtocolSecretsStream(request, options)
    
    
    listMeasurementProtocolSecretsStream(request?: protos.google.analytics.admin.v1beta.IListMeasurementProtocolSecretsRequest, options?: CallOptions): Transform;

Equivalent to `listMeasurementProtocolSecrets`, but returns a NodeJS Stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListMeasurementProtocolSecretsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ilistmeasurementprotocolsecretsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Transform` | {Stream} An object stream which emits an object representing [MeasurementProtocolSecret](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.measurementprotocolsecret) on 'data' event. The client library will perform auto-pagination by default: it will call the API as many times as needed. Note that it can affect your quota. We recommend using `listMeasurementProtocolSecretsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listProperties(request, options)
    
    
    listProperties(request?: protos.google.analytics.admin.v1beta.IListPropertiesRequest, options?: CallOptions): Promise<[
            protos.google.analytics.admin.v1beta.IProperty[],
            protos.google.analytics.admin.v1beta.IListPropertiesRequest | null,
            protos.google.analytics.admin.v1beta.IListPropertiesResponse
        ]>;

Returns child Properties under the specified parent Account.

Properties will be excluded if the caller does not have access. Soft-deleted (ie: "trashed") properties are excluded by default. Returns an empty list if no relevant properties are found.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListPropertiesRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ilistpropertiesrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.analytics.admin.v1beta.IProperty](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.iproperty)[], [protos.google.analytics.admin.v1beta.IListPropertiesRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ilistpropertiesrequest) | null, [protos.google.analytics.admin.v1beta.IListPropertiesResponse](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ilistpropertiesresponse) ]>` | {Promise} - The promise which resolves to an array. The first element of the array is Array of [Property](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.property). The client library will perform auto-pagination by default: it will call the API as many times as needed and will merge results from all the pages into this array. Note that it can affect your quota. We recommend using `listPropertiesAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listProperties(request, options, callback)
    
    
    listProperties(request: protos.google.analytics.admin.v1beta.IListPropertiesRequest, options: CallOptions, callback: PaginationCallback<protos.google.analytics.admin.v1beta.IListPropertiesRequest, protos.google.analytics.admin.v1beta.IListPropertiesResponse | null | undefined, protos.google.analytics.admin.v1beta.IProperty>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListPropertiesRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ilistpropertiesrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `PaginationCallback<[protos.google.analytics.admin.v1beta.IListPropertiesRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ilistpropertiesrequest), [protos.google.analytics.admin.v1beta.IListPropertiesResponse](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ilistpropertiesresponse) | null | undefined, [protos.google.analytics.admin.v1beta.IProperty](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.iproperty)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listProperties(request, callback)
    
    
    listProperties(request: protos.google.analytics.admin.v1beta.IListPropertiesRequest, callback: PaginationCallback<protos.google.analytics.admin.v1beta.IListPropertiesRequest, protos.google.analytics.admin.v1beta.IListPropertiesResponse | null | undefined, protos.google.analytics.admin.v1beta.IProperty>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListPropertiesRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ilistpropertiesrequest)`   
  
`callback` |  `PaginationCallback<[protos.google.analytics.admin.v1beta.IListPropertiesRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ilistpropertiesrequest), [protos.google.analytics.admin.v1beta.IListPropertiesResponse](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ilistpropertiesresponse) | null | undefined, [protos.google.analytics.admin.v1beta.IProperty](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.iproperty)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listPropertiesAsync(request, options)
    
    
    listPropertiesAsync(request?: protos.google.analytics.admin.v1beta.IListPropertiesRequest, options?: CallOptions): AsyncIterable<protos.google.analytics.admin.v1beta.IProperty>;

Equivalent to `listProperties`, but returns an iterable object.

`for`-`await`-`of` syntax is used with the iterable to get response elements on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListPropertiesRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ilistpropertiesrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.analytics.admin.v1beta.IProperty](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.iproperty)>` | {Object} An iterable Object that allows [async iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols). When you iterate the returned iterable, each element will be an object representing [Property](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.property). The API will be called under the hood as needed, once per the page, so you can stop the iteration when you don't need more results. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. An expression for filtering the results of the request.
       *  Fields eligible for filtering are:
       *  `parent:`(The resource name of the parent account/property) or
       *  `ancestor:`(The resource name of the parent account) or
       *  `firebase_project:`(The id or number of the linked firebase project).
       *  Some examples of filters:
       *  
    
    
       *  | Filter                      | Description                               |
       *  |-----------------------------|-------------------------------------------|
       *  | parent:accounts/123         | The account with account id: 123.       |
       *  | parent:properties/123       | The property with property id: 123.       |
       *  | ancestor:accounts/123       | The account with account id: 123.         |
       *  | firebase_project:project-id | The firebase project with id: project-id. |
       *  | firebase_project:123        | The firebase project with number: 123.    |
       *  

`

_/ // const filter = 'abc123' /_ *

  * Optional. The maximum number of resources to return. The service may return
  * fewer than this value, even if there are additional pages.
  * If unspecified, at most 50 resources will be returned.
  * The maximum value is 200; (higher values will be coerced to the maximum) _/ // const pageSize = 1234 /_ *
  * Optional. A page token, received from a previous `ListProperties` call.
  * Provide this to retrieve the subsequent page.
  * When paginating, all other parameters provided to `ListProperties` must
  * match the call that provided the page token. _/ // const pageToken = 'abc123' /_ *
  * Whether to include soft-deleted (ie: "trashed") Properties in the
  * results. Properties can be inspected to determine whether they are deleted
  * or not. */ // const showDeleted = true

// Imports the Admin library const {AnalyticsAdminServiceClient} = require('@google-analytics/admin').v1beta;

// Instantiates a client const adminClient = new AnalyticsAdminServiceClient();

async function callListProperties() { // Construct request const request = { filter, };

// Run request const iterable = adminClient.listPropertiesAsync(request); for await (const response of iterable) { console.log(response); } }

callListProperties();




``

### listPropertiesStream(request, options)
    
    
    listPropertiesStream(request?: protos.google.analytics.admin.v1beta.IListPropertiesRequest, options?: CallOptions): Transform;

Equivalent to `listProperties`, but returns a NodeJS Stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListPropertiesRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ilistpropertiesrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Transform` | {Stream} An object stream which emits an object representing [Property](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.property) on 'data' event. The client library will perform auto-pagination by default: it will call the API as many times as needed. Note that it can affect your quota. We recommend using `listPropertiesAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### matchAccountFromAccountName(accountName)
    
    
    matchAccountFromAccountName(accountName: string): string | number;

Parse the account from Account resource.

**Parameter**  
---  
**Name** | **Description**  
`accountName` |  `string`   
A fully-qualified path representing Account resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the account.  
  
### matchAccountFromDataSharingSettingsName(dataSharingSettingsName)
    
    
    matchAccountFromDataSharingSettingsName(dataSharingSettingsName: string): string | number;

Parse the account from DataSharingSettings resource.

**Parameter**  
---  
**Name** | **Description**  
`dataSharingSettingsName` |  `string`   
A fully-qualified path representing DataSharingSettings resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the account.  
  
### matchAccountSummaryFromAccountSummaryName(accountSummaryName)
    
    
    matchAccountSummaryFromAccountSummaryName(accountSummaryName: string): string | number;

Parse the account_summary from AccountSummary resource.

**Parameter**  
---  
**Name** | **Description**  
`accountSummaryName` |  `string`   
A fully-qualified path representing AccountSummary resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the account_summary.  
  
### matchConversionEventFromConversionEventName(conversionEventName)
    
    
    matchConversionEventFromConversionEventName(conversionEventName: string): string | number;

Parse the conversion_event from ConversionEvent resource.

**Parameter**  
---  
**Name** | **Description**  
`conversionEventName` |  `string`   
A fully-qualified path representing ConversionEvent resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the conversion_event.  
  
### matchCustomDimensionFromCustomDimensionName(customDimensionName)
    
    
    matchCustomDimensionFromCustomDimensionName(customDimensionName: string): string | number;

Parse the custom_dimension from CustomDimension resource.

**Parameter**  
---  
**Name** | **Description**  
`customDimensionName` |  `string`   
A fully-qualified path representing CustomDimension resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the custom_dimension.  
  
### matchCustomMetricFromCustomMetricName(customMetricName)
    
    
    matchCustomMetricFromCustomMetricName(customMetricName: string): string | number;

Parse the custom_metric from CustomMetric resource.

**Parameter**  
---  
**Name** | **Description**  
`customMetricName` |  `string`   
A fully-qualified path representing CustomMetric resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the custom_metric.  
  
### matchDataStreamFromDataStreamName(dataStreamName)
    
    
    matchDataStreamFromDataStreamName(dataStreamName: string): string | number;

Parse the data_stream from DataStream resource.

**Parameter**  
---  
**Name** | **Description**  
`dataStreamName` |  `string`   
A fully-qualified path representing DataStream resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the data_stream.  
  
### matchDataStreamFromMeasurementProtocolSecretName(measurementProtocolSecretName)
    
    
    matchDataStreamFromMeasurementProtocolSecretName(measurementProtocolSecretName: string): string | number;

Parse the data_stream from MeasurementProtocolSecret resource.

**Parameter**  
---  
**Name** | **Description**  
`measurementProtocolSecretName` |  `string`   
A fully-qualified path representing MeasurementProtocolSecret resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the data_stream.  
  
### matchFirebaseLinkFromFirebaseLinkName(firebaseLinkName)
    
    
    matchFirebaseLinkFromFirebaseLinkName(firebaseLinkName: string): string | number;

Parse the firebase_link from FirebaseLink resource.

**Parameter**  
---  
**Name** | **Description**  
`firebaseLinkName` |  `string`   
A fully-qualified path representing FirebaseLink resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the firebase_link.  
  
### matchGoogleAdsLinkFromGoogleAdsLinkName(googleAdsLinkName)
    
    
    matchGoogleAdsLinkFromGoogleAdsLinkName(googleAdsLinkName: string): string | number;

Parse the google_ads_link from GoogleAdsLink resource.

**Parameter**  
---  
**Name** | **Description**  
`googleAdsLinkName` |  `string`   
A fully-qualified path representing GoogleAdsLink resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the google_ads_link.  
  
### matchKeyEventFromKeyEventName(keyEventName)
    
    
    matchKeyEventFromKeyEventName(keyEventName: string): string | number;

Parse the key_event from KeyEvent resource.

**Parameter**  
---  
**Name** | **Description**  
`keyEventName` |  `string`   
A fully-qualified path representing KeyEvent resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the key_event.  
  
### matchMeasurementProtocolSecretFromMeasurementProtocolSecretName(measurementProtocolSecretName)
    
    
    matchMeasurementProtocolSecretFromMeasurementProtocolSecretName(measurementProtocolSecretName: string): string | number;

Parse the measurement_protocol_secret from MeasurementProtocolSecret resource.

**Parameter**  
---  
**Name** | **Description**  
`measurementProtocolSecretName` |  `string`   
A fully-qualified path representing MeasurementProtocolSecret resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the measurement_protocol_secret.  
  
### matchPropertyFromConversionEventName(conversionEventName)
    
    
    matchPropertyFromConversionEventName(conversionEventName: string): string | number;

Parse the property from ConversionEvent resource.

**Parameter**  
---  
**Name** | **Description**  
`conversionEventName` |  `string`   
A fully-qualified path representing ConversionEvent resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the property.  
  
### matchPropertyFromCustomDimensionName(customDimensionName)
    
    
    matchPropertyFromCustomDimensionName(customDimensionName: string): string | number;

Parse the property from CustomDimension resource.

**Parameter**  
---  
**Name** | **Description**  
`customDimensionName` |  `string`   
A fully-qualified path representing CustomDimension resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the property.  
  
### matchPropertyFromCustomMetricName(customMetricName)
    
    
    matchPropertyFromCustomMetricName(customMetricName: string): string | number;

Parse the property from CustomMetric resource.

**Parameter**  
---  
**Name** | **Description**  
`customMetricName` |  `string`   
A fully-qualified path representing CustomMetric resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the property.  
  
### matchPropertyFromDataRetentionSettingsName(dataRetentionSettingsName)
    
    
    matchPropertyFromDataRetentionSettingsName(dataRetentionSettingsName: string): string | number;

Parse the property from DataRetentionSettings resource.

**Parameter**  
---  
**Name** | **Description**  
`dataRetentionSettingsName` |  `string`   
A fully-qualified path representing DataRetentionSettings resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the property.  
  
### matchPropertyFromDataStreamName(dataStreamName)
    
    
    matchPropertyFromDataStreamName(dataStreamName: string): string | number;

Parse the property from DataStream resource.

**Parameter**  
---  
**Name** | **Description**  
`dataStreamName` |  `string`   
A fully-qualified path representing DataStream resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the property.  
  
### matchPropertyFromFirebaseLinkName(firebaseLinkName)
    
    
    matchPropertyFromFirebaseLinkName(firebaseLinkName: string): string | number;

Parse the property from FirebaseLink resource.

**Parameter**  
---  
**Name** | **Description**  
`firebaseLinkName` |  `string`   
A fully-qualified path representing FirebaseLink resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the property.  
  
### matchPropertyFromGoogleAdsLinkName(googleAdsLinkName)
    
    
    matchPropertyFromGoogleAdsLinkName(googleAdsLinkName: string): string | number;

Parse the property from GoogleAdsLink resource.

**Parameter**  
---  
**Name** | **Description**  
`googleAdsLinkName` |  `string`   
A fully-qualified path representing GoogleAdsLink resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the property.  
  
### matchPropertyFromKeyEventName(keyEventName)
    
    
    matchPropertyFromKeyEventName(keyEventName: string): string | number;

Parse the property from KeyEvent resource.

**Parameter**  
---  
**Name** | **Description**  
`keyEventName` |  `string`   
A fully-qualified path representing KeyEvent resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the property.  
  
### matchPropertyFromMeasurementProtocolSecretName(measurementProtocolSecretName)
    
    
    matchPropertyFromMeasurementProtocolSecretName(measurementProtocolSecretName: string): string | number;

Parse the property from MeasurementProtocolSecret resource.

**Parameter**  
---  
**Name** | **Description**  
`measurementProtocolSecretName` |  `string`   
A fully-qualified path representing MeasurementProtocolSecret resource.  
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
  
### measurementProtocolSecretPath(property, dataStream, measurementProtocolSecret)
    
    
    measurementProtocolSecretPath(property: string, dataStream: string, measurementProtocolSecret: string): string;

Return a fully-qualified measurementProtocolSecret resource name string.

**Parameters**  
---  
**Name** | **Description**  
`property` |  `string`   
  
`dataStream` |  `string`   
  
`measurementProtocolSecret` |  `string`   
  
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
  
### provisionAccountTicket(request, options)
    
    
    provisionAccountTicket(request?: protos.google.analytics.admin.v1beta.IProvisionAccountTicketRequest, options?: CallOptions): Promise<[
            protos.google.analytics.admin.v1beta.IProvisionAccountTicketResponse,
            (protos.google.analytics.admin.v1beta.IProvisionAccountTicketRequest | undefined),
            {} | undefined
        ]>;

Requests a ticket for creating an account.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IProvisionAccountTicketRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.iprovisionaccountticketrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.analytics.admin.v1beta.IProvisionAccountTicketResponse](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.iprovisionaccountticketresponse), ([protos.google.analytics.admin.v1beta.IProvisionAccountTicketRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.iprovisionaccountticketrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [ProvisionAccountTicketResponse](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.provisionaccountticketresponse). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  The account to create.
       */
      // const account = {}
      /**
       *  Redirect URI where the user will be sent after accepting Terms of Service.
       *  Must be configured in Cloud Console as a Redirect URI.
       */
      // const redirectUri = 'abc123'
    
      // Imports the Admin library
      const {AnalyticsAdminServiceClient} = require('[@google-analytics/admin](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const adminClient = new [AnalyticsAdminServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)();
    
      async function callProvisionAccountTicket() {
        // Construct request
        const request = {
        };
    
        // Run request
        const response = await adminClient.provisionAccountTicket(request);
        console.log(response);
      }
    
      callProvisionAccountTicket();
    
    

### provisionAccountTicket(request, options, callback)
    
    
    provisionAccountTicket(request: protos.google.analytics.admin.v1beta.IProvisionAccountTicketRequest, options: CallOptions, callback: Callback<protos.google.analytics.admin.v1beta.IProvisionAccountTicketResponse, protos.google.analytics.admin.v1beta.IProvisionAccountTicketRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IProvisionAccountTicketRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.iprovisionaccountticketrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.analytics.admin.v1beta.IProvisionAccountTicketResponse](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.iprovisionaccountticketresponse), [protos.google.analytics.admin.v1beta.IProvisionAccountTicketRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.iprovisionaccountticketrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### provisionAccountTicket(request, callback)
    
    
    provisionAccountTicket(request: protos.google.analytics.admin.v1beta.IProvisionAccountTicketRequest, callback: Callback<protos.google.analytics.admin.v1beta.IProvisionAccountTicketResponse, protos.google.analytics.admin.v1beta.IProvisionAccountTicketRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IProvisionAccountTicketRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.iprovisionaccountticketrequest)`   
  
`callback` |  `Callback<[protos.google.analytics.admin.v1beta.IProvisionAccountTicketResponse](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.iprovisionaccountticketresponse), [protos.google.analytics.admin.v1beta.IProvisionAccountTicketRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.iprovisionaccountticketrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### runAccessReport(request, options)
    
    
    runAccessReport(request?: protos.google.analytics.admin.v1beta.IRunAccessReportRequest, options?: CallOptions): Promise<[
            protos.google.analytics.admin.v1beta.IRunAccessReportResponse,
            protos.google.analytics.admin.v1beta.IRunAccessReportRequest | undefined,
            {} | undefined
        ]>;

Returns a customized report of data access records. The report provides records of each time a user reads Google Analytics reporting data. Access records are retained for up to 2 years.

Data Access Reports can be requested for a property. Reports may be requested for any property, but dimensions that aren't related to quota can only be requested on Google Analytics 360 properties. This method is only available to Administrators.

These data access records include GA UI Reporting, GA UI Explorations, GA Data API, and other products like Firebase & Admob that can retrieve data from Google Analytics through a linkage. These records don't include property configuration changes like adding a stream or changing a property's time zone. For configuration change history, see [searchChangeHistoryEvents](<https://developers.google.com/analytics/devguides/config/admin/v1/rest/v1alpha/accounts/searchChangeHistoryEvents>).

To give your feedback on this API, complete the [Google Analytics Access Reports feedback](<https://docs.google.com/forms/d/e/1FAIpQLSdmEBUrMzAEdiEKk5TV5dEHvDUZDRlgWYdQdAeSdtR4hVjEhw/viewform>) form.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IRunAccessReportRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.irunaccessreportrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.analytics.admin.v1beta.IRunAccessReportResponse](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.irunaccessreportresponse), [protos.google.analytics.admin.v1beta.IRunAccessReportRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.irunaccessreportrequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [RunAccessReportResponse](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.runaccessreportresponse). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  The Data Access Report supports requesting at the property level or account
       *  level. If requested at the account level, Data Access Reports include all
       *  access for all properties under that account.
       *  To request at the property level, entity should be for example
       *  'properties/123' if "123" is your Google Analytics property ID. To request
       *  at the account level, entity should be for example 'accounts/1234' if
       *  "1234" is your Google Analytics Account ID.
       */
      // const entity = 'abc123'
      /**
       *  The dimensions requested and displayed in the response. Requests are
       *  allowed up to 9 dimensions.
       */
      // const dimensions = [1,2,3,4]
      /**
       *  The metrics requested and displayed in the response. Requests are allowed
       *  up to 10 metrics.
       */
      // const metrics = [1,2,3,4]
      /**
       *  Date ranges of access records to read. If multiple date ranges are
       *  requested, each response row will contain a zero based date range index. If
       *  two date ranges overlap, the access records for the overlapping days is
       *  included in the response rows for both date ranges. Requests are allowed up
       *  to 2 date ranges.
       */
      // const dateRanges = [1,2,3,4]
      /**
       *  Dimension filters let you restrict report response to specific
       *  dimension values which match the filter. For example, filtering on access
       *  records of a single user. To learn more, see Fundamentals of Dimension
       *  Filters (https://developers.google.com/analytics/devguides/reporting/data/v1/basics#dimension_filters)
       *  for examples. Metrics cannot be used in this filter.
       */
      // const dimensionFilter = {}
      /**
       *  Metric filters allow you to restrict report response to specific metric
       *  values which match the filter. Metric filters are applied after aggregating
       *  the report's rows, similar to SQL having-clause. Dimensions cannot be used
       *  in this filter.
       */
      // const metricFilter = {}
      /**
       *  The row count of the start row. The first row is counted as row 0. If
       *  offset is unspecified, it is treated as 0. If offset is zero, then this
       *  method will return the first page of results with `limit` entries.
       *  To learn more about this pagination parameter, see
       *  Pagination (https://developers.google.com/analytics/devguides/reporting/data/v1/basics#pagination).
       */
      // const offset = 1234
      /**
       *  The number of rows to return. If unspecified, 10,000 rows are returned. The
       *  API returns a maximum of 100,000 rows per request, no matter how many you
       *  ask for. `limit` must be positive.
       *  The API may return fewer rows than the requested `limit`, if there aren't
       *  as many remaining rows as the `limit`. For instance, there are fewer than
       *  300 possible values for the dimension `country`, so when reporting on only
       *  `country`, you can't get more than 300 rows, even if you set `limit` to a
       *  higher value.
       *  To learn more about this pagination parameter, see
       *  Pagination (https://developers.google.com/analytics/devguides/reporting/data/v1/basics#pagination).
       */
      // const limit = 1234
      /**
       *  This request's time zone if specified. If unspecified, the property's time
       *  zone is used. The request's time zone is used to interpret the start & end
       *  dates of the report.
       *  Formatted as strings from the IANA Time Zone database
       *  (https://www.iana.org/time-zones); for example "America/New_York" or
       *  "Asia/Tokyo".
       */
      // const timeZone = 'abc123'
      /**
       *  Specifies how rows are ordered in the response.
       */
      // const orderBys = [1,2,3,4]
      /**
       *  Toggles whether to return the current state of this Analytics Property's
       *  quota. Quota is returned in AccessQuota (#AccessQuota). For account-level
       *  requests, this field must be false.
       */
      // const returnEntityQuota = true
      /**
       *  Optional. Determines whether to include users who have never made an API
       *  call in the response. If true, all users with access to the specified
       *  property or account are included in the response, regardless of whether
       *  they have made an API call or not. If false, only the users who have made
       *  an API call will be included.
       */
      // const includeAllUsers = true
      /**
       *  Optional. Decides whether to return the users within user groups. This
       *  field works only when include_all_users is set to true. If true, it will
       *  return all users with access to the specified property or account.
       *  If false, only the users with direct access will be returned.
       */
      // const expandGroups = true
    
      // Imports the Admin library
      const {AnalyticsAdminServiceClient} = require('[@google-analytics/admin](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const adminClient = new [AnalyticsAdminServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)();
    
      async function callRunAccessReport() {
        // Construct request
        const request = {
        };
    
        // Run request
        const response = await adminClient.runAccessReport(request);
        console.log(response);
      }
    
      callRunAccessReport();
    
    

### runAccessReport(request, options, callback)
    
    
    runAccessReport(request: protos.google.analytics.admin.v1beta.IRunAccessReportRequest, options: CallOptions, callback: Callback<protos.google.analytics.admin.v1beta.IRunAccessReportResponse, protos.google.analytics.admin.v1beta.IRunAccessReportRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IRunAccessReportRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.irunaccessreportrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.analytics.admin.v1beta.IRunAccessReportResponse](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.irunaccessreportresponse), [protos.google.analytics.admin.v1beta.IRunAccessReportRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.irunaccessreportrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### runAccessReport(request, callback)
    
    
    runAccessReport(request: protos.google.analytics.admin.v1beta.IRunAccessReportRequest, callback: Callback<protos.google.analytics.admin.v1beta.IRunAccessReportResponse, protos.google.analytics.admin.v1beta.IRunAccessReportRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IRunAccessReportRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.irunaccessreportrequest)`   
  
`callback` |  `Callback<[protos.google.analytics.admin.v1beta.IRunAccessReportResponse](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.irunaccessreportresponse), [protos.google.analytics.admin.v1beta.IRunAccessReportRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.irunaccessreportrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### searchChangeHistoryEvents(request, options)
    
    
    searchChangeHistoryEvents(request?: protos.google.analytics.admin.v1beta.ISearchChangeHistoryEventsRequest, options?: CallOptions): Promise<[
            protos.google.analytics.admin.v1beta.IChangeHistoryEvent[],
            protos.google.analytics.admin.v1beta.ISearchChangeHistoryEventsRequest | null,
            protos.google.analytics.admin.v1beta.ISearchChangeHistoryEventsResponse
        ]>;

Searches through all changes to an account or its children given the specified set of filters.

Only returns the subset of changes supported by the API. The UI may return additional changes.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISearchChangeHistoryEventsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.isearchchangehistoryeventsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.analytics.admin.v1beta.IChangeHistoryEvent](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ichangehistoryevent)[], [protos.google.analytics.admin.v1beta.ISearchChangeHistoryEventsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.isearchchangehistoryeventsrequest) | null, [protos.google.analytics.admin.v1beta.ISearchChangeHistoryEventsResponse](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.isearchchangehistoryeventsresponse) ]>` | {Promise} - The promise which resolves to an array. The first element of the array is Array of [ChangeHistoryEvent](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.changehistoryevent). The client library will perform auto-pagination by default: it will call the API as many times as needed and will merge results from all the pages into this array. Note that it can affect your quota. We recommend using `searchChangeHistoryEventsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### searchChangeHistoryEvents(request, options, callback)
    
    
    searchChangeHistoryEvents(request: protos.google.analytics.admin.v1beta.ISearchChangeHistoryEventsRequest, options: CallOptions, callback: PaginationCallback<protos.google.analytics.admin.v1beta.ISearchChangeHistoryEventsRequest, protos.google.analytics.admin.v1beta.ISearchChangeHistoryEventsResponse | null | undefined, protos.google.analytics.admin.v1beta.IChangeHistoryEvent>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISearchChangeHistoryEventsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.isearchchangehistoryeventsrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `PaginationCallback<[protos.google.analytics.admin.v1beta.ISearchChangeHistoryEventsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.isearchchangehistoryeventsrequest), [protos.google.analytics.admin.v1beta.ISearchChangeHistoryEventsResponse](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.isearchchangehistoryeventsresponse) | null | undefined, [protos.google.analytics.admin.v1beta.IChangeHistoryEvent](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ichangehistoryevent)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### searchChangeHistoryEvents(request, callback)
    
    
    searchChangeHistoryEvents(request: protos.google.analytics.admin.v1beta.ISearchChangeHistoryEventsRequest, callback: PaginationCallback<protos.google.analytics.admin.v1beta.ISearchChangeHistoryEventsRequest, protos.google.analytics.admin.v1beta.ISearchChangeHistoryEventsResponse | null | undefined, protos.google.analytics.admin.v1beta.IChangeHistoryEvent>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISearchChangeHistoryEventsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.isearchchangehistoryeventsrequest)`   
  
`callback` |  `PaginationCallback<[protos.google.analytics.admin.v1beta.ISearchChangeHistoryEventsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.isearchchangehistoryeventsrequest), [protos.google.analytics.admin.v1beta.ISearchChangeHistoryEventsResponse](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.isearchchangehistoryeventsresponse) | null | undefined, [protos.google.analytics.admin.v1beta.IChangeHistoryEvent](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ichangehistoryevent)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### searchChangeHistoryEventsAsync(request, options)
    
    
    searchChangeHistoryEventsAsync(request?: protos.google.analytics.admin.v1beta.ISearchChangeHistoryEventsRequest, options?: CallOptions): AsyncIterable<protos.google.analytics.admin.v1beta.IChangeHistoryEvent>;

Equivalent to `searchChangeHistoryEvents`, but returns an iterable object.

`for`-`await`-`of` syntax is used with the iterable to get response elements on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISearchChangeHistoryEventsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.isearchchangehistoryeventsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.analytics.admin.v1beta.IChangeHistoryEvent](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ichangehistoryevent)>` | {Object} An iterable Object that allows [async iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols). When you iterate the returned iterable, each element will be an object representing [ChangeHistoryEvent](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.changehistoryevent). The API will be called under the hood as needed, once per the page, so you can stop the iteration when you don't need more results. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The account resource for which to return change history
       *  resources. Format: accounts/{account}
       *  Example: `accounts/100`
       */
      // const account = 'abc123'
      /**
       *  Optional. Resource name for a child property. If set, only return changes
       *  made to this property or its child resources.
       *  Format: properties/{propertyId}
       *  Example: `properties/100`
       */
      // const property = 'abc123'
      /**
       *  Optional. If set, only return changes if they are for a resource that
       *  matches at least one of these types.
       */
      // const resourceType = [1,2,3,4]
      /**
       *  Optional. If set, only return changes that match one or more of these types
       *  of actions.
       */
      // const action = [1,2,3,4]
      /**
       *  Optional. If set, only return changes if they are made by a user in this
       *  list.
       */
      // const actorEmail = ['abc','def']
      /**
       *  Optional. If set, only return changes made after this time (inclusive).
       */
      // const earliestChangeTime = {}
      /**
       *  Optional. If set, only return changes made before this time (inclusive).
       */
      // const latestChangeTime = {}
      /**
       *  Optional. The maximum number of ChangeHistoryEvent items to return.
       *  If unspecified, at most 50 items will be returned. The maximum value is 200
       *  (higher values will be coerced to the maximum).
       *  Note that the service may return a page with fewer items than this value
       *  specifies (potentially even zero), and that there still may be additional
       *  pages. If you want a particular number of items, you'll need to continue
       *  requesting additional pages using `page_token` until you get the needed
       *  number.
       */
      // const pageSize = 1234
      /**
       *  Optional. A page token, received from a previous
       *  `SearchChangeHistoryEvents` call. Provide this to retrieve the subsequent
       *  page. When paginating, all other parameters provided to
       *  `SearchChangeHistoryEvents` must match the call that provided the page
       *  token.
       */
      // const pageToken = 'abc123'
    
      // Imports the Admin library
      const {AnalyticsAdminServiceClient} = require('[@google-analytics/admin](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const adminClient = new [AnalyticsAdminServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)();
    
      async function callSearchChangeHistoryEvents() {
        // Construct request
        const request = {
          account,
        };
    
        // Run request
        const iterable = adminClient.searchChangeHistoryEventsAsync(request);
        for await (const response of iterable) {
            console.log(response);
        }
      }
    
      callSearchChangeHistoryEvents();
    
    

### searchChangeHistoryEventsStream(request, options)
    
    
    searchChangeHistoryEventsStream(request?: protos.google.analytics.admin.v1beta.ISearchChangeHistoryEventsRequest, options?: CallOptions): Transform;

Equivalent to `searchChangeHistoryEvents`, but returns a NodeJS Stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISearchChangeHistoryEventsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.isearchchangehistoryeventsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Transform` | {Stream} An object stream which emits an object representing [ChangeHistoryEvent](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.changehistoryevent) on 'data' event. The client library will perform auto-pagination by default: it will call the API as many times as needed. Note that it can affect your quota. We recommend using `searchChangeHistoryEventsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### updateAccount(request, options)
    
    
    updateAccount(request?: protos.google.analytics.admin.v1beta.IUpdateAccountRequest, options?: CallOptions): Promise<[
            protos.google.analytics.admin.v1beta.IAccount,
            protos.google.analytics.admin.v1beta.IUpdateAccountRequest | undefined,
            {} | undefined
        ]>;

Updates an account.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateAccountRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.iupdateaccountrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.analytics.admin.v1beta.IAccount](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.iaccount), [protos.google.analytics.admin.v1beta.IUpdateAccountRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.iupdateaccountrequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [Account](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.account). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The account to update.
       *  The account's `name` field is used to identify the account.
       */
      // const account = {}
      /**
       *  Required. The list of fields to be updated. Field names must be in snake
       *  case (for example, "field_to_update"). Omitted fields will not be updated.
       *  To replace the entire entity, use one path with the string "*" to match all
       *  fields.
       */
      // const updateMask = {}
    
      // Imports the Admin library
      const {AnalyticsAdminServiceClient} = require('[@google-analytics/admin](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const adminClient = new [AnalyticsAdminServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)();
    
      async function callUpdateAccount() {
        // Construct request
        const request = {
          account,
          updateMask,
        };
    
        // Run request
        const response = await adminClient.updateAccount(request);
        console.log(response);
      }
    
      callUpdateAccount();
    
    

### updateAccount(request, options, callback)
    
    
    updateAccount(request: protos.google.analytics.admin.v1beta.IUpdateAccountRequest, options: CallOptions, callback: Callback<protos.google.analytics.admin.v1beta.IAccount, protos.google.analytics.admin.v1beta.IUpdateAccountRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateAccountRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.iupdateaccountrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.analytics.admin.v1beta.IAccount](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.iaccount), [protos.google.analytics.admin.v1beta.IUpdateAccountRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.iupdateaccountrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateAccount(request, callback)
    
    
    updateAccount(request: protos.google.analytics.admin.v1beta.IUpdateAccountRequest, callback: Callback<protos.google.analytics.admin.v1beta.IAccount, protos.google.analytics.admin.v1beta.IUpdateAccountRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateAccountRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.iupdateaccountrequest)`   
  
`callback` |  `Callback<[protos.google.analytics.admin.v1beta.IAccount](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.iaccount), [protos.google.analytics.admin.v1beta.IUpdateAccountRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.iupdateaccountrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateConversionEvent(request, options)
    
    
    updateConversionEvent(request?: protos.google.analytics.admin.v1beta.IUpdateConversionEventRequest, options?: CallOptions): Promise<[
            protos.google.analytics.admin.v1beta.IConversionEvent,
            (protos.google.analytics.admin.v1beta.IUpdateConversionEventRequest | undefined),
            {} | undefined
        ]>;

Deprecated: Use `UpdateKeyEvent` instead. Updates a conversion event with the specified attributes.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateConversionEventRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.iupdateconversioneventrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.analytics.admin.v1beta.IConversionEvent](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.iconversionevent), ([protos.google.analytics.admin.v1beta.IUpdateConversionEventRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.iupdateconversioneventrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The conversion event to update.
       *  The `name` field is used to identify the settings to be updated.
       */
      // const conversionEvent = {}
      /**
       *  Required. The list of fields to be updated. Field names must be in snake
       *  case (e.g., "field_to_update"). Omitted fields will not be updated. To
       *  replace the entire entity, use one path with the string "*" to match all
       *  fields.
       */
      // const updateMask = {}
    
      // Imports the Admin library
      const {AnalyticsAdminServiceClient} = require('[@google-analytics/admin](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const adminClient = new [AnalyticsAdminServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)();
    
      async function callUpdateConversionEvent() {
        // Construct request
        const request = {
          conversionEvent,
          updateMask,
        };
    
        // Run request
        const response = await adminClient.updateConversionEvent(request);
        console.log(response);
      }
    
      callUpdateConversionEvent();
    
    

### updateConversionEvent(request, options, callback)
    
    
    updateConversionEvent(request: protos.google.analytics.admin.v1beta.IUpdateConversionEventRequest, options: CallOptions, callback: Callback<protos.google.analytics.admin.v1beta.IConversionEvent, protos.google.analytics.admin.v1beta.IUpdateConversionEventRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateConversionEventRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.iupdateconversioneventrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.analytics.admin.v1beta.IConversionEvent](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.iconversionevent), [protos.google.analytics.admin.v1beta.IUpdateConversionEventRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.iupdateconversioneventrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateConversionEvent(request, callback)
    
    
    updateConversionEvent(request: protos.google.analytics.admin.v1beta.IUpdateConversionEventRequest, callback: Callback<protos.google.analytics.admin.v1beta.IConversionEvent, protos.google.analytics.admin.v1beta.IUpdateConversionEventRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateConversionEventRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.iupdateconversioneventrequest)`   
  
`callback` |  `Callback<[protos.google.analytics.admin.v1beta.IConversionEvent](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.iconversionevent), [protos.google.analytics.admin.v1beta.IUpdateConversionEventRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.iupdateconversioneventrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateCustomDimension(request, options)
    
    
    updateCustomDimension(request?: protos.google.analytics.admin.v1beta.IUpdateCustomDimensionRequest, options?: CallOptions): Promise<[
            protos.google.analytics.admin.v1beta.ICustomDimension,
            (protos.google.analytics.admin.v1beta.IUpdateCustomDimensionRequest | undefined),
            {} | undefined
        ]>;

Updates a CustomDimension on a property.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateCustomDimensionRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.iupdatecustomdimensionrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.analytics.admin.v1beta.ICustomDimension](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.icustomdimension), ([protos.google.analytics.admin.v1beta.IUpdateCustomDimensionRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.iupdatecustomdimensionrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  The CustomDimension to update
       */
      // const customDimension = {}
      /**
       *  Required. The list of fields to be updated. Omitted fields will not be
       *  updated. To replace the entire entity, use one path with the string "*" to
       *  match all fields.
       */
      // const updateMask = {}
    
      // Imports the Admin library
      const {AnalyticsAdminServiceClient} = require('[@google-analytics/admin](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const adminClient = new [AnalyticsAdminServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)();
    
      async function callUpdateCustomDimension() {
        // Construct request
        const request = {
          updateMask,
        };
    
        // Run request
        const response = await adminClient.updateCustomDimension(request);
        console.log(response);
      }
    
      callUpdateCustomDimension();
    
    

### updateCustomDimension(request, options, callback)
    
    
    updateCustomDimension(request: protos.google.analytics.admin.v1beta.IUpdateCustomDimensionRequest, options: CallOptions, callback: Callback<protos.google.analytics.admin.v1beta.ICustomDimension, protos.google.analytics.admin.v1beta.IUpdateCustomDimensionRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateCustomDimensionRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.iupdatecustomdimensionrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.analytics.admin.v1beta.ICustomDimension](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.icustomdimension), [protos.google.analytics.admin.v1beta.IUpdateCustomDimensionRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.iupdatecustomdimensionrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateCustomDimension(request, callback)
    
    
    updateCustomDimension(request: protos.google.analytics.admin.v1beta.IUpdateCustomDimensionRequest, callback: Callback<protos.google.analytics.admin.v1beta.ICustomDimension, protos.google.analytics.admin.v1beta.IUpdateCustomDimensionRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateCustomDimensionRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.iupdatecustomdimensionrequest)`   
  
`callback` |  `Callback<[protos.google.analytics.admin.v1beta.ICustomDimension](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.icustomdimension), [protos.google.analytics.admin.v1beta.IUpdateCustomDimensionRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.iupdatecustomdimensionrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateCustomMetric(request, options)
    
    
    updateCustomMetric(request?: protos.google.analytics.admin.v1beta.IUpdateCustomMetricRequest, options?: CallOptions): Promise<[
            protos.google.analytics.admin.v1beta.ICustomMetric,
            (protos.google.analytics.admin.v1beta.IUpdateCustomMetricRequest | undefined),
            {} | undefined
        ]>;

Updates a CustomMetric on a property.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateCustomMetricRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.iupdatecustommetricrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.analytics.admin.v1beta.ICustomMetric](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.icustommetric), ([protos.google.analytics.admin.v1beta.IUpdateCustomMetricRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.iupdatecustommetricrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  The CustomMetric to update
       */
      // const customMetric = {}
      /**
       *  Required. The list of fields to be updated. Omitted fields will not be
       *  updated. To replace the entire entity, use one path with the string "*" to
       *  match all fields.
       */
      // const updateMask = {}
    
      // Imports the Admin library
      const {AnalyticsAdminServiceClient} = require('[@google-analytics/admin](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const adminClient = new [AnalyticsAdminServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)();
    
      async function callUpdateCustomMetric() {
        // Construct request
        const request = {
          updateMask,
        };
    
        // Run request
        const response = await adminClient.updateCustomMetric(request);
        console.log(response);
      }
    
      callUpdateCustomMetric();
    
    

### updateCustomMetric(request, options, callback)
    
    
    updateCustomMetric(request: protos.google.analytics.admin.v1beta.IUpdateCustomMetricRequest, options: CallOptions, callback: Callback<protos.google.analytics.admin.v1beta.ICustomMetric, protos.google.analytics.admin.v1beta.IUpdateCustomMetricRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateCustomMetricRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.iupdatecustommetricrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.analytics.admin.v1beta.ICustomMetric](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.icustommetric), [protos.google.analytics.admin.v1beta.IUpdateCustomMetricRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.iupdatecustommetricrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateCustomMetric(request, callback)
    
    
    updateCustomMetric(request: protos.google.analytics.admin.v1beta.IUpdateCustomMetricRequest, callback: Callback<protos.google.analytics.admin.v1beta.ICustomMetric, protos.google.analytics.admin.v1beta.IUpdateCustomMetricRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateCustomMetricRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.iupdatecustommetricrequest)`   
  
`callback` |  `Callback<[protos.google.analytics.admin.v1beta.ICustomMetric](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.icustommetric), [protos.google.analytics.admin.v1beta.IUpdateCustomMetricRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.iupdatecustommetricrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateDataRetentionSettings(request, options)
    
    
    updateDataRetentionSettings(request?: protos.google.analytics.admin.v1beta.IUpdateDataRetentionSettingsRequest, options?: CallOptions): Promise<[
            protos.google.analytics.admin.v1beta.IDataRetentionSettings,
            (protos.google.analytics.admin.v1beta.IUpdateDataRetentionSettingsRequest | undefined),
            {} | undefined
        ]>;

Updates the singleton data retention settings for this property.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateDataRetentionSettingsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.iupdatedataretentionsettingsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.analytics.admin.v1beta.IDataRetentionSettings](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.idataretentionsettings), ([protos.google.analytics.admin.v1beta.IUpdateDataRetentionSettingsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.iupdatedataretentionsettingsrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The settings to update.
       *  The `name` field is used to identify the settings to be updated.
       */
      // const dataRetentionSettings = {}
      /**
       *  Required. The list of fields to be updated. Field names must be in snake
       *  case (e.g., "field_to_update"). Omitted fields will not be updated. To
       *  replace the entire entity, use one path with the string "*" to match all
       *  fields.
       */
      // const updateMask = {}
    
      // Imports the Admin library
      const {AnalyticsAdminServiceClient} = require('[@google-analytics/admin](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const adminClient = new [AnalyticsAdminServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)();
    
      async function callUpdateDataRetentionSettings() {
        // Construct request
        const request = {
          dataRetentionSettings,
          updateMask,
        };
    
        // Run request
        const response = await adminClient.updateDataRetentionSettings(request);
        console.log(response);
      }
    
      callUpdateDataRetentionSettings();
    
    

### updateDataRetentionSettings(request, options, callback)
    
    
    updateDataRetentionSettings(request: protos.google.analytics.admin.v1beta.IUpdateDataRetentionSettingsRequest, options: CallOptions, callback: Callback<protos.google.analytics.admin.v1beta.IDataRetentionSettings, protos.google.analytics.admin.v1beta.IUpdateDataRetentionSettingsRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateDataRetentionSettingsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.iupdatedataretentionsettingsrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.analytics.admin.v1beta.IDataRetentionSettings](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.idataretentionsettings), [protos.google.analytics.admin.v1beta.IUpdateDataRetentionSettingsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.iupdatedataretentionsettingsrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateDataRetentionSettings(request, callback)
    
    
    updateDataRetentionSettings(request: protos.google.analytics.admin.v1beta.IUpdateDataRetentionSettingsRequest, callback: Callback<protos.google.analytics.admin.v1beta.IDataRetentionSettings, protos.google.analytics.admin.v1beta.IUpdateDataRetentionSettingsRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateDataRetentionSettingsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.iupdatedataretentionsettingsrequest)`   
  
`callback` |  `Callback<[protos.google.analytics.admin.v1beta.IDataRetentionSettings](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.idataretentionsettings), [protos.google.analytics.admin.v1beta.IUpdateDataRetentionSettingsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.iupdatedataretentionsettingsrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateDataStream(request, options)
    
    
    updateDataStream(request?: protos.google.analytics.admin.v1beta.IUpdateDataStreamRequest, options?: CallOptions): Promise<[
            protos.google.analytics.admin.v1beta.IDataStream,
            protos.google.analytics.admin.v1beta.IUpdateDataStreamRequest | undefined,
            {} | undefined
        ]>;

Updates a DataStream on a property.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateDataStreamRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.iupdatedatastreamrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.analytics.admin.v1beta.IDataStream](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.idatastream), [protos.google.analytics.admin.v1beta.IUpdateDataStreamRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.iupdatedatastreamrequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  The DataStream to update
       */
      // const dataStream = {}
      /**
       *  Required. The list of fields to be updated. Omitted fields will not be
       *  updated. To replace the entire entity, use one path with the string "*" to
       *  match all fields.
       */
      // const updateMask = {}
    
      // Imports the Admin library
      const {AnalyticsAdminServiceClient} = require('[@google-analytics/admin](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const adminClient = new [AnalyticsAdminServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)();
    
      async function callUpdateDataStream() {
        // Construct request
        const request = {
          updateMask,
        };
    
        // Run request
        const response = await adminClient.updateDataStream(request);
        console.log(response);
      }
    
      callUpdateDataStream();
    
    

### updateDataStream(request, options, callback)
    
    
    updateDataStream(request: protos.google.analytics.admin.v1beta.IUpdateDataStreamRequest, options: CallOptions, callback: Callback<protos.google.analytics.admin.v1beta.IDataStream, protos.google.analytics.admin.v1beta.IUpdateDataStreamRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateDataStreamRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.iupdatedatastreamrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.analytics.admin.v1beta.IDataStream](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.idatastream), [protos.google.analytics.admin.v1beta.IUpdateDataStreamRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.iupdatedatastreamrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateDataStream(request, callback)
    
    
    updateDataStream(request: protos.google.analytics.admin.v1beta.IUpdateDataStreamRequest, callback: Callback<protos.google.analytics.admin.v1beta.IDataStream, protos.google.analytics.admin.v1beta.IUpdateDataStreamRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateDataStreamRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.iupdatedatastreamrequest)`   
  
`callback` |  `Callback<[protos.google.analytics.admin.v1beta.IDataStream](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.idatastream), [protos.google.analytics.admin.v1beta.IUpdateDataStreamRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.iupdatedatastreamrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateGoogleAdsLink(request, options)
    
    
    updateGoogleAdsLink(request?: protos.google.analytics.admin.v1beta.IUpdateGoogleAdsLinkRequest, options?: CallOptions): Promise<[
            protos.google.analytics.admin.v1beta.IGoogleAdsLink,
            (protos.google.analytics.admin.v1beta.IUpdateGoogleAdsLinkRequest | undefined),
            {} | undefined
        ]>;

Updates a GoogleAdsLink on a property

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateGoogleAdsLinkRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.iupdategoogleadslinkrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.analytics.admin.v1beta.IGoogleAdsLink](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.igoogleadslink), ([protos.google.analytics.admin.v1beta.IUpdateGoogleAdsLinkRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.iupdategoogleadslinkrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [GoogleAdsLink](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.googleadslink). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  The GoogleAdsLink to update
       */
      // const googleAdsLink = {}
      /**
       *  Required. The list of fields to be updated. Field names must be in snake
       *  case (e.g., "field_to_update"). Omitted fields will not be updated. To
       *  replace the entire entity, use one path with the string "*" to match all
       *  fields.
       */
      // const updateMask = {}
    
      // Imports the Admin library
      const {AnalyticsAdminServiceClient} = require('[@google-analytics/admin](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const adminClient = new [AnalyticsAdminServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)();
    
      async function callUpdateGoogleAdsLink() {
        // Construct request
        const request = {
          updateMask,
        };
    
        // Run request
        const response = await adminClient.updateGoogleAdsLink(request);
        console.log(response);
      }
    
      callUpdateGoogleAdsLink();
    
    

### updateGoogleAdsLink(request, options, callback)
    
    
    updateGoogleAdsLink(request: protos.google.analytics.admin.v1beta.IUpdateGoogleAdsLinkRequest, options: CallOptions, callback: Callback<protos.google.analytics.admin.v1beta.IGoogleAdsLink, protos.google.analytics.admin.v1beta.IUpdateGoogleAdsLinkRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateGoogleAdsLinkRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.iupdategoogleadslinkrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.analytics.admin.v1beta.IGoogleAdsLink](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.igoogleadslink), [protos.google.analytics.admin.v1beta.IUpdateGoogleAdsLinkRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.iupdategoogleadslinkrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateGoogleAdsLink(request, callback)
    
    
    updateGoogleAdsLink(request: protos.google.analytics.admin.v1beta.IUpdateGoogleAdsLinkRequest, callback: Callback<protos.google.analytics.admin.v1beta.IGoogleAdsLink, protos.google.analytics.admin.v1beta.IUpdateGoogleAdsLinkRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateGoogleAdsLinkRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.iupdategoogleadslinkrequest)`   
  
`callback` |  `Callback<[protos.google.analytics.admin.v1beta.IGoogleAdsLink](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.igoogleadslink), [protos.google.analytics.admin.v1beta.IUpdateGoogleAdsLinkRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.iupdategoogleadslinkrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateKeyEvent(request, options)
    
    
    updateKeyEvent(request?: protos.google.analytics.admin.v1beta.IUpdateKeyEventRequest, options?: CallOptions): Promise<[
            protos.google.analytics.admin.v1beta.IKeyEvent,
            protos.google.analytics.admin.v1beta.IUpdateKeyEventRequest | undefined,
            {} | undefined
        ]>;

Updates a Key Event.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateKeyEventRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.iupdatekeyeventrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.analytics.admin.v1beta.IKeyEvent](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ikeyevent), [protos.google.analytics.admin.v1beta.IUpdateKeyEventRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.iupdatekeyeventrequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The Key Event to update.
       *  The `name` field is used to identify the settings to be updated.
       */
      // const keyEvent = {}
      /**
       *  Required. The list of fields to be updated. Field names must be in snake
       *  case (e.g., "field_to_update"). Omitted fields will not be updated. To
       *  replace the entire entity, use one path with the string "*" to match all
       *  fields.
       */
      // const updateMask = {}
    
      // Imports the Admin library
      const {AnalyticsAdminServiceClient} = require('[@google-analytics/admin](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const adminClient = new [AnalyticsAdminServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)();
    
      async function callUpdateKeyEvent() {
        // Construct request
        const request = {
          keyEvent,
          updateMask,
        };
    
        // Run request
        const response = await adminClient.updateKeyEvent(request);
        console.log(response);
      }
    
      callUpdateKeyEvent();
    
    

### updateKeyEvent(request, options, callback)
    
    
    updateKeyEvent(request: protos.google.analytics.admin.v1beta.IUpdateKeyEventRequest, options: CallOptions, callback: Callback<protos.google.analytics.admin.v1beta.IKeyEvent, protos.google.analytics.admin.v1beta.IUpdateKeyEventRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateKeyEventRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.iupdatekeyeventrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.analytics.admin.v1beta.IKeyEvent](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ikeyevent), [protos.google.analytics.admin.v1beta.IUpdateKeyEventRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.iupdatekeyeventrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateKeyEvent(request, callback)
    
    
    updateKeyEvent(request: protos.google.analytics.admin.v1beta.IUpdateKeyEventRequest, callback: Callback<protos.google.analytics.admin.v1beta.IKeyEvent, protos.google.analytics.admin.v1beta.IUpdateKeyEventRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateKeyEventRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.iupdatekeyeventrequest)`   
  
`callback` |  `Callback<[protos.google.analytics.admin.v1beta.IKeyEvent](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ikeyevent), [protos.google.analytics.admin.v1beta.IUpdateKeyEventRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.iupdatekeyeventrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateMeasurementProtocolSecret(request, options)
    
    
    updateMeasurementProtocolSecret(request?: protos.google.analytics.admin.v1beta.IUpdateMeasurementProtocolSecretRequest, options?: CallOptions): Promise<[
            protos.google.analytics.admin.v1beta.IMeasurementProtocolSecret,
            (protos.google.analytics.admin.v1beta.IUpdateMeasurementProtocolSecretRequest | undefined),
            {} | undefined
        ]>;

Updates a measurement protocol secret.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateMeasurementProtocolSecretRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.iupdatemeasurementprotocolsecretrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.analytics.admin.v1beta.IMeasurementProtocolSecret](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.imeasurementprotocolsecret), ([protos.google.analytics.admin.v1beta.IUpdateMeasurementProtocolSecretRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.iupdatemeasurementprotocolsecretrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [MeasurementProtocolSecret](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.measurementprotocolsecret). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The measurement protocol secret to update.
       */
      // const measurementProtocolSecret = {}
      /**
       *  Required. The list of fields to be updated. Omitted fields will not be
       *  updated.
       */
      // const updateMask = {}
    
      // Imports the Admin library
      const {AnalyticsAdminServiceClient} = require('[@google-analytics/admin](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const adminClient = new [AnalyticsAdminServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)();
    
      async function callUpdateMeasurementProtocolSecret() {
        // Construct request
        const request = {
          measurementProtocolSecret,
          updateMask,
        };
    
        // Run request
        const response = await adminClient.updateMeasurementProtocolSecret(request);
        console.log(response);
      }
    
      callUpdateMeasurementProtocolSecret();
    
    

### updateMeasurementProtocolSecret(request, options, callback)
    
    
    updateMeasurementProtocolSecret(request: protos.google.analytics.admin.v1beta.IUpdateMeasurementProtocolSecretRequest, options: CallOptions, callback: Callback<protos.google.analytics.admin.v1beta.IMeasurementProtocolSecret, protos.google.analytics.admin.v1beta.IUpdateMeasurementProtocolSecretRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateMeasurementProtocolSecretRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.iupdatemeasurementprotocolsecretrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.analytics.admin.v1beta.IMeasurementProtocolSecret](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.imeasurementprotocolsecret), [protos.google.analytics.admin.v1beta.IUpdateMeasurementProtocolSecretRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.iupdatemeasurementprotocolsecretrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateMeasurementProtocolSecret(request, callback)
    
    
    updateMeasurementProtocolSecret(request: protos.google.analytics.admin.v1beta.IUpdateMeasurementProtocolSecretRequest, callback: Callback<protos.google.analytics.admin.v1beta.IMeasurementProtocolSecret, protos.google.analytics.admin.v1beta.IUpdateMeasurementProtocolSecretRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateMeasurementProtocolSecretRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.iupdatemeasurementprotocolsecretrequest)`   
  
`callback` |  `Callback<[protos.google.analytics.admin.v1beta.IMeasurementProtocolSecret](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.imeasurementprotocolsecret), [protos.google.analytics.admin.v1beta.IUpdateMeasurementProtocolSecretRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.iupdatemeasurementprotocolsecretrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateProperty(request, options)
    
    
    updateProperty(request?: protos.google.analytics.admin.v1beta.IUpdatePropertyRequest, options?: CallOptions): Promise<[
            protos.google.analytics.admin.v1beta.IProperty,
            protos.google.analytics.admin.v1beta.IUpdatePropertyRequest | undefined,
            {} | undefined
        ]>;

Updates a property.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdatePropertyRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.iupdatepropertyrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.analytics.admin.v1beta.IProperty](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.iproperty), [protos.google.analytics.admin.v1beta.IUpdatePropertyRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.iupdatepropertyrequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [Property](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.property). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The property to update.
       *  The property's `name` field is used to identify the property to be
       *  updated.
       */
      // const property = {}
      /**
       *  Required. The list of fields to be updated. Field names must be in snake
       *  case (e.g., "field_to_update"). Omitted fields will not be updated. To
       *  replace the entire entity, use one path with the string "*" to match all
       *  fields.
       */
      // const updateMask = {}
    
      // Imports the Admin library
      const {AnalyticsAdminServiceClient} = require('[@google-analytics/admin](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const adminClient = new [AnalyticsAdminServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)();
    
      async function callUpdateProperty() {
        // Construct request
        const request = {
          property,
          updateMask,
        };
    
        // Run request
        const response = await adminClient.updateProperty(request);
        console.log(response);
      }
    
      callUpdateProperty();
    
    

### updateProperty(request, options, callback)
    
    
    updateProperty(request: protos.google.analytics.admin.v1beta.IUpdatePropertyRequest, options: CallOptions, callback: Callback<protos.google.analytics.admin.v1beta.IProperty, protos.google.analytics.admin.v1beta.IUpdatePropertyRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdatePropertyRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.iupdatepropertyrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.analytics.admin.v1beta.IProperty](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.iproperty), [protos.google.analytics.admin.v1beta.IUpdatePropertyRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.iupdatepropertyrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateProperty(request, callback)
    
    
    updateProperty(request: protos.google.analytics.admin.v1beta.IUpdatePropertyRequest, callback: Callback<protos.google.analytics.admin.v1beta.IProperty, protos.google.analytics.admin.v1beta.IUpdatePropertyRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdatePropertyRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.iupdatepropertyrequest)`   
  
`callback` |  `Callback<[protos.google.analytics.admin.v1beta.IProperty](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.iproperty), [protos.google.analytics.admin.v1beta.IUpdatePropertyRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.iupdatepropertyrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
