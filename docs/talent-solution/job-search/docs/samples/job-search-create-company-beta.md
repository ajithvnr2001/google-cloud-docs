---
url: https://docs.cloud.google.com/talent-solution/job-search/docs/samples/job-search-create-company-beta/
title: Create company with client (v4beta1) \u00a0|\u00a0 Job Search \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:34:44.950406+00:00
---

# Create company with client (v4beta1)  |  Job Search  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/talent-solution/job-search/docs/samples/job-search-create-company-beta/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Cloud Talent Solution ](https://docs.cloud.google.com/talent-solution/docs)
  * [ Job Search ](https://docs.cloud.google.com/talent-solution/job-search/docs)
  * [ Samples ](https://docs.cloud.google.com/talent-solution/job-search/docs/samples)



#  Create company with client (v4beta1) Stay organized with collections  Save and categorize content based on your preferences. 

Create company with client.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Create and update companies](https://docs.cloud.google.com/talent-solution/job-search/docs/companies)
  * [Create and update companies (v4beta1)](https://docs.cloud.google.com/talent-solution/job-search/v4beta1/docs/companies)
  * [Quickstart: Create companies and jobs](https://docs.cloud.google.com/talent-solution/job-search/docs/quickstart-jobs-and-companies)
  * [Quickstart: Create companies and jobs (v4beta1)](https://docs.cloud.google.com/talent-solution/job-search/v4beta1/docs/quickstart-jobs-and-companies)



## Code sample

### Java

To learn how to install and use the client library for CTS, see [CTS client libraries](https://docs.cloud.google.com/talent-solution/job-search/docs/libraries). For more information, see the [CTS Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/overview). 

To authenticate to CTS, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=talentsolution). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
