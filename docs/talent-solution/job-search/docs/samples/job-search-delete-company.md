---
url: https://docs.cloud.google.com/talent-solution/job-search/docs/samples/job-search-delete-company/
title: Delete company using client (v4beta1) \u00a0|\u00a0 Job Search \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:41:45.312695+00:00
---

# Delete company using client (v4beta1)  |  Job Search  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/talent-solution/job-search/docs/samples/job-search-delete-company/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Cloud Talent Solution ](https://docs.cloud.google.com/talent-solution/docs)
  * [ Job Search ](https://docs.cloud.google.com/talent-solution/job-search/docs)
  * [ Samples ](https://docs.cloud.google.com/talent-solution/job-search/docs/samples)



#  Delete company using client (v4beta1) Stay organized with collections  Save and categorize content based on your preferences. 

Delete company using client.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Create and update companies](https://docs.cloud.google.com/talent-solution/job-search/docs/companies)
  * [Create and update companies (v4beta1)](https://docs.cloud.google.com/talent-solution/job-search/v4beta1/docs/companies)



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
    
    // deleteCompany deletes an existing company. Companies with
    // existing jobs cannot be deleted until those jobs have been deleted.
    func deleteCompany(w io.Writer, projectID, companyID string) error {
    	ctx := context.Background()
    
    	// Initialize a companyService client.
    	c, err := talent.[NewCompanyClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/talent/latest/apiv4beta1.html#cloud_google_com_go_talent_apiv4beta1_CompanyClient_NewCompanyClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("talent.NewCompanyClient: %w", err)
    	}
    	defer c.Close()
    
    	// Construct a deleteCompany request.
    	companyName := fmt.Sprintf("projects/%s/companies/%s", projectID, companyID)
    	req := &talentpb.DeleteCompanyRequest{
    		// The resource name of the company to be deleted.
    		// The format is "projects/{project_id}/companies/{company_id}".
    		Name: companyName,
    	}
    
    	if err := c.DeleteCompany(ctx, req); err != nil {
    		return fmt.Errorf("DeleteCompany(%s): %w", companyName, err)
    	}
    
    	fmt.Fprintf(w, "Deleted company: %q\n", companyName)
    
    	return nil
    }
    

### Node.js

To learn how to install and use the client library for CTS, see [CTS client libraries](https://docs.cloud.google.com/talent-solution/job-search/docs/libraries). For more information, see the [CTS Node.js API reference documentation](https://docs.cloud.google.com/nodejs/docs/reference/talent/latest). 

To authenticate to CTS, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    const talent = require('[@google-cloud/talent](https://docs.cloud.google.com/nodejs/docs/reference/talent/latest/overview.html)').v4;
    
    /** Delete Company */
    function sampleDeleteCompany(projectId, tenantId, companyId) {
      const client = new talent.[CompanyServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/talent/latest/overview.html)();
      // const projectId = 'Your Google Cloud Project ID';
      // const tenantId = 'Your Tenant ID (using tenancy is optional)';
      // const companyId = 'ID of the company to delete';
      const formattedName = client.companyPath(projectId, tenantId, companyId);
      client.deleteCompany({name: formattedName}).catch(err => {
        console.error(err);
      });
      console.log('Deleted company');
    }
    

### Python

To learn how to install and use the client library for CTS, see [CTS client libraries](https://docs.cloud.google.com/talent-solution/job-search/docs/libraries). For more information, see the [CTS Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/talent/latest). 

To authenticate to CTS, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import talent
    
    
    def delete_company(project_id, tenant_id, company_id):
        """Delete Company"""
    
        client = talent.[CompanyServiceClient](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.company_service.CompanyServiceClient.html)()
    
        # project_id = 'Your Google Cloud Project ID'
        # tenant_id = 'Your Tenant ID (using tenancy is optional)'
        # company_id = 'ID of the company to delete'
    
        if isinstance(project_id, bytes):
            project_id = project_id.decode("utf-8")
        if isinstance(tenant_id, bytes):
            tenant_id = tenant_id.decode("utf-8")
        if isinstance(company_id, bytes):
            company_id = company_id.decode("utf-8")
        name = client.[company_path](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.company_service.CompanyServiceClient.html#google_cloud_talent_v4_services_company_service_CompanyServiceClient_company_path)(project_id, tenant_id, company_id)
    
        client.[delete_company](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.company_service.CompanyServiceClient.html#google_cloud_talent_v4_services_company_service_CompanyServiceClient_delete_company)(name=name)
        print("Deleted company")
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=talentsolution). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
