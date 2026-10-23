---
url: https://docs.cloud.google.com/talent-solution/job-search/v4beta1/docs/quickstart-jobs-and-companies/
title: Quickstart: Create companies and jobs (v4beta1) \u00a0|\u00a0 Cloud Talent Solution - Job Search v4beta1 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:40:15.599094+00:00
---

# Quickstart: Create companies and jobs (v4beta1)  |  Cloud Talent Solution - Job Search v4beta1  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/talent-solution/job-search/v4beta1/docs/quickstart-jobs-and-companies/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Cloud Talent Solution ](https://docs.cloud.google.com/talent-solution/docs)
  * [ Job Search ](https://docs.cloud.google.com/talent-solution/job-search/docs)
  * [ Job Search v4beta1 (deprecated) ](https://docs.cloud.google.com/talent-solution/job-search/v4beta1/docs)



Send feedback 

#  Quickstart: Create companies and jobs (v4beta1) Stay organized with collections  Save and categorize content based on your preferences. 

This tutorial is designed to get you started exploring and developing applications with Cloud Talent Solution. Familiarity with basic programming is assumed, though even without much programming knowledge, you should be able to follow along. After going through this tutorial, you should be able to use the [Reference](https://docs.cloud.google.com/talent-solution/job-search/v4beta1/docs/reference/rest) documentation to create your own basic applications. Video tutorials and interactive codelabs are also [available](https://docs.cloud.google.com/talent-solutuon/job-search/v4beta1/docs/video).Please [contact us](https://docs.cloud.google.com/talent-solution/docs/support) if you have any questions.

## Prerequisites

You have:

  * followed the steps to create and set up your project, as listed in [Before You Begin](https://docs.cloud.google.com/talent-solution/job-search/v4beta1/docs/before-you-begin),
  * set up your environment using [Application Default Credentials](https://developers.google.com/identity/protocols/application-default-credentials),
  * basic familiarity with Java or Python programming,
  * installed the latest [Google API Java client](https://developers.google.com/api-client-library/java/google-api-java-client/setup) or [Google API Python client](https://developers.google.com/api-client-library/python/start/get_started).



## Create a Company with Jobs and search for those Jobs

This tutorial walks you through a basic Cloud Talent Solution application, and guides you through creating a single Job resource that you associate to a Company resource. The next tutorial walks you through the steps to search for Jobs within the Company based on attributes of the Jobs and the search query. The `search` API attempts to return jobs most relevant to a job seeker's query based on available fields within a Job (company name, job title, job description, job categories, job location, and so on).

**Note:** Copy the code to your clipboard by mousing over the copy icon in the code snippet, and clicking. Copy this code into a file within your development directory.

## Create a Company

A [Company](https://docs.cloud.google.com/talent-solution/job-search/v4beta1/docs/reference/rest/v4beta1/projects.companies) is an entity associated with a set of job listings. You must create the Company object before you can post Jobs on Cloud Talent Solution for that Company. You can send any freeform string as the `externalId` when creating the Company. This means you can use the primary key from your existing database (if you have one) when creating and referring to a Company.

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
    
    

## Create a Job

To post a new Job resource, you must provide all of the required fields about the job along with the `companyName` of the Company you want to associate this Job with. You specified the `companyName` earlier when you created the Company resource.

The data object with the Job data filled in is sent to the Cloud Talent Solution endpoint using a POST request. The `name` field should not be set in the initial request since it is an "output only" field of the `createJob` API: it's a part of the API response when a new job entity is created by the server. The API endpoint to interact with a Jobs resource is specified in the [Cloud Talent Solution Client Libraries document](https://docs.cloud.google.com/talent-solution/job-search/v4beta1/docs/libraries).

The response to the request is a new Job object. It should include a Job `name` which uniquely represents the posting. The Job `name` is used when the posting needs to be updated or deleted. As a best practice, store this `name` and map it to your own unique ID for the Job.

The server returns an error if you attempt to create a new Job when another Job already exists in the system with the same `companyName`, `requisitionId` and `languageCode`.

Cloud Talent Solution also allows you to create Jobs that are specific to a location. See [`locations`](https://docs.cloud.google.com/talent-solution/job-search/v4beta1/docs/reference/rest/v4beta1/projects.jobs#Job.FIELDS.locations) for more information.

The following code creates a Job with just the required fields for the Company specified in the `companyName` field.

You can create a Job using the code sample below. See [Quickstart: Create companies and jobs](https://docs.cloud.google.com/talent-solution/job-search/v4beta1/docs/quickstart-jobs-and-companies#create_a_job_in_your_company) for more details.

### Go

For more on installing and creating a Cloud Talent Solution client, see [Cloud Talent Solution Client Libraries](https://docs.cloud.google.com/talent-solution/job-search/v4beta1/docs/libraries). 
    
    
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

For more on installing and creating a Cloud Talent Solution client, see [Cloud Talent Solution Client Libraries](https://docs.cloud.google.com/talent-solution/job-search/v4beta1/docs/libraries). 
    
    
    import com.google.cloud.talent.v4beta1.CreateJobRequest;
    import com.google.cloud.talent.v4beta1.Job;
    import com.google.cloud.talent.v4beta1.JobServiceClient;
    import com.google.cloud.talent.v4beta1.TenantName;
    import java.io.IOException;
    import java.sql.Timestamp;
    import java.time.LocalDate;
    import java.time.LocalDateTime;
    import java.util.Arrays;
    import java.util.Calendar;
    import java.util.List;
    import java.util.Locale;
    
    public class JobSearchCreateJob {
    
      public static void createJob() throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "your-project-id";
        String tenantId = "your-tenant-id";
        String companyId = "your-company-id";
        String requisitionId = "your-unique-req-id";
        String jobApplicationUrl = "your-job-url";
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
        try (JobServiceClient jobServiceClient = JobServiceClient.create()) {
          TenantName parent = TenantName.of(projectId, tenantId);
          Job.ApplicationInfo applicationInfo =
              Job.ApplicationInfo.newBuilder().addUris(jobApplicationUrl).build();
    
          List<String> addresses =
              Arrays.asList(
                  "1600 Amphitheatre Parkway, Mountain View, CA 94043",
                  "111 8th Avenue, New York, NY 10011");
    
          // By default, job will expire in 30 days.
          // https://cloud.google.com/talent-solution/job-search/docs/jobs
          Job job =
              Job.newBuilder()
                  .setCompany(companyId)
                  .setRequisitionId(requisitionId)
                  .setTitle("Software Developer")
                  .setDescription("Develop, maintain the software solutions.")
                  .setApplicationInfo(applicationInfo)
                  .addAllAddresses(addresses)
                  .setLanguageCode("en-US")
                  .build();
    
          CreateJobRequest request =
              CreateJobRequest.newBuilder().setParent(parent.toString()).setJob(job).build();
    
          Job response = jobServiceClient.createJob(request);
          System.out.format("Created job: %s%n", response.getName());
        }
      }
    }

### Python

For more on installing and creating a Cloud Talent Solution client, see [Cloud Talent Solution Client Libraries](https://docs.cloud.google.com/talent-solution/job-search/v4beta1/docs/libraries). 
    
    
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

Cloud Talent Solution includes several job fields that are built in to the API schema. However, you may need additional fields that aren't present in the out-of-the-box options. While we recommended that you use the out-of-the box fields wherever possible, Cloud Talent Solution also provides some `customAttributes` fields for a Job. These can be filterable or non-filterable. Refer to the [`customAttributes`](https://docs.cloud.google.com/talent-solution/job-search/v4beta1/docs/reference/rest/v4beta1/projects.jobs#Job.FIELDS.custom_attributes) documentation for more information.

The following code example shows how to create a Job with a `customAttribute`:

### Go

For more on installing and creating a Cloud Talent Solution client, see [Cloud Talent Solution Client Libraries](https://docs.cloud.google.com/talent-solution/job-search/v4beta1/docs/libraries). 
    
    
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

For more on installing and creating a Cloud Talent Solution client, see [Cloud Talent Solution Client Libraries](https://docs.cloud.google.com/talent-solution/job-search/v4beta1/docs/libraries). 
    
    
    import com.google.cloud.talent.v4beta1.CreateJobRequest;
    import com.google.cloud.talent.v4beta1.CustomAttribute;
    import com.google.cloud.talent.v4beta1.Job;
    import com.google.cloud.talent.v4beta1.JobServiceClient;
    import com.google.cloud.talent.v4beta1.TenantName;
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
              String projectId,
              String tenantId,
              String companyId,
              String requisitionId)
              throws IOException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clean up any remaining background resources.
        try (JobServiceClient jobServiceClient = JobServiceClient.create()) {
          TenantName parent = TenantName.of(projectId, tenantId);
    
          // Custom attribute can be string or numeric value, and can be filtered in search queries.
          // https://cloud.google.com/talent-solution/job-search/docs/custom-attributes
          CustomAttribute customAttribute = CustomAttribute.newBuilder()
                  .addStringValues("Internship")
                  .addStringValues("Apprenticeship")
                  .setFilterable(true)
                  .build();
    
          Job job =
                  Job.newBuilder()
                          .setCompany(companyId)
                          .setTitle("Software Developer I")
                          .setDescription("This is a description of this <i>wonderful</i> job!")
                          .putCustomAttributes("FOR_STUDENTS", customAttribute)
                          .setRequisitionId(requisitionId)
                          .setLanguageCode("en-US")
                          .build();
    
          CreateJobRequest request =
                  CreateJobRequest.newBuilder().setParent(parent.toString()).setJob(job).build();
          Job response = jobServiceClient.createJob(request);
          System.out.printf("Created job: %s\n", response.getName());
        }
      }
    }

### Python

For more on installing and creating a Cloud Talent Solution client, see [Cloud Talent Solution Client Libraries](https://docs.cloud.google.com/talent-solution/job-search/v4beta1/docs/libraries). 
    
    
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

For more on installing and creating a Cloud Talent Solution client, see [Cloud Talent Solution Client Libraries](https://docs.cloud.google.com/talent-solution/job-search/v4beta1/docs/libraries). 
    
    
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

For more on installing and creating a Cloud Talent Solution client, see [Cloud Talent Solution Client Libraries](https://docs.cloud.google.com/talent-solution/job-search/v4beta1/docs/libraries). 
    
    
    import com.google.cloud.talent.v4beta1.GetJobRequest;
    import com.google.cloud.talent.v4beta1.Job;
    import com.google.cloud.talent.v4beta1.JobName;
    import com.google.cloud.talent.v4beta1.JobServiceClient;
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
        try (JobServiceClient jobServiceClient = JobServiceClient.create()) {
          JobName name = JobName.ofProjectTenantJobName(projectId, tenantId, jobId);
    
          GetJobRequest request = GetJobRequest.newBuilder().setName(name.toString()).build();
    
          Job response = jobServiceClient.getJob(request);
          System.out.format("Job name: %s%n", response.getName());
          System.out.format("Requisition ID: %s%n", response.getRequisitionId());
          System.out.format("Title: %s%n", response.getTitle());
          System.out.format("Description: %s%n", response.getDescription());
          System.out.format("Posting language: %s%n", response.getLanguageCode());
          for (String address : response.getAddressesList()) {
            System.out.format("Address: %s%n", address);
          }
          for (String email : response.getApplicationInfo().getEmailsList()) {
            System.out.format("Email: %s%n", email);
          }
          for (String websiteUri : response.getApplicationInfo().getUrisList()) {
            System.out.format("Website: %s%n", websiteUri);
          }
        }
      }
    }

### Python

For more on installing and creating a Cloud Talent Solution client, see [Cloud Talent Solution Client Libraries](https://docs.cloud.google.com/talent-solution/job-search/v4beta1/docs/libraries). 
    
    
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

You've created your first Company and Job using the Cloud Talent Solution! You're now ready to conduct a [search](https://docs.cloud.google.com/talent-solution/job-search/v4beta1/docs/quickstart-searching) across these Jobs.

## More APIs

For more information regarding the APIs and different configurations available, please see the latest [reference documentation](https://docs.cloud.google.com/talent-solution/job-search/v4beta1/docs/apis).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
