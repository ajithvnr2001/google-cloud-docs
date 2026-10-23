---
url: https://docs.cloud.google.com/talent-solution/job-search/docs/samples/job-discovery-generate-featured-job/
title: Create featured job (v3) \u00a0|\u00a0 Job Search \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:41:47.049484+00:00
---

# Create featured job (v3)  |  Job Search  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/talent-solution/job-search/docs/samples/job-discovery-generate-featured-job/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Cloud Talent Solution ](https://docs.cloud.google.com/talent-solution/docs)
  * [ Job Search ](https://docs.cloud.google.com/talent-solution/job-search/docs)
  * [ Samples ](https://docs.cloud.google.com/talent-solution/job-search/docs/samples)



#  Create featured job (v3) Stay organized with collections  Save and categorize content based on your preferences. 

Create a featured job.

## Code sample

### Ruby

To learn how to install and use the client library for CTS, see [CTS client libraries](https://docs.cloud.google.com/talent-solution/job-search/docs/libraries). 

To authenticate to CTS, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    # company_name   = "The resource name of the company listing the job. The format is "projects/{project_id}/companies/{company_id}""
    # requisition_id = "The posting ID, assigned by the client to identify a job"
    
    require "google/apis/jobs_v3"
    require "securerandom"
    # Instantiate the client
    jobs = Google::Apis::JobsV3
    
    talent_solution_client = jobs::CloudTalentSolutionService.new
    # @see
    # https://developers.google.com/identity/protocols/application-default-credentials#callingruby
    talent_solution_client.authorization = Google::Auth.get_application_default(
      "https://www.googleapis.com/auth/jobs"
    )
    
    application_info = jobs::ApplicationInfo.new uris: ["http://careers.google.com"]
    job_generated = jobs::Job.new requisition_id:   requisition_id,
                                  title:            " Lab Technician",
                                  company_name:     company_name,
                                  application_info: application_info,
                                  description:      "Design, develop, test, deploy, " +
                                                    "maintain and improve software."
    # Featured job is the job with positive promotion value
    job_generated.promotion_value = 2
    puts "Featured Job generated: #{job_generated.to_json}"
    job_generated

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=talentsolution). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
