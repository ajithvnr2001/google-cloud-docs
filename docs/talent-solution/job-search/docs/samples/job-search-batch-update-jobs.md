---
url: https://docs.cloud.google.com/talent-solution/job-search/docs/samples/job-search-batch-update-jobs/
title: Batch update jobs (v4beta1) \u00a0|\u00a0 Job Search \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:34:47.676905+00:00
---

# Batch update jobs (v4beta1)  |  Job Search  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/talent-solution/job-search/docs/samples/job-search-batch-update-jobs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Cloud Talent Solution ](https://docs.cloud.google.com/talent-solution/docs)
  * [ Job Search ](https://docs.cloud.google.com/talent-solution/job-search/docs)
  * [ Samples ](https://docs.cloud.google.com/talent-solution/job-search/docs/samples)



#  Batch update jobs (v4beta1) Stay organized with collections  Save and categorize content based on your preferences. 

Batch update jobs.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Batch operations](https://docs.cloud.google.com/talent-solution/job-search/docs/batch)



## Code sample

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
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=talentsolution). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
