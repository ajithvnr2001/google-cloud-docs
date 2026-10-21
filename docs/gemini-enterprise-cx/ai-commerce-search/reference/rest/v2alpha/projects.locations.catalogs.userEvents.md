---
url: https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.userEvents
title: REST Resource: projects.locations.catalogs.userEvents \u00a0|\u00a0 AI Commerce Search in Gemini Enterprise for Customer Experience \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T16:54:12.065056+00:00
---

# REST Resource: projects.locations.catalogs.userEvents  |  AI Commerce Search in Gemini Enterprise for Customer Experience  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.userEvents

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ AI Commerce Search ](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search)



Send feedback 

#  REST Resource: projects.locations.catalogs.userEvents Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: UserEvent
    * JSON representation
  * ProductDetail
    * JSON representation
  * CompletionDetail
    * JSON representation
  * PurchaseTransaction
    * JSON representation
  * UserInfo
    * JSON representation
  * PanelInfo
    * JSON representation
  * Methods



## Resource: UserEvent

UserEvent captures all metadata information AI Commerce Search API needs to know about how end users interact with customers' website.

JSON representation  
---  
      
    
    {
      "eventType": string,
      "visitorId": string,
      "sessionId": string,
      "eventTime": string,
      "experimentIds": [
        string
      ],
      "attributionToken": string,
      "productDetails": [
        {
          object ([ProductDetail](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.userEvents#ProductDetail))
        }
      ],
      "completionDetail": {
        object ([CompletionDetail](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.userEvents#CompletionDetail))
      },
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
      "cartId": string,
      "purchaseTransaction": {
        object ([PurchaseTransaction](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.userEvents#PurchaseTransaction))
      },
      "searchQuery": string,
      "filter": string,
      "orderBy": string,
      "offset": integer,
      "pageCategories": [
        string
      ],
      "userInfo": {
        object ([UserInfo](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.userEvents#UserInfo))
      },
      "uri": string,
      "referrerUri": string,
      "pageViewId": string,
      "entity": string,
      "panels": [
        {
          object ([PanelInfo](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.userEvents#PanelInfo))
        }
      ]
    }  
  
Fields  
---  
`eventType` |  `string` Required. User event type. Allowed values are:

  * `add-to-cart`: Products being added to cart.
  * `remove-from-cart`: Products being removed from cart.
  * `category-page-view`: Special pages such as sale or promotion pages viewed.
  * `detail-page-view`: Products detail page viewed.
  * `home-page-view`: Homepage viewed.
  * `purchase-complete`: User finishing a purchase.
  * `search`: Product search.
  * `shopping-cart-page-view`: User viewing a shopping cart.

  
`visitorId` |  `string` Required. A unique identifier for tracking visitors.For example, this could be implemented with an HTTP cookie, which should be able to uniquely identify a visitor on a single device. This unique identifier should not change if the visitor log in/out of the website.Don't set the field to the same fixed ID for different users. This mixes the event history of those users together, which results in degraded model quality.The field must be a UTF-8 encoded string with a length limit of 128 characters. Otherwise, an INVALID_ARGUMENT error is returned.The field should not contain PII or user-data. We recommend to use Google Analytics [Client ID](https://developers.google.com/analytics/devguides/collection/analyticsjs/field-reference#clientId) for this field.  
`sessionId` |  `string` A unique identifier for tracking a visitor session with a length limit of 128 bytes. A session is an aggregation of an end user behavior in a time span.A general guideline to populate the sessionId: 1. If user has no activity for 30 min, a new sessionId should be assigned. 2. The sessionId should be unique across users, suggest use uuid or add visitorId as prefix.  
`eventTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Only required for `[UserEventService.ImportUserEvents](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.userEvents/import#google.cloud.retail.v2alpha.UserEventService.ImportUserEvents)` method. Timestamp of when the user event happened.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`experimentIds[]` |  `string` A list of identifiers for the independent experiment groups this user event belongs to. This is used to distinguish between user events associated with different experiment setups (e.g. using AI Commerce Search API, using different recommendation models).  
`attributionToken` |  `string` Highly recommended for user events that are the result of `[PredictionService.Predict](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.placements/predict#google.cloud.retail.v2alpha.PredictionService.Predict)`. This field enables accurate attribution of recommendation model performance.The value must be a valid `[PredictResponse.attribution_token](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/PredictResponse#FIELDS.attribution_token)` for user events that are the result of `[PredictionService.Predict](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.placements/predict#google.cloud.retail.v2alpha.PredictionService.Predict)`. The value must be a valid `[SearchResponse.attribution_token](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/SearchResponse#FIELDS.attribution_token)` for user events that are the result of `[SearchService.Search](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.placements/search#google.cloud.retail.v2alpha.SearchService.Search)`.This token enables us to accurately attribute page view or purchase back to the event and the particular predict response containing this clicked/purchased product. If user clicks on product K in the recommendation results, pass `[PredictResponse.attribution_token](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/PredictResponse#FIELDS.attribution_token)` as a URL parameter to product K's page. When recording events on product K's page, log the `[PredictResponse.attribution_token](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/PredictResponse#FIELDS.attribution_token)` to this field.  
`productDetails[]` |  `object (`[ProductDetail](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.userEvents#ProductDetail)`)` The main product details related to the event.This field is optional except for the following event types:

  * `add-to-cart`
  * `detail-page-view`
  * `purchase-complete`

In a `search` event, this field represents the products returned to the end user on the current page (the end user may have not finished browsing the whole page yet). When a new page is returned to the end user, after pagination/filtering/ordering even for the same query, a new `search` event with different `[productDetails](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.userEvents#UserEvent.FIELDS.product_details)` is desired. The end user may have not finished browsing the whole page yet.  
`completionDetail` |  `object (`[CompletionDetail](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.userEvents#CompletionDetail)`)` The main auto-completion details related to the event.This field should be set for `search` event when autocomplete function is enabled and the user clicks a suggestion for search.  
`attributes` |  `map (key: string, value: object)` Extra user event features to include in the recommendation model.If you provide custom attributes for ingested user events, also include them in the user events that you associate with prediction requests. Custom attribute formatting must be consistent between imported events and events provided with prediction requests. This lets the AI Commerce Search API use those custom attributes when training models and serving predictions, which helps improve recommendation quality.This field needs to pass all below criteria, otherwise an INVALID_ARGUMENT error is returned:

  * The key must be a UTF-8 encoded string with a length limit of 5,000 characters.
  * For text attributes, at most 400 values are allowed. Empty values are not allowed. Each value must be a UTF-8 encoded string with a length limit of 256 characters.
  * For number attributes, at most 400 values are allowed.

For product recommendations, an example of extra user information is traffic_channel, which is how a user arrives at the site. Users can arrive at the site by coming to the site directly, coming through Google search, or in other ways.  
`attributes.text[]` |  `string` The textual values of this custom attribute. For example, `["yellow", "green"]` when the key is "color".Empty string is not allowed. Otherwise, an INVALID_ARGUMENT error is returned.Exactly one of `text` or `numbers` should be set. Otherwise, an INVALID_ARGUMENT error is returned.  
`attributes.numbers[]` |  `number` The numerical values of this custom attribute. For example, `[2.3, 15.4]` when the key is "lengths_cm".Exactly one of `text` or `numbers` should be set. Otherwise, an INVALID_ARGUMENT error is returned.  
`attributes.searchable  
**(deprecated)**` |  `boolean` This field is normally ignored unless `[AttributesConfig.attribute_config_level](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.attributesConfig#AttributesConfig.FIELDS.attribute_config_level)` of the `[Catalog](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs#Catalog)` is set to the deprecated 'PRODUCT_LEVEL_ATTRIBUTE_CONFIG' mode. For information about product-level attribute configuration, see [Configuration modes](https://cloud.google.com/gemini-enterprise-cx/ai-commerce-search/attribute-config#config-modes). If true, custom attribute values are searchable by text queries in `[SearchService.Search](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.placements/search#google.cloud.retail.v2alpha.SearchService.Search)`.This field is ignored in a `[UserEvent](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.userEvents#UserEvent)`.Only set if type `text` is set. Otherwise, a INVALID_ARGUMENT error is returned.  
`attributes.indexable  
**(deprecated)**` |  `boolean` This field is normally ignored unless `[AttributesConfig.attribute_config_level](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.attributesConfig#AttributesConfig.FIELDS.attribute_config_level)` of the `[Catalog](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs#Catalog)` is set to the deprecated 'PRODUCT_LEVEL_ATTRIBUTE_CONFIG' mode. For information about product-level attribute configuration, see [Configuration modes](https://cloud.google.com/gemini-enterprise-cx/ai-commerce-search/attribute-config#config-modes). If true, custom attribute values are indexed, so that they can be filtered, faceted or boosted in `[SearchService.Search](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.placements/search#google.cloud.retail.v2alpha.SearchService.Search)`.This field is ignored in a `[UserEvent](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.userEvents#UserEvent)`.See `[SearchRequest.filter](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.placements/search#body.request_body.FIELDS.filter)`, `[SearchRequest.facet_specs](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.placements/search#body.request_body.FIELDS.facet_specs)` and `[SearchRequest.boost_spec](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.placements/search#body.request_body.FIELDS.boost_spec)` for more details.  
`cartId` |  `string` The ID or name of the associated shopping cart. This ID is used to associate multiple items added or present in the cart before purchase.This can only be set for `add-to-cart`, `purchase-complete`, or `shopping-cart-page-view` events.  
`purchaseTransaction` |  `object (`[PurchaseTransaction](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.userEvents#PurchaseTransaction)`)` A transaction represents the entire purchase transaction.Required for `purchase-complete` events. Other event types should not set this field. Otherwise, an INVALID_ARGUMENT error is returned.  
`searchQuery` |  `string` The user's search query.See `[SearchRequest.query](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.placements/search#body.request_body.FIELDS.query)` for definition.The value must be a UTF-8 encoded string with a length limit of 5,000 characters. Otherwise, an INVALID_ARGUMENT error is returned.At least one of `[searchQuery](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.userEvents#UserEvent.FIELDS.search_query)` or `[pageCategories](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.userEvents#UserEvent.FIELDS.page_categories)` is required for `search` events. Other event types should not set this field. Otherwise, an INVALID_ARGUMENT error is returned.  
`filter` |  `string` The filter syntax consists of an expression language for constructing a predicate from one or more fields of the products being filtered.See `[SearchRequest.filter](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.placements/search#body.request_body.FIELDS.filter)` for definition and syntax.The value must be a UTF-8 encoded string with a length limit of 1,000 characters. Otherwise, an INVALID_ARGUMENT error is returned.  
`orderBy` |  `string` The order in which products are returned.See `[SearchRequest.order_by](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.placements/search#body.request_body.FIELDS.order_by)` for definition and syntax.The value must be a UTF-8 encoded string with a length limit of 1,000 characters. Otherwise, an INVALID_ARGUMENT error is returned.This can only be set for `search` events. Other event types should not set this field. Otherwise, an INVALID_ARGUMENT error is returned.  
`offset` |  `integer` An integer that specifies the current offset for pagination (the 0-indexed starting location, amongst the products deemed by the API as relevant).See `[SearchRequest.offset](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.placements/search#body.request_body.FIELDS.offset)` for definition.If this field is negative, an INVALID_ARGUMENT is returned.This can only be set for `search` events. Other event types should not set this field. Otherwise, an INVALID_ARGUMENT error is returned.  
`pageCategories[]` |  `string` Optional. The categories associated with a category page.To represent the full path of category, use the '>' sign, with one space on each side, to separate different hierarchies. If '>' is part of the category name, replace it with other character(s).Category pages include special pages such as sales or promotions. For instance, a special sale page may have the category hierarchy: "pageCategories" : ["Sales > 2017 Black Friday Deals"].Required for `category-page-view` events. At least one of `[searchQuery](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.userEvents#UserEvent.FIELDS.search_query)` or `[pageCategories](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.userEvents#UserEvent.FIELDS.page_categories)` is required for `search` events. Other event types should not set this field. Otherwise, an INVALID_ARGUMENT error is returned.  
`userInfo` |  `object (`[UserInfo](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.userEvents#UserInfo)`)` User information.  
`uri` |  `string` Complete URL (window.location.href) of the user's current page.When using the client side event reporting with JavaScript pixel and Google Tag Manager, this value is filled in automatically. Maximum length 5,000 characters.  
`referrerUri` |  `string` The referrer URL of the current page.When using the client side event reporting with JavaScript pixel and Google Tag Manager, this value is filled in automatically.  
`pageViewId` |  `string` A unique ID of a web page view.This should be kept the same for all user events triggered from the same pageview. For example, an item detail page view could trigger multiple events as the user is browsing the page. The `pageViewId` property should be kept the same for all these events so that they can be grouped together properly.When using the client side event reporting with JavaScript pixel and Google Tag Manager, this value is filled in automatically.  
`entity` |  `string` The entity for customers that may run multiple different entities, domains, sites or regions, for example, `Google US`, `Google Ads`, `Waymo`, `google.com`, `youtube.com`, etc. We recommend that you set this field to get better per-entity search, completion, and prediction results.  
`panels[]` |  `object (`[PanelInfo](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.userEvents#PanelInfo)`)` Optional. List of panels associated with this event. Used for panel-level impression data.  
  
## ProductDetail

Detailed product information associated with a user event.

JSON representation  
---  
      
    
    {
      "product": {
        object ([Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product))
      },
      "quantity": integer
    }  
  
Fields  
---  
`product` |  `object (`[Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product)`)` Required. `[Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product)` information.Required field(s):

  * `[Product.id](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.FIELDS.id)`

Optional override field(s):

  * `[Product.price_info](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.branches.products#Product.FIELDS.price_info)`

If any supported optional fields are provided, we will treat them as a full override when looking up product information from the catalog. Thus, it is important to ensure that the overriding fields are accurate and complete.All other product fields are ignored and instead populated via catalog lookup after event ingestion.  
`quantity` |  `integer` Quantity of the product associated with the user event.For example, this field will be 2 if two products are added to the shopping cart for `purchase-complete` event. Required for `add-to-cart` and `purchase-complete` event types.  
  
## CompletionDetail

Detailed completion information including completion attribution token and clicked completion info.

JSON representation  
---  
      
    
    {
      "completionAttributionToken": string,
      "selectedSuggestion": string,
      "selectedPosition": integer
    }  
  
Fields  
---  
`completionAttributionToken` |  `string` Completion attribution token in `[CompleteQueryResponse.attribution_token](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs/completeQuery#body.CompleteQueryResponse.FIELDS.attribution_token)`.  
`selectedSuggestion` |  `string` End user selected `[CompleteQueryResponse.CompletionResult.suggestion](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs/completeQuery#CompletionResult.FIELDS.suggestion)`.  
`selectedPosition` |  `integer` End user selected `[CompleteQueryResponse.CompletionResult.suggestion](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs/completeQuery#CompletionResult.FIELDS.suggestion)` position, starting from 0.  
  
## PurchaseTransaction

A transaction represents the entire purchase transaction.

JSON representation  
---  
      
    
    {
      "id": string,
      "revenue": number,
      "tax": number,
      "cost": number,
      "currencyCode": string
    }  
  
Fields  
---  
`id` |  `string` The transaction ID with a length limit of 128 characters.  
`revenue` |  `number` Required. Total non-zero revenue or grand total associated with the transaction. This value include shipping, tax, or other adjustments to total revenue that you want to include as part of your revenue calculations.  
`tax` |  `number` All the taxes associated with the transaction.  
`cost` |  `number` All the costs associated with the products. These can be manufacturing costs, shipping expenses not borne by the end user, or any other costs, such that:

  * Profit = `[revenue](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.userEvents#PurchaseTransaction.FIELDS.revenue)` \- `[tax](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.userEvents#PurchaseTransaction.FIELDS.tax)` \- `[cost](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.userEvents#PurchaseTransaction.FIELDS.cost)`

  
`currencyCode` |  `string` Required. Currency code. Use three-character ISO-4217 code.  
  
## UserInfo

Information of an end user.

JSON representation  
---  
      
    
    {
      "userId": string,
      "ipAddress": string,
      "userAgent": string,
      "directUserRequest": boolean
    }  
  
Fields  
---  
`userId` |  `string` Highly recommended for logged-in users. Unique identifier for logged-in user, such as a user name. Don't set for anonymous users.Always use a hashed value for this ID.Don't set the field to the same fixed ID for different users. This mixes the event history of those users together, which results in degraded model quality.The field must be a UTF-8 encoded string with a length limit of 128 characters. Otherwise, an INVALID_ARGUMENT error is returned.  
`ipAddress` |  `string` The end user's IP address. This field is used to extract location information for personalization.This field must be either an IPv4 address (e.g. "104.133.9.80") or an IPv6 address (e.g. "2001:0db8:85a3:0000:0000:8a2e:0370:7334"). Otherwise, an INVALID_ARGUMENT error is returned.This should not be set when:

  * setting `[SearchRequest.user_info](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.placements/search#body.request_body.FIELDS.user_info)`.
  * using the JavaScript tag in `[UserEventService.CollectUserEvent](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.userEvents/collect#google.cloud.retail.v2alpha.UserEventService.CollectUserEvent)` or if `[directUserRequest](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.userEvents#UserInfo.FIELDS.direct_user_request)` is set.

  
`userAgent` |  `string` User agent as included in the HTTP header. The field must be a UTF-8 encoded string with a length limit of 1,000 characters. Otherwise, an INVALID_ARGUMENT error is returned.This should not be set when using the client side event reporting with GTM or JavaScript tag in `[UserEventService.CollectUserEvent](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.userEvents/collect#google.cloud.retail.v2alpha.UserEventService.CollectUserEvent)` or if `[directUserRequest](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.userEvents#UserInfo.FIELDS.direct_user_request)` is set.  
`directUserRequest` |  `boolean` True if the request is made directly from the end user, in which case the `[ipAddress](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.userEvents#UserInfo.FIELDS.ip_address)` and `[userAgent](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.userEvents#UserInfo.FIELDS.user_agent)` can be populated from the HTTP request. This flag should be set only if the API request is made directly from the end user such as a mobile app (and not if a gateway or a server is processing and pushing the user events).This should not be set when using the JavaScript tag in `[UserEventService.CollectUserEvent](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.userEvents/collect#google.cloud.retail.v2alpha.UserEventService.CollectUserEvent)`.  
  
## PanelInfo

Detailed panel information associated with a user event.

JSON representation  
---  
      
    
    {
      "panelId": string,
      "displayName": string,
      "productDetails": [
        {
          object ([ProductDetail](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.userEvents#ProductDetail))
        }
      ],
      "totalPanels": integer,
      "panelPosition": integer,
      "attributionToken": string
    }  
  
Fields  
---  
`panelId` |  `string` Required. The panel ID.  
`displayName` |  `string` Optional. The display name of the panel.  
`productDetails[]` |  `object (`[ProductDetail](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.userEvents#ProductDetail)`)` Optional. The product details associated with the panel.  
`totalPanels` |  `integer` Optional. The total number of panels, including this one, shown to the user. Must be set if `[panelPosition](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.userEvents#PanelInfo.FIELDS.panel_position)` is set.  
`panelPosition` |  `integer` Optional. The ordered position of the panel, if shown to the user with other panels. If set, then `[totalPanels](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.userEvents#PanelInfo.FIELDS.total_panels)` must also be set.  
`attributionToken` |  `string` Optional. The attribution token of the panel.  
  
## Methods  
  
---  
  
### `[collect](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.userEvents/collect)`

|  Writes a single user event from the browser.  
  
### `[export](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.userEvents/export)`

|  Exports user events.  
  
### `[import](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.userEvents/import)`

|  Bulk import of User events.  
  
### `[purge](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.userEvents/purge)`

|  Deletes permanently all user events specified by the filter provided.  
  
### `[rejoin](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.userEvents/rejoin)`

|  Starts a user-event rejoin operation with latest product catalog.  
  
### `[write](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.userEvents/write)`

|  Writes a single user event.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-08 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-08 UTC."],[],[]] 
