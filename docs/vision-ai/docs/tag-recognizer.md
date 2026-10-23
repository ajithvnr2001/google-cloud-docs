---
url: https://docs.cloud.google.com/vision-ai/docs/tag-recognizer/
title: Tag Recognizer guide \u00a0|\u00a0 Agent Platform Vision \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:36:22.440211+00:00
---

# Tag Recognizer guide  |  Agent Platform Vision  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vision-ai/docs/tag-recognizer/

Vertex AI Vision is deprecated as of June 15, 2026 and reaches End of Life on September 30, 2026. To migrate, see the [Cloud Vision API](https://docs.cloud.google.com/vision/docs), [Agent Platform serverless training](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/training/overview), or [Agent Platform models](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Platform Vision ](https://docs.cloud.google.com/vision-ai/docs)
  * [ Guides ](https://docs.cloud.google.com/vision-ai/docs/cloud-environment)



Send feedback 

#  Tag Recognizer guide Stay organized with collections  Save and categorize content based on your preferences. 

The **Tag Recognizer** model helps you solve key problems in understanding your retail shelf, namely recognizing and parsing the tags (for example, the price tag or other label tags) according to user-defined key-value pair entity extraction schema.

This model can serve as the primary AI building block for analyzing and interpreting product image data in retail stores. For example, you can use this model on shelf images that are captured by local cameras or mobile devices.

## Tag Recognizer and Product Recognizer use cases

The **Product Recognizer** and **Tag Recognizer** models can serve as the primary AI building blocks for analyzing and interpreting the image data around products and tags image data, which you might have captured from retail stores.

The Product recognizer and Tag recognizer models incorporate several core Google AI modeling and data capabilities to help the retailers and/or technical partners to solve key problems in understanding the product and price-tag image data, including:

  * Recognizing, so understanding what product is in the image.
  * Recognizing and parsing the tag (price-tag, for example, or any other text label tags) according to user defined key-value pair entity extraction schema.



In particular, several differentiating Google AI models are included to support these use-cases problem solving, such as

  * Product thumbnail visual embedding model, which turns a product thumbnail image into a numerical feature space representation.
  * Google OCR model, which extracts all texts visible in the image.
  * Google entity extraction model (that you can customize), which turns the raw texts into the user defined key-value pair named entities.



In addition to these Google AI models, the product recognizer also leverages Google's large database of product information. The product data in this Product database includes the product's GTIN / UPC identity, product brand, title, and cross-language descriptions, product logo, and imagery with various packaging variations. The Product database with the previously mentioned product thumbnail visual embedding model enables the Product recognizer model to be able to recognize many products immediately.

The two major AI features are Product Recognizer and Tag Recognizer models.

## Tag Recognizer functionality

This model recognizes all text strings in the tag, and then tries to parse the text into the user-defined key-value pair entity extraction schema, such as product item description or price value. It includes the following differentiating Google AI models:

  * The Google OCR technology, which extracts all visible text in the image.
  * The Google entity extraction model which turns the raw text into the user defined key-value pair named entities. Customize this model using [ Vertex AI](https://docs.cloud.google.com/vertex-ai/docs/training-overview). For example, if you mainly care about the product item description, product price value, or sale price, but nothing else, user can define their tag parsing schema as follows:
        
        key: item_description   value: string
        key: regular_price      value: number
        key: sale_price         value: number
        




### Tag Parsing Schema

With the customized entity extraction model training, the detected tag item box will then be recognized and parsed in conformance with the user defined schema, for example as follows:
    
    
      item_description:   COLLECTION 18PC GFT BX
      regular_price:      1099
      sale_price:         999
    

### Example Output JSON Object
    
    
    {
      "imageUri": "gs://test_bucket/test_image.jpg",
      "tagRecognitionAnnotations": [
        {
          "entities": [
            {
              "confidence": 0.99646133,
              "mentionText": "NISSIN TOP RAMEN\n\nBOW CHICKEN\n\n",
              "region": {
                "xMax": 0.4618055,
                "xMin": 0.042725038,
                "yMax": 0.45387268,
                "yMin": 0.18415153
              },
              "type":"description"
            },
            {
              "confidence": 0.95828205,
              "mentionText": "$3.90\n",
              "region": {
                "xMax": 0.24819264,
                "xMin": 0.04185935,
                "yMax": 0.96134734,
                "yMin": 0.80382305
              },
              "type":"unit_price"
            },
            {
              "confidence": 0.60659707,
              "mentionText": "$14.99\n",
              "region": {
                "xMax": 0.9754113,
                "xMin": 0.3654699,
                "yMax": 0.92825794,
                "yMin": 0.40368474
              },
              "type":"price"
            }
          ]
        }
      ]
    }

## Environment setup

This section describes how to interact with Store Vision AI RESTful API.
    
    
    API_ENDPOINT=visionai.googleapis.com
    PROJECT_ID=your project ID
    

All the `create` methods require specifying the to-be-created resource name/ID explicitly. You may use a meaningful string identifier, for example, "product-ABC" or a randomly generated identifier for example, UUID.

To grant a person role the editor access to use Store Vision API, please run the following iam binding command:
    
    
    gcloud projects add-iam-policy-binding PROJECT_ID --member='user:USER_ACCOUNT' --role='roles/visionai.editor'
    

To grant a service account the editor access, please use the below command:
    
    
    gcloud projects add-iam-policy-binding PROJECT_ID --member='serviceAccount:SERVICE_ACCOUNT' --role='roles/visionai.editor'
    

[Learn more about IAM binding](https://docs.cloud.google.com/sdk/gcloud/reference/projects/add-iam-policy-binding).

## Tag Recognizer user journey

  1. Perform tag detection model customized training by using [Vertex AI / AutoML Vision Object Detection](https://docs.cloud.google.com/vision/automl/object-detection/docs) feature.
  2. Perform tag entity parsing model training by using [Vertex AI / AutoML Vision Object Detection](https://docs.cloud.google.com/vision/automl/object-detection/docs) feature with customized OCR engine.
  3. Create an Endpoint with desired Tag Recognition config.
  4. Perform BatchAnalyze with TagRecognition feature. In the backend, the system will identify tags from each input image, analyze the text on each detected tag to produce a structured parsing output. T ## Tag Detection & Entity Parsing model training



You can train the customized Tag Detection model using our existing [ Vertex AI / AutoML Vision](https://docs.cloud.google.com/vision/automl/object-detection/docs) product's image Object Detection model training feature. Though Vertex AI / AutoML Vision Object Detection model training feature provides a fully managed model training experience, it's still your responsibility to prepare a well sampled image dataset with fully labeled object bounding box annotations as the training dataset to feed into the model training console. Google Cloud provides the Vertex AI Data Labeling Service to let you create the data labeling task. Please follow the following Vertex AI data labeling job link for details: [/vertex-ai/docs/datasets/data-labeling-job](https://docs.cloud.google.com/vertex-ai/docs/datasets/data-labeling-job). Provide clear data labeling instructions to the human raters so that they know how to label the tag detection bounding boxes in the images as the training dataset preparation.

To train the Tag Entity Parsing model, you need to prepare a collection of training data, with images and their associated annotations.

  * The image is the already cropped tag image.
  * In each image, you need to define and provide the key entity field (such as product_title, price, unit_price fields.) they want to detect and recognize / parse, and their associated image bounding box coordinate location in this cropped image view.
  * To support the correct recognition / parsing, we also require you to provide the regular expression syntax to characterize each field. This is needed to assist the tag parsing algorithm's training and inference routine.



![recognized tag image](https://docs.cloud.google.com/static/vision-ai/docs/images/tag-recognizer_sample-product_EDITED.png)

Tag Entity Parsing Training Example

For example, with the previous tag entity parsing training example, you can provide one line of annotation info in the training data annotation CSV file as follows:
    
    
    "image_filepath", "product_title", "(x0, y0, x1, y1)", "", "price", "(x0, y0, x1, y1)", "\\$\\d+\\.\\d{2}", "unit_price", "(x0, y0, x1, y1)", "\\$\\d+\\.\\d{2}"
    

From the previous example:

  * The "product_title" field has its corresponding box image coordinate "(x0, y0, x1, y1)" and the regular expression constraint for this field is none "".
  * The "price" field has its corresponding box image coordinate "(x0, y0, x1, y1)" and the regular expression constraint for this field is "\$\d+\\.\d{2}", which is indicating we are looking to recognize and parse this field with the $ sign at the beginning of text entry, and a few number digits before the "." and two digits after the ".".
  * The "unit_price" field has the same annotation syntax as the "price" field, for example, the box image coordinates "(x0, y0, x1, y1)" and the regular expression constraint for this field is "\$\d+\\.\d{2}", which is indicating we are looking to recognize and parse this field with the $ sign at the beginning of text entry, and a few number digits before the "." and two digits after the ".".



Hence, a proper price-tag parsing / entity detection model training data will have a collection of price-tag images, with the annotation in a CSV file with each CSV row entry just like the entry in the previous example.
    
    
    "image_filepath", "product_title", "(x0, y0, x1, y1)", "", "price", "(x0, y0, x1, y1)", "\\$\\d+\\.\\d{2}", "unit_price", "(x0, y0, x1, y1)", "\\$\\d+\\.\\d{2}"
    
    "image_filepath", "product_title", "(x0, y0, x1, y1)", "", "price", "(x0, y0, x1, y1)", "\\$\\d+\\.\\d{2}", "unit_price", "(x0, y0, x1, y1)", "\\$\\d+\\.\\d{2}"
    
    "image_filepath", "product_title", "(x0, y0, x1, y1)", "", "price", "(x0, y0, x1, y1)", "\\$\\d+\\.\\d{2}", "unit_price", "(x0, y0, x1, y1)", "\\$\\d+\\.\\d{2}"
    
    [...]
    

You can train the customized Tag Entity Parsing model using our existing [Vertex AI /AutoML Vision](https://docs.cloud.google.com/vision/automl/object-detection/docs) product's Image Object Detection model training feature, plus the Google OCR engine customization.

As of 07/2022, customized Tag Detection and Tag Entity Parsing model training and deployment to Store Vision AI's BatchAnalyze API is not yet fully supported as an integrated console experience, you're still able to take advantage of this customized Tag Detection and Tag Entity Parsing model training (using Agent Platform Vision's Object Detection feature) and serving them in Store Vision AI's BatchAnalyze API by taking several manual self-serving steps.

## API usage - batch analyze inference

##### Create Endpoint

  * ENDPOINT_ID=Your endpoint id
  * TAG_DETECTOR=Your tag detection model name
  * TAG_PARSER=Your tag parsing model name


    
    
    curl -sS -X POST \
    -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    -H "Content-Type: application/json" https://visionai.googleapis.com/v1alpha1/projects/PROJECT_ID/locations/us-central1/retailEndpoints?retail_endpoint_id=ENDPOINT_ID \
    -d '{
      "tagRecognitionConfig": {
        "tag_detection_model": "TAG_DETECTOR_NAME",
        "tag_parsing_model": "TAG_PARSER_NAME"
      }
    }'
    

  * INPUT_FILE_URI=Cloud Storage uri of your input file, each line in the input file is just a Cloud Storage uri of image to process, for example, gs://my-bucket/my-image.jpg
  * OUTPUT_URI_PREFIX=Cloud Storage uri prefix for output results file, for example, gs://my-bucket/my-output-dir


    
    
    curl -sS -X POST \
    -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    -H "Content-Type: application/json" https://visionai.googleapis.com/v1alpha1/projects/PROJECT_ID/locations/us-central1/retailEndpoints/ENDPOINT_ID:batchAnalyze 
    -d '{
      "gcsSource": {
        "uris": ["INPUT_FILE_URI"]
      },
      "features": [
        {
          "type": "TYPE_TAG_RECOGNITION",
         }
      ],
      "outputGcsDestination": {
        "outputUriPrefix": "OUTPUT_URI_PREFIX"
      }
    }'
    

**Note:** You can override the `tagRecognitionConfig` on the Endpoint by specifying it in the BatchAnalyze request instead.
    
    
    "features": [
        {
          "type": "TYPE_TAG_RECOGNITION",
          "tagRecognitionConfig": {
            "tag_detection_model": "'TAG_DETECTOR_NAME'",
            "tag_parsing_model": "TAG_PARSER_NAME"
          }
        }
      ],
    

There are also more fields that you can set and configure in the `tagRecognitionConfig`, which is a `RetailTagRecognitionConfig` object. Please see the resource description in the API reference for more details.

## API reference

### Resource: projects.locations.retailCatalogs

JSON Representation
    
    
    {
      "name": string,
      "displayName": string,
      "createTime": string,
      "updateTime": string,
      "resourceState": enum(RetailResourceState),
      "labels": {
        string: string,
        ...
      }
    }
    

**Fields**

  
name |   
String |   
Output only. Resource name of the RetailCatalog  
---|---|---  
  
displayName |   
String |   
Optional. Display name of the RetailCatalog.  
  
createTime |   
string ([Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Timestamp) format) |   
Output only. Timestamp when this RetailCatalog was created.  
  
updateTime |   
string ([Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Timestamp) format) |   
Output only. The update timestamp.  
  
resourceState |   
enum |   
Output only. State of the RetailCatalog.  
  
labels |   
map (key: string, value: string) |   
The labels with user-defined metadata to organize your RetailCatalog.  
  
Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed.  
  
See[ https://goo.gl/xmQnxf](https://goo.gl/xmQnxf) for more information on and examples of labels.  
  
An object containing a list of "key": value pairs. Example: { "name": "wrench", "mass": "1.3kg", "count": "3" }.  
  
### Method: projects.locations.retailCatalogs.create

HTTP request

POST https://visionai.googleapis.com/v1alpha1/{parent=projects/*/locations/us-central1}/retailCatalogs

**Path parameters**

|  |   
---|---|---  
parent | string | Required. Parent identifier.  
  
**Request body**

The request body contains an instance of `RetailCatalog`.

**Response body**

If successful, the response body contains a newly created instance of `RetailCatalog`.

### Method: projects.locations.retailCatalogs.get

HTTP request

GET https://visionai.googleapis.com/v1alpha1/{name=projects/*/locations/us-central1/retailCatalogs/*}

**Path parameters**

|  |   
---|---|---  
name | string | Required. `RetailCatalog` identifier.  
  
**Request body**

The request body must be empty.

**Response body**

If successful, the response body contains an instance of `RetailCatalog`.

### Method: projects.locations.retailCatalogs.list

HTTP request

GET https://visionai.googleapis.com/v1alpha1/{parent=projects/*/locations/us-central1}/retailCatalogs

**Path parameters**

|  |   
---|---|---  
parent | string | Required. Parent identifier.  
  
**Query parameters**

filter  | string  | Optional. An expression for filtering the results of the request.  
---|---|---  
pageToken  | string  | Optional. A token identifying a page of results the server should return.  
pageSize  | integer  | Optional. Requested page size. Server may return fewer items than requested. If unspecified, server will pick an appropriate default.  
orderBy  | string  | Optional. A comma-separated list of fields to order by sorted in ascending order. Use "desc" after a field name for descending.  
  
**Request body**

The request body must be empty.

**Response body**

If successful, the response body contains data with the following structure: JSON representation
    
    
    {
      "retailCatalogs": [
        {
          object (RetailCatalog)
        }
      ],
      "nextPageToken": string
    }
    

### Method: projects.locations.retailCatalogs.delete

HTTP request

DELETE https://visionai.googleapis.com/v1alpha1/{name=projects/*/locations/us-central1/retailCatalogs/*}

**Path parameters**

|  |   
---|---|---  
name | string | Required. `RetailCatalog` identifier.  
  
**Request body**

The request body must be empty.

**Response body**

If successful, the response body contains an instance of `Operation`.

### Method: projects.locations.retailCatalogs.importRetailProducts

HTTP request

POST https://visionai.googleapis.com/v1alpha1/{name=projects/*/locations/us-central1/retailCatalogs/*}:importRetailProducts

**Path parameters**

|  |   
---|---|---  
name | string | Required. `RetailCatalog` resource name.  
  
**Request body**

JSON representation
    
    
    {
      "gcsSource": { object(GcsSource) },
      "format": enum(Format)
    }
    

**Fields**

gcsSource | object | Required. The Cloud Storage location for the input content. Multiple input locations can be provided. The contents of all input locations will be imported in one batch. Supported file extensions: 1. A JSONL file. Each line is a JSON format of RetailProductIoFormat.   
2\. A TXT file. Each line is the gtin of a Product to be imported.  
---|---|---  
format | enum | Required. The import file format.  
  
Format ENUM values

FORMAT_UNSPECIFIED | Should not be used.  
---|---  
FORMAT_TXT | TXT format.  
FORMAT_JSONL | JSONL format.  
  
**Response body**

If successful, the response body contains an instance of `Operation`.

### Resource: projects.locations.retailProducts

JSON Representation
    
    
    {
      "name": string,
      "gtins": [string],
      "normalizedGtins": [string],
      "thirdPartyIds": [ { object(ThirdPartyId) }],
      "locale": string,
      "brand": string,
      "title": string,
      "productUri": string,
      "resourceState": enum(RetailResourceState),
       "labels": {
        string: string,
        ...
        }
       "createTime": string,
       "updateTime": string
    }
    

**Fields**

  
name |   
String |   
Output only. Resource name of the RetailProductImage  
---|---|---  
  
displayName |   
String |   
Optional. Display name of the RetailProductImage.  
  
sourceType |   
enum |   
Optional. Source type  
  
gcsUri |   
string |   
Optional. Cloud Storage location of the RetailProductImage. It should be set except when the image is provided by Google, for example, when the source type is SOURCE_TYPE_GOOGLE.  
  
resourceState |   
enum |   
Output only. State of the RetailProductImage.  
  
labels |   
map (key: string, value: string) |   
The labels with user-defined metadata to organize your RetailProductImage.  
  
Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed.  
  
See[ https://goo.gl/xmQnxf](https://goo.gl/xmQnxf) for more information on and examples of labels.  
  
An object containing a list of "key": value pairs. Example: { "name": "wrench", "mass": "1.3kg", "count": "3" }.  
  
createTime |   
string ([Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Timestamp) format) |   
Output only. The create Timestamp.  
  
updateTime |   
string ([Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Timestamp) format) |   
Output only. The update timestamp.  
  
**`RetailThirdPartyId` JSON Presentation**
    
    
    {
      "id": string,
      "owner": string
    }
    

**Fields**

|  |   
---|---|---  
id  | string  | Third party id used by the retailer or manufacturer (for example,, SKU or MPN).  
owner  | string  | The entity that 'owns' the third party identifier, for example, the manufacturer or the retailer selling this product.  
  
### Method: projects.locations.retailCatalogs.retailProducts.create

HTTP request

POST https://visionai.googleapis.com/v1alpha1/{parent=projects/*/locations/*/retailCatalogs/*}/retailProducts

**Path parameters**

|  |   
---|---|---  
parent | string | Required. Parent identifier.  
  
**Request body**

The request body contains an instance of `RetailProduct`.

**Response body**

If successful, the response body contains a newly created instance of `RetailProduct`.

### Method: projects.locations.retailCatalogs.retailProducts.get

HTTP request

GET https://visionai.googleapis.com/v1alpha1/{name=projects/*/locations/*/retailCatalogs/*/retailProducts/*

**Path parameters**

|  |   
---|---|---  
name | string | Required. `RetailProduct` identifier.  
  
**Request body**

The request body must be empty.

**Response body**

If successful, the response body contains an instance of `RetailProduct`.

### Method: projects.locations.retailCatalogs.retailProducts.list

HTTP request

GET https://visionai.googleapis.com/v1alpha1/{parent=projects/*/locations/*/retailCatalogs/*}/retailProducts

**Path parameters**

|  |   
---|---|---  
parent | string | Required. Parent identifier.  
  
**Query parameters**

filter  | string  | Optional. An expression for filtering the results of the request.  
---|---|---  
pageToken  | string  | Optional. A token identifying a page of results the server should return.  
pageSize  | integer  | Optional. Requested page size. Server may return fewer items than requested. If unspecified, server will pick an appropriate default.  
orderBy  | string  | Optional. A comma-separated list of fields to order by sorted in ascending order. Use "desc" after a field name for descending.  
  
**Request body**

The request body must be empty.

**Response body**

If successful, the response body contains data with the following structure: JSON representation
    
    
    {
      "retailProducts": [
        {
          object (RetailProducts)
        }
      ],
      "nextPageToken": string
    }
    

### Method: projects.locations.retailCatalogs.retailProducts.delete

HTTP request

DELETE https://visionai.googleapis.com/v1alpha1/{name=projects/*/locations/*/retailCatalogs/*/retailProducts/*

**Path parameters**

|  |   
---|---|---  
name | string | Required. `RetailProduct` identifier.  
  
**Request body**

The request body must be empty.

**Response body**

If successful, the response body is empty.

### Resource: projects.locations.retailProductImages

JSON Representation
    
    
    {
      "name": string,
      "displayName": string,
      "sourceType": enum(SourceType),
      "gcsUri": string,
      "resourceState": enum(RetailResourceState),
       "labels": {
        string: string,
        ...
        }
       "createTime": string,
       "updateTime": string
    }
    

**Fields**

  
name |   
String |   
Output only. Resource name of the RetailProductImage  
---|---|---  
  
displayName |   
String |   
Optional. Display name of the RetailProductImage.  
  
sourceType |   
enum |   
Optional. Source type  
  
gcsUri |   
string |   
Optional. Cloud Storage location of the RetailProductImage. It should be set except when the image is provided by Google, for example, when the source type is SOURCE_TYPE_GOOGLE.  
  
resourceState |   
enum |   
Output only. State of the RetailProductImage.  
  
labels |   
map (key: string, value: string) |   
The labels with user-defined metadata to organize your RetailProductImage.  
  
Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed.  
  
See[ https://goo.gl/xmQnxf](https://goo.gl/xmQnxf) for more information on and examples of labels.  
  
An object containing a list of "key": value pairs. Example: { "name": "wrench", "mass": "1.3kg", "count": "3" }.  
  
createTime |   
string ([Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Timestamp) format) |   
Output only. The create Timestamp.  
  
updateTime |   
string ([Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Timestamp) format) |   
Output only. The update timestamp.  
  
SourceType ENUM values

SOURCE_TYPE_UNSPECIFIED | Unknown data source. Should not be used.  
---|---  
SOURCE_TYPE_FIXED_CAMERA | Image is captured from fixed camera.  
SOURCE_TYPE_HAND_HELD_CAMERA | Image is captured from hand-held camera.  
SOURCE_TYPE_CRAWLED | Image is crawled from the web.  
SOURCE_TYPE_SYSTEM_GENERATED  | Image is cropped from an original image with human labeling.  
  
### Method: projects.locations.retailCatalogs.retailProducts.retailProductImages.create

HTTP request

POST https://visionai.googleapis.com/v1alpha1/{parent=projects/*/locations/*/retailCatalogs/*/retailProducts/*}/retailProductImages

**Path parameters**

|  |   
---|---|---  
parent | string | Required. Parent identifier.  
  
**Request body**

The request body contains an instance of `RetailProductImage`.

**Response body**

If successful, the response body contains a newly created instance of `RetailProductImage`.

### Method: projects.locations.retailCatalogs.retailProducts.retailProductImages.get

HTTP request

GET https://visionai.googleapis.com/v1alpha1/{name=projects/*/locations/*/retailCatalogs/*/retailProducts/*/retailProductImages/*

**Path parameters**

|  |   
---|---|---  
name | string | Required. `RetailProductImage` identifier.  
  
**Request body**

The request body must be empty.

**Response body**

If successful, the response body contains an instance of `RetailProductImage`.

### Method: projects.locations.retailCatalogs.retailProducts.retailProductImages.list

HTTP request

GET https://visionai.googleapis.com/v1alpha1/{parent=projects/*/locations/*/retailCatalogs/*/retailProducts/*}/retailProductImages

**Path parameters**

|  |   
---|---|---  
parent | string | Required. Parent identifier.  
  
**Query parameters**

filter  | string  | Optional. An expression for filtering the results of the request.  
---|---|---  
pageToken  | string  | Optional. A token identifying a page of results the server should return.  
pageSize  | integer  | Optional. Requested page size. Server may return fewer items than requested. If unspecified, server will pick an appropriate default.  
orderBy  | string  | Optional. A comma-separated list of fields to order by sorted in ascending order. Use "desc" after a field name for descending.  
  
**Request body**

The request body must be empty.

**Response body**

If successful, the response body contains data with the following structure:

JSON representation
    
    
    {
      "retailProductImages": [
        {
          object (RetailProductImages)
        }
      ],
      "nextPageToken": string
    }
    

### Method: projects.locations.retailCatalogs.retailProducts.retailProductImages.delete

HTTP request

DELETE https://visionai.googleapis.com/v1alpha1/{name=projects/*/locations/*/retailCatalogs/*/retailProducts/*/retailProductImages/*

**Path parameters**

|  |   
---|---|---  
name | string | Required. `RetailProductImage` identifier.  
  
**Request body**

The request body must be empty.

**Response body**

If successful, the response body is empty.

### Resource: projects.locations.retailCatalogs.retailProductSets

JSON representation
    
    
    {
      "name": string,
      "displayName": string,
      "retailProductIds": [string],
      "resourceState": enum(RetailResourceState),
       "labels": {
        string: string,
        ...
        }
       "createTime": string,
       "updateTime": string
    }
    

**Fields**

  
name |   
String |   
Output only. Resource name of the RetailProductSet  
---|---|---  
  
displayName |   
String |   
Optional. Display name of the RetailProductSet.  
  
retailProductIds [] |   
String |   
Output only. Resource ids of products belonging to this RetailProductSet. The products in a RetailProductSet should be in the same catalog.  
  
resourceState |   
enum |   
Output only. State of the RetailProductSet.  
  
labels |   
map (key: string, value: string) |   
The labels with user-defined metadata to organize your RetailProductSet.  
  
Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed.  
  
See[ https://goo.gl/xmQnxf](https://goo.gl/xmQnxf) for more information on and examples of labels.  
  
An object containing a list of "key": value pairs. Example: { "name": "wrench", "mass": "1.3kg", "count": "3" }.  
  
createTime |   
string ([Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Timestamp) format) |   
Output only. The create Timestamp.  
  
updateTime |   
string ([Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Timestamp) format) |   
Output only. The update timestamp.  
  
### Method: projects.locations.retailCatalogs.retailProductSets.create

HTTP request

POST https://visionai.googleapis.com/v1alpha1/{parent=projects/*/locations/*/retailCatalogs/*}/retailProductSets

**Path parameters**

|  |   
---|---|---  
parent | string | Required. Parent identifier.  
  
**Request body**

The request body contains an instance of RetailProductSet.

**Response body**

If successful, the response body contains a newly created instance of RetailProductSet.

### Method: projects.locations.retailCatalogs.retailProductSets.get

HTTP request

GET https://visionai.googleapis.com/v1alpha1/{name=projects/*/locations/*/retailCatalogs/*/retailProductSets/*

**Path parameters**

|  |   
---|---|---  
name | string | Required. RetailProductSet identifier.  
  
**Request body**

The request body must be empty.

**Response body**

If successful, the response body contains an instance of RetailProductSet.

### Method: projects.locations.retailCatalogs.retailProductSets.list

HTTP request

GET https://visionai.googleapis.com/v1alpha1/{parent=projects/*/locations/*/retailCatalogs/*}/retailProductSets

**Path parameters**

|  |   
---|---|---  
parent | string | Required. Parent identifier.  
  
**Query parameters**

filter  | string  | Optional. An expression for filtering the results of the request.  
---|---|---  
pageToken  | string  | Optional. A token identifying a page of results the server should return.  
pageSize  | integer  | Optional. Requested page size. Server may return fewer items than requested. If unspecified, server will pick an appropriate default.  
orderBy  | string  | Optional. A comma-separated list of fields to order by sorted in ascending order. Use "desc" after a field name for descending.  
  
**Request body**

The request body must be empty.

**Response body**

If successful, the response body contains data with the following structure:

JSON representation
    
    
    {
      "retailProductSets": [
        {
          object (RetailProductSets)
        }
      ],
      "nextPageToken": string
    }
    

### Method: projects.locations.retailCatalogs.retailProductSets.delete

HTTP request

DELETE https://visionai.googleapis.com/v1alpha1/{name=projects/*/locations/*/retailCatalogs/*/retailProductSets/*

**Path parameters**

|  |   
---|---|---  
name | string | Required. RetailProductSet identifier.  
  
**Request body**

The request body must be empty.

**Response body**

If successful, the response body is empty.

### Method: projects.locations.retailCatalogs.retailProductSets.add

HTTP request

POST https://visionai.googleapis.com/v1alpha1/{name=projects/*/locations/*/retailCatalogs/*/retailProductSets/*}:remove

**Path parameters**

|  |   
---|---|---  
name | string | Required. RetailProductSet resource name.  
  
**Request body**

JSON representation
    
    
    {
      "productIds": [string],
      "productFilter": string
    }
    

**Fields**

  
productIds[ ] |   
string |   
Resource id of the RetailProducts to be added. They must all belong to the same RetailCatalog as the specified destination RetailProductSet. Up to 200 RetailProducts ids can be specified in one request. Can not be used together with productFilter.  
---|---|---  
  
productFilter |   
string |   
A standard filter that will be applied to all RetailProducts in the parent RetailCatalog, select items which satisfy filter conditions and add them into the RetailProductSet. Cannot be used together with product_ids. Supported filters: <https://google.aip.dev/160>  
  
**Response body**

If successful, the response body contains an instance of `Operation`.

### Method: projects.locations.retailCatalogs.retailProductSets.remove

HTTP request

POST https://visionai.googleapis.com/v1alpha1/{name=projects/*/locations/*/retailCatalogs/*/retailProductSets/*}:add

**Path parameters**

|  |   
---|---|---  
name | string | Required. RetailProductSet resource name.  
  
**Request body**

JSON representation
    
    
    {
      "productIds": [string],
      "productFilter": string
    }
    

**Fields**

  
productIds[ ] |   
string |   
Resource ids of the RetailProducts to be removed. If the specified RetailProducts does not belong to this RetailProductSet, it will be ignored. Up to 200 RetailProducts ids can be specified in one request. Can not be used together with products_filter.  
---|---|---  
  
productFilter |   
string |   
A standard filter that will be applied to all RetailProducts in the specified RetailProductSet, select items which satisfy filter conditions and remove them from the RetailProductSet. Cannot be used together with product_ids. Supported filters:<https://google.aip.dev/160>  
  
**Response body**

If successful, the response body contains an instance of `Operation`.

### Resource: projects.locations.retailCatalogs.retailProductRecognitionIndexes

JSON representation
    
    
    {
      "name": string,
      "displayName": string,
      "description": string,
      "retailProductSet": [string],
       "resourceState": enum(RetailResourceState),
       "labels": {
        string: string,
        ...
        }
       "createTime": string,
       "updateTime": string
    }
    

**Fields**

  
name |   
String |   
Output only. Resource name of the RetailProductRecognitionIndex resource.  
---|---|---  
  
displayName |   
String |   
Optional. Display name of the RetailProductRecognitionIndex.  
  
description |   
String |   
Optional. The description of the RetailProductRecognitionIndex.  
  
retailProductSet[] |   
string |   
Optional. The resource name of RetailProductSet to use for creating this resource. If set, the RetailProductRecognitionIndex will only contain products in the given RetailProductSet. If not set, all products in the parent catalog will be used.  
  
resourceState |   
enum |   
Output only. State of the RetailProductRecognitionIndex.  
  
labels |   
map (key: string, value: string) |   
The labels with user-defined metadata to organize your RetailProductRecognitionIndex.  
  
Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed.  
  
See[ https://goo.gl/xmQnxf](https://goo.gl/xmQnxf) for more information on and examples of labels.  
  
An object containing a list of "key": value pairs. Example: { "name": "wrench", "mass": "1.3kg", "count": "3" }.  
  
createTime |   
string ([Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Timestamp) format) |   
Output only. The create Timestamp.  
  
updateTime |   
string ([Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Timestamp) format) |   
Output only. The update timestamp.  
  
### Method: projects.locations.retailCatalogs.retailProductRecognitionIndexes.create

HTTP request

POST https://visionai.googleapis.com/v1alpha1/{parent=projects/*/locations/*/retailCatalogs/*}/retailProductRecognitionIndexes

**Path parameters**

|  |   
---|---|---  
parent | string | Required. Parent identifier.  
  
**Request body**

The request body contains an instance of `RetailProductRecognitionIndex`.

**Response body**

If successful, the response body contains a newly created instance of `RetailProductRecognitionIndex`.

### Method: projects.locations.retailCatalogs.retailProductRecognitionIndexes.get

HTTP request

GET https://visionai.googleapis.com/v1alpha1/{name=projects/*/locations/*/retailCatalogs/*/retailProductRecognitionIndexes/*

**Path parameters**

|  |   
---|---|---  
name | string | Required. `RetailProductRecognitionIndex` identifier.  
  
**Request body**

The request body must be empty.

**Response body**

If successful, the response body contains an instance of `RetailProductRecognitionIndex`.

### Method: projects.locations.retailCatalogs.retailProductRecognitionIndexes.list

HTTP request

GET https://visionai.googleapis.com/v1alpha1/{parent=projects/*/locations/*/retailCatalogs/*}/retailProductRecognitionIndexes

**Path parameters**

|  |   
---|---|---  
parent | string | Required. Parent identifier.  
  
**Query parameters**

filter  | string  | Optional. An expression for filtering the results of the request.  
---|---|---  
pageToken  | string  | Optional. A token identifying a page of results the server should return.  
pageSize  | integer  | Optional. Requested page size. Server may return fewer items than requested. If unspecified, server will pick an appropriate default.  
orderBy  | string  | Optional. A comma-separated list of fields to order by sorted in ascending order. Use "desc" after a field name for descending.  
  
**Request body**

The request body must be empty.

**Response body**

If successful, the response body contains data with the following structure:

JSON representation
    
    
    {
      "retailProductRecognitionIndexes": [
        {
          object (RetailProductRecognitionIndex)
        }
      ],
      "nextPageToken": string
    }
    

### Method: projects.locations.retailCatalogs.retailProductRecognitionIndexes.delete

HTTP request

DELETE https://visionai.googleapis.com/v1alpha1/{name=projects/*/locations/*/retailCatalogs/*/retailProductRecognitionIndexes/*

**Path parameters**

|  |   
---|---|---  
name | string | Required. ProductRecognitionIndex identifier.  
  
**Request body**

The request body must be empty.

**Response body**

If successful, the response body contains an instance of `Operation`.

### Resource: projects.locations.retailEndpoints

JSON representation
    
    
    {
      "name": string,
      "displayName": string,
      "description": string,
      "deployedProductRecognitionIndex": string,
      "resourceState": enum(RetailResourceState),
      "productRecognitionConfig": { object(RetailProductRecognitionConfig) },
      "tagRecognitionConfig": { object(RetailTagRecognitionConfig) },
      "labels": {
        string: string,
        ...
       }
      "createTime": string,
      "updateTime": string
    }
    

**Fields**

  
name |   
String |   
Output only. Resource name of the RetailEndpoint resource.  
---|---|---  
  
displayName |   
String |   
Optional. Display name of the RetailEndpoint.  
  
description |   
String |   
Optional. The description of the RetailEndpoint.  
  
deployedProductRecognitionIndex |   
String |   
Output only. Resource name of the ProductRecognitionIndex deployed to this RetailEndpoint.  
  
productRecognitionConfig |   
object |   
Optional. Configuration for product recognition.  
  
tagRecognitionConfig |   
object |   
Optional. Configuration for tag recognition.  
  
resourceState |   
enum |   
Output only. State of the RetailProductRecognitionIndex.  
  
labels |   
map (key: string, value: string) |   
The labels with user-defined metadata to organize your RetailProductRecognitionIndex.  
  
Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed.  
  
See[ https://goo.gl/xmQnxf](https://goo.gl/xmQnxf) for more information on and examples of labels.  
  
An object containing a list of "key": value pairs. Example: { "name": "wrench", "mass": "1.3kg", "count": "3" }.  
  
createTime |   
string ([Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Timestamp) format) |   
Output only. The create Timestamp.  
  
updateTime |   
string ([Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Timestamp) format) |   
Output only. The update timestamp.  
  
### RetailProductRecognitionConfig

JSON representation
    
    
    {
      "productDetectionModel": string,
      "detectionConfidenceThreshold": float,
      "recognitionConfidenceThreshold": float,
      "additionalConfig": { object }
    }
    

**Fields**

|

productDetectionModel | string | Required. Model to use to detect products in input images. Supported values: "builtin/stable" (the default) or Vertex AI model resource name.  
---|---|---  
detectionConfidenceThreshold | float | Optional. Confidence threshold to filter detection results. If not set, a system default value will be used.  
recognitionConfidenceThreshold | float | Optional. Confidence threshold to filter recognition results. If not set, a system default value will be used.  
additionalConfig | object ([Struct](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Struct) format) | Optional. Additional configurations for product recognition.  
  
### RetailTagRecognitionConfig

JSON representation
    
    
    {
      "tagDetectionModel": string,
      "tagParsingModel": string,
      "detectionConfidenceThreshold": float,
      "parsingConfidenceThreshold": float,
      "additionalConfig": { object }
    }
    

**Fields**

tagDetectionModel | string | Required. Model to use to detect tags in input images. Supported values: Vertex AI model resource.  
---|---|---  
tagParsingModel | string | Required. Model to parse text on detected tags. Supported values: Vertex AI model resource.  
detectionConfidenceThreshold | float | Optional. Confidence threshold to filter detection results. If not set, a system default value will be used.  
parsingConfidenceThreshold | float | Optional. Confidence threshold to filter text parsing results. If not set, a system default value will be used.  
additionalConfig | object ([Struct](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Struct) format) | Optional. Additional configurations for tag recognition.  
  
### Method: projects.locations.retailEndpoints.create

HTTP request

POST https://visionai.googleapis.com/v1alpha1/{parent=projects/*/locations/*}/retailEndpoints

**Path parameters**

|  |   
---|---|---  
parent | string | Required. Parent identifier.  
  
**Request body**

The request body contains an instance of `RetailEndpoint`.

**Response body**

If successful, the response body contains a newly created instance of `RetailEndpoint`.

### Method: projects.locations.retailEndpoints.get

HTTP request

GET https://visionai.googleapis.com/v1alpha1/{name=projects/*/locations/*/retailEndpoints/*}

**Path parameters**

|  |   
---|---|---  
name | string | Required. `RetailEndpoint` identifier.  
  
**Request body**

The request body must be empty.

**Response body**

If successful, the response body contains an instance of `RetailEndpoint`.

### Method: projects.locations.retailEndpoints.list

HTTP request

GET https://visionai.googleapis.com/v1alpha1/{parent=projects/*/locations/*}/retailEndpoints

**Path parameters**

|  |   
---|---|---  
parent | string | Required. Parent identifier.  
  
**Query parameters**

filter  | string  | Optional. An expression for filtering the results of the request.  
---|---|---  
pageToken  | string  | Optional. A token identifying a page of results the server should return.  
pageSize  | integer  | Optional. Requested page size. Server may return fewer items than requested. If unspecified, server will pick an appropriate default.  
orderBy  | string  | Optional. A comma-separated list of fields to order by sorted in ascending order. Use "desc" after a field name for descending.  
  
**Request body**

The request body must be empty.

**Response body**

If successful, the response body contains data with the following structure:

JSON representation
    
    
    {
      "retailEndpoints": [
        {
          object (RetailEndpoint)
        }
      ],
      "nextPageToken": string
    }
    

### Method: projects.locations.retailEndpoints.delete

HTTP request

DELETE https://visionai.googleapis.com/v1alpha1/{name=projects/*/locations/*/retailEndpoints/*

**Path parameters**

|  |   
---|---|---  
name | string | Required. `RetailEndpoint` identifier.  
  
**Request body**

The request body must be empty.

**Response body**

If successful, the response body is empty.

### Method: projects.locations.retailEndpoints.deployRetailProductRecognitionIndex

HTTP request

POST https://visionai.googleapis.com/v1alpha1/{retailEndpoint=projects/*/locations/*/retailEndpoints/*}:deployRetailProductRecognitionIndex

**Path parameters**

|  |   
---|---|---  
retailEndpoint  | string  | Required. Resource name of the `RetailEndpoint` resource into where the `RetailProductRecognitionIndex` is deployed.  
  
**Request body**

JSON representation
    
    
    {
      "retailProductRecognitionIndex": string,
    }
    

**Fields**

|  |   
---|---|---  
retailProductRecognitionIndex  | string  | Required. The resource name of `RetailProductRecognitionIndex` to deploy.  
  
**Response body**

If successful, the response body contains an instance of `Operation`.

### Method: projects.locations.retailEndpoints.undeployRetailProductRecognitionIndex

HTTP request

POST https://visionai.googleapis.com/v1alpha1/{retailEndpoint=projects/*/locations/*/retailEndpoints/*}:undeployRetailProductRecognitionIndex

**Path parameters**

|  |   
---|---|---  
retailEndpoint  | string  | Required. Resource name of the `RetailEndpoint` resource on which the undeployment will act.  
  
**Request body**

The request body must be empty.

**Response body**

If successful, the response body contains an instance of `Operation`.

### Method: projects.locations.retailEndpoints.batchAnalyze

HTTP request

POST https://visionai.googleapis.com/v1alpha1/{retailEndpoint=projects/*/locations/*/retailEndpoints/*}:batchAnalyze

**Path parameters**

|  |   
---|---|---  
retailEndpoint  | string  | Required. Resource name of the `RetailEndpoint` to serve the inference request.  
  
**Request body**

JSON representation
    
    
    {
      "gcsSource": string,
      "features": { object(Feature) },
      // Union field output can be only one of the following:
      "outputGcsDestination": string,
      "corpus": string,
      // End of list of possible types for union field output.
      "bigqueryTable": string
    }
    

**Fields**

gcsSource | string | Required. The Cloud Storage location for the input content. Multiple input locations can be provided. The contents of all input locations will be processed in one batch. Supported content: A TXT file, each line is the full path to an image. A maximum of 50k images can be supported in one request.  
---|---|---  
outputGcsDestination | string | Optional. The Cloud Storage location of the directory where the output is to be written to.  
corpus | string | Optional. Resource name of image warehouse corpus. Not yet supported.  
bigqueryTable | string | Optional. Resource name of the bigquery table for annotation exports. In the format of "projects/*/datasets/*/tables/*". If set, annotations generated from ML inference will also be exported to the given bigquery table. Not yet supported.  
features[] | Object  | Required. The type of ML inference to perform.  
  
Feature

JSON representation
    
    
    {
      "type": enum(Type),
      "productRecognitionConfig": object(RetailProductRecognitionConfig),
      "tagRecognitionConfig": object(RetailTagRecognitionConfig)
    }
    

**Fields**

type | enum | Required. The Feature Type.  
---|---|---  
productRecognitionConfig  | object  | Optional. Per request overrides for product recognition feature. It's effective only if type is set to TYPE_PRODUCT_RECOGNITION.  
tagRecognitionConfig  | object  | Optional. Per request overrides for tag recognition feature. It's effective only if type is set to TYPE_TAG_RECOGNITION.  
  
**Response body**

If successful, the response body contains an instance of `Operation`.

Types

`GcsSource`

JSON representation
    
    
    {
      "uris": [string]
    }
    

**Fields**

|  |   
---|---|---  
uris[] | string | Required. References to a Cloud Storage paths.  
  
Type

ENUM values

TYPE_UNSPECIFIED | The default value. Should not be used.  
---|---  
TYPE_PRODUCT_RECOGNITION  | Product Recognition. Must be used on a `RetailEndpoint` with deployed `RetailProductRecognitionIndex`.  
TYPE_TAG_RECOGNITION  | Tag Detection and Parsing. Must be used on a `RetailEndpoint` with RetailTagRecognitionConfig.  
  
### RetailProductIoFormat

JSON representation
    
    
    {
      "retailProduct": { object(RetailProduct) },
      "retailProductImages": [ { object(RetailProductImage) }]
    }
    

**Fields**

retailProduct | object | Required. `RetailProduct` to be imported  
---|---|---  
retailProductImages[ ]  | object  | Optional. `RetailProductImage`s of the given `RetailProduct` to be imported.  
  
`RetailResourceState`

ENUM values

RETAIL_RESOURCE_STATE_UNSPECIFIED  | The default value. Should not be used.  
---|---  
RETAIL_RESOURCE_STATE_CREATING | State Creating.  
RETAIL_RESOURCE_STATE_CREATED | State Created.  
RETAIL_RESOURCE_STATE_UPDATING | State Updating.  
RETAIL_RESOURCE_STATE_DELETED | State Deleted.  
RETAIL_RESOURCE_STATE_ERROR | State Error.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
