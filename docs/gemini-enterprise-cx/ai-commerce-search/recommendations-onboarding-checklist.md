---
url: https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/recommendations-onboarding-checklist/
title: Recommendations onboarding checklist \u00a0|\u00a0 AI Commerce Search in Gemini Enterprise for Customer Experience \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:11:48.350811+00:00
---

# Recommendations onboarding checklist  |  AI Commerce Search in Gemini Enterprise for Customer Experience  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/recommendations-onboarding-checklist/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ AI Commerce Search ](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search)



Send feedback 

#  Recommendations onboarding checklist Stay organized with collections  Save and categorize content based on your preferences. 

This guide for recommendations onboarding provides instructions to optimize product recommendations and increase user engagement. It outlines catalog data checks to ensure data accuracy and consistency, serving logs checks to monitor performance, serving config checks to verify configurations, and user event checks to track and measure user interactions. 

Click each item in the checklist to reveal more detailed information about how to proceed. Check off each onboarding step after you have completed it. By following these steps, you can improve the overall effectiveness of your recommendations implementation. 

****

###  Catalog data checks

### Attribute data

  * **Attribute filtering limits** : Given the attribute filtering limit of 10, prioritize the selection of the most important attributes. Analyze patterns in selected custom attributes and add similar, relevant ones to the catalog. Ensure high coverage for attribute filter keys in the catalog to enable effective filtering and refine recommendations.

  * **Maximize impact of attributes** : Don't delete or disable attributes because it might affect the model. Improve coverage for auto-selected attributes by filling in these fields for more products.

  * **Check attribute settings** : Recommendations use filterable attribute settings that can be used in recommendation filter expressions. This control is applicable only for text attributes.




### Categories

Monitor category distribution and address categories with excessive representation. High-quality product categories enable rule-based diversity to recommend products from a variety of categories.

### Out-of-stock ratio

Maintain a low out-of-stock ratio (ideally < 90%) to avoid skewing recommendations and ensure relevant results. If you have the majority of products as `OUT_OF_STOCK` (OOS), the predict response would have many OOS products, and on adding a filter, the recall numbers will reduce. Keep the `Product.availability` field as up-to-date as possible using the `patchProduct` APIs or import APIs with a `readMask`.

### Variants and primary details

Ensure both primary and variant products have complete and accurate details. Consider the product's SKU structure and designate products as primaries or variants accordingly. Prioritize the accuracy and completeness of `product.categories`, `product.title`, `product.attributes`, and `product.prices` for both primary and variant products.

Make sure to think carefully when determining which products or groups of products are primary and which are variants.

Primaries and variants are sometimes described as parent and child items.

### Price on primary and variants

Accurately populate price information for both primary and variant products to ensure accurate recommendations and filtering. If the product doesn't have product-level pricing, and all the pricing is always tied to a local inventory, then fill the median price information of all the inventory level pricing at the product level price info.

### Data upload frequency

Be aware that the model picks up new product information approximately every six hours.

Ideally, you should update the catalog should regularly (hourly or daily or better preferably real time) using periodic catalog imports to prevent model quality from decreasing over time.

During peak events like BFCM, ensure your data ingestion pipeline can handle rapid price changes across the entire catalog.

### Inconsistent uploads per branch

Ensure consistent product uploads across branches to avoid missing product information for some queries, which can worsen model quality.

Import data to different branches as a way to stage and preview recommendations or predict results.

###  Serving config checks

### Balance between filters and diversity settings

Optimize the balance between the number of filters applied and diversity settings. Use data-driven diversity to produce recommendations results that balance relevance and diversity. Data-driven diversity learns from product catalog metadata, such as titles or categories.

Adjust prediction results based on product category by setting `diversityLevel` to values such as `RULE_BASED_DIVERSITY`, `DATA_DRIVEN_DIVERSITY`, `no-diversity`, `low-diversity`, `medium-diversity`, `high-diversity`, or `auto-diversity`.

  * `RULE_BASED_DIVERSITY` diversifies recommendation results based on product category.
  * `DATA_DRIVEN_DIVERSITY` diversifies recommendations based on learning from product metadata to balance relevance and category diversity.



### Price reranking parameters

Adjust prediction results based on product price by using the `priceRerankLevel` parameter, with options for no, low, medium, or high price reranking.

Allowed values are `no-price-reranking` (default value if unset), `low-price-reranking`, `medium-price-reranking`, and `high-price-reranking`.

###  User events checks

### Bad filter data in user events

Ensure multi-word filters in user events match the catalog exactly, including capitalization (**OnePiece** versus **One-Piece**).

Accurate filter use is crucial for optimal dynamic facet performance. The model infers facet popularity from filters present in predict requests.

### Events requirements

For all event types (per model type), ensure a sufficient number of events.

Make sure that ingested events are _attributable_ , which means the timestamps, visitor ID, and product ID details should be accurate for the model to train. This means, the model should be able to construct a user journey from the events.

Check the event requirement per model type in the documentation or in the AI Commerce Search in Gemini Enterprise for Customer Experience at the time of model creation.

### Average impression per product

For all event types (per model type), aim for an average impression per product ID greater than 10. One to two weeks of detailed page views can be enough to start training Others You May Like and Recommended for You models.

### Purchase average order size

Ensure the purchase average order size is greater than one, excluding item quantity, whenever applicable. Don't flatten multi-item baskets into multiple purchase events. Keep them as single purchase events that include multiple products.

Check that some purchase events include multiple products as this helps the model learn co-purchase patterns, especially for models like Frequently Bought Together.

###  Recommendation response handling

### API Responses: search and recommendations differ

A key distinction in AI Commerce Search is how the Search and Recommendations APIs handle product variants in their responses. Understanding this difference is vital for implementation.

Search responses include specific product variants; recommendations responses don't.

  * **Search** : When a user submits a query (such as _red running shoes size 10_), the API returns a list of primary products and details for the top five matching variants. The user's query provides the necessary context to identify and rank the most relevant variants.
  * **Recommendations** : The response for models like Frequently Bought Together or Recommended for You intentionally returns only primary product IDs. These recommendations are broad and lack a specific user query to guide variant selection.



This design gives developers the flexibility to implement their own variant selection logic. Because there is no guiding query, you control which variant gets displayed based on your own business rules, such as showing the best-seller, the variant with the highest inventory, or one that is on promotion. This intentional design ensures the final recommendation aligns with your specific ecommerce strategy.

###  Personalization requirements

Personalized models like Recommended for You or Others you may like are most effective when they adapt to a user's immediate actions. The key to this responsiveness lies in how user interaction data, or events, are processed.

  * **Real-time personalization:** This approach leverages a continuous stream of user events, such as clicks or additions to a cart. By ingesting these events in real time, recommendation models can instantly tailor their output to a user's most recent interests. This ensures the suggestions are always fresh and highly relevant.
  * **Model training vs. personalization:** It's important to distinguish between the core model and the personalization layer. 
    * **Model training:** The underlying recommendation model in AI Commerce Search typically retrains daily, learning from all historical data.
    * **Real-time personalization:** This happens on top of the trained model. With each API call, it computes fresh, personalized recommendations that incorporate user events that have occurred in the last few minutes.
  * **The ingestion method matters:** The speed of personalization is directly tied to how you ingest user events. 
    * **Real-time ingestion:** This is crucial for instant personalization. If your business needs to capitalize on in-the-moment user intent, prioritizing a real-time event stream is essential.
    * **Batch ingestion:** Using a batch process will introduce a delay to personalization, equivalent to your batch schedule's frequency. While not inherently bad, it's a critical trade-off to consider based on your business requirements.



###  Model placement guide

The effectiveness of AI-powered product recommendations hinges on their strategic placement. Positioning the right model on the right page is critical for maximizing user engagement and achieving key business metrics. This guide offers proven strategies for placing AI Commerce Search models, while emphasizing the flexibility needed to meet your unique business goals.

### Core recommendation models and placements

AI Commerce Search offers specialized models for different shopping contexts. This table summarizes our primary models and their recommended placements for maximum impact.

Ecommerce page | Primary Goal | Best model for page | Alternative model 1 | Alternative model 2  
---|---|---|---|---  
Product Detail Page | Surfacing similar or alternative items | Others you make like | Frequently Bought Together | Similar Items  
Home page / Category page | Personalized discovery | Recommended for you | Buy it again | On Sale  
Shopping Cart page | Increasing average order value | Frequently Brought together | Recommended for you | On Sale  
  
  * **Recommended for You** : Creates a personalized experience by leveraging a user's historical data. Its placement on the Home Page or Category Pages immediately engages returning customers with tailored suggestions.
  * **Others You May Like** : Ideal for Product Detail Pages, this model presents similar or alternative items to the product being viewed. A key tool for driving product discovery, it can be optimized for click-through rate (CTR) or revenue.
  * **Frequently Bought Together** : Designed to increase AOV by suggesting complementary products. It's most effective on Product Detail Pages and within the cart or checkout flow, where it prompts logical add-on purchases.



### A/B test for data-driven decisions

While these guidelines provide a strong foundation, A/B testing is essential to validate the optimal strategy for your specific audience. You can, for example, test whether Others You May Like or Frequently Bought Together performs better on your Product Detail Pages by serving each model to a different user cohort.

By tracking key performance indicators like conversion rates and revenue for each group, you can make data-driven decisions on which model to deploy. This empirical approach eliminates guesswork and ensures your placement strategy is finely tuned to your business objectives.

### Balance guidelines with business needs

Consider these recommendations as a starting point. The flexibility of AI Commerce Search allows for customizations to meet specific strategic goals. However, for businesses without a pre-existing placement strategy, these tried-and-tested guidelines provide a reliable path to success. By thoughtfully placing your models and continuously refining your approach through testing, you can unlock a more engaging and profitable ecommerce experience.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
