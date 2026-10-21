---
url: https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/features/
title: Features and capabilities of AI Commerce Search \u00a0|\u00a0 AI Commerce Search in Gemini Enterprise for Customer Experience \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:38:55.408727+00:00
---

# Features and capabilities of AI Commerce Search  |  AI Commerce Search in Gemini Enterprise for Customer Experience  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/features/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ AI Commerce Search ](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search)



Send feedback 

#  Features and capabilities of AI Commerce Search Stay organized with collections  Save and categorize content based on your preferences. 

Within the AI Commerce Search product, you get both the recommendations capability and the search and browse capability. You can upload and manage product catalog information and user event logs for your ecommerce applications. You can get and customize results based on this information, and this data continues to be used to train and update models, thus improving your recommendations and search results.

For more information about the process of implementing AI Commerce Search for your application, see [Implementing AI Commerce Search](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/overview).

## Recommendations

AI Commerce Search lets you build high quality, personalized product recommendation systems without requiring a high level of expertise in machine learning, systems design, or operations. Leveraging your site's retail products and user behavior, you can use recommendations to build recommendation models specific to your use case, such as "Frequently Bought Together" and "Recommended for You".

AI Commerce Search uses user events and your product catalog to train your [recommendation machine learning models](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/models), which provide recommendations based on this data.

When you deploy recommendation models to your application, you can then request recommendations for other products in your catalog and display to your users.

Recommendations capabilities include:

  * **Custom models**. Each model is trained specifically for your data, based on sequence-based machine learning models using transformers.

  * **Personalized results**. Use personalization algorithms without any machine learning expertise. Recommendations are based on user behavior and activities like views, clicks, and in-store purchases as well as online activity, so that every prediction result is personalized.

  * **Real-time predictions**. Each recommendation served considers previous user activity like click, view, and purchase events, so recommendations are in real time.

  * **Automatic model training and tuning**. Daily model retraining ensures all the models can accurately capture user behavior every day.

  * **Optimization objectives**. Goals like conversion rate, click-through rate, and revenue optimization help you precisely optimize for your business goal.

  * **Omnichannel recommendations**. With the API model, go beyond website recommendations to personalize your entire shopper journey to recommendations on mobile apps, personalized email recommendations, store kiosks, or call center applications.




## Search

AI Commerce Search lets you provide high quality product search results that are customizable for your retail business needs. Use Google's query and contextual understanding to improve product discovery across your website and mobile applications.

Search capabilities include:

  * **Product hierarchies** : You can include collections and variants in your searchable product catalog.

  * **Query expansion** : Increase the relevant results returned for query terms that would normally produce fewer results, such as queries that use very specific keywords.

  * **Relevance thresholding** : Adjust how AI Commerce Search balances returning precision (the relevance of the search results returned) and recall (returning more results for that query).

  * **Pagination** : Control pagination of your search results to decrease lookup time and response size.

  * **Filtering** : Use expression syntax to provide filtering that refines your site's search results.

  * **Ordering** : Set the order of search results by multiple fields in order of priority.

  * **Faceting** : Generate faceting to provide more relevant options to your users based on attributes you provide. Buckets need to be provided for numerical attributes in the search request to return them in the search response.

  * **Dynamic faceting** : Automatically generate facet keys based on search queries and automatically combine (and rerank) with facet keys provided in the search request. This feature is based on an allowlist. Contact support for help enabling this feature.

  * **Boosting and burying** : Control search result ranking by prioritizing or deprioritizing some types of results.

  * **Browsing** : Get results that are sorted to maximize revenue when your users browse products using site navigation. Browse search can be combined with filtering, ordering, faceting, dynamic faceting, boosting, and burying.

  * **Personalized results**. Deliver personalized text search and browse search results that are personalized for each end-user, based on each user's behavior on your site, including each user's history of product views, clicks, add to cart, and purchases.




## Use AI Commerce Search

In order to build machine learning models for recommendations or search, you need to supply two sets of information:

  * **Product catalog:** Information about the products being recommended to customers. This includes the product title, description, in-stock availability, and pricing.

  * **User events:** End user behavior on your website. This includes events such as when a user views or purchases a specific item, or when your website shows the user a list of products.




With many integration options, you can ingest your data using tools you might already use, such as BigQuery, Cloud Storage, Tag Manager, and Google Analytics.

**Important:** AI Commerce Search processes data on your behalf. It is your responsibility to ensure that the data you send to AI Commerce Search is collected in accordance with applicable laws.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
