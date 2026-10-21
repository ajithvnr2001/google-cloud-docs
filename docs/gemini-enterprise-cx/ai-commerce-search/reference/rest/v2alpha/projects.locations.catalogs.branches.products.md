---
url: https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products
title: REST Resource: projects.locations.catalogs.branches.products \u00a0|\u00a0 AI Commerce Search in Gemini Enterprise for Customer Experience \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T14:19:13.056835+00:00
---

# REST Resource: projects.locations.catalogs.branches.products  |  AI Commerce Search in Gemini Enterprise for Customer Experience  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ AI Commerce Search ](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search)



Send feedback 

#  REST Resource: projects.locations.catalogs.branches.products Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Product
    * JSON representation
    * Type
    * PriceInfo
      * JSON representation
    * PriceRange
      * JSON representation
    * Rating
      * JSON representation
    * Availability
    * FulfillmentInfo
      * JSON representation
    * Image
      * JSON representation
    * Audience
      * JSON representation
    * ColorInfo
      * JSON representation
    * Promotion
      * JSON representation
    * LocalInventory
      * JSON representation
    * Availability
  * Methods



## Resource: Product

Product captures all metadata information of items to be recommended or searched.

JSON representation  
---  
      
    
    {
      "name": string,
      "id": string,
      "type": enum ([Type](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.Type)),
      "primaryProductId": string,
      "collectionMemberIds": [
        string
      ],
      "gtin": string,
      "categories": [
        string
      ],
      "title": string,
      "brands": [
        string
      ],
      "description": string,
      "languageCode": string,
      "attributes": {
        string: {
          "text": [
            string
          ],
          "numbers": [
            number
          ],
          "searchable": boolean,
          "indexable": boolean
        },
        ...
      },
      "tags": [
        string
      ],
      "priceInfo": {
        object ([PriceInfo](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.PriceInfo))
      },
      "rating": {
        object ([Rating](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.Rating))
      },
      "availableTime": string,
      "availability": enum ([Availability](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.Availability)),
      "availableQuantity": integer,
      "fulfillmentInfo": [
        {
          object ([FulfillmentInfo](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.FulfillmentInfo))
        }
      ],
      "uri": string,
      "images": [
        {
          object ([Image](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.Image))
        }
      ],
      "audience": {
        object ([Audience](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.Audience))
      },
      "colorInfo": {
        object ([ColorInfo](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.ColorInfo))
      },
      "sizes": [
        string
      ],
      "materials": [
        string
      ],
      "patterns": [
        string
      ],
      "conditions": [
        string
      ],
      "promotions": [
        {
          object ([Promotion](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.Promotion))
        }
      ],
      "publishTime": string,
      "retrievableFields": string,
      "variants": [
        {
          object ([Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product))
        }
      ],
      "localInventories": [
        {
          object ([LocalInventory](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.LocalInventory))
        }
      ],
    
      // Union field expiration can be only one of the following:
      "expireTime": string,
      "ttl": string
      // End of list of possible types for union field expiration.
    }  
  
Fields  
---  
`name` |  `string` Immutable. Full resource name of the product, such as `projects/*/locations/global/catalogs/default_catalog/branches/default_branch/products/productId`.  
`id` |  `string` Immutable. `[Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product)` identifier, which is the final component of `[name](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.FIELDS.name)`. For example, this field is "id_1", if `[name](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.FIELDS.name)` is `projects/*/locations/global/catalogs/default_catalog/branches/default_branch/products/id_1`.This field must be a UTF-8 encoded string with a length limit of 128 characters. Otherwise, an INVALID_ARGUMENT error is returned.Corresponding properties: Google Merchant Center property [id](https://support.google.com/merchants/answer/6324405). Schema.org property [Product.sku](https://schema.org/sku).  
`type` |  `enum (`[Type](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.Type)`)` Immutable. The type of the product. Default to `[Catalog.product_level_config.ingestion_product_type](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs#ProductLevelConfig.FIELDS.ingestion_product_type)` if unset.  
`primaryProductId` |  `string` Variant group identifier. Must be an `[id](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.FIELDS.id)`, with the same parent branch with this product. Otherwise, an error is thrown.For `[Type.PRIMARY](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.Type.ENUM_VALUES.PRIMARY)` `[Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product)`s, this field can only be empty or set to the same value as `[id](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.FIELDS.id)`.For VARIANT `[Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product)`s, this field cannot be empty. A maximum of 2,000 products are allowed to share the same `[Type.PRIMARY](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.Type.ENUM_VALUES.PRIMARY)` `[Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product)`. Otherwise, an INVALID_ARGUMENT error is returned.Corresponding properties: Google Merchant Center property [item_group_id](https://support.google.com/merchants/answer/6324507). Schema.org property [Product.inProductGroupWithID](https://schema.org/inProductGroupWithID).  
`collectionMemberIds[]` |  `string` The `[id](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.FIELDS.id)` of the collection members when `[type](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.FIELDS.type)` is `[Type.COLLECTION](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.Type.ENUM_VALUES.COLLECTION)`.Non-existent product ids are allowed. The `[type](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.FIELDS.type)` of the members must be either `[Type.PRIMARY](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.Type.ENUM_VALUES.PRIMARY)` or `[Type.VARIANT](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.Type.ENUM_VALUES.VARIANT)` otherwise an INVALID_ARGUMENT error is thrown. Should not set it for other types. A maximum of 1000 values are allowed. Otherwise, an INVALID_ARGUMENT error is return.  
`gtin` |  `string` The Global Trade Item Number (GTIN) of the product.This field must be a UTF-8 encoded string with a length limit of 128 characters. Otherwise, an INVALID_ARGUMENT error is returned.This field must be a Unigram. Otherwise, an INVALID_ARGUMENT error is returned.Corresponding properties: Google Merchant Center property [gtin](https://support.google.com/merchants/answer/6324461). Schema.org property [Product.isbn](https://schema.org/isbn), [Product.gtin8](https://schema.org/gtin8), [Product.gtin12](https://schema.org/gtin12), [Product.gtin13](https://schema.org/gtin13), or [Product.gtin14](https://schema.org/gtin14).If the value is not a valid GTIN, an INVALID_ARGUMENT error is returned.  
`categories[]` |  `string` Optional. Product categories. This field is repeated for supporting one product belonging to several parallel categories. Strongly recommended using the full path for better search / recommendation quality.To represent the full path of category, use the '>' sign, with one space on each side, to separate different hierarchies. If '>' is part of the category name, replace it with other character(s).For example, if a shoes product belongs to both ["Shoes & Accessories" -> "Shoes"] and ["Sports & Fitness" -> "Athletic Clothing" -> "Shoes"], it could be represented as:
    
    
     "categories": [
       "Shoes & Accessories > Shoes",
       "Sports & Fitness > Athletic Clothing > Shoes"
     ]
    

Must be set for `[Type.PRIMARY](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.Type.ENUM_VALUES.PRIMARY)` `[Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product)` otherwise an INVALID_ARGUMENT error is returned.At most 250 values are allowed per `[Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product)` unless overridden through the Google Cloud console. Empty values are not allowed. Each value must be a UTF-8 encoded string with a length limit of 5,000 characters. Otherwise, an INVALID_ARGUMENT error is returned.Corresponding properties: Google Merchant Center property [google_product_category](https://support.google.com/merchants/answer/6324436). Schema.org property [Product.category](https://schema.org/category).  
`title` |  `string` Required. Product title.This field must be a UTF-8 encoded string with a length limit of 1,000 characters. Otherwise, an INVALID_ARGUMENT error is returned.Corresponding properties: Google Merchant Center property [title](https://support.google.com/merchants/answer/6324415). Schema.org property [Product.name](https://schema.org/name).  
`brands[]` |  `string` The brands of the product.A maximum of 30 brands are allowed unless overridden through the Google Cloud console. Each brand must be a UTF-8 encoded string with a length limit of 1,000 characters. Otherwise, an INVALID_ARGUMENT error is returned.Corresponding properties: Google Merchant Center property [brand](https://support.google.com/merchants/answer/6324351). Schema.org property [Product.brand](https://schema.org/brand).  
`description` |  `string` Product description.This field must be a UTF-8 encoded string with a length limit of 5,000 characters. Otherwise, an INVALID_ARGUMENT error is returned.Corresponding properties: Google Merchant Center property [description](https://support.google.com/merchants/answer/6324468). Schema.org property [Product.description](https://schema.org/description).  
`languageCode` |  `string` Language of the title/description and other string attributes. Use language tags defined by [BCP 47](https://www.rfc-editor.org/rfc/bcp/bcp47.txt).For product prediction, this field is ignored and the model automatically detects the text language. The `[Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product)` can include text in different languages, but duplicating `[Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product)`s to provide text in multiple languages can result in degraded model performance.For product search this field is in use. It defaults to "en-US" if unset.  
`attributes` |  `map (key: string, value: object)` Highly encouraged. Extra product attributes to be included. For example, for products, this could include the store name, vendor, style, color, etc. These are very strong signals for recommendation model, thus we highly recommend providing the attributes here.Features that can take on one of a limited number of possible values. Two types of features can be set are:Textual features. some examples would be the brand/maker of a product, or country of a customer. Numerical features. Some examples would be the height/weight of a product, or age of a customer.For example: `{ "vendor": {"text": ["vendor123", "vendor456"]}, "lengths_cm": {"numbers":[2.3, 15.4]}, "heights_cm": {"numbers":[8.1, 6.4]} }`.This field needs to pass all below criteria, otherwise an INVALID_ARGUMENT error is returned:

  * Max entries count: 200.
  * The key must be a UTF-8 encoded string with a length limit of 128 characters.
  * For indexable attribute, the key must match the pattern: `[a-zA-Z0-9][a-zA-Z0-9_]*`. For example, `key0LikeThis` or `KEY_1_LIKE_THIS`.
  * For text attributes, at most 400 values are allowed. Empty values are not allowed. Each value must be a non-empty UTF-8 encoded string with a length limit of 256 characters.
  * For number attributes, at most 400 values are allowed.

  
`attributes.text[]` |  `string` The textual values of this custom attribute. For example, `["yellow", "green"]` when the key is "color".Empty string is not allowed. Otherwise, an INVALID_ARGUMENT error is returned.Exactly one of `text` or `numbers` should be set. Otherwise, an INVALID_ARGUMENT error is returned.  
`attributes.numbers[]` |  `number` The numerical values of this custom attribute. For example, `[2.3, 15.4]` when the key is "lengths_cm".Exactly one of `text` or `numbers` should be set. Otherwise, an INVALID_ARGUMENT error is returned.  
`attributes.searchable  
**(deprecated)**` |  `boolean` This field is normally ignored unless `[AttributesConfig.attribute_config_level](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.attributesConfig#AttributesConfig.FIELDS.attribute_config_level)` of the `[Catalog](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs#Catalog)` is set to the deprecated 'PRODUCT_LEVEL_ATTRIBUTE_CONFIG' mode. For information about product-level attribute configuration, see [Configuration modes](https://cloud.google.com/gemini-enterprise-cx/ai-commerce-search/attribute-config#config-modes). If true, custom attribute values are searchable by text queries in `[SearchService.Search](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.placements/search#google.cloud.retail.v2alpha.SearchService.Search)`.This field is ignored in a `[UserEvent](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.userEvents#UserEvent)`.Only set if type `text` is set. Otherwise, a INVALID_ARGUMENT error is returned.  
`attributes.indexable  
**(deprecated)**` |  `boolean` This field is normally ignored unless `[AttributesConfig.attribute_config_level](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.attributesConfig#AttributesConfig.FIELDS.attribute_config_level)` of the `[Catalog](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs#Catalog)` is set to the deprecated 'PRODUCT_LEVEL_ATTRIBUTE_CONFIG' mode. For information about product-level attribute configuration, see [Configuration modes](https://cloud.google.com/gemini-enterprise-cx/ai-commerce-search/attribute-config#config-modes). If true, custom attribute values are indexed, so that they can be filtered, faceted or boosted in `[SearchService.Search](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.placements/search#google.cloud.retail.v2alpha.SearchService.Search)`.This field is ignored in a `[UserEvent](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.userEvents#UserEvent)`.See `[SearchRequest.filter](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.placements/search#body.request_body.FIELDS.filter)`, `[SearchRequest.facet_specs](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.placements/search#body.request_body.FIELDS.facet_specs)` and `[SearchRequest.boost_spec](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.placements/search#body.request_body.FIELDS.boost_spec)` for more details.  
`tags[]` |  `string` Custom tags associated with the product.At most 250 values are allowed per `[Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product)`. This value must be a UTF-8 encoded string with a length limit of 1,000 characters. Otherwise, an INVALID_ARGUMENT error is returned.This tag can be used for filtering recommendation results by passing the tag as part of the `[PredictRequest.filter](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.placements/predict#body.request_body.FIELDS.filter)`.Corresponding properties: Google Merchant Center property [custom_label_0–4](https://support.google.com/merchants/answer/6324473).  
`priceInfo` |  `object (`[PriceInfo](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.PriceInfo)`)` Product price and cost information.Corresponding properties: Google Merchant Center property [price](https://support.google.com/merchants/answer/6324371).  
`rating` |  `object (`[Rating](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.Rating)`)` The rating of this product.  
`availableTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` The timestamp when this `[Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product)` becomes available for `[SearchService.Search](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.placements/search#google.cloud.retail.v2alpha.SearchService.Search)`. Note that this is only applicable to `[Type.PRIMARY](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.Type.ENUM_VALUES.PRIMARY)` and `[Type.COLLECTION](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.Type.ENUM_VALUES.COLLECTION)`, and ignored for `[Type.VARIANT](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.Type.ENUM_VALUES.VARIANT)`.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`availability` |  `enum (`[Availability](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.Availability)`)` The online availability of the `[Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product)`. Default to `[Availability.IN_STOCK](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.Availability.ENUM_VALUES.IN_STOCK)`.For primary products with variants set the availability of the primary as `[Availability.OUT_OF_STOCK](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.Availability.ENUM_VALUES.OUT_OF_STOCK)` and set the true availability at the variant level. This way the primary product will be considered "in stock" as long as it has at least one variant in stock.For primary products with no variants set the true availability at the primary level.Corresponding properties: Google Merchant Center property [availability](https://support.google.com/merchants/answer/6324448). Schema.org property [Offer.availability](https://schema.org/availability).  
`availableQuantity` |  `integer` The available quantity of the item.  
`fulfillmentInfo[]` |  `object (`[FulfillmentInfo](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.FulfillmentInfo)`)` Fulfillment information, such as the store IDs for in-store pickup or region IDs for different shipping methods.All the elements must have distinct `[FulfillmentInfo.type](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.FulfillmentInfo.FIELDS.type)`. Otherwise, an INVALID_ARGUMENT error is returned.  
`uri` |  `string` Canonical URL directly linking to the product detail page.It is strongly recommended to provide a valid uri for the product, otherwise the service performance could be significantly degraded.This field must be a UTF-8 encoded string with a length limit of 5,000 characters. Otherwise, an INVALID_ARGUMENT error is returned.Corresponding properties: Google Merchant Center property [link](https://support.google.com/merchants/answer/6324416). Schema.org property [Offer.url](https://schema.org/url).  
`images[]` |  `object (`[Image](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.Image)`)` Product images for the product. We highly recommend putting the main image first.A maximum of 300 images are allowed.Corresponding properties: Google Merchant Center property [image_link](https://support.google.com/merchants/answer/6324350). Schema.org property [Product.image](https://schema.org/image).  
`audience` |  `object (`[Audience](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.Audience)`)` The target group associated with a given audience (e.g. male, veterans, car owners, musicians, etc.) of the product.  
`colorInfo` |  `object (`[ColorInfo](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.ColorInfo)`)` The color of the product.Corresponding properties: Google Merchant Center property [color](https://support.google.com/merchants/answer/6324487). Schema.org property [Product.color](https://schema.org/color).  
`sizes[]` |  `string` The size of the product. To represent different size systems or size types, consider using this format: [[[size_system:]size_type:]size_value].For example, in "US:MENS:M", "US" represents size system; "MENS" represents size type; "M" represents size value. In "GIRLS:27", size system is empty; "GIRLS" represents size type; "27" represents size value. In "32 inches", both size system and size type are empty, while size value is "32 inches".A maximum of 20 values are allowed per `[Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product)`. Each value must be a UTF-8 encoded string with a length limit of 128 characters. Otherwise, an INVALID_ARGUMENT error is returned.Corresponding properties: Google Merchant Center property [size](https://support.google.com/merchants/answer/6324492), [size_type](https://support.google.com/merchants/answer/6324497), and [size_system](https://support.google.com/merchants/answer/6324502). Schema.org property [Product.size](https://schema.org/size).  
`materials[]` |  `string` The material of the product. For example, "leather", "wooden".A maximum of 20 values are allowed. Each value must be a UTF-8 encoded string with a length limit of 200 characters. Otherwise, an INVALID_ARGUMENT error is returned.Corresponding properties: Google Merchant Center property [material](https://support.google.com/merchants/answer/6324410). Schema.org property [Product.material](https://schema.org/material).  
`patterns[]` |  `string` The pattern or graphic print of the product. For example, "striped", "polka dot", "paisley".A maximum of 20 values are allowed per `[Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product)`. Each value must be a UTF-8 encoded string with a length limit of 128 characters. Otherwise, an INVALID_ARGUMENT error is returned.Corresponding properties: Google Merchant Center property [pattern](https://support.google.com/merchants/answer/6324483). Schema.org property [Product.pattern](https://schema.org/pattern).  
`conditions[]` |  `string` The condition of the product. Strongly encouraged to use the standard values: "new", "refurbished", "used".A maximum of 1 value is allowed per `[Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product)`. Each value must be a UTF-8 encoded string with a length limit of 128 characters. Otherwise, an INVALID_ARGUMENT error is returned.Corresponding properties: Google Merchant Center property [condition](https://support.google.com/merchants/answer/6324469). Schema.org property [Offer.itemCondition](https://schema.org/itemCondition).  
`promotions[]` |  `object (`[Promotion](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.Promotion)`)` The promotions applied to the product. A maximum of 10 values are allowed per `[Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product)`. Only `[Promotion.promotion_id](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.Promotion.FIELDS.promotion_id)` will be used, other fields will be ignored if set.  
`publishTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` The timestamp when the product is published by the retailer for the first time, which indicates the freshness of the products. Note that this field is different from `[availableTime](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.FIELDS.available_time)`, given it purely describes product freshness regardless of when it is available on search and recommendation.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`retrievableFields  
**(deprecated)**` |  `string (`[FieldMask](https://protobuf.dev/reference/protobuf/google.protobuf/#field-mask)` format)` This item is deprecated!Indicates which fields in the `[Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product)`s are returned in `[SearchResponse](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/SearchResponse)`.Supported fields for all `[type](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.FIELDS.type)`s:

  * `[audience](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.FIELDS.audience)`
  * `[availability](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.FIELDS.availability)`
  * `[brands](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.FIELDS.brands)`
  * `[colorInfo](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.FIELDS.color_info)`
  * `[conditions](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.FIELDS.conditions)`
  * `[gtin](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.FIELDS.gtin)`
  * `[materials](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.FIELDS.materials)`
  * `[name](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.FIELDS.name)`
  * `[patterns](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.FIELDS.patterns)`
  * `[priceInfo](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.FIELDS.price_info)`
  * `[rating](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.FIELDS.rating)`
  * `[sizes](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.FIELDS.sizes)`
  * `[title](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.FIELDS.title)`
  * `[uri](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.FIELDS.uri)`

Supported fields only for `[Type.PRIMARY](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.Type.ENUM_VALUES.PRIMARY)` and `[Type.COLLECTION](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.Type.ENUM_VALUES.COLLECTION)`:

  * `[categories](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.FIELDS.categories)`
  * `[description](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.FIELDS.description)`
  * `[images](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.FIELDS.images)`

Supported fields only for `[Type.VARIANT](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.Type.ENUM_VALUES.VARIANT)`:

  * Only the first image in `[images](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.FIELDS.images)`

To mark `[attributes](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.FIELDS.attributes)` as retrievable, include paths of the form "attributes.key" where "key" is the key of a custom attribute, as specified in `[attributes](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.FIELDS.attributes)`.For `[Type.PRIMARY](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.Type.ENUM_VALUES.PRIMARY)` and `[Type.COLLECTION](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.Type.ENUM_VALUES.COLLECTION)`, the following fields are always returned in `[SearchResponse](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/SearchResponse)` by default:

  * `[name](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.FIELDS.name)`

For `[Type.VARIANT](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.Type.ENUM_VALUES.VARIANT)`, the following fields are always returned in by default:

  * `[name](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.FIELDS.name)`
  * `[colorInfo](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.FIELDS.color_info)`

Note: Returning more fields in `[SearchResponse](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/SearchResponse)` can increase response payload size and serving latency.This field is deprecated. Use the retrievable site-wide control instead.This is a comma-separated list of fully qualified names of fields. Example: `"user.displayName,photo"`.  
`variants[]` |  `object (`[Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product)`)` Output only. Product variants grouped together on primary product which share similar product attributes. It's automatically grouped by `[primaryProductId](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.FIELDS.primary_product_id)` for all the product variants. Only populated for `[Type.PRIMARY](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.Type.ENUM_VALUES.PRIMARY)` `[Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product)`s.Note: This field is OUTPUT_ONLY for `[ProductService.GetProduct](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products/get#google.cloud.retail.v2alpha.ProductService.GetProduct)`. Do not set this field in API requests.  
`localInventories[]` |  `object (`[LocalInventory](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.LocalInventory)`)` Output only. A list of local inventories specific to different places.This field can be managed by `[ProductService.AddLocalInventories](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products/addLocalInventories#google.cloud.retail.v2alpha.ProductService.AddLocalInventories)` and `[ProductService.RemoveLocalInventories](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products/removeLocalInventories#google.cloud.retail.v2alpha.ProductService.RemoveLocalInventories)` APIs if fine-grained, high-volume updates are necessary.  
Union field `expiration`.`expiration` can be only one of the following:  
`expireTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Note that this field is applied in the following ways:

  * If the `[Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product)` is already expired when it is uploaded, this product is not indexed for search.
  * If the `[Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product)` is not expired when it is uploaded, only the `[Type.PRIMARY](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.Type.ENUM_VALUES.PRIMARY)`'s and `[Type.COLLECTION](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.Type.ENUM_VALUES.COLLECTION)`'s expireTime is respected, and `[Type.VARIANT](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.Type.ENUM_VALUES.VARIANT)`'s expireTime is not used.

In general, we suggest the users to delete the stale products explicitly, instead of using this field to determine staleness.`[expireTime](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.FIELDS.expire_time)` must be later than `[availableTime](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.FIELDS.available_time)` and `[publishTime](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.FIELDS.publish_time)`, otherwise an INVALID_ARGUMENT error is thrown.Corresponding properties: Google Merchant Center property [expiration_date](https://support.google.com/merchants/answer/6324499).Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`ttl` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` Input only. The TTL (time to live) of the product. Note that this is only applicable to `[Type.PRIMARY](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.Type.ENUM_VALUES.PRIMARY)` and `[Type.COLLECTION](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.Type.ENUM_VALUES.COLLECTION)`, and ignored for `[Type.VARIANT](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.Type.ENUM_VALUES.VARIANT)`. In general, we suggest the users to delete the stale products explicitly, instead of using this field to determine staleness.If it is set, it must be a non-negative value, and `[expireTime](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.FIELDS.expire_time)` is set as current timestamp plus `[ttl](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.FIELDS.ttl)`. The derived `[expireTime](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.FIELDS.expire_time)` is returned in the output and `[ttl](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.FIELDS.ttl)` is left blank when retrieving the `[Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product)`.If it is set, the product is not available for `[SearchService.Search](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.placements/search#google.cloud.retail.v2alpha.SearchService.Search)` after current timestamp plus `[ttl](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.FIELDS.ttl)`. However, the product can still be retrieved by `[ProductService.GetProduct](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products/get#google.cloud.retail.v2alpha.ProductService.GetProduct)` and `[ProductService.ListProducts](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products/list#google.cloud.retail.v2alpha.ProductService.ListProducts)`.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
  
### Type

The type of this product.

Enums  
---  
`TYPE_UNSPECIFIED` | Default value. Default to `[Catalog.product_level_config.ingestion_product_type](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs#ProductLevelConfig.FIELDS.ingestion_product_type)` if unset.  
`PRIMARY` | The primary type.As the primary unit for predicting, indexing and search serving, a `[Type.PRIMARY](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.Type.ENUM_VALUES.PRIMARY)` `[Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product)` is grouped with multiple `[Type.VARIANT](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.Type.ENUM_VALUES.VARIANT)` `[Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product)`s.  
`VARIANT` | The variant type.`[Type.VARIANT](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.Type.ENUM_VALUES.VARIANT)` `[Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product)`s usually share some common attributes on the same `[Type.PRIMARY](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.Type.ENUM_VALUES.PRIMARY)` `[Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product)`s, but they have variant attributes like different colors, sizes and prices, etc.  
`COLLECTION` | The collection type. Collection products are bundled `[Type.PRIMARY](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.Type.ENUM_VALUES.PRIMARY)` `[Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product)`s or `[Type.VARIANT](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.Type.ENUM_VALUES.VARIANT)` `[Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product)`s that are sold together, such as a jewelry set with necklaces, earrings and rings, etc.  
  
### PriceInfo

The price information of a `[Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product)`.

JSON representation  
---  
      
    
    {
      "currencyCode": string,
      "price": number,
      "originalPrice": number,
      "cost": number,
      "priceEffectiveTime": string,
      "priceExpireTime": string,
      "priceRange": {
        object ([PriceRange](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.PriceRange))
      }
    }  
  
Fields  
---  
`currencyCode` |  `string` The 3-letter currency code defined in [ISO 4217](https://www.iso.org/iso-4217-currency-codes.html).If this field is an unrecognizable currency code, an INVALID_ARGUMENT error is returned.The `[Product.Type.VARIANT](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.Type.ENUM_VALUES.VARIANT)` `[Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product)`s with the same `[Product.primary_product_id](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.FIELDS.primary_product_id)` must share the same `[currencyCode](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.PriceInfo.FIELDS.currency_code)`. Otherwise, a FAILED_PRECONDITION error is returned.  
`price` |  `number` Price of the product.Google Merchant Center property [price](https://support.google.com/merchants/answer/6324371). Schema.org property [Offer.price](https://schema.org/price).  
`originalPrice` |  `number` Price of the product without any discount. If zero, by default set to be the `[price](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.PriceInfo.FIELDS.price)`. If set, `[originalPrice](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.PriceInfo.FIELDS.original_price)` should be greater than or equal to `[price](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.PriceInfo.FIELDS.price)`, otherwise an INVALID_ARGUMENT error is thrown.  
`cost` |  `number` The costs associated with the sale of a particular product. Used for gross profit reporting.

  * Profit = `[price](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.PriceInfo.FIELDS.price)` \- `[cost](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.PriceInfo.FIELDS.cost)`

Google Merchant Center property [cost_of_goods_sold](https://support.google.com/merchants/answer/9017895).  
`priceEffectiveTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` The timestamp when the `[price](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.PriceInfo.FIELDS.price)` starts to be effective. This can be set as a future timestamp, and the `[price](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.PriceInfo.FIELDS.price)` is only used for search after `[priceEffectiveTime](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.PriceInfo.FIELDS.price_effective_time)`. If so, the `[originalPrice](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.PriceInfo.FIELDS.original_price)` must be set and `[originalPrice](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.PriceInfo.FIELDS.original_price)` is used before `[priceEffectiveTime](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.PriceInfo.FIELDS.price_effective_time)`.Do not set if `[price](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.PriceInfo.FIELDS.price)` is always effective because it will cause additional latency during search.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`priceExpireTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` The timestamp when the `[price](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.PriceInfo.FIELDS.price)` stops to be effective. The `[price](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.PriceInfo.FIELDS.price)` is used for search before `[priceExpireTime](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.PriceInfo.FIELDS.price_expire_time)`. If this field is set, the `[originalPrice](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.PriceInfo.FIELDS.original_price)` must be set and `[originalPrice](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.PriceInfo.FIELDS.original_price)` is used after `[priceExpireTime](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.PriceInfo.FIELDS.price_expire_time)`.Do not set if `[price](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.PriceInfo.FIELDS.price)` is always effective because it will cause additional latency during search.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`priceRange` |  `object (`[PriceRange](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.PriceRange)`)` Output only. The price range of all the child `[Product.Type.VARIANT](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.Type.ENUM_VALUES.VARIANT)` `[Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product)`s grouped together on the `[Product.Type.PRIMARY](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.Type.ENUM_VALUES.PRIMARY)` `[Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product)`. Only populated for `[Product.Type.PRIMARY](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.Type.ENUM_VALUES.PRIMARY)` `[Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product)`s.Note: This field is OUTPUT_ONLY for `[ProductService.GetProduct](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products/get#google.cloud.retail.v2alpha.ProductService.GetProduct)`. Do not set this field in API requests.  
  
### PriceRange

The price range of all `[variant](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.Type.ENUM_VALUES.VARIANT)` `[Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product)` having the same `[Product.primary_product_id](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.FIELDS.primary_product_id)`.

JSON representation  
---  
      
    
    {
      "price": {
        object ([Interval](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/Interval))
      },
      "originalPrice": {
        object ([Interval](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/Interval))
      }
    }  
  
Fields  
---  
`price` |  `object (`[Interval](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/Interval)`)` The inclusive `[Product.pricing_info.price](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.PriceInfo.FIELDS.price)` interval of all `[variant](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.Type.ENUM_VALUES.VARIANT)` `[Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product)` having the same `[Product.primary_product_id](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.FIELDS.primary_product_id)`.  
`originalPrice` |  `object (`[Interval](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/Interval)`)` The inclusive `[Product.pricing_info.original_price](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.PriceInfo.FIELDS.original_price)` internal of all `[variant](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.Type.ENUM_VALUES.VARIANT)` `[Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product)` having the same `[Product.primary_product_id](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.FIELDS.primary_product_id)`.  
  
### Rating

The rating of a `[Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product)`.

JSON representation  
---  
      
    
    {
      "ratingCount": integer,
      "averageRating": number,
      "ratingHistogram": [
        integer
      ]
    }  
  
Fields  
---  
`ratingCount` |  `integer` The total number of ratings. This value is independent of the value of `[ratingHistogram](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.Rating.FIELDS.rating_histogram)`.This value must be nonnegative. Otherwise, an INVALID_ARGUMENT error is returned.  
`averageRating` |  `number` The average rating of the `[Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product)`.The rating is scaled at 1-5. Otherwise, an INVALID_ARGUMENT error is returned.  
`ratingHistogram[]` |  `integer` List of rating counts per rating value (index = rating - 1). The list is empty if there is no rating. If the list is non-empty, its size is always 5. Otherwise, an INVALID_ARGUMENT error is returned.For example, [41, 14, 13, 47, 303]. It means that the `[Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product)` got 41 ratings with 1 star, 14 ratings with 2 star, and so on.  
  
### Availability

Product availability. If this field is unspecified, the product is assumed to be in stock.

Enums  
---  
`AVAILABILITY_UNSPECIFIED` | Default product availability. Default to `[Availability.IN_STOCK](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.Availability.ENUM_VALUES.IN_STOCK)` if unset.  
`IN_STOCK` | Product in stock.  
`OUT_OF_STOCK` | Product out of stock.  
`PREORDER` | Product that is in pre-order state.  
`BACKORDER` | Product that is back-ordered (i.e. temporarily out of stock).  
  
### FulfillmentInfo

Fulfillment information, such as the store IDs for in-store pickup or region IDs for different shipping methods.

JSON representation  
---  
      
    
    {
      "type": string,
      "placeIds": [
        string
      ]
    }  
  
Fields  
---  
`type` |  `string` The fulfillment type, including commonly used types (such as pickup in store and same day delivery), and custom types. Customers have to map custom types to their display names before rendering UI.Supported values:

  * "pickup-in-store"
  * "ship-to-store"
  * "same-day-delivery"
  * "next-day-delivery"
  * "custom-type-1"
  * "custom-type-2"
  * "custom-type-3"
  * "custom-type-4"
  * "custom-type-5"

If this field is set to an invalid value other than these, an INVALID_ARGUMENT error is returned.  
`placeIds[]` |  `string` The IDs for this `[type](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.FulfillmentInfo.FIELDS.type)`, such as the store IDs for `[FulfillmentInfo.type.pickup-in-store](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.FulfillmentInfo.FIELDS.type)` or the region IDs for `[FulfillmentInfo.type.same-day-delivery](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.FulfillmentInfo.FIELDS.type)`.A maximum of 3000 values are allowed. Each value must be a string with a length limit of 30 characters, matching the pattern `[a-zA-Z0-9_-]+`, such as "store1" or "REGION-2". Otherwise, an INVALID_ARGUMENT error is returned.  
  
### Image

`[Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product)` image. Recommendations AI and Retail Search use product images to improve prediction and search results. Product images can be returned in results, and are shown in prediction or search previews in the console. Please try to provide correct product images and avoid using images with size too small.

JSON representation  
---  
      
    
    {
      "uri": string,
      "height": integer,
      "width": integer
    }  
  
Fields  
---  
`uri` |  `string` Required. URI of the image.This field must be a valid UTF-8 encoded URI with a length limit of 5,000 characters. Otherwise, an INVALID_ARGUMENT error is returned.Google Merchant Center property [image_link](https://support.google.com/merchants/answer/6324350). Schema.org property [Product.image](https://schema.org/image).  
`height` |  `integer` Height of the image in number of pixels.This field must be nonnegative. Otherwise, an INVALID_ARGUMENT error is returned.  
`width` |  `integer` Width of the image in number of pixels.This field must be nonnegative. Otherwise, an INVALID_ARGUMENT error is returned.  
  
### Audience

An intended audience of the `[Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product)` for whom it's sold.

JSON representation  
---  
      
    
    {
      "genders": [
        string
      ],
      "ageGroups": [
        string
      ]
    }  
  
Fields  
---  
`genders[]` |  `string` The genders of the audience. Strongly encouraged to use the standard values: "male", "female", "unisex".At most 5 values are allowed. Each value must be a UTF-8 encoded string with a length limit of 128 characters. Otherwise, an INVALID_ARGUMENT error is returned.Google Merchant Center property [gender](https://support.google.com/merchants/answer/6324479). Schema.org property [Product.audience.suggestedGender](https://schema.org/suggestedGender).  
`ageGroups[]` |  `string` The age groups of the audience. Strongly encouraged to use the standard values: "newborn" (up to 3 months old), "infant" (3–12 months old), "toddler" (1–5 years old), "kids" (5–13 years old), "adult" (typically teens or older).At most 5 values are allowed. Each value must be a UTF-8 encoded string with a length limit of 128 characters. Otherwise, an INVALID_ARGUMENT error is returned.Google Merchant Center property [age_group](https://support.google.com/merchants/answer/6324463). Schema.org property [Product.audience.suggestedMinAge](https://schema.org/suggestedMinAge) and [Product.audience.suggestedMaxAge](https://schema.org/suggestedMaxAge).  
  
### ColorInfo

The color information of a `[Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product)`.

JSON representation  
---  
      
    
    {
      "colorFamilies": [
        string
      ],
      "colors": [
        string
      ]
    }  
  
Fields  
---  
`colorFamilies[]` |  `string` The standard color families. Strongly recommended to use the following standard color groups: "Red", "Pink", "Orange", "Yellow", "Purple", "Green", "Cyan", "Blue", "Brown", "White", "Gray", "Black" and "Mixed". Normally it is expected to have only 1 color family. May consider using single "Mixed" instead of multiple values.A maximum of 5 values are allowed. Each value must be a UTF-8 encoded string with a length limit of 128 characters. Otherwise, an INVALID_ARGUMENT error is returned.Google Merchant Center property [color](https://support.google.com/merchants/answer/6324487). Schema.org property [Product.color](https://schema.org/color).The colorFamilies field as a system attribute is not a required field but strongly recommended to be specified. Google Search models treat this field as more important than a custom product attribute when specified.  
`colors[]` |  `string` The color display names, which may be different from standard color family names, such as the color aliases used in the website frontend. Normally it is expected to have only 1 color. May consider using single "Mixed" instead of multiple values.A maximum of 75 colors are allowed. Each value must be a UTF-8 encoded string with a length limit of 128 characters. Otherwise, an INVALID_ARGUMENT error is returned.Google Merchant Center property [color](https://support.google.com/merchants/answer/6324487). Schema.org property [Product.color](https://schema.org/color).  
  
### Promotion

Promotion specification.

JSON representation  
---  
      
    
    {
      "promotionId": string
    }  
  
Fields  
---  
`promotionId` |  `string` `[Promotion](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.Promotion)` identifier, which is the final component of `name`. For example, this field is "free_gift", if `name` is `projects/*/locations/global/catalogs/default_catalog/promotions/free_gift`.The value must be a UTF-8 encoded string with a length limit of 128 characters, and match the pattern: `[a-zA-Z][a-zA-Z0-9_]*`. For example, id0LikeThis or ID_1_LIKE_THIS. Otherwise, an INVALID_ARGUMENT error is returned.Corresponds to Google Merchant Center property [promotionId](https://support.google.com/merchants/answer/7050148).  
  
### LocalInventory

The inventory information at a place (e.g. a store) identified by a place ID.

JSON representation  
---  
      
    
    {
      "placeId": string,
      "priceInfo": {
        object ([PriceInfo](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.PriceInfo))
      },
      "availability": enum ([Availability](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.Availability_1)),
      "attributes": {
        string: {
          "text": [
            string
          ],
          "numbers": [
            number
          ],
          "searchable": boolean,
          "indexable": boolean
        },
        ...
      },
      "fulfillmentTypes": [
        string
      ]
    }  
  
Fields  
---  
`placeId` |  `string` Optional. The place ID for the current set of inventory information.  
`priceInfo` |  `object (`[PriceInfo](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.PriceInfo)`)` Optional. Product price and cost information.Google Merchant Center property [price](https://support.google.com/merchants/answer/6324371).  
`availability` |  `enum (`[Availability](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.Availability_1)`)` Optional. The availability of the `[Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product)` at this placeId. Default to `[Availability.IN_STOCK](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.Availability_1.ENUM_VALUES.IN_STOCK)`.For primary products with variants set the availability of the primary as `[Availability.OUT_OF_STOCK](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.Availability_1.ENUM_VALUES.OUT_OF_STOCK)` and set the true availability at the variant level. This way the primary product will be considered "in stock" as long as it has at least one variant in stock.For primary products with no variants set the true availability at the primary level.Corresponding properties: Google Merchant Center property [availability](https://support.google.com/merchants/answer/6324448). Schema.org property [Offer.availability](https://schema.org/availability).This field is currently only used by the Recommendations API. For Search, please make use of `[fulfillmentTypes](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.LocalInventory.FIELDS.fulfillment_types)` or custom attributes for similar behaviour. See [here]( <https://cloud.google.com/gemini-enterprise-cx/ai-commerce-search/local-inventory-updates#local-inventory-update-methods>) for more details.  
`attributes` |  `map (key: string, value: object)` Optional. Additional local inventory attributes, for example, store name, promotion tags, etc.This field needs to pass all below criteria, otherwise an INVALID_ARGUMENT error is returned:

  * At most 30 attributes are allowed.
  * The key must be a UTF-8 encoded string with a length limit of 32 characters.
  * The key must match the pattern: `[a-zA-Z0-9][a-zA-Z0-9_]*`. For example, key0LikeThis or KEY_1_LIKE_THIS.
  * The attribute values must be of the same type (text or number).
  * Only 1 value is allowed for each attribute.
  * For text values, the length limit is 256 UTF-8 characters.
  * The attribute does not support search. The `searchable` field should be unset or set to false.
  * The max summed total bytes of custom attribute keys and values per product is 5MiB.

  
`attributes.text[]` |  `string` The textual values of this custom attribute. For example, `["yellow", "green"]` when the key is "color".Empty string is not allowed. Otherwise, an INVALID_ARGUMENT error is returned.Exactly one of `text` or `numbers` should be set. Otherwise, an INVALID_ARGUMENT error is returned.  
`attributes.numbers[]` |  `number` The numerical values of this custom attribute. For example, `[2.3, 15.4]` when the key is "lengths_cm".Exactly one of `text` or `numbers` should be set. Otherwise, an INVALID_ARGUMENT error is returned.  
`attributes.searchable  
**(deprecated)**` |  `boolean` This field is normally ignored unless `[AttributesConfig.attribute_config_level](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.attributesConfig#AttributesConfig.FIELDS.attribute_config_level)` of the `[Catalog](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs#Catalog)` is set to the deprecated 'PRODUCT_LEVEL_ATTRIBUTE_CONFIG' mode. For information about product-level attribute configuration, see [Configuration modes](https://cloud.google.com/gemini-enterprise-cx/ai-commerce-search/attribute-config#config-modes). If true, custom attribute values are searchable by text queries in `[SearchService.Search](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.placements/search#google.cloud.retail.v2alpha.SearchService.Search)`.This field is ignored in a `[UserEvent](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.userEvents#UserEvent)`.Only set if type `text` is set. Otherwise, a INVALID_ARGUMENT error is returned.  
`attributes.indexable  
**(deprecated)**` |  `boolean` This field is normally ignored unless `[AttributesConfig.attribute_config_level](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.attributesConfig#AttributesConfig.FIELDS.attribute_config_level)` of the `[Catalog](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs#Catalog)` is set to the deprecated 'PRODUCT_LEVEL_ATTRIBUTE_CONFIG' mode. For information about product-level attribute configuration, see [Configuration modes](https://cloud.google.com/gemini-enterprise-cx/ai-commerce-search/attribute-config#config-modes). If true, custom attribute values are indexed, so that they can be filtered, faceted or boosted in `[SearchService.Search](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.placements/search#google.cloud.retail.v2alpha.SearchService.Search)`.This field is ignored in a `[UserEvent](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.userEvents#UserEvent)`.See `[SearchRequest.filter](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.placements/search#body.request_body.FIELDS.filter)`, `[SearchRequest.facet_specs](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.placements/search#body.request_body.FIELDS.facet_specs)` and `[SearchRequest.boost_spec](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.placements/search#body.request_body.FIELDS.boost_spec)` for more details.  
`fulfillmentTypes[]` |  `string` Optional. Supported fulfillment types. Valid fulfillment type values include commonly used types (such as pickup in store and same day delivery), and custom types. Customers have to map custom types to their display names before rendering UI.Supported values:

  * "pickup-in-store"
  * "ship-to-store"
  * "same-day-delivery"
  * "next-day-delivery"
  * "custom-type-1"
  * "custom-type-2"
  * "custom-type-3"
  * "custom-type-4"
  * "custom-type-5"

If this field is set to an invalid value other than these, an INVALID_ARGUMENT error is returned.All the elements must be distinct. Otherwise, an INVALID_ARGUMENT error is returned.  
  
### Availability

Product availability. If this field is unspecified, the product is assumed to be in stock.

Enums  
---  
`AVAILABILITY_UNSPECIFIED` | Default product availability. Default to `[Availability.IN_STOCK](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.Availability_1.ENUM_VALUES.IN_STOCK)` if unset.  
`IN_STOCK` | Product in stock.  
`OUT_OF_STOCK` | Product out of stock.  
`PREORDER` | Product that is in pre-order state.  
`BACKORDER` | Product that is back-ordered (i.e. temporarily out of stock).  
  
## Methods  
  
---  
  
### `[addFulfillmentPlaces](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products/addFulfillmentPlaces)`

|  We recommend that you use the `[ProductService.AddLocalInventories](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products/addLocalInventories#google.cloud.retail.v2alpha.ProductService.AddLocalInventories)` method instead of the `[ProductService.AddFulfillmentPlaces](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products/addFulfillmentPlaces#google.cloud.retail.v2alpha.ProductService.AddFulfillmentPlaces)` method.  
  
### `[addLocalInventories](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products/addLocalInventories)`

|  Updates local inventory information for a `[Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product)` at a list of places, while respecting the last update timestamps of each inventory field.  
  
### `[create](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products/create)`

|  Creates a `[Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product)`.  
  
### `[delete](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products/delete)`

|  Deletes a `[Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product)`.  
  
### `[export](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products/export)`

|  Exports multiple `[Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product)`s.  
  
### `[get](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products/get)`

|  Gets a `[Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product)`.  
  
### `[import](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products/import)`

|  Bulk import of multiple `[Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product)`s.  
  
### `[list](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products/list)`

|  Gets a list of `[Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product)`s.  
  
### `[patch](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products/patch)`

|  Updates a `[Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product)`.  
  
### `[purge](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products/purge)`

|  Permanently deletes all selected `[Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product)`s under a branch.  
  
### `[removeFulfillmentPlaces](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products/removeFulfillmentPlaces)`

|  We recommend that you use the `[ProductService.RemoveLocalInventories](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products/removeLocalInventories#google.cloud.retail.v2alpha.ProductService.RemoveLocalInventories)` method instead of the `[ProductService.RemoveFulfillmentPlaces](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products/removeFulfillmentPlaces#google.cloud.retail.v2alpha.ProductService.RemoveFulfillmentPlaces)` method.  
  
### `[removeLocalInventories](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products/removeLocalInventories)`

|  Remove local inventory information for a `[Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product)` at a list of places at a removal timestamp.  
  
### `[setInventory](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products/setInventory)`

|  Updates inventory information for a `[Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product)` while respecting the last update timestamps of each inventory field.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-08 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-08 UTC."],[],[]] 
