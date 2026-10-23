---
url: https://docs.cloud.google.com/talent-solution/job-search/docs/samples/job-search-create-company/
title: Create company with client (v4beta1) \u00a0|\u00a0 Job Search \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:41:45.985934+00:00
---

# Create company with client (v4beta1)  |  Job Search  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/talent-solution/job-search/docs/samples/job-search-create-company/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Cloud Talent Solution ](https://docs.cloud.google.com/talent-solution/docs)
  * [ Job Search ](https://docs.cloud.google.com/talent-solution/job-search/docs)
  * [ Samples ](https://docs.cloud.google.com/talent-solution/job-search/docs/samples)



#  Create company with client (v4beta1) Stay organized with collections  Save and categorize content based on your preferences. 

Create company with client.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Create and update companies](https://docs.cloud.google.com/talent-solution/job-search/docs/companies)
  * [Create and update companies (v4beta1)](https://docs.cloud.google.com/talent-solution/job-search/v4beta1/docs/companies)
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
    
    // createCompany creates a company as given.
    func createCompany(w io.Writer, projectID, externalID, displayName string) (*talentpb.Company, error) {
    	ctx := context.Background()
    
    	// Initializes a companyService client.
    	c, err := talent.[NewCompanyClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/talent/latest/apiv4beta1.html#cloud_google_com_go_talent_apiv4beta1_CompanyClient_NewCompanyClient)(ctx)
    	if err != nil {
    		return nil, fmt.Errorf("talent.NewCompanyClient: %w", err)
    	}
    	defer c.Close()
    
    	// Construct a createCompany request.
    	req := &talentpb.CreateCompanyRequest{
    		Parent: fmt.Sprintf("projects/%s", projectID),
    		Company: &talentpb.Company{
    			ExternalId:  externalID,
    			DisplayName: displayName,
    		},
    	}
    
    	resp, err := c.CreateCompany(ctx, req)
    	if err != nil {
    		return nil, fmt.Errorf("CreateCompany: %w", err)
    	}
    
    	fmt.Fprintf(w, "Created company: %q\n", resp.GetName())
    
    	return resp, nil
    }
    

### Node.js

To learn how to install and use the client library for CTS, see [CTS client libraries](https://docs.cloud.google.com/talent-solution/job-search/docs/libraries). For more information, see the [CTS Node.js API reference documentation](https://docs.cloud.google.com/nodejs/docs/reference/talent/latest). 

To authenticate to CTS, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    const talent = require('[@google-cloud/talent](https://docs.cloud.google.com/nodejs/docs/reference/talent/latest/overview.html)').v4;
    
    /**
     * Create Company
     *
     * @param projectId {string} Your Google Cloud Project ID
     * @param tenantId {string} Identifier of the Tenant
     */
    function sampleCreateCompany(projectId, tenantId, displayName, externalId) {
      const client = new talent.[CompanyServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/talent/latest/overview.html)();
      // const projectId = 'Your Google Cloud Project ID';
      // const tenantId = 'Your Tenant ID (using tenancy is optional)';
      // const displayName = 'My Company Name';
      // const externalId = 'Identifier of this company in my system';
      const formattedParent = client.tenantPath(projectId, tenantId);
      const company = {
        displayName: displayName,
        externalId: externalId,
      };
      const request = {
        parent: formattedParent,
        company: company,
      };
      client
        .createCompany(request)
        .then(responses => {
          const response = responses[0];
          console.log('Created Company');
          console.log(`Name: ${response.name}`);
          console.log(`Display Name: ${response.displayName}`);
          console.log(`External ID: ${response.externalId}`);
        })
        .catch(err => {
          console.error(err);
        });
    }
    

### Python

To learn how to install and use the client library for CTS, see [CTS client libraries](https://docs.cloud.google.com/talent-solution/job-search/docs/libraries). For more information, see the [CTS Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/talent/latest). 

To authenticate to CTS, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import talent
    
    
    def create_company(project_id, tenant_id, display_name, external_id):
        """Create Company"""
    
        client = talent.[CompanyServiceClient](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.company_service.CompanyServiceClient.html)()
    
        # project_id = 'Your Google Cloud Project ID'
        # tenant_id = 'Your Tenant ID (using tenancy is optional)'
        # display_name = 'My Company Name'
        # external_id = 'Identifier of this company in my system'
    
        if isinstance(project_id, bytes):
            project_id = project_id.decode("utf-8")
        if isinstance(tenant_id, bytes):
            tenant_id = tenant_id.decode("utf-8")
        if isinstance(display_name, bytes):
            display_name = display_name.decode("utf-8")
        if isinstance(external_id, bytes):
            external_id = external_id.decode("utf-8")
        parent = f"projects/{project_id}/tenants/{tenant_id}"
        company = {"display_name": display_name, "external_id": external_id}
    
        response = client.[create_company](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.company_service.CompanyServiceClient.html#google_cloud_talent_v4_services_company_service_CompanyServiceClient_create_company)(parent=parent, company=company)
        print("Created Company")
        print(f"Name: {response.name}")
        print(f"Display Name: {response.display_name}")
        print(f"External ID: {response.external_id}")
        return response.name
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=talentsolution). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
