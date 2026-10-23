---
url: https://docs.cloud.google.com/talent-solution/job-search/docs/samples/job-discovery-batch-create-jobs/
title: Batch create jobs (v3) \u00a0|\u00a0 Job Search \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:41:11.075072+00:00
---

# Batch create jobs (v3)  |  Job Search  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/talent-solution/job-search/docs/samples/job-discovery-batch-create-jobs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Cloud Talent Solution ](https://docs.cloud.google.com/talent-solution/docs)
  * [ Job Search ](https://docs.cloud.google.com/talent-solution/job-search/docs)
  * [ Samples ](https://docs.cloud.google.com/talent-solution/job-search/docs/samples)



#  Batch create jobs (v3) Stay organized with collections  Save and categorize content based on your preferences. 

Create multiple jobs.

## Code sample

### Ruby

To learn how to install and use the client library for CTS, see [CTS client libraries](https://docs.cloud.google.com/talent-solution/job-search/docs/libraries). 

To authenticate to CTS, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    # project_id     = "Id of the project"
    # company_name   = "The resource name of the company listing the job. The format is "projects/{project_id}/companies/{company_id}""
    
    require "google/apis/jobs_v3"
    
    jobs = Google::Apis::JobsV3
    talent_solution_client = jobs::CloudTalentSolutionService.new
    # @see https://developers.google.com/identity/protocols/application-default-credentials#callingruby
    talent_solution_client.authorization = Google::Auth.get_application_default(
      "https://www.googleapis.com/auth/jobs"
    )
    
    jobs_created = []
    job_generated1 = jobs::Job.new requisition_id:   "Job: #{company_name} 1",
                                   title:            " Lab Technician",
                                   company_name:     company_name,
                                   employment_types: ["FULL_TIME"],
                                   language_code:    "en-US",
                                   application_info:
                                                     (jobs::ApplicationInfo.new uris: ["http://careers.google.com"]),
                                   description:      "Design and improve software."
    job_generated2 = jobs::Job.new requisition_id:   "Job: #{company_name} 2",
                                   title:            "Systems Administrator",
                                   company_name:     company_name,
                                   employment_types: ["FULL_TIME"],
                                   language_code:    "en-US",
                                   application_info:
                                                     (jobs::ApplicationInfo.new uris: ["http://careers.google.com"]),
                                   description:      "System Administrator for software."
    
    create_job_request1 = jobs::CreateJobRequest.new job: job_generated1
    create_job_request2 = jobs::CreateJobRequest.new job: job_generated2
    
    talent_solution_client.batch do |client|
      client.create_job project_id, create_job_request1 do |job, err|
        if err.nil?
          jobs_created.push job
        else
          puts "Batch job create error message: #{err.message}"
        end
      end
      client.create_job project_id, create_job_request2 do |job, err|
        if err.nil?
          jobs_created.push job
        else
          puts "Batch job create error message: #{err.message}"
        end
      end
    end
    # jobCreated = batchCreate.create_job(project_id, create_job_request1)
    puts "Batch job created: #{jobs_created.to_json}"
    jobs_created

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=talentsolution). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
