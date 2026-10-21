---
url: https://docs.cloud.google.com/talent-solution/job-search/v3/docs/custom-attributes/
title: Custom attributes (v3) \u00a0|\u00a0 Cloud Talent Solution - Job Search v3 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:53:47.901290+00:00
---

# Custom attributes (v3)  |  Cloud Talent Solution - Job Search v3  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/talent-solution/job-search/v3/docs/custom-attributes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Cloud Talent Solution ](https://docs.cloud.google.com/talent-solution/docs)
  * [ Job Search ](https://docs.cloud.google.com/talent-solution/job-search/docs)
  * [ Job Search v3 (deprecated) ](https://docs.cloud.google.com/talent-solution/job-search/v3/docs)



Send feedback 

#  Custom attributes (v3) Stay organized with collections  Save and categorize content based on your preferences. 

Cloud Talent Solution provides several different job attributes out-of-the-box to support the needs of various customers. **To gain the best performance from Cloud Talent Solution, it's highly recommended you use the out-of-the-box fields as much as possible.**

In addition, Cloud Talent Solution also provides custom attributes to store generic information. Custom attributes are used to provide even more flexibility to allow customers to support their business logic. Custom attributes store either a string or numerical information, and can be filtered against in search queries by setting appropriate [filters](https://docs.cloud.google.com/talent-solution/job-search/v3/docs/reference/rest/v3/JobQuery).

## Custom attributes features

  * **Define your own custom field name** : Define a name for a particular attribute of a job. Set this attribute to be either filterable or non-filterable depending on the need. Typically, if the UI needs a filterable facet that is not provided out-of-the-box by Cloud Talent Solution a [`customAttribute`](https://docs.cloud.google.com/talent-solution/job-search/v3/docs/reference/rpc/google.cloud.talent.v3#google.cloud.talent.v3.CustomAttribute) can be used to provide the right filtering.
  * **Case (in)sensitive search** : Each search request can specify whether the search against all custom attributes is case sensitive or case insensitive.
  * **Range based filtering** : `customAttribute` search filters can filter jobs between a range of specified numeric values. For example, if a given `customAttribute` field is used to store the minimum GPA requirements of a job, the `customAttribute` search filter can be used to return jobs within a certain minimum GPA range, greater than a minimum GPA value, lesser than a minimum GPA value, etc.
  * **Cross-field filtering** : `customAttribute` also provides customers of Cloud Talent Solution with the ability to define expressions that filter a combination of custom attributes. For example, a customer has business logic that states they only want jobs that sponsor visas, or telecommute jobs. The customer stores both these fields in a different `customAttribute`. The customer can then specify a search filter with an expression that defines the logic needed. Only 3 levels of nested expressions are supported.

  * **Keyword specific search** : Specify a certain `customAttribute` in the `keywordSearchableCustomAttributes` of the associated company to ensure search requests that contain a value in the specified customAttribute return the jobs containing this value in that customAttribute.

  * **SQL based searches:** `customAttribute` allows you to define boolean-style expressions in the search request. Cloud Talent Solution automatically parses these expressions, applies the filters to the search request, and returns results accordingly. Only 3 levels of nesting of the boolean expressions and at most 2000 characters are allowed.

  * **Define custom histogram buckets:** Custom attributes allow customers of Cloud Talent Solution to set custom buckets by which histograms can be calculated. For example, you can use a `customAttribute` to store minimum GPA information, and then create a histogram on this field. You can further create buckets from 3.0 - 3.5, 3.51 - 4.0, etc., to group all the minimum GPAs within these buckets.




## Using custom attributes

**Create a new job with the[`customAttribute`](https://docs.cloud.google.com/talent-solution/job-search/v3/docs/reference/rpc/google.cloud.talent.v3#google.cloud.talent.v3.CustomAttribute) field (can be used with either numeric or string values):**

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
    

**Create a filter on the[`customAttribute`](https://docs.cloud.google.com/talent-solution/job-search/v3/docs/reference/rpc/google.cloud.talent.v3#google.cloud.talent.v3.CustomAttribute) field:**

### Java

For more on installing and creating a Cloud Talent Solution client, see [Cloud Talent Solution Client Libraries](https://docs.cloud.google.com/talent-solution/job-search/v3/docs/libraries). 
    
    
    /** CustomAttributeFilter on String value CustomAttribute */
    public static void filtersOnStringValueCustomAttribute()
        throws IOException, InterruptedException {
      // Make sure to set the requestMetadata the same as the associated search request
      RequestMetadata requestMetadata =
          new RequestMetadata()
              // Make sure to hash your userID
              .setUserId("HashedUserId")
              // Make sure to hash the sessionID
              .setSessionId("HashedSessionID")
              // Domain of the website where the search is conducted
              .setDomain("www.google.com");
    
      String customAttributeFilter = "NOT EMPTY(someFieldName1)";
      JobQuery jobQuery = new JobQuery().setCustomAttributeFilter(customAttributeFilter);
    
      SearchJobsRequest searchJobsRequest =
          new SearchJobsRequest()
              .setJobQuery(jobQuery)
              .setRequestMetadata(requestMetadata)
              .setJobView("JOB_VIEW_FULL");
      SearchJobsResponse response =
          talentSolutionClient
              .projects()
              .jobs()
              .search(DEFAULT_PROJECT_ID, searchJobsRequest)
              .execute();
      Thread.sleep(1000);
      System.out.printf("Custom search job results (String value): %s\n", response);
    }

### Python

For more on installing and creating a Cloud Talent Solution client, see [Cloud Talent Solution Client Libraries](https://docs.cloud.google.com/talent-solution/job-search/v3/docs/libraries). 
    
    
    def custom_attribute_filter_string_value(client_service):
        request_metadata = {
            "user_id": "HashedUserId",
            "session_id": "HashedSessionId",
            "domain": "www.google.com",
        }
    
        custom_attribute_filter = "NOT EMPTY(someFieldName1)"
        job_query = {"custom_attribute_filter": custom_attribute_filter}
        request = {
            "request_metadata": request_metadata,
            "job_query": job_query,
            "job_view": "JOB_VIEW_FULL",
        }
    
        response = (
            client_service.projects().jobs().search(parent=parent, body=request).execute()
        )
        print(response)

### Go

For more on installing and creating a Cloud Talent Solution client, see [Cloud Talent Solution Client Libraries](https://docs.cloud.google.com/talent-solution/job-search/v3/docs/libraries). 
    
    
    // filterOnStringValueCustomAttribute searches for jobs on a string value custom
    // atrribute.
    func filterOnStringValueCustomAttribute(w io.Writer, projectID string) (*talent.SearchJobsResponse, error) {
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
    	req := &talent.SearchJobsRequest{
    		JobQuery: &talent.JobQuery{
    			CustomAttributeFilter: "NOT EMPTY(someFieldString)",
    		},
    		// Make sure to set the RequestMetadata the same as the associated
    		// search request.
    		RequestMetadata: &talent.RequestMetadata{
    			// Make sure to hash your userID.
    			UserId: "HashedUsrId",
    			// Make sure to hash the sessionID.
    			SessionId: "HashedSessionId",
    			// Domain of the website where the search is conducted.
    			Domain: "www.googlesample.com",
    		},
    		JobView: "JOB_VIEW_FULL",
    	}
    	resp, err := service.Projects.Jobs.Search(parent, req).Do()
    	if err != nil {
    		return nil, fmt.Errorf("failed to search for jobs with string value custom attribute: %w", err)
    	}
    
    	fmt.Fprintln(w, "Jobs:")
    	for _, j := range resp.MatchingJobs {
    		fmt.Fprintf(w, "\t%q\n", j.Job.Name)
    	}
    
    	return resp, nil
    }
    

**Create another filter with[`customAttribute`](https://docs.cloud.google.com/talent-solution/job-search/v3/docs/reference/rpc/google.cloud.talent.v3#google.cloud.talent.v3.CustomAttribute):**

### Java

For more on installing and creating a Cloud Talent Solution client, see [Cloud Talent Solution Client Libraries](https://docs.cloud.google.com/talent-solution/job-search/v3/docs/libraries). 
    
    
    /** CustomAttributeFilter on Long value CustomAttribute */
    public static void filtersOnLongValueCustomAttribute() throws IOException, InterruptedException {
      // Make sure to set the requestMetadata the same as the associated search request
      RequestMetadata requestMetadata =
          new RequestMetadata()
              // Make sure to hash your userID
              .setUserId("HashedUserId")
              // Make sure to hash the sessionID
              .setSessionId("HashedSessionID")
              // Domain of the website where the search is conducted
              .setDomain("www.google.com");
    
      String customAttributeFilter = "(255 <= someFieldName2) AND (someFieldName2 <= 257)";
      JobQuery jobQuery = new JobQuery().setCustomAttributeFilter(customAttributeFilter);
    
      SearchJobsRequest searchJobsRequest =
          new SearchJobsRequest()
              .setJobQuery(jobQuery)
              .setJobView("JOB_VIEW_FULL")
              .setRequestMetadata(requestMetadata);
    
      SearchJobsResponse response =
          talentSolutionClient
              .projects()
              .jobs()
              .search(DEFAULT_PROJECT_ID, searchJobsRequest)
              .execute();
      Thread.sleep(1000);
      System.out.printf("Custom search job results (Long value): %s\n", response);
    }

### Python

For more on installing and creating a Cloud Talent Solution client, see [Cloud Talent Solution Client Libraries](https://docs.cloud.google.com/talent-solution/job-search/v3/docs/libraries). 
    
    
    def custom_attribute_filter_long_value(client_service):
        request_metadata = {
            "user_id": "HashedUserId",
            "session_id": "HashedSessionId",
            "domain": "www.google.com",
        }
    
        custom_attribute_filter = "(255 <= someFieldName2) AND" " (someFieldName2 <= 257)"
        job_query = {"custom_attribute_filter": custom_attribute_filter}
        request = {
            "request_metadata": request_metadata,
            "job_query": job_query,
            "job_view": "JOB_VIEW_FULL",
        }
    
        response = (
            client_service.projects().jobs().search(parent=parent, body=request).execute()
        )
        print(response)

### Go

For more on installing and creating a Cloud Talent Solution client, see [Cloud Talent Solution Client Libraries](https://docs.cloud.google.com/talent-solution/job-search/v3/docs/libraries). 
    
    
    // filterOnLongValueCustomAttribute searches for jobs on a long value custom
    // atrribute.
    func filterOnLongValueCustomAttribute(w io.Writer, projectID string) (*talent.SearchJobsResponse, error) {
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
    	req := &talent.SearchJobsRequest{
    		JobQuery: &talent.JobQuery{
    			CustomAttributeFilter: "someFieldLong < 1000",
    		},
    		// Make sure to set the RequestMetadata the same as the associated
    		// search request.
    		RequestMetadata: &talent.RequestMetadata{
    			// Make sure to hash your userID.
    			UserId: "HashedUsrId",
    			// Make sure to hash the sessionID.
    			SessionId: "HashedSessionId",
    			// Domain of the website where the search is conducted.
    			Domain: "www.googlesample.com",
    		},
    		JobView: "JOB_VIEW_FULL",
    	}
    	resp, err := service.Projects.Jobs.Search(parent, req).Do()
    	if err != nil {
    		return nil, fmt.Errorf("failed to search for jobs with long value custom attribute: %w", err)
    	}
    
    	fmt.Fprintln(w, "Jobs:")
    	for _, j := range resp.MatchingJobs {
    		fmt.Fprintf(w, "\t%q\n", j.Job.Name)
    	}
    
    	return resp, nil
    }
    

**Leverage custom attributes to facilitate cross-field-filtering:**

The following example illustrates how to define a search request that searches for jobs with a target bonus rate between 10% and 20%, or a job which required the skills of "Team Management", OR a job which has a non-empty value in the "visa_required" `customAttribute`.

### Java

For more on installing and creating a Cloud Talent Solution client, see [Cloud Talent Solution Client Libraries](https://docs.cloud.google.com/talent-solution/job-search/v3/docs/libraries). 
    
    
    /** CustomAttributeFilter on multiple CustomAttributes */
    public static void filtersOnMultiCustomAttributes() throws IOException, InterruptedException {
      // Make sure to set the requestMetadata the same as the associated search request
      RequestMetadata requestMetadata =
          new RequestMetadata()
              // Make sure to hash your userID
              .setUserId("HashedUserId")
              // Make sure to hash the sessionID
              .setSessionId("HashedSessionID")
              // Domain of the website where the search is conducted
              .setDomain("www.google.com");
    
      String customAttributeFilter =
          "(someFieldName1 = \"value1\") "
              + "AND ((255 <= someFieldName2) OR (someFieldName2 <= 213))";
      JobQuery jobQuery = new JobQuery().setCustomAttributeFilter(customAttributeFilter);
    
      SearchJobsRequest searchJobsRequest =
          new SearchJobsRequest()
              .setJobQuery(jobQuery)
              .setRequestMetadata(requestMetadata)
              .setJobView("JOB_VIEW_FULL");
      SearchJobsResponse response =
          talentSolutionClient
              .projects()
              .jobs()
              .search(DEFAULT_PROJECT_ID, searchJobsRequest)
              .execute();
      Thread.sleep(1000);
      System.out.printf("Custom search job results (multiple value): %s\n", response);
    }

### Python

For more on installing and creating a Cloud Talent Solution client, see [Cloud Talent Solution Client Libraries](https://docs.cloud.google.com/talent-solution/job-search/v3/docs/libraries). 
    
    
    def custom_attribute_filter_multi_attributes(client_service):
        request_metadata = {
            "user_id": "HashedUserId",
            "session_id": "HashedSessionId",
            "domain": "www.google.com",
        }
    
        custom_attribute_filter = (
            '(someFieldName1 = "value1") AND ((255 <= someFieldName2) OR '
            "(someFieldName2 <= 213))"
        )
        job_query = {"custom_attribute_filter": custom_attribute_filter}
        request = {
            "request_metadata": request_metadata,
            "job_query": job_query,
            "job_view": "JOB_VIEW_FULL",
        }
    
        response = (
            client_service.projects().jobs().search(parent=parent, body=request).execute()
        )
        print(response)

### Go

For more on installing and creating a Cloud Talent Solution client, see [Cloud Talent Solution Client Libraries](https://docs.cloud.google.com/talent-solution/job-search/v3/docs/libraries). 
    
    
    // filterOnLongValueCustomAttribute searches for jobs on multiple custom
    // atrributes.
    func filterOnMultiCustomAttributes(w io.Writer, projectID string) (*talent.SearchJobsResponse, error) {
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
    	req := &talent.SearchJobsRequest{
    		JobQuery: &talent.JobQuery{
    			CustomAttributeFilter: "(someFieldString = \"someStrVal\") AND (someFieldLong < 1000)",
    		},
    		// Make sure to set the RequestMetadata the same as the associated
    		// search request.
    		RequestMetadata: &talent.RequestMetadata{
    			// Make sure to hash your userID.
    			UserId: "HashedUsrId",
    			// Make sure to hash the sessionID.
    			SessionId: "HashedSessionId",
    			// Domain of the website where the search is conducted.
    			Domain: "www.googlesample.com",
    		},
    		JobView: "JOB_VIEW_FULL",
    	}
    	resp, err := service.Projects.Jobs.Search(parent, req).Do()
    	if err != nil {
    		return nil, fmt.Errorf("failed to search for jobs with multiple custom attributes: %w", err)
    	}
    
    	fmt.Fprintln(w, "Jobs:")
    	for _, j := range resp.MatchingJobs {
    		fmt.Fprintf(w, "\t%q\n", j.Job.Name)
    	}
    
    	return resp, nil
    }
    

**Note:** Custom attributes are only available in the V2 and V3 version of Cloud Talent Solution. Cloud Talent Solution allows setting both the `filterableCustomFields` and the custom attributes while creating a job, however, only one of them can be set in a single search request.

By default, the `searchJobs` and `seachJobsForAlert` endpoints only search against out-of-the-box fields. If you also need to search against customAttribute fields, use the [keywordSearchableJobCustomAttributes](https://docs.cloud.google.com/talent-solution/job-search/v3/docs/reference/rest/v3/projects.companies#Company.FIELDS.keyword_searchable_job_custom_attributes) field to define a list of custom attributes to search.

For example, if a recruiter wishes to use a `customAttribute` "customRequisitions" to store the requisition ids of jobs particular to a specific employer, then by setting `keywordSearchableJobCustomAttributes` to include this field, a regular search conducted by a recruiter for "ABC123" returns all jobs that have the `customAttribute` "customRequisitions" with a value of "ABC123".

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
