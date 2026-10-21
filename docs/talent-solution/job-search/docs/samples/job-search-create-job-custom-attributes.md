---
url: https://docs.cloud.google.com/talent-solution/job-search/docs/samples/job-search-create-job-custom-attributes/
title: Create job with client using custom attributes (v4beta1) \u00a0|\u00a0 Job Search \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:53:17.362822+00:00
---

# Create job with client using custom attributes (v4beta1)  |  Job Search  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/talent-solution/job-search/docs/samples/job-search-create-job-custom-attributes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Cloud Talent Solution ](https://docs.cloud.google.com/talent-solution/docs)
  * [ Job Search ](https://docs.cloud.google.com/talent-solution/job-search/docs)
  * [ Samples ](https://docs.cloud.google.com/talent-solution/job-search/docs/samples)



#  Create job with client using custom attributes (v4beta1) Stay organized with collections  Save and categorize content based on your preferences. 

Create job with client using custom attributes.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Custom attributes](https://docs.cloud.google.com/talent-solution/job-search/docs/custom-attributes)
  * [Custom attributes (v4beta1)](https://docs.cloud.google.com/talent-solution/job-search/v4beta1/docs/custom-attributes)
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

To learn how to install and use the client library for CTS, see [CTS client libraries](https://docs.cloud.google.com/talent-solution/job-search/docs/libraries). For more information, see the [CTS Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/overview). 

To authenticate to CTS, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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

### Node.js

To learn how to install and use the client library for CTS, see [CTS client libraries](https://docs.cloud.google.com/talent-solution/job-search/docs/libraries). For more information, see the [CTS Node.js API reference documentation](https://docs.cloud.google.com/nodejs/docs/reference/talent/latest). 

To authenticate to CTS, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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

To learn how to install and use the client library for CTS, see [CTS client libraries](https://docs.cloud.google.com/talent-solution/job-search/docs/libraries). For more information, see the [CTS Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/talent/latest). 

To authenticate to CTS, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=talentsolution). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
