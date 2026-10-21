---
url: https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products/setInventory/
title: Method: projects.locations.catalogs.branches.products.setInventory \u00a0|\u00a0 AI Commerce Search in Gemini Enterprise for Customer Experience \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T01:17:27.635916+00:00
---

# Method: projects.locations.catalogs.branches.products.setInventory  |  AI Commerce Search in Gemini Enterprise for Customer Experience  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products/setInventory/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ AI Commerce Search ](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search)



Send feedback 

#  Method: projects.locations.catalogs.branches.products.setInventory Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
      * JSON representation
      * JSON representation
      * JSON representation
      * JSON representation
      * JSON representation
      * JSON representation
      * JSON representation
      * JSON representation
      * JSON representation
  * Response body
  * Authorization scopes
  * IAM Permissions
  * Try it!



Updates inventory information for a `[Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product)` while respecting the last update timestamps of each inventory field.

This process is asynchronous and does not require the `[Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product)` to exist before updating fulfillment information. If the request is valid, the update is enqueued and processed downstream. As a consequence, when a response is returned, updates are not immediately manifested in the `[Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product)` queried by `[ProductService.GetProduct](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products/get#google.cloud.retail.v2alpha.ProductService.GetProduct)` or `[ProductService.ListProducts](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products/list#google.cloud.retail.v2alpha.ProductService.ListProducts)`.

When inventory is updated with `[ProductService.CreateProduct](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products/create#google.cloud.retail.v2alpha.ProductService.CreateProduct)` and `[ProductService.UpdateProduct](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products/patch#google.cloud.retail.v2alpha.ProductService.UpdateProduct)`, the specified inventory field value(s) overwrite any existing value(s) while ignoring the last update time for this field. Furthermore, the last update times for the specified inventory fields are overwritten by the times of the `[ProductService.CreateProduct](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products/create#google.cloud.retail.v2alpha.ProductService.CreateProduct)` or `[ProductService.UpdateProduct](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products/patch#google.cloud.retail.v2alpha.ProductService.UpdateProduct)` request.

If no inventory fields are set in `CreateProductRequest.product`, then any pre-existing inventory information for this product is used.

If no inventory fields are set in `[SetInventoryRequest.set_mask](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products/setInventory#body.request_body.FIELDS.set_mask)`, then any existing inventory information is preserved.

Pre-existing inventory information can only be updated with `[ProductService.SetInventory](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products/setInventory#google.cloud.retail.v2alpha.ProductService.SetInventory)`, `[ProductService.AddFulfillmentPlaces](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products/addFulfillmentPlaces#google.cloud.retail.v2alpha.ProductService.AddFulfillmentPlaces)`, and `[ProductService.RemoveFulfillmentPlaces](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products/removeFulfillmentPlaces#google.cloud.retail.v2alpha.ProductService.RemoveFulfillmentPlaces)`.

The returned `[Operation](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/Shared.Types/ListOperationsResponse#Operation)`s is obsolete after one day, and the `[operations.get](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.operations/get#google.longrunning.Operations.GetOperation)` API returns `NOT_FOUND` afterwards.

If conflicting updates are issued, the `[Operation](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/Shared.Types/ListOperationsResponse#Operation)`s associated with the stale updates are not marked as `[done](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/Shared.Types/ListOperationsResponse#Operation.FIELDS.done)` until they are obsolete.

### HTTP request

`POST https://retail.googleapis.com/v2alpha/{inventory.name=projects/*/locations/*/catalogs/*/branches/*/products/**}:setInventory`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`inventory.name` |  `string` Immutable. Full resource name of the product, such as `projects/*/locations/global/catalogs/default_catalog/branches/default_branch/products/productId`.  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "inventory": {
        "expireTime": string,
        "ttl": string,
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
          "currencyCode": string,
          "price": number,
          "originalPrice": number,
          "cost": number,
          "priceEffectiveTime": string,
          "priceExpireTime": string,
          "priceRange": {
            object ([PriceRange](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.PriceRange))
          }
        },
        "rating": {
          "ratingCount": integer,
          "averageRating": number,
          "ratingHistogram": [
            integer
          ]
        },
        "availableTime": string,
        "availability": enum ([Availability](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.Availability)),
        "availableQuantity": integer,
        "fulfillmentInfo": [
          {
            "type": string,
            "placeIds": [
              string
            ]
          }
        ],
        "uri": string,
        "images": [
          {
            "uri": string,
            "height": integer,
            "width": integer
          }
        ],
        "audience": {
          "genders": [
            string
          ],
          "ageGroups": [
            string
          ]
        },
        "colorInfo": {
          "colorFamilies": [
            string
          ],
          "colors": [
            string
          ]
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
            "promotionId": string
          }
        ],
        "publishTime": string,
        "retrievableFields": string,
        "variants": [
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
        ],
        "localInventories": [
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
        ]
      },
      "setMask": string,
      "setTime": string,
      "allowMissing": boolean
    }  
  
Fields  
---  
`inventory.id` |  `string` Immutable. `[Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product)` identifier, which is the final component of `[name](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.FIELDS.name)`. For example, this field is "id_1", if `[name](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.FIELDS.name)` is `projects/*/locations/global/catalogs/default_catalog/branches/default_branch/products/id_1`.This field must be a UTF-8 encoded string with a length limit of 128 characters. Otherwise, an INVALID_ARGUMENT error is returned.Corresponding properties: Google Merchant Center property [id](https://support.google.com/merchants/answer/6324405). Schema.org property [Product.sku](https://schema.org/sku).  
`inventory.type` |  `enum (`[Type](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.Type)`)` Immutable. The type of the product. Default to `[Catalog.product_level_config.ingestion_product_type](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs#ProductLevelConfig.FIELDS.ingestion_product_type)` if unset.  
`inventory.primaryProductId` |  `string` Variant group identifier. Must be an `[id](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.FIELDS.id)`, with the same parent branch with this product. Otherwise, an error is thrown.For `[Type.PRIMARY](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.Type.ENUM_VALUES.PRIMARY)` `[Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product)`s, this field can only be empty or set to the same value as `[id](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.FIELDS.id)`.For VARIANT `[Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product)`s, this field cannot be empty. A maximum of 2,000 products are allowed to share the same `[Type.PRIMARY](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.Type.ENUM_VALUES.PRIMARY)` `[Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product)`. Otherwise, an INVALID_ARGUMENT error is returned.Corresponding properties: Google Merchant Center property [item_group_id](https://support.google.com/merchants/answer/6324507). Schema.org property [Product.inProductGroupWithID](https://schema.org/inProductGroupWithID).  
`inventory.collectionMemberIds[]` |  `string` The `[id](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.FIELDS.id)` of the collection members when `[type](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.FIELDS.type)` is `[Type.COLLECTION](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.Type.ENUM_VALUES.COLLECTION)`.Non-existent product ids are allowed. The `[type](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.FIELDS.type)` of the members must be either `[Type.PRIMARY](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.Type.ENUM_VALUES.PRIMARY)` or `[Type.VARIANT](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.Type.ENUM_VALUES.VARIANT)` otherwise an INVALID_ARGUMENT error is thrown. Should not set it for other types. A maximum of 1000 values are allowed. Otherwise, an INVALID_ARGUMENT error is return.  
`inventory.gtin` |  `string` The Global Trade Item Number (GTIN) of the product.This field must be a UTF-8 encoded string with a length limit of 128 characters. Otherwise, an INVALID_ARGUMENT error is returned.This field must be a Unigram. Otherwise, an INVALID_ARGUMENT error is returned.Corresponding properties: Google Merchant Center property [gtin](https://support.google.com/merchants/answer/6324461). Schema.org property [Product.isbn](https://schema.org/isbn), [Product.gtin8](https://schema.org/gtin8), [Product.gtin12](https://schema.org/gtin12), [Product.gtin13](https://schema.org/gtin13), or [Product.gtin14](https://schema.org/gtin14).If the value is not a valid GTIN, an INVALID_ARGUMENT error is returned.  
`inventory.categories[]` |  `string` Optional. Product categories. This field is repeated for supporting one product belonging to several parallel categories. Strongly recommended using the full path for better search / recommendation quality.To represent the full path of category, use the '>' sign, with one space on each side, to separate different hierarchies. If '>' is part of the category name, replace it with other character(s).For example, if a shoes product belongs to both ["Shoes & Accessories" -> "Shoes"] and ["Sports & Fitness" -> "Athletic Clothing" -> "Shoes"], it could be represented as:
    
    
     "categories": [
       "Shoes & Accessories > Shoes",
       "Sports & Fitness > Athletic Clothing > Shoes"
     ]
    

Must be set for `[Type.PRIMARY](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.Type.ENUM_VALUES.PRIMARY)` `[Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product)` otherwise an INVALID_ARGUMENT error is returned.At most 250 values are allowed per `[Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product)` unless overridden through the Google Cloud console. Empty values are not allowed. Each value must be a UTF-8 encoded string with a length limit of 5,000 characters. Otherwise, an INVALID_ARGUMENT error is returned.Corresponding properties: Google Merchant Center property [google_product_category](https://support.google.com/merchants/answer/6324436). Schema.org property [Product.category](https://schema.org/category).  
`inventory.title` |  `string` Required. Product title.This field must be a UTF-8 encoded string with a length limit of 1,000 characters. Otherwise, an INVALID_ARGUMENT error is returned.Corresponding properties: Google Merchant Center property [title](https://support.google.com/merchants/answer/6324415). Schema.org property [Product.name](https://schema.org/name).  
`inventory.brands[]` |  `string` The brands of the product.A maximum of 30 brands are allowed unless overridden through the Google Cloud console. Each brand must be a UTF-8 encoded string with a length limit of 1,000 characters. Otherwise, an INVALID_ARGUMENT error is returned.Corresponding properties: Google Merchant Center property [brand](https://support.google.com/merchants/answer/6324351). Schema.org property [Product.brand](https://schema.org/brand).  
`inventory.description` |  `string` Product description.This field must be a UTF-8 encoded string with a length limit of 5,000 characters. Otherwise, an INVALID_ARGUMENT error is returned.Corresponding properties: Google Merchant Center property [description](https://support.google.com/merchants/answer/6324468). Schema.org property [Product.description](https://schema.org/description).  
`inventory.languageCode` |  `string` Language of the title/description and other string attributes. Use language tags defined by [BCP 47](https://www.rfc-editor.org/rfc/bcp/bcp47.txt).For product prediction, this field is ignored and the model automatically detects the text language. The `[Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product)` can include text in different languages, but duplicating `[Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product)`s to provide text in multiple languages can result in degraded model performance.For product search this field is in use. It defaults to "en-US" if unset.  
`inventory.attributes` |  `map (key: string, value: object)` Highly encouraged. Extra product attributes to be included. For example, for products, this could include the store name, vendor, style, color, etc. These are very strong signals for recommendation model, thus we highly recommend providing the attributes here.Features that can take on one of a limited number of possible values. Two types of features can be set are:Textual features. some examples would be the brand/maker of a product, or country of a customer. Numerical features. Some examples would be the height/weight of a product, or age of a customer.For example: `{ "vendor": {"text": ["vendor123", "vendor456"]}, "lengths_cm": {"numbers":[2.3, 15.4]}, "heights_cm": {"numbers":[8.1, 6.4]} }`.This field needs to pass all below criteria, otherwise an INVALID_ARGUMENT error is returned:

  * Max entries count: 200.
  * The key must be a UTF-8 encoded string with a length limit of 128 characters.
  * For indexable attribute, the key must match the pattern: `[a-zA-Z0-9][a-zA-Z0-9_]*`. For example, `key0LikeThis` or `KEY_1_LIKE_THIS`.
  * For text attributes, at most 400 values are allowed. Empty values are not allowed. Each value must be a non-empty UTF-8 encoded string with a length limit of 256 characters.
  * For number attributes, at most 400 values are allowed.

  
`inventory.attributes.text[]` |  `string` The textual values of this custom attribute. For example, `["yellow", "green"]` when the key is "color".Empty string is not allowed. Otherwise, an INVALID_ARGUMENT error is returned.Exactly one of `text` or `numbers` should be set. Otherwise, an INVALID_ARGUMENT error is returned.  
`inventory.attributes.numbers[]` |  `number` The numerical values of this custom attribute. For example, `[2.3, 15.4]` when the key is "lengths_cm".Exactly one of `text` or `numbers` should be set. Otherwise, an INVALID_ARGUMENT error is returned.  
`inventory.attributes.searchable  
**(deprecated)**` |  `boolean` This field is normally ignored unless `[AttributesConfig.attribute_config_level](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.attributesConfig#AttributesConfig.FIELDS.attribute_config_level)` of the `[Catalog](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs#Catalog)` is set to the deprecated 'PRODUCT_LEVEL_ATTRIBUTE_CONFIG' mode. For information about product-level attribute configuration, see [Configuration modes](https://cloud.google.com/gemini-enterprise-cx/ai-commerce-search/attribute-config#config-modes). If true, custom attribute values are searchable by text queries in `[SearchService.Search](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.placements/search#google.cloud.retail.v2alpha.SearchService.Search)`.This field is ignored in a `[UserEvent](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.userEvents#UserEvent)`.Only set if type `text` is set. Otherwise, a INVALID_ARGUMENT error is returned.  
`inventory.attributes.indexable  
**(deprecated)**` |  `boolean` This field is normally ignored unless `[AttributesConfig.attribute_config_level](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.attributesConfig#AttributesConfig.FIELDS.attribute_config_level)` of the `[Catalog](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs#Catalog)` is set to the deprecated 'PRODUCT_LEVEL_ATTRIBUTE_CONFIG' mode. For information about product-level attribute configuration, see [Configuration modes](https://cloud.google.com/gemini-enterprise-cx/ai-commerce-search/attribute-config#config-modes). If true, custom attribute values are indexed, so that they can be filtered, faceted or boosted in `[SearchService.Search](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.placements/search#google.cloud.retail.v2alpha.SearchService.Search)`.This field is ignored in a `[UserEvent](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.userEvents#UserEvent)`.See `[SearchRequest.filter](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.placements/search#body.request_body.FIELDS.filter)`, `[SearchRequest.facet_specs](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.placements/search#body.request_body.FIELDS.facet_specs)` and `[SearchRequest.boost_spec](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.placements/search#body.request_body.FIELDS.boost_spec)` for more details.  
`inventory.tags[]` |  `string` Custom tags associated with the product.At most 250 values are allowed per `[Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product)`. This value must be a UTF-8 encoded string with a length limit of 1,000 characters. Otherwise, an INVALID_ARGUMENT error is returned.This tag can be used for filtering recommendation results by passing the tag as part of the `[PredictRequest.filter](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.placements/predict#body.request_body.FIELDS.filter)`.Corresponding properties: Google Merchant Center property [custom_label_0–4](https://support.google.com/merchants/answer/6324473).  
`inventory.priceInfo` |  `object (`[PriceInfo](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.PriceInfo)`)` Product price and cost information.Corresponding properties: Google Merchant Center property [price](https://support.google.com/merchants/answer/6324371).  
`inventory.rating` |  `object (`[Rating](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.Rating)`)` The rating of this product.  
`inventory.availableTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` The timestamp when this `[Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product)` becomes available for `[SearchService.Search](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.placements/search#google.cloud.retail.v2alpha.SearchService.Search)`. Note that this is only applicable to `[Type.PRIMARY](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.Type.ENUM_VALUES.PRIMARY)` and `[Type.COLLECTION](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.Type.ENUM_VALUES.COLLECTION)`, and ignored for `[Type.VARIANT](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.Type.ENUM_VALUES.VARIANT)`.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`inventory.availability` |  `enum (`[Availability](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.Availability)`)` The online availability of the `[Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product)`. Default to `[Availability.IN_STOCK](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.Availability.ENUM_VALUES.IN_STOCK)`.For primary products with variants set the availability of the primary as `[Availability.OUT_OF_STOCK](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.Availability.ENUM_VALUES.OUT_OF_STOCK)` and set the true availability at the variant level. This way the primary product will be considered "in stock" as long as it has at least one variant in stock.For primary products with no variants set the true availability at the primary level.Corresponding properties: Google Merchant Center property [availability](https://support.google.com/merchants/answer/6324448). Schema.org property [Offer.availability](https://schema.org/availability).  
`inventory.availableQuantity` |  `integer` The available quantity of the item.  
`inventory.fulfillmentInfo[]` |  `object (`[FulfillmentInfo](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.FulfillmentInfo)`)` Fulfillment information, such as the store IDs for in-store pickup or region IDs for different shipping methods.All the elements must have distinct `[FulfillmentInfo.type](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.FulfillmentInfo.FIELDS.type)`. Otherwise, an INVALID_ARGUMENT error is returned.  
`inventory.uri` |  `string` Canonical URL directly linking to the product detail page.It is strongly recommended to provide a valid uri for the product, otherwise the service performance could be significantly degraded.This field must be a UTF-8 encoded string with a length limit of 5,000 characters. Otherwise, an INVALID_ARGUMENT error is returned.Corresponding properties: Google Merchant Center property [link](https://support.google.com/merchants/answer/6324416). Schema.org property [Offer.url](https://schema.org/url).  
`inventory.images[]` |  `object (`[Image](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.Image)`)` Product images for the product. We highly recommend putting the main image first.A maximum of 300 images are allowed.Corresponding properties: Google Merchant Center property [image_link](https://support.google.com/merchants/answer/6324350). Schema.org property [Product.image](https://schema.org/image).  
`inventory.audience` |  `object (`[Audience](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.Audience)`)` The target group associated with a given audience (e.g. male, veterans, car owners, musicians, etc.) of the product.  
`inventory.colorInfo` |  `object (`[ColorInfo](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.ColorInfo)`)` The color of the product.Corresponding properties: Google Merchant Center property [color](https://support.google.com/merchants/answer/6324487). Schema.org property [Product.color](https://schema.org/color).  
`inventory.sizes[]` |  `string` The size of the product. To represent different size systems or size types, consider using this format: [[[size_system:]size_type:]size_value].For example, in "US:MENS:M", "US" represents size system; "MENS" represents size type; "M" represents size value. In "GIRLS:27", size system is empty; "GIRLS" represents size type; "27" represents size value. In "32 inches", both size system and size type are empty, while size value is "32 inches".A maximum of 20 values are allowed per `[Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product)`. Each value must be a UTF-8 encoded string with a length limit of 128 characters. Otherwise, an INVALID_ARGUMENT error is returned.Corresponding properties: Google Merchant Center property [size](https://support.google.com/merchants/answer/6324492), [size_type](https://support.google.com/merchants/answer/6324497), and [size_system](https://support.google.com/merchants/answer/6324502). Schema.org property [Product.size](https://schema.org/size).  
`inventory.materials[]` |  `string` The material of the product. For example, "leather", "wooden".A maximum of 20 values are allowed. Each value must be a UTF-8 encoded string with a length limit of 200 characters. Otherwise, an INVALID_ARGUMENT error is returned.Corresponding properties: Google Merchant Center property [material](https://support.google.com/merchants/answer/6324410). Schema.org property [Product.material](https://schema.org/material).  
`inventory.patterns[]` |  `string` The pattern or graphic print of the product. For example, "striped", "polka dot", "paisley".A maximum of 20 values are allowed per `[Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product)`. Each value must be a UTF-8 encoded string with a length limit of 128 characters. Otherwise, an INVALID_ARGUMENT error is returned.Corresponding properties: Google Merchant Center property [pattern](https://support.google.com/merchants/answer/6324483). Schema.org property [Product.pattern](https://schema.org/pattern).  
`inventory.conditions[]` |  `string` The condition of the product. Strongly encouraged to use the standard values: "new", "refurbished", "used".A maximum of 1 value is allowed per `[Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product)`. Each value must be a UTF-8 encoded string with a length limit of 128 characters. Otherwise, an INVALID_ARGUMENT error is returned.Corresponding properties: Google Merchant Center property [condition](https://support.google.com/merchants/answer/6324469). Schema.org property [Offer.itemCondition](https://schema.org/itemCondition).  
`inventory.promotions[]` |  `object (`[Promotion](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.Promotion)`)` The promotions applied to the product. A maximum of 10 values are allowed per `[Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product)`. Only `[Promotion.promotion_id](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.Promotion.FIELDS.promotion_id)` will be used, other fields will be ignored if set.  
`inventory.publishTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` The timestamp when the product is published by the retailer for the first time, which indicates the freshness of the products. Note that this field is different from `[availableTime](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.FIELDS.available_time)`, given it purely describes product freshness regardless of when it is available on search and recommendation.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`inventory.retrievableFields  
**(deprecated)**` |  `string (`[FieldMask](https://protobuf.dev/reference/protobuf/google.protobuf/#field-mask)` format)` Indicates which fields in the `[Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product)`s are returned in `[SearchResponse](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/SearchResponse)`.Supported fields for all `[type](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.FIELDS.type)`s:

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
`inventory.variants[]` |  `object (`[Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product)`)` Output only. Product variants grouped together on primary product which share similar product attributes. It's automatically grouped by `[primaryProductId](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.FIELDS.primary_product_id)` for all the product variants. Only populated for `[Type.PRIMARY](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.Type.ENUM_VALUES.PRIMARY)` `[Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product)`s.Note: This field is OUTPUT_ONLY for `[ProductService.GetProduct](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products/get#google.cloud.retail.v2alpha.ProductService.GetProduct)`. Do not set this field in API requests.  
`inventory.localInventories[]` |  `object (`[LocalInventory](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.LocalInventory)`)` Output only. A list of local inventories specific to different places.This field can be managed by `[ProductService.AddLocalInventories](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products/addLocalInventories#google.cloud.retail.v2alpha.ProductService.AddLocalInventories)` and `[ProductService.RemoveLocalInventories](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products/removeLocalInventories#google.cloud.retail.v2alpha.ProductService.RemoveLocalInventories)` APIs if fine-grained, high-volume updates are necessary.  
`setMask` |  `string (`[FieldMask](https://protobuf.dev/reference/protobuf/google.protobuf/#field-mask)` format)` Indicates which inventory fields in the provided `[Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product)` to update.At least one field must be provided.If an unsupported or unknown field is provided, an INVALID_ARGUMENT error is returned and the entire update will be ignored.This is a comma-separated list of fully qualified names of fields. Example: `"user.displayName,photo"`.  
`setTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` The time when the request is issued, used to prevent out-of-order updates on inventory fields with the last update time recorded. If not provided, the internal system time will be used.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`allowMissing` |  `boolean` If set to true, and the `[Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product)` with name `[Product.name](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.FIELDS.name)` is not found, the inventory update will still be processed and retained for at most 1 day until the `[Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product)` is created. If set to false, a NOT_FOUND error is returned if the `[Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product)` is not found.  
Union field `expiration`.`expiration` can be only one of the following:  
`inventory.expireTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Note that this field is applied in the following ways:

  * If the `[Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product)` is already expired when it is uploaded, this product is not indexed for search.
  * If the `[Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product)` is not expired when it is uploaded, only the `[Type.PRIMARY](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.Type.ENUM_VALUES.PRIMARY)`'s and `[Type.COLLECTION](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.Type.ENUM_VALUES.COLLECTION)`'s expireTime is respected, and `[Type.VARIANT](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.Type.ENUM_VALUES.VARIANT)`'s expireTime is not used.

In general, we suggest the users to delete the stale products explicitly, instead of using this field to determine staleness.`[expireTime](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.FIELDS.expire_time)` must be later than `[availableTime](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.FIELDS.available_time)` and `[publishTime](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.FIELDS.publish_time)`, otherwise an INVALID_ARGUMENT error is thrown.Corresponding properties: Google Merchant Center property [expiration_date](https://support.google.com/merchants/answer/6324499).Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`inventory.ttl` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` Input only. The TTL (time to live) of the product. Note that this is only applicable to `[Type.PRIMARY](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.Type.ENUM_VALUES.PRIMARY)` and `[Type.COLLECTION](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.Type.ENUM_VALUES.COLLECTION)`, and ignored for `[Type.VARIANT](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.Type.ENUM_VALUES.VARIANT)`. In general, we suggest the users to delete the stale products explicitly, instead of using this field to determine staleness.If it is set, it must be a non-negative value, and `[expireTime](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.FIELDS.expire_time)` is set as current timestamp plus `[ttl](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.FIELDS.ttl)`. The derived `[expireTime](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.FIELDS.expire_time)` is returned in the output and `[ttl](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.FIELDS.ttl)` is left blank when retrieving the `[Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product)`.If it is set, the product is not available for `[SearchService.Search](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.placements/search#google.cloud.retail.v2alpha.SearchService.Search)` after current timestamp plus `[ttl](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.FIELDS.ttl)`. However, the product can still be retrieved by `[ProductService.GetProduct](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products/get#google.cloud.retail.v2alpha.ProductService.GetProduct)` and `[ProductService.ListProducts](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products/list#google.cloud.retail.v2alpha.ProductService.ListProducts)`.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
  
### Response body

If successful, the response body contains an instance of `[Operation](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/Shared.Types/ListOperationsResponse#Operation)`.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `retail.products.update`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-08 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-08 UTC."],[],[]] 
