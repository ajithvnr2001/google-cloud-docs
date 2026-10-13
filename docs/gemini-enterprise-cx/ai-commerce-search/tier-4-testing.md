---
url: https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/tier-4-testing/
title: Starter A/B checklist \u00a0|\u00a0 AI Commerce Search in Gemini Enterprise for Customer Experience \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:39:05.168201+00:00
---

# Starter A/B checklist  |  AI Commerce Search in Gemini Enterprise for Customer Experience  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/tier-4-testing/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ AI Commerce Search ](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search)



Send feedback 

#  Starter A/B checklist Stay organized with collections  Save and categorize content based on your preferences. 

This 17-point checklist for monitoring AI Commerce Search A/B tests details item checks for visitor or user ID distribution, API/event data consistency, and experiment lane integrity. Each item describes what's monitored and explains the potential impact on A/B test accuracy and AI Commerce Search model training. 

Proper data attribution, consistent user identification, and accurate event tracking achieve reliable results and optimal model performance. Issues can cause skewed metrics, biased comparisons, and corrupted training data. Such results hinder informed decisions and search improvement.

## Before you begin

Refer to the [General guidance on conducting A/B experiments](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/a-b-testing).

## Test components

The starter A/B checks incorporate these test components:

**Visitor ID** : Required for tracking a visitor on a device, regardless of login state. It shouldn't change, whether the visitor logs in or out. If the user does sign in between user journeys, the visitor ID remains constant.

**Session ID** : For tracking a visitor's interaction session. Defined as an aggregation of user behavior in a time span, typically ending after 30 minutes of inactivity.

**User ID** : Highly recommended, persistent identifier for a logged-in user (like a customer ID) that's used across devices for personalization. It should always be a hashed value.

**Attribution token** : A hash token returned in every search response. Attribution tokens are unique, regardless of whether the search query parameters matched precisely. 

****

###  Count unique visitor ID distribution across lanes

### Description

This check involves verifying that the number of unique visitor IDs is randomly split between the control and test groups in an A/B experiment.

The visitor ID is a unique identifier for a user on a single device.

### Impact

An unfair split of visitor IDs can historically cause measurement errors in A/B testing.

If one experiment arm contains a disproportionate number of certain types of visitors, such as a bot visitor sending high volumes of probing traffic, it can negatively impact the metrics for that arm. This skews key performance indicator comparisons and affects measurement heavily but not directly on model training.

###  Count of unique user ID distribution across lanes

### Description

This check ensures that the number of unique user IDs, which represents a signed-in user, is evenly distributed between the control and test groups. The user ID should remain consistent across devices.

### Impact

The impact is similar to visitor ID. If logged-in users are not randomly assigned between test and control lanes, it can lead to a biased demographic split.

  * If, for example, the experimental group contains predominantly new users while high spenders remain in the control group, the metrics will appear artificially favored for one side.

  * This affects measurement and key performance indicator (KPI) comparisons.




###  Power user (visitor ID with more purchases) distribution

### Description

This check specifically looks at the distribution of users with high transaction counts or repeat purchases, often identified by their visitor IDs and purchase history, across the experiment lanes.

The goal is to ensure that these high-spending users are evenly split.

### Impact

  * An uneven distribution of power users, who contribute significantly to revenue, can heavily skew KPI comparisons between the experiment groups.
  * Debugging biases based on demographic information like spending habits can be complex.
  * This disproportionately affects revenue-based metrics like Revenue Per Visitor (RPV) or Revenue Per Session.
  * Emphasize the impact on measurement accuracy during A/B testing.



###  Number of unique AI Commerce Search token to search events token (apply this to browse if needed)

### Description

This check verifies that the attribution token returned in the search response is correctly included in search event that resulted from that search.

The attribution token is required for AI Commerce Search to link events back to the search that generated them:

  * This is typically relevant for traffic served by AI Commerce Search.
  * This issue also indicates possibility of search response caching, which will degrade the search performance and user experience due to stale inventory and outdated ranking.



### Impact

Proper attribution using the token is crucial for linking user behavior, including clicks and purchases, to specific search API calls. Without the token, search events might be incorrectly used as if they were from another search provider, and subsequent events cannot be accurately linked to the search.

Inaccurate or missing attribution tokens disrupt model training, because it is used to link event data (like searches followed by purchases) to generate positive and negative examples to train the ranking model. It also prevents the accurate computation of per-search metrics, such as revenue per search, which are vital for evaluating performance during A/B experiments.

This affects both model training and measurement and performance analysis.

###  Match visitor ID and user ID in the AI Commerce Search and search events (appy this to browse if needed)

### Description

This check ensures that the visitor ID and user ID used in a search request call to the Search API is the same visitor ID and user ID included in the subsequent search user event (if possible to detail-page-view, add-to-cart, and purchase-complete events, that are related to that search interaction).

  * The `visitorId` and `userId` fields, respectively, is a unique identifier for a user on a single device.
  * Consistent formatting of visitor and use ID across search requests and user events is necessary for search to identify user activity correctly.
  * Debugging approaches can involve using the visitor ID and user ID to trace interactions.



### Impact

A mismatch indicates potential issues like missing events or corrupted data.

The visitor ID and user ID are crucial for AI Commerce Search model training, particularly for personalization features. Accurate purchase attribution relies on the consistent use of a visitor ID and a user ID.

AI Commerce Search uses the visitor ID to link search results seen by a user to whether that same visitor ID later purchased a shown product. It is used to link search-to-click, add-to-cart, or purchase data to generate positive and negative examples for training the ranking model.

If the visitor ID does not match, it leads to a breakage where purchase events cannot be attributed to the search or detail page view that preceded them, making it look as if no search has a follow-up purchase. Not only does this disrupt model training, it also makes it difficult to compute per-search metrics like revenue per search. Another challenge lies in accurately calculating key performance indicators (KPIs) such as revenue per visitor, conversion rate, and average order value, which rely on accurately linking user events to searches. So this check affects both model training and measurement.

###  Query count match between Search API and events (apply this to browse if needed)

### Description

This check compares the volume of search requests made to the Search API for a specific experiment lane (particularly the Google lane) with the volume of search user events recorded for that same lane.

The expectation is that the number of search events collected should closely match the number of search API calls made.

### Impact

  * A significant mismatch indicates that user events are not being properly collected or sent to Google.
  * This can be caused by event ingestion issues (missing or incomplete events) or incorrect tagging of user events with the experiment ID.
  * Proper user event collection is essential because user interactions captured in events provide the model with the necessary feedback to optimize results.
  * If events are missing, the model receives less data for training, which can negatively impact its performance.
  * The accuracy and reliability of metrics used for evaluating A/B tests (like click-through rate, conversion rate, revenue metrics) depend entirely on the completeness and correctness of the user event data.
  * Missing events mean these metrics cannot be accurately computed, leading to skewed performance analysis and unreliable A/B test results.
  * A mismatch in query counts between API calls and events affects both model training and measurement.



###  Filters match between Search API and search events, both joined by token and overall (apply this to browse if needed)

### Description

This check verifies that when a user applies filters to search results (reflected in the search request), the corresponding search user event, linked by the attribution token, also includes the correct filter information.

This check involves verifying consistency for specific token-linked pairs, as well as verifying the overall consistency of filter data present in events as compared to API calls.

### Impact

  * Including filter statements in search events is required to use dynamic facets.
  * The AI Commerce Search model deduces facet popularity from the filters present in search requests, which is crucial for optimal dynamic facet performance.
  * If filter data is missing or incorrect in the user events, the model's ability to learn from user interactions involving filters is impaired.
  * This directly impacts the training and effectiveness of features like dynamic faceting.
  * This check is also useful for debugging issues related to search results, conversational search, and dynamic facets.
  * While the primary impact is on model training specifically for dynamic facets and related features, it also affects the ability to accurately debug and measure the performance of these specific functionalities.
  * Affects model training related to dynamic facets and is important for debugging and performance analysis (measurement) of features relying on filter data.



###  Offset and order by match between Search API and search event, both joined by token and overall (apply this to browse if needed)

### Description

  * This check verifies that the pagination parameters (offset) and sorting criteria (order by) included in a search request made to the Search API are correctly represented in the corresponding search user event.
  * These events are typically linked to the original request using the attribution token.
  * The check ensures consistency for specific token-linked interactions and overall data sent in events.
  * Maintaining this consistency in event data is important for debugging user journeys that involve pagination or sorting and for features like conversational search and dynamic facets.



### Impact

  * A mismatch hinders the ability to accurately analyze how users interact with search results under specific pagination or sorting conditions.
  * This impacts debugging efforts for these features and makes it difficult to assess their performance accurately (affecting measurement of features like conversational search or dynamic faceting performance).
  * Consistent event data is foundational for model training, and inconsistencies could indirectly affect insights derived from user behavior analysis under varying display conditions.
  * The consistency of request parameters and event values is noted as important for the performance of click-based reranking models.
  * **This primarily impacts debugging and measurement of specific features** and, to some extent, the model training effectiveness tied to understanding user interaction with paginated or sorted results.



###  Visitor ID switching experiment lanes

### Description

  * This check ensures that a unique visitor ID (used for non-logged-in users) remains assigned to a single experiment group or lane, meaning the control or test, throughout the A/B test period.
  * A consistent visitor assignment is expected unless there is a planned change like traffic ramping or explicit reshuffling.
  * Detecting switches means a single user, identified by their visitor ID, is unexpectedly moving between experiment groups.
  * This can stem from issues like improper event sending, incorrect experiment ID tagging in events, frontend implementation problems, or misconfigured search traffic routing.



### Impact

  * Consistent site visitor assignment is crucial for a fair A/B test.
  * If a site visitor switches lanes, their user events (clicks, add-to-carts, purchases) might be recorded under different experiment IDs, making it impossible to accurately attribute their overall behavior to a single experience. This corrupts the data used for calculating key performance indicators (KPIs) for each lane, leading to skewed and unreliable measurement results.
  * AI Commerce Search model training, especially for personalization, heavily relies on consistent `visitorId` and `userId` fields to link user interactions over time and attribute purchases to preceding search events.
  * Visitor ID switching breaks this link, preventing the model from learning effectively from a user's journey within a consistent search experience. This significantly affects both measurement and model training.



###  Search events with tokens in other experiment lane (apply this to browse if needed)

### Description

  * This check specifically looks at search user events that are tagged with an experiment ID belonging to the control group or holdout traffic, but which unexpectedly contain a Google-generated attribution token.
  * Attribution tokens are returned by the AI Commerce Search API, and are intended to be included in subsequent user events for Google-served traffic.
  * Control traffic uses the existing search engine and shouldn't receive or send Google attribution tokens.
  * This issue is related to the experiment ID switching check, as it implies events are being mistakenly tagged or routed.
  * This issue might indicate the possibility of search response caching which will degrade search performance and user experience due to stale inventory and outdated ranking.



### Impact

  * The presence of a Google attribution token in a control group event leads to mistakenly tagged attributions.
  * This means events from users who experienced the control (non-Google) search are incorrectly associated with the Google experiment lane.
  * This directly skews the metrics calculation for the Google lane by including data from the control group, distorting the perceived performance and invalidating measurement.
  * From a model training perspective, the model uses attributed user events to learn from interactions with search results.
  * Including mistakenly attributed events from the control group introduces irrelevant or conflicting data into the training set, potentially leading to a degradation in model performance.
  * This check affects both measurement and model training.



###  Search APIs with visitors from other experiment lane (apply this to browse if needed)

### Description

  * This check focuses on the incoming search request calls to the AI Commerce Search API itself.
  * It looks for requests that originate from visitor IDs or experiment IDs that are designated for the control group or holdout traffic.
  * This indicates that traffic intended for the control or holdout group is being incorrectly directed to the Google experiment lane's API endpoint.
  * This issue is very similar to the visitor ID switching check but is observed from the API request side rather than solely the user event side.



### Impact

  * This finding points to a fundamental misconfiguration in the traffic splitting and routing mechanism of the A/B test.
  * Experiment arms are not properly isolated if control traffic is sent to the Google API.
  * This invalidates the A/B test setup and compromises the fairness of the comparison.
  * It directly impacts measurement because the traffic volume and composition in the Google lane are inflated by the inclusion of unintended users, leading to inaccurate metric calculation and analysis.
  * For model training, while the API logs themselves aren't the primary training data, the subsequent user events generated by this misrouted traffic, if also mistakenly attributed, introduces noise and potentially incorrect signals into the training data.
  * This issue affects both measurement and model training.



###  Purchase events with visitor ID from other experiment lane

### Description

  * This check validates that purchase-complete user events recorded for a user (identified by their visitor ID or user ID) are tagged with the correct `experimentIds` corresponding to the A/B test lane they were assigned to, such as the control or the experiment.
  * It detects instances where a user's purchase event is associated with an experiment lane other than the one they were in when they performed the relevant search actions that led to the purchase.
  * This issue is closely related to maintaining consistent visitor assignment to experiment groups and relies on experimentIds being included in the purchase-complete event.



### Impact

  * Consistent visitor assignment to experiment lanes is crucial for accurate A/B testing.
  * If purchase-complete events are mistakenly tagged with the wrong experiment ID, they will be incorrectly attributed to that lane.
  * This directly skews metrics that rely on purchase data per lane, such as revenue rate, purchase order rate, average order value, and conversion rate.
  * Mistaken attribution makes it impossible to accurately compare the performance of different experiment groups, leading to invalid and unreliable A/B test measurement results.
  * From a model training perspective, AI Commerce Search models, particularly those optimizing for revenue or conversion rate, train by linking user interactions (like search) to subsequent purchases to understand which results lead to conversions.
  * Proper attribution, which often uses visitor, user, and experiment IDs to connect purchase events back to searches, is essential for creating these positive training examples. 
    * If purchase events are mistakenly attributed due to inconsistent IDs or experiment lane switching, the training data becomes corrupted with incorrect signals.
  * **Valid if experiment IDs are sent in purchase event:** As noted, this check is valid and impactful only if `experimentIds` are correctly implemented and sent within the purchase-complete user events.



###  Add-to-cart events with visitor IDs from the other experiment lane

### Description

  * Similar to the purchase event check, this verifies that add-to-cart user events for a given visitor ID are correctly associated with the user's assigned experiment lane using the experiment IDs field.
  * It identifies cases where an add-to-cart event is tagged with an experiment ID for a lane the user was not assigned to.
  * This issue can stem from inconsistent visitor ID usage across different event types or incorrect `experimentIds` tagging.



### Impact

  * Mistakenly tagged add-to-cart events lead to incorrect attribution of this user behavior to the experiment lanes.
  * This directly skews metrics like add-to-cart rate and conversion rate, especially if add-to-cart rate is considered an important step in the conversion funnel.
  * Inaccurate metrics compromise the reliability of the A/B test results and the ability to correctly measure the impact of the experiment.
  * From a model training perspective, add-to-cart events serve as important positive signals that models, particularly revenue-optimized ones, learn from.
  * If these events are mistakenly attributed to the wrong experiment lane due to inconsistent ID or `experimentIds` tagging, the model receives noisy or incorrect training signals.
  * Valid if experiment IDs are sent in add-to-cart event: As noted, this check is valid and impactful only if `experimentIds` are correctly implemented and sent within the add-to-cart user events.



###  Distribution of devices in each type of events across experiment lanes

### Description

  * This check assesses whether the distribution of user activity, categorized by device type (e.g., mobile, desktop, app), is balanced across the control and experiment lanes for each type of user event (**Search** , **Detail page view** , **Add-to-cart** , **Purchase**).
  * It aims to ensure that the proportion of users interacting with the site using mobile is roughly the same in the control group as in the test group, and similarly for other device types.
  * Detecting a significant skew indicates a potential issue in the mechanism used to split traffic or route events based on device type.



### Impact

  * A skewed distribution of devices means the control and test groups are not demographically balanced in terms of the devices used, similar to the demographic split issue.

  * User behavior, browse patterns, and conversion rates can vary significantly depending on the device used. This is why an imbalanced device split between experiment lanes introduces bias into the A/B test comparison, leading to inaccurate measurement of key business metrics for each lane. This is also attributed to the fact that the results from one group might be disproportionately influenced by a higher or lower percentage of users from a specific device type, making it difficult to determine the true impact of the experiment.

  * While device type isn't always a direct feature in all models, ensuring balanced traffic helps ensure that the training data, which is derived from user events within each lane, accurately reflects the real-world distribution of user behavior across devices. An imbalance could indirectly lead to training data that over-represents or underrepresents user behavior from certain devices, potentially leading to a model that is not optimally tuned for the overall user base.

  * Events form the basis for KPI tracking and general troubleshooting.




###  Search events with filters between experiment lanes, comparison (apply this to browse if needed)

### Description

  * This check compares the filter data included within search user events between the control and experiment lanes for similar search queries.
  * It verifies that filter information is being captured correctly, consistently, and with parity between the lanes. 
    * This includes checking if the available filter options (facets) presented to users are the same or equivalent, if the filter values sent in events match expected formats or catalog data, and if the UI/UX for filtering is comparable.
  * A discrepancy could arise if filters are not captured, captured incorrectly, or if the filtering UI/options differ, which can usually be traced back to config issue in the Catalog or Search API.



### Impact

  * Differences in the filtering experience or how filter data is captured between experiment lanes can directly influence how users interact with search results.
  * If one lane offers better or different filtering options, users in that lane might refine their searches differently, leading to variations in user behavior and potentially affecting metrics like conversion rates for filtered searches.
  * This introduces variable bias into the A/B test, making it challenging to attribute observed metric differences solely to the core search ranking differences.
  * A lack of captured filter data in events also limits the ability to analyze performance metrics sliced by filter usage, impacting measurement insights.
  * For model training, filter information in search events is critical for training dynamic facet models, as the model learns facet popularity from user filter usage signals.
  * Accurate filter usage information in events is also important for click-based reranking models; if filter values in events don't match those in search requests, the model's performance for queries with filters is negatively impacted.
  * Inconsistent or missing filter data in events degrades model quality related to dynamic facets and reranking for filtered queries.



###  Query between search event and Search API match by token but not matching by query (apply this to browse if needed)

### Description

  * This check involves examining a specific search user journey by linking a search event to its corresponding Search API request using the `attributionToken`.
  * The attribution token is generated by AI Commerce Search and returned with each search request.
  * This check specifically compares the `searchQuery` field in the search event with the actual query string sent in the initial Search API request that returned the attribution Token.
  * If these query strings don't match despite the presence of a linking attribution token, it indicates that the searchQuery being sent in the user event does not accurately reflect the user's original search query.



### Impact

  * This issue heavily affects model training.
  * AI Commerce Search uses event data to train its models.
  * The models, particularly click-based reranking models, learn by linking user interactions (like clicks, add-to-carts, and purchases) back to the search requests that generated the results.
  * This linkage relies on accurate information within the events, including the `searchQuery` and `attributionToken` fields.
  * If the `searchQuery` in the event is mismatched with the actual query from the Search API request, the model is trained on incorrect data, associating user behavior with the wrong query.
  * This can lead to a severe negative impact on search result quality because the model learns suboptimal ranking strategies based on flawed query data.
  * While the primary impact is on model training quality, this can also indirectly affect measurement, as models trained on bad data can perform poorly, leading to skewed A/B test results even if events are otherwise captured.



###  Search API tracking for a single visitor and matching search event (apply this to browse if needed)

### Description

  * This check is a manual validation process where a tester simulates a typical user journey involving a sequence of actions like search, clicking a product (`detail-page-view` event), adding to the cart, and potentially making a purchase.
  * By noting the visitor iD and timestamps for these actions, the tester then retrieves the recorded user events for that specific visitor ID from logs or data platforms.
  * The goal is to verify a 1:1 correspondence between the user's observed actions and the events recorded in the system (such as a search action should generate a search event, a click, or a `detail-page-view` event).
  * Missing events, events with incorrect visitor Ids, or corrupted data within the events (like missing product IDs or experiment IDs) indicate issues in the event plumbing.



### Impact

  * Issues identified by this check heavily affect both measurement and model training.



#### Measurement

  * Accurate and complete user events are fundamental for calculating key business metrics in an A/B test, such as search click-through rate, search conversion rate, search add-to-cart rate, and revenue per visitor.
  * These metrics rely on attributing user behavior (clicks, adds-to-cart, purchases) to specific search results and experiment lanes.
  * If events are missing or corrupted for a user, their actions are not fully captured, leading to incorrect calculation of these metrics for the experiment lane they were in.
  * This introduces bias and noise, making the A/B test results inaccurate and unreliable for decision-making. For example, missing purchase events directly impacts conversion rate and revenue lift metrics.



#### Model training

  * AI Commerce Search models train extensively on user event data to learn user behavior patterns and optimize ranking.
  * Visitor and user IDs are crucial for personalization features and linking events to create training examples.
  * Missing or corrupted events mean the model loses valuable training signals from that user's interaction sequence. For example, missing purchase or add-to-cart events prevent the model from learning which product interactions led to conversions.
  * Similarly, missing detail page view events mean the model doesn't get signals about clicks. This reduction in the quantity and quality of training data degrades the model's ability to learn effectively, leading to poor search result quality and potentially negating the benefits of using an ML-based search engine.
  * Inconsistent visitor Id mapping or formatting can also disrupt this process.
  * Missing purchase events impact model training because the model never sees purchases.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
