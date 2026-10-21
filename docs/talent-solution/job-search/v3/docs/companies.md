---
url: https://docs.cloud.google.com/talent-solution/job-search/v3/docs/companies/
title: Create and update companies (v3) \u00a0|\u00a0 Cloud Talent Solution - Job Search v3 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:53:09.623100+00:00
---

# Create and update companies (v3)  |  Cloud Talent Solution - Job Search v3  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/talent-solution/job-search/v3/docs/companies/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Cloud Talent Solution ](https://docs.cloud.google.com/talent-solution/docs)
  * [ Job Search ](https://docs.cloud.google.com/talent-solution/job-search/docs)
  * [ Job Search v3 (deprecated) ](https://docs.cloud.google.com/talent-solution/job-search/v3/docs)



Send feedback 

#  Create and update companies (v3) Stay organized with collections  Save and categorize content based on your preferences. 

A Company resource in the Cloud Talent Solution API represents a single company. Any job belonging to that company refers to a job posting that is created for an open position in that company. It contains information such as the company name and address, as well as internal fields that tie the resource in the Cloud Talent Solution service back to your internal databases.

## Create a company

To create a Company, send a POST request to the `companies` endpoint, specifying at least the two required fields. Refer to the [Quickstart: Create companies and jobs](https://docs.cloud.google.com/talent-solution/job-search/v3/docs/create-company-job) page for details on how to create a company.

### Java

For more on installing and creating a Cloud Talent Solution client, see [Cloud Talent Solution Client Libraries](https://docs.cloud.google.com/talent-solution/job-search/v3/docs/libraries). 
    
    
    /** Create a company. */
    public static Company createCompany(Company companyToBeCreated) throws IOException {
      try {
        CreateCompanyRequest createCompanyRequest =
            new CreateCompanyRequest().setCompany(companyToBeCreated);
        Company companyCreated =
            talentSolutionClient
                .projects()
                .companies()
                .create(DEFAULT_PROJECT_ID, createCompanyRequest)
                .execute();
        System.out.println("Company created: " + companyCreated);
        return companyCreated;
      } catch (IOException e) {
        System.out.println("Got exception while creating company");
        throw e;
      }
    }

### Python

For more on installing and creating a Cloud Talent Solution client, see [Cloud Talent Solution Client Libraries](https://docs.cloud.google.com/talent-solution/job-search/v3/docs/libraries). 
    
    
    def create_company(client_service, company_to_be_created):
        try:
            request = {"company": company_to_be_created}
            company_created = (
                client_service.projects()
                .companies()
                .create(parent=parent, body=request)
                .execute()
            )
            print("Company created: %s" % company_created)
            return company_created
        except Error as e:
            print("Got exception while creating company")
            raise e

### Go

For more on installing and creating a Cloud Talent Solution client, see [Cloud Talent Solution Client Libraries](https://docs.cloud.google.com/talent-solution/job-search/v3/docs/libraries). 
    
    
    // createCompany creates a company as given.
    func createCompany(w io.Writer, projectID string, companyToCreate *talent.Company) (*talent.Company, error) {
    	ctx := context.Background()
    
    	client, err := google.DefaultClient(ctx, talent.CloudPlatformScope)
    	if err != nil {
    		return nil, fmt.Errorf("google.DefaultClient: %w", err)
    	}
    	// Create the jobs service client.
    	service, err := talent.New(client)
    	if err != nil {
    		return nil, fmt.Errorf("talent.New: %w", err)
    	}
    
    	parent := "projects/" + projectID
    	req := &talent.CreateCompanyRequest{
    		Company: companyToCreate,
    	}
    	company, err := service.Projects.Companies.Create(parent, req).Do()
    	if err != nil {
    		return nil, fmt.Errorf("failed to create company %q: %w", companyToCreate.DisplayName, err)
    	}
    
    	return company, nil
    }
    

## Required fields

The following fields are required in create/update requests:

  * [`displayName`](https://docs.cloud.google.com/talent-solution/job-search/v3/docs/reference/rest/v3/projects.companies#Company.FIELDS.display_name): The name of the employer displayed with the job, for example, "Google LLC".

  * [`externalId`](https://docs.cloud.google.com/talent-solution/job-search/v3/docs/reference/rest/v3/projects.companies#Company.FIELDS.external_id): Your internal ID for this company. This field allows you to map your internal identifiers to the company in Google's system. If the company doesn't have a separate internal identifier, set this field to the same value as `displayName`.




## Commonly used fields

  * [`headquartersAddress`](https://docs.cloud.google.com/talent-solution/job-search/v3/docs/reference/rest/v3/projects.companies#Company.FIELDS.headquarters_address): The street address of the company's main headquarters, which may be different from the job location. Cloud Talent Solution only accepts a single HQ location per company. The service attempts to geolocate the address, and populates a more specific location when possible in `derivedInfo.headquartersLocation` (which is output only).

  * `size`: A bucket value representing the size of the company in terms of number of employees, from `MINI` to `GIANT`. See the [`size`](https://docs.cloud.google.com/talent-solution/job-search/v3/docs/reference/rest/v3/projects.companies#CompanySize) reference for enums and their definitions.

  * `eeoText`: A string containing the Equal Employment Opportunity legal disclaimer text to be associated with all jobs for this company.

  * [`keywordSearchableJobCustomAttributes`](https://docs.cloud.google.com/talent-solution/job-search/v3/docs/reference/rest/v3/projects.companies#Company.FIELDS.keyword_searchable_job_custom_attributes): Specifies which `customAttributes` on this company's jobs should be indexed and searchable by general keyword search.




## Update a company

To update a company, send a PATCH request to the following endpoint:
    
    
     PATCH https://jobs.googleapis.com/v3/COMPANY_NAME 

Where `COMPANY_NAME` is the value of the `name` field for the company. `name` is the unique identifier of the company that is returned at creation time and also by `company.get` and `list` requests.

The body of the request must contain the entire resource, including fields not being updated. These fields can be set in the `updateMask`. If fields are set in the `updateMask`, then only those fields are updated, and updates to other fields are ignored. If the `updateMask` is not set, then all fields are updated.

### Java

For more on installing and creating a Cloud Talent Solution client, see [Cloud Talent Solution Client Libraries](https://docs.cloud.google.com/talent-solution/job-search/v3/docs/libraries). 
    
    
    /** Updates a company. */
    public static Company updateCompany(String companyName, Company companyToBeUpdated)
        throws IOException {
      try {
        UpdateCompanyRequest updateCompanyRequest =
            new UpdateCompanyRequest().setCompany(companyToBeUpdated);
    
        Company companyUpdated =
            talentSolutionClient
                .projects()
                .companies()
                .patch(companyName, updateCompanyRequest)
                .execute();
    
        System.out.println("Company updated: " + companyUpdated);
        return companyUpdated;
      } catch (IOException e) {
        System.out.println("Got exception while updating company");
        throw e;
      }
    }

### Python

For more on installing and creating a Cloud Talent Solution client, see [Cloud Talent Solution Client Libraries](https://docs.cloud.google.com/talent-solution/job-search/v3/docs/libraries). 
    
    
    def update_company(client_service, company_name, company_to_be_updated):
        try:
            request = {"company": company_to_be_updated}
            company_updated = (
                client_service.projects()
                .companies()
                .patch(name=company_name, body=request)
                .execute()
            )
            print("Company updated: %s" % company_updated)
            return company_updated
        except Error as e:
            print("Got exception while updating company")
            raise e

### Go

For more on installing and creating a Cloud Talent Solution client, see [Cloud Talent Solution Client Libraries](https://docs.cloud.google.com/talent-solution/job-search/v3/docs/libraries). 
    
    
    // updateCompany update a company with all fields.
    func updateCompany(w io.Writer, name string, companyToUpdate *talent.Company) (*talent.Company, error) {
    	ctx := context.Background()
    
    	client, err := google.DefaultClient(ctx, talent.CloudPlatformScope)
    	if err != nil {
    		return nil, fmt.Errorf("google.DefaultClient: %w", err)
    	}
    	// Create the jobs service client.
    	service, err := talent.New(client)
    	if err != nil {
    		return nil, fmt.Errorf("talent.New: %w", err)
    	}
    
    	updateCompanyRequest := &talent.UpdateCompanyRequest{
    		Company: companyToUpdate,
    	}
    	company, err := service.Projects.Companies.Patch(name, updateCompanyRequest).Do()
    	if err != nil {
    		return nil, fmt.Errorf("failed to update company %q: %w", name, err)
    	}
    
    	return company, nil
    }
    

Update Company with `updateMask`

### Java

For more on installing and creating a Cloud Talent Solution client, see [Cloud Talent Solution Client Libraries](https://docs.cloud.google.com/talent-solution/job-search/v3/docs/libraries). 
    
    
    /** Updates a company. */
    public static Company updateCompanyWithFieldMask(
        String companyName, String fieldMask, Company companyToBeUpdated) throws IOException {
      try {
        // String foo = String.format("?updateCompanyFields=%s",fieldMask);
        UpdateCompanyRequest updateCompanyRequest =
            new UpdateCompanyRequest().setUpdateMask(fieldMask).setCompany(companyToBeUpdated);
    
        Company companyUpdated =
            talentSolutionClient
                .projects()
                .companies()
                .patch(companyName, updateCompanyRequest)
                .execute();
    
        System.out.println("Company updated: " + companyUpdated);
        return companyUpdated;
      } catch (IOException e) {
        System.out.println("Got exception while updating company");
        throw e;
      }
    }

### Python

For more on installing and creating a Cloud Talent Solution client, see [Cloud Talent Solution Client Libraries](https://docs.cloud.google.com/talent-solution/job-search/v3/docs/libraries). 
    
    
    def update_company_with_field_mask(
        client_service, company_name, company_to_be_updated, field_mask
    ):
        try:
            request = {"company": company_to_be_updated, "update_mask": field_mask}
            company_updated = (
                client_service.projects()
                .companies()
                .patch(name=company_name, body=request)
                .execute()
            )
            print("Company updated: %s" % company_updated)
            return company_updated
        except Error as e:
            print("Got exception while updating company with field mask")
            raise e

### Go

For more on installing and creating a Cloud Talent Solution client, see [Cloud Talent Solution Client Libraries](https://docs.cloud.google.com/talent-solution/job-search/v3/docs/libraries). 
    
    
    // updateCompanyWithMask updates a company with specific fields.
    // mask is a comma separated list of top-level fields of talent.Company.
    func updateCompanyWithMask(w io.Writer, name string, mask string, companyToUpdate *talent.Company) (*talent.Company, error) {
    	ctx := context.Background()
    
    	client, err := google.DefaultClient(ctx, talent.CloudPlatformScope)
    	if err != nil {
    		return nil, fmt.Errorf("google.DefaultClient: %w", err)
    	}
    	// Create the jobs service client.
    	service, err := talent.New(client)
    	if err != nil {
    		return nil, fmt.Errorf("talent.New: %w", err)
    	}
    
    	req := &talent.UpdateCompanyRequest{
    		Company:    companyToUpdate,
    		UpdateMask: mask,
    	}
    	company, err := service.Projects.Companies.Patch(name, req).Do()
    	if err != nil {
    		return nil, fmt.Errorf("failed to update company %q with mask %q: %w", name, mask, err)
    	}
    
    	return company, nil
    }
    

## Best practices

### Confidential companies

In cases where you want to post a confidential job, we recommend creating a separate company that mimics the company's fields, but obfuscates the `displayName`, `externalId`, and any other identifying fields.

In cases where the end employer should be anonymous (for example, the Staffing Agency use case), we recommend setting the `externalId` and `displayName` to random but unique values.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
