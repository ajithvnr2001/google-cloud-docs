---
url: https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/search-vs-recommendations/
title: Search and browse \u00a0|\u00a0 AI Commerce Search in Gemini Enterprise for Customer Experience \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:39:02.305472+00:00
---

# Search and browse  |  AI Commerce Search in Gemini Enterprise for Customer Experience  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/search-vs-recommendations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ AI Commerce Search ](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search)



Send feedback 

#  Search and browse Stay organized with collections  Save and categorize content based on your preferences. 

This document aims to clarify the distinctions between search and browse functionalities within AI Commerce Search in order to explore how to configure each effectively and get more out of them.

## Understand the core differences

While search and browse help customers find products, they cater to different user journeys and require distinct configurations.

### Search

Driven by user intent, where a shopper enters a specific query, such as _red running shoes._ AI Commerce Search analyzes this query to understand the user's needs and returns relevant products optimized for revenue.

In short, for search, AI Commerce Search is responsible for the relevance of products and its ranking (**revenue optimized**).

### Browse

Guided by predefined categories, where a shopper navigates through product listings organized by attributes like brand, category, or promotions, such as **Shirts** in the **Men's Clothing** category. You define these categories, displaying products in them.

You're responsible for the relevance of products listed (through filters), and AI Commerce Search is responsible for its ranking (revenue-optimized).

## Configure search and browse

The beauty of AI Commerce Search lies in its unified API for both search and browse requests.

### Configure search

User events for search should have these fields, along with other standard mandatory fields for user events (`eventType = "search"`):

  * **Text query** : The core of a search request. It captures the user's search intent.
  * **Filters (Optional)** : Allow users to refine search results by applying facets like brand, price range, or color.
  * **Ranking and Personalization** : AI Commerce Search automatically optimizes the ranking of search results based on relevance and potential revenue. Personalization further tailors results based on individual user behavior.

**Note:** These examples represent request structures as would pass to configuration dictionary methods using the Python client libraries.
    
    
      # Construct the search request
      search_request = {
          "query": "red running shoes", # User's search query
          "filter": "brand:ANY('Nike')", # Optional filter
          "page_size": 10 # Number of results per page
      }
    
    
    
    # Send the request to the VAIS:Commerce API
      search_response = client.search(search_request)
    
    
    
    
    
    # Process the search results
      for product in search_response.results:
          print(product.title, product.price)
      

For basic querying with search, including text query searches, browse searches, pagination, optimization, and personalized results, refer to [Get search results](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/search-basic).

### Configure browse

User events for browse searches must have these fields, along with other standard mandatory fields for user events (`eventType = "search"` for browse events):

  * **Page categories** : `page_categories` represents the category or banner under which products appear. Although, in physical client libraries or older APIs, this field might still appear as the singular `page_category`. The plural can optionally be the same as `categories[]` in the catalog. It just must represent the category that the filter represents.

  * **Compulsory filter** : Defines the criteria for products to be included in the browse results. This ensures only relevant products appear in the category.

  * **Alignment between event and request** : The user event corresponding to the browse action should contain the same `page_categories` and filter values matching what was passed in the API request.

  * **Browse and filter set with the same value** : To set the `pageCategories` (browse) and `attributes.pageCategories` (filter) fields with the same value, create a non-searchable `attributes.pageCategories` object, and list every page this product should appear in to facilitate filtering.


**Note:** The catalog's `categories[]` field is designed to provide the overall taxonomy. It's normally a read-only attribute meant for model training (e.g., structure for VAIS:Commerce models) and _is not for filtering_ in browse requests. While the `categories[]` field can hold multiple values, it avoids holding purely flat, unrelated values. It's meant to represent valid hierarchies.

For browse filters, fields like `category` or `categoryid`, as shown in these examples, are typically custom attributes that you provide.

Here are the aforementioned four examples of different browse request options. (Just choose one format.).

**Note:** These examples represent request structures as would be passed to configuration dictionary methods using the Python client libraries.
    
    
      # a browse request with a custom category attribute
      browse_request = {
          "page_categories": ["Men's > Clothing > Shirts"], # Represents full taxonomy Path on the site
          "filter": "category:ANY('Shirts') AND gender: ANY('Male')", # Compulsory filter on custom attribute
          "page_size": 10
      }
      # a browse request showing category ID (Men's shirts custom id)
      browse_request = {
          "page_categories": ["Men's > Clothing > Shirts"],
          "filter": "categoryid:ANY(1234)", # Another custom attribute for categories
          "page_size": 10
      }
      # another example showing category ID's (Men's shirts custom id)
      browse_request = {
          "page_categories": ["1234"],  # Also ok to use unique category id's here
          "filter": "categoryid:ANY(1234)",
          "page_size": 10
      }
      # browse and filter set with the same value
      browse_request = {
          "page_category": ["Men's > Clothing > Shirts"], # Browse category
          "filter": "attributes.pageCategories:ANY('Men's > Clothing > Shirts')", # Compulsory filter
          "page_size": 10 # Number of results per page
      }
      # Send the request to the API
      browse_response = client.search(browse_request)
      # Process the browse results
      for product in browse_response.results:
          print(product.title, product.price)
      

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
