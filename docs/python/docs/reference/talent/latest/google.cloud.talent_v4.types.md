---
url: https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.types
title: Package types (2.22.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:33:12.495067+00:00
---

# Package types (2.22.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.types

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Package types (2.22.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.22.0 (latest)  2.21.0  2.20.0  2.19.0  2.18.0  2.17.2  2.16.0  2.15.0  2.14.1  2.13.5  2.12.0  2.11.1  2.10.1  2.9.1  2.8.0  2.7.3  2.6.0  2.5.2  2.4.0  2.3.0  2.2.1  2.1.0  2.0.0  1.0.2  0.6.3  0.5.0  0.4.0  0.3.0 

API documentation for `talent_v4.types` package.

## Classes 

### [BatchCreateJobsRequest](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.types.BatchCreateJobsRequest)

Request to create a batch of jobs.

### [BatchCreateJobsResponse](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.types.BatchCreateJobsResponse)

The result of JobService.BatchCreateJobs. It's used to replace `google.longrunning.Operation.response][google.longrunning.Operation.response]` in case of success.

### [BatchDeleteJobsRequest](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.types.BatchDeleteJobsRequest)

Request to delete a batch of jobs.

### [BatchDeleteJobsResponse](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.types.BatchDeleteJobsResponse)

The result of JobService.BatchDeleteJobs. It's used to replace `google.longrunning.Operation.response][google.longrunning.Operation.response]` in case of success.

### [BatchOperationMetadata](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.types.BatchOperationMetadata)

Metadata used for long running operations returned by CTS batch APIs. It's used to replace `google.longrunning.Operation.metadata][google.longrunning.Operation.metadata]`.

### [BatchUpdateJobsRequest](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.types.BatchUpdateJobsRequest)

Request to update a batch of jobs.

### [BatchUpdateJobsResponse](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.types.BatchUpdateJobsResponse)

The result of JobService.BatchUpdateJobs. It's used to replace `google.longrunning.Operation.response][google.longrunning.Operation.response]` in case of success.

### [ClientEvent](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.types.ClientEvent)

An event issued when an end user interacts with the application that implements Cloud Talent Solution. Providing this information improves the quality of results for the API clients, enabling the service to perform optimally. The number of events sent must be consistent with other calls, such as job searches, issued to the service by the client.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [CommuteFilter](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.types.CommuteFilter)

Parameters needed for commute search.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [CommuteMethod](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.types.CommuteMethod)

Method for commute. Walking, biking and wheelchair accessible transit is still in the Preview stage.

### [Company](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.types.Company)

A Company resource represents a company in the service. A company is the entity that owns job postings, that is, the hiring entity responsible for employing applicants for the job position.

### [CompanySize](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.types.CompanySize)

An enum that represents the size of the company.

### [CompensationFilter](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.types.CompensationFilter)

Filter on job compensation type and amount.

### [CompensationInfo](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.types.CompensationInfo)

Job compensation details.

### [CompleteQueryRequest](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.types.CompleteQueryRequest)

Auto-complete parameters.

### [CompleteQueryResponse](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.types.CompleteQueryResponse)

Response of auto-complete query.

### [CreateClientEventRequest](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.types.CreateClientEventRequest)

The report event request.

### [CreateCompanyRequest](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.types.CreateCompanyRequest)

The Request of the CreateCompany method.

### [CreateJobRequest](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.types.CreateJobRequest)

Create job request.

### [CreateTenantRequest](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.types.CreateTenantRequest)

The Request of the CreateTenant method.

### [CustomAttribute](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.types.CustomAttribute)

Custom attribute values that are either filterable or non-filterable.

### [DegreeType](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.types.DegreeType)

Educational degree level defined in International Standard Classification of Education (ISCED).

### [DeleteCompanyRequest](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.types.DeleteCompanyRequest)

Request to delete a company.

### [DeleteJobRequest](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.types.DeleteJobRequest)

Delete job request.

### [DeleteTenantRequest](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.types.DeleteTenantRequest)

Request to delete a tenant.

### [DeviceInfo](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.types.DeviceInfo)

Device information collected from the job seeker, candidate, or other entity conducting the job search. Providing this information improves the quality of the search results across devices.

### [EmploymentType](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.types.EmploymentType)

An enum that represents the employment type of a job.

### [GetCompanyRequest](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.types.GetCompanyRequest)

Request for getting a company by name.

### [GetJobRequest](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.types.GetJobRequest)

Get job request.

### [GetTenantRequest](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.types.GetTenantRequest)

Request for getting a tenant by name.

### [HistogramQuery](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.types.HistogramQuery)

The histogram request.

### [HistogramQueryResult](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.types.HistogramQueryResult)

Histogram result that matches HistogramQuery specified in searches.

### [HtmlSanitization](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.types.HtmlSanitization)

Option for HTML content sanitization on user input fields, for example, job description. By setting this option, user can determine whether and how sanitization is performed on these fields.

### [Job](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.types.Job)

A Job resource represents a job posting (also referred to as a "job listing" or "job requisition"). A job belongs to a Company, which is the hiring entity responsible for the job.

### [JobBenefit](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.types.JobBenefit)

An enum that represents employee benefits included with the job.

### [JobCategory](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.types.JobCategory)

An enum that represents the categorization or primary focus of specific role. This value is different than the "industry" associated with a role, which is related to the categorization of the company listing the job.

### [JobEvent](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.types.JobEvent)

An event issued when a job seeker interacts with the application that implements Cloud Talent Solution.

### [JobLevel](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.types.JobLevel)

An enum that represents the required experience level required for the job.

### [JobQuery](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.types.JobQuery)

The query required to perform a search query.

### [JobResult](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.types.JobResult)

Mutation result of a job from a batch operation.

### [JobView](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.types.JobView)

An enum that specifies the job attributes that are returned in the MatchingJob.job or ListJobsResponse.jobs fields.

### [ListCompaniesRequest](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.types.ListCompaniesRequest)

List companies for which the client has ACL visibility.

### [ListCompaniesResponse](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.types.ListCompaniesResponse)

The List companies response object.

### [ListJobsRequest](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.types.ListJobsRequest)

List jobs request.

### [ListJobsResponse](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.types.ListJobsResponse)

List jobs response.

### [ListTenantsRequest](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.types.ListTenantsRequest)

List tenants for which the client has ACL visibility.

### [ListTenantsResponse](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.types.ListTenantsResponse)

The List tenants response object.

### [Location](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.types.Location)

A resource that represents a location with full geographic information.

### [LocationFilter](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.types.LocationFilter)

Geographic region of the search.

### [PostingRegion](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.types.PostingRegion)

An enum that represents the job posting region. In most cases, job postings don't need to specify a region. If a region is given, jobs are eligible for searches in the specified region.
    
    
        Administrative area refers to top-level administrative
        subdivision of this country. For example, US state, IT
        region, UK constituent nation and JP prefecture.
    NATION (2):
        In addition to exact location matching, job is returned when
        <xref uid="google.cloud.talent.v4.LocationFilter">LocationFilter</xref> in
        search query is in the same country as this job. For
        example, if a `NATION_WIDE` job is posted in "USA", it's
        returned if
        <xref uid="google.cloud.talent.v4.LocationFilter">LocationFilter</xref> has
        'Mountain View'.
    TELECOMMUTE (3):
        Job allows employees to work remotely
        (telecommute). If locations are provided with
        this value, the job is considered as having a
        location, but telecommuting is allowed.
    

### [RequestMetadata](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.types.RequestMetadata)

Meta information related to the job searcher or entity conducting the job search. This information is used to improve the performance of the service.

### [ResponseMetadata](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.types.ResponseMetadata)

Additional information returned to client, such as debugging information.

### [SearchJobsRequest](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.types.SearchJobsRequest)

The Request body of the `SearchJobs` call.

### [SearchJobsResponse](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.types.SearchJobsResponse)

Response for SearchJob method.

### [SpellingCorrection](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.types.SpellingCorrection)

Spell check result.

### [Tenant](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.types.Tenant)

A Tenant resource represents a tenant in the service. A tenant is a group or entity that shares common access with specific privileges for resources like jobs. Customer may create multiple tenants to provide data isolation for different groups.

### [TimestampRange](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.types.TimestampRange)

Message representing a period of time between two timestamps.

### [UpdateCompanyRequest](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.types.UpdateCompanyRequest)

Request for updating a specified company.

### [UpdateJobRequest](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.types.UpdateJobRequest)

Update job request.

### [UpdateTenantRequest](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.types.UpdateTenantRequest)

Request for updating a specified tenant.

### [Visibility](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.types.Visibility)

Deprecated. All resources are only visible to the owner.

An enum that represents who has view access to the resource.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
