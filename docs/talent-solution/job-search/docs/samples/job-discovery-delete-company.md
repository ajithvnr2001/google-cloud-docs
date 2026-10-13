---
url: https://docs.cloud.google.com/talent-solution/job-search/docs/samples/job-discovery-delete-company/
title: Delete company (v3) \u00a0|\u00a0 Job Search \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:50:43.201875+00:00
---

# Delete company (v3)  |  Job Search  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/talent-solution/job-search/docs/samples/job-discovery-delete-company/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Cloud Talent Solution ](https://docs.cloud.google.com/talent-solution/docs)
  * [ Job Search ](https://docs.cloud.google.com/talent-solution/job-search/docs)
  * [ Samples ](https://docs.cloud.google.com/talent-solution/job-search/docs/samples)



#  Delete company (v3) Stay organized with collections  Save and categorize content based on your preferences. 

Delete a company.

## Code sample

### Ruby

To learn how to install and use the client library for CTS, see [CTS client libraries](https://docs.cloud.google.com/talent-solution/job-search/docs/libraries). 

To authenticate to CTS, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    # company_name  = "The name of the company you want to delete. The format is "projects/{project_id}/companies/{company_id}""
    
    require "google/apis/jobs_v3"
    
    jobs = Google::Apis::JobsV3
    talent_solution_client = jobs::CloudTalentSolutionService.new
    # @see
    # https://developers.google.com/identity/protocols/application-default-credentials#callingruby
    talent_solution_client.authorization = Google::Auth.get_application_default(
      "https://www.googleapis.com/auth/jobs"
    )
    
    begin
      talent_solution_client.delete_project_company company_name
      puts "Company deleted. CompanyName: #{company_name}"
    rescue StandardError => e
      puts "Exception occurred while deleting company: #{e}"
    end

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=talentsolution). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
