---
url: https://docs.cloud.google.com/talent-solution/job-search/docs/samples/job-custom-attribute-job/
title: define field-value pairs \u00a0|\u00a0 Job Search \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:01:11.281574+00:00
---

# define field-value pairs  |  Job Search  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/talent-solution/job-search/docs/samples/job-custom-attribute-job/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Cloud Talent Solution ](https://docs.cloud.google.com/talent-solution/docs)
  * [ Job Search ](https://docs.cloud.google.com/talent-solution/job-search/docs)
  * [ Samples ](https://docs.cloud.google.com/talent-solution/job-search/docs/samples)



#  define field-value pairs Stay organized with collections  Save and categorize content based on your preferences. 

Used to add extra fields and values to a job entry

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Custom attributes (v3)](https://docs.cloud.google.com/talent-solution/job-search/v3/docs/custom-attributes)
  * [Quickstart: Create company and job](https://docs.cloud.google.com/talent-solution/job-search/v3/docs/create-company-job)



## Code sample

### Go

To learn how to install and use the client library for CTS, see [CTS client libraries](https://docs.cloud.google.com/talent-solution/job-search/docs/libraries). For more information, see the [CTS Go API reference documentation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/talent/latest/apiv4). 

To authenticate to CTS, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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
    

### Java

To learn how to install and use the client library for CTS, see [CTS client libraries](https://docs.cloud.google.com/talent-solution/job-search/docs/libraries). For more information, see the [CTS Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/overview). 

To authenticate to CTS, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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

To learn how to install and use the client library for CTS, see [CTS client libraries](https://docs.cloud.google.com/talent-solution/job-search/docs/libraries). For more information, see the [CTS Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/talent/latest). 

To authenticate to CTS, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=talentsolution). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
