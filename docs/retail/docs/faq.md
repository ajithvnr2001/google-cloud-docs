---
url: https://docs.cloud.google.com/retail/docs/faq/
title: Frequently asked questions \u00a0|\u00a0 AI Commerce Search in Gemini Enterprise for Customer Experience \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T11:26:08.393410+00:00
---

# Frequently asked questions  |  AI Commerce Search in Gemini Enterprise for Customer Experience  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/retail/docs/faq/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ AI Commerce Search ](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search)



Send feedback 

#  Frequently asked questions Stay organized with collections  Save and categorize content based on your preferences. 

Have other challenges or don't see your issue outlined here? [Report a bug or request a feature](https://issuetracker.google.com/issues?q=componentid:911831) and join the [cloud-recommendations-users](https://groups.google.com/forum/#!forum/cloud-recommendations-users) Google group or [Stack Overflow](http://stackoverflow.com/questions/tagged/google-cloud-recommendations) discussions.

## General

These are general frequently asked questions.

### Do you have client libraries for AI Commerce Search or more sample code?

Yes. You can see the [client libraries guide](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/libraries) for setup and reference information for each library.

The [Google API Discovery Service](https://developers.google.com/discovery/) can also be used instead of raw REST calls.

### Are all the recommendation models personalized?

The Recommended for You, Others You May Like, and Buy it Again models make personalized recommendations when provided with user history. The Frequently Bought Together and Similar Items models are not personalized.

See [About recommendation models](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/models).

### Will I receive personalized recommendations immediately, or will I need to wait for these to improve over time?

Recommendations improve as you collect more user history. The Recommended for You model shows popular products and the Others You May Like model shows similar products based mostly on other's views. Both of these models start taking user behavior into account immediately, so it's important to send real-time events. See [About recommendation models](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/models).

User events need to be sent in real-time, or very close to real-time, for personalization to be effective. If user events are only submitted daily, or in batches throughout the day, the personalized models may not perform as well as they could if real-time events were sent.

### Are you using Google user demographic data in your models?

The models only use the catalog and user event data that you provide. If you want to include demographic data, you can include other textual or numerical information that might be useful as [custom attributes](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/user-events#custom-attributes). This data will begin to be used by the model after it has been retuned.

Don't include personally identifiable information (PII) such as email addresses or usernames. We suggest you anonymize demographic data, such as by hashing the values or using group IDs.

### Can I make recommendations based on the event history of a group of users rather than a single user's history?

Recommendations are based on a single visitor ID or user ID. You would need to make individual requests and then combine the results to base recommendations on a group's history. If the users have common metadata attributes, you could use group IDs as user IDs to provide group-level recommendations.

### I noticed that you can submit image URLs for products. Do the models take into consideration the product images?

Yes, product images can be submitted as part of your product catalog data. AI Commerce Search uses product URLs and the identifiers behind them (URIs) to [enrich product descriptions](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/catalog#product-urls).

The `Product` object contains an images field, which is a list of image objects. Each image object can include a URI, height, and width. Up to 300 images are allowed per product. While optional, providing product images is highly recommended. ([Prediction preview](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/predict#preview)) also uses image URLs to display the images when you preview a model's prediction results in the AI Commerce Search in Gemini Enterprise for Customer Experience console.

### My company isn't a retail ecommerce website. Can I still use recommendations for predicting x,y,z?

We've had customers use recommendations for content recommendations, video streaming and gaming, and other use cases. However, our content and experience is designed with the retail ecommerce use case in mind and may not be suited for other use cases yet.

### Can I place recommendations on any page of my site?

Yes, but the models are each designed for specific use cases and may work best on certain pages. See [About recommendation models](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/models).

Frequently Bought Together and Others You May Like require item IDs, so they should be used for recommendations using, for example, a product ID or items in a cart. Frequently Bought Together typically works best on add-to-cart or checkout pages, while Others You May Like and Similar Items work best on product detail pages. Recommended for You could be placed on any page, since it only requires a visitor ID as input, but it is designed as a home page serving config. Buy it Again is designed to be placed on any page.

### Can I use recommendations for recommendations in email newsletters?

Yes. This can be done by making a call to the API with a visitor ID or user ID, then incorporating the results into an email template. If you want the items to be loaded dynamically at email-read time, you would need to use an intermediary endpoint, such as a [Google Cloud Function](https://docs.cloud.google.com/functions/docs/concepts/overview), to send the predict request. The API only provides a list of ordered product IDs and metadata, so you will also need to write your own code to render the image results.

### Can I use AI Commerce Search for other non-web use cases (mobile apps, kiosks)?

Yes. You can set up an endpoint (for example, [Google Google Cloud Function](https://docs.cloud.google.com/functions/docs/concepts/overview)) to get results for the app. You also need a similar mechanism to send real-time events.

### I don't have 3+ months of event data. Can I still use AI Commerce Search? Can I add more data at a later point?

The Similar Items model does not use user event data or model tuning. If you don't have any event data, you can still create and train a Similar Items model as long as you have catalog data.

If you can record sufficient traffic for real-time events, recent data can be used for training other models. If you have additional data available at a later date, you can upload it after the initial model training. The newly backfilled data gets incorporated into the models during daily retraining. However, if the data is significantly different than the events that were used for the initial training, the models may need to be [retuned](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/manage-models#tune).

Most models work best with at least three months of product page views, home page views, and add-to-cart events for all models, and ideally one to two years of purchase history for the Frequently Bought Together model.

One to two weeks of detail page views can be enough to start training Others You May Like and Recommended for You models, while Frequently Bought Together and Buy it Again usually require more because there are typically fewer purchases per day than there are page views. Model quality can be significantly improved with more data; the minimum amount might not produce optimal results. A year's worth of purchases, for example, allows the models to better take advantage of seasonality and trends.

### Can I recommend categories along with products?

Recommendations returns product recommendations only, but you can get the categories for each product returned as part of the results.

### Do you have integrations for uploading data from SQL databases or other systems, such as BigQuery?

Yes. For events, there is [sample code](https://github.com/flowstack/recommendations-ai-utils/tree/master/bq-export) that reads from BigQuery. See a [Google Analytics sample dataset for BigQuery](https://support.google.com/analytics/answer/7586738).

### Does AI Commerce Search use cookies?

No, it doesn't use cookies. However, all events sent to the AI Commerce Search must have a visitor ID specified, which is often a session identifier from a cookie.

### Do I need a dedicated Google Cloud project?

You can create a new, dedicated project, or enable AI Commerce Search in an existing project.

### Why aren't my credentials working when using Cloud Shell?

Check that you've completed the [authentication setup steps](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/setting-up#authentication) for AI Commerce Search. You should be using a service account that you've made available in your environment. Otherwise, you might get an error like this: **Your application has authenticated using end user credentials from the Google Cloud SDK or Google Cloud Shell which are not supported.**

For more about service accounts, see the [Authentication section](https://docs.cloud.google.com/docs/authentication) of the Google Cloud documentation.

### How can I compare AI Commerce Search to similar solutions?

You can conduct [A/B tests](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/a-b-testing) to compare results from AI Commerce Search to those of other products.

### I think feature x,y,z would be great. Can you add this?

We'd love to hear from you. Feature requests can be submitted through your account team, Google Support, or the [issue-tracker](https://issuetracker.google.com/issues/new?component=911831).

### Can I still use the old API for recommendations?

Recommendations has migrated from the Recommendations Engine API to AI Commerce Search. If you were using the Recommendations Engine API while it was in beta, we recommend migrating your recommendations to AI Commerce Search (service endpoint `https://retail.googleapis.com`), which is GA.

The previous API (service endpoint `https://recommendationengine.googleapis.com`) and its [documentation](https://docs.cloud.google.com/recommendations-ai/docs/apis) remain available, but they are no longer updated.

## Catalogs and products

These are frequently asked questions about catalogs and products.

### How does recommendations handle cold starts for new products?

For products that don't have any purchase history, we make recommendations based on similar products. In these cases, it is especially important to have good product titles, categories, and descriptions defined in the catalog.

For cold-start users (visitors with no history) the models start with the most popular general products, and become more personalized in real time as more user events are received.

See [About catalogs and products](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/catalog) and the [product reference page](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.branches.products).

### Can I use my Merchant Center catalog for recommendations?

Yes, you can export a Merchant Center catalog to BigQuery using the Merchant Center Data Transfer Service. Then we can read the catalog directly from BigQuery. See [Import catalog data from Merchant Center](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/upload-catalog#mc).

### How else can I import my catalog?

  * [Merchant Center](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/upload-catalog#mc): Import with Merchant Center. If you use search, you can use the console to link Merchant Center so that its catalog syncs automatically.
  * [BigQuery](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/upload-catalog#bq): Import directly from a table or view.
  * [Cloud Storage](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/upload-catalog#json): Import using text files with one JSON catalog item per line.
  * [Inline import](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/upload-catalog#inline): Import with an API call, using text files with one JSON catalog item per line.
  * [Create product items](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.branches.products/create): Use the `Products` create method.



### How can I keep my catalog updated? How often does the catalog need to be updated?

See [Keep your catalog up to date](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/upload-catalog#current).

We recommend updating your catalog daily. You can do a full update from Cloud Storage or BigQuery, or an incremental update (i.e., new and changed items only).

If possible, update price and availability in real time. This affects how quickly new items can be made searchable with search.

If you have a way to be notified of catalog changes (such as using Pub/Sub, message queue, events, etc.) then you can update the catalog in real-time using the [import](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/upload-catalog#inline) or [create](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.branches.products/create) API methods.

For example, [Cloud Scheduler](https://cloud.google.com/scheduler) can be used to make a daily BigQuery import call.

### Are there minimum and maximum catalog sizes?

There is no minimum, but very small catalog sizes (< 100 items) may not see much benefit from recommendations due to there being very few different products to recommend.

The catalog maximum is 40 million items.

See the documentation for default [quotas and limits](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/quotas) and for how to request a change to your quota.

### My company operates websites in multiple countries. Should I use one catalog for all of my data?

It is usually best to have just one catalog with all items. Events must be submitted all using a single currency. There is no way to have multiple catalogs within the same project, but, if you use [entities](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/entities), you can specify search, recommendations, and autocomplete behavior for a particular country.

If the catalogs are considerably different between websites, we recommend having a separate project for each website. Also, if the countries have different languages, we recommend having separate projects, one for each language.

If there are similar websites with low traffic compared to the main website, it may be best to use a single catalog if there are not enough events to produce high quality models for all individual websites.

To use a single catalog, the catalog item IDs should be consistent, i.e., the same product should have a single item ID on all websites so that there is no duplication of products within the catalog.

For recommendations only, an alternative to using entities is to filter to a specific website using [filters](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/predict#filters). However, filters may take up to 8 hours to update, so if there are country-specific availability (out of stock) requirements, they normally need to be handled by a business rule that filters out the results after the predict response. This applies to v1 `filter_tag` filtering and v2 attribute-based filtering.

### Does AI Commerce Search support multiple currencies per catalog?

No, only one one currency type per catalog is supported. Events must be uploaded using a single currency.

If you plan to use the [AI Commerce Search in Gemini Enterprise for Customer Experience](https://console.cloud.google.com/ai/retail/catalogs/default_catalog/analytics/) console to get your revenue metrics, make sure your events all use a single currency or convert them all to the same currency before uploading them.

### I have multiple websites with a shared catalog or similar items. Can recommendations provide cross-site recommendations?

We typically recommend using a single catalog like this only if there is significant overlap between the sites; they should share many or all of the same products. Then, as with multi-region sites, you can use [entities](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/entities) or [filter tags](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/predict#filters) to return only site-specific items for a particular predict call.

If the sites don't share many, or any, catalog items, then multiple catalogs should be used. Using multiple catalogs requires a separate Google Cloud project for each catalog.

### Does including more metadata improve the model? Does the model consider fields x,y,z?

See [Required catalog item information](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/catalog#required-fields) for required fields.

Other metadata fields are optional (for example, images and itemAttributes). They may be used for prediction preview, results analysis, training, and tuning. We recommend including useful attributes such as color, size, material, etc. These fields can be returned as part of [predict](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.placements/predict#request-body) results by specifying `returnProduct:true`, so they can be useful for rendering results. Images and item attributes are used for [prediction preview](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/predict#preview) in the AI Commerce Search in Gemini Enterprise for Customer Experience console.

### Which attributes of a catalog item are used as inputs of model training?

A combination of both user behavior and product attributes is used. The primary fields used are ID, title, category hierarchy, price, and URL. You can include other custom key-value attributes that might be useful in [`Product.attributes[]`](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.userEvents#UserEvent.FIELDS.attributes).

Image URLs are more of a convenience feature; you can return this metadata as part of the [prediction](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.placements/predict#request-body) results by specifying `returnProduct:true`, which can save an extra call to retrieve this information. Having image URLs also allows [prediction preview](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/predict#preview) to display the images when you preview a model's prediction results in the AI Commerce Search in Gemini Enterprise for Customer Experience console.

### What languages are supported for my products?

  * **The recommendations feature** : Supports most languages. The model automatically detects the text language. For a list of all languages that can be automatically detected, see the Compact Language Detector [GitHub README](https://github.com/google/cld3#supported-languages).
  * **The search feature** : Supports [these world languages](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/supported-languages). You set the language when you upload the catalog. The catalog should be in one language only and the queries should be sent in the same language. Having multiple languages in the catalog degrades model performance.



> Note: If you already have a mixed language catalog for search, you can improve results by adding synonyms. For information about synonyms, see [OnewaySynonymsAction](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2#onewaysynonymsaction) and [TwowaySynonymsAction](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2#twowaysynonymsaction).

### My catalog has primary/variant or parent/child SKUs. Are these supported?

Yes. This would be similar to the [`item_group_id`](https://support.google.com/merchants/answer/6324507) in Merchant Center. You need to determine how you want to get recommendations back (at the parent or child level) and if the events are at the parent or child level.

See [Product levels](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/catalog#product-levels) for more about product levels.

Determine and set your correct product level before sending any items or events. The product level [can be changed](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/manage-catalog#change), but requires rejoining the items and retuning the models.

### Can I delete products from the catalog when they are no longer available?

If an item is no longer current, we recommend that you set its status to `OUT_OF_STOCK` rather than deleting it, so that previous user events that reference it are not invalidated.

## User events

These are frequently asked questions about user events.

### What user events do I need to collect?

See [About user events](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/user-events) for a list of user event types as well as user event requirements and best practices.

### How do I troubleshoot data quality issues in model creation?

In the AI Commerce Search in Gemini Enterprise for Customer Experience console, go to the **Data Quality** page for data quality metrics about your ingested catalog and user events.

### Can I integrate with Google Analytics 360?

You can use historical data from Google Analytics 360 (GA360). Similar to Merchant Center data, GA360 data can be exported to BigQuery, and then AI Commerce Search can read the events directly from BigQuery.

For real-time events, we recommend integrating tracking pixels with Google Tag Manager, because events are delayed from GA360.

### I want to import user events from Google Analytics 360. Does it provide all the user events needed?

Google Analytics 360 natively supports all user events used by AI Commerce Search except for search events. You can still import search user events from Analytics 360, but note that AI Commerce Search constructs the search user event from search queries and, if present, product impressions.

### How do I feed events into Recommendations AI?

  * [Cloud Storage](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/manage-user-events#importing_user_events_from)
  * [API inline import](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/manage-user-events#importing_user_events_inline)
  * [JavaScript Pixel](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/record-events#javascript-pixel)
  * [Google Tag Manager](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/manage-user-events#importing_user_events_from)
  * [API write method](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.userEvents/write)



Users typically import historical events using Cloud Storage or API import, then stream real-time events using the JavaScript Pixel or GTM tag.

### What if I can't send all of the user event types listed as required for a model? What are the minimum event types needed for each model?

Each model and optimization objective has slightly different requirements. See the [User event data requirements](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/create-models#import-reqs).

Model performance is typically better when there are more events per catalog item. Sites with large amounts of traffic may start with a smaller volume of historical data but still need at least a few weeks of data.

### I have add-to-cart and purchase-complete events that don't have a value for revenue or quantity. What should I submit?

If you don't have a value for quantity, you can pass a default value of 1 without affecting model results. Items should always have displayPrice set. originalPrice and cost are optional.

### My data only covered limited types of events. Can I still use AI Commerce Search?

See [User event data requirements](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/create-models#import-reqs) for the minimum data requirements of each model type.

## Search results

These are frequently asked questions about search results.

### Are search results personalized?

Yes. Search can provide personalized results. Search results are personalized based on visitor IDs. For more information, see [Personalization](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/search-basic#personalization).

### How do I include context, like the store a user is shopping from, as part of the search request?

Store ID-based availability and fulfilment options are attributes of the product catalog. Attributes can be sent as a parameter in the search request. The results can be filtered or ranked higher based on the store ID in the request.

### Can I hide products from search results?

Yes. The [`filter`](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.placements/search#request-body.FIELDS.filter) parameter can filter results out based on their tags.

### Is it possible to rank on multiple criteria, such as both availability and price?

Yes, the `boostSpec` allows complex ranking rules.

### Is it possible to group some attributes in order to deliver results with multiple facets? For example, grouping cities in the same country for origin of production.

Product attributes are not hierarchical. However, you could use multiple custom attributes to accomplish this (e.g., separate attributes for country and city).

### How do suggestions work?

Suggestions are a combination of user queries, rewritten queries, product names etc. To generate high quality autocomplete suggestions, a sufficient number of search events should be ingested along with the catalog.

### Is search case-sensitive?

Text queries are generally case-insensitive due to linguistic analysis. However, filter expressions and sort orders are strictly case-sensitive.

### How do I make part numbers with hyphens searchable?

Standard linguistic analysis may strip special characters. Map these values to a custom attribute with the `exact-searchable` flag enabled. Also consider breaking the string into n-grams prior to ingestion.

### Will the search engine translate a user's query if my catalog is in another language?

No. The catalog language and search query language must match. If you expect users to search in multiple languages, you should implement synonym controls to map their queries to your catalog's base language.

### Why are my searches filtering incorrectly by category?

Check your category names for this character: >. It's strictly reserved as the hierarchy separator (such as `Clothing > Mens`). If it appears in your category name by default, it will break the filter and must be replaced.

## Prediction results

These are frequently asked questions about prediction results.

### Is there a limit to the number of predictions I can return?

By default, a prediction request returns 20 items in the response. This can be increased or decreased by submitting a value for [pageSize](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.placements/predict#request-body).

If you need to return more than 100 items, contact Google Support. Note that returning more than 100 items can increase response latency.

### Am I able to view the reasons why a model made a specific product recommendation?

No.

### Can I download and cache prediction results?

Because prediction results improve in real-time in response to user activity on your site, we don't recommend using cached predictions. The models retrain daily to incorporate changes to your catalog and react to new trends.

On our end, using cached search and browse results infringes customer data privacy terms. It triggers a cache-detection mechanism, which automatically removes personalization.

More broadly, you can cache images and product details, as long as you don't cache the search results for a particular query and you send a fresh query for each search request.

### I need to re-rank the returned recommendations based on a business rule. Is this supported?

Yes. But while you can re-rank the returned recommendations based on your business rules, be aware that re-ordering or filtering recommended results can reduce the overall effectiveness of the model. Price reranking is available as a built-in customization for the Others You May Like and Recommended for You models. See [Price reranking](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/configs#price-reranking).

### Are there restrictions on the number of filter tags that I can create and use?

There are no hard limits on the number of unique tags. However, the system is not designed to handle many filter tags per item. We recommend keeping filter tags limited to a maximum of 10 per catalog item if possible. The limit for total tags across the entire catalog is 100,000,000. See [quotas and limits](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/quotas).

### Can I diversify recommendations?

Yes. [Recommendation diversification](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/predict#diversity) can be specified as part of the serving configuration or in the predict request [parameters](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.placements/predict#request-body).

### Can I prioritize recommendations by price?

Yes. [Price reranking](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/predict#price-rerank) causes recommended products with a similar recommendation probability to be ordered by price, with the highest-priced items first.

## Conversational features

These are frequently asked questions about AI Commerce Search's conversational features, product filtering, and commerce.

### How is a conversational session maintained, and how do I refresh the context?

A conversational session is maintained using the conversation ID returned in the Conversational agent response. You must pass this conversation ID in all subsequent requests within the same conversation. To refresh or start a new conversation, initiate a new API request _without_ a conversation ID.

### How does the streaming API affect my implementation and user experience?

The streaming nature means that you can immediately receive query types. This lets you differentiate between queries that have a conversational text response and those that won't like `SIMPLE_PRODUCT_SEARCH`. For `SIMPLE_PRODUCT_SEARCH`, you can immediately trigger a call to the core Search API.

### Why is it important for `searchParams` in the `ConversationalSearchRequest` to mirror my core Search API calls?

You want to maintain consistency in your `searchParams`, such as filters, sort order, and boost rules. Maintaining consistency helps to ensure that any conversational answers or refined queries provided by the API are aligned with the actual product results being displayed to the user.

### If a basic product search is detected, does the conversation end? Can the user go back to other conversational modes?

The conversation **doesn't end**. The conversation ID remains valid. Retailers can design their UX to keep the chat window persistent and allow users to continue the conversation. The ability to "revert back" depends on this specific UX implementation choice.

### What data does the Conversational API store for conversation context, and for how long?

To maintain the flow of a conversation, the Conversational API stores the user query, the conversational text response, and the follow-up question. This contextual information is retained for **seven days**.

### Why doesn't the Conversational API provide suggested answers for follow up questions, similarly to how conversational product filtering does?

While providing suggested answers to follow up questions isn't supported, it is on our roadmap to provide this capability. Stay tuned!

### How does the Conversational API use caching for performance and context?

The Conversational API caches the query types and refined search queries for a given customer and project for up to **10 days**. This means that if the same query is repeated, then the system can quickly retrieve the intent and suggested refinements.

## Machine learning models

These are frequently asked questions about models.

### I've uploaded my catalog & events, but I'm still getting this response when I call the predict API: Recommendation model is not ready.

You can set 'dryRun' to true in prediction request for integration purpose, which returns arbitrary catalog items from your Catalog (please DO NOT use this for production traffic)."

This usually means that your model has not finished training. If it has been more than 10 days since you created the model and you are continuing to get this response, please contact Support.

### How long does it take to train a model?

Initial model training and tuning takes 2-5 days to complete, but can take longer for large datasets. Subsequently, models are automatically retrained daily unless disabled. See [Pause and resume training for a model](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/manage-models).

### Can I download or export the model?

No.

### Can I use models I created in an existing project in a new project?

No. You need to [create and retrain](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/create-models) the models in the new project.

### I want to use a model for my category pages. Can I do that?

Yes. Recommended for You is useful on category pages. A category page is similar to a home page, except that you display only items from that category. You can achieve this using a standard Recommended for You model with filter tags. For example, you can add customized filter tags (corresponding to each category page) to the items in your catalog. When you send the prediction request, set the user event object as `category-page-view` and specify a specific category page's tag in the `filter` field. Only recommendation results matching the requested filter tag are returned. Diversity should be disabled in this use case, because diversity can conflict with category-based filter tags. 

### Can I disable personalization for my models?

By default, prediction results are personalized for the [Others You May Like](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/models#oyml), [Recommended for You](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/models#rfy), and [Buy it Again](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/models#bia) recommendation model types.

Disabling personalization isn't recommended. If you need non-personalized results, you can use a random unique visitor ID in a prediction request.

## AI Commerce Search in Gemini Enterprise for Customer Experience console

These are frequently asked questions about using the AI Commerce Search in Gemini Enterprise for Customer Experience console.

### I purged a number of events, but the dashboard still shows the counts for those event types.

This is expected. The AI Commerce Search in Gemini Enterprise for Customer Experience dashboard shows the number of events ingested over a certain period of time; it doesn't show the current count or number of events.

Generally, you should leave user events in place after they have been recorded. Purging events is not recommended. If you do need to purge events, see the documentation for [Remove user events](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/manage-user-events#remove-event).

### How can I tell if there are errors with my catalog or user events?

Most API calls return an error if there is a problem with syntax. The AI Commerce Search in Gemini Enterprise for Customer Experience dashboard shows percentage of unjoined events, which is also a useful metric. [Cloud Monitoring](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/monitor) and [Cloud Logging](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/error-reporting) can be used to monitor the status of events.

### Why do my recommendation serving configs show as inactive? How do I activate them?

In order to use recommendation serving configs, you first need to submit [catalog](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/upload-catalog) and [user event data](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/record-events) to train the corresponding model. Once a model has been trained, the dashboard indicates that the model is ready to query.

### In what currency does AI Commerce Search in Gemini Enterprise for Customer Experience report revenue metrics?

AI Commerce Search in Gemini Enterprise for Customer Experience reports metrics in the currency used in your uploaded data. AI Commerce Search does not support using multiple currencies per catalog and does not convert currencies.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
