---
url: https://docs.cloud.google.com/talent-solution/job-search/docs/samples/job-search-get-job-beta/
title: Get job with client (v4beta1) \u00a0|\u00a0 Job Search \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:53:19.589496+00:00
---

# Get job with client (v4beta1)  |  Job Search  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/talent-solution/job-search/docs/samples/job-search-get-job-beta/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Cloud Talent Solution ](https://docs.cloud.google.com/talent-solution/docs)
  * [ Job Search ](https://docs.cloud.google.com/talent-solution/job-search/docs)
  * [ Samples ](https://docs.cloud.google.com/talent-solution/job-search/docs/samples)



#  Get job with client (v4beta1) Stay organized with collections  Save and categorize content based on your preferences. 

Get job with client.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Job basics](https://docs.cloud.google.com/talent-solution/job-search/docs/jobs)
  * [Job basics (v4beta1)](https://docs.cloud.google.com/talent-solution/job-search/v4beta1/docs/jobs)
  * [Quickstart: Create companies and jobs](https://docs.cloud.google.com/talent-solution/job-search/docs/quickstart-jobs-and-companies)
  * [Quickstart: Create companies and jobs (v4beta1)](https://docs.cloud.google.com/talent-solution/job-search/v4beta1/docs/quickstart-jobs-and-companies)



## Code sample

### Java

To learn how to install and use the client library for CTS, see [CTS client libraries](https://docs.cloud.google.com/talent-solution/job-search/docs/libraries). For more information, see the [CTS Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/overview). 

To authenticate to CTS, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=talentsolution). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
