---
url: https://docs.cloud.google.com/healthcare-api/docs/how-tos/best-practices-fhir-search/
title: Implementing pagination and search totals with FHIR search \u00a0|\u00a0 Cloud Healthcare API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:52:35.735208+00:00
---

# Implementing pagination and search totals with FHIR search  |  Cloud Healthcare API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/healthcare-api/docs/how-tos/best-practices-fhir-search/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Cloud Healthcare API ](https://docs.cloud.google.com/healthcare-api/docs)
  * [ Guides ](https://docs.cloud.google.com/healthcare-api/docs/introduction)



Send feedback 

#  Implementing pagination and search totals with FHIR search Stay organized with collections  Save and categorize content based on your preferences. 

The Cloud Healthcare API FHIR search implementation is highly scalable and performant while still following the guidelines and limitations of REST and the FHIR specification. To help achieve this, FHIR search has the following properties:

  * **The search total is an estimate until the last page is returned.** Search results returned by the `fhir.search` method include the search total (the `Bundle.total` property), which is the total number of matches in the search. The search total is an estimate until the last page of search results is returned. The search total returned with the last page of results is an accurate sum of all the matches in the search.

  * **Search results provide sequential, forward pagination.** When there are more search results to return, the response includes a pagination URL (`Bundle.link.url`) for getting the next page of results.




## Basic use cases

FHIR search provides solutions to the following use cases:

  * **Browse sequentially.** A user browses forward sequentially through a limited number of pages of search results. An estimated search total is returned with each page.
  * **Process a set of search results.** An app gets a set of search results, reads through the results, and processes the data.



See the following sections for possible solutions for these use cases.

### Browse sequentially

You can build a low-latency application that lets a user browse forward sequentially through pages of results until the user finds the match that they want. This solution is feasible if the number of matches is small enough that the user can find the desired match by browsing page by page without skipping results. If your use case requires users to navigate forward multiple pages at a time, or to navigate backwards, see Navigate to a nearby page.

This solution cannot provide an accurate search total until the last page of results is returned. However, it can provide an approximate search total with each page of results. While an accurate search total could be a requirement for a background process, an approximate search total is typically adequate for a human user.

#### Workflow

Here is an example workflow for this solution:

  1. An app calls the `fhir.search` method, which returns the first page of search results. The response includes a pagination URL (`Bundle.link.url`) if there are more results to return. The response also includes the search total (`Bundle.total`). If there are more results to return than in the initial response, the search total is only an estimate. For more information, see [Pagination and sorting](https://docs.cloud.google.com/healthcare-api/docs/how-tos/fhir-search#pagination_and_sorting).

  2. The app displays the page of search results, a link to the next page of results (if any), and the search total.

  3. If the user wants to see the next page of results, they click the link, which results in a call to the pagination URL. The response include a new pagination URL if there are more results to return. The response also includes the search total. This is an updated estimate if there are more results to return.

  4. The app displays the new page of search results, a link to the next page of results (if any), and the search total.

  5. The previous two steps are repeated until the user stops searching or the last page of results is returned.




#### Best practice

Choose a page size appropriate for a human to read without difficulty. Depending on your use case, this might be 10 to 20 matches per page. Smaller pages load faster, and too many links on a page can be difficult for a user to manage. You control the page size with the `_count` parameter.

### Process a set of search results

You can get a set of search results by making successive calls to the `fhir.search` method using the pagination URL. If the number of search results is small enough, you can get a complete set of results by continuing until there are no more pages to return. An accurate search total is included in the last page of results. After getting the search results, your app can read through them and perform whatever processing, analyzing, or aggregating you require.

Bear in mind that if you have a very large number of search results, it might not be possible to get the last page of search results (and the accurate search total) in a practical amount of time.

#### Workflow

Here is an example workflow for this solution:

  1. The app calls the `fhir.search` method, which returns the first page of search results. The response include a pagination URL (`Bundle.link.url`) if there are more results to return.

  2. If there are more results to return, the app calls the pagination URL from the previous step to get the next page of search results.

  3. The app repeats the previous step until there are no more results to return or some other predefined limit is reached. If you reach the last page of search results, the search total is accurate.

  4. The app processes the search results.




Depending on your use case, you app can do any of the following:

  * Wait until all of the search results are received before processing the data.
  * Process data as it's received with each successive call to `fhir.search`.
  * Set some kind of limit, such as the number of matches returned or the amount of time elapsed. When the limit is reached you can process the data, not process the data, or do some other action.



#### Design options

Here are some design options that might decrease search latency:

  * **Set a large page size.** Use the `_count` parameter to set a large page size, perhaps 500 to 1,000, depending on your use case. Using a larger page size increases the latency for each page fetch, but it might speed up the overall process, as fewer page fetches are required to get the entire set of search results.

  * **Limit the search results.** If all you need is an accurate search total (you don't need to return resource content), set the `_elements` parameter of the `fhir.search` method to `identifier`. This might decrease the latency of your search query, compared to requesting the return of full FHIR resources. For more information, see [Limiting fields returned in search results](https://docs.cloud.google.com/healthcare-api/docs/how-tos/fhir-advanced-search#limiting_fields_returned_in_search_results).




## Use cases that require prefetching and caching

You might need functionality beyond what is possible using the simple mechanism of successively calling the `fhir.search` method using pagination URLs. One possibility is to build a caching layer between your app and the FHIR store that maintains session state while prefetching and caching search results. The app can group the search results into small "app pages" of 10 or 20 matches. The app can then quickly serve these small app pages to the user in a direct, non-sequential way, based on a user's selections. See Navigate to a nearby page for an example of this type of workflow.

**Note:** You can create a caching layer using [Apigee API Management](https://docs.cloud.google.com/apigee) or any solution that works for you.

### Navigate to a nearby page

You can build a low-latency solution that lets a user traverse a large number of search results until they find the match they are looking for. It can scale to a virtually unlimited number of matches while keeping latency low and incurring a relatively small increase in resource consumption. A user can navigate directly to a page of search results, up to a predetermined number of pages forward or backward from the current page. You can provide an estimated search total with each page of results. For reference, this design is similar to the design for Google Search.

#### Workflow

Figure 1 shows an example workflow for this solution. With this workflow, each time the user selects a page of results to view, the app provides links to nearby pages. In this case, the app provides links to pages up to five pages backward from the selected page and up to four pages forward from the selected page. To make the four forward pages available for viewing, the app prefetches 40 additional matches when the user selects a page of results.

![prefetch and cache](https://docs.cloud.google.com/static/healthcare-api/images/prefetch-and-cache.svg)

**Figure 1.** The app groups search results into "app pages" that are cached and made available to the user.

Figure 1 illustrates these steps:

  1. The user enters a search query into the app frontend, initiating the following actions:

     1. The app calls the `fhir.search` method to prefetch the first page of search results.

The `_count` parameter is set to 100 to keep the page size of the response relatively small, resulting in relatively fast response times. The response includes a pagination URL (`Bundle.link.url`) if there are more results to return. The response also includes the search total (`Bundle.total`). The search total is an estimate if there are more results to return. For more information, see [Pagination and sorting](https://docs.cloud.google.com/healthcare-api/docs/how-tos/fhir-search#pagination_and_sorting).

     2. The app sends the response to the caching layer.

  2. In the caching layer, the app groups the 100 matches from the response into 10 app pages of 10 matches each. An app page is a small grouping of matches that the app can display to the user.

  3. The app displays app page 1 to the user. App page 1 includes links to app pages 2-10 and the estimated search total.

  4. The user clicks a link to a different app page (app page 10 in this example), initiating the following actions:

     1. The app calls the `fhir.search` method, using the pagination URL that was returned with the previous prefetch, to prefetch the next page of search results.

The `_count` parameter is set to 40 to prefetch the next 40 matches from the user's search query. The 40 matches are for the next four app pages that the app makes available to the user.

     2. The app sends the response to the caching layer.

  5. In the caching layer, the app groups the 40 matches from the response into four app pages of 10 matches each.

  6. The app displays app page 10 to the user. App page 10 includes links to app pages 5-9 (the five app pages backward from app page 10) and links to app pages 11-14 (the four app pages forward from app page 10). App page 10 also includes the estimated search total.




This can continue for as long as the user wants to continue clicking links to app pages. Note that if the user navigates backward from the current app page and you already have all of the nearby app pages cached, you can choose not to do a new prefetch, depending on your use case.

This solution is fast and efficient for the following reasons:

  * Small prefetches, and even smaller app pages, process quickly.
  * Cached search results reduce the need to make multiple calls for the same results.
  * The mechanism remains fast regardless of how high the number of search results scales.



#### Design options

Here are some design options to consider, depending on your use case:

  * **App page size.** Your app pages can contain more than 10 matches if it suits your use case. Bear in mind that smaller pages load faster, and too many links on a page can be difficult for a user to manage.

  * **Number of app page links.** In the workflow suggested here, each app page returns nine links to other app pages: five links to the app pages directly backward from the current app page, and four links to the pages directly forward from the current app page. You can adjust these numbers to suit your use case.




#### Best practices

  * **Use the caching layer only when necessary.** If you set up a caching layer, use it only when your use case requires it. Searches that don't require the caching layer should bypass it.

  * **Reduce the size of your cache.** To conserve resources, you can reduce the size of your cache by purging your old search results while keeping the page URLs that you used to get the results. You can then reconstruct the cache as needed by calling the page URLs. Bear in mind that the results from multiple calls to the same pagination URL can change over time, as resources in the FHIR store are created, updated, and deleted in the background. Whether to purge, how to purge, and how often to purge your cache are design decisions that depend on your use case.

  * **Purge your cache for a given search.** To conserve resources, you can completely remove from the cache the results from inactive searches. Consider removing the longest-inactive searches first. Bear in mind that if a purged search becomes active again, this might cause an error state that forces the caching layer to restart the search.




### Navigate to any page

If you want a user to be able to navigate to any page in the search results, not just the pages nearby the current page, you can use a caching layer similar to the one described in Navigate to a nearby page. To allow a user to navigate to **any** app page of search results, however, you'll need to prefetch and cache **all** of the search results. With a relatively small number of search results, this is possible. With a very large number of search results, it can be impractical or impossible to prefetch them all. Even with a modest number of search results, the time it takes to prefetch them can be longer than it's reasonable to expect a user to wait.

#### Workflow

Set up a workflow similar to Navigate to a nearby page, with this key difference: the app continues prefetching search results in the background until all matches are returned or some other predefined limit is reached.

Here is an example workflow for this solution:

  1. The app calls the `fhir.search` method to prefetch the first page of search results from the user's search query. The response includes a pagination URL (`Bundle.link.url`) if there are more results to return. The response also includes the search total (`Bundle.total`). This is an estimate if there are more results to return.

**Note:** Use the `_count` parameter to set the page size, perhaps 100 to 200 matches per page, depending on your use case. Smaller page sizes are returned faster, improving the response time for the user. For more information, see [Pagination and sorting](https://docs.cloud.google.com/healthcare-api/docs/how-tos/fhir-search#pagination_and_sorting).
  2. The app groups the matches from the response into app pages of 20 matches each and stores them in the cache. An app page is a small grouping of matches that the app can display to the user.

  3. The app displays the first app page to the user. The app page includes links to the cached app pages and the estimated search total.

  4. If there are more results to return, the app does the following:

     * Calls the pagination URL returned from the previous prefetch to get the next page of search results.
     * Groups the matches from the response into app pages of 20 matches each and stores them in the cache.
     * Refreshes the app page that the user is currently viewing with new links to the newly prefetched and cached app pages.
  5. The app repeats the previous step until there are no more results to return or some other predefined limit is reached. An accurate search total is returned with the last page of search results.




While the app is prefetching and caching matches in the background, the user can continue clicking links to cached pages.

#### Design options

Here are some design options to consider, depending on your use case:

  * **App page size.** Your app pages can contain more or fewer than 20 matches if it suits your use case. Bear in mind that smaller pages load faster, and too many links on a page can be difficult for a user to manage.

  * **Refresh the search total.** While your app is prefetching and caching search results in the background, you can display progressively more accurate search totals to the user. To do this, configure your app to do the following:

    * At a set interval, get the search total (the `Bundle.total` property) from the latest prefetch in the caching layer. This is the current best estimate of the search total. Display the search total to the user, indicating that it's an estimate. Determine the frequency of this refresh based on your use case.

    * Recognize when the search total from the caching layer is accurate. That is, the search total is from the last page of search results. When the last page of search results is reached, the app displays the search total and indicates to the user that the search total is accurate. The app then stops getting search totals from the caching layer.

Note that with a large number of matches, background prefetching and caching might not reach the last page of search results (and the accurate search total) before the user completes their search session.




#### Best practices

  * **Deduplicate included resources.** If you use the `_include` and `_revinclude` parameters when prefetching and caching search results, we recommend deduplicating the included resources in the cache after each prefetch. This will help save memory by reducing the size of your cache. When you group matches into app pages, add the appropriate included resources to each app page. For more information, see [Including additional resources in search results](https://docs.cloud.google.com/healthcare-api/docs/how-tos/fhir-advanced-search#including_additional_resources_in_search_results).

  * **Set a limit on prefetching and caching.** With a very large number of search results, it can be impractical or impossible to prefetch them all. We recommend setting a limit on the number of search results to prefetch. This keeps your cache at a manageable size and helps save memory. For example, you could limit your cache size to 10,000 or 20,000 matches. Alternatively, you could limit the number of pages to prefetch, or set a time limit after which prefetching stops. The type of limit you impose and way you impose it are design decisions that depend on your use case. If the limit is reached before all search results are returned, consider indicating this to the user, including that the search total is still an estimate.




### Frontend caching

The application frontend, such as a web browser or mobile app, can provide some caching of search results as an alternative to introducing a caching layer into the architecture. This approach can provide navigation to the previous page, or any page in the navigation history, by leveraging AJAX calls and storing search results and/or pagination URLs. Here are some advantages to this approach:

  * It can be less resource-intensive than a caching layer.
  * It's more scalable, as it distributes the caching work across many clients.
  * It's easier to determine when cached resources are no longer needed — for example, when the user closes a tab or navigates away from the search interface.



## General best practices

Here are some best practices that apply to all of the solutions in this document.

  * **Plan for pages being smaller than the _count value.** In some circumstances, a search might return pages containing fewer matches than the `_count` value that you specify. For example, this might happen if you specify a page size that is particularly large. If your search returns a page that is smaller than the `_count` value, and your app uses a caching layer, you might need to decide whether to (1) Display fewer results than expected on an app page, or (2) Fetch a few more results to get enough for a complete app page. For more information, see [Pagination and sorting](https://docs.cloud.google.com/healthcare-api/docs/how-tos/fhir-search#pagination_and_sorting).

  * **Retry retryable HTTP request errors.** Your app should expect retryable HTTP request errors, such as `429` or `500`, and retry after receiving them. 




## Evaluate your use cases

Implementing features such as navigating to any page, getting accurate search totals, and updating estimated totals increases the complexity and development costs for your app. These features can also increase latency and increase monetary costs for usage of Google Cloud resources. We recommend carefully evaluating your use cases to ensure that the value of these features justifies the costs. Here are some things to consider:

  * **Navigating to any page.** A user typically does not need to navigate to a specific page, many pages from the current page. In most cases, Navigating to a nearby page is adequate.

  * **Accurate search totals.** Search totals can change as resources in the FHIR store are created, updated, and deleted. For this reason, an accurate search total is accurate at the moment it's returned (with the last page of search results), but it might not remain accurate over time. Therefore, accurate search totals might be of limited value for your app, depending on your use case.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
