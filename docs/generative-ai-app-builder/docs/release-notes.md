---
url: https://docs.cloud.google.com/generative-ai-app-builder/docs/release-notes/
title: Agent Search release notes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:23:03.231648+00:00
---

# Agent Search release notes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/generative-ai-app-builder/docs/release-notes/

**Note:** Vertex AI Search is being renamed to Agent Search. We are in the process of updating content to reflect the new branding. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Search ](https://docs.cloud.google.com/generative-ai-app-builder/docs)
  * [ Resources ](https://docs.cloud.google.com/generative-ai-app-builder/docs/resources)



Send feedback 

#  Agent Search release notes Stay organized with collections  Save and categorize content based on your preferences. 

This page documents production updates to Agent Search. Check this page for announcements about new or updated features, bug fixes, known issues, and deprecated functionality. **Product rebrand** : This product has been renamed since its introduction. Some of the former names include _Vertex AI Search, AI Applications,_ _Agent Builder,_ _Vertex AI Search and Conversation, Enterprise Search,_ and _Generative AI App Builder._ Regardless of the rebrand, the product's functionalities, such as search, recommendations, generative AI answers, and browse, remain true to the Google quality.

You can see the latest product updates for all of Google Cloud on the [ Google Cloud](https://docs.cloud.google.com/release-notes) page, browse and filter all release notes in the [Google Cloud console](https://console.cloud.google.com/release-notes), or programmatically access release notes in [BigQuery](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=google_cloud_release_notes&t=release_notes&page=table). 

To get the latest product updates delivered to you, add the URL of this page to your [feed reader](https://wikipedia.org/wiki/Comparison_of_feed_aggregators), or add the [feed URL](https://docs.cloud.google.com/feeds/gen-app-builder-release-notes.xml) directly. 

## October 16, 2026

Change

**Agent Search: Update to the stable model**

The `stable` model for answer generation is updated to `gemini-3.5-flash/answer_gen/v1` from `gemini-2.5-flash/answer_gen/v1`.

For more information, see [Answer generation model versions and lifecycle](https://docs.cloud.google.com/generative-ai-app-builder/docs/answer-generation-models).

## September 14, 2026

Feature

**Agent Search: Rotate CMEK keys (GA)**

Rotating customer-managed encryption keys (CMEK) that protect your Agent Search apps and data connectors is generally available (GA). When you make a new version of a registered key the primary version in Cloud Key Management Service (Cloud KMS), Agent Search detects the change and re-encrypts your data with the new key version automatically.

For more information, see [Rotate Cloud KMS keys](https://docs.cloud.google.com/generative-ai-app-builder/docs/cmek#rotate-keys).

Feature

**Agent Search: Search query add-ons for configurable pricing (GA)**

Search query add-on specifications (`searchAddonSpec`) for configurable pricing are generally available (GA) in the v1 API. You can use `searchAddonSpec` when you want to save money by turning off add-ons for individual search requests made programmatically.

For more information, see [About controlling which add-ons apply to a search request](https://docs.cloud.google.com/generative-ai-app-builder/docs/enable-configurable-pricing#control-addons) and [REST, per search request](https://docs.cloud.google.com/generative-ai-app-builder/docs/enable-configurable-pricing#search-configurable) in _Manage configurable pricing for search query add-ons_.

## August 13, 2026

Feature

**Agent Search: Gemini 3.5 Flash answer generation**

You can generate answers with the Gemini 3.5 Flash model.

For more information, see [Answer generation model versions and lifecycle](https://docs.cloud.google.com/generative-ai-app-builder/docs/answer-generation-models) and [Gemini 3.5 Flash](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/gemini/3-5-flash).

## July 23, 2026

Feature

**Agent Search: Decrease thresholds for configurable pricing**

You can decrease the storage size and queries per minute (QPM) subscription thresholds for configurable pricing. Previously, you could only increase these thresholds.

Decreased thresholds take effect at the start of the next billing cycle.

For more information, see [Modify subscription thresholds](https://docs.cloud.google.com/generative-ai-app-builder/docs/enable-configurable-pricing#modify-thresholds). This feature is generally available (GA).

## June 08, 2026

Feature

**Agent Search: Prefix and partial matching for filtering search queries (Preview)**

You can configure schema fields to support prefix matching and partial matching in filter expressions:

  * Prefix matching lets you filter search results based on whether a field value starts with a specific string.

  * Partial matching lets you filter results based on whether the query contains some of the words in the field value. Partial matching doesn't require a perfect match like the `ANY` operator does.




This feature is in Public Preview. For more information, see [Configure field settings](https://docs.cloud.google.com/generative-ai-app-builder/docs/configure-field-settings).

Feature

**Agent Search:`EXISTS` filter for filtering search queries (Preview)**

You can use the `EXISTS` filter to filter search results for documents. Specifying `EXISTS` for a field means that a document can only be returned in a search request if the field has a value and that value is not the default. This filter is available for custom search and for media search. Use `EXISTS` with other filters such as `ANY` and `IN` to create expressions to scope the documents that can be returned in a search query.

This feature is in Public Preview. For more information, see [Filter custom search for structured or unstructured data](https://docs.cloud.google.com/generative-ai-app-builder/docs/filter-search-metadata), [Filter website search](https://docs.cloud.google.com/generative-ai-app-builder/docs/filter-website-search), and [Filter media search](https://docs.cloud.google.com/generative-ai-app-builder/docs/filter-media-search).

## May 27, 2026

Feature

**Agent Search: Table and image annotation in layout parser**

The table annotation and image annotation features of the layout parser are generally available (GA).

You can ask the layout parser to annotate images or tables with a descriptive block of text describing the information in the image or table. The annotation can then be used as a source in a generated answer. For more information, see [Layout parser](https://docs.cloud.google.com/generative-ai-app-builder/docs/parse-chunk-documents#layout-parsing).

## May 15, 2026

Deprecated

**Agent Search: Agent Search for healthcare is deprecated**

Agent Search for healthcare is deprecated.

For a comprehensive, managed solution, consider building [custom search apps](https://docs.cloud.google.com/generative-ai-app-builder/docs/about-generic-search) on Agent Search. Or, if you require fine-grained control over the underlying retrieval mechanisms and are prepared for a more customer-managed integration, use Agent Retrieval (formerly known as [Vector Search 2.0](https://docs.cloud.google.com/vertex-ai/docs/vector-search-2/overview)).

## May 13, 2026

Feature

**Agent Search: Weight searchable fields (Preview)**

You can specify a weight for searchable fields in your schema to indicate their relative importance in search results.

This feature is in Public Preview. For more information, see [Weight searchable fields](https://docs.cloud.google.com/generative-ai-app-builder/docs/configure-field-settings#weight-search).

Feature

**Agent Search: Stream answers using agentic retrieval (GA with allowlist)**

You can use agentic retrieval with the streaming answer method.

Agentic retrieval can return better results as compared to the standard streaming answer method. This is because agentic retrieval can do multi-pass searches across multiple data stores. The agent plans and executes searches sequentially, choosing the best tools, such as Google Search and Google Maps, for each step. Agentic retrieval also enables multi-turn search queries (follow-up questions) on blended search apps.

For more information, see [Stream answers using agentic retrieval](https://docs.cloud.google.com/generative-ai-app-builder/docs/agentic-retrieval-stream-answer).

This feature is GA with an allowlist, available for select customers.

## April 22, 2026

Feature

**Agent Search: MCP server (GA)**

Agent Search has a Model Context Protocol (MCP) server hosted at the following endpoint: `https://discoveryengine.googleapis.com/mcp`

This feature is generally available (GA). For more information, see [MCP Reference: discoveryengine.googleapis.com](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/mcp).

Feature

**Agent Search: Dense reciprocal rank for custom ranking**

You can use the dense reciprocal rank transformation function, `drr`, to customize search result ranking. It's an improvement on the reciprocal rank function, `rr`. Using the dense reciprocal rank function leads to higher quality ranking when there are duplicate signal values.

Duplicate signal values are more common when the ranking formula contains the following types of signal:

  * The `boosting_factor` signal
  * The `geo_distance()` function signal
  * Categorical and integer custom signals



This feature is generally available (GA). For more information, see [Customize search results ranking](https://docs.cloud.google.com/generative-ai-app-builder/docs/custom-ranking).

Feature

**Agent Search: Geodistance function for custom ranking (GA)**

The `geo_distance` function can be used in custom ranking formulas to calculate the distance between a source location and a destination location. The function supports query locations extracted from natural language, explicitly provided coordinates, and addresses.

This feature is generally available (GA). For more information, see [Custom ranking: Geodistance—a derived signal](https://docs.cloud.google.com/generative-ai-app-builder/docs/custom-ranking#geodistance).

Feature

**Agent Search: Filter searches by document-level relevance (GA)**

When searching in your Agent Search app, you can specify document-level relevance filters so that only the documents that meet the filter threshold are returned as results.

You can specify either the relevance threshold or semantic-relevance threshold to filter documents by relevance based on keyword and semantic search similarity.

This feature is Generally Available (GA). For more information, see [Filter searches by document-level relevance](https://docs.cloud.google.com/generative-ai-app-builder/docs/filter-by-relevance).

Change

**Agent Search: Renamed from Vertex AI Search**

The Vertex AI Search product has been renamed as Agent Search in the following contexts:

  * The documentation set. See [What is Agent Search?](https://docs.cloud.google.com/generative-ai-app-builder/docs/introduction)



What has not changed:

  * The user interface in the Google Cloud console is still referred to as Vertex AI Search and AI Applications. See [Vertex AI Search](https://console.cloud.google.com/gen-app-builder).

  * The APIs still use the Discovery Engine API endpoints. See [APIs and reference](https://docs.cloud.google.com/generative-ai-app-builder/docs/apis).




Despite the rebrand, the product functionality remains the same.

## March 26, 2026

Feature

**Vertex AI Search: Gemini 3.1 Pro and Gemini 3 Flash for answer generation (Preview)**

You can generate answers with the Gemini 3.1 Pro (Preview) and Gemini 3 Flash (Preview) models.

For more information, see [Answer generation model versions and lifecycle](https://docs.cloud.google.com/generative-ai-app-builder/docs/answer-generation-models), [Gemini 3.1 Pro](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/models/gemini/3-1-pro), and [Gemini 3 Flash](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/models/gemini/3-flash).

Announcement

**Vertex AI Search: Gemini 3 Pro (Preview) for answer generation discontinued**

The Gemini 3 Pro (Preview) model has been discontinued and is no longer available for answer generation. If you have been using that model, upgrade to the Gemini 3.1 Pro (Preview) model.

For information about available models, see [Answer generation model versions and lifecycle](https://docs.cloud.google.com/generative-ai-app-builder/docs/answer-generation-models).

## February 24, 2026

Feature

**Vertex AI Search: Change the pricing model for a project**

There are two pricing models for apps and data stores: the general model (pay-as-you-go consumption-based) and the configurable subscription model (a monthly subscription).

You can switch from configurable pricing to general pricing for a project if all its data stores and apps use the general model. For more information, see [Disable configurable pricing for project](https://docs.cloud.google.com/generative-ai-app-builder/docs/enable-configurable-pricing#disable-configurable).

## February 17, 2026

Feature

**Vertex AI Search: Gemini 3 Pro for answer generation (Preview)**

You can generate answers with the Gemini 3 Pro model.

For more information, see [Answer generation model versions and lifecycle](https://docs.cloud.google.com/generative-ai-app-builder/docs/answer-generation-models) and [Gemini 3 Pro](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/models/gemini/3-pro).

## February 05, 2026

Feature

**Vertex AI Search: MCP server (Preview)**

Vertex AI Search has a Model Context Protocol (MCP) server hosted at the following endpoint: `https://discoveryengine.googleapis.com/mcp`

This feature is in Public Preview. For more information, see [MCP Reference: discoveryengine.googleapis.com](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/mcp).

## January 26, 2026

Feature

**Vertex AI Search: Change the pricing model for apps and data stores**

There are two pricing models for apps and data stores: the general model (pay-as-you-go consumption-based) and the configurable subscription model (a monthly subscription).

If you have enabled configurable pricing for your project, you can change the pricing model for apps and data stores from configurable to general, as well as from general to configurable. See [Disable configurable pricing](https://docs.cloud.google.com/generative-ai-app-builder/docs/enable-configurable-pricing#disable-configurable-pricing).

## December 16, 2025

Feature

**Vertex AI Search: Filter searches by document-level relevance (Preview)**

When searching in your Vertex AI Search app, you can specify document-level relevance filters so that only the documents that meet the filter threshold are returned as results.

You can specify either the relevance threshold or semantic-relevance threshold to filter documents by relevance based on keyword and semantic search similarity.

This feature is in Public Preview. For more information, see [Filter searches by document-level relevance](https://docs.cloud.google.com/generative-ai-app-builder/docs/filter-by-relevance).

## December 09, 2025

Feature

**Vertex AI Search: Configurable pricing for custom search (GA)**

Configurable pricing is available for custom search apps and data stores.

Configurable pricing offers a flexible alternative to the default pay-as-you-go model. Configurable pricing lets you to choose a subscription that fits your needs. There are two subscriptions, one for storage and one for search queries, plus add-ons that let you add more features according to your needs.

For storage, the minimum subscription is 50 GiB/month and the available add-on is semantic embedding. For search queries, the minimum subscription is 1000 queries per minute per project, and the available add-ons are semantic query, KPI & personalization, and AI overview.

After you set up configurable pricing for a project, apply configurable pricing to apps and data stores as needed. In a project, you can have some apps and data store using the general pricing and others using configurable pricing.

Configurable pricing is generally available (GA). For more information, see [Enable configurable pricing for custom search](https://docs.cloud.google.com/generative-ai-app-builder/docs/enable-configurable-pricing) and [Vertex AI Search pricing](https://docs.cloud.google.com/generative-ai-app-builder/pricing).

## November 24, 2025

Feature

**Vertex AI Search: Natural language query filters (GA)**

For queries on structured data stores, the natural language queries can be reformulated as filters and a residual query. For example, "Find a coffee shop serving banana bread" becomes `"query": "banana bread", "filter": "type": ANY("cafe")`.

The natural-language query understanding feature only applies to custom search apps attached to a single, structured, data store.

By default, a hard restriction filter is applied, but a softer, boost-like filter can be used instead.

This feature is generally available (GA). For more information, see [Filter with natural language understanding](https://docs.cloud.google.com/generative-ai-app-builder/docs/natural-language-queries).

## November 21, 2025

Feature

**Vertex AI Search: Allowlist fields for natural language query understanding**

You can specify an allowlist of fields to be used for filter extraction. If you have some fields, perhaps for internal use, that you don't want to be used in filters, then specify an allowlist to restrict the fields that can be used.

For more information, see [Specify fields for natural-language queries](https://docs.cloud.google.com/generative-ai-app-builder/docs/natural-language-queries#search-nl-allowlist).

## November 20, 2025

Feature

**Vertex AI Search: Updated file size restrictions for unstructured data**

The file size restrictions for unstructured data import have been unified. For unstructured data, you can import files up to 200 MB regardless of the parser type.

For more information, see [Unstructured data](https://docs.cloud.google.com/generative-ai-app-builder/docs/prepare-data#unstructured).

## November 14, 2025

Feature

**Vertex AI Search: Gemini layout parser (Preview)**

For data stores with unstructured documents, you can use Gemini to get layout analysis and content extraction on PDF files. Layout parsing with Gemini provides high quality table recognition, improved reading order and more accurate text recognition.

This feature is in Public Preview. For more information, see [Parse and chunk documents](https://docs.cloud.google.com/generative-ai-app-builder/docs/parse-chunk-documents).

## November 05, 2025

Feature

**Vertex AI Search: Layout parser support for DOCX, PPTX, and XLSX (GA)**

With the layout parser, support for parsing DOCX, PPTX, and XLSX file formats is Generally Available (GA). Both the layout and digital parsers can parse PDF, HTML, DOCX, PPTX, and XLSX files. For more information about the parsers, see [Parse and chunk documents](https://docs.cloud.google.com/generative-ai-app-builder/docs/parse-chunk-documents).

**Important:** If you have been using the layout parser for these file formats, you will now be billed when parsing new documents. For information about layout parser pricing, see [Document AI feature pricing](https://cloud.google.com/document-ai/pricing).

## October 02, 2025

Change

**Vertex AI Search: Renamed from AI Applications**

The AI Applications product has been renamed as Vertex AI Search in the following contexts:

  * The documentation set. See [What is Vertex AI Search?](https://docs.cloud.google.com/generative-ai-app-builder/docs/introduction)
  * The marketing collateral. See [Vertex AI Search](https://docs.cloud.google.com/enterprise-search).



What has not changed:

  * The user interface in the Google Cloud console is still referred to as AI Applications. See [AI Applications](https://console.cloud.google.com/gen-app-builder).
  * The APIs still use the Discovery Engine API endpoints. See [APIs and reference](https://docs.cloud.google.com/generative-ai-app-builder/docs/apis).



Despite the rebrand, the product functionality remains the same.

## August 13, 2025

Feature

**Vertex AI Search: Custom ranking of search results (GA)**

You can modify the ranking behavior of your search app using custom ranking. Custom ranking lets you provide a [mathematical expression](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.dataStores.servingConfigs/search#body.request_body.FIELDS.ranking_expression) that relies on a set of model-computed signals (such as semantic relevance score and keyword similarity score) and document-based signals (such as a custom field like distance or document age). The resulting ranking of the search results is more considered and likely matches a user's needs better than a purely embedding-based ranking.

For more information, see [Customize search results ranking](https://docs.cloud.google.com/generative-ai-app-builder/docs/custom-ranking).

## August 06, 2025

Feature

**Vertex AI Search: Advanced autocomplete (GA)**

Use advanced autocomplete to enable autocomplete on blended search apps.

For more information, see [Configure advanced autocomplete](https://docs.cloud.google.com/generative-ai-app-builder/docs/configure-advanced-autocomplete). This feature is Generally Available (GA).

## August 04, 2025

Change

**Vertex AI Search: gemini-2.5-flash/answer_gen/v1 model is the default model**

Model version gemini-2.5-flash/answer_gen/v1 is the default model for generating answers in Vertex AI Search.

For more information, see [Answer generation model versions and lifecycle](https://docs.cloud.google.com/generative-ai-app-builder/docs/answer-generation-models).

## July 09, 2025

Announcement

**AI Applications: Quotas**

AI Applications offers the following allocation quotas in the global region (`global`), the US multi-region (`us`), and the EU multi-region (`eu`) under the Discovery Engine API:

  * Number of data stores per project
  * Number of documents per project
  * Number of engines per project
  * Number of user events



The number of data stores, documents, user events, and engines across all locations can't exceed the total per-project quota for that resource.

For more information, see [Quotas](https://docs.cloud.google.com/generative-ai-app-builder/quotas).

## July 02, 2025

Feature

**Vertex AI Search: Search for an exact match (GA)**

To search for an exact match, you can enclose your search query in double quotes (`"`). For example, when you search for `"Mary had a little lamb"`, Vertex AI Search looks for the phrase exactly as it is. It doesn't return search results that contain `Mary had lamb`, which has missing words; or `a little lamb had Mary`, which has the words in a different order.

This feature is Generally Available when you use the [`engines.servingConfigs.search`](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.engines.servingConfigs/search) method to get search results for [custom data](https://docs.cloud.google.com/generative-ai-app-builder/docs/preview-search-results), [media data](https://docs.cloud.google.com/generative-ai-app-builder/docs/get-media-search-results), and [healthcare data](https://docs.cloud.google.com/generative-ai-app-builder/docs/search-hc-data).

## June 26, 2025

Feature

**Vertex AI Search: gemini-2.5-flash/answer_gen/v1 model**

You can generate answers with the Gemini 2.5 Flash (`gemini-2.5-flash`) model. This model is tuned to address context-based question and answering tasks.

For more information, see [Answer generation model versions and lifecycle](https://docs.cloud.google.com/generative-ai-app-builder/docs/answer-generation-models).

## June 16, 2025

Change

**AI Applications: Custom search and recommendations**

The vertical-agnostic apps, formerly known as _generic_ search and recommendations, are renamed to _custom_ search and recommendations. You'll see this new name in the product console and the documentation set. The functionality and the endpoints remain the same.

## June 06, 2025

Feature

**Vertex AI Search: Skip layout parsing for types of HTML content (GA)**

The [layout parser](https://docs.cloud.google.com/generative-ai-app-builder/docs/parse-chunk-documents#layout-parsing) can skip parsing specific types of HTML content. By excluding less relevant content such as boilerplate, you can improve data quality. The layout parser can exclude based on HTML tags and IDs and on CSS classes.

This feature is Generally Available (GA) and accessible only through the API. For more information, see [Exclude HTML content](https://docs.cloud.google.com/generative-ai-app-builder/docs/parse-chunk-documents#exclude-html-content).

## May 29, 2025

Feature

**Vertex AI Search: Adjust autocomplete settings to reduce risk of PII leaks (Public Preview)**

If you use either the search history or user events model for autocomplete suggestions and you have concerns about your users entering their personally identifiable information (PII) as search queries, then see [Reduce the risk of returning suggestions that contain PII](https://docs.cloud.google.com/generative-ai-app-builder/docs/configure-autocomplete#update-thresholds). 

This feature is in Public Preview.

## May 20, 2025

Feature

**Vertex AI Search: Media search automatically chooses the results mode**

Media search can respond to queries as full queries or as partial (search-as-you-type) queries. You can specify which query mode to use or you can specify the auto mode. 

With auto mode, Media search makes the choice for you by assessing and weighting various signals such as query length and content. Use the auto mode if you have one search box that some users expect to respond with search-as-you-type suggestions and others expect to respond as a full query search.

Auto mode is the default mode. For more information, see [Get search results for media](https://docs.cloud.google.com/generative-ai-app-builder/docs/get-media-search-results).

## April 24, 2025

Feature

**Vertex AI Search: Obtain claim-level grounding scores (GA)**

Claim-level scores from the check grounding API is Generally Available (GA). In addition to the answer-level support score, you can obtain a support score for each claim in an answer candidate.

For more information, see [Obtain claim-level scores for an answer candidate](https://docs.cloud.google.com/generative-ai-app-builder/docs/check-grounding#claim-level-score-procedure).

## April 07, 2025

Feature

**Vertex AI Search: Stream Google Cloud Storage buckets to data stores**

In addition to one time and periodic imports from Cloud Storage, you can stream unstructured data from Cloud Storage into a data store. This lets you serve results from the bucket to your users in near real time.

Streaming must be set up at the bucket-level (not at the folder- or file-level), and the bucket may only contain unstructured data.

For general information about creating data stores, see [Create a search data store](https://docs.cloud.google.com/generative-ai-app-builder/docs/create-data-store-es).

Change

**Vertex AI Search: Grounded generation with the`generateGroundedContent` API**

The `generateGroundedContent` API to that grounds your answers with your inline text, Vertex AI Search data store, and Google Search is no longer available.

Instead, to generate grounded answers, Google recommends that you use the Generally Available [`generateContent`](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.endpoints/generateContent) API. You can either ground your answers [with Google Search](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/grounding/grounding-with-google-search) or [with your own data](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/grounding/grounding-with-your-data). For more information, see [Overview](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/grounding/overview).

## April 02, 2025

Change

**AI Applications: Renamed from Vertex AI Agent Builder**

The _Vertex AI Agent Builder_ product has been renamed _AI Applications_. You'll see this new name in the product console, the documentation set, and the marketing collateral. The product functionality and endpoints remain the same.

## March 19, 2025

Feature

**Vertex AI Search: Generate and return charts in answers and with follow-ups (Public Preview)**

The answer method can include a chart in an answer, as well as text. The chart is generated from the data in the data store. A chart is generated if there is sufficient data, and the query either asks for a chart or the answer is sufficiently complex that the method itself determines that a chart is helpful.

This feature is in Public Preview and is only available through the API. For more information, see [Generate charts for answers](https://docs.cloud.google.com/generative-ai-app-builder/docs/answer#get-charts).

Feature

**Vertex AI Search: Return corpus images in answers and with follow-ups (Public Preview)**

The answer method can return images in answers, along with text. 

If appropriate, one image from the data store can be returned with the answer. Citations can also include images from the data store.

This feature is restricted to queries made to unstructured data stores where the layout parser is in effect and is only available through the API. For more information, see [Retrieve existing images from the data store](https://docs.cloud.google.com/generative-ai-app-builder/docs/answer#get-images).

## March 03, 2025

Feature

**Vertex AI Search: Ranking visibility and custom ranking (Private Preview)**

You can access the signals that contribute to your ranking and then tune these signals to customize the ranking. To tune the ranking signals, you can modify predefined ranking expressions or specify custom ranking expressions.

Ranking visibility and custom ranking is a Private Preview feature.

## February 28, 2025

Feature

**Vertex AI Search: Document-relevance scores for search results (GA)**

You can ask to have a relevance score returned for each search result associated with a query. The returned score can be used to do post-search ranking or filtering of the results. This feature is available for search apps associated with structured and unstructured data stores.

This feature is Generally Available (GA). For more information, see [Get document-relevance score with search results](https://docs.cloud.google.com/generative-ai-app-builder/docs/preview-search-results#relevance-scores).

## February 26, 2025

Feature

**Vertex AI Search: Personalize responses from the answer method (GA)**

When making a query call to the answer method, you can provide information about the user to personalize the generated answer. 

This feature is Generally Available (GA). For more information, see [Personalize answers](https://docs.cloud.google.com/generative-ai-app-builder/docs/answer#personalize-answers).

## February 13, 2025

Feature

**Vertex AI Search: Stream answers (GA)**

Vertex AI Search now supports answer streaming. This feature returns generated answers in sequential parts, reducing the perception of latency. As the end users read the first part of the answer, the subsequent parts of the answer are being generated. 

This feature also includes many of the features of the original answer method. 

This feature is Generally Available to all customers. For more information, see [Stream answers](https://docs.cloud.google.com/generative-ai-app-builder/docs/stream-answer).

## February 10, 2025

Change

**Vertex AI Search: gemini-2.0-flash-001 model for the answer method**

The Gemini 2.0 Flash (`gemini-2.0-flash-001`) model is available for answer generation in Vertex AI Search. This model is tuned to address context-based question and answering tasks.

For more information, see [Answer generation model versions and lifecycle](https://docs.cloud.google.com/generative-ai-app-builder/docs/answer-generation-models).

## January 24, 2025

Feature

**Vertex AI Search: Identity mapping store (GA)**

You can map your identity provider (IDP) to external identities from third-party applications that aren't managed by your identity provider. This information allows Google to enforce access control correctly by syncing users from your IDP and third-party applications. For more information, see the [`IdentityMappingStore`](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.identityMappingStores) resource in the API docs.

## January 14, 2025

Feature

**Vertex AI Search: gemini-1.5-flash-001/answer_gen/v2 for healthcare**

The `gemini-1.5-flash-001/answer_gen/v2` model is available for answer generation in healthcare search apps.

For more information, see [Available models](https://docs.cloud.google.com/generative-ai-app-builder/docs/answer-generation-models#models).

## January 09, 2025

Feature

**Vertex AI Search: View widget metrics on the Analytics page (GA with allowlist)**

You can view metrics from the widget on the Analytics page.

This feature is available to select Google Cloud customers (GA with allowlist). For more information, see [View search analytics](https://docs.cloud.google.com/generative-ai-app-builder/docs/view-analytics#search-analytics).

## December 09, 2024

Feature

**Vertex AI Agent Builder: Grounding is available in more languages (GA with allowlist)**

The grounded generation API supports more than 35 languages.

This feature is available to select Google Cloud customers (GA with allowlist). For general information about grounding, see [Generate grounded answers with RAG](https://docs.cloud.google.com/generative-ai-app-builder/docs/grounded-gen). For available languages, see [Languages](https://docs.cloud.google.com/generative-ai-app-builder/docs/languages-locales).

Feature

**Vertex AI Agent Builder: Additional inputs for generating grounded answers (GA with allowlist)**

You can specify a language code and a latitude-longitude value when making calls to the grounded generation API. 

If the language can't be determined from the query, then the language code is used to set the language for the answer. If the language code is not present, then the latitude-longitude value is used to set the language. 

The latitude-longitude value is also used to answer location-related queries, such as "restaurants near me".

This feature is available to select Google Cloud customers (GA with allowlist). For more information, see [Generate grounded answers with RAG](https://docs.cloud.google.com/generative-ai-app-builder/docs/grounded-gen).

## December 04, 2024

Feature

**Vertex AI Search: gemini-1.5-flash-002-high-fidelity model (Public Preview)**

The `gemini-1.5-flash-002-high-fidelity` model is available for grounded answer generation with RAG. This model is based on the `gemini-1.5-flash-002` model and has been further tuned to address context-based question and answering tasks. This model is suitable for specialized industries, such as financial services, healthcare, and insurance.

This model is available in Public Preview.

For more information, see [High fidelity models](https://docs.cloud.google.com/generative-ai-app-builder/docs/grounded-gen#high-fidelity-models).

Feature

**Vertex AI Search: Boost controls for media recommendations (Public Preview)**

Boost controls are used to affect the order in which recommendations are listed. Boost controls use filters on `string` and `boolean` values in the schema data to determine what media content to boost or bury. The boost value (-1 to 1) determines whether the content should be placed lower (buried) or higher (boosted) in the list of recommendations returned. 

Boost controls are attached to serving configs and applied to `recommend` method calls.

The boost feature is in Public Preview and is available through the API. For more information about the feature, see [Boost and bury media recommendations](https://docs.cloud.google.com/generative-ai-app-builder/docs/media-recommendations-boost-bury).

## December 03, 2024

Feature

**Vertex AI Search: Index and refresh web pages using sitemap (Public Preview)**

If advanced website indexing is enabled in your data store, you can submit and use sitemaps and sitemap indexes to index and refresh the web pages in your data store. This feature supports only XML sitemaps and sitemap indexes.

This feature is in Public Preview and is available through the API. For more information about the feature, see [Index and refresh web pages using sitemaps](https://docs.cloud.google.com/generative-ai-app-builder/docs/index-refresh-sitemap).

## November 26, 2024

Feature

**Vertex AI Search: Check ingested data quality for media recommendations (GA)**

You can check the quality of your ingested data for media recommendations through the Google Cloud console. These checks are not blocking but can suggest ways that your data can be improved. This feature is Generally Available (GA).

Previously, this check was only available through API method calls. 

For more information, see [Check data quality for media recommendations](https://docs.cloud.google.com/generative-ai-app-builder/docs/check-media-data-quality).

## October 31, 2024

Feature

**Vertex AI Search: Stream answers (GA with allowlist)**

The answer streaming method can return generated answers in sequential parts. This reduces the perception of latency. As the end users read the first part of the answer, the subsequent parts of the answer are being generated. 

The answer streaming method also includes many of the features of the original [answer](https://docs.cloud.google.com/generative-ai-app-builder/docs/answer) method.

This feature is Generally Available to select Google customers (GA with allowlist). For more information, see [Stream answers](https://docs.cloud.google.com/generative-ai-app-builder/docs/stream-answer).

## October 25, 2024

Feature

**Vertex AI Search: Return only well-grounded answers with summaries and follow-ups (GA)**

With the answer method, you can choose to filter out poorly-grounded answers. There are two filter levels: choose to return only answers with high grounding scores (at the risk of losing some helpful answers) or choose a lower filter to get more answers.

This feature is Generally Available (GA). For more information, see [Show only well-grounded answers](https://docs.cloud.google.com/generative-ai-app-builder/docs/answer#show-grounded-answers).

Feature

**Vertex AI Search: Get grounding scores for answers with summaries and follow-ups (GA)**

The answer method can return aggregated grounding scores for answers and individual grounding scores for claims.

This feature is Generally Available (GA). For more information, see [Return grounding support scores](https://docs.cloud.google.com/generative-ai-app-builder/docs/answer#return-support-scores).

Feature

**Vertex AI Search: Advanced autocomplete (Public Preview)**

Use advanced autocomplete to enable autocomplete on blended search apps. Also, advanced autocomplete supports:

  * Access control
  * Language boosting
  * Rich suggestions, which return document suggestions or recent search suggestions



For more information, see [Configure advanced autocomplete](https://docs.cloud.google.com/generative-ai-app-builder/docs/configure-advanced-autocomplete). This feature is in Public Preview.

## October 17, 2024

Feature

**Vertex AI Search: CMEK for US and EU (GA) and CMEK with EKM and HSM (GA with allowlist)**

Customer-managed encryption keys (CMEK) are Generally Available (GA) in the US and the EU. You no longer need to be added to an allowlist to use CMEK. If you store your data in a US or EU multi-region data store, you can provide your own encryption key to protect your data at rest.

Using external key manager (EKM) or hardware security module (HSM) with CMEK is in GA with allowlist.

For information, see [Customer-managed encryption keys](https://docs.cloud.google.com/generative-ai-app-builder/docs/cmek).

## October 14, 2024

Feature

**Vertex AI Search: Answers with summaries and follow-ups for blended search apps (GA with allowlist)**

The answer method can be used to query blended search apps. You can apply the answer method to blended search apps in the same way that you apply the method to search apps that are connected to only one data store.

This feature is Generally Available to select Google customers (GA with allowlist). For more information, see [Get answers and follow-ups](https://docs.cloud.google.com/generative-ai-app-builder/docs/answer).

## October 01, 2024

Feature

**Vertex AI Agent Builder: Dynamic retrieval for grounded results (GA with allowlist)**

Dynamic retrieval lets you choose when to turn off grounding with Google Search. This is useful when a prompt doesn't require an answer grounded in Google Search and the supported models can provide an answer based on their own knowledge without grounding. Dynamic retrieval helps you manage latency, quality, and cost more effectively. 

This feature is available to select Google Cloud customers (GA with allowlist). For more information, see [Dynamic retrieval](https://cloud.google.com/generative-ai-app-builder/docs/grounded-gen#dynamic-retrieval).

## September 25, 2024

Change

**Vertex AI Search: gemini-1.5-flash-002/answer_gen/v1 model**

The `gemini-1.5-flash-002/answer_gen/v1` model is available for answer generation. This model is based on the `gemini-1.5-flash-002` model and has been further tuned to address question and answering tasks.

For more information, see [Answer generation model versions and lifecycle](https://docs.cloud.google.com/generative-ai-app-builder/docs/answer-generation-models).

Change

**Vertex AI Search: Update to the preview model**

The preview model for answer generation has been updated to `gemini-1.5-pro-002` from `gemini-1.5-pro-001`.

For more information, see [Answer generation model versions and lifecycle](https://docs.cloud.google.com/generative-ai-app-builder/docs/answer-generation-models).

## September 18, 2024

Feature

**Vertex AI Agent Builder: Redirection URI for grounded results (GA)**

When you use Grounding with Google Search, the grounded result contains a redirection URI that leads you to the publisher's URI. This redirection URI remains accessible for up to 30 days after the grounded result is generated.

This feature is Generally Available (GA). For more information, see [Generate grounded answers with RAG](https://docs.cloud.google.com/generative-ai-app-builder/docs/grounded-gen).

## September 17, 2024

Feature

**Vertex AI Search: Firestore and Cloud SQL import (GA)**

Importing data from Firestore and Cloud SQL is Generally Available.

For more information, see [Import from Firestore](https://docs.cloud.google.com/generative-ai-app-builder/docs/create-data-store-es#firestore) and [Import from Cloud SQL](https://docs.cloud.google.com/generative-ai-app-builder/docs/create-data-store-es#cloud-sql).

## September 11, 2024

Feature

**Vertex AI Search: Natural language query filters (Public Preview)**

For queries on structured data stores, the natural language queries can be reformulated as filters and a residual query. For example, `"Find a coffee shop serving banana bread"` becomes `"query": "banana bread", "filter": "type": ANY(\"cafe\")`.

The natural-language query understanding feature only applies to generic apps that use structured data stores.

This feature is in Public Preview. For more information, see [Filter with natural language understanding](https://docs.cloud.google.com/generative-ai-app-builder/docs/natural-language-queries).

Feature

**Vertex AI APIs: Updated model for ranking and reranking documents for RAG**

The ranking API model is upgraded. This underlying model significantly improves the relevance of top-ranked documents and provides more nuanced scores. For more information about ranking documents, see [Rank and rerank documents with RAG](https://docs.cloud.google.com/generative-ai-app-builder/docs/ranking).

## August 28, 2024

Feature

**Vertex AI Search: Turn off schema auto-detect for structured data**

By default, schema auto-detect dynamically adds new properties to the schema when the property fields are detected on data import. 

However, you can turn off the dynamic feature so that only data that corresponds to fields already in the schema get imported. This is good approach for not-so-clean data because you can choose not to import extraneous data that isn't part of your defined schema and that you don't want in your structured data store.

For more information, see [About providing your own schema as a JSON object](https://docs.cloud.google.com/generative-ai-app-builder/docs/provide-schema#about_providing_your_own_schema_as_a_json_object).

Feature

**Vertex AI Search: Datetime and geolocation detection for structured data**

By default, when structured data is imported, fields that are detected in `datetime` and `geolocation` format are assigned those types in the schema.

However, you can turn off datetime and geolocation detection so that in the schema the `datetime` fields are set to type `string` and the `geolocation` fields are set to type `object`.

For more information, see [About providing your own schema as a JSON object](https://docs.cloud.google.com/generative-ai-app-builder/docs/provide-schema#about_providing_your_own_schema_as_a_json_object).

## August 23, 2024

Feature

**Vertex AI Search: Connect Google Cloud Storage datasets to Vertex AI Search (Public Preview)**

You can create Vertex AI Search data stores that periodically sync with data in Cloud Storage datasets. You can choose how often you want to update your data stores: every day, every 3 days, or every 5 days.

Synchronizing Cloud Storage data to Vertex AI Search is available in Public Preview. For more information, see [Import from Cloud Storage](https://docs.cloud.google.com/generative-ai-app-builder/docs/create-data-store-es#cloud-storage).

## August 16, 2024

Feature

**Vertex AI Search: Search tuning (GA)**

Search tuning for unstructured data stores is Generally Available (GA). You can upload training files to tune the model for your search app.

Search tuning supports Data Residency; you can tune data stores in the US and EU multi-regions as well as global data stores.

For information, see [Improve search results with search tuning](https://docs.cloud.google.com/generative-ai-app-builder/docs/tune-search).

## August 06, 2024

Feature

**Vertex AI Search: Layout parser GA**

The layout parser for Vertex AI Agent Builder is Generally Available. The layout parser transforms documents in various formats into structured representations. It makes content like paragraphs, tables, lists, and structural elements like headings, page headers, and footers easily accessible.

For more information, see [Layout parser](https://docs.cloud.google.com/generative-ai-app-builder/docs/parse-chunk-documents#layout-parsing).

Feature

**Vertex AI Search: Generative answers performance improvements**

Generative answers have been updated with performance improvements.

  * Re-ranking for generative answers has been updated to decrease response latency. 
  * Detection of adversarial queries has been updated for improved accuracy.



## July 25, 2024

Feature

**Vertex AI Search: Domain verification (GA)**

Domain verification for advanced website indexing using domain association is Generally Available (GA). You can use domain association to associate your Vertex AI Search data store to the specified domain. This is useful when you're not the owner of the specified domain or when you don't have access to the Google Search console needed to verify the domain.

For more information, see [Verify website domains](https://docs.cloud.google.com/generative-ai-app-builder/docs/domain-verification).

## July 23, 2024

Change

**Vertex AI Search: Widget uses new method for generative answers**

The search widget now uses the search and answer methods together, instead of the older search with summaries for **Search with an answer** and the converse method for **Search with follow-ups**.

The answer method is expected to improve the quality of the results.

For general information about the answer method, see [Get answers and follow-ups](https://docs.cloud.google.com/generative-ai-app-builder/docs/answer).

## July 19, 2024

Feature

**Vertex AI Search: Multi-step retrieval for answer (GA)**

For the `answer` method, multi-step retrieval using multi-step (ReAct) reasoning is Generally Available (GA).

For information about this feature, see [Query rephrasing](https://docs.cloud.google.com/generative-ai-app-builder/docs/answer#query_rephrasing) and [Search and answer (specify maximum steps)](https://docs.cloud.google.com/generative-ai-app-builder/docs/answer#search-answer-max-steps).

## July 17, 2024

Feature

**Vertex AI Search: Evaluate search quality (Public Preview)**

Evaluate the search quality of your generic search applications using sample query sets. This lets you assess your search engine's performance, understand potential biases or shortcomings in ranking algorithms, and compare historical evaluation results to understand the impact of changes in your search configuration.

For more information, see [Evaluate search quality](https://docs.cloud.google.com/generative-ai-app-builder/docs/evaluate-search-quality). This feature is in Public Preview.

## July 15, 2024

Feature

**Vertex AI Search: Rotation of CMEK keys, which protect data stores (Private Preview)**

Customer-managed encryption keys (CMEK) for data stores associated with search apps can be rotated. 

Don't rotate keys for data stores associated with recommendations apps. Also, if you rely on analytics, don't rotate keys.

Key rotation is available in Private Preview. For information about rotating CMEK keys to protect Vertex AI Agent data stores, see [Customer-managed encryption keys](https://docs.cloud.google.com/generative-ai-app-builder/docs/cmek).

## July 10, 2024

Feature

**Vertex AI Search: Edit the schema for structured data on import (Public Preview)**

When you create a data store by importing structured data from BigQuery or Cloud Storage, you can review and edit the schema before you import the data. This saves time over the alternative method of importing the data first and subsequently editing the schema. 

This feature is available in Public Preview and applies to generic and media data stores. To try this feature for healthcare data stores, contact your Google account team and ask for access to the Private Preview.

Feature

**Vertex AI Search: Media app creation (Public Preview)**

Media data stores can be created directly from the Data Stores page. 

This is an alternative to the method where you create a media data store as part of the app creation workflow.

This feature is available in Public Preview.

Feature

**Vertex AI Search: Bring your own schema for media data stores (Public Preview)**

Previously, all media data stores had to follow a JSON schema for media predefined by Google. However, now you can use your own JSON schema for media data, provided that you map fields in your schema to the key properties: `category`, `media_available_time`, `media_duration`, `title`, and `uri`. 

This feature is in Public Preview.

## July 03, 2024

Breaking

**Vertex AI Search: On July 6, text-bison@001/answer_gen/v1 is discontinued**

As of July 6, 2024, model version `text-bison@001/answer_gen/v1` is discontinued.

If you specify `text-bison@001/answer_gen/v1` by name in your search requests, replace `text-bison@001/answer_gen/v1` with a newer model or with `stable`.

For more information, see [Answer generation model versions and lifecycle](https://docs.cloud.google.com/generative-ai-app-builder/docs/answer-generation-models).

Change

**Vertex AI Search: gemini-1.5-flash-001/answer_gen/v1 for answer generation**

Model version `gemini-1.5-flash-001/answer_gen/v1` is the stable model for generating answers in Vertex AI Search.

For more information, see [Answer generation model versions and lifecycle](https://docs.cloud.google.com/generative-ai-app-builder/docs/answer-generation-models).

Issue

**Vertex AI Search: You can't use the Folder option to upload structured data from Cloud Storage**

When creating a data store for structured or media data, you must use the **File** option when importing from a Cloud Storage bucket. Choosing the **Folder** option results in an error, "Schema preview failed. Requested entity was not found."

To work around this issue, use the **File** option and upload one file from the folder. After you've created the data store, import the folder contents from the **Documents** tab of the data store.

## July 01, 2024

Feature

**Vertex AI Search: Healthcare search using natural language query with generative AI answers (GA with allowlist)**

Healthcare data search using natural language query with generative AI answer is Generally Available to select Google customers (GA with allowlist).

For more information, see [Search using natural language query with generative AI answer](https://docs.cloud.google.com/generative-ai-app-builder/docs/search-hc-data#nl-search-genAI).

Feature

**Vertex AI Search: Filter search results by relevance (Public Preview)**

Each document returned by a search query is given an estimated level of relevance to the query. When you make a query through an API call, you can set a relevance threshold.

Setting a high relevance threshold can greatly reduce the number of documents returned by a query. You can experiment with low, medium, and high thresholds to find the right level for your users.

Filter by relevance is available in Public Preview.

For more information, see [Filter searches by document-level relevance](https://docs.cloud.google.com/generative-ai-app-builder/docs/filter-by-relevance).

## June 27, 2024

Feature

**Vertex AI Search: Connect BigQuery datasets to Vertex AI Search (Public Preview)**

You can create Vertex AI Search data stores that periodically sync with data in BigQuery datasets. You can choose how often you want to update your data stores: every day, every 3 days, or every 5 days.

Synchronizing BigQuery data to Vertex AI Search is available in Public Preview.

For more information, see [Import from BigQuery](https://docs.cloud.google.com/generative-ai-app-builder/docs/create-data-store-es#bigquery).

## June 24, 2024

Feature

**Vertex AI Search: Check ingested data quality for media recommendations (Public Preview)**

You can check the quality of your ingested data for media recommendations. 

By running the Public Preview `requirements:checkRequirement` method, you find out if your data store meets the minimum quality requirements for your recommendations app. If your data doesn't meet the minimum threshold for the key metrics for your model and objective, you receive a warning about the issues. Address the issues and rerun the check.

For more information, see [Check data quality for media recommendations](https://docs.cloud.google.com/generative-ai-app-builder/docs/check-media-data-quality).

## June 21, 2024

Feature

**Vertex AI Search: Answers with summaries and follow-ups (GA)**

The answer API improves on the search with summary and search with follow-ups features. For example, it better handles complex queries and provides customization of answer styles.

The answer API is Generally Available (GA). However, the multi-step retrieval functionality remains in Public Preview. 

For more information, see [Get answers and follow-ups](https://docs.cloud.google.com/generative-ai-app-builder/docs/answer).

Feature

**Vertex AI Search: Generate grounded answers (GA with allowlist)**

You can add system instructions as preambles to your prompts. System instructions govern the behavior of the model and modify the output accordingly. For example, you can add a persona to the generated answer or instruct the model to format the output text a certain way.

For more information, see [Generate grounded answers](https://docs.cloud.google.com/generative-ai-app-builder/docs/grounded-gen).

Feature

**Vertex AI Search: Add structured data for advanced website indexing (Public Preview)**

If advanced website indexing is enabled in your data store, you can use structured data, such as schema.org data, to enrich your indexing.

For more information, see [Use structured data for advanced site indexing](https://docs.cloud.google.com/generative-ai-app-builder/docs/add-website-metadata).

Feature

**Vertex AI Search: The answer method can skip irrelevant answers**

The answer method can be set to generate an answer only if at least one of the results is deemed relevant. 

If you choose to ignore low relevant content and if all the results are deemed irrelevant or almost irrelevant, then the answer method doesn't generate an answer. Instead, a fallback message replaces the answer.

For more information, see [Show only relevant answers](https://docs.cloud.google.com/generative-ai-app-builder/docs/answer#ignore-irrelevant-answers).

Change

**Vertex AI Search: The generated answer message doesn't contain the name field for synchronous and sessionless queries**

The name field is only included in the answer response for session queries and for asynchronous queries. These are stateful and context-aware queries. 

If a query is a synchronous and stateless query, the `name` field is no longer included in the generated `answer` message.

For more information about the answer method, see [Get answers and follow-ups](https://docs.cloud.google.com/generative-ai-app-builder/docs/answer).

Feature

**Vertex AI Search: Choose when to enable autocomplete**

You can choose to enable autocomplete as soon as possible instead of waiting a couple of days for sufficiently good autocomplete data. If you choose to make autocomplete available sooner, at first, you won't get suggestions for all queries and some suggestions might be of poor quality.

For more information, see **Enable autocomplete** in [Update autocomplete settings](https://docs.cloud.google.com/generative-ai-app-builder/docs/configure-autocomplete#update-autocomplete).

## June 14, 2024

Feature

**Vertex AI Search: Boost search results**

Boosting search results for media apps and for generic search apps that contain unstructured and website data is Generally Available.

For more information, see [Boost search results](https://docs.cloud.google.com/generative-ai-app-builder/docs/boost-search-results).

Feature

**Vertex AI Search: Specify a language code in search request (Public Preview)**

Setting a language code in a search query can improve the quality of the search results. Language codes in search queries are supported in Public Preview.

For information about the language code field in `search`, see the [`servingConfigs.search`](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/projects.locations.collections.dataStores.servingConfigs/search) method.

Feature

**Vertex AI Search: Set language codes for data stores (Public Preview)**

Setting a language code for a data store can improve the quality of the extractive segments and extractive answers returned in search results. Language codes for data stores are supported in Public Preview.

For information about the language code field for data stores, see the [DataStore resource](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/projects.locations.collections.dataStores#resource:-datastore).

## June 05, 2024

Feature

**Vertex AI Search: Generate grounded answers (GA with allowlist)**

Generating grounded answers is Generally Available to select Google Cloud customers (GA with allowlist).

As part of your Retrieval Augmented Generation (RAG) experience, generate grounded answers based on Google Search, inline text, or the content in your Vertex AI Search data store. You can generate answers in a single turn or over multiple turns. For more information, see [Generate grounded answers](https://docs.cloud.google.com/generative-ai-app-builder/docs/grounded-gen).

When you use Google Search as a grounding source, you connect your Gemini large language model (LLM) to the most up-to-date information on the internet. You must display a Google Search entry point when grounding with Google Search. For more information, see [Use Google Search entry point](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/multimodal/grounding-search-entry-points).

## May 31, 2024

Feature

**Vertex AI Search: Document ranking API (GA)**

The ranking API takes a list of documents and reranks those documents based on how relevant the documents are to a query. This is a stateless API that does not require you to index documents in advance.

The ranking API is Generally Available (GA).

For more information, see [Rank and rerank documents](https://docs.cloud.google.com/generative-ai-app-builder/docs/ranking).

## May 14, 2024

Feature

**Vertex AI Search: Check grounding (GA)**

The check grounding API is Generally Available (GA).

The check grounding API determines how grounded a piece of text is in a given set of facts. The API returns support scores and citations.

Filler and introductory statements can be deemed as not requiring attribution. No scores or citations are provided for those statements.

Additionally, as an experimental feature, the API also generates contradicting citations that show which facts contradict the text and how strongly.

For more information, see [Check grounding](https://docs.cloud.google.com/generative-ai-app-builder/docs/check-grounding) and the [`check`](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.groundingConfigs/check) API.

## April 29, 2024

Feature

**Vertex AI Search: Add structured data for advanced website indexing (Public Preview)**

If advanced website indexing is enabled in your data store, you can use structured data, such as Google-inferred page dates, `meta` tags, and PageMap content, to enrich your indexing.

For more information, see [Use structured data for advanced site indexing](https://docs.cloud.google.com/generative-ai-app-builder/docs/add-website-metadata) and [Example use case using a Google-inferred page date](https://docs.cloud.google.com/generative-ai-app-builder/docs/boost-search-results#predefined-date-example).

Feature

**Vertex AI Search: Order healthcare search results (Public Preview)**

When you search over FHIR resource types that contain unstructured text, you can order your search results according to their relevance to your query. For more information, see [Order healthcare search results](https://docs.cloud.google.com/generative-ai-app-builder/docs/order-hc-results).

Feature

**Vertex AI Search: Boost search results (Public Preview)**

Boosting search results for media apps and for generic search apps that contain unstructured and website data is available in Public Preview. For more information, see [Boost search results](https://docs.cloud.google.com/generative-ai-app-builder/docs/boost-search-results).

Feature

**Vertex AI Search: gemini-1.0-pro-002/answer_gen/v1 for answer generation**

Model version `gemini-1.0-pro-002/answer_gen/v1` is available for generating answers in Vertex AI Search. For more information, see [Answer generation model versions and lifecycle](https://docs.cloud.google.com/generative-ai-app-builder/docs/answer-generation-models).

## April 24, 2024

Change

**Vertex AI Agent Builder: Renamed in the console and documentation**

The Google Cloud console and the documentation at _cloud.google.com_ have been updated to show the current product name for Vertex AI Agent Builder. On the console, look for "Agent Builder".

You might see the old name (Vertex AI Search and Conversation) in some places—for example, in videos.

## April 09, 2024

Feature

**Vertex AI Search: Document chunking support for more search types (Public Preview)**

When document chunking is turned on for an unstructured data store, search summaries and search with follow-ups are supported in Public Preview. 

For information, see [Chunk documents for RAG](https://docs.cloud.google.com/generative-ai-app-builder/docs/parse-chunk-documents#parse-chunk-rag).

Feature

**Vertex AI Search: Connect Google Drive to Vertex AI Search (GA)**

Syncing Google Drive data to Vertex AI Search is available in GA. For more information about creating a Google Drive data store, see [Sync from Google Drive](https://docs.cloud.google.com/generative-ai-app-builder/docs/create-data-store-es#google-drive).

Feature

**Vertex AI Search: Document ranking API (Public Preview)**

The ranking API takes a list of documents and reranks those documents based on how relevant the documents are to a query. This is a stateless API that does not require you to index documents in advance. 

For more information, see [Rank and rerank documents](https://docs.cloud.google.com/generative-ai-app-builder/docs/ranking).

Feature

**Vertex AI Search: Check grounding (Public Preview)**

The check grounding API is available as a Public Preview feature.

The check grounding API determines how grounded a piece of text is in a given set of facts. Perfect grounding requires that every statement in the text can be attributed to one or more of the given facts. The API returns support scores and citations. 

Additionally, as an experimental feature, the API also generates contradicting citations that show which facts contradict the text and how strongly.

For more information, see [Check grounding](https://docs.cloud.google.com/generative-ai-app-builder/docs/check-grounding) and the [`check`](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/projects.locations.groundingConfigs/check) API.

Feature

**Vertex AI Search: Answers with summaries and follow-ups (Public Preview)**

The answer API improves on the search with summary and search with follow-ups features. For example, it better handles complex queries, can do multi-step retrieval, and provides customization of answer styles.

The answer API is supported in Public Preview.

For more information, see [Get answers and follow-ups](https://docs.cloud.google.com/generative-ai-app-builder/docs/answer).

Feature

**Vertex AI Search: Connect multiple search apps to the same data store (GA)**

Connecting more than one generic search app to a single data store is supported in GA. With this capability, you can create multiple apps that search across the same data without having to ingest that data multiple times.

Feature

**Vertex AI Search: Connect Spanner, Cloud SQL, Firestore, and Bigtable to Vertex AI Search (Public Preview)**

Importing data from Spanner, Cloud SQL, Firestore, and Bigtable to Vertex AI Search is available in Public Preview. For more information about creating a Google Drive data store, see [Create a search data store](https://docs.cloud.google.com/generative-ai-app-builder/docs/create-data-store-es).

Feature

**Vertex AI Search: FHIR data streaming ingestion (Private Preview)**

Select the import frequency for your healthcare FHIR data. You can either perform a one-time batch import or set up a streaming import. Streaming import is available as a Private Preview feature.

For more information, see [Create a healthcare search data store](https://docs.cloud.google.com/generative-ai-app-builder/docs/create-data-store-hc).

Feature

**Vertex AI Search: Blended search (GA)**

Blended search, where you can search across multiple data stores using a single search app, is available in GA. For more information about blended search, see [About connecting multiple data stores](https://docs.cloud.google.com/generative-ai-app-builder/docs/create-data-store-es#multi-data-stores).

Feature

**Vertex AI Search: Autocomplete support for healthcare search (Public Preview)**

Autocomplete is available as a Public Preview feature for healthcare data search. The autocomplete configuration uses a canonical medical data source to generate autocomplete suggestions for healthcare data stores.

For more information, see [Configure autocomplete](https://docs.cloud.google.com/generative-ai-app-builder/docs/configure-autocomplete).

Announcement

**Vertex AI Search: Media search (GA)**

Vertex AI Search for media is Generally Available (GA). 

You can create media search apps on media data stores. You can connect the media search app to an existing media data store or create a new one. You can also use document metadata to filter search queries of your media content.

Feature

**Vertex AI Search: Search-as-you-type for media apps**

Search results are returned after each character instead of after the full query is entered. Search-as-you-type is ideal for search apps with awkward input devices such as television remotes. You can enable search-as-you-type through the widget UI as well as through the API.

For more information, see [Get search-as-you-type results for a media app](https://docs.cloud.google.com/generative-ai-app-builder/docs/preview-search-results#media-search).

Feature

**Vertex AI Search: Additional languages supported for media search**

Vertex AI Search for media is supported in nine languages: Arabic, English, French, German, Hindi, Korean, Japanese, Portuguese, and Spanish. 

For more information, see [Languages](https://docs.cloud.google.com/generative-ai-app-builder/docs/languages-locales).

## March 28, 2024

Feature

**Vertex AI Search: Document chunking and parsing improvements (Public Preview)**

The following improvements have been introduced for document chunking and parsing:

  * Adjacent chunks: When returning chunks in search responses, you can return chunks from immediately before and after the relevant chunk in the source document. Doing so can improve context and accuracy.
  * Page span: Chunk metadata in search responses includes the span of pages where the chunk appeared in the source document.
  * List chunks: List all chunks from a specific source document.
  * Get chunks: Get a specific chunk.
  * Get processed documents in JSON: Get a parsed document or a chunked document in JSON format.
  * Bring your own chunks (Preview with allowlist): Upload data that you've already chunked. Contact your Google account team if you're interested in trying this feature.



For more information, see [Parse and chunk documents](https://docs.cloud.google.com/generative-ai-app-builder/docs/parse-chunk-documents).

Feature

**Vertex AI Search: Structured data stores (GA)**

Use of data stores containing structured data is Generally Available (GA). Additionally, two new field value types are allowed for structured data stores: `geolocation` and `datetime`.

For information about structured data stores, see [Structured data](https://docs.cloud.google.com/generative-ai-app-builder/docs/prepare-data#structured) in _Prepare for ingesting_ and [Schemas: auto-dectection versus providing you own](https://docs.cloud.google.com/generative-ai-app-builder/docs/provide-schema).

Feature

**Vertex AI Search: Extractive segments and relevance scores (GA)**

Extractive segments and relevance scores for extractive segments are GA.

For more information, see [Extractive segments](https://docs.cloud.google.com/generative-ai-app-builder/docs/snippets#extractive-segments).

Feature

**Vertex AI Search: Media recommendations analytics (GA)**

Analytics for media recommendations are GA. You can view analytics for your media recommendations apps in the Google Cloud console.

For more information, see [View analytics](https://docs.cloud.google.com/generative-ai-app-builder/docs/view-analytics).

Feature

**Vertex AI Search: Autocomplete updates**

Autocomplete is Generally Available (GA) for the US and EU multi-regions as well for the global region.

Autocomplete supports access transparency. This means that, when access transparency is enabled, if Google personal access your autocomplete data, this is recorded in the Access Transparency logs. 

For information about autocomplete, see [Configure autocomplete](https://docs.cloud.google.com/generative-ai-app-builder/docs/configure-autocomplete#feature-summary), and for information about Access Transparency, see [Enable Access Transparency in Vertex AI Search](https://docs.cloud.google.com/generative-ai-app-builder/docs/access-transparency).

Feature

**Vertex AI Search: Boost search results (Public Preview)**

Boosting search results using custom numerical attributes and according to freshness is available in Public Preview.

For more information, see [Boost search results](https://docs.cloud.google.com/generative-ai-app-builder/docs/boost-search-results).

## March 15, 2024

Feature

**Vertex AI Search: Sync from Google Drive (Preview with allowlist)**

Connecting to Google Drive as a data source for Vertex AI Search is available as a Preview with allowlist feature. For more information, see [Sync from Google Drive](https://docs.cloud.google.com/generative-ai-app-builder/docs/create-data-store-es#google-drive).

## March 12, 2024

Announcement

**Vertex AI Search: Vertex AI Search for healthcare (GA)**

Vertex AI Search for healthcare is Generally Available (GA). Healthcare search lets you query healthcare records stored in FHIR data stores. For more information, see [Vertex AI Search](https://docs.cloud.google.com/generative-ai-app-builder/docs/introduction#es-and-personalize). With healthcare search, you can:

  * [Create a healthcare search data store and import FHIR R4 data](https://docs.cloud.google.com/generative-ai-app-builder/docs/create-data-store-hc)
  * [Create a healthcare search app](https://docs.cloud.google.com/generative-ai-app-builder/docs/create-app-hc)
  * [Search healthcare data using keywords and natural language queries](https://docs.cloud.google.com/generative-ai-app-builder/docs/search-hc-data)
  * [Search healthcare data using natural language queries with generative AI answers](https://docs.cloud.google.com/generative-ai-app-builder/docs/search-hc-data#nl-search-genAI) (Private Preview)



Feature

**Vertex AI Search: Turn on document chunking (Public Preview)**

To use Vertex AI Search for retrieval-augmented generation (RAG) for LLMs, you can turn on document chunking when creating a data store. Document chunking is available in Public Preview.

When document chunking is turned on, your documents are split into chunks when you ingest documents into your data store, and your search app can return chunks of data in search results instead of full documents. Using chunked data for RAG increases relevance for LLM answers and reduces computational load for LLMs. Document chunking is in Public Preview. For more information, see [Chunk documents for RAG](https://docs.cloud.google.com/generative-ai-app-builder/docs/parse-chunk-documents#parse-chunk-rag).

Feature

**Vertex AI Search: Specify a parser for unstructured content (Public Preview)**

You can control how documents are parsed when they are uploaded to Vertex AI Search. Parser specification is available in Public Preview.

Vertex AI Search provides a digital parser (GA), an OCR parser for PDFs (Public Preview), and a layout parser (Public Preview). During data store creation for generic search apps with unstructured data, you can set a default parser for the data store and an override parser for specific file types.

For more information, see [Parse documents](https://docs.cloud.google.com/generative-ai-app-builder/docs/parse-chunk-documents#parsing).

Feature

**Vertex AI Search: Connect ServiceNow as a data source (Private Preview)**

You can connect ServiceNow as a third-party data source for Vertex AI Search. For more information, see [Connect a third-party data source](https://docs.cloud.google.com/generative-ai-app-builder/docs/connect-third-party-data-source).

## March 05, 2024

Feature

**Vertex AI Search: Watch time duration objective for media recommendations apps**

When you create a media recommendations app, you can select watch duration per session as a business objective. Optimizing for watch duration per session maximizes the duration of media consumption.

For more information, see [Watch duration per session](https://docs.cloud.google.com/generative-ai-app-builder/docs/about-media-recommendations-types#watch-duration).

## February 28, 2024

Feature

**Vertex AI Search: Add metadata to your web index (Public Preview)**

If advanced website indexing is enabled in your data store, you can add metadata to the data store schema to enrich your indexing.

For more information, see [Add metadata for advanced site indexing](https://docs.cloud.google.com/generative-ai-app-builder/docs/add-website-metadata).

Feature

**Vertex AI Search: Automatic web page refresh (Public Preview)**

With advanced website indexing, Vertex AI Search performs conditional, automatic refresh. 

For more information, see [Refresh web pages](https://docs.cloud.google.com/generative-ai-app-builder/docs/recrawl-websites).

Feature

**Vertex AI Search: Search analytics (GA)**

Search analytics are GA for global data stores. For data stores in US and EU multi-regions, viewing analytics is in Public Preview.

For more information, see [View analytics](https://docs.cloud.google.com/generative-ai-app-builder/docs/view-analytics).

Feature

**Vertex AI Search: Access controlled data sources (Public Preview)**

Access control for BigQuery, Cloud Storage, and Confluence data is available in Public Preview. This feature allows you to limit the data that users can view in your search app's results. Google uses your identity provider to identify the end user performing a search and determine if they have access to the documents that are returned as results. Google Identity and third-party identity provider federation are supported.

For more information, see [Use data source access control](https://docs.cloud.google.com/generative-ai-app-builder/docs/data-source-access-control).

Feature

**Vertex AI Search: Blended search (Public Preview)**

Blended search, where multiple data stores can be connected to a single generic search app, is available in Public Preview. This feature allows you to use one generic search app to search across multiple sources and types of data.

For more information, see [About connecting multiple data stores](https://docs.cloud.google.com/generative-ai-app-builder/docs/create-data-store-es#multi-data-stores).

Feature

**Vertex AI Search: Apply tuned search to some queries (Public Preview)**

You can specify whether you want a query to use the tuned search model or the non-tuned search model. This is particularly helpful for testing the difference between the two versions of the model. 

Previously, the tuned search model was enabled (or disabled) for all queries against the data store.

For more information, see [Test tuned search and use it for individual search queries](https://docs.cloud.google.com/generative-ai-app-builder/docs/tune-search#tune-search-test).

## February 26, 2024

Feature

**Vertex AI Search: Use Terraform to create search apps**

You can use Terraform to create search apps for your Vertex AI Search. 

For information, see [Create a search app](https://docs.cloud.google.com/generative-ai-app-builder/docs/create-engine-es).

## February 15, 2024

Feature

**Vertex AI Search: Stable Gemini Pro answer generation model**

`gemini-pro@001/answer_gen/v1` is available as a stable, Generally Available model for answer generation. For information about all available models for answer generation, see [Specify the summarization model](https://docs.cloud.google.com/generative-ai-app-builder/docs/get-search-summaries#summary-model).

## January 31, 2024

Feature

**Vertex AI Search and Conversation: Use Terraform to create data stores**

You can use Terraform to create data stores for your Vertex AI Search and Conversation apps. The data stores are created empty; you then ingest the data through the console or an API call.

For information, see, for example, [Create a search data store](https://docs.cloud.google.com/generative-ai-app-builder/docs/create-data-store-es).

Feature

**Vertex AI Search: Gemini Pro for search summaries**

You can now choose Gemini Pro as a model for generating search summaries.

For more information, see [Specify the summarization model](https://docs.cloud.google.com/generative-ai-app-builder/docs/get-search-summaries#summary-model).

Feature

**Vertex AI Search: Check grounding in Preview with allowlist**

The CheckGrounding API determines how grounded a piece of text is in a given set of facts. Perfect grounding requires that every statement in the text can be attributed to one or more of the given facts. The API returns an overall score of 0 to 1, indicating how grounded the text is, along with citations to the appropriate given facts for each statement.

See [Check grounding](https://docs.cloud.google.com/generative-ai-app-builder/docs/check-grounding).

Feature

**Vertex AI Search: CMEK for US and EU is GA**

Customer-managed encryption keys (CMEK) are available in the US and the EU as GA with allowlist.

If you store your data in a US or EU multi-region data store, you can provide your own encryption key to protect your data at rest.

For information, see [Customer-managed encryption keys](https://docs.cloud.google.com/generative-ai-app-builder/docs/cmek).

Feature

**Vertex AI Search: Updates to autocomplete**

  * Autocomplete is available for your search apps in the US and EU multi-regions as Public Preview.

See [Configure autocomplete](https://docs.cloud.google.com/generative-ai-app-builder/docs/configure-autocomplete).

  * Autocomplete removes unsafe and offensive terms in eight languages in addition to English (`en`).

For more information, see [Autocomplete features](https://docs.cloud.google.com/generative-ai-app-builder/docs/configure-autocomplete#feature-summary).




## December 21, 2023

Feature

**Vertex AI Search: Access controlled data sources in Preview with allowlist**

Access control for BigQuery, Cloud Storage, and Confluence data is available in Preview with allowlist. This feature allows you to limit the data that users can view in your search app's results. Google uses your identity provider to identify the end user performing a search and determine if they have access to the documents that are returned as results. Google Identity and third-party identity provider federation are supported.

See [Use data source access control](https://docs.cloud.google.com/generative-ai-app-builder/docs/data-source-access-control).

Feature

**Vertex AI Search: Bring your own parsed documents in Preview with allowlist**

Importing pre-parsed unstructured documents into Vertex AI Search data stores is available in Preview with allowlist. For example, instead of importing a raw PDF document, you can parse the PDF yourself and import the parsing result instead. This lets you to import your documents in a structured way, ensuring that search and answer generation have full information about the document's layout and elements.

See [Bring your own parsed document](https://docs.cloud.google.com/generative-ai-app-builder/docs/create-data-store-es#bring-parsed-document). For more information, contact your Google account team.

Change

**Vertex AI Search: User events joined with documents asynchronously for generic apps**

For generic search and recommendation apps, user events are joined with their associated documents asynchronously. For media apps, user events continue to be joined synchronously.

For more about user event import, see [Import historical user events](https://docs.cloud.google.com/generative-ai-app-builder/docs/import-user-events).

## December 13, 2023

Feature

**Vertex AI Search: Media search (Preview with allowlist)**

You can create media search apps on media data stores. You can connect the media search app to an existing media data store or create a new one. You can also use document metadata to filter search queries of your media content.

Media search is available as a Preview with allowlist capability. To use this capability, contact your Google account team.

See [About media documents and data stores](https://docs.cloud.google.com/generative-ai-app-builder/docs/media-documents) and [Filter media search](https://docs.cloud.google.com/generative-ai-app-builder/docs/filter-media-search).

Feature

**Vertex AI Search: Support for Access Transparency is GA**

[Access Transparency](https://docs.cloud.google.com/assured-workloads/access-transparency/docs/overview) supports Vertex AI Search in GA.

See [Enable Access Transparency in Vertex AI Search](https://docs.cloud.google.com/generative-ai-app-builder/docs/access-transparency).

Feature

**Vertex AI Search: Search tuning (Public Preview)**

Search tuning is available as a Public Preview feature. You can upload additional training data to tune the model for your search app.

For information, see [Improve search results with search tuning](https://docs.cloud.google.com/generative-ai-app-builder/docs/tune-search).

Feature

**Vertex AI Search: Blended search (Preview with allowlist)**

Blended search, where multiple data stores can be connected to a single generic search app, is available in Preview with allowlist. This feature allows you to use one generic search app to search across multiple sources and types of data.

See [About connecting multiple data stores](https://docs.cloud.google.com/generative-ai-app-builder/docs/create-data-store-es#multi-data-stores).

Feature

**Vertex AI Search: Use multiple serving configs for media recommendations apps**

For media recommendations apps, you can create, edit, and delete serving configs. Serving configs contain recommendation demotion and diversity configurations that are used when generating results. When you make recommendations calls to a media app, you can specify different serving configs to get different levels of demotion and diversity in recommendations from the same app.

For more information, see [Create and manage serving configs](https://docs.cloud.google.com/generative-ai-app-builder/docs/serving-configs).

Feature

**Vertex AI Search: OCR processing (Public Preview)**

OCR processing is available in Public Preview. If you have non-searchable PDFs (scanned PDFs or PDFs with text inside images), you can turn on optical character recognition (OCR) processing during data store creation. This allows Vertex AI Search to extract elements such as text blocks and tables. If you instead have searchable PDFs that contain many tables, you might also consider turning on OCR processing with `useNativeText` set to `true` and `enhancedDocumentElements` set to `table`.

See [OCR processing for PDFs](https://docs.cloud.google.com/generative-ai-app-builder/docs/create-data-store-es#ocr-processing).

Feature

**Vertex AI Search: Filter search with follow-ups**

You can filter your queries for search with follow-ups, both for website data and for structured data with metada.

See [Filter search with follow-ups](https://docs.cloud.google.com/generative-ai-app-builder/docs/multi-turn-search#filter-search-with-follow-ups).

Feature

**Vertex AI Search: Company name field for search apps**

When you create a search app, you supply the name of your company or organization. This can improve the quality of the responses for summarization and search with follow-ups.

See [Create a search app](https://docs.cloud.google.com/generative-ai-app-builder/docs/create-engine-es).

Feature

**Vertex AI Search: Citations with metadata for summaries (Public Preview)**

When citations are turned on for summaries, the response includes citation metadata. This includes metadata about the sources that are being referenced and information about which sources apply to specific sentences in the summary.

See [Get citations](https://docs.cloud.google.com/generative-ai-app-builder/docs/get-search-summaries#get-citations).

Feature

**Vertex AI Search: Upgrade to advanced website indexing**

You can update an existing data store to advanced website indexing.

See [Turn on advanced website indexing](https://docs.cloud.google.com/generative-ai-app-builder/docs/turn-on-advanced-indexing).

Feature

**Vertex AI Search: Additional languages supported**

The search, snippets, and extractive answers features are supported in 25 languages. 

Summarization is supported in most languages. 

See [Languages](https://docs.cloud.google.com/generative-ai-app-builder/docs/languages-locales).

Feature

**Vertex AI Search: Customized Summaries is GA**

Customized summaries are available in GA. For search with answers and search with follow-ups, you can provide free-form natural-language instructions to customize the summaries that are returned with your results. Customize summaries through the console for search widget results and through the API for other search requests.

For more information, see [Get customizable summaries](https://docs.cloud.google.com/generative-ai-app-builder/docs/get-search-summaries#customizable-summaries).

Feature

**Vertex AI Search: Estimate the size of your web data**

You can call an API to get an estimate of the size of your web data prior to importing it into a data store. With this information, you can estimate your monthly storage costs using the Vertex AI Search and Conversation pricing page or the Google Cloud Pricing Calculator.

See [Estimate the size of your web data](https://docs.cloud.google.com/generative-ai-app-builder/docs/estimate-size-web-data).

## November 15, 2023

Feature

**Vertex AI Search: Autocomplete denylist (Preview with allowlist)**

Importing an autocomplete denylist is available as a preview with allowlist feature. To use this feature, contact your Google account team.

For information about autocomplete denylists, see [Use an autocomplete denylist](https://docs.cloud.google.com/generative-ai-app-builder/docs/configure-autocomplete#denylist).

## November 14, 2023

Feature

**Vertex AI Search: Additional languages supported**

Extractive answers are now supported in the following languages: 

  * Arabic
  * Chinese (Simplified)
  * Japanese



See [Languages](https://docs.cloud.google.com/generative-ai-app-builder/docs/languages-locales).

## November 09, 2023

Change

**Vertex AI Search: New model for search summarization**

A better model for generating search summaries has been launched. This underlying model improves the quality of search summaries and their grounding in the provided document corpus. You might see some differences in summary output after this update.

For more information about search summaries, see [Get search summaries](https://docs.cloud.google.com/generative-ai-app-builder/docs/get-search-summaries).

Change

**Vertex AI Search: Confidence scores are changed to relevance scores (Preview with allowlist)**

Confidence scores are renamed to relevance scores. Scores are returned in the `relevanceScore` field. Previously, they were returned in the `confidenceScore` field. 

This feature is in preview with allowlist. For more information about relevance scores, see [Get snippets and extracted content](https://docs.cloud.google.com/generative-ai-app-builder/docs/snippets).

## November 06, 2023

Feature

**Vertex AI Search: Multi-region support for US and EU locations is GA**

The US multi-region and the EU multi-region APIs are Generally Available (GA).

For more information about multi-regions including limitations, see [Vertex AI Search locations](https://docs.cloud.google.com/generative-ai-app-builder/docs/locations).

## October 27, 2023

Feature

**Vertex AI Search: Create media recommendations in Vertex AI Search**

You can now create apps for media recommendations in Vertex AI Search. Media recommendations include content such as videos, news, and music. For more information, see [Vertex AI Search](https://docs.cloud.google.com/generative-ai-app-builder/docs/introduction#es-and-personalize).

**Important:** If you are using Discovery for Media for media recommendations, you need to switch to the media recommendations capability of Vertex AI Search. All of the existing data and models that you created with Discovery for Media will automatically appear in the Vertex AI Search and Conversation console, with the models appearing as apps. For more information, see [Migrate from Discovery for Media to media recommendations](https://docs.cloud.google.com/generative-ai-app-builder/docs/migrate-from-discovery-for-media).

## October 13, 2023

Feature

**Vertex AI Search: Customer-managed encryption key integration for the EU**

Customer-managed encryption keys (CMEK) is available in the EU as an allowlisted preview feature.

If you store your data in an EU multi-region data store, you can provide your own encryption key to protect your data at rest. 

For information, see [Customer-managed encryption keys](https://docs.cloud.google.com/generative-ai-app-builder/docs/cmek).

## October 09, 2023

Change

**Vertex AI Search and Conversation: Renamed in the console and documentation**

The Google Cloud console and the documentation at _cloud.google.com_ have been updated to show the current product name for Vertex AI Search and Conversation. On the console, look for "Search and Conversation".

You might see the old name (Generative AI App Builder) in some places—for example, in the API reference.

## September 29, 2023

Announcement

**Vertex AI Search (Enterprise Search): VPC Service Controls are GA**

Virtual Private Cloud Service Controls support for Enterprise Search is Generally Available (GA). 

For more information, see [Supported products and limitations](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_gen_app_builder_es) in the _VPC Service Controls_ documentation. For general information about VPC Service Controls, see [Overview of VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview).

Feature

**Vertex AI Search (Enterprise Search): Search tuning**

Search tuning is available as an allowlisted preview feature. You provide additional training data in the form of query and segment pairs. We use this data to tune the model for your app.

For information, see [Improve search results with search tuning](https://docs.cloud.google.com/generative-ai-app-builder/docs/tune-search).

Feature

**Vertex AI Search (Enterprise Search): Data location**

Vertex AI Search may be configured for data location pursuant to the "Data Location" section of the [Service Specific Terms](https://cloud.google.com/terms/service-terms).

For information about data residency in Vertex AI Search, see [Enterprise Search locations](https://docs.cloud.google.com/generative-ai-app-builder/docs/locations).

Feature

**Vertex AI Search (Enterprise Search): Customer-managed encryption key integration**

Customer-managed encryption keys (CMEK) is available as an allowlisted preview feature.

If you store your data in a US multi-region data store, you can provide your own encryption key to protect your data at rest. 

For information, see [Customer-managed encryption keys](https://docs.cloud.google.com/generative-ai-app-builder/docs/cmek).

Feature

**Vertex AI Search (Enterprise Search): Additional languages supported**

Search, snippets, and other features are now supported in the following languages: 

  * Arabic
  * Chinese (Simplified)
  * Greek
  * Hebrew
  * Japanese
  * Korean
  * Polish
  * Russian



See [Languages](https://docs.cloud.google.com/generative-ai-app-builder/docs/languages-locales).

Feature

**Vertex AI Search (Enterprise Search): Support for Access Transparency**

[Access Transparency](https://docs.cloud.google.com/assured-workloads/access-transparency/docs/overview) supports Vertex AI Search in preview.

For more information, see [Enable Access Transparency in Enterprise Search](https://docs.cloud.google.com/generative-ai-app-builder/docs/access-transparency).

Feature

**Vertex AI Search (Enterprise Search): Citations for search with follow-ups**

Citations indicate from which search results specific sentences in the summary are taken.

For more information, see [Configure the summary](https://docs.cloud.google.com/generative-ai-app-builder/docs/multi-turn-search#configure_the_summary).

Feature

**Vertex AI Search (Enterprise Search): Ignore adversarial queries and non-summary seeking queries for search with follow-ups**

Ignore adversarial queries can stop generation of summaries that are unsafe or violate policy. 

Non-summary seeking queries stop generation of summaries that aren't helpful for some queries.

For more information, see [Configure the summary](https://docs.cloud.google.com/generative-ai-app-builder/docs/multi-turn-search#configure_the_summary).

## September 22, 2023

Feature

**Vertex AI Search (Enterprise Search): Third-party data connectors**

You can set up your Vertex AI Search data stores to sync with data from Jira, Confluence, or Salesforce.

This feature is in private preview. To try this feature, contact your Google account team to find out if you qualify.

For more about setting up a connection to third-party data, see [Create an Enterprise Search data store](https://docs.cloud.google.com/generative-ai-app-builder/docs/create-data-store-es).

## September 20, 2023

Feature

**Manually refresh your web pages**

Call the `recrawlUris` method to manually refresh specific web pages in a data store with Advanced website indexing turned on. You can check the status of the recrawl operation by polling the `operations.get` method.

See [Manually refresh your web pages](https://docs.cloud.google.com/generative-ai-app-builder/docs/recrawl-websites).

## September 19, 2023

Change

**Vertex AI Search (Enterprise Search): Turn Enterprise edition on or off**

You can turn Enterprise edition features on or off for existing apps.

For more about Enterprise edition, see [About advanced features](https://docs.cloud.google.com/generative-ai-app-builder/docs/about-advanced-features).

## September 15, 2023

Feature

**Vertex AI Search (Enterprise Search): Adjacent segments for preview with allowlist**

When getting extractive segments, you can also get up to 3 segments from immediately before and after the relevant segment. Adjacent segments can add context and accuracy to the relevant segment. Turning on adjacent segments can increase latency. 

Adjacent segments is in preview with allowlist. Contact your Google account team to try out adjacent segments.

See [Extractive segments](https://docs.cloud.google.com/generative-ai-app-builder/docs/snippets#extractive-segments).

Feature

**Vertex AI Search (Enterprise Search): Customizable summaries for preview with allowlist**

When you request summaries, you can customize them by providing natural-language instructions. You can request customizations such as such as the length and level of detail, style of output (such as "simple"), language of output, focus of answer, and format (such as tables, bullets, and XML).

Customizable summaries are in preview with allowlist. Contact your Google account team if you're interested in trying this feature. 

See [Get customizable summaries](https://docs.cloud.google.com/generative-ai-app-builder/docs/get-search-summaries#customizable-summaries).

Feature

**Vertex AI Search (Enterprise Search): Languages for summarization**

Summarization is supported in the following languages in addition to English: 

  * German (`de-DE`)
  * Spanish (`es-ES`)
  * Italian (`it-IT`)
  * French (`fr-FR`)
  * Dutch (`nl-NL`)
  * Portuguese (`pt-BR`)
  * Swedish (`sv-SE`)



See [Languages](https://docs.cloud.google.com/generative-ai-app-builder/docs/languages-locales).

Announcement

**Vertex AI Search (Enterprise Search): ISO compliance**

Vertex AI Search meets ISO 27001, ISO 27017, ISO 27018, and ISO 27701 compliance standards.

See [Compliance and security controls](https://docs.cloud.google.com/generative-ai-app-builder/docs/compliance-security-controls#certifications).

## September 08, 2023

Feature

**Vertex AI Search (Enterprise Search): Page numbers for extractive segments**

Page numbers can be returned with extractive segments. Page numbers indicate where an answer was extracted from in a document.

For more about extractive segments, see [Get snippets and extracted content](https://docs.cloud.google.com/generative-ai-app-builder/docs/snippets).

Announcement

**Vertex AI Search (Enterprise Search): Image search is GA**

Image search is now Generally Available (GA).

See [Search for images using a website search engine](https://docs.cloud.google.com/generative-ai-app-builder/docs/image-search).

## August 29, 2023

Announcement

**Vertex AI Search and Conversation** is the new product name for _Generative AI App Builder_.

Announcement

**Generative AI App Builder: GA**

Gen AI App Builder is publicly and Generally Available (GA).

Change

**Separation of data stores and apps**

Data stores and apps are separate entities. In the console, you can see your apps on the **Apps** page and your data stores on the **Data Stores** page. You can create a data store and attach it to an app during app creation, or create a new data store during app creation.

Apps and data stores have a one-to-one relationship. Each app is associated with one data store; they can't be disconnected after you attach them. This change does not affect the functionality of your existing apps.

Feature

**Enterprise Search: Multi-region support for US and EU locations**

When you create a data store, you can specify global, the US multi-region, or the EU multi-region.

For more information including limitations associated with multi-region use, see [Enterprise Search locations](https://docs.cloud.google.com/generative-ai-app-builder/docs/locations).

Feature

**Enterprise Search: Search with follow-ups is GA**

Previously, the search with follow-ups feature was called multi-turn search.

Search with follow-ups is now Generally Available (GA).

Search with follow-ups can be applied to websites if advanced website indexing is enabled and to unstructured data.

In addition, to improve consistency between search with an answer and search with follow-ups, the response from the `conversations.converse` method [v1](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/ConverseConversationResponse) provides the `summary` object and no longer provides the `reply` and `references` objects. The response from the [v1beta](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/ConverseConversationResponse) version of the method remains unchanged.

SafeSearch is available with the search with follow-ups feature.

For general information about search with follow-ups, see [Search with follow-ups](https://docs.cloud.google.com/generative-ai-app-builder/docs/multi-turn-search).

Feature

**Enterprise Search: Serving controls using the API are allowlisted GA**

Boost, filter, synonym, and redirect serving controls affect search results returned through API method calls. 

For more information, see [Configure serving controls](https://docs.cloud.google.com/generative-ai-app-builder/docs/configure-serving-controls).

Feature

**Enterprise Search: Languages**

More features in more languages are supported for Enterprise Search. 

See [Languages](https://docs.cloud.google.com/generative-ai-app-builder/docs/languages-locales).

Feature

**Enterprise Search: Verify website domains**

New requirement to verify your domain ownership for any websites in your data stores with advanced website indexing turned on.

See [Verify website domains](https://docs.cloud.google.com/generative-ai-app-builder/docs/domain-verification).

Feature

**Enterprise Search: Improvements to snippets, extractive answers, and extractive segments**

  * Snippet **status** is now returned along with the snippet.

  * Extractive answers include the document **page number** where the answer was found. 

  * Up to **10** extractive segments can be returned for a search result.




See [Get snippets and extracted content](https://docs.cloud.google.com/generative-ai-app-builder/docs/snippets).

Feature

**Enterprise Search: Confidence scores**

Confidence scores for extractive segments are available in preview with allowlist. Scores are based on the similarity of the query to the extracted segment.

See [Extractive segments](https://docs.cloud.google.com/generative-ai-app-builder/docs/snippets#extractive-segments).

Feature

**Enterprise Search: Related questions**

Related questions are available as an allowlisted, preview feature for search with follow-ups. 

For information, see [Related questions](https://docs.cloud.google.com/generative-ai-app-builder/docs/multi-turn-search#related_questions).

## August 18, 2023

Feature

**Enterprise Search: Multi-turn, conversational search UI**

Multi-turn, conversational search from within the Google Cloud console is available in preview. 

For information, see [Configure search results for unstructured data](https://docs.cloud.google.com/generative-ai-app-builder/docs/configure-widget-attributes#display-unstructured) and [Search with multi-turn](https://docs.cloud.google.com/generative-ai-app-builder/docs/multi-turn-search).

Feature

**Enterprise Search: Languages**

Search results and snippets are supported in:

  * Danish (`da-DK`) 
  * Dutch (`nl-NL`) 
  * Hindi (`hi-IN`) 
  * Portuguese (`pt-BR`) 
  * Swedish (`sv-SE`) 



Search results and snippets are also supported in English (`en-US`), French (`fr-FR`), Spanish (`es-ES`), German (`de-DE`), and Italian (`it-IT`). 

For more information, see [Languages](https://docs.cloud.google.com/generative-ai-app-builder/docs/languages-locales).

## August 09, 2023

Feature

**Enterprise Search: Support for VPC Service Controls**

VPC Service Controls supports Enterprise Search in preview. 

For more information, see [Supported products and limitations](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_gen_app_builder_es) in the _VPC Service Controls_ documentation. For general information about VPC Service Controls, see [Overview of VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview).

## August 04, 2023

Change

**Enterprise Search: Summaries are GA**

Summaries for searches are now Generally Available (GA). These are a short summarization of the top one or more search results returned in a search response. 

For more information, see [Get search summaries](https://docs.cloud.google.com/generative-ai-app-builder/docs/get-search-summaries).

Feature

**Enterprise Search: Languages**

Search and snippets results are supported in French (`fr-FR`), in addition to English (`en-US`), Spanish (`es-ES`), German (`de-DE`), and Italian (`it-IT`). 

For more information, see [Languages](https://docs.cloud.google.com/generative-ai-app-builder/docs/languages-locales).

Change

**Enterprise Search: Ignore adversarial and non-summary seeking queries are GA**

The Ignore adversarial and non-summary seeking queries features are now Generally Available (GA). 

For more information, see [Ignore adversarial queries](https://docs.cloud.google.com/generative-ai-app-builder/docs/get-search-summaries#ignore-adversarial-queries) and [Ignore non-summary seeking queries](https://docs.cloud.google.com/generative-ai-app-builder/docs/get-search-summaries#ignore-non-summary-seeking-queries).

Change

**Enterprise Search: Citations are GA**

Summary citations are now Generally Available (GA). Citations indicate from which search results specific sentences in the summary are taken.

For more information, see [Get citations](https://docs.cloud.google.com/generative-ai-app-builder/docs/get-search-summaries#get-citations).

## August 02, 2023

Feature

**Enterprise Search: Use custom embeddings**

Bringing your own custom vector embeddings to Enterprise Search is supported in preview. If you've created your own embeddings on your data, you can upload them to Enterprise Search and use them when querying.

For more information, see [Use custom embeddings](https://docs.cloud.google.com/generative-ai-app-builder/docs/bring-embeddings).

## July 20, 2023

Feature

**Enterprise Search: Citations**

Summary citations are now available in preview. Citations indicate from which search results specific sentences in the summary are taken.

For more information, see [Get citations](https://docs.cloud.google.com/generative-ai-app-builder/docs/get-search-summaries#get-citations).

Feature

**Enterprise Search: Ignore adverserial and non-summary seeking queries**

You can now configure search requests so that adversarial queries and non-summary seeking queries do not include a summary in the response. This feature is in preview.

For more information, see [Ignore adversarial queries](https://docs.cloud.google.com/generative-ai-app-builder/docs/get-search-summaries#ignore-adversarial-queries) and [Ignore non-summary seeking queries](https://docs.cloud.google.com/generative-ai-app-builder/docs/get-search-summaries#ignore-non-summary-seeking-queries).

Change

**Enterprise Search: Personalize**

We have renamed the "Personalize" feature of Generative AI App Builder to "Recommendations". This is a naming change only. There is no change to product functionality.

## July 10, 2023

Breaking

**Enterprise Search: Snippets no longer provide page numbers**

Snippets are returned as brief extracts of text of uniform length. They no longer provide page numbers. If you previously used snippets as inputs for large language models to generate responses and summaries, we recommend using extractive answers or extractive segments. If you need page numbers in your extracts, we recommend using extractive answers, which provide page numbers where available.

Feature

**Enterprise Search: Languages**

Search and snippets results are supported in English (`en-US`), Spanish (`es-ES`), German (`de-DE`), and Italian (`it-IT`). 

For more information, see [Languages](https://docs.cloud.google.com/generative-ai-app-builder/docs/languages-locales).

Feature

**Enterprise Search: Snippets with hit highlighting**

Snippets in search responses are available with hit highlighting for rendering in UIs.

For more information, see [Use snippets and extracted content](https://docs.cloud.google.com/generative-ai-app-builder/docs/snippets).

## June 30, 2023

Feature

**Enterprise Search: Extractive answers**

Extractive answers are available in preview. An extractive answer is verbatim text that is returned with each search result. This text is extracted directly from the search result document and is typically displayed near the top of web pages to provide an end user with a brief answer that is contextually relevant to their query. 

For more information, see [Use snippets and extracted content](https://docs.cloud.google.com/generative-ai-app-builder/docs/snippets).

Feature

**Enterprise Search: Image search**

Search for images on your website. Provide an image (Base64 encoded PNG, JPG, or BMP) as the query and use an API method to return similar images. 

For more information, see [Search for images using a website search engine](https://docs.cloud.google.com/generative-ai-app-builder/docs/image-search).

Feature

**Enterprise Search: OCR processing**

Optical character recognition (OCR) processing is available, improving parsing and segmentation of PDF files at data ingestion. This enables Gen App Builder to take into account structures such as paragraphs and tables when ingesting your documents, providing more accurate search results, snippets, and summarizations. To request this functionality, contact your Google Cloud account team.

For more information, see [OCR processing](https://docs.cloud.google.com/generative-ai-app-builder/docs/prepare-data#ocr_processing).

Feature

**Enterprise Search: Extractive segments**

Extractive segments are available in preview. An extractive segment is verbatim text that is returned with each search result and is usually more verbose than an extractive answer. Extractive segments can be displayed as an answer to a query and be used in post-processing tasks and as input for large language models to generate answers or new text. 

For more information, see [Use snippets and extracted content](https://docs.cloud.google.com/generative-ai-app-builder/docs/snippets).

## June 05, 2023

Breaking

**Enterprise Search: Specify domains for the widget**

To use the widget externally, you must provide a list of domains where the widget appears.

If, in an earlier version, you created a widget with API key authentication, that widget might not be supported. 

To ensure that the widget continues working, you must reconfigure it: Follow the instructions on [Add the widget to a webpage](https://docs.cloud.google.com/generative-ai-app-builder/docs/add-widget) to specify one or more domains for your widget and to generate a fresh snippet for the widget.

Change

**Enterprise Search: No API keys**

Generated API keys are no longer used by the widget. You can enable Public Access instead.

Feature

**Personalize**

Like Enterprise Search and Infobot, Personalize is a component of Gen App Builder. With Personalize, you build a state-of-the-art recommendation engines based on your own data. The recommendation engine uses AI to suggest documents that are similar to the document that the user is currently viewing.

Personalize is available in preview.

For information, see [Get started with Personalize](https://docs.cloud.google.com/generative-ai-app-builder/docs/try-personalize).

Feature

**Enterprise Search: Multi-turn search**

Multi-turn search is available in allowlisted preview. Multi-turn search enables follow up questions in context. For information, see [Search with multi-turn](https://docs.cloud.google.com/generative-ai-app-builder/docs/multi-turn-search).

Feature

**Enterprise Search: PPTX, DOCX, and TXT formats**

Enterprise Search supports search over PPTX, DOCX, and TXT documents as well as HTML and PDF documents. Support for the PPTX, DOCX, and TXT formats is available in preview.

For general information about unstructured data, see [Unstructured data](https://docs.cloud.google.com/generative-ai-app-builder/docs/prepare-data#unstructured).

Feature

**Enterprise Search: Purge data**

The addition of the **Purge Data** button on the **Documents** page makes it easier to delete data from a data store. For information, see [Delete data from a data store](https://docs.cloud.google.com/generative-ai-app-builder/docs/delete-datastores).

Feature

**Enterprise Search: Collect feedback from users**

You have the option to collect feedback (thumbs up or thumbs down) about the quality of the search results provided through the widget. Users who don't like the results can also select, from a list, the reason for their dislike. Feedback collection is available in preview.

For information about feedback collection, see [Configure widget feedback](https://docs.cloud.google.com/generative-ai-app-builder/docs/configure-feedback).

Feature

**Enterprise Search: Schema editing**

Schemas for structured data stores can be viewed and updated from within the Google Cloud console. Schema editing is available in preview.

For information about schema viewing and editing, see [View the schema definition for structured data](https://docs.cloud.google.com/generative-ai-app-builder/docs/get-schema-definition), [Update a schema for structured data](https://docs.cloud.google.com/generative-ai-app-builder/docs/update-schemas), and [Schemas: auto-detecting versus providing your own](https://docs.cloud.google.com/generative-ai-app-builder/docs/provide-schema).

Feature

**Enterprise Search: Analytics**

On the analytics dashboard, you can compare metrics for two time periods. The analytics dashboard is available in preview.

For information, see [View analytics](https://docs.cloud.google.com/generative-ai-app-builder/docs/view-analytics).

Feature

**Enterprise Search: HIPAA compliance**

Enterprise Search is ready to support [HIPAA](https://docs.cloud.google.com/security/compliance/hipaa) compliance.

Fixed

**Enterprise Search: Re-import after changing the indexable setting on a field**

It is no longer necessary to re-import data after changing an indexable field setting. See [Configure search attributes](https://docs.cloud.google.com/generative-ai-app-builder/docs/configure-search-attributes).

## April 28, 2023

Feature

**Enterprise Search: Purge data**

The addition of the `documents.purge` method makes it easier to delete data. For information, see [Delete data from a datastore](https://docs.cloud.google.com/generative-ai-app-builder/docs/delete-datastores).

Feature

**Enterprise Search: Image search**

Search for images on your website. Provide a text string as the query and use an API method to return images. For information, see [Search for images using a website search engine](https://docs.cloud.google.com/generative-ai-app-builder/docs/preview-search-results#api-image-website).

Feature

**Enterprise Search: Advanced autocomplete**

_Experimental feature:_ The advanced autocomplete document data model uses Google's large language models to generate high-quality autocomplete suggestions. For information, see [Experimental: Advanced autocomplete document data model](https://docs.cloud.google.com/generative-ai-app-builder/docs/configure-autocomplete#experimental_advanced_autocomplete_document_data_model).

## April 14, 2023

Feature

**Enterprise Search**

Search engines for unstructured data can be created through the Google Cloud console. For information, see [Console instructions: Create a search engine and ingest unstructured data](https://docs.cloud.google.com/generative-ai-app-builder/docs/create-datastore-ingest#console-create-ingest-unstructured).

## March 29, 2023

Announcement

Generative AI App Builder is available for preview to those on the allowlist.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
