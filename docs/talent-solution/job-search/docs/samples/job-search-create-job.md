---
url: https://docs.cloud.google.com/talent-solution/job-search/docs/samples/job-search-create-job/
title: Create job with client (v4beta1) \u00a0|\u00a0 Job Search \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:34:45.356706+00:00
---

# Create job with client (v4beta1)  |  Job Search  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/talent-solution/job-search/docs/samples/job-search-create-job/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Cloud Talent Solution ](https://docs.cloud.google.com/talent-solution/docs)
  * [ Job Search ](https://docs.cloud.google.com/talent-solution/job-search/docs)
  * [ Samples ](https://docs.cloud.google.com/talent-solution/job-search/docs/samples)



#  Create job with client (v4beta1) Stay organized with collections  Save and categorize content based on your preferences. 

Create job with client.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Job basics](https://docs.cloud.google.com/talent-solution/job-search/docs/jobs)
  * [Job basics (v4beta1)](https://docs.cloud.google.com/talent-solution/job-search/v4beta1/docs/jobs)
  * [Quickstart: Create companies and jobs](https://docs.cloud.google.com/talent-solution/job-search/docs/quickstart-jobs-and-companies)
  * [Quickstart: Create companies and jobs (v4beta1)](https://docs.cloud.google.com/talent-solution/job-search/v4beta1/docs/quickstart-jobs-and-companies)



## Code sample

### Go

To learn how to install and use the client library for CTS, see [CTS client libraries](https://docs.cloud.google.com/talent-solution/job-search/docs/libraries). For more information, see the [CTS Go API reference documentation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/talent/latest/apiv4). 

To authenticate to CTS, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	talent "cloud.google.com/go/talent/apiv4beta1"
    	"cloud.google.com/go/talent/apiv4beta1/talentpb"
    )
    
    // createJob create a job as given.
    func createJob(w io.Writer, projectID, companyID, requisitionID, title, URI, description, address1, address2, languageCode string) (*talentpb.Job, error) {
    	ctx := context.Background()
    
    	// Initialize a jobService client.
    	c, err := talent.[NewJobClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/talent/latest/apiv4beta1.html#cloud_google_com_go_talent_apiv4beta1_JobClient_NewJobClient)(ctx)
    	if err != nil {
    		return nil, fmt.Errorf("talent.NewJobClient: %w", err)
    	}
    	defer c.Close()
    
    	jobToCreate := &talentpb.Job{
    		Company:       fmt.Sprintf("projects/%s/companies/%s", projectID, companyID),
    		RequisitionId: requisitionID,
    		Title:         title,
    		ApplicationInfo: &talentpb.Job_ApplicationInfo{
    			Uris: []string{URI},
    		},
    		Description:  description,
    		Addresses:    []string{address1, address2},
    		LanguageCode: languageCode,
    	}
    
    	// Construct a createJob request.
    	req := &talentpb.CreateJobRequest{
    		Parent: fmt.Sprintf("projects/%s", projectID),
    		Job:    jobToCreate,
    	}
    
    	resp, err := c.CreateJob(ctx, req)
    	if err != nil {
    		return nil, fmt.Errorf("CreateJob: %w", err)
    	}
    
    	fmt.Fprintf(w, "Created job: %q\n", resp.GetName())
    
    	return resp, nil
    }
    

### Node.js

To learn how to install and use the client library for CTS, see [CTS client libraries](https://docs.cloud.google.com/talent-solution/job-search/docs/libraries). For more information, see the [CTS Node.js API reference documentation](https://docs.cloud.google.com/nodejs/docs/reference/talent/latest). 

To authenticate to CTS, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    const talent = require('[@google-cloud/talent](https://docs.cloud.google.com/nodejs/docs/reference/talent/latest/overview.html)').v4;
    
    /**
     * Create Job
     *
     * @param projectId {string} Your Google Cloud Project ID
     * @param tenantId {string} Identifier of the Tenant
     */
    function sampleCreateJob(
      projectId,
      tenantId,
      companyName,
      requisitionId,
      title,
      description,
      jobApplicationUrl,
      addressOne,
      addressTwo,
      languageCode
    ) {
      const client = new talent.[JobServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/talent/latest/overview.html)();
      // const projectId = 'Your Google Cloud Project ID';
      // const tenantId = 'Your Tenant ID (using tenancy is optional)';
      // const companyName = 'Company name, e.g. projects/your-project/companies/company-id';
      // const requisitionId = 'Job requisition ID, aka Posting ID. Unique per job.';
      // const title = 'Software Engineer';
      // const description = 'This is a description of this <i>wonderful</i> job!';
      // const jobApplicationUrl = 'https://www.example.org/job-posting/123';
      // const addressOne = '1600 Amphitheatre Parkway, Mountain View, CA 94043';
      // const addressTwo = '111 8th Avenue, New York, NY 10011';
      // const languageCode = 'en-US';
      const formattedParent = client.tenantPath(projectId, tenantId);
      const uris = [jobApplicationUrl];
      const applicationInfo = {
        uris: uris,
      };
      const addresses = [addressOne, addressTwo];
      const job = {
        company: companyName,
        requisitionId: requisitionId,
        title: title,
        description: description,
        applicationInfo: applicationInfo,
        addresses: addresses,
        languageCode: languageCode,
      };
      const request = {
        parent: formattedParent,
        job: job,
      };
      client
        .createJob(request)
        .then(responses => {
          const response = responses[0];
          console.log(`Created job: ${response.name}`);
        })
        .catch(err => {
          console.error(err);
        });
    }
    

### Python

To learn how to install and use the client library for CTS, see [CTS client libraries](https://docs.cloud.google.com/talent-solution/job-search/docs/libraries). For more information, see the [CTS Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/talent/latest). 

To authenticate to CTS, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import talent
    
    
    def create_job(
        project_id,
        tenant_id,
        company_id,
        requisition_id,
        job_application_url,
    ):
        """Create Job"""
    
        client = talent.[JobServiceClient](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.job_service.JobServiceClient.html)()
    
        # project_id = 'Your Google Cloud Project ID'
        # tenant_id = 'Your Tenant ID (using tenancy is optional)'
        # company_id = 'Company name, e.g. projects/your-project/companies/company-id'
        # requisition_id = 'Job requisition ID, aka Posting ID. Unique per job.'
        # title = 'Software Engineer'
        # description = 'This is a description of this <i>wonderful</i> job!'
        # job_application_url = 'https://www.example.org/job-posting/123'
        # address_one = '1600 Amphitheatre Parkway, Mountain View, CA 94043'
        # address_two = '111 8th Avenue, New York, NY 10011'
        # language_code = 'en-US'
    
        if isinstance(project_id, bytes):
            project_id = project_id.decode("utf-8")
        if isinstance(tenant_id, bytes):
            tenant_id = tenant_id.decode("utf-8")
        if isinstance(company_id, bytes):
            company_id = company_id.decode("utf-8")
        if isinstance(requisition_id, bytes):
            requisition_id = requisition_id.decode("utf-8")
        if isinstance(job_application_url, bytes):
            job_application_url = job_application_url.decode("utf-8")
        parent = f"projects/{project_id}/tenants/{tenant_id}"
        uris = [job_application_url]
        application_info = {"uris": uris}
        addresses = [
            "1600 Amphitheatre Parkway, Mountain View, CA 94043",
            "111 8th Avenue, New York, NY 10011",
        ]
        job = {
            "company": company_id,
            "requisition_id": requisition_id,
            "title": "Software Developer",
            "description": "Develop, maintain the software solutions.",
            "application_info": application_info,
            "addresses": addresses,
            "language_code": "en-US",
        }
    
        response = client.[create_job](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.job_service.JobServiceClient.html#google_cloud_talent_v4_services_job_service_JobServiceClient_create_job)(parent=parent, job=job)
        print(f"Created job: {response.name}")
        return response.name
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=talentsolution). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
