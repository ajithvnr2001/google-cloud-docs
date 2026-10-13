---
url: https://docs.cloud.google.com/cpp/docs/reference/vision/latest/classgoogle_1_1cloud_1_1vision__v1_1_1ProductSearchConnection/
title: Class ProductSearchConnection (3.13.0-rc) \u00a0|\u00a0 C++ client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:22:40.185381+00:00
---

# Class ProductSearchConnection (3.13.0-rc)  |  C++ client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cpp/docs/reference/vision/latest/classgoogle_1_1cloud_1_1vision__v1_1_1ProductSearchConnection/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ C++ ](https://docs.cloud.google.com/cpp/docs)
  * [ Client libraries ](https://docs.cloud.google.com/cpp/docs/reference)



Send feedback 

#  Class ProductSearchConnection (3.13.0-rc) Stay organized with collections  Save and categorize content based on your preferences. 

3.13.0-rc  3.12.0 (latest)  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  2.48.0-rc  2.47.1  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.40.0  2.39.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.0  2.27.0  2.26.0  2.25.1  2.24.0  2.23.0  2.22.1  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.1  2.14.0  2.13.0  2.12.0  2.11.0 

The [`ProductSearchConnection`](https://docs.cloud.google.com/cpp/docs/reference/vision/latest/classgoogle_1_1cloud_1_1vision__v1_1_1ProductSearchConnection) object for [`ProductSearchClient`](https://docs.cloud.google.com/cpp/docs/reference/vision/latest/classgoogle_1_1cloud_1_1vision__v1_1_1ProductSearchClient). 

This interface defines virtual methods for each of the user-facing overload sets in [`ProductSearchClient`](https://docs.cloud.google.com/cpp/docs/reference/vision/latest/classgoogle_1_1cloud_1_1vision__v1_1_1ProductSearchClient). This allows users to inject custom behavior (e.g., with a Google Mock object) when writing tests that use objects of type [`ProductSearchClient`](https://docs.cloud.google.com/cpp/docs/reference/vision/latest/classgoogle_1_1cloud_1_1vision__v1_1_1ProductSearchClient).

To create a concrete instance, see [`MakeProductSearchConnection()`](https://docs.cloud.google.com/cpp/docs/reference/vision/latest/namespacegoogle_1_1cloud_1_1vision__v1).

For mocking, see [`vision_v1_mocks::MockProductSearchConnection`](https://docs.cloud.google.com/cpp/docs/reference/vision/latest/classgoogle_1_1cloud_1_1vision__v1__mocks_1_1MockProductSearchConnection). 

## Functions 

### virtual options()

**Returns**  
---  
**Type** | **Description**  
`Options` |   
  
### virtual CreateProductSet(google::cloud::vision::v1::CreateProductSetRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::vision::v1::CreateProductSetRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::vision::v1::ProductSet >` |   
  
### virtual ListProductSets(google::cloud::vision::v1::ListProductSetsRequest)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::vision::v1::ListProductSetsRequest`   
  
**Returns**  
---  
**Type** | **Description**  
`StreamRange< google::cloud::vision::v1::ProductSet >` |   
  
### virtual GetProductSet(google::cloud::vision::v1::GetProductSetRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::vision::v1::GetProductSetRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::vision::v1::ProductSet >` |   
  
### virtual UpdateProductSet(google::cloud::vision::v1::UpdateProductSetRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::vision::v1::UpdateProductSetRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::vision::v1::ProductSet >` |   
  
### virtual DeleteProductSet(google::cloud::vision::v1::DeleteProductSetRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::vision::v1::DeleteProductSetRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`Status` |   
  
### virtual CreateProduct(google::cloud::vision::v1::CreateProductRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::vision::v1::CreateProductRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::vision::v1::Product >` |   
  
### virtual ListProducts(google::cloud::vision::v1::ListProductsRequest)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::vision::v1::ListProductsRequest`   
  
**Returns**  
---  
**Type** | **Description**  
`StreamRange< google::cloud::vision::v1::Product >` |   
  
### virtual GetProduct(google::cloud::vision::v1::GetProductRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::vision::v1::GetProductRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::vision::v1::Product >` |   
  
### virtual UpdateProduct(google::cloud::vision::v1::UpdateProductRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::vision::v1::UpdateProductRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::vision::v1::Product >` |   
  
### virtual DeleteProduct(google::cloud::vision::v1::DeleteProductRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::vision::v1::DeleteProductRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`Status` |   
  
### virtual CreateReferenceImage(google::cloud::vision::v1::CreateReferenceImageRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::vision::v1::CreateReferenceImageRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::vision::v1::ReferenceImage >` |   
  
### virtual DeleteReferenceImage(google::cloud::vision::v1::DeleteReferenceImageRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::vision::v1::DeleteReferenceImageRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`Status` |   
  
### virtual ListReferenceImages(google::cloud::vision::v1::ListReferenceImagesRequest)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::vision::v1::ListReferenceImagesRequest`   
  
**Returns**  
---  
**Type** | **Description**  
`StreamRange< google::cloud::vision::v1::ReferenceImage >` |   
  
### virtual GetReferenceImage(google::cloud::vision::v1::GetReferenceImageRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::vision::v1::GetReferenceImageRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::vision::v1::ReferenceImage >` |   
  
### virtual AddProductToProductSet(google::cloud::vision::v1::AddProductToProductSetRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::vision::v1::AddProductToProductSetRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`Status` |   
  
### virtual RemoveProductFromProductSet(google::cloud::vision::v1::RemoveProductFromProductSetRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::vision::v1::RemoveProductFromProductSetRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`Status` |   
  
### virtual ListProductsInProductSet(google::cloud::vision::v1::ListProductsInProductSetRequest)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::vision::v1::ListProductsInProductSetRequest`   
  
**Returns**  
---  
**Type** | **Description**  
`StreamRange< google::cloud::vision::v1::Product >` |   
  
### virtual ImportProductSets(google::cloud::vision::v1::ImportProductSetsRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::vision::v1::ImportProductSetsRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::vision::v1::ImportProductSetsResponse > >` |   
  
### virtual ImportProductSets(NoAwaitTag, google::cloud::vision::v1::ImportProductSetsRequest const &)

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::vision::v1::ImportProductSetsRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### virtual ImportProductSets(google::longrunning::Operation const &)

**Parameter**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::vision::v1::ImportProductSetsResponse > >` |   
  
### virtual PurgeProducts(google::cloud::vision::v1::PurgeProductsRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::vision::v1::PurgeProductsRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::vision::v1::BatchOperationMetadata > >` |   
  
### virtual PurgeProducts(NoAwaitTag, google::cloud::vision::v1::PurgeProductsRequest const &)

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::vision::v1::PurgeProductsRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### virtual PurgeProducts(google::longrunning::Operation const &)

**Parameter**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::vision::v1::BatchOperationMetadata > >` |   
  
### virtual GetOperation(google::longrunning::GetOperationRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::longrunning::GetOperationRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
