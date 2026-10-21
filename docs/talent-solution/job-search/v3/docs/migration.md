---
url: https://docs.cloud.google.com/talent-solution/job-search/v3/docs/migration/
title: Migrating from Cloud Talent Solution v2beta1 to v2 \u00a0|\u00a0 Cloud Talent Solution - Job Search v3 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:53:31.940996+00:00
---

# Migrating from Cloud Talent Solution v2beta1 to v2  |  Cloud Talent Solution - Job Search v3  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/talent-solution/job-search/v3/docs/migration/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Cloud Talent Solution ](https://docs.cloud.google.com/talent-solution/docs)
  * [ Job Search ](https://docs.cloud.google.com/talent-solution/job-search/docs)
  * [ Job Search v3 (deprecated) ](https://docs.cloud.google.com/talent-solution/job-search/v3/docs)



Send feedback 

#  Migrating from Cloud Talent Solution v2beta1 to v2 Stay organized with collections  Save and categorize content based on your preferences. 

**Beta**  
This is a Beta release of Cloud Talent Solution. This release is not covered by any SLA or deprecation policy and is not intended for real-time use in critical applications. 

This documents explains the steps and considerations involved when migrating from Cloud Talent Solution v2beta1 to v2.

## Processes

The general processes to create, read, update, delete and search for jobs remains the same.

## Changes to the Job object

  * Several fields within the Job object have been renamed. See the V2 version of the Job object for a full list of changes.
  * A new "Telecommute" type has been added to specify remote jobs.
  * Fields marked as deprecated in V2Beta1 have been removed from V2.
  * A new "CompensationInfo" field has been added to replace the existing compensation fields.
  * The Geolocations field has been renamed to the JobLocation field.



## Changes to Job indexing methods

### Job Creation

  * The field "disable_fast_process" has been removed. Creation calls will now be asynchronous by default.
  * A new field "disable_street_address_resolution" has been added. By setting this field, the service will not attempt to infer the actual street address of the job. This is primarily meant for staffing agencies, that do not want to specify the end employer.



### Job Update

  * The "Update" service endpoint has been renamed to "Patch".
  * The field "disable_fast_process" has been removed. Creation calls will now be asynchronous by default.
  * A new field "disable_street_address_resolution" has been added. By setting this field, the service will not attempt to infer the actual street address of the job. This is primarily meant for staffing agencies, who do not want to specify the end employer.



### Job Completion

  * The autocompletion method - "Complete(CompletionQuery)" autocompletion method has been renamed to "CompleteQuery(CompletionQuery)".
  * The response of this function has also been renamed to "CompleteQueryResponse".



## Changes to Search methods

  * The SearchFeaturedJobs and searchJobsForAlert methods have been removed. Instead, a single search method can be used by specifying the search "Mode" field to generate the same behavior.
  * The method "ListCities" has been renamed to "ListCompanycities". Additionally, the parameter "ListCitiesRequest" has been renamed to "ListCompanyCitiesRequest" and the response has been changed from "ListCitiesResponse" to "ListCompanyCitiesResponse".
  * Several fields within the search method have been renamed. See the V2 version of the search method for a full list of changes.
  * A "MatchingJob" object has been added to host job and related search metadata such as jobSummary and snippets.
  * The type of search (regular, featured or search for the job alerts use case) is specified through the "Mode" field.
  * The "sort_by" field has been renamed to "order_by".
  * The "histogram_facets" is now returned as a part of the ResponseMetaData object.



## Changes to List methods

  * Several fields within the list methods have been renamed. See the V2 version of the list methods for a full list of changes.
  * The request and response objects have been renamed.
  * The method "ListCities" has been renamed to "ListCompanyCities". Please see ListCompanyCities for the new function signature.
  * The method "ListJobs" has been renamed to "ListCompanyJobs". Please see ListCompanyJobs for the new function signature.
  * The method "ListJobCategories" has been renamed to "ListCategories". Please see ListCompanyCities for the new function signature.



## Changes to Histograms

  * The function signature of the histogram request has changed. See the V2 version of Histogram for more details.



## Changes to ENUMERATION strings

  * The "JobCategory" ENUM string has been changed to "Category"
  * The LocationType class has several changes to the names of the different field types, such as "ADMIN1" being renamed to "ADMINISTRATIVE_AREA". Consult the v2 LocationType schema for the updated nomenclature.
  * A new Enumerated string "Mode" has been introduced to specify the mode of the search request. As a result, there will now be a single search method for the regular search, searching on featured jobs, and searching for the job alert use case.
  * The "PostingRegion" enumerated string has been renamed to "Region".
  * A "Telecommute" Enumerated string, has been added to specify the telecommute attributes of a job.
  * The TimeRange enumerated string has been renamed to "DateRange". See the DateRange enumerated string for field details.
  * A new Enumerated string has been added to specify the Geolocation Type. See Geolocation.LocationType for more details.



## Changes to the Jobs Analytic Framework messages (through Pub/Sub)

  * Several fields within the ClientEvent object have been renamed. See the V2 version of the ClientEvent object for a full list of changes.
  * A "SENT_CV" event type has been added.
  * The event_details field and the UserId field have been removed.
  * The Related_job_ids field has been renamed to related_job_names. However, this field still takes only the jobIds returned by the search as an accepted value.
  * The version field has been removed.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
