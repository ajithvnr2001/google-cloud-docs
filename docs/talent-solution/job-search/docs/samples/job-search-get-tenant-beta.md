---
url: https://docs.cloud.google.com/talent-solution/job-search/docs/samples/job-search-get-tenant-beta/
title: Get tenant (v4beta1) \u00a0|\u00a0 Job Search \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:58:52.671462+00:00
---

# Get tenant (v4beta1)  |  Job Search  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/talent-solution/job-search/docs/samples/job-search-get-tenant-beta/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Cloud Talent Solution ](https://docs.cloud.google.com/talent-solution/docs)
  * [ Job Search ](https://docs.cloud.google.com/talent-solution/job-search/docs)
  * [ Samples ](https://docs.cloud.google.com/talent-solution/job-search/docs/samples)



#  Get tenant (v4beta1) Stay organized with collections  Save and categorize content based on your preferences. 

Get tenant.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Tenant basics](https://docs.cloud.google.com/talent-solution/job-search/docs/tenants)
  * [Tenant basics (v4beta1)](https://docs.cloud.google.com/talent-solution/job-search/v4beta1/docs/tenants)



## Code sample

### Java

To learn how to install and use the client library for CTS, see [CTS client libraries](https://docs.cloud.google.com/talent-solution/job-search/docs/libraries). For more information, see the [CTS Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/overview). 

To authenticate to CTS, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.talent.v4beta1.GetTenantRequest;
    import com.google.cloud.talent.v4beta1.Tenant;
    import com.google.cloud.talent.v4beta1.TenantName;
    import com.google.cloud.talent.v4beta1.TenantServiceClient;
    import java.io.IOException;
    
    public class JobSearchGetTenant {
    
      public static void getTenant() throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "your-project-id";
        String tenantId = "your-tenant-id";
        getTenant(projectId, tenantId);
      }
    
      // Get Tenant by name.
      public static void getTenant(String projectId, String tenantId) throws IOException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clean up any remaining background resources.
        try (TenantServiceClient tenantServiceClient = TenantServiceClient.create()) {
          TenantName name = TenantName.of(projectId, tenantId);
    
          GetTenantRequest request = GetTenantRequest.newBuilder().setName(name.toString()).build();
    
          Tenant response = tenantServiceClient.getTenant(request);
          System.out.format("Name: %s%n", response.getName());
          System.out.format("External ID: %s%n", response.getExternalId());
        }
      }
    }

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=talentsolution). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
