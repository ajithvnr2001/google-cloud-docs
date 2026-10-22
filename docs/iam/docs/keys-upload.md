---
url: https://docs.cloud.google.com/iam/docs/keys-upload/
title: Upload service account keys \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:52:04.640190+00:00
---

# Upload service account keys  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/keys-upload/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Guides ](https://docs.cloud.google.com/iam/docs/overview)



Send feedback 

#  Upload service account keys Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to upload a public key for a service account. After you upload the public key, you can use the private key from the key pair to authenticate as the service account.

**Note:** If you need to access resources from a workload that runs outside of Google Cloud, such as on Amazon Web Services (AWS) or Microsoft Azure, consider using [Workload Identity Federation](https://docs.cloud.google.com/iam/docs/workload-identity-federation) instead of service account keys. Federation lets your workloads access resources directly, using a short-lived access token, and eliminates the maintenance and security burden associated with service account keys. 

## Before you begin

  * Enable the IAM API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=iam.googleapis.com&redirect=https%3A//console.cloud.google.com)

  * Understand [service account credentials](https://docs.cloud.google.com/iam/docs/service-account-creds).




### Required roles

To get the permissions that you need to upload service account keys, ask your administrator to grant you the [Service Account Key Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountKeyAdmin) (`roles/iam.serviceAccountKeyAdmin`) IAM role on the project, or the service account whose keys you want to manage. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

**Note:** [IAM basic roles](https://docs.cloud.google.com/iam/docs/roles-overview#basic) might also contain permissions to upload service account keys. You shouldn't grant basic roles in a production environment, but you can grant them in a development or test environment. 

Depending on your organization policy configuration, you might also need to allow service account keys to be uploaded in your project before uploading a key.

To get the permissions that you need to allow service account keys to be uploaded in a project, ask your administrator to grant you the following IAM roles on your organization: 

  * [Organization Policy Administrator ](https://docs.cloud.google.com/iam/docs/roles-permissions/orgpolicy#orgpolicy.policyAdmin) (`roles/orgpolicy.policyAdmin`)
  * [Organization Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.organizationViewer) (`roles/resourcemanager.organizationViewer`)
  * [Tag Administrator ](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagAdmin) (`roles/resourcemanager.tagAdmin`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to allow service account keys to be uploaded in a project. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to allow service account keys to be uploaded in a project:

  * `orgpolicy.constraints.list`
  * `orgpolicy.customConstraints.create`
  * `orgpolicy.customConstraints.delete`
  * `orgpolicy.customConstraints.get`
  * `orgpolicy.customConstraints.list`
  * `orgpolicy.customConstraints.update`
  * `orgpolicy.policies.create`
  * `orgpolicy.policies.delete`
  * `orgpolicy.policies.list`
  * `orgpolicy.policies.update`
  * `orgpolicy.policy.get`
  * `orgpolicy.policy.set`
  * `resourcemanager.organizations.get`
  * `resourcemanager.projects.listTagBindings`
  * `resourcemanager.projects.listEffectiveTags`
  * `resourcemanager.tagKeys.get`
  * `resourcemanager.tagKeys.list`
  * `resourcemanager.tagValues.list`
  * `resourcemanager.tagValues.get`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

**Note:** [IAM basic roles](https://docs.cloud.google.com/iam/docs/roles-overview#basic) might also contain permissions to allow service account keys to be uploaded in a project. You shouldn't grant basic roles in a production environment, but you can grant them in a development or test environment. 

## Allow service account key upload

Before you create a service account key, make sure that the `iam.disableServiceAccountKeyUpload` organization policy constraint isn't enforced for your project. If this constraint is enforced for your project, you can't upload service account keys in that project.

**Note** : If your organization was created on or after May 3, 2024, this constraint is enforced by default. 

We recommend enforcing this constraint for most projects and only exempting projects that truly require service account keys. For more information about alternative authentication methods, see [Choose the right authentication method for your use case](https://docs.cloud.google.com/docs/authentication#auth-decision-tree).

To exempt a project from the `iam.disableServiceAccountKeyUpload` organization policy constraint, ask an organization policy administrator to do the following:

  1. At the organization level, create a tag key and tag value that you will use to define whether a resource should be exempt from the organization policy. We recommend creating a tag with the key `disableServiceAccountKeyUpload` and the values `enforced` and `not_enforced`. 

To learn how to create tag keys and tag values, see [Creating and defining a new tag](https://docs.cloud.google.com/resource-manager/docs/tags/tags-creating-and-managing#creating). 

  2. Attach the `disableServiceAccountKeyUpload` tag to the organization and set its value to `enforced`. All resources in the organization inherit this tag value, unless it's overwritten with a different tag value. 

To learn how to attach tags to resources, see [Attaching tags to resources](https://docs.cloud.google.com/resource-manager/docs/tags/tags-creating-and-managing#attaching). 

  3. For each project or folder that you want to exempt from the organization policy, attach the `disableServiceAccountKeyUpload` tag and set its value to `not_enforced`. Setting a tag value for a project or folder in this way overrides the tag value inherited from the organization. 
  4. [Create or update the organization policy](https://docs.cloud.google.com/resource-manager/docs/organization-policy/creating-managing-policies) that prevents uploading service account keys so that it doesn't enforce the constraint for exempt resources. This policy should have the following rules: 

     * Configure the `iam.disableServiceAccountKeyUpload` constraint to not be enforced on any resources with the `disableServiceAccountKeyUpload: not_enforced` tag. The condition in this rule should look like the following: 
           
           "resource.matchTag('ORGANIZATION_ID/disableServiceAccountKeyUpload', 'not_enforced')"
           

     * Configure the `iam.disableServiceAccountKeyUpload` constraint to be enforced on all other resources. 



## Upload a public key for a service account

You can upload the public key portion of a [user-managed key pair](https://docs.cloud.google.com/iam/docs/service-account-creds#user-managed) to associate it with a service account. After you upload the public key, you can use the private key from the key pair as a service account key.

The key you upload must be an RSA public key that is wrapped in an [X.509 v3 certificate](https://tools.ietf.org/html/rfc5280) and encoded in base64. You can use tools such as [OpenSSL](https://www.openssl.org/) to generate a key and certificate in this format.

**Do not include any private information in the X.509 certificate.** Specifically, use a generic subject, and do not add any optional attributes. Certificates are publicly visible; any private information in the certificate is visible to anyone who retrieves the certificate. For more information, see [Avoid disclosing confidential information in uploaded X.509 certificates](https://docs.cloud.google.com/iam/docs/best-practices-for-managing-service-account-keys#confidential-information).

If the [`iam.serviceAccountKeyExpiryHours`](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-service-accounts#limit_key_expiry) organization policy constraint is enforced for your project, then the key that you upload needs to expire within the time period specified in the constraint. To set the expiry time of the key, use the `-days` value in the command that you use to generate the X.509 certificate. If the `-days` value is greater than the time period specified in the constraint, then the command will fail.

For example, the following command generates a 2048-bit RSA key pair and wraps the public key in a self-signed certificate that is valid for 365 days:
    
    
    openssl req -x509 -nodes -newkey rsa:2048 -days 365 \
        -keyout /path/to/private_key.pem \
        -out /path/to/public_key.pem \
        -subj "/CN=unused"
    

You can then upload the `public_key.pem` file as the public key for a service account.

### Console

  1. In the Google Cloud console, go to the **Service accounts** page. 

[Go to Service accounts](https://console.cloud.google.com/iam-admin/serviceaccounts?walkthrough_id=iam--upload-service-account-keys&start_index=1#step_index=1)

The remaining steps appear in the Google Cloud console.

  2. Select a project.
  3. On the **Service accounts** page, click the email address of the service account that you want to upload a key for.
  4. Click the **Keys** tab.
  5. Click the **Add key** drop-down menu, then select **Upload existing key**.
  6. Click **Browse** , then find and select your public key file. Alternatively, you can copy and paste the contents of your public key file into the **Paste existing key** box.
  7. Click **Upload**.



### gcloud

Execute the [`gcloud iam service-accounts keys upload`](https://docs.cloud.google.com/sdk/gcloud/reference/iam/service-accounts/keys/upload) command to upload a public key for signing service account keys.

Replace the following values:

  * `KEY_FILE`: The path to the file containing the key data to upload—for example, `./public_key.pem`.
  * `SA_NAME`: The name of the service account to upload a key for.
  * `PROJECT_ID`: Your Google Cloud project ID.


    
    
    gcloud iam service-accounts keys upload KEY_FILE \
        --iam-account=SA_NAME@PROJECT_ID.iam.gserviceaccount.com
    

The output contains a unique identifier for the uploaded key:
    
    
    Name: projects/PROJECT_ID/serviceAccounts/SA_NAME@PROJECT_ID.iam.gserviceaccount.com/keys/c7b74879da78e4cdcbe7e1bf5e129375c0bfa8d0
    

To determine whether the command was successful, execute the [`gcloud iam service-accounts keys list`](https://docs.cloud.google.com/sdk/gcloud/reference/iam/service-accounts/keys/list) command:
    
    
    gcloud iam service-accounts keys list \
        --iam-account=SA_NAME@PROJECT_ID.iam.gserviceaccount.com
    

The output will contain the same unique identifier that was returned after the key was created:

KEY_ID | CREATED_AT | EXPIRES_AT | DISABLED  
---|---|---|---  
c7b74879da78e4cdcbe7e1bf5e129375c0bfa8d0 | 2019-06-26T21:01:42Z | 9999-12-31T23:59:59Z |   
  
### REST

The `[projects.serviceAccounts.keys.upload](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.serviceAccounts.keys/upload)` method uploads the public key from a user-managed key pair, and adds this key to the service account. 

Before using any of the request data, make the following replacements: 

  * `PROJECT_ID`: Your Google Cloud project ID. Project IDs are alphanumeric strings, like `my-project`.
  * `SA_NAME`: The name of the service account to associate the key with.
  * `PUBLIC_KEY_DATA`: The public key data for the key pair. Must be an RSA public key that is wrapped in an X.509 v3 certificate. Encode the public key data in base64, including the first line, `-----BEGIN CERTIFICATE-----`, and the last line, `-----END CERTIFICATE-----`. 



HTTP method and URL: 
    
    
    POST https://iam.googleapis.com/v1/projects/PROJECT_ID/serviceAccounts/SA_NAME@PROJECT_ID.iam.gserviceaccount.com/keys:upload

Request JSON body: 
    
    
    {
      "publicKeyData": "PUBLIC_KEY_DATA"
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://iam.googleapis.com/v1/projects/PROJECT_ID/serviceAccounts/SA_NAME@PROJECT_ID.iam.gserviceaccount.com/keys:upload"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://iam.googleapis.com/v1/projects/PROJECT_ID/serviceAccounts/SA_NAME@PROJECT_ID.iam.gserviceaccount.com/keys:upload" | Select-Object -Expand Content

#### APIs Explorer (browser)

Copy the request body and open the [method reference page](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.serviceAccounts.keys/upload). The APIs Explorer panel opens on the right side of the page. You can interact with this tool to send requests. Paste the request body in this tool, complete any other required fields, and click **Execute**. 

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/my-project/serviceAccounts/my-service-account@my-project.iam.gserviceaccount.com/keys/c7b74879da78e4cdcbe7e1bf5e129375c0bfa8d0",
      "validAfterTime": "2020-05-17T19:31:19Z",
      "validBeforeTime": "2021-05-17T19:31:19Z",
      "keyAlgorithm": "KEY_ALG_RSA_2048",
      "keyOrigin": "USER_PROVIDED",
      "keyType": "USER_MANAGED"
    }
    

## Disable public key uploads

To disable the ability to upload keys for your project, see [Restricting service account key upload](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-service-accounts#disable_service_account_key_upload).

**Note** : If your organization was created on or after May 3, 2024, this constraint is enforced by default. 

## What's next

  * Learn how to [create and delete service account keys](https://docs.cloud.google.com/iam/docs/keys-create-delete).
  * Learn how to [list and get service account keys](https://docs.cloud.google.com/iam/docs/keys-list-get).
  * Learn about [alternatives to service account keys for authentication](https://docs.cloud.google.com/docs/authentication#auth-decision-tree).
  * Learn how to use service account keys to [authenticate as a service account](https://docs.cloud.google.com/docs/authentication/set-up-adc-on-premises#wlif-key).
  * Understand the [best practices for managing service account keys](https://docs.cloud.google.com/iam/docs/best-practices-for-managing-service-account-keys).



##  Try it for yourself 

If you're new to Google Cloud, create an account to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 

[ Get started for free ](https://console.cloud.google.com/freetrial)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
