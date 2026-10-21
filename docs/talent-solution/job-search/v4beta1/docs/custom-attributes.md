---
url: https://docs.cloud.google.com/talent-solution/job-search/v4beta1/docs/custom-attributes/
title: Custom attributes (v4beta1) \u00a0|\u00a0 Cloud Talent Solution - Job Search v4beta1 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:53:40.918235+00:00
---

# Custom attributes (v4beta1)  |  Cloud Talent Solution - Job Search v4beta1  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/talent-solution/job-search/v4beta1/docs/custom-attributes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Cloud Talent Solution ](https://docs.cloud.google.com/talent-solution/docs)
  * [ Job Search ](https://docs.cloud.google.com/talent-solution/job-search/docs)
  * [ Job Search v4beta1 (deprecated) ](https://docs.cloud.google.com/talent-solution/job-search/v4beta1/docs)



Send feedback 

#  Custom attributes (v4beta1) Stay organized with collections  Save and categorize content based on your preferences. 

Cloud Talent Solution provides several different job attributes out-of-the-box to support the needs of various customers. **To gain the best performance from Cloud Talent Solution, it's highly recommended you use the out-of-the-box fields as much as possible.**

In addition, Cloud Talent Solution also provides custom attributes to store generic information. Custom attributes are used to provide even more flexibility to allow customers to support their business logic. Custom attributes store either a string or numerical information, and can be filtered against in search queries by setting appropriate [filters](https://docs.cloud.google.com/talent-solution/job-search/v4beta1/docs/reference/rest/v4beta1/JobQuery).

## Custom attributes features

  * **Define your own custom field name** : Define a name for a particular attribute of a job. Set this attribute to be either filterable or non-filterable depending on your needs. Typically, if the UI needs a filterable facet that is not provided out-of-the-box by Cloud Talent Solution a [`customAttribute`](https://docs.cloud.google.com/talent-solution/job-search/v4beta1/docs/reference/rpc/google.cloud.talent.v4beta1#customattribute) can be used to provide the right filtering.
  * **Case (in)sensitive search** : Each search request can specify whether the search against all custom attributes is case sensitive or case insensitive.
  * **Range based filtering** : `customAttribute` search filters can filter jobs between a range of specified numeric values. For example, if a given `customAttribute` field is used to store the minimum GPA requirements of a job, the `customAttribute` search filter can be used to return jobs within a certain minimum GPA range, greater than a minimum GPA value, lesser than a minimum GPA value, etc.
  * **Cross-field filtering** : `customAttribute` also provides customers of Cloud Talent Solution with the ability to define expressions that filter a combination of custom attributes. For example, a customer has business logic that states they only want jobs that sponsor visas, or telecommute jobs. The customer stores both these fields in a different `customAttribute`. The customer can then specify a search filter with an expression that defines the logic needed. Only 3 levels of nested expressions are supported.

  * **Keyword specific search** : Specify a certain `customAttribute` in the `keywordSearchableCustomAttributes` of the associated company to ensure search requests that contain a value in the specified customAttribute return the jobs containing this value in that customAttribute.

  * **SQL based searches:** `customAttribute` allows you to define boolean-style expressions in the search request. Cloud Talent Solution automatically parses these expressions, applies the filters to the search request, and returns results accordingly. Only 3 levels of nesting of the boolean expressions and at most 2000 characters are allowed.

  * **Define custom histogram buckets:** Custom attributes allow customers of Cloud Talent Solution to set custom buckets by which histograms can be calculated. For example, you can use a `customAttribute` to store minimum GPA information, and then create a histogram on this field. You can further create buckets from 3.0 - 3.5, 3.51 - 4.0, etc., to group all the minimum GPAs within these buckets.




## Using custom attributes

Create a new job with the [`customAttribute`](https://docs.cloud.google.com/talent-solution/job-search/v4beta1/docs/reference/rpc/google.cloud.talent.v4beta1#customattribute) field (can be used with either numeric or string values):

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
    
    

**Note:** Cloud Talent Solution allows setting both the `filterableCustomFields` and the custom attributes when creating a job, however only one of either `filterableCustomFields` or custom attributes can be set in a single search request.

By default, the `searchJobs` and `searchJobsForAlert` endpoints only search against out-of-the-box fields. If you also need to search against customAttribute fields, use the [keywordSearchableJobCustomAttributes](https://docs.cloud.google.com/talent-solution/job-search/v4beta1/docs/reference/rpc/google.cloud.talent.v4beta1#customattribute) field to define a list of custom attributes to search.

For example, if a recruiter wishes to use a `customAttribute` "customRequisitions" to store the requisition ids of jobs particular to a specific employer, then by setting `keywordSearchableJobCustomAttributes` to include this field, a regular search conducted by a recruiter for "ABC123" returns all jobs that have the `customAttribute` "customRequisitions" with a value of "ABC123".

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
