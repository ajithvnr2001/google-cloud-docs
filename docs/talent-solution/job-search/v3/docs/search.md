---
url: https://docs.cloud.google.com/talent-solution/job-search/v3/docs/search/
title: Search basics (v3) \u00a0|\u00a0 Cloud Talent Solution - Job Search v3 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:53:56.451532+00:00
---

# Search basics (v3)  |  Cloud Talent Solution - Job Search v3  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/talent-solution/job-search/v3/docs/search/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Cloud Talent Solution ](https://docs.cloud.google.com/talent-solution/docs)
  * [ Job Search ](https://docs.cloud.google.com/talent-solution/job-search/docs)
  * [ Job Search v3 (deprecated) ](https://docs.cloud.google.com/talent-solution/job-search/v3/docs)



Send feedback 

#  Search basics (v3) Stay organized with collections  Save and categorize content based on your preferences. 

Cloud Talent Solution allows users to search against jobs you have stored in Cloud Talent Solution's index. This document walks you through the various search and related offerings of Cloud Talent Solution.

## Search requests

To make a job search request, send a POST request to the `jobs:search` endpoint, passing the search data in the body.

## Required fields

The following field is required:

  * `searchMode`: Specifies the type of job search to apply. Options are:

    * `JOB_SEARCH`: This is the default, and recommended, search mode. All jobs are searched against. The most relevant jobs are returned in the order of relevance to the search query.
    * `FEATURED_JOB_SEARCH`: Searches only for jobs with a `promotionValue` greater than 0. Results are ordered by the highest `promotionValue` first; in the case of a tie, relevance is used to decide position. See [Featured Jobs](https://docs.cloud.google.com/talent-solution/job-search/v3/docs/featured-jobs) for more info.



## Commonly used fields

  * `JobQuery`: Specify the job criteria to match against. These include location, job categories, employment types, text queries, companies, etc. See [Search Filters](https://docs.cloud.google.com/talent-solution/job-search/v3/docs/search-filters) for more information.

  * `requestMetadata`: Contains user and session information for this search request. See RequestMetadata for details.

  * `jobView`: Defines the number of fields that are returned for each matching job. Can be `JOB_VIEW_SMALL` (the default), `JOB_VIEW_MINIMAL`, or `JOB_VIEW_FULL`. Descriptions for each option are in the [`JobView`](https://docs.cloud.google.com/talent-solution/job-search/v3/docs/reference/rest/v3/JobView) reference.

  * `orderBy`: The sort order for returned jobs. See the [reference](https://docs.cloud.google.com/talent-solution/job-search/v3/docs/reference/rest/v3/projects.jobs/search#body.request_body.FIELDS.order_by) for allowed values. The default is to sort by relevance, descending (`RELEVANCE_DESC`).




## Relevance thresholding and location/category broadening

To return a higher number of jobs for your searches, the following two fields loosen the restrictions on relevance:

  * `enableBroadening`: Setting this to `true` loosens the restrictions on location and job category of the search request, in order to return more results. For example, if a search request specified jobs within a 2 mile radius of Anytown, WA, setting this flag to `true` may also return jobs from NextTownOver, WA as well.

  * `disableKeywordMatch`: This flag is false by default. Setting this flag to false allows Cloud Talent Solution to append the jobs that are relevant to this search query with jobs that also match the exact query string in the title or description.




## RequestMetadata

Every search and histogram request should include a [`RequestMetadata`](https://docs.cloud.google.com/talent-solution/job-search/v3/docs/reference/rest/v3/RequestMetadata) object. This object contains information about the user initiating the search.

There are a few reasons this object is important:

  * User consistency. Cloud Talent Solution runs several versions of the underlying models simultaneously in an effort to improve search relevance. Fill in this field to ensure a job seeker has a consistent experiences. Cloud Talent Solution ensures that a job seeker (identified by [userId](https://cloud.google.com/talent-solution/job-search/v3/docs/reference/rest/v3/RequestMetadata#FIELDS.user_id), [sessionId](https://cloud.google.com/talent-solution/job-search/v3/docs/reference/rest/v3/RequestMetadata#FIELDS.session_id), and [domain](https://cloud.google.com/talent-solution/job-search/v3/docs/reference/rest/v3/RequestMetadata#FIELDS.domain)) has a consistent experience. Note: These fields should be obfuscated.

  * Search improvements.The tuning algorithms are based on the information provided in the `RequestMetadata` fields along with the job seekers' data you provide. This improves search result relevance.




## Search operators

Operator | Description  
---|---  
( ) | Groups one or more keywords together.  
AND | Searches for results relevant to the keywords or groups of keywords on both sides of the operator.  
OR | Searches for results relevant to the keyword or group of keyword(s) on either side of the operator.  
NOT | Excludes results relevant to the keyword or group of keyword(s), in parentheses, immediately following the operator.  
- | Excludes results relevant to the keyword or group of keyword(s) appended to the operator.  
  
For example:

  * `"software OR java"` returns jobs with _either_ "software" or "java" in their metadata.

  * `"software" -java` returns jobs relevant to "software" but excludes jobs that are relevant to "java".

  * `"(software OR java) AND (marketing)"` returns jobs relevant to both "software" and "marketing", and jobs that are relevant to both "java" and "marketing".




## Job seeker query

Search terms can also be detected as actual job related entities. For example, if the query was for 'intern', Cloud Talent Solution would treat this as the employment type "INTERN" and filter on jobs that only had the EMPLOYMENT_TYPE - INTERN. Therefore, even if intern was necessarily in the job description, it wouldn't be returned if the employment type for that job was set to something else.  It is very important to specify the employment type for each job. Not doing so negatively impacts the job seeker's experience. 

## Troubleshooting

Each search request generates a unique search `requestID` in our system that is used to track the parameters of that search as well as the response. This is crucial in troubleshooting issues related to specific search, CRUD requests, and should be appropriately logged. The `requestId` is returned inside the [ResponseMetadata](https://docs.cloud.google.com/talent-solution/job-search/v3/docs/reference/rest/v3/ResponseMetadata) field in the [search response body](https://docs.cloud.google.com/talent-solution/job-search/v3/docs/reference/rest/v3/projects.jobs/search#response-body). or the associated CRUD call response object.

For support issues that relate to relevance, search inquiries, indexing inquiries, etc., please [file a ticket](https://docs.cloud.google.com/talent-solution/docs/support) with our support team, and include relevant request ids or request themselves.

## Result counts

The result count is used to communicate the number of search results to the job seeker. This doesn't always correspond to the [histogram](https://docs.cloud.google.com/talent-solution/job-search/v3/docs/histogram) results or the actual number of jobs returned. Job Search returns a maximum of 5000 jobs.

## Pagination

By default, Job Search returns 100 results per page (or fewer, if the total number of results is less than 100). You can implement pagination using the fields associated with this feature.

**Note:** If the total number of results exceeds the maximum of 5000, all pages after the page containing the 5000th result will be blank.

  * **`pageSize`** : The number of results returned per page.
  * **`nextPageToken`** : A unique token, returned with the results of each page of search results, that specifies the starting position for the next page of results. This field is left empty if there are no more results.
  * **`offset`** : Specifies the offset between the relevance ranking of the job returned at the top of a given page and 1 (the most relevant Job returned). As an example, a user performs a search and `pageSize` is set to 10. The first page returns the #1 job at the top, therefore the `offset` value for this page is 0. The next page returns job #11 at the top; `offset` for this page is 10.



Set the page size to 20 results or less to avoid latency issues. As a best practice, issue a separate search call per page rendered to the job seeker. The alternative, a single search call to return a larger number of jobs and paginating on the client side, impedes the ability of the machine learning model to learn accurately through the Jobs Analytics Framework.

## Spell checking

Spell check is a feature of Cloud Talent Solution search request that accounts for potentially misspelled search terms, corrects them and returns results based on the corrected query. For example, when spell check is enabled, if a job seeker searches for "manaer" instead of "manager", Cloud Talent Solution returns jobs for "manager". Spell checking can be enabled/disabled by setting the `disableSpellCheck` field of the JobQuery. If spell checking is enabled, the corrected query can be found in the search response, in the `spellResult` field.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
