---
url: https://docs.cloud.google.com/generative-ai-app-builder/docs/about-media-recommendations-types/
title: About media app recommendations types \u00a0|\u00a0 Agent Search \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:35:20.044037+00:00
---

# About media app recommendations types  |  Agent Search  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/generative-ai-app-builder/docs/about-media-recommendations-types/

**Note:** Vertex AI Search is being renamed to Agent Search. We are in the process of updating content to reflect the new branding. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Search ](https://docs.cloud.google.com/generative-ai-app-builder/docs)



Send feedback 

#  About media app recommendations types Stay organized with collections  Save and categorize content based on your preferences. 

This page describes the recommendations types that are available when you [create a media recommendations app](https://docs.cloud.google.com/generative-ai-app-builder/docs/create-app-media), including the business objectives, context event types, and other customizations that are available with each recommendations type.

## Recommendations types

The following recommendations types are available with media recommendations apps:

  * Others You May Like
  * Recommended for You
  * More Like This
  * Most Popular



### Others You May Like

The Others You May Like recommendations type recommends the next document that a user is most likely to engage with. The recommendation is based on the user's engagement history and the current context document.

**Default optimization objective:** click-through rate

**Default serving config:** N/A

**Available customizations:**

  * Business objective



**Supported pages for app deployment:**

  * Detail page. For more information, see the [`view-item`](https://docs.cloud.google.com/generative-ai-app-builder/docs/media-user-events#view-item) and [`media-play`](https://docs.cloud.google.com/generative-ai-app-builder/docs/media-user-events#media-play) events.



**User event requirements:**

  * `view-item` or `media-play` for click-through rate objective

  * `media-complete` and either `media-play` or `view-item` for conversion rate objective and watch duration per session objective




### Recommended for You

The Recommended for You recommendations type predicts the next document that a user is most likely to engage with based on the engagement history of that user. This recommendations type is typically used on the home page.

If you use Recommended for You on the home page, select Home Page Context as the context event type for the app. Home Page Context can deliver better performance because it uses additional usage signals that are not available with the Generic option. Only use the Generic option if you don't have `view-home-page` events.

**Default optimization objective:** click-through rate

**Default context event type:** Home page context

**Default serving config:** N/A

**Available customizations:**

  * Business objective

  * Context event type




**Supported pages for app deployment:**

  * All. On category pages, you must provide filter tags.



**User event requirements:**

  * `view-item` or `media-play` for click-through rate objective. For home page context, `view-home-page` is also required.

  * (`media-play` or `view-item`) and `media-complete` for conversion rate objective and watch duration per session objective. For home page context, `view-home-page` is also required.




### More Like This

The More Like This recommendations type recommends media that is similar to a context item and is likely to be engaged with next by a viewer of the context item. More Like This is based on the context item and the aggregate viewing history of all users who viewed the context item. A More Like This app is typically used on detail pages or on the home page with a fixed context item.

The More Like This recommendations type uses a variety of factors to determine how similar two media documents are, including the [categories](https://docs.cloud.google.com/generative-ai-app-builder/docs/media-documents#key-properties) field of the media documents. For best results, media documents that are similar should have overlapping categories—for example, `["Action", "Comedy"]` categories are somewhat similar to `["Action", "Thriller"]`, but not similar to `["Drama"]`.

**Default optimization objective:** click-through rate

**Default serving config:** N/A

**Available customizations:**

  * Business objective



**Supported pages for app deployment:**

  * Detail page

  * Home page (requires a context item)




**User event requirements:**

  * `view-item` or `media-play` for click-through rate objective

  * (`media-play` or `view-item`) and `media-complete` for conversion rate objective and watch duration per session objective




### Most Popular

The Most Popular recommendations type recommends media that has been most popular among all users in recent days. The recommendation is based on the watching or viewing history of all users. You can customize the time window to check the popularity of the documents.

**Default optimization objective:** click-through rate

**Default serving config:** N/A

**Available customizations:**

  * Business objective

  * Time window. Specify the time window in days to check the popularity of documents in the last _X_ days.




**Supported pages for app deployment:**

  * Home page



**User event requirements:**

  * `view-item` or `media-play` for click-through rate objective

  * `media-complete` for conversion rate objective




**Limitations:**

  * Most Popular doesn't support customizing serving configs or creating multiple serving configs

  * Most Popular doesn't support filtering based on categories




## Optimization for business objectives

The machine learning models that underlie media recommendation apps are created to optimize for a particular business objective, which determines how the model is built.

After you have trained an app (which is training the underlying model), you cannot change the optimization objective. You must train a new app to use a different optimization objective.

Recommendations for Media supports the following optimization objectives.

### Click-through rate (CTR)

Optimizing for CTR emphasizes engagement. You should optimize for CTR when you want to maximize the likelihood that the user interacts with the recommendation.

CTR is the default optimization objective for the Others You May Like and Recommended for You recommendations types.

### Conversion rate (CVR)

Optimizing for conversion rate maximizes the likelihood that the user consumes the content up to the conversion threshold defined in the app.

The conversion threshold can be specified in seconds or percentage. For example, if the conversion threshold is set to 25% and the user watches at least 25% of the program, then the conversion objective is met.

### Watch duration per session

Optimizing for watch duration per session maximizes the duration of media consumption. This objective uses information from clicks, conversions, and watch duration derived from `media-complete` user events in order to recommend items that have a higher probability of being watched longer than others.

When logging user events, make sure that the `mediaProgressDuration` is non-negative and is correctly logged in `media-complete` events in the last 90 days.

The watch duration per session objective is available for Others You May Like, Recommended for You, and More Like This recommendation types.

## What's next

  * [Create a media app and a data store](https://docs.cloud.google.com/generative-ai-app-builder/docs/create-app-media)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
