---
url: https://docs.cloud.google.com/recaptcha/docs/samples/recaptcha-enterprise-list-related-account-group/
title: List related account groups \u00a0|\u00a0 Google Cloud Fraud Defense \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:57:55.075763+00:00
---

# List related account groups  |  Google Cloud Fraud Defense  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/recaptcha/docs/samples/recaptcha-enterprise-list-related-account-group/

reCAPTCHA is a part of Google Cloud Fraud Defense. For more information, see [Google Cloud Fraud Defense](https://docs.cloud.google.com/security/products/fraud-defense). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Cloud Fraud Defense ](https://docs.cloud.google.com/recaptcha/docs)
  * [ Samples ](https://docs.cloud.google.com/recaptcha/docs/samples)



#  List related account groups Stay organized with collections  Save and categorize content based on your preferences. 

List related account groups in a project.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Identify accounts that show related behaviors](https://docs.cloud.google.com/recaptcha/docs/account-query-apis)



## Code sample

### Java

To authenticate to Fraud Defense, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.recaptchaenterprise.v1.[RecaptchaEnterpriseServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.cloud.recaptchaenterprise.v1.RecaptchaEnterpriseServiceClient.html);
    import com.google.recaptchaenterprise.v1.[ListRelatedAccountGroupsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.ListRelatedAccountGroupsRequest.html);
    import com.google.recaptchaenterprise.v1.[RelatedAccountGroup](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.RelatedAccountGroup.html);
    import java.io.IOException;
    
    public class ListRelatedAccountGroups {
    
      public static void main(String[] args) throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        // projectId : Google Cloud Project Id.
        String projectId = "project-id";
    
        listRelatedAccountGroups(projectId);
      }
    
      // List related account groups in the project.
      public static void listRelatedAccountGroups(String projectId) throws IOException {
        try ([RecaptchaEnterpriseServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.cloud.recaptchaenterprise.v1.RecaptchaEnterpriseServiceClient.html) client = [RecaptchaEnterpriseServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.cloud.recaptchaenterprise.v1.RecaptchaEnterpriseServiceClient.html).create()) {
    
          [ListRelatedAccountGroupsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.ListRelatedAccountGroupsRequest.html) request =
              [ListRelatedAccountGroupsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.ListRelatedAccountGroupsRequest.html).newBuilder().setParent("projects/" + projectId).build();
    
          System.out.println("Listing related account groups..");
          for ([RelatedAccountGroup](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.RelatedAccountGroup.html) group : client.listRelatedAccountGroups(request).iterateAll()) {
            System.out.println(group.getName());
          }
        }
      }
    }

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=recaptcha_enterprise). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
