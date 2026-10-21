---
url: https://docs.cloud.google.com/docs/authentication/set-up-adc-attached-service-account/
title: Set up ADC for a resource with an attached service account \u00a0|\u00a0 Authentication \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:05:48.091307+00:00
---

# Set up ADC for a resource with an attached service account  |  Authentication  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/docs/authentication/set-up-adc-attached-service-account/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Authentication ](https://docs.cloud.google.com/docs/authentication)
  * [ Guides ](https://docs.cloud.google.com/sdk/docs/overview)



Send feedback 

#  Set up ADC for a resource with an attached service account Stay organized with collections  Save and categorize content based on your preferences. 

Some Google Cloud services—such as Compute Engine, App Engine, and Cloud Run functions—support attaching a [user-managed service account](https://docs.cloud.google.com/iam/docs/service-account-types#user-created) to some types of resources. Generally, attaching a service account is supported when that service's resources can run or include application code. When you attach a service account to a resource, the code running on the resource can use that service account as its identity. 

Attaching a user-managed service account is the preferred way to provide credentials to ADC for production code running on Google Cloud.

**Note:** Many of these Google Cloud services also provide a default service account. Using the default service account is not recommended, because by default the default service account is highly privileged, which violates the [principle of least privilege](https://docs.cloud.google.com/iam/docs/using-iam-securely#least_privilege).

For help determining the roles that you need to provide to your service account, see [Choose predefined roles](https://docs.cloud.google.com/iam/docs/choose-predefined-roles).

For information about which resources you can attach a service account to, and help with attaching the service account to the resource, see the [IAM documentation on attaching a service account](https://docs.cloud.google.com/iam/docs/attach-service-accounts#attaching-new-resource).

Set up authentication:

  1. Ensure that you have the Create Service Accounts IAM role (`roles/iam.serviceAccountCreator`) and the Project IAM Admin role (`roles/resourcemanager.projectIamAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
  2. Create the service account: 
         
         gcloud iam service-accounts create SERVICE_ACCOUNT_NAME

Replace `SERVICE_ACCOUNT_NAME` with a name for the service account. 

  3. To provide access to your project and your resources, grant a role to the service account: 
         
         gcloud projects add-iam-policy-binding PROJECT_ID --member="serviceAccount:SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com" --role=ROLE

Replace the following: 

     * `SERVICE_ACCOUNT_NAME`: the name of the service account
     * `PROJECT_ID`: the project ID where you created the service account
     * `ROLE`: the role to grant
**Note** : The `--role` flag affects which resources the service account can access in your project. You can revoke these roles or grant additional roles later. In production environments, do not grant the Owner, Editor, or Viewer roles. Instead, grant a [predefined role](https://docs.cloud.google.com/iam/docs/understanding-roles#predefined_roles) or [custom role](https://docs.cloud.google.com/iam/docs/understanding-custom-roles) that meets your needs. 
  4. To grant another role to the service account, run the command as you did in the previous step. 
  5. Grant the required role to the principal that will attach the service account to other resources. 
         
         gcloud iam service-accounts add-iam-policy-binding SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com --member="user:USER_EMAIL" --role=roles/iam.serviceAccountUser

Replace the following: 

     * `SERVICE_ACCOUNT_NAME`: the name of the service account
     * `PROJECT_ID`: the project ID where you created the service account
     * `USER_EMAIL`: the email address for a Google Account



## What's next

  * Understand best practices for using [service accounts](https://docs.cloud.google.com/iam/docs/best-practices-service-accounts) and [service account keys](https://docs.cloud.google.com/iam/docs/best-practices-for-managing-service-account-keys).
  * Learn more about [how ADC finds credentials](https://docs.cloud.google.com/docs/authentication/application-default-credentials).
  * [Authenticate for using Cloud Client Libraries](https://docs.cloud.google.com/docs/authentication/client-libraries).
  * Explore [authentication methods](https://docs.cloud.google.com/docs/authentication).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
