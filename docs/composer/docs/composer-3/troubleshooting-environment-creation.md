---
url: https://docs.cloud.google.com/composer/docs/composer-3/troubleshooting-environment-creation/
title: Troubleshooting environment creation \u00a0|\u00a0 Managed Service for Apache Airflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:02:53.177705+00:00
---

# Troubleshooting environment creation  |  Managed Service for Apache Airflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/composer/docs/composer-3/troubleshooting-environment-creation/

To more strongly embrace the success and growing customer preference for OSS solutions, Cloud Composer is evolving to become **Managed Service for Apache Airflow**. This name change provides improved customer understanding of our portfolio while reinforcing our commitment to being the most open cloud ecosystem. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Airflow ](https://docs.cloud.google.com/composer/docs)
  * [ Gen 3 Guides ](https://docs.cloud.google.com/composer/docs/composer-3/composer-overview)



Send feedback 

#  Troubleshooting environment creation Stay organized with collections  Save and categorize content based on your preferences. 

**Managed Airflow (Gen 3)** | [Managed Airflow (Gen 2)](https://docs.cloud.google.com/composer/docs/composer-2/troubleshooting-environment-creation "View this page for Managed Airflow \(Gen 2\)") | [Managed Airflow (Legacy Gen 1)](https://docs.cloud.google.com/composer/docs/composer-1/troubleshooting-environment-creation "View this page for Managed Airflow \(Legacy Gen 1\)")

This page provides troubleshooting information for problems that you might encounter while creating Managed Airflow environments.

For troubleshooting information related to updating and upgrading environments, see [Troubleshooting environment updates and upgrades](https://docs.cloud.google.com/composer/docs/composer-3/troubleshooting-updates-upgrades).

When Managed Airflow environments are created, the majority of issues happen because of the following reasons:

  * Service account permission problems.

  * Incorrect Firewall, DNS or routing information.

  * Network-related issues. For example, invalid VPC configuration, IP address conflicts, or network IP ranges that are too narrow.

  * Quota-related issues.

  * Incompatible Organization Policies.




## Insufficient permissions to create an environment

**Note:** You can validate that you configured permissions are correct using the [IAM permission validation](https://github.com/arunjvattoly/Composer) script. The script validates the permissions for both Shared VPC and non-Shared VPC configuration.

If Managed Airflow cannot create an environment because your account has insufficient permissions, it outputs the following error messages:
    
    
    ERROR: (gcloud.composer.environments.create) PERMISSION_DENIED: The caller
    does not have permission
    

or
    
    
    ERROR: (gcloud.composer.environments.create) PERMISSION_DENIED: User not
    authorized to act as service account <service-account-name>.
    The user must be granted iam.serviceAccounts.actAs permission, included in
    Owner, Editor, Service Account User role. See https://cloud.google.com/iam/docs
    /understanding-service-accounts for additional details.
    

**Solution** : Assign roles to both to your account and to the service account of your environment as described in [Access control](https://docs.cloud.google.com/composer/docs/composer-3/access-control).

  * In Managed Airflow (Gen 2), make sure that **Cloud Composer Service Agent** service account (`service-PROJECT_NUMBER@cloudcomposer-accounts.iam.gserviceaccount.com`) has the **Cloud Composer v2 API Service Agent Extension** role assigned.

  * Make sure that **Google APIs Service Agent** (`PROJECT_NUMBER@cloudservices.gserviceaccount.com`) has the **Editor** role assigned.

  * In the Shared VPC configuration, follow [Configure Shared VPC instructions](https://docs.cloud.google.com/composer/docs/composer-3/configure-shared-vpc).




## The service account of the environment has insufficient permissions

When creating a Managed Airflow environment, you specify a service account that runs the environment's GKE cluster nodes. If this service account does not have enough permissions for the requested operation, Managed Airflow outputs the following error:
    
    
    Errors in: [Web server]; Error messages:
      Creation of airflow web server version failed. This may be an intermittent
      issue of the App Engine service. You may retry the operation later.
    {"ResourceType":"appengine.v1.version","ResourceErrorCode":"504","ResourceError
    Message":"Your deployment has failed to become healthy in the allotted time
    and therefore was rolled back. If you believe this was an error, try adjusting
    the 'app_start_timeout_sec' setting in the 'readiness_check' section."}
    

**Solution** : Assign roles to both to your account and to the service account of your environment as described in [Access control](https://docs.cloud.google.com/composer/docs/composer-3/access-control).

## Warnings about missing IAM roles in service accounts

When an environment creation fails, Managed Airflow generates the following warning message after an error occurred: `The issue may be caused by missing IAM roles in the following Service Accounts ...`.

This warning message highlights possible causes for the error. Managed Airflow checks for required roles on the service accounts in your project, and if these roles are not present, it generates this warning message.

**Note:** This check applies only to the project where you create the environment. In case of Shared VPC configuration, Managed Airflow does not perform this check in the host project. To enable this check in Shared VPC, the Managed Airflow Service Agent account from the service project must have permission to view roles in the host project. To allow it, grant the **Role Viewer** (`roles/iam.roleViewer`) role to the Managed Airflow Service Agent account from the service project at the host project level.

**Solution** : Check that service accounts mentioned in the warning message have the required roles. For more information about roles and permissions in Managed Airflow, see [Access control](https://docs.cloud.google.com/composer/docs/composer-3/access-control).

In some cases, you can ignore this warning. Managed Airflow does not check individual permissions assigned to roles. For example, If you use custom IAM roles, it is possible that the service account mentioned in the warning message already has all required permissions. In this case, you can ignore this warning.

## Incompatible organization policies

The following policies must be configured appropriately so that Managed Airflow environments can be created successfully.

**Important:** This page only **lists incompatible organization policies** for Managed Airflow and how they must be configured. For **detailed instructions about configuring each policy** , see [Organization policy constraints](https://docs.cloud.google.com/resource-manager/docs/organization-policy/org-policy-constraints) in the Resource Manager documentation.Organization Policy | Managed Airflow (Gen 3) | Managed Airflow (Gen 2) | Managed Airflow (Legacy Gen 1)  
---|---|---|---  
`compute.disableSerialPortLogging` | Any value is allowed | Must be disabled | Disabled for versions earlier than 1.13.0; otherwise any value  
`compute.requireOsLogin` | Any value is allowed | Any value is allowed | Must be disabled  
`compute.vmCanIpForward` | Any value is allowed | Any value is allowed | Must be allowed (required for Managed Airflow-owned GKE clusters) when VPC-native mode (using alias IP) is not configured  
`compute.vmExternalIpAccess` | Any value is allowed | Must be allowed for Public IP environments | Must be allowed for Public IP environments  
`compute.restrictVpcPeering` | Can be enforced | Cannot be enforced | Cannot be enforced  
`compute.disablePrivateServiceConnectCreationForConsumers` | Any value is allowed | Cannot disallow SERVICE_PRODUCERS for Private and Public IP environments. Does not affect existing environments, they can operate when this policy is enabled. | Cannot disallow SERVICE_PRODUCERS for Private IP environments. Does not affect existing environments, they can operate when this policy is enabled.  
`compute.restrictPrivateServiceConnectProducer` | When active, allowlist the `google.com` organization | When active, allowlist the `google.com` organization | Any value is allowed  
  
## Incompatible principal access boundary policies

[Principal access boundary policies](https://docs.cloud.google.com/iam/docs/principal-access-boundary-policies) configured in your organization can be configured in a way that blocks some of your environment's operations or prevents the creation of new environments.

If this is the case, you might see the following line in the error messages:
    
    
    Operations on resource are denied due to an IAM Principal Access Boundary Policy.
    

The components of your environment are located in [a tenant and a customer project](https://docs.cloud.google.com/composer/docs/composer-3/environment-architecture#about-customer-tenant). The tenant project is Google-managed and doesn't belong to the organization where the environment is located. The [service account of your environment](https://docs.cloud.google.com/composer/docs/composer-3/access-control#service-account) must have permissions to perform operations in the tenant project.

**Solution** :

  * Add a condition expression to the policy's binding to exclude the environment's service account from the policy. For an example of how to exclude a principal so that the policy doesn't apply to it, see [Conditional policy bindings for principal access boundary policies](https://docs.cloud.google.com/iam/docs/principal-access-boundary-policies#conditions) in the Identity and Access Management documentation.



## Restricting services used within organization or project

Organization or project administrators can restrict what Google services can be used in their projects using the [`gcp.restrictServiceUsage`](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-resources) organization policy constraint.

When using this organization policy, it's important to [allow all the services required by Managed Airflow](https://docs.cloud.google.com/composer/docs/composer-3/enable-composer-service#required-services).

## What's next

  * [Creating environments](https://docs.cloud.google.com/composer/docs/composer-3/create-environments)
  * [Troubleshooting environment updates and upgrades](https://docs.cloud.google.com/composer/docs/composer-3/troubleshooting-updates-upgrades)
  * [Access control](https://docs.cloud.google.com/composer/docs/composer-3/access-control)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
