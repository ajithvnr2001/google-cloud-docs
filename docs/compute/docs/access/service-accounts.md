---
url: https://docs.cloud.google.com/compute/docs/access/service-accounts/
title: Service accounts \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:16:58.320467+00:00
---

# Service accounts  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/access/service-accounts/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Service accounts Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how service accounts work with Compute Engine.

For step-by-step information about attaching a service account to a virtual machine (VM) instance, review one of the following documents:

  * To set up service account during VM creation, see [Create a VM that uses a user-managed service account](https://docs.cloud.google.com/compute/docs/access/create-enable-service-accounts-for-instances).
  * To set up service account on an existing VM, see [Change the attached service account](https://docs.cloud.google.com/compute/docs/instances/change-service-account).



To learn about best practices for creating and managing service accounts, read the [Best practices for working with service accounts](https://docs.cloud.google.com/iam/docs/best-practices-service-accounts) documentation.

##  Try it for yourself 

If you're new to Google Cloud, create an account to evaluate how Compute Engine performs in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 

[ Try Compute Engine free ](https://console.cloud.google.com/freetrial)

## What is a service account?

A [service account](https://docs.cloud.google.com/iam/docs/service-accounts) is a special kind of account used by an application or compute workload, rather than a person. Service accounts are managed by [Identity and Access Management (IAM)](https://docs.cloud.google.com/iam/docs).

Keep the following in mind when using service accounts with your VMs:

  * You can attach the same service account to multiple VMs, but a single VM can only have one service account attached to it.
  * If you attach the same service account to multiple VMs, any subsequent changes you make to the service account affects all VMs that use the service account. This includes any changes you make to the IAM roles granted to the service account. For example, if you remove a role, all VMs using the service account lose the permissions granted by that role.



## How Compute Engine uses service accounts

Compute Engine uses two types of service accounts:

  * User-managed service accounts
  * Service agents



A user-managed service account can be attached to a Compute Engine instance to provide credentials to applications running on the instance. These credentials are used by the application for authentication to Google Cloud APIs, and authorization to access Google Cloud resources. Only user-managed service accounts can be attached to an instance, and an instance can have only one attached service account. You can change the service account that is attached to an instance at creation time or later on.

Service agents are used by the instance to access internal processes on your behalf.

In addition, you can create [firewall rules](https://docs.cloud.google.com/vpc/docs/firewalls) that allow or deny traffic to and from instances based on the service account that you associate with each instance.

### How authorization is determined

The authorization provided to applications hosted on a Compute Engine instance is limited by two separate configurations: the roles granted to the attached service account, and the access scopes that you set on the instance. Both of these configurations must allow access before the application running on the instance can access a resource.

Suppose you have an app that reads and writes files on Cloud Storage, it must first authenticate to the Cloud Storage API. You can create an instance with the `cloud-platform` scope and attach a service account to the instance. You can then grant Identity and Access Management (IAM) roles to the service account to give your app access to the appropriate resources. Your app uses the service account credentials to authenticate to the Cloud Storage API without embedding any secret keys or user credentials in your instance, image, or app code. Your app also uses the authorization provided by the IAM roles on the service account to access resources. For more information about authorization, see Authorization on this page.

## User-managed service accounts

User-managed service accounts include new service accounts that you explicitly create and the Compute Engine default service account.

### New service accounts

You can create and manage your own service accounts using [IAM](https://docs.cloud.google.com/iam). After you create an account, you grant the account IAM roles and set up instances to run as the service account. Apps running on instances with the service account attached can use the account's credentials to make requests to other Google APIs.

To create and set up a new service account, see [Create a VM that uses a user-managed service account](https://docs.cloud.google.com/compute/docs/access/create-enable-service-accounts-for-instances).

### Compute Engine default service account

New projects that have [enabled](https://console.cloud.google.com/apis/api/compute.googleapis.com/overview) the Compute Engine API have a Compute Engine default service account, which has the following email:
    
    
    PROJECT_NUMBER-compute@developer.gserviceaccount.com

The Compute Engine default service account has the following attributes:

  * Automatically created, with an autogenerated name and email address, and added to your project when you enable the Compute Engine API. You have full control over the account.
  * Attached by default to all VMs that you created by using the Google Cloud CLI or the Google Cloud console. You can override this behavior by specifying a different service account when you create the VM, or by explicitly specifying that no service account be attached to the VM.
  * Depending on your organization policy configuration, the default service account might automatically be granted the [Editor role](https://docs.cloud.google.com/iam/docs/roles-overview#basic) on your project. We strongly recommend that you disable the automatic role grant by [ enforcing the `iam.automaticIamGrantsForDefaultServiceAccounts` organization policy constraint](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-service-accounts#disable_service_account_default_grants). If you created your organization after May 3, 2024, this constraint is enforced by default. 

If you disable the automatic role grant, you must decide which roles to grant to the default service accounts, and then [grant these roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access) yourself. 

If the default service account already has the Editor role, we recommend that you replace the Editor role with less permissive roles.To safely modify the service account's roles, use [Policy Simulator](https://docs.cloud.google.com/policy-intelligence/docs/simulate-iam-policies) to see the impact of the change, and then [grant and revoke the appropriate roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).




You can disable or delete this service account from your project, but doing so might cause any applications that depend on the service account's credentials to fail. If you accidentally delete the Compute Engine default service account, you can try to recover the account within 30 days. For more information, see [Delete and undelete service accounts](https://docs.cloud.google.com/iam/docs/service-accounts-delete-undelete#undeleting).

If the Compute Engine default service account was deleted more than 30 days ago, you can try to recover the service account by following the process in [Troubleshooting default service accounts](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-default-service-accounts).

## Service agents

[_Service agents_](https://docs.cloud.google.com/iam/docs/service-account-types#service-agents) are created and managed by Google Cloud and assigned to your project automatically. These accounts represent different Google Cloud services, and each account typically has some level of access to your Google Cloud resources.

You cannot attach service agents to a Compute Engine instance.

### Google APIs Service Agent

Apart from the default service account, all projects enabled with Compute Engine come with a **Google APIs Service Agent** , identifiable using the email:
    
    
    PROJECT_NUMBER@cloudservices.gserviceaccount.com

This service agent is designed specifically to run internal Google processes on your behalf. This service agent is owned by Google and is not listed in the **Service Accounts** section of Google Cloud console. By default, this service agent is automatically granted the project editor role on the project and is listed in the **IAM** section of Google Cloud console. This service agent is deleted only when the project is deleted. However, you can change the roles granted to this account, including revoking all access to your project.

Certain resources rely on the default editor permissions granted to this service agent. For example, managed instance groups and autoscaling uses the credentials of this service agent to create, delete, and manage instances. If you revoke permissions to this service agent, or modify the permissions in such a way that it doesn't grant permissions to create instances, this will cause managed instance groups and autoscaling to stop working.

For these reasons, you should not modify this service agent's roles unless a [role recommendation](https://docs.cloud.google.com/iam/docs/recommender-overview) explicitly suggests that you modify them.

### Compute Engine Service Agent

All projects that have enabled the Compute Engine API have a **Compute Engine Service Agent** , which has the following email:
    
    
    service-PROJECT_NUMBER@compute-system.iam.gserviceaccount.com

This service agent is designed specifically for Compute Engine to perform its service duties on your project. It relies on the Service Agent IAM Policy granted on your Google Cloud Project. It is also the service agent Compute Engine uses to access the user-managed service account on VM instances. Google owns this account, but it is specific to your project. This service agent is hidden from the [IAM page](https://console.cloud.google.com/iam-admin/iam) in the console unless you select **Include Google-provided role grants**. By default, this service agent is automatically granted the `compute.serviceAgent` role on your project.

This service agent is deleted only when you delete your project. You can change the roles granted to this service agent and revoke all access to your project from this agent. Revoking or changing the permissions for this service agent prevents Compute Engine from accessing the identities of your service accounts on your VMs, and can cause outages of software running inside your VMs.

For these reasons, you should avoid modifying the roles for this service agent as much as possible.

## Attaching a service account to an instance

To avoid providing an application with excess permissions, we recommend that you create a user-managed service account, grant it only the roles your application needs to function properly, and attach it to your Compute Engine instance. Your code can then use [Application Default Credentials](https://docs.cloud.google.com/docs/authentication/application-default-credentials) to authenticate with the credentials provided by the service account.

You can attach a service account to a Compute Engine instance when you create the instance, or later. Only one service account can be attached to an instance at a time; if you attach a service account to an instance that already has a service account attached, the previous service account is no longer used by that instance.

When you attach a service account to a Compute Engine instance, you must also ensure that the scopes set on the instance are correct. Otherwise, your app might not be able to access all of the APIs it needs. For more information, see Access scopes on this page.

For step-by-step information about attaching a service account to a Compute Engine instance, review one of the following documents:

  * [Create a VM that uses a user-managed service account](https://docs.cloud.google.com/compute/docs/access/create-enable-service-accounts-for-instances)
  * [Change the attached service account](https://docs.cloud.google.com/compute/docs/instances/change-service-account)



## Authorization

When you set up an instance to run as a service account, you determine the level of access the service account has by the IAM roles that you [grant to the service account](https://docs.cloud.google.com/iam/docs/granting-roles-to-service-accounts). If the service account has no IAM roles, then no resources can be accessed using the service account on that instance.

Furthermore, an instance's access scopes determine the default OAuth scopes for requests made through the gcloud CLI and client libraries on the instance. As a result, access scopes potentially further limit access to API methods when authenticating through OAuth. However, they don't extend to other authentication protocols like gRPC.

The best practice is to set the full `cloud-platform` access scope on the instance, then control the service account's access using IAM roles.

Essentially:

  * IAM restricts access to APIs based on the IAM roles that are granted to the service account.
  * Access scopes potentially further limit access to API methods.



Both access scopes and IAM roles are described in detail in the following sections.

### IAM roles

You must [grant the appropriate IAM roles to a service account](https://docs.cloud.google.com/iam/docs/granting-roles-to-service-accounts) to allow that service account access to relevant API methods.

For example, you can grant a service account the IAM roles for managing Cloud Storage objects, or for managing Cloud Storage buckets, or both, which limits the account to the permissions granted by those roles.

When you grant an IAM role to a service account, any application running on an instance that has that service account attached will have the authorization conferred by that role.

Some things to keep in mind:

  * **Some IAM roles are in Beta.**

If there isn't a predefined role for the access level you want, you can create and grant [custom roles](https://docs.cloud.google.com/iam/docs/understanding-custom-roles).

  * **You must set access scopes on the instance to authorize access.**

While a service account's access level is determined by the roles granted to the service account, an instance's access scopes determine the default OAuth scopes for requests made through the gcloud CLI and client libraries on the instance. As a result, access scopes potentially further limit access to API methods when authenticating through OAuth.




### Access scopes

Access scopes are the legacy method of specifying authorization for your VM instance. They define the default OAuth scopes used in requests from the gcloud CLI or the client libraries. Access scopes don't apply for calls made using gRPC.

Access scopes apply on a per-VM basis and persists only for the life of the VM. You can set access scopes when creating a VM or [update the access scope](https://docs.cloud.google.com/compute/docs/instances/change-service-account#changeserviceaccountandscopes) on an existing VM.

Generally, the documentation for each API method lists the scopes required for that method. For example, the `instances.insert` method provides a list of valid scopes in its [authorization](https://docs.cloud.google.com/compute/docs/reference/latest/instances/insert#authorization-scopes) section.

Access scopes have no effect if you have not enabled the related API on the project that the service account belongs to. For example, granting an access scope for Cloud Storage on a virtual machine instance allows the instance to call the Cloud Storage API only if you have enabled the Cloud Storage API on the project.

#### Default scopes

When you create a new Compute Engine instance, it is automatically configured with the following access scopes:

  * Read-only access to Cloud Storage:   
`https://www.googleapis.com/auth/devstorage.read_only`
  * Write access to write Compute Engine logs:   
`https://www.googleapis.com/auth/logging.write`
  * Write access to publish metric data to your Google Cloud projects:   
`https://www.googleapis.com/auth/monitoring.write`
  * Read-only access to Service Management features required for Google Cloud Endpoints(Alpha):   
`https://www.googleapis.com/auth/service.management.readonly`
  * Read or write access to Service Control features required for Google Cloud Endpoints(Alpha):   
`https://www.googleapis.com/auth/servicecontrol`
  * Write access to [Cloud Trace](https://docs.cloud.google.com/trace) allows an application running on a VM to write trace data to a project.   
`https://www.googleapis.com/auth/trace.append`



#### Scopes best practice

There are many [access scopes](https://developers.google.com/identity/protocols/googlescopes) available to choose from, but a best practice is to set the `cloud-platform` access scope, which is an OAuth scope for Google Cloud services, and then control the service account's access by granting it IAM roles.
    
    
    https://www.googleapis.com/auth/cloud-platform

#### Scopes examples

Following the scopes best practice, if you enabled the `cloud-platform` access scope on an instance and then granted the following [predefined IAM roles](https://docs.cloud.google.com/iam/docs/roles-permissions):

  * `roles/compute.instanceAdmin.v1`
  * `roles/storage.objectViewer`
  * `roles/compute.networkAdmin`



Then the service account has only the permissions included in those three roles. Applications impersonating that service account cannot perform actions outside of these roles despite the Google Cloud access scope.

On the other hand, if you grant a more restrictive scope on the instance, like the Cloud Storage read-only scope (`https://www.googleapis.com/auth/devstorage.read_only`), and set the `roles/storage.objectAdmin` administrator role on the service account, then by default, requests from the gcloud CLI and the client libraries wouldn't be able to manage Cloud Storage objects from that instance, even though you granted the service account the `roles/storage.ObjectAdmin` role. This is because the Cloud Storage read-only scope does not authorize the instance to manipulate Cloud Storage data.

Example access scopes include the following:

  * `https://www.googleapis.com/auth/cloud-platform`. View and manage your data across Google Cloud services in the specified Google Cloud project.
  * `https://www.googleapis.com/auth/compute`. Full control access to Compute Engine methods.
  * `https://www.googleapis.com/auth/compute.readonly`. Read-only access to Compute Engine methods.
  * `https://www.googleapis.com/auth/devstorage.read_only`. Read-only access to Cloud Storage.
  * `https://www.googleapis.com/auth/logging.write`. Write access to the Compute Engine logs.



## What's next

  * [Authenticate workloads using service accounts](https://docs.cloud.google.com/compute/docs/access/authenticate-workloads).
  * Learn more about [creating and managing service accounts](https://docs.cloud.google.com/iam/docs/creating-managing-service-accounts).
  * Learn more about [IAM](https://docs.cloud.google.com/iam/docs).
  * Learn about other [Compute Engine access control options](https://docs.cloud.google.com/compute/docs/access).
  * Learn how to [view audit logs](https://docs.cloud.google.com/compute/docs/audit-logging) to monitor how your Compute Engine resources are modified.
  * If you need to use a service account from a different project, read about [configuring service accounts for a resource in a different project](https://docs.cloud.google.com/iam/docs/attach-service-accounts#attaching-different-project).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
