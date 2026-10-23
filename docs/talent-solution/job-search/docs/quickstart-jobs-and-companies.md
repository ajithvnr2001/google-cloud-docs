---
url: https://docs.cloud.google.com/talent-solution/job-search/docs/quickstart-jobs-and-companies/
title: Quickstart: Create companies and jobs \u00a0|\u00a0 Job Search \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:41:11.905514+00:00
---

# Quickstart: Create companies and jobs  |  Job Search  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/talent-solution/job-search/docs/quickstart-jobs-and-companies/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Cloud Talent Solution ](https://docs.cloud.google.com/talent-solution/docs)
  * [ Job Search ](https://docs.cloud.google.com/talent-solution/job-search/docs)
  * [ Guides ](https://docs.cloud.google.com/talent-solution/job-search/docs/basics)



Send feedback 

#  Quickstart: Create companies and jobs Stay organized with collections  Save and categorize content based on your preferences. 

This tutorial is designed to get you started exploring and developing applications with Cloud Talent Solution. Familiarity with basic programming is assumed, though even without much programming knowledge, you should be able to follow along. After going through this tutorial, you should be able to use the [Reference](https://docs.cloud.google.com/talent-solution/job-search/docs/reference/rest) documentation to create your own basic applications. Video tutorials and interactive codelabs are also [available](https://docs.cloud.google.com/talent-solutuon/job-search/docs/video).Please [contact us](https://docs.cloud.google.com/talent-solution/docs/support) if you have any questions.

## Prerequisites

You have:

  * followed the steps to create and set up your project, as listed in [Before You Begin](https://docs.cloud.google.com/talent-solution/job-search/docs/before-you-begin),
  * set up your environment using [Application Default Credentials](https://developers.google.com/identity/protocols/application-default-credentials),
  * basic familiarity with Java or Python programming,
  * installed the latest [Google API Java client](https://developers.google.com/api-client-library/java/google-api-java-client/setup) or [Google API Python client](https://developers.google.com/api-client-library/python/start/get_started).



## Create a Company with Jobs and search for those Jobs

This tutorial walks you through a basic Cloud Talent Solution application, and guides you through creating a single Job resource that you associate to a Company resource. The next tutorial walks you through the steps to search for Jobs within the Company based on attributes of the Jobs and the search query. The `search` API attempts to return jobs most relevant to a job seeker's query based on available fields within a Job (company name, job title, job description, job categories, job location, and so on).

**Note:** Copy the code to your clipboard by mousing over the copy icon in the code snippet, and clicking. Copy this code into a file within your development directory.

## Create a Company

A [Company](https://docs.cloud.google.com/talent-solution/job-search/docs/reference/rest/v4/projects.tenants.companies) is an entity associated with a set of job listings. You must create the Company object before you can post Jobs on Cloud Talent Solution for that Company. You can send any freeform string as the `externalId` when creating the Company. This means you can use the primary key from your existing database (if you have one) when creating and referring to a Company.

The following sample shows how to create a new client to perform the request. We recommend that you create one client per program or system process, then use either connection pooling or a singleton client to share that client across multiple requests. Creating a new client with each request can cause performance problems or trigger DoS protection.

**Note:** Cloud Talent Solution creation calls return a unique name for each Company/Job. Store these names as they are used to update/delete/reference Companies/Jobs.

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

For more on installing and creating a Cloud Talent Solution client, see [Cloud Talent Solution Client Libraries](https://docs.cloud.google.com/talent-solution/job-search/docs/libraries). 
    
    
    import com.google.cloud.talent.v4.[Company](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.Company.html);
    import com.google.cloud.talent.v4.[CompanyServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.CompanyServiceClient.html);
    import com.google.cloud.talent.v4.[CreateCompanyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.CreateCompanyRequest.html);
    import com.google.cloud.talent.v4.[TenantName](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.TenantName.html);
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
        try ([CompanyServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.CompanyServiceClient.html) companyServiceClient = [CompanyServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.CompanyServiceClient.html).create()) {
          [TenantName](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.TenantName.html) parent = [TenantName](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.TenantName.html).of(projectId, tenantId);
          [Company](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.Company.html) company =
              [Company](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.Company.html).newBuilder().[setDisplayName](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.Company.Builder.html#com_google_cloud_talent_v4_Company_Builder_setDisplayName_java_lang_String_)(displayName).setExternalId(externalId).build();
    
          [CreateCompanyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.CreateCompanyRequest.html) request =
              [CreateCompanyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.CreateCompanyRequest.html).newBuilder()
                  .setParent(parent.[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.TenantName.html#com_google_cloud_talent_v4_TenantName_toString__)())
                  .setCompany(company)
                  .build();
    
          [Company](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.Company.html) response = companyServiceClient.createCompany(request);
          System.out.println("Created Company");
          System.out.format("Name: %s%n", response.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.Company.html#com_google_cloud_talent_v4_Company_getName__)());
          System.out.format("Display Name: %s%n", response.[getDisplayName](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.Company.html#com_google_cloud_talent_v4_Company_getDisplayName__)());
          System.out.format("External ID: %s%n", response.[getExternalId](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.Company.html#com_google_cloud_talent_v4_Company_getExternalId__)());
        }
      }
    }

### Node.js

For more on installing and creating a Cloud Talent Solution client, see [Cloud Talent Solution Client Libraries](https://docs.cloud.google.com/talent-solution/job-search/docs/libraries). 
    
    
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

For more on installing and creating a Cloud Talent Solution client, see [Cloud Talent Solution Client Libraries](https://docs.cloud.google.com/talent-solution/job-search/docs/libraries). 
    
    
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
    
    

## Create a Job

To post a new Job resource, you must provide all of the required fields about the job along with the `companyName` of the Company you want to associate this Job with. You specified the `companyName` earlier when you created the Company resource.

The data object with the Job data filled in is sent to the Cloud Talent Solution endpoint using a POST request. The `name` field should not be set in the initial request since it is an "output only" field of the `createJob` API: it's a part of the API response when a new job entity is created by the server. The API endpoint to interact with a Jobs resource is specified in the [Cloud Talent Solution Client Libraries document](https://docs.cloud.google.com/talent-solution/job-search/docs/libraries).

The response to the request is a new Job object. It should include a Job `name` which uniquely represents the posting. The Job `name` is used when the posting needs to be updated or deleted. As a best practice, store this `name` and map it to your own unique ID for the Job.

The server returns an error if you attempt to create a new Job when another Job already exists in the system with the same `companyName`, `requisitionId` and `languageCode`.

Cloud Talent Solution also allows you to create Jobs that are specific to a location. See [`locations`](https://docs.cloud.google.com/talent-solution/job-search/docs/reference/rest/v4/projects.tenants.jobs#Job.FIELDS.locations) for more information.

The following code creates a Job with just the required fields for the Company specified in the `companyName` field.

You can create a Job using the code sample below. See [Quickstart: Create companies and jobs](https://docs.cloud.google.com/talent-solution/job-search/docs/quickstart-jobs-and-companies#create_a_job_in_your_company) for more details.

### Go

For more on installing and creating a Cloud Talent Solution client, see [Cloud Talent Solution Client Libraries](https://docs.cloud.google.com/talent-solution/job-search/docs/libraries). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	talent "cloud.google.com/go/talent/apiv4beta1"
    	talentpb "google.golang.org/genproto/googleapis/cloud/talent/v4beta1"
    )
    
    // createJob create a job as given.
    func createJob(w io.Writer, projectID, companyID, requisitionID, title, URI, description, address1, address2, languageCode string) (*talentpb.[Job](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/talent/latest/apiv4beta1/talentpb.html#cloud_google_com_go_talent_apiv4beta1_talentpb_Job), error) {
    	ctx := context.Background()
    
    	// Initialize a jobService client.
    	c, err := talent.[NewJobClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/talent/latest/apiv4beta1.html#cloud_google_com_go_talent_apiv4beta1_JobClient_NewJobClient)(ctx)
    	if err != nil {
    		fmt.Printf("talent.NewJobClient: %v\n", err)
    		return nil, err
    	}
    
    	jobToCreate := &talentpb.[Job](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/talent/latest/apiv4beta1/talentpb.html#cloud_google_com_go_talent_apiv4beta1_talentpb_Job){
    		CompanyName:   fmt.Sprintf("projects/%s/companies/%s", projectID, companyID),
    		RequisitionId: requisitionID,
    		Title:         title,
    		ApplicationInfo: &talentpb.[Job_ApplicationInfo](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/talent/latest/apiv4beta1/talentpb.html#cloud_google_com_go_talent_apiv4beta1_talentpb_Job_ApplicationInfo){
    			Uris: []string{URI},
    		},
    		Description:  description,
    		Addresses:    []string{address1, address2},
    		LanguageCode: languageCode,
    	}
    
    	// Construct a createJob request.
    	req := &talentpb.[CreateJobRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/talent/latest/apiv4beta1/talentpb.html#cloud_google_com_go_talent_apiv4beta1_talentpb_CreateJobRequest){
    		Parent: fmt.Sprintf("projects/%s", projectID),
    		Job:    jobToCreate,
    	}
    
    	resp, err := c.CreateJob(ctx, req)
    	if err != nil {
    		fmt.Printf("Failed to create job: %v\n", err)
    		return nil, err
    	}
    
    	fmt.Printf("Created job: %q\n", resp.GetName())
    
    	return resp, nil
    }
    

### Java

For more on installing and creating a Cloud Talent Solution client, see [Cloud Talent Solution Client Libraries](https://docs.cloud.google.com/talent-solution/job-search/docs/libraries). 
    
    
    import com.google.cloud.talent.v4.[CreateJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.CreateJobRequest.html);
    import com.google.cloud.talent.v4.[Job](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.Job.html);
    import com.google.cloud.talent.v4.[JobServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.JobServiceClient.html);
    import com.google.cloud.talent.v4.[TenantName](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.TenantName.html);
    import java.io.IOException;
    import java.util.Arrays;
    import java.util.List;
    
    public class JobSearchCreateJob {
    
      public static void createJob() throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "your-project-id";
        String tenantId = "your-tenant-id";
        String companyId = "your-company-id";
        String requisitionId = "your-unique-req-id";
        String jobApplicationUrl = "your-job-url";
        // String projectId = "me-qa-1";
        // String tenantId = "8ed97629-27ee-4215-909b-18cfe3b7e8e3";
        // String companyId = "05317758-b30e-4b26-a57d-d9e54e4cccd8";
        // String requisitionId = "test-requisitionid-1";
        // String jobApplicationUrl = "http://job.url";
        createJob(projectId, tenantId, companyId, requisitionId, jobApplicationUrl);
      }
    
      // Create a job.
      public static void createJob(
          String projectId,
          String tenantId,
          String companyId,
          String requisitionId,
          String jobApplicationUrl)
          throws IOException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clean up any remaining background resources.
        try ([JobServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.JobServiceClient.html) jobServiceClient = [JobServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.JobServiceClient.html).create()) {
          [TenantName](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.TenantName.html) parent = [TenantName](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.TenantName.html).of(projectId, tenantId);
          [Job](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.Job.html).[ApplicationInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.Job.ApplicationInfo.html) applicationInfo =
              [Job](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.Job.html).ApplicationInfo.newBuilder().[addUris](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.Job.ApplicationInfo.Builder.html#com_google_cloud_talent_v4_Job_ApplicationInfo_Builder_addUris_java_lang_String_)(jobApplicationUrl).build();
    
          List<String> addresses =
              Arrays.asList(
                  "1600 Amphitheatre Parkway, Mountain View, CA 94043",
                  "111 8th Avenue, New York, NY 10011");
    
          // By default, job will expire in 30 days.
          // https://cloud.google.com/talent-solution/job-search/docs/jobs
          [Job](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.Job.html) job =
              [Job](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.Job.html).newBuilder()
                  .setCompany(companyId)
                  .[setRequisitionId](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.Job.Builder.html#com_google_cloud_talent_v4_Job_Builder_setRequisitionId_java_lang_String_)(requisitionId)
                  .[setTitle](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.Job.Builder.html#com_google_cloud_talent_v4_Job_Builder_setTitle_java_lang_String_)("Software Developer")
                  .setDescription("Develop, maintain the software solutions.")
                  .[setApplicationInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.Job.Builder.html#com_google_cloud_talent_v4_Job_Builder_setApplicationInfo_com_google_cloud_talent_v4_Job_ApplicationInfo_)(applicationInfo)
                  .[addAllAddresses](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.Job.Builder.html#com_google_cloud_talent_v4_Job_Builder_addAllAddresses_java_lang_Iterable_java_lang_String__)(addresses)
                  .[setLanguageCode](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.Job.Builder.html#com_google_cloud_talent_v4_Job_Builder_setLanguageCode_java_lang_String_)("en-US")
                  .build();
    
          [CreateJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.CreateJobRequest.html) request =
              [CreateJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.CreateJobRequest.html).newBuilder().setParent(parent.[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.TenantName.html#com_google_cloud_talent_v4_TenantName_toString__)()).setJob(job).build();
    
          [Job](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.Job.html) response = jobServiceClient.createJob(request);
          System.out.format("Created job: %s%n", response.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.Job.html#com_google_cloud_talent_v4_Job_getName__)());
        }
      }
    }

### Node.js

For more on installing and creating a Cloud Talent Solution client, see [Cloud Talent Solution Client Libraries](https://docs.cloud.google.com/talent-solution/job-search/docs/libraries). 
    
    
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

For more on installing and creating a Cloud Talent Solution client, see [Cloud Talent Solution Client Libraries](https://docs.cloud.google.com/talent-solution/job-search/docs/libraries). 
    
    
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
    
    

## Create a Job with custom fields

Cloud Talent Solution includes several job fields that are built in to the API schema. However, you may need additional fields that aren't present in the out-of-the-box options. While we recommended that you use the out-of-the box fields wherever possible, Cloud Talent Solution also provides some `customAttributes` fields for a Job. These can be filterable or non-filterable. Refer to the [`customAttributes`](https://docs.cloud.google.com/talent-solution/job-search/docs/reference/rest/v4/projects.tenants.jobs#Job.FIELDS.custom_attributes) documentation for more information.

The following code example shows how to create a Job with a `customAttribute`:

### Go

For more on installing and creating a Cloud Talent Solution client, see [Cloud Talent Solution Client Libraries](https://docs.cloud.google.com/talent-solution/job-search/docs/libraries). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	talent "cloud.google.com/go/talent/apiv4beta1"
    	"cloud.google.com/go/talent/apiv4beta1/talentpb"
    	"github.com/gofrs/uuid"
    	money "google.golang.org/genproto/googleapis/type/money"
    )
    
    // createJobWithCustomAttributes creates a job with custom attributes.
    func createJobWithCustomAttributes(w io.Writer, projectID, companyID, jobTitle string) (*talentpb.Job, error) {
    	ctx := context.Background()
    
    	// Initialize a job service client.
    	c, err := talent.[NewJobClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/talent/latest/apiv4beta1.html#cloud_google_com_go_talent_apiv4beta1_JobClient_NewJobClient)(ctx)
    	if err != nil {
    		return nil, fmt.Errorf("talent.NewJobClient: %w", err)
    	}
    	defer c.Close()
    
    	// requisitionID shoud be the unique ID in your system
    	requisitionID := fmt.Sprintf("job-with-custom-attribute-%s", uuid.Must(uuid.NewV4()).String())
    	jobToCreate := &talentpb.Job{
    		Company:       fmt.Sprintf("projects/%s/companies/%s", projectID, companyID),
    		RequisitionId: requisitionID,
    		Title:         jobTitle,
    		ApplicationInfo: &talentpb.Job_ApplicationInfo{
    			Uris: []string{"https://googlesample.com/career"},
    		},
    		Description:     "Design, devolop, test, deploy, maintain and improve software.",
    		LanguageCode:    "en-US",
    		PromotionValue:  2,
    		EmploymentTypes: []talentpb.EmploymentType{talentpb.[EmploymentType_FULL_TIME](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/talent/latest/apiv4beta1/talentpb.html#cloud_google_com_go_talent_apiv4beta1_talentpb_EmploymentType_EMPLOYMENT_TYPE_UNSPECIFIED_EmploymentType_FULL_TIME_EmploymentType_PART_TIME_EmploymentType_CONTRACTOR_EmploymentType_CONTRACT_TO_HIRE_EmploymentType_TEMPORARY_EmploymentType_INTERN_EmploymentType_VOLUNTEER_EmploymentType_PER_DIEM_EmploymentType_FLY_IN_FLY_OUT_EmploymentType_OTHER_EMPLOYMENT_TYPE)},
    		Addresses:       []string{"Mountain View, CA"},
    		CustomAttributes: map[string]*talentpb.CustomAttribute{
    			"someFieldString": {
    				Filterable:   true,
    				StringValues: []string{"someStrVal"},
    			},
    			"someFieldLong": {
    				Filterable: true,
    				LongValues: []int64{900},
    			},
    		},
    		CompensationInfo: &talentpb.CompensationInfo{
    			Entries: []*talentpb.CompensationInfo_CompensationEntry{
    				{
    					Type: talentpb.[CompensationInfo_BASE](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/talent/latest/apiv4beta1/talentpb.html#cloud_google_com_go_talent_apiv4beta1_talentpb_CompensationInfo_COMPENSATION_TYPE_UNSPECIFIED_CompensationInfo_BASE_CompensationInfo_BONUS_CompensationInfo_SIGNING_BONUS_CompensationInfo_EQUITY_CompensationInfo_PROFIT_SHARING_CompensationInfo_COMMISSIONS_CompensationInfo_TIPS_CompensationInfo_OTHER_COMPENSATION_TYPE),
    					Unit: talentpb.[CompensationInfo_HOURLY](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/talent/latest/apiv4beta1/talentpb.html#cloud_google_com_go_talent_apiv4beta1_talentpb_CompensationInfo_COMPENSATION_UNIT_UNSPECIFIED_CompensationInfo_HOURLY_CompensationInfo_DAILY_CompensationInfo_WEEKLY_CompensationInfo_MONTHLY_CompensationInfo_YEARLY_CompensationInfo_ONE_TIME_CompensationInfo_OTHER_COMPENSATION_UNIT),
    					CompensationAmount: &talentpb.CompensationInfo_CompensationEntry_Amount{
    						Amount: &money.Money{
    							CurrencyCode: "USD",
    							Units:        1,
    						},
    					},
    				},
    			},
    		},
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
    
    	fmt.Fprintf(w, "Created job with custom attributres: %q\n", resp.GetName())
    	fmt.Fprintf(w, "Custom long field has value: %v\n", resp.GetCustomAttributes()["someFieldLong"].GetLongValues())
    
    	return resp, nil
    }
    

### Java

For more on installing and creating a Cloud Talent Solution client, see [Cloud Talent Solution Client Libraries](https://docs.cloud.google.com/talent-solution/job-search/docs/libraries). 
    
    
    import com.google.cloud.talent.v4.[CreateJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.CreateJobRequest.html);
    import com.google.cloud.talent.v4.[CustomAttribute](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.CustomAttribute.html);
    import com.google.cloud.talent.v4.[Job](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.Job.html);
    import com.google.cloud.talent.v4.[JobServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.JobServiceClient.html);
    import com.google.cloud.talent.v4.[TenantName](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.TenantName.html);
    import java.io.IOException;
    
    public class JobSearchCreateJobCustomAttributes {
    
      public static void createJob() throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "your-project-id";
        String tenantId = "your-tenant-id";
        String companyId = "your-company-id";
        String requisitionId = "your-unique-req-id";
        createJob(projectId, tenantId, companyId, requisitionId);
      }
    
      // Create Job with Custom Attributes.
      public static void createJob(
          String projectId, String tenantId, String companyId, String requisitionId)
          throws IOException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clean up any remaining background resources.
        try ([JobServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.JobServiceClient.html) jobServiceClient = [JobServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.JobServiceClient.html).create()) {
          [TenantName](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.TenantName.html) parent = [TenantName](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.TenantName.html).of(projectId, tenantId);
    
          // Custom attribute can be string or numeric value, and can be filtered in search queries.
          // https://cloud.google.com/talent-solution/job-search/docs/custom-attributes
          [CustomAttribute](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.CustomAttribute.html) customAttribute =
              [CustomAttribute](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.CustomAttribute.html).newBuilder()
                  .[addStringValues](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.CustomAttribute.Builder.html#com_google_cloud_talent_v4_CustomAttribute_Builder_addStringValues_java_lang_String_)("Internship")
                  .[addStringValues](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.CustomAttribute.Builder.html#com_google_cloud_talent_v4_CustomAttribute_Builder_addStringValues_java_lang_String_)("Apprenticeship")
                  .[setFilterable](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.CustomAttribute.Builder.html#com_google_cloud_talent_v4_CustomAttribute_Builder_setFilterable_boolean_)(true)
                  .build();
    
          [Job](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.Job.html) job =
              [Job](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.Job.html).newBuilder()
                  .setCompany(companyId)
                  .[setTitle](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.Job.Builder.html#com_google_cloud_talent_v4_Job_Builder_setTitle_java_lang_String_)("Software Developer I")
                  .setDescription("This is a description of this <i>wonderful</i> job!")
                  .[putCustomAttributes](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.Job.Builder.html#com_google_cloud_talent_v4_Job_Builder_putCustomAttributes_java_lang_String_com_google_cloud_talent_v4_CustomAttribute_)("FOR_STUDENTS", customAttribute)
                  .[setRequisitionId](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.Job.Builder.html#com_google_cloud_talent_v4_Job_Builder_setRequisitionId_java_lang_String_)(requisitionId)
                  .[setLanguageCode](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.Job.Builder.html#com_google_cloud_talent_v4_Job_Builder_setLanguageCode_java_lang_String_)("en-US")
                  .build();
    
          [CreateJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.CreateJobRequest.html) request =
              [CreateJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.CreateJobRequest.html).newBuilder().setParent(parent.[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.TenantName.html#com_google_cloud_talent_v4_TenantName_toString__)()).setJob(job).build();
          [Job](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.Job.html) response = jobServiceClient.createJob(request);
          System.out.printf("Created job: %s\n", response.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.Job.html#com_google_cloud_talent_v4_Job_getName__)());
        }
      }
    }

### Node.js

For more on installing and creating a Cloud Talent Solution client, see [Cloud Talent Solution Client Libraries](https://docs.cloud.google.com/talent-solution/job-search/docs/libraries). 
    
    
    const talent = require('[@google-cloud/talent](https://docs.cloud.google.com/nodejs/docs/reference/talent/latest/overview.html)').v4;
    
    /**
     * Create Job with Custom Attributes
     *
     * @param projectId {string} Your Google Cloud Project ID
     * @param tenantId {string} Identifier of the Tenantd
     */
    function sampleCreateJob(
      projectId,
      tenantId,
      companyName,
      requisitionId,
      languageCode
    ) {
      const client = new talent.[JobServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/talent/latest/overview.html)();
      // const projectId = 'Your Google Cloud Project ID';
      // const tenantId = 'Your Tenant ID (using tenancy is optional)';
      // const companyName = 'Company name, e.g. projects/your-project/companies/company-id';
      // const requisitionId = 'Job requisition ID, aka Posting ID. Unique per job.';
      // const languageCode = 'en-US';
      const formattedParent = client.tenantPath(projectId, tenantId);
      const job = {
        company: companyName,
        requisitionId: requisitionId,
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

For more on installing and creating a Cloud Talent Solution client, see [Cloud Talent Solution Client Libraries](https://docs.cloud.google.com/talent-solution/job-search/docs/libraries). 
    
    
    from google.cloud import talent
    
    
    def create_job(project_id, tenant_id, company_id, requisition_id):
        """Create Job with Custom Attributes"""
    
        client = talent.[JobServiceClient](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.job_service.JobServiceClient.html)()
    
        # project_id = 'Your Google Cloud Project ID'
        # tenant_id = 'Your Tenant ID (using tenancy is optional)'
        # company_id = 'Company name, e.g. projects/your-project/companies/company-id'
        # requisition_id = 'Job requisition ID, aka Posting ID. Unique per job.'
        # language_code = 'en-US'
    
        if isinstance(project_id, bytes):
            project_id = project_id.decode("utf-8")
        if isinstance(tenant_id, bytes):
            tenant_id = tenant_id.decode("utf-8")
        if isinstance(company_id, bytes):
            company_id = company_id.decode("utf-8")
    
        # Custom attribute can be string or numeric value,
        # and can be filtered in search queries.
        # https://cloud.google.com/talent-solution/job-search/docs/custom-attributes
        custom_attribute = talent.[CustomAttribute](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.types.CustomAttribute.html)()
        custom_attribute.filterable = True
        custom_attribute.string_values.append("Intern")
        custom_attribute.string_values.append("Apprenticeship")
    
        parent = f"projects/{project_id}/tenants/{tenant_id}"
    
        job = talent.[Job](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.types.Job.html)(
            company=company_id,
            title="Software Engineer",
            requisition_id=requisition_id,
            description="This is a description of this job",
            language_code="en-us",
            custom_attributes={"FOR_STUDENTS": custom_attribute},
        )
    
        response = client.[create_job](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.job_service.JobServiceClient.html#google_cloud_talent_v4_services_job_service_JobServiceClient_create_job)(parent=parent, job=job)
        print(f"Created job: {response.name}")
        return response.name
    
    

## Retrieve a Job

You can confirm that the Job was created by using the GET operation to GET the details of the Job. Note that it might take a few minutes for the Job to become available, based on the current volume of jobs being created in Cloud Talent Solution.

You can retrieve the details of a previously-inserted Job by sending a GET request to theCloud Talent Solution API. The URI should include the previously-inserted Job `name` returned by the original CREATE request as a URL parameter.

The following example uses a GET operation to retrieve the details of a Job with a given `name`:

### Go

For more on installing and creating a Cloud Talent Solution client, see [Cloud Talent Solution Client Libraries](https://docs.cloud.google.com/talent-solution/job-search/docs/libraries). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	talent "cloud.google.com/go/talent/apiv4beta1"
    	talentpb "google.golang.org/genproto/googleapis/cloud/talent/v4beta1"
    )
    
    // getJob gets an existing job by its resource name.
    func getJob(w io.Writer, projectID, jobID string) (*talentpb.[Job](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/talent/latest/apiv4beta1/talentpb.html#cloud_google_com_go_talent_apiv4beta1_talentpb_Job), error) {
    	ctx := context.Background()
    
    	// Initialize a jobService client.
    	c, err := talent.[NewJobClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/talent/latest/apiv4beta1.html#cloud_google_com_go_talent_apiv4beta1_JobClient_NewJobClient)(ctx)
    	if err != nil {
    		fmt.Printf("talent.NewJobClient: %v\n", err)
    		return nil, err
    	}
    
    	// Construct a getJob request.
    	jobName := fmt.Sprintf("projects/%s/jobs/%s", projectID, jobID)
    	req := &talentpb.[GetJobRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/talent/latest/apiv4beta1/talentpb.html#cloud_google_com_go_talent_apiv4beta1_talentpb_GetJobRequest){
    		// The resource name of the job to retrieve.
    		// The format is "projects/{project_id}/jobs/{job_id}".
    		Name: jobName,
    	}
    
    	resp, err := c.GetJob(ctx, req)
    	if err != nil {
    		fmt.Printf("Failed to get job %s: %v\n", jobName, err)
    		return nil, err
    	}
    
    	fmt.Fprintf(w, "Job: %q\n", resp.GetName())
    	fmt.Fprintf(w, "Job title: %v\n", resp.[GetTitle](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/talent/latest/apiv4beta1/talentpb.html#cloud_google_com_go_talent_apiv4beta1_talentpb_Job_GetTitle)())
    
    	return resp, err
    }
    

### Java

For more on installing and creating a Cloud Talent Solution client, see [Cloud Talent Solution Client Libraries](https://docs.cloud.google.com/talent-solution/job-search/docs/libraries). 
    
    
    import com.google.cloud.talent.v4.[GetJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.GetJobRequest.html);
    import com.google.cloud.talent.v4.[Job](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.Job.html);
    import com.google.cloud.talent.v4.[JobName](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.JobName.html);
    import com.google.cloud.talent.v4.[JobServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.JobServiceClient.html);
    import java.io.IOException;
    
    public class JobSearchGetJob {
    
      public static void getJob() throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "your-project-id";
        String tenantId = "your-tenant-id";
        String jobId = "your-job-id";
        getJob(projectId, tenantId, jobId);
      }
    
      // Get Job.
      public static void getJob(String projectId, String tenantId, String jobId) throws IOException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clean up any remaining background resources.
        try ([JobServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.JobServiceClient.html) jobServiceClient = [JobServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.JobServiceClient.html).create()) {
          [JobName](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.JobName.html) name = [JobName](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.JobName.html).of(projectId, tenantId, jobId);
    
          [GetJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.GetJobRequest.html) request = [GetJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.GetJobRequest.html).newBuilder().setName(name.[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.JobName.html#com_google_cloud_talent_v4_JobName_toString__)()).build();
    
          [Job](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.Job.html) response = jobServiceClient.getJob(request);
          System.out.format("Job name: %s%n", response.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.Job.html#com_google_cloud_talent_v4_Job_getName__)());
          System.out.format("Requisition ID: %s%n", response.[getRequisitionId](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.Job.html#com_google_cloud_talent_v4_Job_getRequisitionId__)());
          System.out.format("Title: %s%n", response.[getTitle](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.Job.html#com_google_cloud_talent_v4_Job_getTitle__)());
          System.out.format("Description: %s%n", response.[getDescription](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.Job.html#com_google_cloud_talent_v4_Job_getDescription__)());
          System.out.format("Posting language: %s%n", response.[getLanguageCode](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.Job.html#com_google_cloud_talent_v4_Job_getLanguageCode__)());
          for (String address : response.[getAddressesList](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.Job.html#com_google_cloud_talent_v4_Job_getAddressesList__)()) {
            System.out.format("Address: %s%n", address);
          }
          for (String email : response.[getApplicationInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.Job.html#com_google_cloud_talent_v4_Job_getApplicationInfo__)().getEmailsList()) {
            System.out.format("Email: %s%n", email);
          }
          for (String websiteUri : response.[getApplicationInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.Job.html#com_google_cloud_talent_v4_Job_getApplicationInfo__)().getUrisList()) {
            System.out.format("Website: %s%n", websiteUri);
          }
        }
      }
    }

### Node.js

For more on installing and creating a Cloud Talent Solution client, see [Cloud Talent Solution Client Libraries](https://docs.cloud.google.com/talent-solution/job-search/docs/libraries). 
    
    
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

For more on installing and creating a Cloud Talent Solution client, see [Cloud Talent Solution Client Libraries](https://docs.cloud.google.com/talent-solution/job-search/docs/libraries). 
    
    
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
    
    

## Search for Jobs

You've created your first Company and Job using the Cloud Talent Solution! You're now ready to conduct a [search](https://docs.cloud.google.com/talent-solution/job-search/docs/quickstart-searching) across these Jobs.

## More APIs

For more information regarding the APIs and different configurations available, please see the latest [reference documentation](https://docs.cloud.google.com/talent-solution/job-search/docs/apis).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
