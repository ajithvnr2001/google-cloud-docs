---
url: https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.branches.products/import/
title: Method: projects.locations.catalogs.branches.products.import \u00a0|\u00a0 AI Commerce Search in Gemini Enterprise for Customer Experience \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:39:28.033677+00:00
---

# Method: projects.locations.catalogs.branches.products.import  |  AI Commerce Search in Gemini Enterprise for Customer Experience  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.branches.products/import/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ AI Commerce Search ](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search)



Send feedback 

#  Method: projects.locations.catalogs.branches.products.import Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
  * Authorization scopes
  * IAM Permissions
  * ProductInputConfig
    * JSON representation
  * ProductInlineSource
    * JSON representation
  * ReconciliationMode
  * Try it!



Bulk import of multiple `[Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.branches.products#Product)`s.

Request processing may be synchronous. Non-existing items are created.

Note that it is possible for a subset of the `[Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.branches.products#Product)`s to be successfully updated.

### HTTP request

`POST https://retail.googleapis.com/v2beta/{parent=projects/*/locations/*/catalogs/*/branches/*}/products:import`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. `projects/1234/locations/global/catalogs/default_catalog/branches/default_branch`If no updateMask is specified, requires products.create permission. If updateMask is specified, requires products.update permission.  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "requestId": string,
      "inputConfig": {
        object ([ProductInputConfig](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.branches.products/import#ProductInputConfig))
      },
      "errorsConfig": {
        object ([ImportErrorsConfig](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/ImportErrorsConfig))
      },
      "updateMask": string,
      "reconciliationMode": enum ([ReconciliationMode](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.branches.products/import#ReconciliationMode)),
      "notificationPubsubTopic": string
    }  
  
Fields  
---  
`requestId  
**(deprecated)**` |  `string` Deprecated. This field has no effect.  
`inputConfig` |  `object (`[ProductInputConfig](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.branches.products/import#ProductInputConfig)`)` Required. The desired input location of the data.  
`errorsConfig` |  `object (`[ImportErrorsConfig](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/ImportErrorsConfig)`)` The desired location of errors incurred during the Import.  
`updateMask` |  `string (`[FieldMask](https://protobuf.dev/reference/protobuf/google.protobuf/#field-mask)` format)` Indicates which fields in the provided imported `products` to update. If not set, all fields are updated. If provided, only the existing product fields are updated. Missing products will not be created.This is a comma-separated list of fully qualified names of fields. Example: `"user.displayName,photo"`.  
`reconciliationMode` |  `enum (`[ReconciliationMode](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.branches.products/import#ReconciliationMode)`)` The mode of reconciliation between existing products and the products to be imported. Defaults to `[ReconciliationMode.INCREMENTAL](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.branches.products/import#ReconciliationMode.ENUM_VALUES.INCREMENTAL)`.  
`notificationPubsubTopic` |  `string` Full Pub/Sub topic name for receiving notification. If this field is set, when the import is finished, a notification is sent to specified Pub/Sub topic. The message data is JSON string of a `[Operation](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/Shared.Types/ListOperationsResponse#Operation)`.Format of the Pub/Sub topic is `projects/{project}/topics/{topic}`. It has to be within the same project as `[ImportProductsRequest.parent](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.branches.products/import#body.PATH_PARAMETERS.parent)`. Make sure that both `cloud-retail-customer-data-access@system.gserviceaccount.com` and `service-<project number>@gcp-sa-retail.iam.gserviceaccount.com` have the `pubsub.topics.publish` IAM permission on the topic.Only supported when `[ImportProductsRequest.reconciliation_mode](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.branches.products/import#body.request_body.FIELDS.reconciliation_mode)` is set to `FULL`.  
  
### Response body

If successful, the response body contains an instance of `[Operation](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/Shared.Types/ListOperationsResponse#Operation)`.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `retail.products.import`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

## ProductInputConfig

The input config source for products.

JSON representation  
---  
      
    
    {
    
      // Union field source can be only one of the following:
      "productInlineSource": {
        object ([ProductInlineSource](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.branches.products/import#ProductInlineSource))
      },
      "gcsSource": {
        object ([GcsSource](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/GcsSource))
      },
      "bigQuerySource": {
        object ([BigQuerySource](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/BigQuerySource))
      }
      // End of list of possible types for union field source.
    }  
  
Fields  
---  
Union field `source`. Required. The source of the input. `source` can be only one of the following:  
`productInlineSource` |  `object (`[ProductInlineSource](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.branches.products/import#ProductInlineSource)`)` The Inline source for the input content for products.  
`gcsSource` |  `object (`[GcsSource](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/GcsSource)`)` Google Cloud Storage location for the input content.  
`bigQuerySource` |  `object (`[BigQuerySource](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/BigQuerySource)`)` BigQuery input source.  
  
## ProductInlineSource

The inline source for the input config for products.import method.

JSON representation  
---  
      
    
    {
      "products": [
        {
          object ([Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.branches.products#Product))
        }
      ]
    }  
  
Fields  
---  
`products[]` |  `object (`[Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.branches.products#Product)`)` Required. A list of products to update/create. Each product must have a valid `[Product.id](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.branches.products#Product.FIELDS.id)`. Recommended max of 100 items.  
  
## ReconciliationMode

Indicates how imported products are reconciled with the existing products created or imported before.

Enums  
---  
`RECONCILIATION_MODE_UNSPECIFIED` | Defaults to INCREMENTAL.  
`INCREMENTAL` | Inserts new products or updates existing products.  
`FULL` | Calculates diff and replaces the entire product dataset. Existing products may be deleted if they are not present in the source location.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-08 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-08 UTC."],[],[]] 
