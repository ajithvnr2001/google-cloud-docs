---
url: https://docs.cloud.google.com/talent-solution/job-search/v3/docs/best-practices/
title: Job search API parameters: Best practices (v3) \u00a0|\u00a0 Cloud Talent Solution - Job Search v3 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:53:21.027258+00:00
---

# Job search API parameters: Best practices (v3)  |  Cloud Talent Solution - Job Search v3  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/talent-solution/job-search/v3/docs/best-practices/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Cloud Talent Solution ](https://docs.cloud.google.com/talent-solution/docs)
  * [ Job Search ](https://docs.cloud.google.com/talent-solution/job-search/docs)
  * [ Job Search v3 (deprecated) ](https://docs.cloud.google.com/talent-solution/job-search/v3/docs)



Send feedback 

#  Job search API parameters: Best practices (v3) Stay organized with collections  Save and categorize content based on your preferences. 

## Configuring the API

### Factors affecting search results

Together, "Featured Jobs", "Enable Broadening", and "Disable Keyword Match" have a significant impact on the number and relevance of jobs returned to the job seeker. The most appropriate configuration of these three factors depends on your business needs. The best method for determining your optimal configuration is to apply different test scenarios and evaluate the outcomes during a testing phase.

  1. Featured Jobs: You can use Featured Jobs to assign promotional values to individual jobs, which allows you to highlight jobs that are important to your business needs. See the [Featured jobs](https://cloud.google.com/talent-solution/job-search/v3/docs/featured-jobs) documentation for best practices and implementation details.

  2. [`disableKeywordMatch`](https://docs.cloud.google.com/talent-solution/job-search/v3/docs/reference/rest/v3/projects.jobs/search): This parameter allows the API to return keyword matches in addition to the relevant results determined by the ML algorithm. The default setting is `false`. Keeping the default setting means the CTS Job search API returns jobs that were not returned as relevant by the ML algorithm, but there is a keyword match in the title or job description with the job seeker's query string. Setting this parameter to `true` disables the keyword match, so fewer jobs (only those determined to be relevant by the ML feature) are returned.

  3. [`enableBroadening`](https://docs.cloud.google.com/talent-solution/job-search/v3/docs/reference/rest/v3/projects.jobs/search): This parameter allows you expand the job seeker's query by relaxing their stated restrictions on location and job categories. It's set to `false` by default and enabled when set to `true`. It's used to increase the number of search results returned.




#### Search configuration outcomes

**To return only the most relevant jobs** : Set `disableKeywordMatch` to `true` and `enableBroadening` to `false`. This improves the API's performance metrics related to search relevance since only the relevant jobs are returned. However, fewer jobs overall are returned in the search results.

**To return a higher number of jobs including both relevant and keyword matched results** : Set `disableKeywordMatch` to `false` and `enableBroadening` to `false`. The keyword-matched results are listed after the relevant jobs in the results, but query expansion results are not returned.

**To return a higher number of jobs including both relevant and query expanded jobs** : Set `disableKeywordMatch` to `true` and `enableBroadening` to `true`. The job seeker's query is expanded to include related job categories and nearby locations, listed after the relevant results. Keyword based matches are not returned.

**To return the highest possible number of jobs** : Set `disableKeywordMatch` to `false` and `enableBroadening` to `true`. The Job Search API returns the most relevant jobs at the top of the search results, followed by keyword matched jobs and query expanded jobs (by location, job category, etc). This maximizes the total number of jobs returned.

diasableKeywordMatch | enableBroadening | Outcome  
---|---|---  
- | - | Returns a higher number of jobs including both relevant and keyword matched results (but assume featured jobs is set to `false`).  
+ | + | Returns a higher number of jobs including both relevant and query expanded jobs (but assume featured jobs is set to `false`).  
- | + | Returns the highest number of jobs (but assume featured jobs is set to `false`).  
+ | - | Returns only the most relevant jobs (but assume featured jobs is set to `false`).  
  
### `Request.page_size`

For best performance and to avoid latency, set up the results page to display 20 or fewer jobs at a time.

### `customAttributes`

`customAttributes` gives you the flexibility to assign additional values to your jobs according to your business needs (for example, GPA scores) and use these values to filter the results.

**Note:** Avoid setting up any `customAttributes` valuess that are related to location. The API's existing location filter has a built-in algorithm that automatically detects location information related to the job seeker's search query.

### Location field

A detailed overview of the Location field can be found on the [Location fields](https://docs.cloud.google.com/talent-solution/job-search/v3/docs/jobs#location_fields) page. Providing the job's street address instead of GPS coordinates in the address field helps the API improve location detection and search relevance.

### `locationFilter`

Use the `regionCode` if a single company has multiple job openings located in different geographic regions. Assigning a `regionCode` to each listing ensures that a search query returns jobs only in the job seeker's desired location rather than the global results for that company. For example, a search on the location keyword "Cambridge" without a `regionCode` in place returns results from both Cambridge, UK and Cambridge, MA, USA. This decreases search relevance.

### `Region_code` and `Language_code`

Set `request.filters.location_filters.region_code` to match the geographic location that the user is searching (such as the United Kingdom). Set `request.filters.language_code` to the appropriate language code for that region (`en_GB` in this case) so that the API can use localised search logic (for example, "lorry driver" in `en_GB` as opposed to "truck driver" in the United States).

### `radiusinMiles`

This parameter sets a radius (in miles) around a job seeker's indicated location. The API returns results inside this geographic range. How this distance is applied to the geography of the search results depends on the type of location information entered. If the job seeker enters a street address, the `radiusInMiles` distance is set from a single point. If the job seeker enters a city, the API applies a bounding box around the city limits and calculates distance from the box edges. If the user enters only a state or country, `radiusInMiles` is ignored.

Make sure that the mileage radius is as small as possible. Setting the mileage to a larger range returns results that may be outside the job seeker's desired location, decreasing relevance. For example, searching for jobs in New York city with `radiusInMiles` set to 100 miles returns results in both upstate New York and New Jersey. Keeping the radius as small as possible increases the relevance of the results.

### `postingExpireTime`

This parameter sets the length of time that the job posting is active before it is removed from search results. The default is 30 days after the job creation time in the UTC time zone.

### `Job_employment_type`

This is not a required field, however using Job_employment_type increases the relevance of job search results.

## Configuring the API: Custom Ranking

**Featured Jobs** gives you the ability to influence search results and highlight jobs based on a single variable (`promotionValue`). See the [Featured Jobs](https://docs.cloud.google.com/talent-solution/job-search/v3/docs/featured-jobs) documentation for details. **Custom Ranking** gives you the ability to influence the results based on multiple variables, offering more control over the rankings regardless of relevance. This feature is useful to applications that require balancing relevance with economic interests, such as a multi-tiered Cost-per-Click (CPC) subscriber system. Influence on how jobs are ranked on top of the existing relevance score is based on two variables: `rankingExpression` and `importanceLevel`.

  * **`rankingExpression`** : This variable controls how jobs are ranked based on their existing relevance scores (as determined by the API algorithm). 'rankingExpression' must be set to 'filterable' in order for the API to index the parameter.

  * **`importanceLevel`** : This parameter sets the importance level of a job's ranking position when it is returned in searches. There are six different levels: Unspecified, `NONE`, `LOW`, `MID`, `HIGH` and `EXTREME`. Setting the value to `EXTREME` means that all other API-generated relevance factors are ignored, so use this value sparingly. Jobs set to `EXTREME` are returned at the top of the job seeker's query instead of the most relevant jobs.

  * **Featured Jobs** versus **Custom Ranking** : **Featured Jobs** is most useful for promoting a single category of jobs (for example, jobs at a certain company) above the relevance ranking. If you need to rank jobs according to multi-level CPC (Cost Per Click) variables in addition to the relevance ranking, **Custom Ranking** is a better choice.




## Commute search

[Commute search](https://docs.cloud.google.com/talent-solution/job-search/v3/docs/search-commute) helps job seekers search for jobs based on commute time. To enable it, include an additional `CommuteFilter` object in the `JobQuery.commuteFilter` field. This object allows the job seeker to select `commuteMethod`, `travelDuration`, and `startCoordinates`. The job seeker can also select options such as `roadTraffic` (`TRAFFIC_FREE` or `BUSY_HOUR`) and `departureTime` when calculating the commute time. See the Commute Search [implementation](https://docs.cloud.google.com/talent-solution/job-search/v3/docs/commute-search) and [how-to](https://docs.cloud.google.com/talent-solution/job-search/v3/docs/search-commute) pages for details.

## Data management & error handling

### Data integrity

  1. **Uploading jobs:** Data issues can prevent jobs from being uploaded to the API. Please see the [HTTP Response Codes](https://docs.cloud.google.com/talent-solution/job-search/v3/docs/http-response-codes) page for more information. Some common examples:

     * Job locations are incorrect, so the request can't be resolved.
     * Company or Job fields do not exist, which returns a bad request.

There are three main options for troubleshooting job uploading issues:

     * Check the logging from your back end.
     * Check the CTS [management tool](https://docs.cloud.google.com/talent-solution/docs/management-tools) for data logging.
     * Set up [Stackdriver Monitoring Tool](https://docs.cloud.google.com/monitoring/docs) on Cloud console to collect metadata, metrics, and events.
  2. **Indexing jobs:** The Job search API is designed to index all of your uploaded jobs in a set period of time. However, you may have quota restrictions on your end. Be sure to check your system for restrictions on indexing requests before sending jobs to CTS.




### Error handling mechanisms

Error handling is crucial to avoid a self-inflicted DDoS attack that results in job seekers being locked out. API services provided via the internet can also have intermittent connection failure, a prolonged outage, sudden service maintenance and other events that require a client application to retry the API request. This retry must be designed with network friendly behavior, for example [exponential backoff](https://docs.cloud.google.com/storage/docs/exponential-backoff).

### Deduping

Duplicate jobs negatively impact a job seeker's search experience. The Job search API includes two features to minimize duplicates:

  1. **Create jobs:** If you try to create 2+ jobs with the following criteria, the record will be rejected and you will encounter a 4xx error:

     * same `companyName`, AND
     * same `job_req_id`, AND
     * same location/`languageCode`
  2. **Search for jobs:** The CTS Job search API surfaces jobs that are relevant to job seeker's search query. A built-in feature of the relevance algorithm makes sure that any returned jobs are diversified, preventing nearly identical jobs from showing up next to each other in search results.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
