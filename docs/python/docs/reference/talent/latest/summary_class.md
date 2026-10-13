---
url: https://docs.cloud.google.com/python/docs/reference/talent/latest/summary_class/
title: Package Classes (2.22.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:33:06.242669+00:00
---

# Package Classes (2.22.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/talent/latest/summary_class/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Package Classes (2.22.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.22.0 (latest)  2.21.0  2.20.0  2.19.0  2.18.0  2.17.2  2.16.0  2.15.0  2.14.1  2.13.5  2.12.0  2.11.1  2.10.1  2.9.1  2.8.0  2.7.3  2.6.0  2.5.2  2.4.0  2.3.0  2.2.1  2.1.0  2.0.0  1.0.2  0.6.3  0.5.0  0.4.0  0.3.0 

Summary of entries of Classes for talent.

## Classes 

### [CompanyServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.company_service.CompanyServiceAsyncClient)

A service that handles company management, including CRUD and enumeration.

### [CompanyServiceClient](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.company_service.CompanyServiceClient)

A service that handles company management, including CRUD and enumeration.

### [ListCompaniesAsyncPager](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.company_service.pagers.ListCompaniesAsyncPager)

A pager for iterating through `list_companies` requests.

This class thinly wraps an initial [ListCompaniesResponse](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.types.ListCompaniesResponse) object, and provides an `__aiter__` method to iterate through its `companies` field.

If there are more pages, the `__aiter__` method will make additional `ListCompanies` requests and continue to iterate through the `companies` field on the corresponding responses.

All the usual [ListCompaniesResponse](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.types.ListCompaniesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListCompaniesPager](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.company_service.pagers.ListCompaniesPager)

A pager for iterating through `list_companies` requests.

This class thinly wraps an initial [ListCompaniesResponse](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.types.ListCompaniesResponse) object, and provides an `__iter__` method to iterate through its `companies` field.

If there are more pages, the `__iter__` method will make additional `ListCompanies` requests and continue to iterate through the `companies` field on the corresponding responses.

All the usual [ListCompaniesResponse](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.types.ListCompaniesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [CompletionAsyncClient](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.completion.CompletionAsyncClient)

A service handles auto completion.

### [CompletionClient](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.completion.CompletionClient)

A service handles auto completion.

### [EventServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.event_service.EventServiceAsyncClient)

A service handles client event report.

### [EventServiceClient](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.event_service.EventServiceClient)

A service handles client event report.

### [JobServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.job_service.JobServiceAsyncClient)

A service handles job management, including job CRUD, enumeration and search.

### [JobServiceClient](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.job_service.JobServiceClient)

A service handles job management, including job CRUD, enumeration and search.

### [ListJobsAsyncPager](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.job_service.pagers.ListJobsAsyncPager)

A pager for iterating through `list_jobs` requests.

This class thinly wraps an initial [ListJobsResponse](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.types.ListJobsResponse) object, and provides an `__aiter__` method to iterate through its `jobs` field.

If there are more pages, the `__aiter__` method will make additional `ListJobs` requests and continue to iterate through the `jobs` field on the corresponding responses.

All the usual [ListJobsResponse](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.types.ListJobsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListJobsPager](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.job_service.pagers.ListJobsPager)

A pager for iterating through `list_jobs` requests.

This class thinly wraps an initial [ListJobsResponse](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.types.ListJobsResponse) object, and provides an `__iter__` method to iterate through its `jobs` field.

If there are more pages, the `__iter__` method will make additional `ListJobs` requests and continue to iterate through the `jobs` field on the corresponding responses.

All the usual [ListJobsResponse](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.types.ListJobsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [TenantServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.tenant_service.TenantServiceAsyncClient)

A service that handles tenant management, including CRUD and enumeration.

### [TenantServiceClient](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.tenant_service.TenantServiceClient)

A service that handles tenant management, including CRUD and enumeration.

### [ListTenantsAsyncPager](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.tenant_service.pagers.ListTenantsAsyncPager)

A pager for iterating through `list_tenants` requests.

This class thinly wraps an initial [ListTenantsResponse](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.types.ListTenantsResponse) object, and provides an `__aiter__` method to iterate through its `tenants` field.

If there are more pages, the `__aiter__` method will make additional `ListTenants` requests and continue to iterate through the `tenants` field on the corresponding responses.

All the usual [ListTenantsResponse](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.types.ListTenantsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListTenantsPager](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.tenant_service.pagers.ListTenantsPager)

A pager for iterating through `list_tenants` requests.

This class thinly wraps an initial [ListTenantsResponse](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.types.ListTenantsResponse) object, and provides an `__iter__` method to iterate through its `tenants` field.

If there are more pages, the `__iter__` method will make additional `ListTenants` requests and continue to iterate through the `tenants` field on the corresponding responses.

All the usual [ListTenantsResponse](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.types.ListTenantsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

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

### [State](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.types.BatchOperationMetadata.State)

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

### [RoadTraffic](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.types.CommuteFilter.RoadTraffic)

The traffic density to use when calculating commute time.

### [CommuteMethod](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.types.CommuteMethod)

Method for commute. Walking, biking and wheelchair accessible transit is still in the Preview stage.

### [Company](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.types.Company)

A Company resource represents a company in the service. A company is the entity that owns job postings, that is, the hiring entity responsible for employing applicants for the job position.

### [DerivedInfo](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.types.Company.DerivedInfo)

Derived details about the company.

### [CompanySize](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.types.CompanySize)

An enum that represents the size of the company.

### [CompensationFilter](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.types.CompensationFilter)

Filter on job compensation type and amount.

### [FilterType](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.types.CompensationFilter.FilterType)

Specify the type of filtering.
    
    
        See
        <xref uid="google.cloud.talent.v4.CompensationInfo.CompensationEntry">CompensationInfo.CompensationEntry</xref>
        for definition of base compensation entry.
    UNIT_AND_AMOUNT (2):
        Filter by `base compensation entry's` unit and amount /
        range. A job is a match if and only if the job contains a
        base CompensationEntry, and the base entry's unit matches
        provided
        <xref uid="google.cloud.talent.v4.CompensationInfo.CompensationUnit">CompensationUnit</xref>
        and amount or range overlaps with provided
        <xref uid="google.cloud.talent.v4.CompensationInfo.CompensationRange">CompensationRange</xref>.
    
        See
        <xref uid="google.cloud.talent.v4.CompensationInfo.CompensationEntry">CompensationInfo.CompensationEntry</xref>
        for definition of base compensation entry.
    
        Set exactly one
        <xref uid="google.cloud.talent.v4.CompensationFilter.units">units</xref> and
        populate
        <xref uid="google.cloud.talent.v4.CompensationFilter.range">range</xref>.
    ANNUALIZED_BASE_AMOUNT (3):
        Filter by annualized base compensation amount and
        `base compensation entry's` unit. Populate
        <xref uid="google.cloud.talent.v4.CompensationFilter.range">range</xref> and
        zero or more
        <xref uid="google.cloud.talent.v4.CompensationFilter.units">units</xref>.
    ANNUALIZED_TOTAL_AMOUNT (4):
        Filter by annualized total compensation amount and
        `base compensation entry's` unit . Populate
        <xref uid="google.cloud.talent.v4.CompensationFilter.range">range</xref> and
        zero or more
        <xref uid="google.cloud.talent.v4.CompensationFilter.units">units</xref>.
    

### [CompensationInfo](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.types.CompensationInfo)

Job compensation details.

### [CompensationEntry](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.types.CompensationInfo.CompensationEntry)

A compensation entry that represents one component of compensation, such as base pay, bonus, or other compensation type.

Annualization: One compensation entry can be annualized if

  * it contains valid amount or range.
  * and its expected_units_per_year is set or can be derived. Its annualized range is determined as (amount or range) times expected_units_per_year.



This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [CompensationRange](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.types.CompensationInfo.CompensationRange)

Compensation range.

### [CompensationType](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.types.CompensationInfo.CompensationType)

The type of compensation.

For compensation amounts specified in non-monetary amounts, describe the compensation scheme in the CompensationEntry.description.

For example, tipping format is described in CompensationEntry.description (for example, "expect 15-20% tips based on customer bill.") and an estimate of the tips provided in CompensationEntry.amount or CompensationEntry.range ($10 per hour).

For example, equity is described in CompensationEntry.description (for example, "1% - 2% equity vesting over 4 years, 1 year cliff") and value estimated in CompensationEntry.amount or CompensationEntry.range. If no value estimate is possible, units are CompensationUnit.COMPENSATION_UNIT_UNSPECIFIED and then further clarified in CompensationEntry.description field.

### [CompensationUnit](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.types.CompensationInfo.CompensationUnit)

Pay frequency.

### [CompleteQueryRequest](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.types.CompleteQueryRequest)

Auto-complete parameters.

### [CompletionScope](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.types.CompleteQueryRequest.CompletionScope)

Enum to specify the scope of completion.

### [CompletionType](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.types.CompleteQueryRequest.CompletionType)

Enum to specify auto-completion topics.
    
    
        For
        <xref uid="google.cloud.talent.v4.CompleteQueryRequest.CompletionType.JOB_TITLE">CompletionType.JOB_TITLE</xref>
        type, only open jobs with the same
        <xref uid="google.cloud.talent.v4.CompleteQueryRequest.language_codes">language_codes</xref>
        are returned.
    COMPANY_NAME (2):
        Suggest company names for jobs autocomplete.
    
        For
        <xref uid="google.cloud.talent.v4.CompleteQueryRequest.CompletionType.COMPANY_NAME">CompletionType.COMPANY_NAME</xref>
        type, only companies having open jobs with the same
        <xref uid="google.cloud.talent.v4.CompleteQueryRequest.language_codes">language_codes</xref>
        are returned.
    COMBINED (3):
        Suggest both job titles and company names for jobs
        autocomplete.
    
        For
        <xref uid="google.cloud.talent.v4.CompleteQueryRequest.CompletionType.COMBINED">CompletionType.COMBINED</xref>
        type, only open jobs with the same
        <xref uid="google.cloud.talent.v4.CompleteQueryRequest.language_codes">language_codes</xref>
        or companies having open jobs with the same
        <xref uid="google.cloud.talent.v4.CompleteQueryRequest.language_codes">language_codes</xref>
        are returned.
    

### [CompleteQueryResponse](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.types.CompleteQueryResponse)

Response of auto-complete query.

### [CompletionResult](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.types.CompleteQueryResponse.CompletionResult)

Resource that represents completion results.

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

### [DeviceType](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.types.DeviceInfo.DeviceType)

An enumeration describing an API access portal and exposure mechanism.

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

### [HistogramEntry](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.types.HistogramQueryResult.HistogramEntry)

The abstract base class for a message.

### [HtmlSanitization](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.types.HtmlSanitization)

Option for HTML content sanitization on user input fields, for example, job description. By setting this option, user can determine whether and how sanitization is performed on these fields.

### [Job](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.types.Job)

A Job resource represents a job posting (also referred to as a "job listing" or "job requisition"). A job belongs to a Company, which is the hiring entity responsible for the job.

### [ApplicationInfo](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.types.Job.ApplicationInfo)

Application related details of a job posting.

### [CustomAttributesEntry](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.types.Job.CustomAttributesEntry)

The abstract base class for a message.

### [DerivedInfo](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.types.Job.DerivedInfo)

Derived details about the job posting.

### [ProcessingOptions](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.types.Job.ProcessingOptions)

Options for job processing.

### [JobBenefit](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.types.JobBenefit)

An enum that represents employee benefits included with the job.

### [JobCategory](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.types.JobCategory)

An enum that represents the categorization or primary focus of specific role. This value is different than the "industry" associated with a role, which is related to the categorization of the company listing the job.

### [JobEvent](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.types.JobEvent)

An event issued when a job seeker interacts with the application that implements Cloud Talent Solution.

### [JobEventType](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.types.JobEvent.JobEventType)

An enumeration of an event attributed to the behavior of the end user, such as a job seeker.

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

### [LocationType](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.types.Location.LocationType)

An enum which represents the type of a location.

### [LocationFilter](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.types.LocationFilter)

Geographic region of the search.

### [TelecommutePreference](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.types.LocationFilter.TelecommutePreference)

Specify whether to include telecommute jobs.

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

### [CustomRankingInfo](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.types.SearchJobsRequest.CustomRankingInfo)

Custom ranking information for SearchJobsRequest.

### [ImportanceLevel](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.types.SearchJobsRequest.CustomRankingInfo.ImportanceLevel)

The importance level for CustomRankingInfo.ranking_expression.

### [DiversificationLevel](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.types.SearchJobsRequest.DiversificationLevel)

Controls whether highly similar jobs are returned next to each other in the search results. Jobs are identified as highly similar based on their titles, job categories, and locations. Highly similar results are clustered so that only one representative job of the cluster is displayed to the job seeker higher up in the results, with the other jobs being displayed lower down in the results.

If you are using pageToken to page through the result set, latency might be lower but we can't guarantee that all results are returned. If you are using page offset, latency might be higher but all results are returned.

### [KeywordMatchMode](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.types.SearchJobsRequest.KeywordMatchMode)

Controls what keyword matching behavior the search has. When keyword matching is enabled, a keyword match returns jobs that may not match given category filters when there are matching keywords. For example, for the query "program manager" with KeywordMatchMode set to KEYWORD_MATCH_ALL, a job posting with the title "software developer," which doesn't fall into "program manager" ontology, and "program manager" appearing in its description will be surfaced.

For queries like "cloud" that don't contain title or location specific ontology, jobs with "cloud" keyword matches are returned regardless of this enum's value.

Use Company.keyword_searchable_job_custom_attributes if company-specific globally matched custom field/attribute string values are needed. Enabling keyword match improves recall of subsequent search requests.

### [RelevanceThreshold](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.types.SearchJobsRequest.RelevanceThreshold)

The relevance threshold of the search results. The higher relevance threshold is, the higher relevant results are shown and the less number of results are returned.

### [SearchMode](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.types.SearchJobsRequest.SearchMode)

A string-represented enumeration of the job search mode. The service operate differently for different modes of service.

### [SearchJobsResponse](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.types.SearchJobsResponse)

Response for SearchJob method.

### [CommuteInfo](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.types.SearchJobsResponse.CommuteInfo)

Commute details related to this job.

### [MatchingJob](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.types.SearchJobsResponse.MatchingJob)

Job entry with metadata inside SearchJobsResponse.

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

### [CompanyServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.company_service.CompanyServiceAsyncClient)

A service that handles company management, including CRUD and enumeration.

### [CompanyServiceClient](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.company_service.CompanyServiceClient)

A service that handles company management, including CRUD and enumeration.

### [ListCompaniesAsyncPager](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.company_service.pagers.ListCompaniesAsyncPager)

A pager for iterating through `list_companies` requests.

This class thinly wraps an initial [ListCompaniesResponse](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.types.ListCompaniesResponse) object, and provides an `__aiter__` method to iterate through its `companies` field.

If there are more pages, the `__aiter__` method will make additional `ListCompanies` requests and continue to iterate through the `companies` field on the corresponding responses.

All the usual [ListCompaniesResponse](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.types.ListCompaniesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListCompaniesPager](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.company_service.pagers.ListCompaniesPager)

A pager for iterating through `list_companies` requests.

This class thinly wraps an initial [ListCompaniesResponse](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.types.ListCompaniesResponse) object, and provides an `__iter__` method to iterate through its `companies` field.

If there are more pages, the `__iter__` method will make additional `ListCompanies` requests and continue to iterate through the `companies` field on the corresponding responses.

All the usual [ListCompaniesResponse](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.types.ListCompaniesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [CompletionAsyncClient](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.completion.CompletionAsyncClient)

A service handles auto completion.

### [CompletionClient](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.completion.CompletionClient)

A service handles auto completion.

### [EventServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.event_service.EventServiceAsyncClient)

A service handles client event report.

### [EventServiceClient](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.event_service.EventServiceClient)

A service handles client event report.

### [JobServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.job_service.JobServiceAsyncClient)

A service handles job management, including job CRUD, enumeration and search.

### [JobServiceClient](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.job_service.JobServiceClient)

A service handles job management, including job CRUD, enumeration and search.

### [ListJobsAsyncPager](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.job_service.pagers.ListJobsAsyncPager)

A pager for iterating through `list_jobs` requests.

This class thinly wraps an initial [ListJobsResponse](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.types.ListJobsResponse) object, and provides an `__aiter__` method to iterate through its `jobs` field.

If there are more pages, the `__aiter__` method will make additional `ListJobs` requests and continue to iterate through the `jobs` field on the corresponding responses.

All the usual [ListJobsResponse](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.types.ListJobsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListJobsPager](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.job_service.pagers.ListJobsPager)

A pager for iterating through `list_jobs` requests.

This class thinly wraps an initial [ListJobsResponse](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.types.ListJobsResponse) object, and provides an `__iter__` method to iterate through its `jobs` field.

If there are more pages, the `__iter__` method will make additional `ListJobs` requests and continue to iterate through the `jobs` field on the corresponding responses.

All the usual [ListJobsResponse](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.types.ListJobsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [SearchJobsAsyncPager](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.job_service.pagers.SearchJobsAsyncPager)

A pager for iterating through `search_jobs` requests.

This class thinly wraps an initial [SearchJobsResponse](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.types.SearchJobsResponse) object, and provides an `__aiter__` method to iterate through its `matching_jobs` field.

If there are more pages, the `__aiter__` method will make additional `SearchJobs` requests and continue to iterate through the `matching_jobs` field on the corresponding responses.

All the usual [SearchJobsResponse](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.types.SearchJobsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [SearchJobsForAlertAsyncPager](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.job_service.pagers.SearchJobsForAlertAsyncPager)

A pager for iterating through `search_jobs_for_alert` requests.

This class thinly wraps an initial [SearchJobsResponse](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.types.SearchJobsResponse) object, and provides an `__aiter__` method to iterate through its `matching_jobs` field.

If there are more pages, the `__aiter__` method will make additional `SearchJobsForAlert` requests and continue to iterate through the `matching_jobs` field on the corresponding responses.

All the usual [SearchJobsResponse](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.types.SearchJobsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [SearchJobsForAlertPager](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.job_service.pagers.SearchJobsForAlertPager)

A pager for iterating through `search_jobs_for_alert` requests.

This class thinly wraps an initial [SearchJobsResponse](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.types.SearchJobsResponse) object, and provides an `__iter__` method to iterate through its `matching_jobs` field.

If there are more pages, the `__iter__` method will make additional `SearchJobsForAlert` requests and continue to iterate through the `matching_jobs` field on the corresponding responses.

All the usual [SearchJobsResponse](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.types.SearchJobsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [SearchJobsPager](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.job_service.pagers.SearchJobsPager)

A pager for iterating through `search_jobs` requests.

This class thinly wraps an initial [SearchJobsResponse](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.types.SearchJobsResponse) object, and provides an `__iter__` method to iterate through its `matching_jobs` field.

If there are more pages, the `__iter__` method will make additional `SearchJobs` requests and continue to iterate through the `matching_jobs` field on the corresponding responses.

All the usual [SearchJobsResponse](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.types.SearchJobsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [TenantServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.tenant_service.TenantServiceAsyncClient)

A service that handles tenant management, including CRUD and enumeration.

### [TenantServiceClient](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.tenant_service.TenantServiceClient)

A service that handles tenant management, including CRUD and enumeration.

### [ListTenantsAsyncPager](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.tenant_service.pagers.ListTenantsAsyncPager)

A pager for iterating through `list_tenants` requests.

This class thinly wraps an initial [ListTenantsResponse](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.types.ListTenantsResponse) object, and provides an `__aiter__` method to iterate through its `tenants` field.

If there are more pages, the `__aiter__` method will make additional `ListTenants` requests and continue to iterate through the `tenants` field on the corresponding responses.

All the usual [ListTenantsResponse](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.types.ListTenantsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListTenantsPager](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.tenant_service.pagers.ListTenantsPager)

A pager for iterating through `list_tenants` requests.

This class thinly wraps an initial [ListTenantsResponse](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.types.ListTenantsResponse) object, and provides an `__iter__` method to iterate through its `tenants` field.

If there are more pages, the `__iter__` method will make additional `ListTenants` requests and continue to iterate through the `tenants` field on the corresponding responses.

All the usual [ListTenantsResponse](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.types.ListTenantsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [BatchCreateJobsRequest](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.types.BatchCreateJobsRequest)

Request to create a batch of jobs.

### [BatchDeleteJobsRequest](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.types.BatchDeleteJobsRequest)

Batch delete jobs request.

### [BatchOperationMetadata](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.types.BatchOperationMetadata)

Metadata used for long running operations returned by CTS batch APIs. It's used to replace `google.longrunning.Operation.metadata][google.longrunning.Operation.metadata]`.

### [State](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.types.BatchOperationMetadata.State)

### [BatchUpdateJobsRequest](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.types.BatchUpdateJobsRequest)

Request to update a batch of jobs.

### [ClientEvent](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.types.ClientEvent)

An event issued when an end user interacts with the application that implements Cloud Talent Solution. Providing this information improves the quality of results for the API clients, enabling the service to perform optimally. The number of events sent must be consistent with other calls, such as job searches, issued to the service by the client.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [CommuteFilter](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.types.CommuteFilter)

Parameters needed for commute search.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [RoadTraffic](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.types.CommuteFilter.RoadTraffic)

The traffic density to use when calculating commute time.

### [CommuteMethod](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.types.CommuteMethod)

Method for commute.

### [Company](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.types.Company)

A Company resource represents a company in the service. A company is the entity that owns job postings, that is, the hiring entity responsible for employing applicants for the job position.

### [DerivedInfo](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.types.Company.DerivedInfo)

Derived details about the company.

### [CompanySize](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.types.CompanySize)

An enum that represents the size of the company.

### [CompensationFilter](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.types.CompensationFilter)

Filter on job compensation type and amount.

### [FilterType](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.types.CompensationFilter.FilterType)

Specify the type of filtering.
    
    
        See
        <xref uid="google.cloud.talent.v4beta1.CompensationInfo.CompensationEntry">CompensationInfo.CompensationEntry</xref>
        for definition of base compensation entry.
    UNIT_AND_AMOUNT (2):
        Filter by `base compensation entry's` unit and amount /
        range. A job is a match if and only if the job contains a
        base CompensationEntry, and the base entry's unit matches
        provided
        <xref uid="google.cloud.talent.v4beta1.CompensationInfo.CompensationUnit">CompensationUnit</xref>
        and amount or range overlaps with provided
        <xref uid="google.cloud.talent.v4beta1.CompensationInfo.CompensationRange">CompensationRange</xref>.
    
        See
        <xref uid="google.cloud.talent.v4beta1.CompensationInfo.CompensationEntry">CompensationInfo.CompensationEntry</xref>
        for definition of base compensation entry.
    
        Set exactly one
        <xref uid="google.cloud.talent.v4beta1.CompensationFilter.units">units</xref>
        and populate
        <xref uid="google.cloud.talent.v4beta1.CompensationFilter.range">range</xref>.
    ANNUALIZED_BASE_AMOUNT (3):
        Filter by annualized base compensation amount and
        `base compensation entry's` unit. Populate
        <xref uid="google.cloud.talent.v4beta1.CompensationFilter.range">range</xref>
        and zero or more
        <xref uid="google.cloud.talent.v4beta1.CompensationFilter.units">units</xref>.
    ANNUALIZED_TOTAL_AMOUNT (4):
        Filter by annualized total compensation amount and
        `base compensation entry's` unit . Populate
        <xref uid="google.cloud.talent.v4beta1.CompensationFilter.range">range</xref>
        and zero or more
        <xref uid="google.cloud.talent.v4beta1.CompensationFilter.units">units</xref>.
    

### [CompensationInfo](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.types.CompensationInfo)

Job compensation details.

### [CompensationEntry](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.types.CompensationInfo.CompensationEntry)

A compensation entry that represents one component of compensation, such as base pay, bonus, or other compensation type.

Annualization: One compensation entry can be annualized if

  * it contains valid amount or range.
  * and its expected_units_per_year is set or can be derived. Its annualized range is determined as (amount or range) times expected_units_per_year.



This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [CompensationRange](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.types.CompensationInfo.CompensationRange)

Compensation range.

### [CompensationType](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.types.CompensationInfo.CompensationType)

The type of compensation.

For compensation amounts specified in non-monetary amounts, describe the compensation scheme in the CompensationEntry.description.

For example, tipping format is described in CompensationEntry.description (for example, "expect 15-20% tips based on customer bill.") and an estimate of the tips provided in CompensationEntry.amount or CompensationEntry.range ($10 per hour).

For example, equity is described in CompensationEntry.description (for example, "1% - 2% equity vesting over 4 years, 1 year cliff") and value estimated in CompensationEntry.amount or CompensationEntry.range. If no value estimate is possible, units are CompensationUnit.COMPENSATION_UNIT_UNSPECIFIED and then further clarified in CompensationEntry.description field.

### [CompensationUnit](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.types.CompensationInfo.CompensationUnit)

Pay frequency.

### [CompleteQueryRequest](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.types.CompleteQueryRequest)

Auto-complete parameters.

### [CompletionScope](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.types.CompleteQueryRequest.CompletionScope)

Enum to specify the scope of completion.

### [CompletionType](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.types.CompleteQueryRequest.CompletionType)

Enum to specify auto-completion topics.
    
    
        For
        <xref uid="google.cloud.talent.v4beta1.CompleteQueryRequest.CompletionType.JOB_TITLE">CompletionType.JOB_TITLE</xref>
        type, only open jobs with the same
        <xref uid="google.cloud.talent.v4beta1.CompleteQueryRequest.language_codes">language_codes</xref>
        are returned.
    COMPANY_NAME (2):
        Suggest company names for jobs autocomplete.
    
        For
        <xref uid="google.cloud.talent.v4beta1.CompleteQueryRequest.CompletionType.COMPANY_NAME">CompletionType.COMPANY_NAME</xref>
        type, only companies having open jobs with the same
        <xref uid="google.cloud.talent.v4beta1.CompleteQueryRequest.language_codes">language_codes</xref>
        are returned.
    COMBINED (3):
        Suggest both job titles and company names for jobs
        autocomplete.
    
        For
        <xref uid="google.cloud.talent.v4beta1.CompleteQueryRequest.CompletionType.COMBINED">CompletionType.COMBINED</xref>
        type, only open jobs with the same
        <xref uid="google.cloud.talent.v4beta1.CompleteQueryRequest.language_codes">language_codes</xref>
        or companies having open jobs with the same
        <xref uid="google.cloud.talent.v4beta1.CompleteQueryRequest.language_codes">language_codes</xref>
        are returned.
    

### [CompleteQueryResponse](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.types.CompleteQueryResponse)

Response of auto-complete query.

### [CompletionResult](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.types.CompleteQueryResponse.CompletionResult)

Resource that represents completion results.

### [CreateClientEventRequest](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.types.CreateClientEventRequest)

The report event request.

### [CreateCompanyRequest](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.types.CreateCompanyRequest)

The Request of the CreateCompany method.

### [CreateJobRequest](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.types.CreateJobRequest)

Create job request.

### [CreateTenantRequest](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.types.CreateTenantRequest)

The Request of the CreateTenant method.

### [CustomAttribute](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.types.CustomAttribute)

Custom attribute values that are either filterable or non-filterable.

### [DegreeType](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.types.DegreeType)

Educational degree level defined in International Standard Classification of Education (ISCED).

### [DeleteCompanyRequest](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.types.DeleteCompanyRequest)

Request to delete a company.

### [DeleteJobRequest](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.types.DeleteJobRequest)

Delete job request.

### [DeleteTenantRequest](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.types.DeleteTenantRequest)

Request to delete a tenant.

### [DeviceInfo](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.types.DeviceInfo)

Device information collected from the job seeker, candidate, or other entity conducting the job search. Providing this information improves the quality of the search results across devices.

### [DeviceType](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.types.DeviceInfo.DeviceType)

An enumeration describing an API access portal and exposure mechanism.

### [EmploymentType](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.types.EmploymentType)

An enum that represents the employment type of a job.

### [GetCompanyRequest](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.types.GetCompanyRequest)

Request for getting a company by name.

### [GetJobRequest](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.types.GetJobRequest)

Get job request.

### [GetTenantRequest](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.types.GetTenantRequest)

Request for getting a tenant by name.

### [HistogramQuery](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.types.HistogramQuery)

The histogram request.

### [HistogramQueryResult](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.types.HistogramQueryResult)

Histogram result that matches HistogramQuery specified in searches.

### [HistogramEntry](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.types.HistogramQueryResult.HistogramEntry)

The abstract base class for a message.

### [HtmlSanitization](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.types.HtmlSanitization)

Option for HTML content sanitization on user input fields, for example, job description. By setting this option, user can determine whether and how sanitization is performed on these fields.

### [Job](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.types.Job)

A Job resource represents a job posting (also referred to as a "job listing" or "job requisition"). A job belongs to a Company, which is the hiring entity responsible for the job.

### [ApplicationInfo](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.types.Job.ApplicationInfo)

Application related details of a job posting.

### [CustomAttributesEntry](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.types.Job.CustomAttributesEntry)

The abstract base class for a message.

### [DerivedInfo](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.types.Job.DerivedInfo)

Derived details about the job posting.

### [ProcessingOptions](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.types.Job.ProcessingOptions)

Options for job processing.

### [JobBenefit](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.types.JobBenefit)

An enum that represents employee benefits included with the job.

### [JobCategory](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.types.JobCategory)

An enum that represents the categorization or primary focus of specific role. This value is different than the "industry" associated with a role, which is related to the categorization of the company listing the job.

### [JobEvent](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.types.JobEvent)

An event issued when a job seeker interacts with the application that implements Cloud Talent Solution.

### [JobEventType](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.types.JobEvent.JobEventType)

An enumeration of an event attributed to the behavior of the end user, such as a job seeker.

### [JobLevel](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.types.JobLevel)

An enum that represents the required experience level required for the job.

### [JobOperationResult](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.types.JobOperationResult)

The result of JobService.BatchCreateJobs or JobService.BatchUpdateJobs APIs. It's used to replace `google.longrunning.Operation.response][google.longrunning.Operation.response]` in case of success.

### [JobResult](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.types.JobOperationResult.JobResult)

Mutation result of a job.

### [JobQuery](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.types.JobQuery)

The query required to perform a search query.

### [JobView](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.types.JobView)

An enum that specifies the job attributes that are returned in the MatchingJob.job or ListJobsResponse.jobs fields.

### [ListCompaniesRequest](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.types.ListCompaniesRequest)

List companies for which the client has ACL visibility.

### [ListCompaniesResponse](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.types.ListCompaniesResponse)

The List companies response object.

### [ListJobsRequest](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.types.ListJobsRequest)

List jobs request.

### [ListJobsResponse](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.types.ListJobsResponse)

List jobs response.

### [ListTenantsRequest](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.types.ListTenantsRequest)

List tenants for which the client has ACL visibility.

### [ListTenantsResponse](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.types.ListTenantsResponse)

The List tenants response object.

### [Location](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.types.Location)

A resource that represents a location with full geographic information.

### [LocationType](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.types.Location.LocationType)

An enum which represents the type of a location.

### [LocationFilter](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.types.LocationFilter)

Geographic region of the search.

### [TelecommutePreference](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.types.LocationFilter.TelecommutePreference)

Specify whether to include telecommute jobs.

### [PostingRegion](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.types.PostingRegion)

An enum that represents the job posting region. In most cases, job postings don't need to specify a region. If a region is given, jobs are eligible for searches in the specified region.
    
    
        Administrative area refers to top-level administrative
        subdivision of this country. For example, US state, IT
        region, UK constituent nation and JP prefecture.
    NATION (2):
        In addition to exact location matching, job is returned when
        <xref uid="google.cloud.talent.v4beta1.LocationFilter">LocationFilter</xref>
        in search query is in the same country as this job. For
        example, if a `NATION_WIDE` job is posted in "USA", it's
        returned if
        <xref uid="google.cloud.talent.v4beta1.LocationFilter">LocationFilter</xref>
        has 'Mountain View'.
    TELECOMMUTE (3):
        Job allows employees to work remotely
        (telecommute). If locations are provided with
        this value, the job is considered as having a
        location, but telecommuting is allowed.
    

### [RequestMetadata](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.types.RequestMetadata)

Meta information related to the job searcher or entity conducting the job search. This information is used to improve the performance of the service.

### [ResponseMetadata](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.types.ResponseMetadata)

Additional information returned to client, such as debugging information.

### [SearchJobsRequest](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.types.SearchJobsRequest)

The Request body of the `SearchJobs` call.

### [CustomRankingInfo](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.types.SearchJobsRequest.CustomRankingInfo)

Custom ranking information for SearchJobsRequest.

### [ImportanceLevel](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.types.SearchJobsRequest.CustomRankingInfo.ImportanceLevel)

The importance level for CustomRankingInfo.ranking_expression.

### [DiversificationLevel](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.types.SearchJobsRequest.DiversificationLevel)

Controls whether highly similar jobs are returned next to each other in the search results. Jobs are identified as highly similar based on their titles, job categories, and locations. Highly similar results are clustered so that only one representative job of the cluster is displayed to the job seeker higher up in the results, with the other jobs being displayed lower down in the results.

### [KeywordMatchMode](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.types.SearchJobsRequest.KeywordMatchMode)

Controls what keyword matching behavior the search has. When keyword matching is enabled, a keyword match returns jobs that may not match given category filters when there are matching keywords. For example, for the query "program manager" with KeywordMatchMode set to KEYWORD_MATCH_ALL, a job posting with the title "software developer," which doesn't fall into "program manager" ontology, and "program manager" appearing in its description will be surfaced.

For queries like "cloud" that don't contain title or location specific ontology, jobs with "cloud" keyword matches are returned regardless of this enum's value.

Use Company.keyword_searchable_job_custom_attributes if company-specific globally matched custom field/attribute string values are needed. Enabling keyword match improves recall of subsequent search requests.

### [RelevanceThreshold](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.types.SearchJobsRequest.RelevanceThreshold)

The relevance threshold of the search results. The higher relevance threshold is, the higher relevant results are shown and the less number of results are returned.

### [SearchMode](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.types.SearchJobsRequest.SearchMode)

A string-represented enumeration of the job search mode. The service operate differently for different modes of service.

### [SearchJobsResponse](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.types.SearchJobsResponse)

Response for SearchJob method.

### [CommuteInfo](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.types.SearchJobsResponse.CommuteInfo)

Commute details related to this job.

### [MatchingJob](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.types.SearchJobsResponse.MatchingJob)

Job entry with metadata inside SearchJobsResponse.

### [SpellingCorrection](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.types.SpellingCorrection)

Spell check result.

### [Tenant](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.types.Tenant)

A Tenant resource represents a tenant in the service. A tenant is a group or entity that shares common access with specific privileges for resources like profiles. Customer may create multiple tenants to provide data isolation for different groups.

### [DataUsageType](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.types.Tenant.DataUsageType)

Enum that represents how user data owned by the tenant is used.

### [TimestampRange](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.types.TimestampRange)

Message representing a period of time between two timestamps.

### [UpdateCompanyRequest](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.types.UpdateCompanyRequest)

Request for updating a specified company.

### [UpdateJobRequest](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.types.UpdateJobRequest)

Update job request.

### [UpdateTenantRequest](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.types.UpdateTenantRequest)

Request for updating a specified tenant.

### [Visibility](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.types.Visibility)

Deprecated. All resources are only visible to the owner.

An enum that represents who has view access to the resource.

## Modules 

### [pagers](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.company_service.pagers)

API documentation for `talent_v4.services.company_service.pagers` module.

### [pagers](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.job_service.pagers)

API documentation for `talent_v4.services.job_service.pagers` module.

### [pagers](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.tenant_service.pagers)

API documentation for `talent_v4.services.tenant_service.pagers` module.

### [pagers](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.company_service.pagers)

API documentation for `talent_v4beta1.services.company_service.pagers` module.

### [pagers](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.job_service.pagers)

API documentation for `talent_v4beta1.services.job_service.pagers` module.

### [pagers](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.tenant_service.pagers)

API documentation for `talent_v4beta1.services.tenant_service.pagers` module.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
