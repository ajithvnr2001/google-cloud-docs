---
url: https://docs.cloud.google.com/feeds/job-release-notes.xml
title: Cloud Talent Solution Job Search - Release notes
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:20:18.106250+00:00
---

# Cloud Talent Solution Job Search - Release notes

> Source: https://docs.cloud.google.com/feeds/job-release-notes.xml

tag:google.com,2016:job-release-notesCloud Talent Solution Job Search - Release notesGoogle Cloud Platform2024-12-19T00:00:00-08:00December 19, 2024tag:google.com,2016:job-release-notes#December_19_20242024-12-19T00:00:00-08:00v4 

### Feature

Add a `RelevanceThreshold` field to the `SearchJobsRequest` to filter results by precision.

### Changed

Improve address resolution for `LocationFilter` with region code.

]]> May 26, 2023tag:google.com,2016:job-release-notes#May_26_20232023-05-26T00:00:00-07:00v3 & v4 

### Changed

Jobs with commutable city-level locations are returned when `allowImpreciseAddresses` is set in `CommuteFilter`.

### Changed

Jobs with matching nation-level locations are boosted for telecommute searches.

**v4**

### Feature

Adds MAX_THREE_PER_COMPANY DiversificationLevel option.

]]> February 27, 2023tag:google.com,2016:job-release-notes#February_27_20232023-02-27T00:00:00-08:00v3 & v4 

### Changed

Added support for more MOC codes.

]]> November 30, 2022tag:google.com,2016:job-release-notes#November_30_20222022-11-30T00:00:00-08:00v4 

### Deprecated

Marking keyword_searchable_job_custom_attributes on the Company as deprecated. Moving forward please use the keyword searchable tag on the Job.CustomAttribute to specify keyword searchable.

### Deprecated

Marking company_size histogram facet as deprecated.

]]> August 19, 2022tag:google.com,2016:job-release-notes#August_19_20222022-08-19T00:00:00-07:00v3 & v4 

### Changed

Extend the functionality for the inferred remote location filter to respect the region code

]]> July 22, 2022tag:google.com,2016:job-release-notes#July_22_20222022-07-22T00:00:00-07:00v4 

### Changed

Histogram query for city and admin1_country can handle multiple location jobs

### Changed

Support special characters in companyDisplayNames fuzzy match

### Changed

Derive annualized compensation info for more employment types

]]> May 27, 2022tag:google.com,2016:job-release-notes#May_27_20222022-05-27T00:00:00-07:00v4 

### Feature

Add a new operator on companyDisplayNames filter to further support fuzzy match by treating input value as a multi word token

### Feature

Add a new option TELECOMMUTE_JOBS_EXCLUDED under enum TelecommutePreference to completely filter out the telecommute jobs in response

### Deprecated

Deprecate option TELECOMMUTE_EXCLUDED under enum TelecommutePreference

]]> May 10, 2022tag:google.com,2016:job-release-notes#May_10_20222022-05-10T00:00:00-07:00v3 & v4 

### Feature

  * Jobs within same state will rank higher in results when search jobs in a state level location with TELECOMMUTE_ALLOWED option

**v4**

### Fixed

  * keywordSearchable will be returned correctly in Job instance responses
  * Fix compensation histogram query to return correct histogram result

]]> March 22, 2022tag:google.com,2016:job-release-notes#March_22_20222022-03-22T00:00:00-07:00v4 

### Feature

The Cloud Talent Solutions dashboard management tool has added a Jobs and Companies page, which displays job statistics and metadata. You can use this page to troubleshoot data issues. The Jobs and Companies page has three tabs:

  * On the Summary tab, see the latest job count snapshots and a visualization of job count statistics over time.
  * On the Job Metadata tab, search for specific jobs and their available metadata.
  * On the Exports tab, export your metadata to a BigQuery table for further analysis.



For more about this new feature, see the [Jobs and Companies data](https://cloud.google.com/talent-solution/docs/management-tools#job-data) documentation.

]]> March 21, 2022tag:google.com,2016:job-release-notes#March_21_20222022-03-21T00:00:00-07:00v3 & v4 

### Feature

Added functionality in the companyDisplayNames filter to support fuzzy matching.

]]> January 28, 2022tag:google.com,2016:job-release-notes#January_28_20222022-01-28T00:00:00-08:00v3 & v4 

### Fixed

Fixed a bug with certain DIVERSIFICATION_LEVELS where results were dropped.

### Changed

Improvements in spell correction.

]]> September 03, 2021tag:google.com,2016:job-release-notes#September_03_20212021-09-03T00:00:00-07:00v4 

### Feature

Added a new `KeywordMatchMode` field to support more keyword matching options.

### Feature

Added more [DiversificationLevel](https://cloud.google.com/talent-solution/job-search/docs/reference/rest/v4/DiversificationLevel) configuration options. 

]]> July 30, 2021tag:google.com,2016:job-release-notes#July_30_20212021-07-30T00:00:00-07:00v4 

### Feature

Added WALKING and CYCLING as commute options in the [CommuteFilter](https://cloud.google.com/talent-solution/job-search/docs/reference/rest/v4/JobQuery#CommuteFilter).

### Changed

Removes companyName requirement for use of [ListJobs](https://cloud.google.com/talent-solution/job-search/docs/reference/rest/v4/projects.tenants.jobs/list) API.

### Changed

Increased the number of characters supported in [custom ranking expressions](https://cloud.google.com/talent-solution/job-search/docs/reference/rest/v4/CustomRankingInfo).

]]> October 13, 2020tag:google.com,2016:job-release-notes#October_13_20202020-10-13T00:00:00-07:00v3 

### Feature

Cloud Talent Solution has launched the v4 version of the API. [Migrate to Cloud Talent Solution v4](https://cloud.google.com/talent-solution/job-search/docs/migrate) by October 14, 2021 to continue using Cloud Talent Solution.

### Deprecated

As of today Cloud Talent Solution versions v3, v3p1beta1, and v4beta1 are deprecated. Deprecated means that these versions will continue to work until October 13, 2021, at which time these versions will be shut down. [Migrate to Cloud Talent Solution](https://cloud.google.com/talent-solution/job-search/docs/migrate) v4 by October 14, 2021 to continue using Cloud Talent Solution.

### Changed

When using [`orderBy`](https://cloud.google.com/talent-solution/job-search/docs/reference/rest/v4/projects.tenants.jobs/search#body.request_body.FIELDS.order_by) to order job search results by `distance_from` from the search location, equidistant jobs from the center of the search location will be tie-broken based on each job's relevance to the search keywords. Previously, jobs in this scenario weren't primarily tie-broken based on each job's relevance to the search keywords.

### Fixed

When using the [`EmploymentType`](https://cloud.google.com/talent-solution/job-search/docs/reference/rest/v4/projects.tenants.jobs#EmploymentType) as part of [`HistogramQuery`](https://cloud.google.com/talent-solution/job-search/docs/reference/rest/v4/HistogramQuery), facet counts for `CONTRACTOR` no longer also include facet counts for `CONTRACT_TO_HIRE`.

### Fixed

[`HistogramQuery`](https://cloud.google.com/talent-solution/job-search/docs/reference/rest/v4/HistogramQuery) facet counts no longer differ from the number of jobs returned when filtering search results by a given facet.

### Fixed

CTS has made improvements to the handling of accented characters and gendered terms in job titles and search keywords.

]]> September 30, 2020tag:google.com,2016:job-release-notes#September_30_20202020-09-30T00:00:00-07:00v3 

### Changed

Cloud Talent Solution's consumption [pricing](https://cloud.google.com/talent-solution/pricing) and [quota](https://cloud.google.com/talent-solution/quotas) limits will change effective January 4, 2021. The new pricing and quota limits are intended to better address the variety of use cases the talent industry has for managing and searching for jobs.

]]> April 03, 2020tag:google.com,2016:job-release-notes#April_03_20202020-04-03T00:00:00-07:00v3 

### Deprecated

As of this date, Cloud Talent Solution Job Search v2 is no longer available. Calls to v2 will result in error. The deprecation of v2 was first communicated in August 2018.

]]> December 05, 2019tag:google.com,2016:job-release-notes#December_05_20192019-12-05T00:00:00-08:00v3 

### Feature

CTS has launched a new [dashboard management tool](https://console.cloud.google.com/talent-solution). This new improvement provides visual data to give you more insight into:

  1. How your job seekers are engaging with Job Search, by showing see top queries and locations by domain.
  2. Whether Job Search is properly configured for your application, by showing inconsistencies in your search API integration.
  3. Whether your client events are properly configured, by showing client events that you can correct or improve to take full advantage of Job Search's machine learning capabilities.

]]> December 03, 2019tag:google.com,2016:job-release-notes#December_03_20192019-12-03T00:00:00-08:00v3 

### Changed

JS has improved the algorithm for better street resolution coverage. This will give you more precise geolocation results when using commute search.

]]> November 15, 2019tag:google.com,2016:job-release-notes#November_15_20192019-11-15T00:00:00-08:00v3 

### Feature

The following fields have been added to SummarizedProfile: 

  * `group_id`
  * `application`
  * `assignment`



### Fixed

Bug fix: Required fields are now marked correctly in the BatchUpdateJobs reference documentation.

### Fixed

Bug fix: CTS has fixed a bug that caused deleted companies to be counted toward the company limit in a job distributor.

]]> November 01, 2019tag:google.com,2016:job-release-notes#November_01_20192019-11-01T00:00:00-07:00v3 

### Feature

CTS has added validation to `job.workHour`.`workHour` now allows hour values between (0-23), otherwise a 400 error is returned.

### Feature

New enum CONTACT_AUTOMATED_SYSTEM has been added to ProfileEventTypes.

### Feature

JS has added new field `query_language_code`.

]]> October 18, 2019tag:google.com,2016:job-release-notes#October_18_20192019-10-18T00:00:00-07:00v3 

### Fixed

Bug fix: Job Search has fixed an issue that caused only some jobs in a specific location to be returned, rather than all options matching the search query.

### Fixed

Bug fix: Job Search has fixed an issue that caused only some of the results to be returned when searching on the string "Chief accountant". All results to this query string are now returned.

]]> September 27, 2019tag:google.com,2016:job-release-notes#September_27_20192019-09-27T00:00:00-07:00v3 

### Fixed

Bug fix: CTS has fixed a bug that caused the job export tool to generate fewer results.

### Changed

All resource (Tenant, Job, Profile, and so on) Create/Update methods now return any duplicated resource names in a structured error response to ALREADY_EXIST errors.

]]> August 30, 2019tag:google.com,2016:job-release-notes#August_30_20192019-08-30T00:00:00-07:00v3 

### Changed

Job update time is now only tracked if the job was updated by a customer.

]]> August 16, 2019tag:google.com,2016:job-release-notes#August_16_20192019-08-16T00:00:00-07:00v3 

### Fixed

Bug fix: CTS has fixed a bug that caused information in the [`addresses`](https://cloud.google.com/talent-solution/job-search/docs/reference/rpc/google.cloud.talent.v4beta1#job) field to be appended to `structuredAddresses`.

]]> July 19, 2019tag:google.com,2016:job-release-notes#July_19_20192019-07-19T00:00:00-07:00v3 

### Changed

The maximum size of the [`customAttributes`](https://cloud.google.com/talent-solution/job-search/docs/reference/rest/v4beta1/JobQuery) filter field of a job has been increased from 3KB to 6KB.

]]> July 02, 2019tag:google.com,2016:job-release-notes#July_02_20192019-07-02T00:00:00-07:00v3 

### Feature

Cloud Talent Solution has launched a new [Batch API](https://cloud.google.com/talent-solution/job-search/docs/reference/rpc/google.cloud.talent.v4beta1#batchcreatejobsrequest).

### Fixed

Bug fix: Cloud Talent Solution has fixed an issue where UpdateJob failed with a 500 error if the job's name didn't have a `tenant_id`.

### Changed

New documentation added: Create an [expired job](https://cloud.google.com/talent-solution/job-search/docs/reference/rest/v4beta1/projects.jobs#Job).

### Fixed

Bug fix: Cloud Talent Solution has fixed issues related to histogramming custom attribute facets. An empty histogram expression now throws an error message.

### Changed

Cloud Talent Solution has added an exception for an invalid profile name.

]]> June 03, 2019tag:google.com,2016:job-release-notes#June_03_20192019-06-03T00:00:00-07:00v3 

### Feature

Cloud Talent Solution has launched new [Batch](https://cloud.google.com/talent-solution/job-search/docs/reference/rest/v4beta1/projects.jobs/batchDelete) API calls. These calls enable you to perform multiple operations at the same time. Note that Batch API calls only apply to Job resources and CTS does not guarantee how quickly they will be reflected in search or recommendation responses.

### Fixed

Bug fix: Compensation filters are now able to account for jobs that have no compensation fields set.

### Fixed

Cloud Talent Solution fixed an issue that would not allow customers to upload expired jobs. You are now able to create an expired job and link it to any associated Application or Assignment records. When loading your historical data, input the following values:

  * `postingPublishTime`=[timestamp when the job was created]
  * `postingExpireTime`=[timestamp when the job was closed]
  * `requisitionState`=[FILLED, LOST, CLOSED]

]]> May 14, 2019tag:google.com,2016:job-release-notes#May_14_20192019-05-14T00:00:00-07:00v3 

### Feature

Cloud Talent Solution has launched the v4beta1 version of the API. You can download these libraries from our Client Libraries page.

### Feature

Cloud Talent Solution has updated it's documentation to include more code samples, and better structured examples on how to use the APIs.

### Changed

Cloud Talent Solution has added validation checks on timestamp related fields on the job and profile entities.

### Changed

Customers can now set the `group_id` field with their values, rather than having to use the Cloud Talent Solution auto-generated values for this field.

]]> April 26, 2019tag:google.com,2016:job-release-notes#April_26_20192019-04-26T00:00:00-07:00v3 

### Fixed

Cloud Talent Solution has fixed issues causing 500 status messages to be returned due to discrepancies in the Profile object.

### Changed

Cloud Talent Solution now allows you to define your own `group_id` to identify the same candidate across multiple profiles.

### Fixed

Cloud Talent Solution fixed issues causing the `excludedJobs` list in the search API to work incorrectly.

]]> March 15, 2019tag:google.com,2016:job-release-notes#March_15_20192019-03-15T00:00:00-07:00v3 

### Changed

For invalid histogram expressions Cloud Talent Solution will now return a 400 response instead of a 500 response.

]]>
