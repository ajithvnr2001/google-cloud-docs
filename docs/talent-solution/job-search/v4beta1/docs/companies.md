---
url: https://docs.cloud.google.com/talent-solution/job-search/v4beta1/docs/companies/
title: Create and update companies (v4beta1) \u00a0|\u00a0 Cloud Talent Solution - Job Search v4beta1 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:53:59.286578+00:00
---

# Create and update companies (v4beta1)  |  Cloud Talent Solution - Job Search v4beta1  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/talent-solution/job-search/v4beta1/docs/companies/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Cloud Talent Solution ](https://docs.cloud.google.com/talent-solution/docs)
  * [ Job Search ](https://docs.cloud.google.com/talent-solution/job-search/docs)
  * [ Job Search v4beta1 (deprecated) ](https://docs.cloud.google.com/talent-solution/job-search/v4beta1/docs)



Send feedback 

#  Create and update companies (v4beta1) Stay organized with collections  Save and categorize content based on your preferences. 

A Company resource in Cloud Talent Solution represents a single company. Any job belonging to that company refers to a job posting that is created for an open position in that company. It contains information such as the company name and address, as well as internal fields that tie the resource in the Cloud Talent Solution service back to your internal databases.

## Create a company

To create a company, send a POST request to the `companies` endpoint, specifying at least the two required fields. Refer to the [Quickstart: Create companies and jobs](https://docs.cloud.google.com/talent-solution/job-search/v4beta1/docs/quickstart-jobs-and-companies) page for details on how to create a company. Video tutorials and interactive codelabs are also [available](https://docs.cloud.google.com/talent-solutuon/job-search/v4beta1/docs/video).

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
    

### Java

For more on installing and creating a Cloud Talent Solution client, see [Cloud Talent Solution Client Libraries](https://docs.cloud.google.com/talent-solution/job-search/v4beta1/docs/libraries). 
    
    
    import com.google.cloud.talent.v4beta1.Company;
    import com.google.cloud.talent.v4beta1.CompanyServiceClient;
    import com.google.cloud.talent.v4beta1.CreateCompanyRequest;
    import com.google.cloud.talent.v4beta1.TenantName;
    import java.io.IOException;
    
    public class JobSearchCreateCompany {
    
      public static void createCompany() throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "your-project-id";
        String tenantId = "your-tenant-id";
        String displayName = "your-company-display-name";
        String externalId = "your-external-id";
        createCompany(projectId, tenantId, displayName, externalId);
      }
    
      // Create a company.
      public static void createCompany(
          String projectId, String tenantId, String displayName, String externalId) throws IOException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clean up any remaining background resources.
        try (CompanyServiceClient companyServiceClient = CompanyServiceClient.create()) {
          TenantName parent = TenantName.of(projectId, tenantId);
          Company company =
              Company.newBuilder().setDisplayName(displayName).setExternalId(externalId).build();
    
          CreateCompanyRequest request =
              CreateCompanyRequest.newBuilder()
                  .setParent(parent.toString())
                  .setCompany(company)
                  .build();
    
          Company response = companyServiceClient.createCompany(request);
          System.out.println("Created Company");
          System.out.format("Name: %s%n", response.getName());
          System.out.format("Display Name: %s%n", response.getDisplayName());
          System.out.format("External ID: %s%n", response.getExternalId());
        }
      }
    }

### Python

For more on installing and creating a Cloud Talent Solution client, see [Cloud Talent Solution Client Libraries](https://docs.cloud.google.com/talent-solution/job-search/v4beta1/docs/libraries). 
    
    
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
    
    

### Required fields

The following fields are required in create/update requests:

  * [`displayName`](https://docs.cloud.google.com/talent-solution/job-search/v4beta1/docs/reference/rest/v4beta1/projects.companies#Company.FIELDS.display_name): The name of the employer displayed with the job, for example, "Google LLC".

  * [`externalId`](https://docs.cloud.google.com/talent-solution/job-search/v4beta1/docs/reference/rest/v4beta1/projects.companies#Company.FIELDS.external_id): Your internal ID for this company. This field allows you to map your internal identifiers to the company in Google's system. If the company doesn't have a separate internal identifier, set this field to the same value as `displayName`.




### Commonly used fields

  * [`headquartersAddress`](https://docs.cloud.google.com/talent-solution/job-search/v4beta1/docs/reference/rest/v4beta1/projects.companies#Company.FIELDS.headquarters_address): The street address of the company's main headquarters, which may be different from the job location. Cloud Talent Solution only accepts a single HQ location per company. The service attempts to geolocate the address, and populates a more specific location when possible in `derivedInfo.headquartersLocation` (which is output only).

  * `size`: A bucket value representing the size of the company in terms of number of employees, from `MINI` to `GIANT`. See the [`size`](https://docs.cloud.google.com/talent-solution/job-search/v4beta1/docs/reference/rest/v4beta1/projects.companies#CompanySize) reference for enums and their definitions.

  * `eeoText`: A string containing the Equal Employment Opportunity legal disclaimer text to be associated with all jobs for this company.

  * [`keywordSearchableJobCustomAttributes`](https://docs.cloud.google.com/talent-solution/job-search/v4beta1/docs/reference/rest/v4beta1/projects.companies#Company.FIELDS.keyword_searchable_job_custom_attributes): Specifies which `customAttributes` on this company's jobs should be indexed and searchable by general keyword search.




### Confidential companies

In cases where you want to post a confidential job, we recommend creating a separate company that mimics the company's fields, but obfuscates the `displayName`, `externalId`, and any other identifying fields.

In cases where the end employer should be anonymous (for example, the Staffing Agency use case), we recommend setting the `externalId` and `displayName` to random but unique values.

## Retrieve a company

### Go

For more on installing and creating a Cloud Talent Solution client, see [Cloud Talent Solution Client Libraries](https://docs.cloud.google.com/talent-solution/job-search/v4beta1/docs/libraries). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	talent "cloud.google.com/go/talent/apiv4beta1"
    	"cloud.google.com/go/talent/apiv4beta1/talentpb"
    )
    
    // getCompany gets an existing company by its resource name.
    func getCompany(w io.Writer, projectID, companyID string) (*talentpb.Company, error) {
    	ctx := context.Background()
    
    	// Initialize a companyService client.
    	c, err := talent.[NewCompanyClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/talent/latest/apiv4beta1.html#cloud_google_com_go_talent_apiv4beta1_CompanyClient_NewCompanyClient)(ctx)
    	if err != nil {
    		return nil, fmt.Errorf("talent.NewCompanyClient: %w", err)
    	}
    	defer c.Close()
    
    	// Construct a getCompany request.
    	companyName := fmt.Sprintf("projects/%s/companies/%s", projectID, companyID)
    	req := &talentpb.GetCompanyRequest{
    		// The resource name of the company to be retrieved.
    		// The format is "projects/{project_id}/companies/{company_id}".
    		Name: companyName,
    	}
    
    	resp, err := c.GetCompany(ctx, req)
    	if err != nil {
    		return nil, fmt.Errorf("GetCompany: %w", err)
    	}
    
    	fmt.Fprintf(w, "Company: %q\n", resp.GetName())
    	fmt.Fprintf(w, "Company display name: %q\n", resp.GetDisplayName())
    
    	return resp, nil
    }
    

### Java

For more on installing and creating a Cloud Talent Solution client, see [Cloud Talent Solution Client Libraries](https://docs.cloud.google.com/talent-solution/job-search/v4beta1/docs/libraries). 
    
    
    import com.google.cloud.talent.v4beta1.Company;
    import com.google.cloud.talent.v4beta1.CompanyName;
    import com.google.cloud.talent.v4beta1.CompanyServiceClient;
    import com.google.cloud.talent.v4beta1.GetCompanyRequest;
    import java.io.IOException;
    
    public class JobSearchGetCompany {
    
      public static void getCompany() throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "your-project-id";
        String tenantId = "your-tenant-id";
        String companyId = "your-company-id";
        getCompany(projectId, tenantId, companyId);
      }
    
      // Get Company.
      public static void getCompany(String projectId, String tenantId, String companyId)
          throws IOException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clean up any remaining background resources.
        try (CompanyServiceClient companyServiceClient = CompanyServiceClient.create()) {
          CompanyName name = CompanyName.ofProjectTenantCompanyName(projectId, tenantId, companyId);
    
          GetCompanyRequest request = GetCompanyRequest.newBuilder().setName(name.toString()).build();
    
          Company response = companyServiceClient.getCompany(request);
          System.out.format("Company name: %s%n", response.getName());
          System.out.format("Display name: %s%n", response.getDisplayName());
        }
      }
    }

### Python

For more on installing and creating a Cloud Talent Solution client, see [Cloud Talent Solution Client Libraries](https://docs.cloud.google.com/talent-solution/job-search/v4beta1/docs/libraries). 
    
    
    from google.cloud import talent
    
    
    def get_company(project_id, tenant_id, company_id):
        """Get Company"""
    
        client = talent.[CompanyServiceClient](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.company_service.CompanyServiceClient.html)()
    
        # project_id = 'Your Google Cloud Project ID'
        # tenant_id = 'Your Tenant ID (using tenancy is optional)'
        # company_id = 'Company ID'
    
        if isinstance(project_id, bytes):
            project_id = project_id.decode("utf-8")
        if isinstance(tenant_id, bytes):
            tenant_id = tenant_id.decode("utf-8")
        if isinstance(company_id, bytes):
            company_id = company_id.decode("utf-8")
        name = client.[company_path](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.company_service.CompanyServiceClient.html#google_cloud_talent_v4_services_company_service_CompanyServiceClient_company_path)(project_id, tenant_id, company_id)
    
        response = client.[get_company](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.company_service.CompanyServiceClient.html#google_cloud_talent_v4_services_company_service_CompanyServiceClient_get_company)(name=name)
        print(f"Company name: {response.name}")
        print(f"Display name: {response.display_name}")
    
    

## List companies

### Java

For more on installing and creating a Cloud Talent Solution client, see [Cloud Talent Solution Client Libraries](https://docs.cloud.google.com/talent-solution/job-search/v4beta1/docs/libraries). 
    
    
    import com.google.cloud.talent.v4beta1.Company;
    import com.google.cloud.talent.v4beta1.CompanyServiceClient;
    import com.google.cloud.talent.v4beta1.ListCompaniesRequest;
    import com.google.cloud.talent.v4beta1.TenantName;
    import java.io.IOException;
    
    public class JobSearchListCompanies {
    
      public static void listCompanies() throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "your-project-id";
        String tenantId = "your-tenant-id";
        listCompanies(projectId, tenantId);
      }
    
      // List Companies.
      public static void listCompanies(String projectId, String tenantId) throws IOException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clean up any remaining background resources.
        try (CompanyServiceClient companyServiceClient = CompanyServiceClient.create()) {
          TenantName parent = TenantName.of(projectId, tenantId);
    
          ListCompaniesRequest request =
              ListCompaniesRequest.newBuilder().setParent(parent.toString()).build();
    
          for (Company responseItem : companyServiceClient.listCompanies(request).iterateAll()) {
            System.out.format("Company Name: %s%n", responseItem.getName());
            System.out.format("Display Name: %s%n", responseItem.getDisplayName());
            System.out.format("External ID: %s%n", responseItem.getExternalId());
          }
        }
      }
    }

## Delete a company

### Go

For more on installing and creating a Cloud Talent Solution client, see [Cloud Talent Solution Client Libraries](https://docs.cloud.google.com/talent-solution/job-search/v4beta1/docs/libraries). 
    
    
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
    

### Java

For more on installing and creating a Cloud Talent Solution client, see [Cloud Talent Solution Client Libraries](https://docs.cloud.google.com/talent-solution/job-search/v4beta1/docs/libraries). 
    
    
    import com.google.cloud.talent.v4beta1.CompanyName;
    import com.google.cloud.talent.v4beta1.CompanyServiceClient;
    import com.google.cloud.talent.v4beta1.DeleteCompanyRequest;
    import java.io.IOException;
    
    public class JobSearchDeleteCompany {
    
      public static void deleteCompany() throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "your-project-id";
        String tenantId = "your-tenant-id";
        String companyId = "your-company-id";
        deleteCompany(projectId, tenantId, companyId);
      }
    
      // Delete Company.
      public static void deleteCompany(String projectId, String tenantId, String companyId)
          throws IOException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clean up any remaining background resources.
        try (CompanyServiceClient companyServiceClient = CompanyServiceClient.create()) {
          CompanyName name = CompanyName.ofProjectTenantCompanyName(projectId, tenantId, companyId);
    
          DeleteCompanyRequest request =
              DeleteCompanyRequest.newBuilder().setName(name.toString()).build();
    
          companyServiceClient.deleteCompany(request);
          System.out.println("Deleted company");
        }
      }
    }

### Python

For more on installing and creating a Cloud Talent Solution client, see [Cloud Talent Solution Client Libraries](https://docs.cloud.google.com/talent-solution/job-search/v4beta1/docs/libraries). 
    
    
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
    
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
