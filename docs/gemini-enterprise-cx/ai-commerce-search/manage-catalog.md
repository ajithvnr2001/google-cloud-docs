---
url: https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/manage-catalog/
title: Manage catalog information \u00a0|\u00a0 AI Commerce Search in Gemini Enterprise for Customer Experience \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:36:17.235965+00:00
---

# Manage catalog information  |  AI Commerce Search in Gemini Enterprise for Customer Experience  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/manage-catalog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ AI Commerce Search ](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search)



Send feedback 

#  Manage catalog information Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to manage your product information after you have imported a catalog into AI Commerce Search. You can read, write, and delete products in your catalog.

To keep your catalog up to date as product information changes, import your catalog the same way as the very first time. For help with importing your catalog, see [Importing catalog information](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/upload-catalog).

## Create, access, and manage product tutorials

This tutorial shows you how to use the API methods, which perform the following actions:

  * Create a product
  * Get a product
  * Update a product
  * Delete a product



* * *

To follow step-by-step guidance for this task directly in the Cloud Shell Editor, click **Guide me** : 

[Guide me](https://shell.cloud.google.com/?walkthrough_tutorial_id=retail--retail_api_v2_crud_select_language&show=ide&environment_deployment=ide)

* * *

### Create product

This tutorial shows you how to create a single product.

* * *

To follow step-by-step guidance for this task directly in the Cloud Shell Editor, click **Guide me** : 

[Guide me](https://shell.cloud.google.com/?walkthrough_tutorial_id=retail--retail_api_v2_create_product_select_language&show=ide&environment_deployment=ide)

* * *

### Get product

This tutorial shows you how to retrieve a product item.

* * *

To follow step-by-step guidance for this task directly in the Cloud Shell Editor, click **Guide me** : 

[Guide me](https://shell.cloud.google.com/?walkthrough_tutorial_id=retail--retail_api_v2_get_product_select_language&show=ide&environment_deployment=ide)

* * *

### Update product

This tutorial shows you how to update a product in a catalog.

* * *

To follow step-by-step guidance for this task directly in the Cloud Shell Editor, click **Guide me** : 

[Guide me](https://shell.cloud.google.com/?walkthrough_tutorial_id=retail--retail_api_v2_update_product_select_language&show=ide&environment_deployment=ide)

* * *

### Delete product

This tutorial shows you how to delete a product from a catalog.

* * *

To follow step-by-step guidance for this task directly in the Cloud Shell Editor, click **Guide me** : 

[Guide me](https://shell.cloud.google.com/?walkthrough_tutorial_id=retail--retail_api_v2_delete_product_select_language&show=ide&environment_deployment=ide)

* * *

## Upload a single product item

### curl

Create a single product item by using the [`products.create`](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.branches.products/create) REST method. 
    
    
    curl -X POST \
         -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
         -H "Content-Type: application/json; charset=utf-8" \
         --data '{
          "title": "PRODUCT_TITLE",
          "categories": "CATEGORY"
        }' \
        "https://retail.googleapis.com/v2/projects/PROJECT_NUMBER/locations/global/catalogs/default_catalog/branches/0/products?productId=PRODUCT_ID"

If the request is successful, the product object is returned, such as in the following example.
    
    
    {
      "name": "projects/PROJECT_NUMBER/locations/global/catalogs/default_catalog/branches/0/products/PRODUCT_ID",
      "id": "PRODUCT_ID",
      "primaryProductId": "PRODUCT_ID",
      "type": "PRIMARY",
      "categories": \[
        "CATEGORY"
      \],
      "title": "PRODUCT_TITLE",
      "availability": "IN_STOCK"
    }

### Java
    
    
    public static Product createProduct(Product productToCreate, String productId)
        throws IOException {
      return getProductServiceClient().createProduct(
          DEFAULT_BRANCH_NAME, productToCreate, productId
      );
    }

## Update product information

As your product catalog changes, you can refresh your catalog by uploading changes in products such as new products, prices, and stock status in real time. You can upload only products that have been added or changed; you don't need to reload your entire catalog.

### curl

Update product information by using the [`products.patch`](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.branches.products/patch) method. 

The following example updates the title for a specific product:
    
    
    curl -X PATCH \
        -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
        -H "Content-Type: application/json; charset=utf-8" \
        --data "{
           "title": "new-title-value"
        }" \
        "https://retail.googleapis.com/v2/projects/PROJECT_NUMBER/locations/global/catalogs/default_catalog/branches/0/products/PRODUCT_ID?updateMask=title"

If the request is successful, the product object is returned, such as in the following example.
    
    
    {
      "name": "projects/PROJECT_NUMBER/locations/global/catalogs/default_catalog/branches/0/products/PRODUCT_ID",
      "id": "PRODUCT_ID",
      "primaryProductId": "PRODUCT_ID",
      "type": "PRIMARY",
      "categories": \[
        "Parent category > Child category"
      \],
      "title": "new product title",
      "availability": "IN_STOCK"
    }

### Java
    
    
    public static Product updateProduct(Product productToUpdate) throws IOException {
      return getProductServiceClient().updateProduct(productToUpdate, FieldMask.getDefaultInstance());
    }

## Delete product information

Although the API provides a way to delete products from your catalog, keep in mind that if you record a user event that relates to a product item that has been deleted, the API cannot process the user event properly and it might be deleted. In addition, including historical catalog data improves the quality of your model and is critical for good recommendations and search results.

You should set the `availability` of obsolete products to `OUT_OF_STOCK` rather than deleting them.

### curl

Delete a product by using the [`delete`](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.branches.products/delete) method, replacing PRODUCT_ID with the ID of the product you want to delete.
    
    
    curl -X DELETE \
         -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
        "https://retail.googleapis.com/v2/projects/PROJECT_NUMBER/locations/global/catalogs/default_catalog/branches/0/products/PRODUCT_ID"

### Java
    
    
    public static void deleteProduct(String productName) throws IOException {
      getProductServiceClient().deleteProduct(productName);
    }

## Retrieve a product item

### curl

You retrieve a product item by making a `GET` request to the [`products`](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.branches.products) endpoint, replacing PRODUCT_ID with the ID of the product you want to retrieve:
    
    
    curl -X GET \
         -H "Authorization: Bearer $(gcloud auth application-default print-access-token)"  \
        "https://retail.googleapis.com/v2/projects/PROJECT_NUMBER/locations/global/catalogs/default_catalog/branches/0/products/PRODUCT_ID"

You should see output similar to the following:
    
    
    {
        "name": "projects/PROJECT_NUMBER/locations/global/catalogs/default_catalog/branches/0/products/PRODUCT_ID"
        "id": "PRODUCT_ID",
        "primaryProductId": "PRODUCT_ID",
        "type": "PRIMARY",
        "categories": \[
          "Parent category > Child category"
        \],
        "title": "product title",
        "availability": "IN_STOCK"
    }

### Java
    
    
    public static Product getProduct(String productName) throws IOException {
      return getProductServiceClient().getProduct(productName);
    }

## View aggregated information about your catalog

You can view aggregated information about your catalog and preview uploaded products under the **Catalog** tab in the [**Data**](https://console.cloud.google.com/ai/retail/catalogs/default_catalog/data/) page of the AI Commerce Search in Gemini Enterprise for Customer Experience console.

## Assess catalog data quality

To assess the quality of your catalog data:

  1. Go to the **Data quality** page in the AI Commerce Search in Gemini Enterprise for Customer Experience console.  
  
[Go to the Data quality page](https://console.cloud.google.com/ai/retail/catalogs/default_catalog/data_quality/)

The [**Data quality** page](https://console.cloud.google.com/ai/retail/catalogs/default_catalog/data_quality/) assesses if you need to update catalog data to improve the quality of your search results and unlock search performance tiers.




For more about how to check search data quality and view search performance tiers, see [Unlock search performance tiers](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/data-quality).

For a summary of available catalog metrics, see [Catalog quality metrics](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/catalog#quality-metrics).

## Change product types

When importing a product, you can specify if the product's type is primary, variant, or a collection. If a product's type changes or was specified incorrectly, you must delete the product and [create it](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/catalog#single) it with the updated type specified.

A product's type can be set to `TYPE_UNSPECIFIED`, `PRIMARY`, `VARIANT`, or `COLLECTION`. For more details, see [`product.Type`](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.branches.products#Product.Type) in the reference documentation.

## Change product level configuration

**Deprecated:** The Merchant Center connector is deprecated and only available to current users. New users must use the Catalog API or BigQuery to import catalogs. Only customers with prior access can use the feature. If you're an existing customer and have access to Merchant Center, then continue reading.

To import a catalog with Merchant Center, you must specify if the products are primaries or variants.

If the [product levels](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/catalog#product-levels) change or were specified incorrectly, use this procedure to correct their configuration. You must have the **Retail Admin** IAM role to complete this procedure.

  1. Make sure no imports are occurring while you reconfigure the product levels. This verifies that data does not get uploaded at the wrong level.

  2. Delete all product items. See [`products.delete`](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.branches.products/delete). The catalog must be completely empty before proceeding to the next step.

  3. Re-import your data to change the product level configuration.

This procedure depends on how you import. Follow the appropriate procedure in [Import Catalog Information](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/upload-catalog) to set the product levels to their new configuration.

  4. Finish importing the new catalog with the modified level configuration, using your chosen procedure in [Import Catalog Information](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/upload-catalog).

  5. Tune all existing models.

To tune a model, go to the [Models page](https://console.cloud.google.com/ai/retail/catalogs/default_catalog/models/), click the model name to view its details page, then click **Manual Tune** in the button bar.

[ Go to the Models page ](https://console.cloud.google.com/ai/retail/catalogs/default_catalog/models/)

For tuning cost details, see [Pricing](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/pricing).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
