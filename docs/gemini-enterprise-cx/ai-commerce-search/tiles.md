---
url: https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/tiles/
title: Tile navigation \u00a0|\u00a0 AI Commerce Search in Gemini Enterprise for Customer Experience \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:38:56.846296+00:00
---

# Tile navigation  |  AI Commerce Search in Gemini Enterprise for Customer Experience  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/tiles/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ AI Commerce Search ](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search)



Send feedback 

#  Tile navigation Stay organized with collections  Save and categorize content based on your preferences. 

This page introduces the tile navigation feature of AI Commerce Search.

## Why tiles?

As a visual representation of attribute value pairs, tiles are a different way to present the same information as dynamic facets, showing only the attributes that are most frequently engaged for a particular query independent of dynamic facet families that are not always intuitive for the shopper. The goal of this is to increase filter usage, which in turn increases revenue per user. Tile navigation makes filter usage on strong HEAD queries more relevant, facilitating more accurate revenue prediction (through regression).

Tile navigation functions as part of the Guided Search package, benefiting the customer by narrowing user queries faster and with greater relevance to the end user. The tile navigation feature was designed to solve the real estate problem of dynamic facets to allow the user to find what is likely more relevant to them more quickly. Tile navigation also prevents the shopper from having to forage through all the facet families in a left or right navigation pane to find exactly which product they are looking for before still having to confirm their narrowed search selection in a second click of a submit button. 

## Tile navigation complements dynamic facets

[Dynamic facets](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/facets-overview#about_dynamic_facets) are provided in the AI Commerce Search in Gemini Enterprise for Customer Experience console by uploading the catalog of products. They are filters that narrow queries by changing the order of filters shown so that the correct filters are on top and make the search return more relevant with each search turn.

Dynamic facets sort families of filters such as Style, Sleeve for a query dress for fashion retailers, or Volume, Variety, or Container for milk for grocery retailers. Often, these dynamic facet families are arranged in a way that is not always intuitive to the user. Additionally, a fly-out pane for dynamic facet selection takes up a lot of real estate on the product site and are likewise not always mobile friendly.

So a need emerged to reduce real estate on merchandise websites and drive up user revenue per search conversion.

## How do tiles work?

Tile navigation gets the user to a narrower search faster to increase search engagement and revenue per search. Tiles can be displayed horizontally across the product site independent of facet families. The tiles feature controls search filters in such a way as to put the most likely engaged filters individually across the top of the page, breaking the search results out of their dynamic facet families to provide immediate visualization. This way, tile navigation offers users a more accessible arrangement of dynamic facets content.

### Shopper journey

When a shopper performs a search on a retailer's website with tile navigation enabled, they will see up to 20 tiles displaying individual filter values that are most likely to be engaged. These tiles are sorted by likelihood of usage, independent of product attribute family. Each tile can include an image representing a typical product with the filter applied. If a customer clicks on a tile, it acts as if the corresponding facet-value has been applied. This updates the product list to match the query and filter, and the applied facet is shown. Additionally, the displayed tiles refresh to reflect the new expected engagement rate, excluding any filters that have already been applied.

### Retailer journey

The retailer sends a query to AI Commerce Search and receives a standard query reply that includes a sorted list of tile values ranked across product attribute families and a way to generate a tile image. The retailer then renders the tiles with or without images. If a potential customer clicks on a tile or facet value, the retailer sends a new query to Google with the filter corresponding to the tile or facet added to the filter field. The retailer site also sends Google an event for the second query with the filter added. The AI Commerce Search response, the query sent to Google, and the events sent to Google are the same for both "user clicked on filter" and "user clicked on tile."

## Filters shown in tiles

Filters can be eligible for tiling based on preferences retailers can set in the AI Commerce Search in Gemini Enterprise for Customer Experience console or the AI Commerce Search API for content, product counts, and related to quantitative queries.

### Based on content

  * Filters cannot have been applied in a previous search.
  * Only tiles that correspond to attribute values in catalog attributes marked as dynamically facetable.
  * The search return (the AI Commerce Search response) must have at least one product.
  * No tiles corresponding to system filters such as "instock = yes" or "available for sale = yes" are shown.
  * Tiles are sorted by likelihood of engagement.



### Based on product counts

  * What if there are < 20 rankable tiles? 
    * If there are between >= 2 and < 20, return as many tiles as possible.
    * If there are < 2 tiles available, return no tiles.
  * If > 20 rankable tiles, return the top 20 based on the likelihood of engagement.



### Based on quantitative queries

  * Tiles support both "categorical" (color = red) and numerical (weight = "1lb - 2lb").
  * Bucketing of numeric tiles: 
    * The bucketing configured using controls for specific attributes is honored. For example, if a facet is manually bucketed into weights of 0-1, 1-3 lbs, and 3-6 lbs, those buckets are used in the tiles. More details can be found in [Dynamic facet and tile controls](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/facets-overview#about_dynamic_facets).
    * If a facet is auto-bucketed, the same buckets should be used in tiles.



## Tile navigation in the AI Commerce Search API?

There is no new API for the tiles feature. However, new fields have been added to the already existing Vertex AI main (query) API.

### Request tileNavigationSpec

#### Query
    
    
    {
      "tile_navigation_requested": boolean,
      "applied_tiles": repeated
    }

**Fields (request)**  
---  
`tile_navigation_requested` | This boolean field specifies whether the customer would like to request tile navigation.   
`applied_tiles` | This repeated field specifies the tiles which are already clicked.   
  
First, set the `tileNavigationSpec` field. Call the object `productAttributeValue` which contains the attribute name and value, such as `name=color` and `value=red`. Leave all other fields the same.

### Response tileNavigationResult

The API then returns up to 20 tiles in the`tileNavigationResult` field, sorted by likelihood of use. The response displays the tiles according to their attribute values and a corresponding representative image:

#### Response
    
    
    ...
      "tileNavigationResult": {
        "tiles": [
          {
            "productAttributeValue": {
              "name": "sizes",
              "value": "large"
            },
            "representativeProductId": "xxxx"
          },
          {
            "productAttributeValue": {
              "name": "attributes.weight",
              "value": "light"
            },
            "representativeProductId": "xxxx"
          },
          {
            "productAttributeValue": {
              "name": "colors",
              "value": "black"
            },
            "representativeProductId": "xxxx"
          }
        ]
      }
      ...

**Fields (response)**  
---  
`tiles` | This repeated field drives the tiles that are shown to the user on the client side. The field contains a list of tiles, where each tile is an object which contains the **`productAttributeValue`** and the **`representativeProductId`**.   
  
No changes are needed to the existing API, and new client libraries are available at GA time and are published in the [public library documentation](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/libraries).

#### What retailers should do with tiles search results

  * **Showing tiles:** Show the returned tiles in the order provided, with the first tile in the response being the first tile shown. `ProductAttributeValue` is a key-value pair which contains the attribute value, so that you know which tiles to show. In the subsequent search requests, the `ProductAttributeValue` should be set in the `appliedTiles` field and also it should be set in the `filter` field (e.g., `filter = "attributes.weight:ANY(\"large\")"`). The response will then have filtered products and a new set of tiles to show.

  * **Showing images:** These images can be obtained by referencing the `representativeProductId` field in the response, which provides the product ID of a typical product that matches the applied filter. Retailers then look up this representative product ID on their end and select an appropriate image to display in the tile. It's important to use the representative product ID, rather than the primary product ID, to ensure the image accurately reflects the filtered attribute (e.g., displaying a red variant for the `color = "red"` filter).




## Configure tile behavior in the console

The selection of tiles to appear across the search screen are directly driven by the catalog attributes, which in turn are extracted from the information the retailer uploads to the product catalog. The candidate tiles are all values within the attributes of all the "dynamically facetable attributes" in the product catalog. 

### Enable dynamic facets and tiling

Facets are controlled by product attributes, which originate from the catalog and user events. Dynamic faceting and tiling is set up to allow end user queries to match product attributes.

**Note:** The minimum requirement for enabling tiling in your project is 7,000 API requests per week on an ongoing basis. Essentially, this means that the project must already be in a production environment.

To control which attributes are eligible for dynamic facets and tiles:

  1. Go to the **Controls** page of the AI Commerce Search in Gemini Enterprise for Customer Experience console. [Go to the Controls page](https://console.cloud.google.com/ai/retail/catalogs/default_catalog/controls/)

  2. Click the **Attribute controls** tab > set your tile controls.

  3. Optional: To modify the attribute controls, click _edit_**Modify controls** next to **Attributes** , then set the controls for each attribute to **True** or **False**.




![Alt text](https://docs.cloud.google.com/static/gemini-enterprise-cx/ai-commerce-search/images/attribute-controls.png)

The third and fourth columns (**Indexable** and **Dynamic faceting**) are key in controlling the tiles. For each attribute row, both of these columns must be marked **True** for tiles to work. **Indexable** enables AI Commerce Search to filter using the attribute. With **Dynamic faceting** enabled, AI Commerce Search can automatically use an attribute as a dynamic facet based on past user behavior such as facet clicks and views.

To see how to do this in the API, refer to Tile control in the API section.

### Individual tile controls

Facet controls let you manage the behavior of your facets without changing your catalog and impact search behavior across your site.

The **Remove facets** control removes an entire facet from the results for dynamic facets for certain queries. It also removes member tiles of this facet from being returnable as tiles.

The following facet _value_ controls flagged with **Dynamic faceting & tiling** at the catalog level likewise impact tiles:

  * **Ignore facet values** : Suppresses the tile from appearing as well as removes the dynamic facet in the search results.
  * **Replace facet values** : Lets the retailer change the facet value (for example, for the attribute `color`, change `navy blue` to `blue`) for specific queries in both tiles and dynamic facets.
  * **Set numerical intervals** : Allows the retailer to specify bucket sizes to output a search response in a given dynamic range, both in dynamic facets and tiles.



The last three dynamic facet control types in the scroll-down menu of facet control types controls don't impact tiles:

  * **Force return facets**
  * **Rerank dynamic facets**
  * **Merge facets**



For more information on controlling specific facet value and tile behavior on each control, refer to [Facet controls](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/facets-overview#facet_controls).

## Tile control in the API

This section describes how to control tile behavior in the AI Commerce Search API.

### Attribute controls

For search and recommendations, you'll find the API at the catalog level under the REST resource Resource: projects.locations.catalogs.attributesConfig. This API provides methods to add, remove, and replace attributes at both the catalog and product level. The field `catalogAttributes` can be mapped to indexable, searchable, and `dynamicFacetable`. `dynamicFacetable` applies to tile behavior if the facets are eligible for tiling.

**[AttributesConfig](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs#resource:-attributesconfig)**

Catalog level attribute config.

**Tile-relevant field**  
---  
`catalogAttributes` | `map` Enables attributes config at the catalog level, which contains information about whether it is searchable, dynamically facetable, and more, by mapping the name of an attribute to a value, which is a callable object, `CatalogAttribute`.   
  
**[CatalogAttribute](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs#AttributesConfig.FIELDS.catalog_attribute)**

The `attributesConfig` resource provides `CatalogAttribute`, a catalog-level object. Two of this object's fields generate controls over which attributes show up as tiles. This means that any attributes in all the "facetable attributes" of the product catalog can be candidates for tiling:

**Tile-relevant fields**  
---  
`DynamicFacetableOption` | `enum` global control field that must be specified as enabled or disabled. This turns dynamic facets on or off, which in turn drives tiles. This one is set under Attribute controls in the Google Cloud console.   
`facetConfig` | object which contains options for individual facet values. This field is a facet control.   
  
### Facet controls

`FacetConfig`

An object that contains facet options for making individual facet values dynamic and thus potentially tileable. It is a field from the catalog level `CatalogAttribute` config.

The object contains already existing fields whose impact now extends to tiles:

#### JSON Example
    
    
      "facetIntervals": [
        {
          object (Interval)
        }
      ],
      "ignoredFacetValues": [
        {
          object (IgnoredFacetValues)
        }
      ]

**Tile-relevant fields**  
---  
`ignoredFacetValues` | This message field in the `FacetConfig` contains facet values to ignore for the current attribute name for a given time range and only in the facet without affecting the product descriptions in the catalog.   
`facetIntervals` | This allows the retailer to specify bucket sizes for a numerical input. This should work the same way for tiles- if a retailer sets specific numerical intervals for a dynamic facet, it should use the same numerical intervals for tiles.   
`removeFacetValue` | Removes facet values for specific facet keys. These are mapped to attribute values.   
  
See how to [create these individual controls in the console](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/facets-overview#facet_controls).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
