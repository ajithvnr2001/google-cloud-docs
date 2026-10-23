---
url: https://docs.cloud.google.com/iam/docs/workload-download-cred-and-grant-access/
title: Download credential configuration and grant access \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:10:09.524470+00:00
---

# Download credential configuration and grant access  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/workload-download-cred-and-grant-access/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Identity and Access Management (IAM) ](https://docs.cloud.google.com/iam/docs)
  * [ Guides ](https://docs.cloud.google.com/iam/docs/overview)



Send feedback 

#  Download credential configuration and grant access Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to configure your workloads to access Google Cloud resources by using Workload Identity Federation and either direct resource access or [service account impersonation](https://docs.cloud.google.com/iam/docs/workload-identity-federation-with-other-clouds#allow_the_external_workload_to_impersonate_the_service_account).

You can find end-to-end, use case-specific instructions in configuration guides for [AWS and Azure](https://docs.cloud.google.com/iam/docs/workload-identity-federation-with-other-clouds), [Active Directory](https://docs.cloud.google.com/iam/docs/workload-identity-federation-with-active-directory), [GitHub, GitLab, and other deployment pipelines](https://docs.cloud.google.com/iam/docs/workload-identity-federation-with-deployment-pipelines), and [Kubernetes](https://docs.cloud.google.com/iam/docs/workload-identity-federation-with-kubernetes).

## Allow your external workload to access Google Cloud resources

To provide your workload with access to Google Cloud resources, we recommend that you grant direct resource access to the principal. In this case, the principal is the federated user. Some Google Cloud products have [Google Cloud API limitations](https://docs.cloud.google.com/iam/docs/federated-identity-supported-services). If your workload calls an API endpoint that has a limitation, you can instead use service account impersonation. In this case, the principal is the Google Cloud service account, which acts as the identity. You grant access to the service account on the resource. 

### Direct resource access

You can grant access to a federated identity directly on resources by using the Google Cloud console or the gcloud CLI.

### Console

To use the Google Cloud console to grant IAM roles directly on a resource, you must go to the resource's page, and then grant the role. The following example shows you how to go to the Cloud Storage page and grant the role Storage Object Viewer (`roles/storage.objectViewer`) to a federated identity directly on a Cloud Storage bucket.

  1. In the Google Cloud console, go to the Cloud Storage **Buckets** page.  


[Go to Buckets](https://console.cloud.google.com/storage/browser)

  2. In the list of buckets, click the name of the bucket for which you want to grant the role.

  3. Select the **Permissions** tab near the top of the page.

  4. Click the _add_box_ **Grant access** button.

The **Add principals** dialog appears.

  5. In the **New principals** field, enter one or more identities that need access to your bucket.

###  By subject 
         
         principal://iam.googleapis.com/projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/POOL_ID/subject/SUBJECT
         

Replace the following:

     * `PROJECT_NUMBER`: the project number
     * `POOL_ID`: the workload pool ID
     * `SUBJECT`: the individual subject mapped from your IdP—for example, `administrator@example.com`

###  By group 
    
    principalSet://iam.googleapis.com/projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/POOL_ID/group/GROUP
    

Replace the following:

     * `PROJECT_NUMBER`: the project number
     * `WORKLOAD_POOL_ID`: the workload pool ID
     * `GROUP`: the group mapped from your IdP—for example: `administrator-group@example.com`

###  By attribute 
    
    principalSet://iam.googleapis.com/projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/POOL_ID/attribute.ATTRIBUTE_NAME/ATTRIBUTE_VALUE
    

Replace the following:

     * `PROJECT_NUMBER`: the project number
     * `WORKLOAD_POOL_ID`: the workload pool ID
     * `ATTRIBUTE_NAME`: one of the attributes that was mapped from your IdP
     * `ATTRIBUTE_VALUE`: the value of the attribute

  6. Select a role (or roles) from the **Select a role** drop-down menu. The roles you select appear in the pane with a short description of the permissions they grant.

  7. Click **Save**.




###  gcloud 

To use the gcloud CLI to grant IAM roles on a resource in a project, do the following:

  1. Obtain the project number of the project in which the resource is defined.
         
         gcloud projects describe $(gcloud config get-value core/project) --format=value\(projectNumber\)
         

  2. Grant access to the resource.

To use the gcloud CLI to grant the role Storage Object Viewer (`roles/storage.objectViewer`) to external identities that meet certain criteria, run the following command. 

### By subject
         
         gcloud storage buckets add-iam-policy-binding BUCKET_ID \
             --role=roles/storage.objectViewer \
             --member="principal://iam.googleapis.com/projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/POOL_ID/subject/SUBJECT"

### By group
         
         gcloud storage buckets add-iam-policy-binding BUCKET_ID \
             --role=roles/storage.objectViewer \
             --member="principalSet://iam.googleapis.com/projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/POOL_ID/group/GROUP"

### By attribute
         
         gcloud storage buckets add-iam-policy-binding BUCKET_ID \
             --role=roles/storage.objectViewer \
             --member="principalSet://iam.googleapis.com/projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/POOL_ID/attribute.ATTRIBUTE_NAME/ATTRIBUTE_VALUE"

Replace the following:

     * `BUCKET_ID`: the bucket on which to grant access
     * `PROJECT_NUMBER`: the [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects). of the project that contains the workload identity pool
     * `POOL_ID`: the pool ID of the workload identity pool
     * `SUBJECT`: the expected value for the attribute that [you've mapped](https://docs.cloud.google.com/iam/docs/workload-identity-federation#mapping) to `google.subject`
     * `GROUP`: the expected value for the attribute that [you've mapped](https://docs.cloud.google.com/iam/docs/workload-identity-federation#mapping) to `google.groups`
     * `ATTRIBUTE_NAME`: the name of a custom attribute in [your attribute mapping](https://docs.cloud.google.com/iam/docs/workload-identity-federation#mapping)
     * `ATTRIBUTE_VALUE`: the value of the custom attribute in [your attribute mapping](https://docs.cloud.google.com/iam/docs/workload-identity-federation#mapping)

You can grant roles on any Google Cloud resource that supports IAM allow policies.

**Note:** You must use the project number, not the project ID, in the member identifier.



### Service account impersonation

  1. To create a service account for the external workload, do the following:

     1. Enable the IAM, Security Token Service, and Service Account Credentials APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=iam.googleapis.com,sts.googleapis.com,iamcredentials.googleapis.com&redirect=https%3A//console.cloud.google.com)

     2. [Create a service account](https://docs.cloud.google.com/iam/docs/creating-managing-service-accounts#creating) that represents the workload. We recommend that you [use a dedicated service account for each workload](https://docs.cloud.google.com/iam/docs/best-practices-for-using-workload-identity-federation#use-dedicated-service-accounts). The service account doesn't need to be in the same project as the workload identity pool, but you must refer to the project that contains the service account.

     3. [Grant the service account access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access) to resources that you want external identities to access.

  2. To let the federated identity impersonate the service account, do the following:




### Console

To use the Google Cloud console to grant IAM roles to a federated identity with service account, do the following:

### Service Account in the same project

  1. To grant access using service account impersonation for a service account in the same project, do the following:

     1. Go to the **Workload Identity Pools** page.

[Go to Workload Identity Pools](https://console.cloud.google.com/iam-admin/workload-identity-pools)

     2. Select **Grant access**.

     3. In the **Grant access to service account** dialog, select **Grant access using Service Account impersonation**.

     4. In the **Service accounts** list, select the service account for the external identities to impersonate, and do the following:

     5. To choose which identities in the pool can impersonate the service account, perform one of the following actions:

        * To allow only specific identities of the workload identity pool to impersonate the service account, select **Only identities matching the filter**.

        * In the **Attribute name** list, select the attribute that you want to filter on.

        * In the **Attribute value** field, enter the expected value of the attribute; for example, if you use an attribute mapping `google.subject=assertion.sub`, set **Attribute** name to `subject` and **Attribute value** to the value of the `sub` claim in tokens that are issued by your external identity provider.

     6. To save the configuration, click **Save** and then **Dismiss**.




### Service account in a different project

**Note:** Service accounts from different projects won't appear in the "CONNECTED SERVICE ACCOUNTS" section of your **Workload Identity Pool**.

  1. To grant access using service account impersonation for a service account in a different project, do the following:

     1. Go to the **Service Accounts** page.

[Go to Service Accounts](https://console.cloud.google.com/iam-admin/serviceaccounts)

     2. Select the service account that you want to impersonate.

     3. Click **Manage access**.

     4. Click **Add principal**.

     5. In the **New principal** field, enter one of the following [principal identifiers](https://docs.cloud.google.com/iam/docs/workload-identity-federation#principal-types) for the identities in your pool that will impersonate the service account.

###  By subject 
            
            principal://iam.googleapis.com/projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/POOL_ID/subject/SUBJECT
            

Replace the following:

        * `PROJECT_NUMBER`: the project number
        * `POOL_ID`: the workload pool ID
        * `SUBJECT`: the individual subject mapped from your IdP—for example, `administrator@example.com`

###  By group 
    
    principalSet://iam.googleapis.com/projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/POOL_ID/group/GROUP
    

Replace the following:

        * `PROJECT_NUMBER`: the project number
        * `WORKLOAD_POOL_ID`: the workload pool ID
        * `GROUP`: the group mapped from your IdP—for example: `administrator-group@example.com`

###  By attribute 
    
    principalSet://iam.googleapis.com/projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/POOL_ID/attribute.ATTRIBUTE_NAME/ATTRIBUTE_VALUE
    

Replace the following:

        * `PROJECT_NUMBER`: the project number
        * `WORKLOAD_POOL_ID`: the workload pool ID
        * `ATTRIBUTE_NAME`: one of the attributes that was mapped from your IdP
        * `ATTRIBUTE_VALUE`: the value of the attribute

### By pool
    
    principalSet://iam.googleapis.com/projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/POOL_ID/*
    

Replace the following:

        * `PROJECT_NUMBER`: the project number
        * `WORKLOAD_POOL_ID`: the workload pool ID

     6. In **Select a role** , select the Workload Identity User role (`roles/iam.workloadIdentityUser`).

     7. To save the configuration, click **Save**.




### gcloud

To grant the Workload Identity User role (`roles/iam.workloadIdentityUser`) to a federated principal or principal set, run the following command. To learn more about Workload Identity Federation principal identifiers, see [Principal types](https://docs.cloud.google.com/iam/docs/workload-identity-federation#principal-types). 

### By subject
    
    
    gcloud iam service-accounts add-iam-policy-binding SERVICE_ACCOUNT_EMAIL \
        --role=roles/iam.workloadIdentityUser \
        --member="principal://iam.googleapis.com/projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/POOL_ID/subject/SUBJECT"

### By group
    
    
    gcloud iam service-accounts add-iam-policy-binding SERVICE_ACCOUNT_EMAIL \
        --role=roles/iam.workloadIdentityUser \
        --member="principalSet://iam.googleapis.com/projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/POOL_ID/group/GROUP"

### By attribute
    
    
    gcloud iam service-accounts add-iam-policy-binding SERVICE_ACCOUNT_EMAIL \
        --role=roles/iam.workloadIdentityUser \
        --member="principalSet://iam.googleapis.com/projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/POOL_ID/attribute.ATTRIBUTE_NAME/ATTRIBUTE_VALUE"

Replace the following:

  * `SERVICE_ACCOUNT_EMAIL`: the email address of the service account
  * `PROJECT_NUMBER`: the [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects). of the project that contains the workload identity pool
  * `POOL_ID`: the pool ID of the workload identity pool
  * `SUBJECT`: the expected value for the attribute that [you've mapped](https://docs.cloud.google.com/iam/docs/workload-identity-federation#mapping) to `google.subject`
  * `GROUP`: the expected value for the attribute that [you've mapped](https://docs.cloud.google.com/iam/docs/workload-identity-federation#mapping) to `google.groups`
  * `ATTRIBUTE_NAME`: the name of a custom attribute in [your attribute mapping](https://docs.cloud.google.com/iam/docs/workload-identity-federation#mapping)
  * `ATTRIBUTE_VALUE`: the value of the custom attribute in [your attribute mapping](https://docs.cloud.google.com/iam/docs/workload-identity-federation#mapping)

**Note:** You must use the project number, not the project ID, in the member identifier.

## Download the configuration

To let your workload access client libraries, you must first download and configure [application default credentials (ADC)](https://docs.cloud.google.com/docs/authentication/provide-credentials-adc) by doing the following: 

  1. In the Google Cloud console, go to the **Workload Identity Pools** page.

[Go to Workload Identity Pools](https://console.cloud.google.com/iam-admin/workload-identity-pools)
  2. In the table, select your pool to go the pool's detail page.

  3. Click **Grant access**.

  4. Select **Grant access using federated identities (Recommended)**. 

  5. To download the Application Default Credential (ADC) so that your workload can access client libraries, do the following: 

     1. Click **Download config**.

     2. In the **Configure your application** dialog, do the following:

        1. In the **Provider** drop-down list, select your provider. 

        2. In **OIDC token path** or **SAML assertion path** , enter the path where the token or assertion is located. 

In the **Format type** drop-down list, select the format. 

     3. Click **Download configuration** , and note the path where you saved the file. 




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
