---
url: https://docs.cloud.google.com/iam/docs/samples/iam-enable-service-account-key/
title: Enable a service account key \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:54:31.634894+00:00
---

# Enable a service account key  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/samples/iam-enable-service-account-key/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Samples ](https://docs.cloud.google.com/iam/docs/samples)



#  Enable a service account key Stay organized with collections  Save and categorize content based on your preferences. 

Demonstrates enabling a disabled IAM service account key.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Disable and enable service account keys](https://docs.cloud.google.com/iam/docs/keys-disable-enable)



## Code sample

### Java

To learn how to install and use the client library for IAM, see [IAM client libraries](https://docs.cloud.google.com/iam/docs/reference/libraries). For more information, see the [IAM Java API reference documentation](https://developers.google.com/api-client-library/java/apis/iam/v1). 

To authenticate to IAM, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.iam.admin.v1.[IAMClient](https://docs.cloud.google.com/java/docs/reference/google-iam-admin/latest/com.google.cloud.iam.admin.v1.IAMClient.html);
    import java.io.IOException;
    
    
    public class EnableServiceAccountKey {
    
      public static void main(String[] args) throws IOException {
        // TODO(Developer): Replace the below variables before running.
        String projectId = "gcloud-project-id";
        String serviceAccountName = "service-account-name";
        String serviceAccountKeyName = "service-account-key-name";
    
        enableServiceAccountKey(projectId, serviceAccountName, serviceAccountKeyName);
      }
    
      // Enables a service account key.
      public static void enableServiceAccountKey(String projectId,
                                                 String accountName,
                                                 String key) throws IOException {
        // Construct the service account email.
        // You can modify the ".iam.gserviceaccount.com" to match the service account name in which
        // you want to enable the key.
        // See, https://cloud.google.com/iam/docs/creating-managing-service-account-keys#enabling
        String email = String.format("%s@%s.iam.gserviceaccount.com", accountName, projectId);
        String name = String.format("projects/%s/serviceAccounts/%s/keys/%s", projectId, email, key);
    
        // Initialize client that will be used to send requests.
        // This client only needs to be created once, and can be reused for multiple requests.
        try ([IAMClient](https://docs.cloud.google.com/java/docs/reference/google-iam-admin/latest/com.google.cloud.iam.admin.v1.IAMClient.html) iamClient = [IAMClient](https://docs.cloud.google.com/java/docs/reference/google-iam-admin/latest/com.google.cloud.iam.admin.v1.IAMClient.html).create()) {
          iamClient.[enableServiceAccountKey](https://docs.cloud.google.com/java/docs/reference/google-iam-admin/latest/com.google.cloud.iam.admin.v1.IAMClient.html#com_google_cloud_iam_admin_v1_IAMClient_enableServiceAccountKey__org_jspecify_annotations_Nullable_com_google_iam_admin_v1_KeyName_)(name);
    
          System.out.println("Enabled service account key: " + name);
        }
      }
    }

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=identityandaccessmanagement). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
