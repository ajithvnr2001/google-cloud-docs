---
url: https://docs.cloud.google.com/talent-solution/job-search/docs/batch/
title: Batch operations \u00a0|\u00a0 Job Search \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:34:28.157555+00:00
---

# Batch operations  |  Job Search  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/talent-solution/job-search/docs/batch/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Cloud Talent Solution ](https://docs.cloud.google.com/talent-solution/docs)
  * [ Job Search ](https://docs.cloud.google.com/talent-solution/job-search/docs)
  * [ Guides ](https://docs.cloud.google.com/talent-solution/job-search/docs/basics)



Send feedback 

#  Batch operations Stay organized with collections  Save and categorize content based on your preferences. 

Cloud Talent Solution supports asynchronous batch operations, which allows you to put multiple API calls into a single HTTP request. The returned response type is `google.longrunning.operation`. The detailed status of the batch operation can be retrieved by calling the `GetOperation` method using the [`name`](https://docs.cloud.google.com/talent-solution/job-search/docs/reference/rpc/google.longrunning#getoperationrequest) field in `google.longrunning.operation`.

Using batching yields decreased latency in the API response time and higher throughput. Note that successfully receiving a batch API response indicates only that the batch request has been created. Actual data processing is done asynchronously. Batch operations created more than 30 days ago will be no longer accessible by the `GetOperation` method.

**Each batch is limited to 200 requests**.

## Batch operation progress indicator

The `google.longrunning.operation` created by calling the batch create or update method falls under one of the following states:

  * STATE_UNSPECIFIED (the default value)
  * INITIALIZING
  * PROCESSING
  * SUCCEEDED
  * FAILED



In state INITIALIZING, `success_count`, `failure_count`, and `total_count` fields are set to 0. If the operation is in state PROCESSING the `success_count` and `failure_count` may increase. In state SUCCEEDED, `success_count` \+ `failure_count` is always equal to `total_count`, and `success_count` > 0\. In state FAILED, `success_count` is always 0.

**Note:** Only the `GetOperation` method is currently only supported on the `google.longrunning.operation` resource.

## Batch create jobs

The following code sample demonstrates how to batch create jobs:

### Python

To learn how to install and use the client library for CTS, see [CTS client libraries](https://docs.cloud.google.com/talent-solution/job-search/docs/libraries). For more information, see the [CTS Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/talent/latest). 

To authenticate to CTS, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import talent
    
    
    def batch_create_jobs(
        project_id,
        tenant_id,
        company_name_one,
        requisition_id_one,
        title_one,
        description_one,
        job_application_url_one,
        address_one,
        language_code_one,
        company_name_two,
        requisition_id_two,
        title_two,
        description_two,
        job_application_url_two,
        address_two,
        language_code_two,
    ):
        """
        Batch Create Jobs
    
        Args:
          project_id Your Google Cloud Project ID
          tenant_id Identifier of the Tenant
        """
    
        client = talent.[JobServiceClient](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.job_service.JobServiceClient.html)()
    
        # project_id = 'Your Google Cloud Project ID'
        # tenant_id = 'Your Tenant ID (using tenancy is optional)'
        # company_name_one = 'Company name, e.g. projects/your-project/companies/company-id'
        # requisition_id_one = 'Job requisition ID, aka Posting ID. Unique per job.'
        # title_one = 'Software Engineer'
        # description_one = 'This is a description of this <i>wonderful</i> job!'
        # job_application_url_one = 'https://www.example.org/job-posting/123'
        # address_one = '1600 Amphitheatre Parkway, Mountain View, CA 94043'
        # language_code_one = 'en-US'
        # company_name_two = 'Company name, e.g. projects/your-project/companies/company-id'
        # requisition_id_two = 'Job requisition ID, aka Posting ID. Unique per job.'
        # title_two = 'Quality Assurance'
        # description_two = 'This is a description of this <i>wonderful</i> job!'
        # job_application_url_two = 'https://www.example.org/job-posting/123'
        # address_two = '111 8th Avenue, New York, NY 10011'
        # language_code_two = 'en-US'
    
        if isinstance(project_id, bytes):
            project_id = project_id.decode("utf-8")
        if isinstance(tenant_id, bytes):
            tenant_id = tenant_id.decode("utf-8")
        if isinstance(company_name_one, bytes):
            company_name_one = company_name_one.decode("utf-8")
        if isinstance(requisition_id_one, bytes):
            requisition_id_one = requisition_id_one.decode("utf-8")
        if isinstance(title_one, bytes):
            title_one = title_one.decode("utf-8")
        if isinstance(description_one, bytes):
            description_one = description_one.decode("utf-8")
        if isinstance(job_application_url_one, bytes):
            job_application_url_one = job_application_url_one.decode("utf-8")
        if isinstance(address_one, bytes):
            address_one = address_one.decode("utf-8")
        if isinstance(language_code_one, bytes):
            language_code_one = language_code_one.decode("utf-8")
        if isinstance(company_name_two, bytes):
            company_name_two = company_name_two.decode("utf-8")
        if isinstance(requisition_id_two, bytes):
            requisition_id_two = requisition_id_two.decode("utf-8")
        if isinstance(title_two, bytes):
            title_two = title_two.decode("utf-8")
        if isinstance(description_two, bytes):
            description_two = description_two.decode("utf-8")
        if isinstance(job_application_url_two, bytes):
            job_application_url_two = job_application_url_two.decode("utf-8")
        if isinstance(address_two, bytes):
            address_two = address_two.decode("utf-8")
        if isinstance(language_code_two, bytes):
            language_code_two = language_code_two.decode("utf-8")
        parent = f"projects/{project_id}/tenants/{tenant_id}"
        uris = [job_application_url_one]
        application_info = {"uris": uris}
        addresses = [address_one]
        jobs_element = {
            "company": company_name_one,
            "requisition_id": requisition_id_one,
            "title": title_one,
            "description": description_one,
            "application_info": application_info,
            "addresses": addresses,
            "language_code": language_code_one,
        }
        uris_2 = [job_application_url_two]
        application_info_2 = {"uris": uris_2}
        addresses_2 = [address_two]
        jobs_element_2 = {
            "company": company_name_two,
            "requisition_id": requisition_id_two,
            "title": title_two,
            "description": description_two,
            "application_info": application_info_2,
            "addresses": addresses_2,
            "language_code": language_code_two,
        }
        jobs = [jobs_element, jobs_element_2]
    
        operation = client.[batch_create_jobs](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.job_service.JobServiceClient.html#google_cloud_talent_v4_services_job_service_JobServiceClient_batch_create_jobs)(parent=parent, jobs=jobs)
    
        print("Waiting for operation to complete...")
        response = operation.result(90)
    
        print(f"Batch response: {response}")
    
    

## Batch update jobs

The following code sample demonstrates how to batch update jobs:

### Python

To learn how to install and use the client library for CTS, see [CTS client libraries](https://docs.cloud.google.com/talent-solution/job-search/docs/libraries). For more information, see the [CTS Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/talent/latest). 

To authenticate to CTS, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import talent
    
    
    def batch_update_jobs(
        project_id,
        tenant_id,
        job_name_one,
        company_name_one,
        requisition_id_one,
        title_one,
        description_one,
        job_application_url_one,
        address_one,
        language_code_one,
        job_name_two,
        company_name_two,
        requisition_id_two,
        title_two,
        description_two,
        job_application_url_two,
        address_two,
        language_code_two,
    ):
        """
        Batch Update Jobs
    
        Args:
          project_id Your Google Cloud Project ID
          tenant_id Identifier of the Tenant
        """
    
        client = talent.[JobServiceClient](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.job_service.JobServiceClient.html)()
    
        # project_id = 'Your Google Cloud Project ID'
        # tenant_id = 'Your Tenant ID (using tenancy is optional)'
        # job_name_one = 'job name, projects/your-project/tenants/tenant-id/jobs/job-id'
        # company_name_one = 'Company name, e.g. projects/your-project/companies/company-id'
        # requisition_id_one = 'Job requisition ID, aka Posting ID. Unique per job.'
        # title_one = 'Software Engineer'
        # description_one = 'This is a description of this <i>wonderful</i> job!'
        # job_application_url_one = 'https://www.example.org/job-posting/123'
        # address_one = '1600 Amphitheatre Parkway, Mountain View, CA 94043'
        # language_code_one = 'en-US'
        # job_name_two = 'job name, projects/your-project/tenants/tenant-id/jobs/job-id'
        # company_name_two = 'Company name, e.g. projects/your-project/companies/company-id'
        # requisition_id_two = 'Job requisition ID, aka Posting ID. Unique per job.'
        # title_two = 'Quality Assurance'
        # description_two = 'This is a description of this <i>wonderful</i> job!'
        # job_application_url_two = 'https://www.example.org/job-posting/123'
        # address_two = '111 8th Avenue, New York, NY 10011'
        # language_code_two = 'en-US'
    
        if isinstance(project_id, bytes):
            project_id = project_id.decode("utf-8")
        if isinstance(tenant_id, bytes):
            tenant_id = tenant_id.decode("utf-8")
        if isinstance(job_name_one, bytes):
            job_name_one = job_name_one.decode("utf-8")
        if isinstance(company_name_one, bytes):
            company_name_one = company_name_one.decode("utf-8")
        if isinstance(requisition_id_one, bytes):
            requisition_id_one = requisition_id_one.decode("utf-8")
        if isinstance(title_one, bytes):
            title_one = title_one.decode("utf-8")
        if isinstance(description_one, bytes):
            description_one = description_one.decode("utf-8")
        if isinstance(job_application_url_one, bytes):
            job_application_url_one = job_application_url_one.decode("utf-8")
        if isinstance(address_one, bytes):
            address_one = address_one.decode("utf-8")
        if isinstance(language_code_one, bytes):
            language_code_one = language_code_one.decode("utf-8")
        if isinstance(job_name_two, bytes):
            job_name_two = job_name_two.decode("utf-8")
        if isinstance(company_name_two, bytes):
            company_name_two = company_name_two.decode("utf-8")
        if isinstance(requisition_id_two, bytes):
            requisition_id_two = requisition_id_two.decode("utf-8")
        if isinstance(title_two, bytes):
            title_two = title_two.decode("utf-8")
        if isinstance(description_two, bytes):
            description_two = description_two.decode("utf-8")
        if isinstance(job_application_url_two, bytes):
            job_application_url_two = job_application_url_two.decode("utf-8")
        if isinstance(address_two, bytes):
            address_two = address_two.decode("utf-8")
        if isinstance(language_code_two, bytes):
            language_code_two = language_code_two.decode("utf-8")
        parent = f"projects/{project_id}/tenants/{tenant_id}"
        uris = [job_application_url_one]
        application_info = {"uris": uris}
        addresses = [address_one]
        jobs_element = talent.[Job](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.types.Job.html)(
            name=job_name_one,
            company=company_name_one,
            requisition_id=requisition_id_one,
            title=title_one,
            description=description_one,
            application_info=application_info,
            addresses=addresses,
            language_code=language_code_one,
        )
    
        uris_2 = [job_application_url_two]
        application_info_2 = {"uris": uris_2}
        addresses_2 = [address_two]
        jobs_element_2 = talent.[Job](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.types.Job.html)(
            name=job_name_two,
            company=company_name_two,
            requisition_id=requisition_id_two,
            title=title_two,
            description=description_two,
            application_info=application_info_2,
            addresses=addresses_2,
            language_code=language_code_two,
        )
    
        jobs = [jobs_element, jobs_element_2]
    
        operation = client.[batch_update_jobs](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.job_service.JobServiceClient.html#google_cloud_talent_v4_services_job_service_JobServiceClient_batch_update_jobs)(parent=parent, jobs=jobs)
    
        print("Waiting for operation to complete...")
        response = operation.result(90)
    
        print(f"Batch response: {response}")
    
    

## Batch delete jobs

The following code sample demonstrates how to batch delete jobs:

### Node.js

To learn how to install and use the client library for CTS, see [CTS client libraries](https://docs.cloud.google.com/talent-solution/job-search/docs/libraries). For more information, see the [CTS Node.js API reference documentation](https://docs.cloud.google.com/nodejs/docs/reference/talent/latest). 

To authenticate to CTS, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    const talent = require('[@google-cloud/talent](https://docs.cloud.google.com/nodejs/docs/reference/talent/latest/overview.html)').v4;
    
    /**
     * Batch delete jobs using a filter
     *
     * @param projectId {string} Your Google Cloud Project ID
     * @param tenantId {string} Identifier of the Tenantd
     * @param filter {string} The filter string specifies the jobs to be deleted.
     * For example:
     * companyName = "projects/api-test-project/companies/123" AND equisitionId = "req-1"
     */
    function sampleBatchDeleteJobs(projectId, tenantId, filter) {
      const client = new talent.[JobServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/talent/latest/overview.html)();
      // const projectId = 'Your Google Cloud Project ID';
      // const tenantId = 'Your Tenant ID (using tenancy is optional)';
      // const filter = '[Query]';
      const formattedParent = client.tenantPath(projectId, tenantId);
      const request = {
        parent: formattedParent,
        filter: filter,
      };
      client.batchDeleteJobs(request).catch(err => {
        console.error(err);
      });
      console.log('Batch deleted jobs from filter');
    }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 

  * ### Products and pricing

    * [ See all products ](https://cloud.google.com/products/)
    * [ Google Cloud pricing ](https://cloud.google.com/pricing/)
    * [ Google Cloud Marketplace ](https://cloud.google.com/marketplace/)
    * [ Contact sales ](https://cloud.google.com/contact/)
  * ### Support

    * [ Community forums ](https://discuss.google.dev/c/google-cloud/14/)
    * [ Support ](https://cloud.google.com/support-hub/)
    * [ Release Notes ](https://docs.cloud.google.com/release-notes)
    * [ System status ](https://status.cloud.google.com)
  * ### Resources

    * [ GitHub ](https://github.com/googlecloudPlatform/)
    * [ Getting Started with Google Cloud ](https://docs.cloud.google.com/docs/get-started/)
    * [ Code samples ](https://docs.cloud.google.com/docs/samples)
    * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture/)
    * [ Training and Certification ](https://cloud.google.com/learn/training/)
    * [ Builders Hub ](https://me.developers.google.com/)
  * ### Engage

    * [ Blog ](https://cloud.google.com/blog/)
    * [ Events ](https://cloud.google.com/events/)
    * [ X (Twitter) ](https://x.com/googlecloud)
    * [ Google Cloud on YouTube ](https://www.youtube.com/googlecloud)
    * [ Google Cloud Tech on YouTube ](https://www.youtube.com/googlecloudplatform)



[ ![Google Developers](https://www.gstatic.com/devrel-devsite/prod/v5a0f9ff8b593048661361a49e11ab98a8b1ac025e19e60e6189f2b56796f8a43/clouddocs/images/lockup-google-for-developers.svg)](https://developers.google.com/)

  * [ Android ](https://developer.android.com/)
  * [ Chrome ](https://developer.chrome.com/)
  * [ Firebase ](https://firebase.google.com/)
  * [ Google AI ](https://ai.google.com/)



  * [ About Google ](https://about.google/)
  * [ Privacy ](https://policies.google.com/privacy)
  * [ Site terms ](https://policies.google.com/terms?hl=en)
  * [ Google Cloud terms ](https://cloud.google.com/product-terms)
  * Manage cookies 
  * [ Our third decade of climate action: join us ](https://cloud.google.com/sustainability)
  * Sign up for the Google Cloud newsletter [ Subscribe ](https://cloud.google.com/newsletter/)



  * English
  * Deutsch
  * Español
  * Español – América Latina
  * Français
  * Indonesia
  * Italiano
  * Português
  * Português – Brasil
  * עברית
  * 中文 – 简体
  * 中文 – 繁體
  * 日本語
  * 한국어


