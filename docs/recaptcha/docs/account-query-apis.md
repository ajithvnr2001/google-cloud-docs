---
url: https://docs.cloud.google.com/recaptcha/docs/account-query-apis/
title: Identify accounts that show related behaviors \u00a0|\u00a0 Google Cloud Fraud Defense \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:58:18.698303+00:00
---

# Identify accounts that show related behaviors  |  Google Cloud Fraud Defense  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/recaptcha/docs/account-query-apis/

reCAPTCHA is a part of Google Cloud Fraud Defense. For more information, see [Google Cloud Fraud Defense](https://docs.cloud.google.com/security/products/fraud-defense). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Cloud Fraud Defense ](https://docs.cloud.google.com/recaptcha/docs)
  * [ Guides ](https://docs.cloud.google.com/recaptcha/docs/implementation-workflow)



Send feedback 

#  Identify accounts that show related behaviors Stay organized with collections  Save and categorize content based on your preferences. 

****

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This document describes how to identify accounts that show related behaviors. For example, you might want to identify all user accounts that are created by a malicious user. You can find accounts, account groups, and account group memberships that show related behaviors.

Identifying accounts that show related behaviors helps you find groups of fake accounts and account takeovers when a previously legitimate account is related to accounts with abusive behavior.

This feature is only available using the reCAPTCHA REST API and Client Libraries.

**Note:** You must have an Enterprise subscription to use the [Related accounts API](https://docs.cloud.google.com/recaptcha/docs/compare-tiers). For more information, see [Compare features between Fraud Defense tiers](https://docs.cloud.google.com/recaptcha/docs/compare-tiers). 

## Retrieve accounts related to a specific account

To retrieve a list of accounts related to a specified account, use the `relatedaccountgroupmemberships.search` method.

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: your Google Cloud project ID.
  * ACCOUNT_ID: the identifier that is uniquely associated with the user account for a user account to your website.
  * PAGE_SIZE: Optional. The number of account memberships to include in the response. The default value is 50, and the maximum value is 1,000. If the number of account memberships is greater than the page size, the response contains a pagination token that you can use to retrieve the next page of results.
  * NEXT_PAGE_TOKEN: Optional. The value of `nextPageToken` returned in the earlier response of this method. Specify this parameter to query more account memberships.



HTTP method and URL: 
    
    
    POST https://recaptchaenterprise.googleapis.com/v1/projects/PROJECT_ID/relatedaccountgroupmemberships:search?page_size=PAGE_SIZE&page_token=NEXT_PAGE_TOKEN

Request JSON body: 
    
    
    {
      "accountId": "ACCOUNT_ID"
    }
    
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://recaptchaenterprise.googleapis.com/v1/projects/PROJECT_ID/relatedaccountgroupmemberships:search?page_size=PAGE_SIZE&page_token=NEXT_PAGE_TOKEN"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://recaptchaenterprise.googleapis.com/v1/projects/PROJECT_ID/relatedaccountgroupmemberships:search?page_size=PAGE_SIZE&page_token=NEXT_PAGE_TOKEN" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "relatedAccountGroupMemberships": [
        {
          "name": "projects/projectId/relatedaccountgroups/groupId187/memberships/membershipId95",
          "accountId": "4RopXS59"
        },
        {
          "name": "projects/projectId/relatedaccountgroups/groupId91/memberships/membershipId23",
          "accountId": "HVMv1DTb"
        }
      ],
    
      "nextPageToken": "Q2N_rZgxUXOjNZtK1T1i0Q"
    }
    

#### Code sample

### Java

To authenticate to Fraud Defense, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.recaptchaenterprise.v1.[RecaptchaEnterpriseServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.cloud.recaptchaenterprise.v1.RecaptchaEnterpriseServiceClient.html);
    import com.google.recaptchaenterprise.v1.[RelatedAccountGroupMembership](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.RelatedAccountGroupMembership.html);
    import com.google.recaptchaenterprise.v1.[SearchRelatedAccountGroupMembershipsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.SearchRelatedAccountGroupMembershipsRequest.html);
    import java.io.IOException;
    import java.security.NoSuchAlgorithmException;
    
    public class SearchRelatedAccountGroupMemberships {
    
      public static void main(String[] args) throws IOException, NoSuchAlgorithmException {
        // TODO(developer): Replace these variables before running the sample.
        // projectId: Google Cloud Project Id.
        String projectId = "project-id";
    
        // Unique id of the customer.
        String accountId = "default" + UUID.randomUUID().toString().split("-")[0];
    
        searchRelatedAccountGroupMemberships(projectId, accountId);
      }
    
      // List group memberships for the account id.
      public static void searchRelatedAccountGroupMemberships(
          String projectId, String accountId) throws IOException {
        try ([RecaptchaEnterpriseServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.cloud.recaptchaenterprise.v1.RecaptchaEnterpriseServiceClient.html) client = [RecaptchaEnterpriseServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.cloud.recaptchaenterprise.v1.RecaptchaEnterpriseServiceClient.html).create()) {
    
          [SearchRelatedAccountGroupMembershipsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.SearchRelatedAccountGroupMembershipsRequest.html) request =
              [SearchRelatedAccountGroupMembershipsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.SearchRelatedAccountGroupMembershipsRequest.html).newBuilder()
                  .setProject(projectId)
                  .setAccountId(accountId)
                  .build();
    
          for ([RelatedAccountGroupMembership](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.RelatedAccountGroupMembership.html) groupMembership :
              client.searchRelatedAccountGroupMemberships(request).iterateAll()) {
            System.out.println(groupMembership.getName());
          }
          System.out.printf(
              "Finished searching related account group memberships for %s!", accountId);
        }
      }
    }

## Retrieve related account groups

To retrieve a list of account groups with similar behaviors, use the `relatedaccountgroups.list` method.

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: your Google Cloud project ID.
  * PAGE_SIZE: Optional. The number of account groups to include in the response. The default value is 50, and the maximum value is 1,000. If the number of account groups is greater than the page size, the response contains a pagination token that you can use to retrieve the next page of results. 
  * NEXT_PAGE_TOKEN: Optional. The value of `nextPageToken` returned in an earlier response of this method. Specify this parameter to query more account groups.



HTTP method and URL: 
    
    
    GET https://recaptchaenterprise.googleapis.com/v1/projects/PROJECT_ID/relatedaccountgroups?page_size=PAGE_SIZE&page_token=NEXT_PAGE_TOKEN

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://recaptchaenterprise.googleapis.com/v1/projects/PROJECT_ID/relatedaccountgroups?page_size=PAGE_SIZE&page_token=NEXT_PAGE_TOKEN"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://recaptchaenterprise.googleapis.com/v1/projects/PROJECT_ID/relatedaccountgroups?page_size=PAGE_SIZE&page_token=NEXT_PAGE_TOKEN" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "relatedAccountGroups": [
        {
          "name": "projects/projectId/relatedaccountgroups/groupId1"
        },
        {
          "name": "projects/projectId/relatedaccountgroups/groupId2"
        }
      ],
      "nextPageToken": "BenimQwKzIOibbOO2Lhisw"
    }
    
    

#### Code sample

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

## Retrieve related account group memberships

To retrieve a list of account group memberships with similar behaviors, use the `relatedaccountgroupmemberships.list` method.

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: your Google Cloud project ID.
  * GROUP_ID: Name of the account group for which you want to find related memberships.
  * PAGE_SIZE: Optional. The number of account group memberships to include in the response. The default value is 50, and the maximum value is 1,000. If the number of account group memberships is greater than the page size, the response contains a pagination token that you can use to retrieve the next page of results. 
  * NEXT_PAGE_TOKEN: Optional. The value of `nextPageToken` returned in the earlier response of this method. Specify this parameter to query more account group memberships.



HTTP method and URL: 
    
    
    GET https://recaptchaenterprise.googleapis.com/v1/projects/PROJECT_ID/relatedaccountgroups/GROUP_ID/memberships?page_size=PAGE_SIZE&page_token=NEXT_PAGE_TOKEN

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://recaptchaenterprise.googleapis.com/v1/projects/PROJECT_ID/relatedaccountgroups/GROUP_ID/memberships?page_size=PAGE_SIZE&page_token=NEXT_PAGE_TOKEN"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://recaptchaenterprise.googleapis.com/v1/projects/PROJECT_ID/relatedaccountgroups/GROUP_ID/memberships?page_size=PAGE_SIZE&page_token=NEXT_PAGE_TOKEN" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "relatedAccountGroupMemberships": [
        {
          "name": "projects/projectId/relatedaccountgroups/groupId/memberships/membershipId1",
          "accountId": "4RopXS59"
        },
        {
          "name": "projects/projectId/relatedaccountgroups/groupId/memberships/membershipId2",
          "accountId": "HVMv1DTb"
        }
      ],
      "nextPageToken": "WPuIn8GHU3JvcJqgvmE7Aw"
    }
    

#### Code sample

### Java

To authenticate to Fraud Defense, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.recaptchaenterprise.v1.[RecaptchaEnterpriseServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.cloud.recaptchaenterprise.v1.RecaptchaEnterpriseServiceClient.html);
    import com.google.recaptchaenterprise.v1.[ListRelatedAccountGroupMembershipsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.ListRelatedAccountGroupMembershipsRequest.html);
    import com.google.recaptchaenterprise.v1.[RelatedAccountGroupMembership](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.RelatedAccountGroupMembership.html);
    import java.io.IOException;
    
    public class ListRelatedAccountGroupMemberships {
    
      public static void main(String[] args) throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        // projectId: Google Cloud Project Id.
        String projectId = "project-id";
    
        // relatedAccountGroup: Name of the account group.
        String relatedAccountGroup = "related-account-group-name";
    
        listRelatedAccountGroupMemberships(projectId, relatedAccountGroup);
      }
    
      /** Given a group name, list memberships in the group. */
      public static void listRelatedAccountGroupMemberships(
          String projectId, String relatedAccountGroup) throws IOException {
        try ([RecaptchaEnterpriseServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.cloud.recaptchaenterprise.v1.RecaptchaEnterpriseServiceClient.html) client = [RecaptchaEnterpriseServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.cloud.recaptchaenterprise.v1.RecaptchaEnterpriseServiceClient.html).create()) {
    
          // Construct the request.
          [ListRelatedAccountGroupMembershipsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.ListRelatedAccountGroupMembershipsRequest.html) request =
              [ListRelatedAccountGroupMembershipsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.ListRelatedAccountGroupMembershipsRequest.html).newBuilder()
                  .setParent(
                      String.format(
                          "projects/%s/relatedaccountgroups/%s", projectId, relatedAccountGroup))
                  .build();
    
          for ([RelatedAccountGroupMembership](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.RelatedAccountGroupMembership.html) relatedAccountGroupMembership :
              client.listRelatedAccountGroupMemberships(request).iterateAll()) {
            System.out.println(relatedAccountGroupMembership.getName());
          }
          System.out.println("Finished listing related account group memberships.");
        }
      }
    }

## What's next

  * Learn about the following account protection features:

    * [Multi-factor authentication](https://docs.cloud.google.com/recaptcha/docs/integrate-account-verification)
    * [Password defense](https://docs.cloud.google.com/recaptcha/docs/check-passwords)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
