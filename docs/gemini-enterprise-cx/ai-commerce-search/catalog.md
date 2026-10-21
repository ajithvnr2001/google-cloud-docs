---
url: https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/catalog/
title: About catalogs and products \u00a0|\u00a0 AI Commerce Search in Gemini Enterprise for Customer Experience \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:38:58.272667+00:00
---

# About catalogs and products  |  AI Commerce Search in Gemini Enterprise for Customer Experience  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/catalog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ AI Commerce Search ](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search)



Send feedback 

#  About catalogs and products Stay organized with collections  Save and categorize content based on your preferences. 

This page provides best practices for creating your catalog information and populating your catalog data.

## Overview

The catalog is a collection of product objects.

The catalog data you import into AI Commerce Search has a direct effect on the quality of the resulting model, and therefore on the quality of search and recommendation results. In general, the more accurate and specific catalog information you can provide, the higher quality your model.

Your catalog should be kept up to date. You can upload catalog changes as often as needed; ideally, every day for catalogs with a high rate of change. You can upload (patch) existing product items; only the changed fields are updated. There is no charge for uploading catalog information. For more information, see [Keeping your catalog up to date](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/upload-catalog#current).

**Note:** There is only one catalog per Google Cloud project. It is named `default_catalog`. You don't need to create the default catalog; it is there by default.

## Catalog branches

**Warning:** If you use recommendations, do not use multiple catalog branches. Branch switching can negatively impact prediction results.

### Catalog branches with search

If you use search, you can use catalog branches to test new data that you've uploaded offline before making it live on your site.

You can use up to three branches, identified as `0`, `1`, and `2`. Your live site points to `default_branch` for its catalog data. Specify which branch is your live `default_branch` (the default is set to branch `0`) using either `setDefaultBranch` or the Data tab in AI Commerce Search in Gemini Enterprise for Customer Experience console. Your site then uses the catalog data provided by the branch that `default_branch` points to.

As an example, say `default_branch` is set to branch ID `0`, so your site is using the catalog data that you've uploaded to that branch. You can upload new catalog data to branch `1` and preview it. After you've confirmed that the catalog has been uploaded correctly, you can switch to branch `1` as the live `default_branch`.

The catalog cache can take up to 30 minutes to update after branch switching.

If you use recommendations, use only the default branch due to the update delay during branch switching. If the data difference between branches is large, update delay can negatively impact prediction results.

## Required product information

The following fields are required; you must provide values for them when you create product items in your catalog. They should also correspond with the values used in your internal product database, and should accurately reflect the product represented, because they are included in training your models.

In some cases, other fields are also required. Refer to the complete list of all product fields on the [`Product`](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.branches.products) reference page.

All product information you provide can be used to improve the quality of recommendations and search results. Be sure to provide as many fields as possible.

Field  | Notes   
---|---  
`name` |  The full, unique resource name of the product. Required for all `Product` methods except for `import`. During import, the name is automatically generated and does not need to be manually provided.   
`id` |  The product ID used by your product database. The ID field must be unique across your entire catalog. The same value is used when you record a user event, and is also returned by the `predict` and `search` methods.   
`title` |  Product title from your product database. A UTF-8 encoded string. Limited to 1250 characters.   
`categories` |  Product categories. Every product must be assigned to at least one category. If a product belongs to more than one category, repeat the field for each category. The value must be a non-empty UTF-8 encoded string with a length limit of 5,000 characters. Always specify the full category path, for example: `["Sports & Fitness > Athletic Clothing > Shoes"]`.   
  
## Catalog categories

This section describes the catalog structure and how to designate it for use in taxonomy and filtering.

### Catalog structure

The `categories` field in the catalog should contain the most granular category path for each product. Parent categories are not required and should not be included.

Here is an example of how to structure your catalog:

  * **Correct** : `categories: ["Flowers, Cards, Occasion > Seasonal Items > Christmas"]`
  * **Incorrect** : `categories: ["Flowers, Cards, Occasion", "Flowers, Cards, Occasion > Seasonal Items", "Flowers, Cards, Occasion > Seasonal Items > Christmas"]`



#### Parent categories

The parent categories for a given product should not be included in the `categories` field. Filtering for browsing should be handled using [other custom attributes](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/attribute-config).

#### Category naming

Category names should be chosen carefully to avoid introducing incorrect keywords and improve performance. Using more specific and accurate terms enhances relevance and reduce issues.

  * **Recommended** : _Frozen Food > Frozen Fruits_
  * **Not recommended** : _Frozen Fruits & Vegetables > Frozen Fruits_



#### Project-specific, catalog-level structure

Create a single catalog for each language. If you operate in multiple countries, you can use the same catalog to provide search results in different countries. 

Provide prices, which are determined through local inventories, in the same currency across countries. If prices differ among countries, create a local inventory for each country. Specify its prices there. 

To optimize your search results, provide each country name as the `SearchRequest.entity` and `UserEvent.entity`. Use country entities for ranking purposes only.

## Product structure

When managing your product catalog in AI Commerce Search, understanding how attributes are handled for primary and variant products is crucial for effective search and recommendations. Product SKU designations determine catalog hierarchy.

![Catalog and inventory structure](https://docs.cloud.google.com/static/gemini-enterprise-cx/ai-commerce-search/images/product-catalog-inventory-structure.png)

### Product designation types

There are three product designation types:

  1. **Primary** or parent items are returned in recommendation or search results and serve as logical containers or groups of similar items. Primaries can be individual (SKU-level) items and groups of similar items (SKU groups).

  2. **Variant** or child items are specific, individual versions of a SKU-group primary product. For example, if the primary product is _V-neck shirt,_ variants could be _Brown V-neck shirt, size XL_ and _White V-neck shirt, size S_.

  3. **Collection** items are bundles of primary products or variant products, such as a jewelry set with a necklace, earrings, and a ring. Hierarchical structures similar to products and variants, collections group related primary products. Customers can't buy them directly, they're not widely used, and they're only available in search.


**Note:** The system strictly enforces primary to variant taxonomic relationships, and incorrect mapping causes import failures. This product `type` is immutable, so changing it requires deleting and recreating the product.

![](https://docs.cloud.google.com/static/gemini-enterprise-cx/ai-commerce-search/images/milk-variants-attributes-values.png)

![](https://docs.cloud.google.com/static/gemini-enterprise-cx/ai-commerce-search/images/milk-variants-attributes-values.png)

![](https://docs.cloud.google.com/static/gemini-enterprise-cx/ai-commerce-search/images/dress-variants-attributes-values.png)

![](https://docs.cloud.google.com/static/gemini-enterprise-cx/ai-commerce-search/images/dress-variants-attributes-values.png)

### Product classification hierarchies

Using the three product-level types, there are three main product classification hierarchies:

  * **Primary-variant** : The primary is almost always only a placeholder of (common) information and the variants are the actual SKUs which can be purchased. For example, T-shirts would be better structured hierarchically, as primaries with their corresponding set of variants. Each variant represents an individual SKU (for each size) and each primary item represents a group of SKUs, where each SKU is a different size for one overarching tee-shirt style. This organization by SKU structure allows the search results and recommendation panels to show a range of tee-shirt styles. It allows the shopper to drill down on a particular primary (style) to select the variant (size) to purchase.
  * **Primary only** : According to these product designation types, grocery items are better cataloged as primary products, each consisting of a single SKU product, such as`"bananas, fresh"`.
  * **Collections** : Collections group related products that a customer might buy. To accurately represent them in the reranking model, AI Commerce Search has a logic that credits them with purchases. For example: A shopper clicks on products in a bedsheets set, then adds to cart or purchases a primary product in that collection. The collection is credited with that purchase, and the model accurately represents the popularity and value of collections.

**Deprecated:** The variant-only catalog type is now deprecated and can only be used with recommendations. For the variant-only catalog, the `ingestionProductType` is set to `variant` during import. A primary is inferred for each variant, based on a primary product ID specified for each variant.

#### Products with a variant

For products that have a variant, structure them as primary-variant, because there are multiple advantages, including:

  * The search page has diverse results that can be displayed to the end users. Otherwise, if the variants were treated as primary products, the search result page is filled with the same products.
  * The products have a richer ranking scheme, as primary with variants are ranked better if a particular variant is getting more engagement. This helps in re-ranking and revenue optimization.
  * Ease of maintaining the catalog. If an attribute has a change for a group of products that differ only by size, then it can be done using a primary-variant structure, such as by changing the attribute at the primary level instead of changing multiple primaries.
  * API features and search response fields of variant rollup keys and retrievable fields are supported only for variants.
  * The search response contains minimum details of the primary and more details of the variants. So you always have to augment or enrich the search response with extra details, which can be returned by AI Commerce Search if marked as retrievable.



## Set up your product catalog

When planning your product catalog, you need to decide whether it contains products designated as only primaries, primaries and variants, or a mixture of the two arrangements. Think of it in terms of your products' SKU structure. Your products can be primary items, which could have variants.

Based on how your product SKUs are designated, consider your options for setting up your product catalog:

  * **You want your SKU to be shown as an individual search result or recommendation** : SKU=primary
  * **Your SKU should be part of a group of similar SKUs** : SKU=variant, group of SKUs=primary
  * **A mixture of both combinations** : SKU=primary, SKU=variant, group of SKUs=primary



![](https://docs.cloud.google.com/static/gemini-enterprise-cx/ai-commerce-search/images/variants-returned.png)

![](https://docs.cloud.google.com/static/gemini-enterprise-cx/ai-commerce-search/images/variants-returned.png)

If your product detail page shows an option, size, or color selector, these options are typically uploaded as variants into your product catalog. Consider whether or not you want different types of the same product with different attributes such as size and color to appear as a single search result or separate ones. For example, for a book you want to decide if you want a hard cover SKU and a soft cover SKU of the same book to appear as separate search results (SKU = primary), or as one (SKU = variant, group of SKUs = primary).

When setting up your product catalog, keep in mind that recommendation and search results only return primary items.

### Minimal primary products

If you determine that your catalog should have both primaries and variants, that is, SKU groups and SKUs, but you only have SKUs now, you need to create primaries for the SKU groups. These primaries are sometimes called virtual primaries or fake primaries.

These primaries only need to contain minimal information: `id`, `title`, and `categories`.

If `type` is not specified, the product type defaults to primary. If you are importing, you don't need to specify `name`. For more information, see the preceding section, Required product information.

### Catalog import

If your catalog is in Cloud Storage or BigQuery or some other storage, then do a bulk data import.

For detailed information about how to upload a catalog, see [Import catalog information](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/upload-catalog).

### Product URL correctness

**Note:** To help ensure quality service and prevent degraded performance, provide a valid URI for each product.

The [`product.uri`](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.branches.products#Product.FIELDS.uri) field is the canonical URL directly linking to the product detail page. It should be a publicly-crawlable URI and not behind any login or authorization wall. This is because the backend crawls the uri webpage and derives as much information as possible, which is used for relevance and popularity scoring. The backend also determines how the URI was interacted with on the web, including backlinks. Have the top level domain name be the same across all the product URIs.

If you have the same product listed in multiple banner sites, consider using the multi-entity feature. Please contact the account team on this.

AI Commerce Search uses product URLs to enrich product descriptions. If you use a different URL in the product catalog than in the actual site, make sure the two URLs refer to the same product and have nearly identical information. 

**Caution:** Do not re-use a product URL once a product is deleted. Instead, have unique URLs for each product.

Product URLs enhance catalogs by:

  * **Enriching product data** : AI Commerce Search extracts supplemental information by crawling the product's URI, the unique resource identifier behind the exact location of each product on the web (URL). This process helps in derive additional details and signals from the linked web pages. The deeper understanding of products gained through URI crawling directly contributes to the quality of the catalog's data.
  * **Improving search quality and relevance** : Web signals gathered from the crawled URIs are used to enhance search quality. The backend utilizes the crawled information, including how the URI was interacted with on the web, such as when your user clicks backlinks, for relevance and popularity scoring in search results.
  * **Providing a foundation for model training** : Besides product ID, title, category hierarchy, and price, URLs are considered one of the primary fields used as inputs for model training.



To maximize the benefits of product URLs, adhere to these best practices:

  * The linked web page must be publicly accessible and load correctly, not located behind a login or authentication wall.
  * Each URI should be unique and consistently point to the correct product's web page. Its content should accurately reflect the product information in the catalog. Maintain the same top-level domain name across all product URIs.



## Product inventory

Product inventory encompasses:

  * Price, both the current and original prices

  * Availability, such as in stock, out-of-stock, back ordered, and pre-ordered

  * Quantity available

  * Fulfillment information such as pickup-in-store, ship-to-store, and next-day-delivery




There are two levels of inventory: product-level and local.

### Product-level inventory

For retailers who only sell online, inventory is specified at the product level. Price, availability, and other inventory data is set for each product in the catalog.

For more information about product-level inventory, including how to maintain inventory data, see [Update inventory for AI Commerce Search](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/inventory-updates).

### Local inventory

Retailers who have brick-and-mortar stores and an online store need to keep inventory information on a per-store basis. They use local inventory to do this.

There are two product fields that can be used to store local inventory. Both fields are lists of locations (place IDs) with associated inventory information:

  * **[Product.fulfillmentInfo](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.branches.products#Product.FIELDS.fulfillment_info).** Pickup and shipping methods at each store location

  * **[Product.localInventories](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.branches.products#Product.FIELDS.local_inventories).** Price information, product attributes, and pickup and shipping methods at each store location




You can use either or both fields for your store-level information.

For more information about local inventories, see [Update local inventory for AI Commerce Search](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/local-inventory-updates).

### Primary-variant-inventory structure

The primary-variant-inventory data structure is composed of primary, variant, and local inventory products:

  * **Primary products** : Primary product data is stored without prices.

  * **Variant products (with the lowest price across the country)** : For example, the variant for the primary (color, size) should have the lowest price across country. Variant price data is rolled up to the primary product data, the primary price in turn being used for ranking purposes. Location-specific prices are ignored.

  * **Local inventory (region or store-specific pricing)** : Use the price information from the local inventory in reranking at serving time

  * **Primary product attributes** : Primary products must only include attributes common to all their associated variants.




### Product availability correctness

The availability field is set by the inventory update system as the product stock state changes. Keep track of all the products that are in `IN_STOCK` and `OUT_OF_STOCK` state.

If you have the majority of products as `OUT_OF_STOCK`, the search response would have many out-of-stock products and on adding a filter, the recall numbers are reduced. If the product has gone out of stock but the catalog state is `IN_STOCK`, then users see the product as available, but probably face issues at the time of purchase or add-to-cart. This has more of an effect on the customer experience than the model training. Keep the `Product.availability` field as up-to-date as possible using the `patchProduct` APIs or import APIs with a `readMask`.

## Product schema

When importing a catalog from BigQuery, use the following AI Commerce Search product schema to create a BigQuery table with the correct format and load it with your catalog data. Then, [import the catalog](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/upload-catalog#bq).

####  AI Commerce Search product schema 

###  BigQuery 
    
    
    [
      {
        "name": "name",
        "type": "STRING",
        "mode": "NULLABLE"
      },
      {
        "name": "id",
        "type": "STRING",
        "mode": "REQUIRED"
      },
      {
        "name": "type",
        "type": "STRING",
        "mode": "NULLABLE"
      },
      {
        "name": "primaryProductId",
        "type": "STRING",
        "mode": "NULLABLE"
      },
      {
        "name": "collectionMemberIds",
        "type": "STRING",
        "mode": "REPEATED"
      },
      {
        "name": "gtin",
        "type": "STRING",
        "mode": "NULLABLE"
      },
      {
        "name": "categories",
        "type": "STRING",
        "mode": "REPEATED"
      },
      {
        "name": "title",
        "type": "STRING",
        "mode": "REQUIRED"
      },
      {
        "name": "brands",
        "type": "STRING",
        "mode": "REPEATED"
      },
      {
        "name": "description",
        "type": "STRING",
        "mode": "NULLABLE"
      },
      {
        "name": "languageCode",
        "type": "STRING",
        "mode": "NULLABLE"
      },
      {
        "name": "attributes",
        "type": "RECORD",
        "mode": "REPEATED",
        "fields": [
          {
            "name": "key",
            "type": "STRING",
            "mode": "NULLABLE"
          },
          {
            "name": "value",
            "type": "RECORD",
            "mode": "NULLABLE",
            "fields": [
              {
                "name": "text",
                "type": "STRING",
                "mode": "REPEATED"
              },
              {
                "name": "numbers",
                "type": "FLOAT",
                "mode": "REPEATED"
              }
            ]
          }
        ]
      },
      {
        "name": "tags",
        "type": "STRING",
        "mode": "REPEATED"
      },
      {
        "name": "priceInfo",
        "type": "RECORD",
        "mode": "NULLABLE",
        "fields": [
          {
            "name": "currencyCode",
            "type": "STRING",
            "mode": "NULLABLE"
          },
          {
            "name": "price",
            "type": "FLOAT",
            "mode": "NULLABLE"
          },
          {
            "name": "originalPrice",
            "type": "FLOAT",
            "mode": "NULLABLE"
          },
          {
            "name": "cost",
            "type": "FLOAT",
            "mode": "NULLABLE"
          },
          {
            "name": "priceEffectiveTime",
            "type": "STRING",
            "mode": "NULLABLE"
          },
          {
            "name": "priceExpireTime",
            "type": "STRING",
            "mode": "NULLABLE"
          }
        ]
      },
      {
        "name": "rating",
        "type": "RECORD",
        "mode": "NULLABLE",
        "fields": [
          {
            "name": "ratingCount",
            "type": "INTEGER",
            "mode": "NULLABLE"
          },
          {
            "name": "averageRating",
            "type": "FLOAT",
            "mode": "NULLABLE"
          },
          {
            "name": "ratingHistogram",
            "type": "INTEGER",
            "mode": "REPEATED"
          }
        ]
      },
      {
        "name": "expireTime",
        "type": "STRING",
        "mode": "NULLABLE"
      },
      {
        "name": "ttl",
        "type": "RECORD",
        "mode": "NULLABLE",
        "fields": [
          {
            "name": "seconds",
            "type": "INTEGER",
            "mode": "NULLABLE"
          },
          {
            "name": "nanos",
            "type": "INTEGER",
            "mode": "NULLABLE"
          }
        ]
      },
      {
        "name": "availableTime",
        "type": "STRING",
        "mode": "NULLABLE"
      },
      {
        "name": "availability",
        "type": "STRING",
        "mode": "NULLABLE"
      },
      {
        "name": "availableQuantity",
        "type": "INTEGER",
        "mode": "NULLABLE"
      },
      {
        "name": "fulfillmentInfo",
        "type": "RECORD",
        "mode": "REPEATED",
        "fields": [
          {
            "name": "type",
            "type": "STRING",
            "mode": "NULLABLE"
          },
          {
            "name": "placeIds",
            "type": "STRING",
            "mode": "REPEATED"
          }
        ]
      },
      {
        "name": "uri",
        "type": "STRING",
        "mode": "NULLABLE"
      },
      {
        "name": "images",
        "type": "RECORD",
        "mode": "REPEATED",
        "fields": [
          {
            "name": "uri",
            "type": "STRING",
            "mode": "REQUIRED"
          },
          {
            "name": "height",
            "type": "INTEGER",
            "mode": "NULLABLE"
          },
          {
            "name": "width",
            "type": "INTEGER",
            "mode": "NULLABLE"
          }
        ]
      },
      {
        "name": "audience",
        "type": "RECORD",
        "mode": "NULLABLE",
        "fields": [
          {
            "name": "genders",
            "type": "STRING",
            "mode": "REPEATED"
          },
          {
            "name": "ageGroups",
            "type": "STRING",
            "mode": "REPEATED"
          }
        ]
      },
      {
        "name": "colorInfo",
        "type": "RECORD",
        "mode": "NULLABLE",
        "fields": [
          {
            "name": "colorFamilies",
            "type": "STRING",
            "mode": "REPEATED"
          },
          {
            "name": "colors",
            "type": "STRING",
            "mode": "REPEATED"
          }
        ]
      },
      {
        "name": "sizes",
        "type": "STRING",
        "mode": "REPEATED"
      },
      {
        "name": "materials",
        "type": "STRING",
        "mode": "REPEATED"
      },
      {
        "name": "patterns",
        "type": "STRING",
        "mode": "REPEATED"
      },
      {
        "name": "conditions",
        "type": "STRING",
        "mode": "REPEATED"
      },
      {
        "name": "publishTime",
        "type": "STRING",
        "mode": "NULLABLE"
      },
      {
        "name": "promotions",
        "type": "RECORD",
        "mode": "REPEATED",
        "fields": [
          {
            "name": "promotionId",
            "type": "STRING",
            "mode": "NULLABLE"
          }
        ]
      }
    ]

**Note:** For reranking on inventory prices, use `placeId` in the search request.

### Use built-in fields instead of custom attributes

For all other product attributes that are not part of the product information schema, use the [`Product.attributes` (custom attributes)](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/attribute-config#attribute-types).

The built-in product fields like title, description, and brands have a bigger impact on the searchability and indexability, as compared to the custom attributes.

In other words, the backend has a deeper understanding of the built-in fields than the custom attributes. The backend takes into account the built-in fields information for relevance optimization. For this reason, use the built-in fields. This means mapping your product information to built-in fields whenever possible, and only use customer attributes when necessary.

For example, setting the brands in the `Product.brands` field has a much higher impact on search and recall than setting the same information in a custom attribute. For an attribute like `sleeve length`, which is not natively supported, it's better to use custom attributes.

### Use the brand field

The brand field in the product information, which is by default searchable, indexable, and facetable, is a strong signal for ranking and relevance. A good percentage of search queries are of the form, `brand query` or `query brand`, and arguably, brand is one of the most heavily used facets.

The click and purchase conversion ratios get affected heavily if the product has the correct brand field. So it's important to have the brand field populated with the correct information and if possible, to never be left blank. What is more detrimental is to fill in random fillers in the brand names like `"NA"` or `"Not available"` or `"Miscellaneous"`. This strongly associates the product with the text mentioned in the brands field, which might lead to wrong product understanding and bad recall.

If a particular product is absolutely not associated with any brands, it's better to keep the fields empty. But care needs to be taken that these empty brand products are a small percentage of the catalog products.

### Use the audience field

There are two subfields in the audience field of the product information. There are `Audience.gender` and `Audience.ageGroup`. It's far more effective to fill these fields with the appropriate data, which helps the model understand the product's intended audience.

This plays a big part when personalization is enabled. Having `gender` and `ageGroup` helps segment the products better and helps the model to recall the right product for the appropriate user.

The `Audience` data is also helpful when you have queries like _shirts for women_ or _men's socks._ With the audience information populated, the product understanding is far better and the model has improved recall for gender-specific queries.

### Look for products with duplicate titles

The `Product.title` is probably the most important field, as most of the search queries would have a huge overlap with what is set as the `Product.title`. It's probably the first information that the end users would see and interact with in the Detail page view, so it's good practice to keep the product.title unique and have text information that is most relevant to the product.

Having two products (primary products) with the same title affect the searchability and relevance of the returned results. If there are two separate primary products with significant differences, keep the titles different. If the products are the same but differ only in a few aspects like color, size, structure the products as primary and variant types.

### Language settings

AI Commerce Search supports multiple languages. Note, however, that any one project can only have one catalog. Any catalog can only have one language.

For this reason, the catalog and search query need to be in the same language. There's no cross-language translation of query or catalog information. For example, if your catalog is in Spanish, the search query also needs to be.

So, it's important to mark the language code in the product information accordingly, otherwise it defaults to English (`en-US`). This is important for search controls like `spellCorrectionSpec` where if the language is not set, it leads to undesired behavior. This is also extremely important for query intent understanding.

For me information on mixed language settings, refer to [Supported languages](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/supported-languages#mixed-languages).

### Price information settings

The `Product.priceInfo` field needs to be as accurate and complete as possible. This price information is used to derive discount-related signals and is used in revenue optimization. This is particularly important for browse queries.

For a primary-variant product structure, populate the price of at least one of the variants.

For a product that doesn't have product-level pricing and all the pricing is in the local inventory, meaning that the search is always tied to a local inventory, fill the median price information of all the inventory level pricing at the product level price information.

## Catalog data quality metrics

The [**Data quality**](https://console.cloud.google.com/ai/retail/catalogs/default_catalog/data/) page in the AI Commerce Search in Gemini Enterprise for Customer Experience console assesses if you need to update catalog data to improve the quality of search results and unlock search performance tiers.

The following table describes the quality metrics that AI Commerce Search uses to help you evaluate your product data. For details about how to view data quality metrics and search performance tiers in the AI Commerce Search in Gemini Enterprise for Customer Experience console, see [Unlock search performance tiers](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/data-quality).

Catalog quality metric | Quality rule | Notes  
---|---|---  
URI is present and accessible | Product has a valid [`Product.uri`](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.branches.products#Product.FIELDS.uri). The URI needs to be accessible and match your domain. | Search uses web signals crawled using this URI to improve search quality.  
Meets time conformance | [`Product.availableTime`](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.branches.products#Product.FIELDS.available_time) is before current time, and [`Product.expireTime`](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.branches.products#Product.FIELDS.expire_time) is after current time. | Only products that meet the time conformance are available for search.  
Searchable attribute is present | Product has at least one [`attribute`](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.branches.products#Product.FIELDS.attributes) set to searchable. | Custom attributes that are marked searchable can be searched by text queries.  
Description is present | Product has non-empty [`Product.description`](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.branches.products#Product.FIELDS.description). | A comprehensive description helps to improve search quality.  
Title consists of at least two words | [`Product.title`](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.branches.products#Product.FIELDS.title) consists of at least two words. | A comprehensive title helps to improve search quality.  
Has variant with image | The [`variant`](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.branches.products#Product.Type.ENUM_VALUES.VARIANT) product has at least one [`Product.image`](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.branches.products#Product.FIELDS.images). You can ignore this metric if all your products are at [`primary`](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.branches.products#Product.Type.ENUM_VALUES.PRIMARY) level. | This metric is for informational purposes and does not impact search quality.  
Has variant with price information | The [`variant`](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.branches.products#Product.Type.ENUM_VALUES.VARIANT) product has [`Product.priceInfo`](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.branches.products#Product.FIELDS.price_info) set. You can ignore this metric if all your products are at [`primary`](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.branches.products#Product.Type.ENUM_VALUES.PRIMARY) level. | This metric is for informational purposes and does not impact search quality.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
