---
url: https://docs.cloud.google.com/talent-solution/job-search/docs/samples/job-search-get-job/
title: Get job with client (v4beta1) \u00a0|\u00a0 Job Search \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:58:49.518196+00:00
---

# Get job with client (v4beta1)  |  Job Search  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/talent-solution/job-search/docs/samples/job-search-get-job/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Cloud Talent Solution ](https://docs.cloud.google.com/talent-solution/docs)
  * [ Job Search ](https://docs.cloud.google.com/talent-solution/job-search/docs)
  * [ Samples ](https://docs.cloud.google.com/talent-solution/job-search/docs/samples)



#  Get job with client (v4beta1) Stay organized with collections  Save and categorize content based on your preferences. 

Get job with client.

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
    
    // getJob gets an existing job by its resource name.
    func getJob(w io.Writer, projectID, jobID string) (*talentpb.Job, error) {
    	ctx := context.Background()
    
    	// Initialize a jobService client.
    	c, err := talent.[NewJobClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/talent/latest/apiv4beta1.html#cloud_google_com_go_talent_apiv4beta1_JobClient_NewJobClient)(ctx)
    	if err != nil {
    		return nil, fmt.Errorf("talent.NewJobClient: %w", err)
    	}
    	defer c.Close()
    
    	// Construct a getJob request.
    	jobName := fmt.Sprintf("projects/%s/jobs/%s", projectID, jobID)
    	req := &talentpb.GetJobRequest{
    		// The resource name of the job to retrieve.
    		// The format is "projects/{project_id}/jobs/{job_id}".
    		Name: jobName,
    	}
    
    	resp, err := c.GetJob(ctx, req)
    	if err != nil {
    		return nil, fmt.Errorf("GetJob: %w", err)
    	}
    
    	fmt.Fprintf(w, "Job: %q\n", resp.GetName())
    	fmt.Fprintf(w, "Job title: %v\n", resp.GetTitle())
    
    	return resp, err
    }
    

### Node.js

To learn how to install and use the client library for CTS, see [CTS client libraries](https://docs.cloud.google.com/talent-solution/job-search/docs/libraries). For more information, see the [CTS Node.js API reference documentation](https://docs.cloud.google.com/nodejs/docs/reference/talent/latest). 

To authenticate to CTS, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    const talent = require('[@google-cloud/talent](https://docs.cloud.google.com/nodejs/docs/reference/talent/latest/overview.html)').v4;
    
    /** Get Job */
    function sampleGetJob(projectId, tenantId, jobId) {
      const client = new talent.[JobServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/talent/latest/overview.html)();
      // const projectId = 'Your Google Cloud Project ID';
      // const tenantId = 'Your Tenant ID (using tenancy is optional)';
      // const jobId = 'Job ID';
      const formattedName = client.jobPath(projectId, tenantId, jobId);
      client
        .getJob({name: formattedName})
        .then(responses => {
          const response = responses[0];
          console.log(`Job name: ${response.name}`);
          console.log(`Requisition ID: ${response.requisitionId}`);
          console.log(`Title: ${response.title}`);
          console.log(`Description: ${response.description}`);
          console.log(`Posting language: ${response.languageCode}`);
          for (const address of response.addresses) {
            console.log(`Address: ${address}`);
          }
          for (const email of response.applicationInfo.emails) {
            console.log(`Email: ${email}`);
          }
          for (const websiteUri of response.applicationInfo.uris) {
            console.log(`Website: ${websiteUri}`);
          }
        })
        .catch(err => {
          console.error(err);
        });
    }
    

### Python

To learn how to install and use the client library for CTS, see [CTS client libraries](https://docs.cloud.google.com/talent-solution/job-search/docs/libraries). For more information, see the [CTS Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/talent/latest). 

To authenticate to CTS, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import talent
    
    
    def get_job(project_id, tenant_id, job_id):
        """Get Job"""
    
        client = talent.[JobServiceClient](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.job_service.JobServiceClient.html)()
    
        # project_id = 'Your Google Cloud Project ID'
        # tenant_id = 'Your Tenant ID (using tenancy is optional)'
        # job_id = 'Job ID'
    
        if isinstance(project_id, bytes):
            project_id = project_id.decode("utf-8")
        if isinstance(tenant_id, bytes):
            tenant_id = tenant_id.decode("utf-8")
        if isinstance(job_id, bytes):
            job_id = job_id.decode("utf-8")
        name = client.[job_path](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.job_service.JobServiceClient.html#google_cloud_talent_v4_services_job_service_JobServiceClient_job_path)(project_id, tenant_id, job_id)
    
        response = client.[get_job](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.job_service.JobServiceClient.html#google_cloud_talent_v4_services_job_service_JobServiceClient_get_job)(name=name)
        print(f"Job name: {response.name}")
        print(f"Requisition ID: {response.requisition_id}")
        print(f"Title: {response.title}")
        print(f"Description: {response.description}")
        print(f"Posting language: {response.language_code}")
        for address in response.addresses:
            print(f"Address: {address}")
        for email in response.application_info.emails:
            print(f"Email: {email}")
        for website_uri in response.application_info.uris:
            print(f"Website: {website_uri}")
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=talentsolution). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
