---
url: https://docs.cloud.google.com/talent-solution/job-search/v3/docs/create-company-job/
title: Quickstart: Create company and job \u00a0|\u00a0 Cloud Talent Solution - Job Search v3 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:53:19.951590+00:00
---

# Quickstart: Create company and job  |  Cloud Talent Solution - Job Search v3  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/talent-solution/job-search/v3/docs/create-company-job/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Cloud Talent Solution ](https://docs.cloud.google.com/talent-solution/docs)
  * [ Job Search ](https://docs.cloud.google.com/talent-solution/job-search/docs)
  * [ Job Search v3 (deprecated) ](https://docs.cloud.google.com/talent-solution/job-search/v3/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Create company and job

This tutorial is designed to get you started exploring and developing applications with Cloud Talent Solution. Familiarity with basic programming is assumed, though even without much programming knowledge, you should be able to follow along. After going through this tutorial, you should be able to use the [Cloud Talent Solution reference](https://docs.cloud.google.com/talent-solution/job-search/v3/docs/reference/rest) documentation to create your own basic applications.

This tutorial steps through a Cloud Talent Solution application using Java code. The purpose here is not to explain the Java client libraries, but to explain how to make calls to Cloud Talent Solution. Applications in Python and Node.js are essentially similar. Please [contact us](https://docs.cloud.google.com/talent-solution/docs/support) if you have any questions.

## Before you begin

You have:

  * followed the steps to create and set up your project, as listed in [Before You Begin](https://docs.cloud.google.com/talent-solution/job-search/v3/docs/before-you-begin),
  * set up your environment using [Application Default Credentials](https://developers.google.com/identity/protocols/application-default-credentials),
  * basic familiarity with Java or Python programming,
  * installed the latest [Google API Java client](https://developers.google.com/api-client-library/java/google-api-java-client/setup) or [Google API Python client](https://developers.google.com/api-client-library/python/start/get_started).



## Create a company with jobs and search for those jobs

This tutorial walks you through a basic Cloud Talent Solution application, and guides you through creating a single job that you associate to a company. The next tutorial walks you through the steps to search for jobs within the company based on attributes of the jobs and the search query. The `search` API attempts to return jobs most relevant to a job seeker's query based on available fields within a job (company name, job title, job description, job categories, job location, etc.).

**Note:** Copy the code to your clipboard by mousing over the copy icon in the code snippet, and clicking. Copy this code into a file within your development directory.

## Create service with your credentials

Create the service with the JSON credential file you downloaded in [Before You Begin](https://docs.cloud.google.com/talent-solution/job-search/v3/docs/before-you-begin):

### Java

For more on installing and creating a Cloud Talent Solution client, see [Cloud Talent Solution Client Libraries](https://docs.cloud.google.com/talent-solution/job-search/v3/docs/libraries). 
    
    
    private static final JsonFactory JSON_FACTORY = new GsonFactory();
    private static final NetHttpTransport NET_HTTP_TRANSPORT = new NetHttpTransport();
    private static final String DEFAULT_PROJECT_ID =
        "projects/" + System.getenv("GOOGLE_CLOUD_PROJECT");
    
    private static CloudTalentSolution talentSolutionClient =
        createTalentSolutionClient(generateCredential());
    
    private static CloudTalentSolution createTalentSolutionClient(GoogleCredentials credential) {
      String url = "https://jobs.googleapis.com";
    
      HttpRequestInitializer requestInitializer =
          request -> {
            new HttpCredentialsAdapter(credential).initialize(request);
            request.setConnectTimeout(60000); // 1 minute connect timeout
            request.setReadTimeout(60000); // 1 minute read timeout
          };
    
      return new CloudTalentSolution.Builder(NET_HTTP_TRANSPORT, JSON_FACTORY, requestInitializer)
          .setApplicationName("JobServiceClientSamples")
          .setRootUrl(url)
          .build();
    }
    
    private static GoogleCredentials generateCredential() {
      try {
        // Credentials could be downloaded after creating service account
        // set the `GOOGLE_APPLICATION_CREDENTIALS` environment variable, for example:
        // export GOOGLE_APPLICATION_CREDENTIALS=/path/to/your/key.json
        return GoogleCredentials.getApplicationDefault()
            .createScoped(Collections.singleton(CloudTalentSolutionScopes.JOBS));
      } catch (Exception e) {
        System.out.println("Error in generating credential");
        throw new RuntimeException(e);
      }
    }
    
    public static CloudTalentSolution getTalentSolutionClient() {
      return talentSolutionClient;
    }
    
    public static void main(String... args) throws Exception {
      try {
        ListCompaniesResponse listCompaniesResponse =
            talentSolutionClient.projects().companies().list(DEFAULT_PROJECT_ID).execute();
        System.out.println("Request Id is " + listCompaniesResponse.getMetadata().getRequestId());
        if (listCompaniesResponse.getCompanies() != null) {
          for (Company company : listCompaniesResponse.getCompanies()) {
            System.out.println(company.getName());
          }
        }
      } catch (IOException e) {
        System.out.println("Got exception while listing companies");
        throw e;
      }
    }
    

### Python

For more on installing and creating a Cloud Talent Solution client, see [Cloud Talent Solution Client Libraries](https://docs.cloud.google.com/talent-solution/job-search/v3/docs/libraries). 
    
    
    import os
    
    from googleapiclient.discovery import build
    from googleapiclient.errors import Error
    
    client_service = build("jobs", "v3")
    
    
    def run_sample():
        try:
            project_id = "projects/" + os.environ["GOOGLE_CLOUD_PROJECT"]
            response = (
                client_service.projects().companies().list(parent=project_id).execute()
            )
            print("Request Id: %s" % response.get("metadata").get("requestId"))
            print("Companies:")
            if response.get("companies") is not None:
                for company in response.get("companies"):
                    print("%s" % company.get("name"))
            print("")
    
        except Error as e:
            print("Got exception while listing companies")
            raise e
    
    
    if __name__ == "__main__":
        run_sample()

### Go

For more on installing and creating a Cloud Talent Solution client, see [Cloud Talent Solution Client Libraries](https://docs.cloud.google.com/talent-solution/job-search/v3/docs/libraries). 
    
    
    // Command quickstart is an example of using the Google Cloud Talent Solution API.
    package main
    
    import (
    	"context"
    	"fmt"
    	"log"
    	"os"
    
    	"golang.org/x/oauth2/google"
    	talent "google.golang.org/api/jobs/v3"
    )
    
    func main() {
    	projectID := os.Getenv("GOOGLE_CLOUD_PROJECT")
    	parent := fmt.Sprintf("projects/%s", projectID)
    
    	// Authorize the client using Application Default Credentials.
    	// See https://g.co/dv/identity/protocols/application-default-credentials
    	ctx := context.Background()
    	client, err := google.DefaultClient(ctx, talent.CloudPlatformScope)
    	if err != nil {
    		log.Fatal(err)
    	}
    
    	// Create the jobs service client.
    	ctsService, err := talent.New(client)
    	if err != nil {
    		log.Fatal(err)
    	}
    
    	// Make the RPC call.
    	response, err := ctsService.Projects.Companies.List(parent).Do()
    	if err != nil {
    		log.Fatalf("Failed to list Companies: %v", err)
    	}
    
    	// Print the request id.
    	fmt.Printf("Request ID: %q\n", response.Metadata.RequestId)
    
    	// Print the returned companies.
    	for _, company := range response.Companies {
    		fmt.Printf("Company: %q\n", company.Name)
    	}
    }
    

This code configures the client service with your application's credential information. The OAuth 2.0 request is sent when an API call is made. The auth token generated using the process above typically has an expiration date of 1 hour, after which you'll get an error if you try to use it. The `GoogleCredential` library takes care of automatically "refreshing" the token which simply means getting a new access token.

## Create company

A company is an entity associated with a set of job listings. You must create the company before you can post jobs on Cloud Talent Solution for that company. You can send any freeform string as the `externalId` when creating the company. This means you can use the primary key from your existing database (if you have one) when creating and referring to a company.

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
    

**Note:** Cloud Talent Solution creation calls return a unique name for each company/job. Store these names as they are used to update/delete/reference companies/jobs.

## Get company

You can read the present state of a company by sending a GET request, along with the `name` of the company assigned by our backend.

### Java

For more on installing and creating a Cloud Talent Solution client, see [Cloud Talent Solution Client Libraries](https://docs.cloud.google.com/talent-solution/job-search/v3/docs/libraries). 
    
    
    /** Get a company. */
    public static Company getCompany(String companyName) throws IOException {
      try {
        Company companyExisted =
            talentSolutionClient.projects().companies().get(companyName).execute();
        System.out.println("Company existed: " + companyExisted);
        return companyExisted;
      } catch (IOException e) {
        System.out.println("Got exception while getting company");
        throw e;
      }
    }

### Python

For more on installing and creating a Cloud Talent Solution client, see [Cloud Talent Solution Client Libraries](https://docs.cloud.google.com/talent-solution/job-search/v3/docs/libraries). 
    
    
    def get_company(client_service, company_name):
        try:
            company_existed = (
                client_service.projects().companies().get(name=company_name).execute()
            )
            print("Company existed: %s" % company_existed)
            return company_existed
        except Error as e:
            print("Got exception while getting company")
            raise e

### Go

For more on installing and creating a Cloud Talent Solution client, see [Cloud Talent Solution Client Libraries](https://docs.cloud.google.com/talent-solution/job-search/v3/docs/libraries). 
    
    
    // getCompany gets an existing company by name.
    func getCompany(w io.Writer, name string) (*talent.Company, error) {
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
    
    	company, err := service.Projects.Companies.Get(name).Do()
    	if err != nil {
    		return nil, fmt.Errorf("failed to get company %q: %w", name, err)
    	}
    
    	fmt.Fprintf(w, "Company: %q\n", company.Name)
    
    	return company, nil
    }
    

## Create job

To post a new job, you must provide all of the required fields about the new job along with the `companyName` of the company you want to associate this job with, which you specified when you created the company resource.

The data object with the job data filled in is sent to the Cloud Talent Solution endpoint using a POST request. Note that the `name` field should not be set in the initial request since it is an "output only" field of the `createJob` API and is a part of the API response when a new job entity is created by the server. The API endpoint to interact with the jobs resource is specified in the [Cloud Talent Solution Client Libraries document](https://docs.cloud.google.com/talent-solution/job-search/v3/docs/libraries).

The response to the request is an object of the new job posting; it should include a job `name` which uniquely represents the posting. The job `name` is used when the posting needs to be updated or deleted. As a best practice, store this `name` and map it to your own unique ID for the job.

The server returns an error if you attempt to insert a job when another job already exists on the system with the same `companyName`, `requisitionId` and `languageCode` for the same company.

The following code creates a job with just the required fields for the company specified in the `companyName` field.

### Java

For more on installing and creating a Cloud Talent Solution client, see [Cloud Talent Solution Client Libraries](https://docs.cloud.google.com/talent-solution/job-search/v3/docs/libraries). 
    
    
    /** Create a job. */
    public static Job createJob(Job jobToBeCreated) throws IOException {
      try {
        CreateJobRequest createJobRequest = new CreateJobRequest().setJob(jobToBeCreated);
    
        Job jobCreated =
            talentSolutionClient
                .projects()
                .jobs()
                .create(DEFAULT_PROJECT_ID, createJobRequest)
                .execute();
        System.out.println("Job created: " + jobCreated);
        return jobCreated;
      } catch (IOException e) {
        System.out.println("Got exception while creating job");
        throw e;
      }
    }

### Python

For more on installing and creating a Cloud Talent Solution client, see [Cloud Talent Solution Client Libraries](https://docs.cloud.google.com/talent-solution/job-search/v3/docs/libraries). 
    
    
    def create_job(client_service, job_to_be_created):
        try:
            request = {"job": job_to_be_created}
            job_created = (
                client_service.projects()
                .jobs()
                .create(parent=parent, body=request)
                .execute()
            )
            print("Job created: %s" % job_created)
            return job_created
        except Error as e:
            print("Got exception while creating job")
            raise e

### Go

For more on installing and creating a Cloud Talent Solution client, see [Cloud Talent Solution Client Libraries](https://docs.cloud.google.com/talent-solution/job-search/v3/docs/libraries). 
    
    
    // createJob create a job as given.
    func createJob(w io.Writer, projectID string, jobToCreate *talent.Job) (*talent.Job, error) {
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
    	req := &talent.CreateJobRequest{
    		Job: jobToCreate,
    	}
    	job, err := service.Projects.Jobs.Create(parent, req).Do()
    	if err != nil {
    		return nil, fmt.Errorf("Failed to create job %q, Err: %w", jobToCreate.RequisitionId, err)
    	}
    	return job, err
    }
    

Cloud Talent Solution also allows you to create jobs that are specific to a location. See [`locations`](https://docs.cloud.google.com/talent-solution/job-search/v3/docs/reference/rest/v3/projects.jobs#Job.FIELDS.locations) for more information.

Cloud Talent Solution has several fields associated with a job that are built in to the API schema. However, you might still have some fields that aren't a part of the out-of-the-box fields. While it is recommended that all customers of Cloud Talent Solution always use the out-of-the box fields wherever possible, Cloud Talent Solution also provides some customAttributes for a job. These might be filterable or non-filterable. Refer to the [`customAttributes`](https://docs.cloud.google.com/talent-solution/job-search/v3/docs/reference/rest/v3/projects.jobs#Job.FIELDS.custom_attributes) for more information.

The following code example shows how to create a job with a `customAttribute`:

### Java

For more on installing and creating a Cloud Talent Solution client, see [Cloud Talent Solution Client Libraries](https://docs.cloud.google.com/talent-solution/job-search/v3/docs/libraries). 
    
    
    /** Generate a job with a custom attribute. */
    @SuppressWarnings("checkstyle:AbbreviationAsWordInName")
    public static Job generateJobWithACustomAttribute(String companyName) {
      // requisition id should be a unique Id in your system.
      String requisitionId = "jobWithACustomAttribute:" + String.valueOf(new Random().nextLong());
      ApplicationInfo applicationInfo =
          new ApplicationInfo().setUris(Arrays.asList("http://careers.google.com"));
    
      // Constructs custom attributes map
      Map<String, CustomAttribute> customAttributes = new HashMap<>();
      customAttributes.put(
          "someFieldName1",
          new CustomAttribute().setStringValues(Arrays.asList("value1")).setFilterable(Boolean.TRUE));
      customAttributes.put(
          "someFieldName2",
          new CustomAttribute().setLongValues(Arrays.asList(256L)).setFilterable(true));
    
      // Creates job with custom attributes
      Job job =
          new Job()
              .setCompanyName(companyName)
              .setRequisitionId(requisitionId)
              .setTitle("Software Engineer")
              .setApplicationInfo(applicationInfo)
              .setDescription("Design, develop, test, deploy, maintain and improve software.")
              .setCustomAttributes(customAttributes);
      System.out.println("Job generated: " + job);
      return job;
    }

### Python

For more on installing and creating a Cloud Talent Solution client, see [Cloud Talent Solution Client Libraries](https://docs.cloud.google.com/talent-solution/job-search/v3/docs/libraries). 
    
    
    def generate_job_with_custom_attributes(company_name):
        # Requisition id should be a unique Id in your system.
        requisition_id = "job_with_custom_attributes:" + "".join(
            random.choice(string.ascii_uppercase + string.digits) for _ in range(16)
        )
    
        job_title = "Software Engineer"
        application_urls = ["http://careers.google.com"]
        description = "Design, develop, test, deploy, maintain and improve " "software."
    
        custom_attributes = {
            "someFieldName1": {"string_values": ["value1"], "filterable": True},
            "someFieldName2": {"long_values": [256], "filterable": True},
        }
    
        job = {
            "company_name": company_name,
            "requisition_id": requisition_id,
            "title": job_title,
            "application_info": {"uris": application_urls},
            "description": description,
            "custom_attributes": custom_attributes,
        }
        print("Job generated: %s" % job)
        return job

### Go

For more on installing and creating a Cloud Talent Solution client, see [Cloud Talent Solution Client Libraries](https://docs.cloud.google.com/talent-solution/job-search/v3/docs/libraries). 
    
    
    // constructJobWithCustomAttributes constructs a job with custom attributes.
    func constructJobWithCustomAttributes(companyName string, jobTitle string) *talent.Job {
    	// requisitionID shoud be the unique ID in your system
    	requisitionID := fmt.Sprintf("job-with-custom-attribute-%d", time.Now().UnixNano())
    
    	job := &talent.Job{
    		RequisitionId: requisitionID,
    		Title:         jobTitle,
    		CompanyName:   companyName,
    		ApplicationInfo: &talent.ApplicationInfo{
    			Uris: []string{"https://googlesample.com/career"},
    		},
    		Description: "Design, devolop, test, deploy, maintain and improve software.",
    		CustomAttributes: map[string]talent.CustomAttribute{
    			"someFieldString": {
    				Filterable:   true,
    				StringValues: []string{"someStrVal"},
    			},
    			"someFieldLong": {
    				Filterable: true,
    				LongValues: []int64{900},
    			},
    		},
    	}
    	return job
    }
    

## Retrieve job

You can confirm that the job was created by using the GET operation to GET the details of the job. Note that it might take a couple of minutes for the job to become available, based on the current volume of jobs being created in Cloud Talent Solution.

You can retrieve the details of a previously inserted job by sending a GET request to the Cloud Talent Solution. The URI should include the previously inserted job `name` returned by the original create request, as a URL parameter.

The following example uses a GET operation to retrieve the details of a job with a given `name`:

### Java

For more on installing and creating a Cloud Talent Solution client, see [Cloud Talent Solution Client Libraries](https://docs.cloud.google.com/talent-solution/job-search/v3/docs/libraries). 
    
    
    /** Get a job. */
    public static Job getJob(String jobName) throws IOException {
      try {
        Job jobExisted = talentSolutionClient.projects().jobs().get(jobName).execute();
        System.out.println("Job existed: " + jobExisted);
        return jobExisted;
      } catch (IOException e) {
        System.out.println("Got exception while getting job");
        throw e;
      }
    }

### Python

For more on installing and creating a Cloud Talent Solution client, see [Cloud Talent Solution Client Libraries](https://docs.cloud.google.com/talent-solution/job-search/v3/docs/libraries). 
    
    
    def get_job(client_service, job_name):
        try:
            job_existed = client_service.projects().jobs().get(name=job_name).execute()
            print("Job existed: %s" % job_existed)
            return job_existed
        except Error as e:
            print("Got exception while getting job")
            raise e

### Go

For more on installing and creating a Cloud Talent Solution client, see [Cloud Talent Solution Client Libraries](https://docs.cloud.google.com/talent-solution/job-search/v3/docs/libraries). 
    
    
    // getJob gets a job by name.
    func getJob(w io.Writer, jobName string) (*talent.Job, error) {
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
    
    	job, err := service.Projects.Jobs.Get(jobName).Do()
    	if err != nil {
    		return nil, fmt.Errorf("Failed to get job %s: %w", jobName, err)
    	}
    
    	fmt.Fprintf(w, "Job: %q", job.Name)
    
    	return job, err
    }
    

## Search for jobs

You've created your first company and job using the Cloud Talent Solution! You're now ready to [search](https://docs.cloud.google.com/talent-solution/job-search/v3/docs/quickstart-searching) to conduct a search across these jobs.

## What's next

  * Learn more about [companies](https://docs.cloud.google.com/talent-solution/job-search/v3/docs/companies).
  * Learn more about [jobs](https://docs.cloud.google.com/talent-solution/job-search/v3/docs/jobs).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
