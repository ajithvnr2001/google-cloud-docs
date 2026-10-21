---
url: https://docs.cloud.google.com/run/docs/configuring/services/service-identity/
title: Configure service identity for services \u00a0|\u00a0 Cloud Run \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T00:15:53.134572+00:00
---

# Configure service identity for services  |  Cloud Run  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/run/docs/configuring/services/service-identity/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run)



Send feedback 

#  Configure service identity for services Stay organized with collections  Save and categorize content based on your preferences. 

A Cloud Run service or revision has a service identity that is used as the authenticated account for accessing Google Cloud APIs from your Cloud Run instance container. To learn more about service identity, see the [Introduction to service identity](https://docs.cloud.google.com/run/docs/securing/service-identity) guide.

## How service identity is used

In Cloud Run, the service identity is a service account that is [both a resource and a principal](https://docs.cloud.google.com/iam/docs/service-account-overview#service-account-permissions).

  * **Service identity as a resource** : To attach a service account as the service identity, the [deployer account](https://docs.cloud.google.com/run/docs/securing/service-identity#cloud-run-deployer-account) must have access on the service identity resource. Certain operations, like creating or updating a service or revision, require the deployer account to have permissions on the service identity resource.
  * **Service identity as a principal** : To access Google Cloud APIs from a Cloud Run service or revision, you must grant the service identity the required roles or permissions for the operations you want your service or revision to perform.



The next section covers the required roles for granting the deployer account access on the service identity resource and granting the roles or permissions that the service account principal needs.

## Required roles

You or your administrator must grant IAM roles and permissions for the deployer account and the service identity.

#### Click to view required roles for the deployer account

To get the permissions that you need to attach a service account as the service identity on the service or revision, you or your administrator must grant your deployer account the [Service Account User](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) role (`roles/iam.serviceAccountUser`) on the service account that is used as the service identity.

This predefined role contains the `iam.serviceAccounts.actAs` permission, which is required to attach a service account on the service or revision. You might also be able to get this permission by configuring [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or using other [predefined roles](https://docs.cloud.google.com/iam/docs/understanding-roles). 

For instructions on how to grant the deployer account this role on the service identity, see [deployment permissions](https://docs.cloud.google.com/run/docs/reference/iam/roles#additional-configuration). If the service account is in a different project from the Cloud Run service or revision, you or your administrator must also configure an IAM role for the Cloud Run service agent and set up an org policy. See use service accounts in other projects for more details. 

**Note:** Depending on the Cloud Run operation you need, refer to Cloud Run pages for the other roles that are needed for the deployer account. 

#### Click to view required roles for the service identity

To allow the service identity to access Google Cloud APIs from Cloud Run, you or your administrator must grant the service identity the [permissions or roles](https://docs.cloud.google.com/iam/docs/overview#permissions) that are required by operations you want to perform. To accessing specific Cloud Client Libraries, refer to the Google Cloud documentation for the Google Cloud service.

If a Cloud Run service or revision does not access other Google Cloud services, you don't need to grant the service identity any roles or permissions, and you can use the default service account that was assigned to the project.

### Get recommendations to create dedicated service accounts

When you create a new service account from the Google Cloud console, the optional step "Grant this service account access to the project" is for any additional access required. For example, one Cloud Run service might invoke another [private Cloud Run service](https://docs.cloud.google.com/run/docs/authenticating/service-to-service), or it might [access a Cloud SQL database](https://docs.cloud.google.com/sql/docs/mysql/connect-run), both which require specific IAM roles. Refer to the documentation on [managing access](https://docs.cloud.google.com/iam/help/service-accounts/granting-access-to-service-accounts) for more information.

The [Recommender service](https://docs.cloud.google.com/run/docs/recommender) also automatically supplies recommendations to create a dedicated service accounts with the minimal required set of permissions.

## Configure service identity

If you haven't already created a service account, you can either create a user-managed service account in [IAM](https://docs.cloud.google.com/iam/docs/service-accounts-create), or in Cloud Run.

To configure service identity, use either the Google Cloud console, the gcloud CLI, the API (YAML) when you [create a new service](https://docs.cloud.google.com/run/docs/deploying#service) or [deploy a new revision](https://docs.cloud.google.com/run/docs/deploying#revision), or Terraform:

### Console

  1. In the Google Cloud console, go to Cloud Run:

[Go to Cloud Run](https://console.cloud.google.com/run)

  2. Select **Services** from the Cloud Run navigation menu:

     1. If you are configuring a new service, click **Deploy container** and fill out the initial service settings page. Then click **Containers, Networking, Security** to expand the service configuration page.

     2. If you are configuring an existing service, click the service.

  3. Click the **Security** tab.

  4. Click the **Service account** drop-down and select an existing service account, or click **Create a new service account** , if applicable.

  5. Click **Create** for a new service. Click **View diff & redeploy**, then **Deploy changes** for an existing service.




###  gcloud 

You can [update an existing service](https://docs.cloud.google.com/sdk/gcloud/reference/run/services/update) to have a new service account by using the following command:
    
    
    gcloud run services update SERVICE --service-account SERVICE_ACCOUNT

Replace the following:

  * SERVICE: the name of your service.
  * SERVICE_ACCOUNT: the service account associated with the new identity: this value is the email address for the service account—for example, `example@myproject.iam.gserviceaccount.com`.



You can also set a service account during [deployment](https://docs.cloud.google.com/sdk/gcloud/reference/run/deploy) using the command:
    
    
    gcloud run deploy --image IMAGE_URL --service-account SERVICE_ACCOUNT

Replace the following:

  * `IMAGE_URL`: a reference to the container image, for example, `us-docker.pkg.dev/cloudrun/container/hello:latest`. If you use Artifact Registry, the [repository](https://docs.cloud.google.com/artifact-registry/docs/repositories/create-repos#docker) REPO_NAME must already be created. The URL follows the format of `LOCATION-docker.pkg.dev/PROJECT_ID/REPO_NAME/PATH:TAG` .
  * SERVICE_ACCOUNT: the service account associated with the new identity: this value is the email address for the service account—for example, `example@myservice.iam.gserviceaccount.com`.



### YAML

  1. If you are creating a new service, skip this step. If you are updating an existing service, download its [YAML configuration](https://docs.cloud.google.com/run/docs/reference/yaml/v1):
         
         gcloud run services describe SERVICE --format export > service.yaml

  2. Update the `serviceAccountName:` attribute:
         
         apiVersion: serving.knative.dev/v1
         kind: Service
         metadata:
           name: SERVICE
         spec:
           template:
             spec:
               serviceAccountName: SERVICE_ACCOUNT

Replace the following:

     * SERVICE: the name of your Cloud Run service.
     * SERVICE_ACCOUNT: the service account associated with the new identity. This value is the email address for the service account—for example, `SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com`.
  3. Create or update the service using the following command:
         
         gcloud run services replace service.yaml

The `gcloud run services replace` command defaults to using `service.yaml` file if present.




### Terraform

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

Add the following to a [`google_cloud_run_v2_service`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/cloud_run_v2_service) resource in your Terraform configuration:  


To create a service account, add the following resource to your to your existing `main.tf` file:
    
    
    resource "google_service_account" "cloudrun_service_identity" {
      account_id = "my-service-account"
    }

Create or update a Cloud Run service and include your service account:
    
    
    resource "google_cloud_run_v2_service" "default" {
      name     = "id-service"
      location = "us-central1"
    
      deletion_protection = false # set to "true" in production
    
      template {
        containers {
          image = "us-docker.pkg.dev/cloudrun/container/hello"
        }
        service_account = google_service_account.cloudrun_service_identity.email
      }
    }

### Use service accounts in other projects

If you configure a service account from a different Google Cloud project than the Cloud Run resource, do the following:

  1. You or your administrator must grant the Service Account User role (`roles/iam.serviceAccountUser`) on the service account that you use as the service identity.

### Console

     1. Go to the **Service accounts** page of the Google Cloud console: 

[Go to Service accounts](https://console.cloud.google.com/iam-admin/serviceaccounts)

     2. Select the service account email address you are using as the service identity.

     3. Click the **Principals with access** tab.

     4. Click the person_add **Grant access** button.

     5. Enter the deployer account email address that matches the principal you're granting the Admin or Developer role to.

     6. In the **Select a role** drop-down, select the **Service Accounts** > **Service Account User** role.

     7. Click **Save**.

###  gcloud 

Use the `gcloud iam service-accounts add-iam-policy-binding` command, replacing the highlighted variables with the appropriate values:
    
    gcloud iam service-accounts add-iam-policy-binding \
        SERVICE_ACCOUNT_NAME@SERVICE_ACCOUNT_PROJECT_ID.iam.gserviceaccount.com \
        --member="PRINCIPAL" \
        --role="roles/iam.serviceAccountUser"

Replace the following:

     * `SERVICE_ACCOUNT_NAME`: the name of the service account that you are attaching the Cloud Run resource to.
     * `SERVICE_ACCOUNT_PROJECT_ID`: the project ID where the service account is located.
     * PRINCIPAL: the deployer account you are adding the binding for, using the format `user|group|serviceAccount:email` or `domain:domain`—for example:

       * `user:test-user@gmail.com`
       * `group:admins@example.com`
       * `serviceAccount:test123@example.domain.com`
       * `domain:example.domain.com`

  2. You or your administrator must grant the Cloud Run resource's service agent the Service Account Token Creator role (`roles/iam.serviceAccountTokenCreator`) on the service account you use as the service identity. The service agent follows the format of `service-PROJECT_NUMBER@serverless-robot-prod.iam.gserviceaccount.com`.

### Console

     1. Go to the **Service accounts** page of the Google Cloud console: 

[Go to Service accounts](https://console.cloud.google.com/iam-admin/serviceaccounts)

     2. Select the service account email address you are using as the service identity.

     3. Click the **Permissions** tab.

     4. Click the person_add **Grant access** button.

     5. Enter the service agent email address. For example: `service-PROJECT_NUMBER@serverless-robot-prod.iam.gserviceaccount.com`.

     6. In the **Select a role** drop-down, select the **Service Accounts** > **Service Account Token Creator** role.

     7. Click **Save**.

###  gcloud 

Use the `gcloud iam service-accounts add-iam-policy-binding` command:
    
    gcloud iam service-accounts add-iam-policy-binding \
        SERVICE_ACCOUNT_NAME@SERVICE_ACCOUNT_PROJECT_ID.iam.gserviceaccount.com \
        --member="serviceAccount:service-CLOUD_RUN_RESOURCE_PROJECT_NUMBER@serverless-robot-prod.iam.gserviceaccount.com" \
        --role="roles/iam.serviceAccountTokenCreator"

Replace the following:

     * `SERVICE_ACCOUNT_NAME`: the name of the service account that you are attaching the Cloud Run resource to.
     * `SERVICE_ACCOUNT_PROJECT_ID`: the project ID where the service account is located.
     * `CLOUD_RUN_RESOURCE_PROJECT_NUMBER`: the project number where the Cloud Run is located.

The command prints the updated allow policy for the user-managed service account.

  3. The project containing this service account requires the org-policy `iam.disableCrossProjectServiceAccountUsage` to be set to false or unenforced at the folder level or inherited from project-level settings. By default, this is set to `true`.

### Console

     1. Go to the **Organization policies** page in the Google Cloud console: 

[Go to Organization policies](https://console.cloud.google.com/iam-admin/orgpolicies)

     2. From the project picker, select the organization and project for which you want to disable cross-project service account usage for.

     3. Select the **disable cross-project service account usage** policy.

     4. Click **Manage policy**.

     5. Under **Policy source** , select **Override parent's policy**.

     6. Click **Add a rule**.

     7. Under **Enforcement** , select **Off**.

     8. To enforce the policy, click **Set policy**.

###  gcloud 

In the project that has the service account, ensure that the `iam.disableCrossProjectServiceAccountUsage` organization policy constraint is not enforced. This constraint is enforced by default.

To disable this organization policy constraint, run:
    
    gcloud resource-manager org-policies disable-enforce iam.disableCrossProjectServiceAccountUsage
        --project=SERVICE_ACCOUNT_PROJECT_ID

Replace SERVICE_ACCOUNT_PROJECT_ID with the project ID that contains the service account.




You can apply role memberships directly to the service account resource or inherit from higher levels in the [resource hierarchy](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy).

## What's next

  * For more information about service accounts, see the [IAM service account](https://docs.cloud.google.com/iam/docs/service-account-overview) and [user-managed service account](https://docs.cloud.google.com/iam/docs/service-accounts-create) guides.
  * If your Cloud Run service, job, worker pool, or instance accesses Google APIs or Google Cloud services, you must configure your service account as the service identity. [Learn more](https://docs.cloud.google.com/run/docs/securing/service-identity).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
