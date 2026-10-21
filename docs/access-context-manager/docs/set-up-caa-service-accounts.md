---
url: https://docs.cloud.google.com/access-context-manager/docs/set-up-caa-service-accounts/
title: Configure Context-Aware Access for service accounts \u00a0|\u00a0 Access Context Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:39:18.479892+00:00
---

# Configure Context-Aware Access for service accounts  |  Access Context Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/access-context-manager/docs/set-up-caa-service-accounts/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Access Context Manager ](https://docs.cloud.google.com/access-context-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/access-context-manager/docs/create-access-level)



Send feedback 

#  Configure Context-Aware Access for service accounts Stay organized with collections  Save and categorize content based on your preferences. 

This guide describes how you can set up Context-Aware Access to help secure service account access to Google Cloud APIs, based on access levels that you define.

## Limitations

The following limitations apply to Context-Aware Access policies for service accounts:

  * Network-based or IP address-based attributes cannot be used for service account bindings if the service account will be used for workflow executions and Cloud Scheduler.

  * Connections to private GKE clusters, using `kubectl`, and to Cloud SQL, using Auth Proxy, cannot be blocked by Context-Aware Access policies.

  * If an access level that is bound to a service account contains unsupported attributes, such as `Device` attributes, then API access is denied.

  * Scoped access levels aren't supported for service accounts.




If you use Cloud Build and Cloud Run, we recommend that you use the following built-in VPC features:

  * For Cloud Run, use [Serverless VPC Access](https://docs.cloud.google.com/vpc/docs/serverless-vpc-access).

  * For Cloud Build, use [private pools](https://docs.cloud.google.com/build/docs/private-pools/private-pools-overview).


**Important:** You can use Context-Aware Access to restrict Google Cloud API access by service accounts to specific VPC networks. If you do, then you must configure all workloads that use those service accounts to use the same VPC networks. For example, a Cloud Run service that uses the service account must be [configured to run within the VPC network](https://docs.cloud.google.com/run/docs/configuring/vpc-direct-vpc).

## Before you begin

  1. Make sure that you have a [Google Cloud organization](https://docs.cloud.google.com/resource-manager/docs/creating-managing-organization) and at least one [Google Cloud project](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects). 

  2. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  3. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  4. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  5. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  6. [Create or select a Google Cloud project](https://cloud.google.com/resource-manager/docs/creating-managing-projects).

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.
     * Create a Google Cloud project:
           
           gcloud projects create PROJECT_ID

Replace `PROJECT_ID` with a name for the Google Cloud project you are creating.

     * Select the Google Cloud project that you created:
           
           gcloud config set project PROJECT_ID

Replace `PROJECT_ID` with your Google Cloud project name.

  7. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  8. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  9. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  10. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  11. [Create or select a Google Cloud project](https://cloud.google.com/resource-manager/docs/creating-managing-projects).

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.
     * Create a Google Cloud project:
           
           gcloud projects create PROJECT_ID

Replace `PROJECT_ID` with a name for the Google Cloud project you are creating.

     * Select the Google Cloud project that you created:
           
           gcloud config set project PROJECT_ID

Replace `PROJECT_ID` with your Google Cloud project name.

  12. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  13. Update Google Cloud CLI components: 
         
         gcloud components update --quiet

  14. [Create a service account](https://docs.cloud.google.com/iam/docs/service-accounts-create) in your project if you don't already have one. This service account is the target of the Context-Aware Access policy.



## Required roles

This section describes the Identity and Access Management (IAM) roles that are required to use Context-Aware Access.

### Project-level roles

To get the permission that you need to at the project level, ask your administrator to grant you the [Service Account Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountAdmin) (`roles/iam.serviceAccountAdmin`) IAM role on the user account or service account. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the `the required permissions` permission, which is required to at the project level. 

You might also be able to get this permission with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

### Organization-level roles

To get the permission that you need to at the organization level, ask your administrator to grant you the following IAM roles on user account or service account: 

  * [Cloud Access Binding Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/accesscontextmanager#accesscontextmanager.gcpAccessAdmin) (`roles/accesscontextmanager.gcpAccessAdmin`)
  * [Access Context Manager Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/accesscontextmanager#accesscontextmanager.policyAdmin) (`roles/accesscontextmanager.policyAdmin`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the `the required permissions` permission, which is required to at the organization level. 

You might also be able to get this permission with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Bind Context-Aware Access policies to different resource levels

You can bind Context-Aware Access policies with the same enforcement mode to resources that are at different levels of the resource hierarchy. When a resource attempts access, Context-Aware Access uses the policy that is bound to that resource before it attempts to use a policy that is bound to a higher-level resource.

For example, you can bind an enforcement-mode policy directly to a service account and a different enforcement-mode policy to the project that contains the service account. When the service account attempts to access resources, Context-Aware Access evaluates the policy that is bound to the service account. For other service accounts in the project that don't have policies bound to them, Context-Aware Access evaluates the enforcement-mode policy that is bound to the project. The same is true if the enforcement mode is set to dry run for both the project-level policy and the service account-level policy.

You can use multiple policies to incrementally and selectively deploy policies—for example, you can do the following:

  1. Bind a policy in dry-run mode at the project level and make sure that it's working as you expect by checking for access denied events in Cloud Audit Logs. 
  2. Bind the policy in enforcement mode only to specific service accounts. 
  3. Bind the policy in enforcement mode at the project level, and bind a less restrictive, enforcement-mode policy to specific service accounts as needed. 



## Access level attributes for service accounts

This section lists the access levels that are supported for service accounts.

**Important:** Only [org-level Access Context Manager access levels](https://docs.cloud.google.com/access-context-manager/docs/create-access-policy#organization-access-policy) can be bound to service accounts. Scoped access levels aren't supported for service accounts. 

The following attributes are supported for service accounts:

  * IP subnetworks, which are based on the public IP address. 
  * VPC networks, which are based on the private IP address. 
  * Geolocation, which is based on the public IP address.

When the service account makes any request to Google Cloud APIs, the request is evaluated by Context-Aware Access, and the IP address of the request is compared to the IP addresses specified in the Context-Aware Access policy. If the IP addresses match, the API call is allowed. If the IP address doesn't match, the API call is denied. 

  * A custom access level with a Common Expression Language (CEL) expression. The expression must evaluate to `true` to allow access and `false` to deny access. 

The following CEL expression is useful for restricting access by service accounts. 

The expression evaluates to `true` if the request originated from one or more specified project numbers: 
        
        expression: "originatesFromProjects(origin, [PROJECT_NUMBER, ...])"
            

`originatesFromProjects` checks whether the request comes from a network that is associated with the specified project and whether the request comes from a private IP address. 

  * Time of day, which is based on the time and date of the request in a specified time zone. 

For more information, see [Configuring time and day access conditions](https://docs.cloud.google.com/access-context-manager/docs/time-and-date-conditions). 




## Create an access level

This section describes how to create an access level within your organization. Access levels define the conditions under which access is permitted.

  1. Follow the instructions to [Create a basic access level](https://docs.cloud.google.com/access-context-manager/docs/create-basic-access-level) or [Create a custom access level](https://docs.cloud.google.com/access-context-manager/docs/create-custom-access-level).

  2. Note the full name of the access level, which has the format: `accessPolicies/POLICY_ID/accessLevels/ACCESS_LEVEL_NAME`.




## Create an access binding

Bind the access level to the selected service account. Doing so enforces the conditions defined in the access level. You can bind the access level to a single service account or all service accounts within a project.

### Bind the access level to a specific service account

This section describes how to bind the access level to a specific service account.

###  gcloud 

Bind the access level to a service account using the gcloud CLI.
    
    
    gcloud access-context-manager cloud-bindings create \
        --organization=ORGANIZATION_ID \
        --service-account=SERVICE_ACCOUNT_NAME@SERVICE_ACCOUNT_PROJECT_ID.iam.gserviceaccount.com \
        --level=accessPolicies/POLICY_ID/accessLevels/ACCESS_LEVEL_NAME
    

Replace the following:

  * `ORGANIZATION_ID`: your Google Cloud organization ID
  * `SERVICE_ACCOUNT_NAME`: the name, not the email, of the target service account
  * `SERVICE_ACCOUNT_PROJECT_ID`: the ID of the project that contains the target service account
  * `POLICY_ID`: the ID of the Access Context Manager access policy
  * `ACCESS_LEVEL_NAME`: the name of the access level that you created

To use Context-Aware Access without enforcing the access level and disallowing access, you can bind the access level in dry-run mode.




###  REST API 

To bind the access level to a specific service account using the REST API, run the following command:

  1. Create a `request.json` file with the following content:
         
         {
           "principal": {
             "serviceAccount": "SERVICE_ACCOUNT_NAME@SERVICE_ACCOUNT_PROJECT_ID.iam.gserviceaccount.com"
           },
           "accessLevels": ["accessPolicies/POLICY_ID/accessLevels/ACCESS_LEVEL_NAME"]
         }
         

Replace the following:

     * `SERVICE_ACCOUNT_NAME`: the name, not the email, of the target service account

     * `SERVICE_ACCOUNT_PROJECT_ID`: the ID of the project that contains the target service account

     * `POLICY_ID`: the ID of the Access Context Manager access policy

     * `ACCESS_LEVEL_NAME`: the name of the access level that you created

  2. Run the following command:
         
         curl -H "X-Goog-User-Project: PROJECT_ID" -X POST \
           -H "Authorization: Bearer $(gcloud auth print-access-token)" \
           -H "Content-Type: application/json; charset=utf-8" \
           -d @request.json \
           "https://accesscontextmanager.googleapis.com/v1/organizations/ORGANIZATION_ID/gcpUserAccessBindings"
         

Replace the following:

     * `PROJECT_ID`: the ID of the project that you are using to make the API calls

     * `ORGANIZATION_ID`: your Google Cloud organization ID.




### Bind the access level to all service accounts in a project

This section describes how to bind the access level to all of the service accounts in a project.

###  gcloud 

To bind the access level to all of the service accounts in a project using the gcloud CLI, run the following command:
    
    
    gcloud access-context-manager cloud-bindings create \
      --organization=ORGANIZATION_ID \
      --service-account-project-number=PROJECT_NUMBER \
      --level=accessPolicies/POLICY_ID/accessLevels/ACCESS_LEVEL_NAME
    

Replace the following:

  * `ORGANIZATION_ID`: your Google Cloud organization ID
  * `PROJECT_NUMBER`: the project number of the project that contains all of the service accounts that you want to bind access to
  * `POLICY_ID`: the ID of the Access Context Manager access policy
  * `ACCESS_LEVEL_NAME`: the name of the access level that you created.



###  REST API 

To bind the access level to all of the service accounts in a project using the REST API, do the following:

  1. Create a `request.json` file with the following content:
         
         {
           "principal": {
             "serviceAccountProjectNumber": "PROJECT_NUMBER"
           },
           "accessLevels": ["accessPolicies/POLICY_ID/accessLevels/ACCESS_LEVEL_NAME"]
         }
         

Replace the following:

     * `PROJECT_NUMBER`: the project number of the project that contains all of the service accounts that you want to bind access to
     * `POLICY_ID`: the ID of the Access Context Manager access policy
     * `ACCESS_LEVEL_NAME`: the name of the access level that you created.
  2. Run the following command:
         
         curl -H "X-Goog-User-Project: PROJECT_ID" -X POST \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Content-Type: application/json; charset=utf-8" \
         -d @request.json \
         "https://accesscontextmanager.googleapis.com/v1/organizations/ORGANIZATION_ID/gcpUserAccessBindings"
         

Replace the following:

     * `PROJECT_ID`: the ID of the project you are using to make the API calls
     * `ORGANIZATION_ID`: your Google Cloud organization ID



To use Context-Aware Access without enforcing the access level and denying access, you can bind the access level in dry-run mode.

The API response for the create binding operation includes the name of the binding, which contains the unique binding ID.

## Use dry-run mode

You can bind the access level in dry-run mode. When you use dry-run mode, your service accounts can continue to access resources without enforcement. However, if your service accounts attempt access that violates the access level, Context-Aware Access logs the violation to Cloud Audit Logs.

### Bind the access level in dry-run mode

###  gcloud 

To bind the access level in dry-run mode, replace the `--level` parameter with `--dry-run-level`, formatted as follows:
    
    
    --dry-run-level=accessPolicies/POLICY_ID/accessLevels/ACCESS_LEVEL_NAME
    

###  REST API 

To bind the access level in dry-run mode, create the `request.json` file with the following content:
    
    
    {
    "principal": {
      "serviceAccountProjectNumber": "TARGET_PROJECT_NUMBER"
    },
    "dryRunAccessLevels": ["accessPolicies/POLICY_ID/accessLevels/ACCESS_LEVEL_NAME"]
    }
    

Replace the following:

  * `TARGET_PROJECT_NUMBER`: the project number of the target project
  * `POLICY_ID`: the ID of the Access Context Manager access policy
  * `ACCESS_LEVEL_NAME`: the name of the access level



### Check Cloud Audit Logs

This section describes how you can check Cloud Audit Logs for dry-run mode access denials for your service account. To learn more about searching for dry-run mode entries in Cloud Audit Logs, see [View dry-run mode logs](https://docs.cloud.google.com/access-context-manager/docs/apply-policies-to-user-groups#view-dry-run-logs).

###  Console 

To view Cloud Audit Logs dry-run mode service account access denials by using the Google Cloud console, do the following:

In the Google Cloud console, go to the segment **Logs Explorer** page: 

[Go to **Logs Explorer**](https://console.cloud.google.com/logs/query)

If you use the search bar to find this page, then select the result whose subheading is **Logging**.

  1. In the Google Cloud console, select your project or organization.

  2. In the Log query field, enter the following query:
         
         protoPayload.serviceName="contextawareaccess.googleapis.com"
         protoPayload.metadata.dryRunEvaluationResult:DENIED
         SEARCH("SERVICE_ACCOUNT_NAME")
         

  3. In the time range selector, choose from a predefined relative time, like **Last 30 minutes** , **Last 1 hour** , or **Last 24 hours** , or specify a custom range.




###  gcloud 

To view Cloud Audit Logs dry-run mode service account access denials by using the gcloud CLI, do the following:
    
    
    gcloud logging read \
    'protoPayload.serviceName="contextawareaccess.googleapis.com" AND
     protoPayload.metadata.dryRunEvaluationResult:DENIED AND
     SEARCH("SERVICE_ACCOUNT_NAME")' \
      --organization=ORGANIZATION_ID
    

Replace the following:

  * `ORGANIZATION_ID`: the ID of the organization
  * `SERVICE_ACCOUNT_NAME`: the name of the service account



The `gcloud logging read` command supports the `--freshness` flag to view logging information over relative timeframes. For example, by adding `--freshness=3h` to the command, you can view dry-run mode log entries over the last 3 hours.

## Troubleshooting

This section describes how to troubleshoot Context-Aware Access for service accounts.

### General troubleshooting

  1. Review Cloud Audit Logs.

Use the following log query and review log entries for more information.
         
         protoPayload.serviceName="contextawareaccess.googleapis.com"
         

  2. Review the access level resource name that Context-Aware Access reports when it logs enforcement events.

  3. Make sure that the access level is an org-level resource.

  4. Make sure that the access level in your Context-Aware Access policy is based on attributes that are supported for service accounts.

  5. Verify that the Context-Aware Access policy is bound to the intended service account.

  6. Make sure that your _user_ identity isn't access restricted by a Context-Aware Access policy. This can happen when a user identity is a member of a Google group that has a bound Context-Aware Access policy. That policy might restrict user access, in turn preventing call flow to the service account.

  7. Contact your security administrator.




### Access denied

Access is denied because of the following:

  * You bound the Context-Aware Access policy in enforcement mode rather than dry-run mode.

Instead of enforcement, you can use dry-run mode to let service accounts access resources and log enforcement events without actually denying access to resources. Additionally, you can follow general troubleshooting instructions.

  * The access level needs to be updated to include more sources. For example, an IP address is being used that wasn't included in the access level when it was created.




## What's next

  * Learn how to [manage access bindings](https://docs.cloud.google.com/access-context-manager/docs/manage-access-bindings).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
