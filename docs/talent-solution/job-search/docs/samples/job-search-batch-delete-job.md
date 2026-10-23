---
url: https://docs.cloud.google.com/talent-solution/job-search/docs/samples/job-search-batch-delete-job/
title: Batch delete jobs (v4beta1) \u00a0|\u00a0 Job Search \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:34:25.452872+00:00
---

# Batch delete jobs (v4beta1)  |  Job Search  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/talent-solution/job-search/docs/samples/job-search-batch-delete-job/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Cloud Talent Solution ](https://docs.cloud.google.com/talent-solution/docs)
  * [ Job Search ](https://docs.cloud.google.com/talent-solution/job-search/docs)
  * [ Samples ](https://docs.cloud.google.com/talent-solution/job-search/docs/samples)



#  Batch delete jobs (v4beta1) Stay organized with collections  Save and categorize content based on your preferences. 

Batch delete jobs.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Batch operations](https://docs.cloud.google.com/talent-solution/job-search/docs/batch)



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
    
    // batchDeleteJobs deletes existing jobs by a filter.
    func batchDeleteJobs(w io.Writer, projectID, companyID, requisitionID string) error {
    	ctx := context.Background()
    
    	// Initialize a jobService client.
    	c, err := talent.[NewJobClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/talent/latest/apiv4beta1.html#cloud_google_com_go_talent_apiv4beta1_JobClient_NewJobClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("talent.NewJobClient: %w", err)
    	}
    	defer c.Close()
    
    	companyName := fmt.Sprintf("projects/%s/companies/%s", projectID, companyID)
    	filter := fmt.Sprintf("companyName=%q AND requisitionId=%q", companyName, requisitionID)
    
    	// Construct a batchDeteleJobs request.
    	req := &talentpb.BatchDeleteJobsRequest{
    		Parent: fmt.Sprintf("projects/%s", projectID),
    		// The fields eligible for filtering are `companyName` and `requisitionId`.
    		Filter: filter,
    	}
    
    	if err := c.BatchDeleteJobs(ctx, req); err != nil {
    		return fmt.Errorf("BatchDeleteJobs(%s): %w", filter, err)
    	}
    
    	fmt.Fprintf(w, "Batch deleted jobs from %s\n", filter)
    
    	return err
    }
    

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
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=talentsolution). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
