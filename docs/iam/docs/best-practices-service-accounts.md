---
url: https://docs.cloud.google.com/iam/docs/best-practices-service-accounts/
title: Best practices for using service accounts securely \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:03:52.180871+00:00
---

# Best practices for using service accounts securely  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/best-practices-service-accounts/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Guides ](https://docs.cloud.google.com/iam/docs/overview)



Send feedback 

#  Best practices for using service accounts securely Stay organized with collections  Save and categorize content based on your preferences. 

This guide describes best practices for securely managing, using, and protecting your Google Cloud service accounts against security threats.

[Service accounts](https://docs.cloud.google.com/iam/docs/service-account-overview) represent non-human users. They're intended for scenarios where a workload, such as a custom application, needs to access resources or perform actions without end-user involvement.

Service accounts differ from user accounts in multiple ways:

  * They don't have a password and can't be used for browser-based sign-in.
  * They're created and managed as a resource that belongs to a Google Cloud project. In contrast, users are managed in a Cloud Identity or Google Workspace account.
  * They're specific to Google Cloud. In contrast, the users managed in Cloud Identity or Google Workspace work across a multitude of Google products and services.
  * They're both a resource and a [principal](https://docs.cloud.google.com/docs/authentication#principal): 
    * As a principal, a service account can be granted access to resources, like a Cloud Storage bucket.
    * As a resource, a service account can be accessed and possibly [impersonated](https://docs.cloud.google.com/iam/docs/service-account-impersonation) by other principals, like a user or group.



Although service accounts are a useful tool, there are several ways in which a service account can be abused:

  * **Privilege escalation:** A bad actor might gain access to resources they otherwise wouldn't have access to by impersonating the service account.
  * **Spoofing:** A bad actor might use service account impersonation to obscure their identity.
  * **Non-repudiation:** A bad actor might conceal their identity and actions by using a service account to carry out operations on their behalf. In some cases, it might not be possible to trace these actions to the bad actor.
  * **Information disclosure:** A bad actor might derive information about your infrastructure, applications, or processes from the existence of certain service accounts.



To help secure service accounts, consider their dual nature:

  * Because a service account is a principal, you must limit its privileges to reduce the potential harm that can be done by a compromised service account.
  * Because a service account is a resource, you must protect it from being compromised.



## Choose when to use service accounts

Not every scenario requires a service account to access Google Cloud services, and many scenarios can authenticate with a more secure method than using a service account key. We recommend that you avoid using service account keys whenever possible.

When you access Google Cloud services by using the Google Cloud CLI, Cloud Client Libraries, tools that support [ Application Default Credentials (ADC)](https://docs.cloud.google.com/docs/authentication/application-default-credentials) like Terraform, or REST requests, use the following diagram to help you choose an authentication method: 

![Decision tree for choosing authentication method based on use case](https://docs.cloud.google.com/static/docs/authentication/images/authn-tree.svg)

This diagram guides you through the following questions: 

  1. Are you running code in a single-user development environment, such as your own workstation, Cloud Shell, or a virtual desktop interface? 
     1. If yes, proceed to question 4.
     2. If no, proceed to question 2.
  2. Are you running code in Google Cloud? 
     1. If yes, proceed to question 3.
     2. If no, proceed to question 5.
  3. Are you running containers in Google Kubernetes Engine? 
     1. If yes, use [ Workload Identity Federation for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity#authenticating_to) to attach service accounts to Kubernetes pods. 
     2. If no, [attach a service account](https://docs.cloud.google.com/iam/docs/attach-service-accounts#attaching-to-resources) to the resource. 
  4. Does your use case require a service account?

For example, you want to configure authentication and authorization consistently for your application across all environments. 

     1. If no, [authenticate with user credentials](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment#local-user-cred). 
     2. If yes, [ impersonate a service account with user credentials](https://docs.cloud.google.com/docs/authentication/use-service-account-impersonation). 
  5. Does your workload authenticate with an external identity provider that supports [workload identity federation](https://docs.cloud.google.com/iam/docs/workload-identity-federation#providers)? 
     1. If yes, [ configure Workload Identity Federation](https://docs.cloud.google.com/iam/docs/workload-identity-federation-with-other-clouds) to let applications running on-premises or on other cloud providers use a service account. 
     2. If no, [create a service account key](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment#local-key). 



## Manage service accounts

Service accounts differ from other types of principals, not only in how they're used, but also in how they must be managed. The following sections provide best practices for managing service accounts.

**Best practices** :

Manage service accounts as resources.  
Create single-purpose service accounts.  
Follow a naming and documentation convention.  
Identify and disable unused service accounts.  
Disable unused service accounts before deleting them.  


### Manage service accounts as resources

Accounts for individual users are typically managed according to an organization's _joiner-mover-leaver_ processes: When an employee joins, a new user account is created for them. When they move departments, their user account is updated. And when they leave the company, their user account is suspended or deleted.

In contrast, service accounts aren't associated with any particular employee. Instead, it's best to think of service accounts as resources that belong to—or are part of—another resource, such as a particular VM instance or an application.

To effectively manage service accounts, don't look at service accounts in isolation. Instead, consider them in the context of the resource they're associated with and manage the service account and its associated resource as one unit: Apply the same processes, same lifecycle, and same diligence to the service account and its associated resource, and use the same tools to manage them.

### Create single-purpose service accounts

Sharing a single service account across multiple applications can complicate the management of the service account:

  * The applications might have different life cycles. If an application is decommissioned, it might not be clear whether the service account can be decommissioned as well or whether it's still needed.
  * Over time, the access requirements of applications might diverge. If applications use the same service account, then you might need to grant the service account access to an increasing number of resources, which in turn increases the overall risk.
  * Cloud Audit Logs include the name of the service account that performed a change or accessed data, but they don't show the name of the application that used the service account. If multiple applications share a service account, you might not be able to trace activity back to the correct application.



In particular, some Google Cloud services, including App Engine and Compute Engine, create a [default service account](https://docs.cloud.google.com/iam/docs/service-account-types#default) that has the Editor role (`roles/editor`) on the project by default. When you create a resource such as a Compute Engine virtual machine (VM) instance, and you don't specify a service account, the resource can automatically use the default service account. Although the default service account makes it easier for you to get started, it's very risky to share such a powerful service account across multiple applications.

You can take several steps to avoid these complications:

  * Create dedicated service accounts for each application, and avoid using default service accounts.
  * Don't use automatic role grants for default service accounts.
  * Use Google's [tools to understand service account usage](https://docs.cloud.google.com/iam/docs/service-account-usage-tools), which can help you monitor usage and prevent service accounts from being shared across multiple applications.



### Follow a naming and documentation convention

To help track the association between a service and an application or resource, follow a naming convention when creating new service accounts:

  * Add a prefix to the service account email address that identifies how the account is used. For example: 
    * `vm-` for service accounts attached to a VM instance.
    * `wlifgke-` for service accounts used by Workload Identity Federation for GKE.
    * `wlif-` for service accounts used by Workload Identity Federation.
    * `onprem-` for service accounts used by on-premises applications.
  * Embed the name of the application in the service account email address, for example: `vm-travelexpenses@` if the VM runs a travel expenses application.
  * Use the description field to add a contact person, links to relevant documentation, or other notes.



Don't embed sensitive information or terms in the email address of a service account.

### Identify and disable unused service accounts

When a service account isn't used anymore, [disable the service account](https://docs.cloud.google.com/iam/docs/service-accounts-disable-enable#disabling). By disabling unused service accounts, you reduce the risk of the service accounts being abused for lateral movement or for privilege escalation by a bad actor.

For single-purpose service accounts that are associated with a particular resource, such as a VM instance, disable the service account as soon as the associated resource is disabled or deleted.

For service accounts that are used for multiple purposes or shared across multiple resources, it can be more difficult to identify whether the service account is still used. In these cases, you can use [Activity Analyzer](https://docs.cloud.google.com/policy-intelligence/docs/service-account-usage-tools#sa-authn) to view the most recent authentication activities for your service accounts.

### Disable unused service accounts before deleting them

If you delete a service account and then create a new service account with the same name, the new service account is assigned a different identity. As a result, none of the original IAM bindings apply to the new service account. In contrast, if you disable and re-enable a service account, all IAM bindings stay intact.

To avoid inadvertently losing IAM bindings, it's best to not delete service accounts immediately. Instead, disable a service account if it isn't needed anymore and delete it only after a certain period has elapsed. By waiting to delete the service account, you are ensuring that you can safely remove it without affecting any of your IAM bindings.

You can delete default service accounts such as the [App Engine default service account](https://docs.cloud.google.com/appengine/docs/standard/python3/service-account) or the [Compute Engine default service account](https://docs.cloud.google.com/compute/docs/access/service-accounts#default_service_account). However, keep the following things in mind when deciding whether to delete a default service account:

  * Deleting a default service account can improve the security of your deployment. However, without a default service account, the corresponding service can't automatically deploy jobs that access other Google Cloud unless you manually configure a new service account and grant it the appropriate roles.
  * You can't recreate default service accounts after deleting them. If there's a chance that you might use the default service accounts in the future, we recommend leaving them disabled instead of deleting them.



Before you delete a default service account, we recommend verifying whether you use it in your deployment. For more information about the tools you can use to verify service account usage, see [Tools to understand service account usage](https://docs.cloud.google.com/iam/docs/service-account-usage-tools).

## Limit service account privileges

Service accounts are principals and can be granted access to a resource like any other type of principal. However, service accounts often have greater access to more resources than other types of principals. In addition, as you add functionality to your applications, their service accounts tend to gain more and more access over time; you might also forget to revoke access that's no longer needed.

**Best practices** :

Don't use automatic role grants for default service accounts.  
Don't rely on access scopes when attaching a service account to a VM instance.  
Avoid using domain-wide delegation.  
Use the IAM credentials API for temporary privilege elevation.  
Use Credential Access Boundaries to downscope access tokens.  
Use role recommendations to identify unused permissions.  
Use lateral movement insights to limit lateral movement.  


### Don't use automatic role grants for default service accounts

Some Google Cloud services create [default service accounts](https://docs.cloud.google.com/iam/docs/service-account-types#default) when you first enable their API in a Google Cloud project. Depending on your organization policy configuration, these service accounts might be automatically granted the Editor role (`roles/editor`) on your Google Cloud project, which allows them to read and modify all resources in the Google Cloud project. The role is granted for your convenience, but isn't essential for the services to work: To access resources in your Google Cloud project, Google Cloud services use [service agents](https://docs.cloud.google.com/iam/docs/service-agents), not the default service accounts.

To prevent default service accounts from automatically being granted the Editor role, enable the [Disable Automatic IAM Grants for Default Service Accounts](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-service-accounts#disable_service_account_default_grants) (`constraints/iam.automaticIamGrantsForDefaultServiceAccounts`) constraint to your organization. To apply the constraint to multiple Google Cloud projects, [configure it on the folder or the organization node](https://docs.cloud.google.com/resource-manager/docs/organization-policy/using-constraints#enforce_list_constraint). Applying the constraint doesn't remove the **Editor** role from existing default service accounts.

If you apply this constraint, then default service accounts in new projects will not have any access to your Google Cloud resources. You must grant appropriate roles to the default service accounts so that they can access your resources.

**Note** : If your organization was created on or after May 3, 2024, this constraint is enforced by default. 

### Don't rely on access scopes when attaching a service account to a VM instance

When you attach a service account to a VM instance, you can [specify one or more access scopes](https://docs.cloud.google.com/compute/docs/access/create-enable-service-accounts-for-instances#changeserviceaccountandscopes). Access scopes let you restrict which services the VM can access. The restrictions are applied in addition to allow policies.

Access scopes are coarse-grained. For example, by using the `https://www.googleapis.com/auth/devstorage.read_only` scope, you can restrict access to Cloud Storage read-only operations, but you can't restrict access to specific buckets. Therefore, access scopes aren't a suitable replacement for fine-grained allow policies.

Instead of relying on access scopes, create a [dedicated service account](https://docs.cloud.google.com/iam/docs/best-practices-for-using-and-managing-service-accounts#single-purpose) and use fine-grained allow policies to restrict which resources the service account has access to.

If _all_ current and future service accounts in a specific project, folder, or organization share requirements, then use [service account principal sets](https://docs.cloud.google.com/iam/docs/principal-identifiers#allow-service-account-principal-sets) to grant them roles instead of using custom groups.

For more information, see [Best practices for using Google groups](https://docs.cloud.google.com/iam/docs/groups-best-practices#members-org).

### Avoid using domain-wide delegation

[Domain-wide delegation](https://support.google.com/a/answer/162106#zippy=%2Cset-up-domain-wide-delegation-for-a-client) enables a service account to impersonate any user in a Cloud Identity or Google Workspace account. Domain-wide delegation enables a service account to perform certain administrative tasks in Google Workspace and Cloud Identity, or to access Google APIs that don't support service accounts from outside of Google Cloud.

Domain-wide delegation doesn't restrict a service account to impersonate a particular user, but allows it to impersonate _any_ user in a Cloud Identity or Google Workspace account, including super-admins. Allowing a service account to use domain-wide delegation can therefore make the service account an attractive target for privilege escalation attacks.

Avoid using domain-wide delegation if you can accomplish your task directly with a service account or by using the [OAuth consent flow](https://developers.google.com/identity/protocols/oauth2/web-server). For example, if you need to use Google Drive to store files, you could directly use a service account to upload files to a shared drive, or you could use the OAuth 2.0 consent flow to upload files on behalf of a user.

If you can't avoid using domain-wide delegation, [restrict the set of OAuth scopes](https://developers.google.com/admin-sdk/directory/v1/guides/delegation#delegate_domain-wide_authority_to_your_service_account) that the service account can use. Although [OAuth scopes](https://developers.google.com/admin-sdk/directory/v1/guides/authorizing) don't restrict which users the service account can impersonate, they restrict the types of user data that the service account can access.

Note that service accounts cannot directly own assets in Google Workspace. If you need to use Google Drive to store files instead of using [Buckets](https://docs.cloud.google.com/storage/docs/buckets), then upload the files directly to a Shared Drive, operate on behalf of a user using OAuth 2.0 consent flow, or use domain-wide delegation.

### Use the Service Account Credentials API for temporary privilege elevation

Some applications only require access to certain resources at specific times or under specific circumstances. For example:

  * An application might require access to configuration data during startup, but might not require that access once it's initialized.
  * A supervisor application might periodically start background jobs where each job has different access requirements.



In such scenarios, using a single service account and granting it access to all resources goes against the principle of least privilege. This is because, at any point in time, the application is likely to have access to more resources than it actually needs.

To help ensure that the different parts of your application only have access to the resources they need, use the Service Account Credentials API for temporary privilege elevation:

  * Create dedicated service accounts for each part of the application or use case and only grant the service account access to the necessary resources.
  * Create another service account that acts as the supervisor. Grant the supervisor service account the [Service Account Token Creator role](https://docs.cloud.google.com/iam/docs/service-account-permissions#token-creator-role) on the other service accounts so that it can request short-lived access tokens for these service accounts.
  * Split your application so that one part of the application serves as token broker and only let this part of the application use the supervisor service accounts.
  * Use the token broker to issue short-lived service accounts to the other parts of the application.



For help with creating short-lived credentials, see [Create short-lived credentials for a service account](https://docs.cloud.google.com/iam/docs/create-short-lived-credentials-direct).

### Use Credential Access Boundaries to downscope access tokens

Google access tokens are bearer tokens, which means that their use isn't tied to any particular application. If your application passes an access token to a different application, then that other application can use the token in the same way your application can. Similarly, if an access token is leaked to a bad actor, they can use the token to gain access.

Because access tokens are bearer tokens, you must protect them from being leaked or becoming visible to unauthorized parties. You can limit the potential damage a leaked access token can cause by restricting the resources it grants access to. This process is called downscoping.

Use [Credential Access Boundaries](https://docs.cloud.google.com/iam/docs/downscoping-short-lived-credentials) to downscope access tokens whenever you pass an access token to a different application, or to a different component of your application. Set the access boundary so that the token grants enough access to the required resources, but no more.

**Note:** Downscoping is only supported by Cloud Storage.

### Use role recommendations to identify unused permissions

When you first deploy an application, you might be unsure about which roles and permissions the application really needs. As a result, you might grant the application's service account more permissions that it requires.

Similarly, an application's access requirements might evolve over time, and some of the roles and permissions you granted initially might not be needed.

Use [role recommendations](https://docs.cloud.google.com/policy-intelligence/docs/role-recommendations-overview) to identify which permissions an application is actually using, and which permissions might be unused. Adjust the allow policies of affected resources to help ensure that an application isn't granted more access than it actually needs.

### Use lateral movement insights to limit lateral movement

Lateral movement is when a service account in one project has permission to impersonate a service account in another project. For example, a service account might have been created in project A, but have permissions to impersonate a service account in project B.

These permissions can result in a chain of impersonations across projects that gives principals unintended access to resources. For example, a principal could impersonate a service account in project A, and then use that service account to impersonate a service account in project B. If the service account in project B has permission to impersonate other service accounts in other projects in your organization, the principal could continue to use service account impersonation to move from project to project, gaining permissions as they go.

**Note:** Attaching a service account from one project to a resource in another project _does not_ constitute lateral movement, because it doesn't give the service account any impersonation permissions.

Recommender provides [lateral movement insights](https://docs.cloud.google.com/policy-intelligence/docs/role-recommendations-overview#lateral-movement-insights) to help you mitigate this issue. Lateral movement insights identify roles that allow a service account in one project to impersonate a service account in another project. To learn how to view and manage lateral movement insights directly, see [Manage lateral movement insights](https://docs.cloud.google.com/policy-intelligence/docs/lateral-movement-insights).

Some lateral movement insights are associated with role recommendations. You can apply those recommendations to reduce lateral movement across your projects. To learn how, see [Review and apply recommendations](https://docs.cloud.google.com/policy-intelligence/docs/review-apply-role-recommendations).

## Protect against privilege-escalation threats

A service account that hasn't been granted any roles, does not have access to any resources, and isn't [associated with any firewall rules](https://docs.cloud.google.com/vpc/docs/firewalls#serviceaccounts) is typically of limited value. After you grant a service account access to resources, the value of the service account increases: The service account becomes more useful to you, but it also becomes a more attractive target for privilege-escalation attacks.

As an example, consider a service account that has full access to a Cloud Storage bucket which contains sensitive information. In this situation, the service account is effectively as valuable as the Cloud Storage bucket itself. Instead of trying to access the bucket directly, a bad actor might attempt to take control of the service account. If that attempt is successful, the bad actor can escalate their privileges by impersonating the service account, which in turn gives them access to the sensitive information in the bucket.

Privilege-escalation techniques involving service accounts typically fall into these categories:

  * **Authenticating as the service account:** You might inadvertently grant a user permission to [impersonate](https://docs.cloud.google.com/iam/docs/service-account-impersonation) a service account or to [create a service account key](https://docs.cloud.google.com/iam/docs/creating-managing-service-account-keys) for a service account. If the service account is more privileged than the user themselves, then the user can authenticate as the service account to escalate their privileges and gain access to resources they otherwise couldn't access.

  * **Using resources that have an attached service account:** If a user has permission to access and modify CI/CD pipelines, VM instances, or other automation systems that have attached service accounts, then they might be able to perform actions using those resources' attached service accounts. As a result, even though they don't have permission to impersonate the service account, they might still be able to use the service account's permissions to perform actions that they wouldn't be allowed to perform themselves.

For example, if a user has SSH access to a Compute Engine VM instance, then they can run code on the instance to access any resource that the instance's attached service account can access.

  * **Allow policy, group, or custom role modifications:** A user who doesn't have access to a privileged service account might still have permission to modify the allow policies of the service account, enclosing Google Cloud project, or folder. The user could then extend one of these allow policies to grant themselves permission to (directly or indirectly) authenticate as the service account.




The following sections provide best practices for protecting service accounts from privilege-escalation threats.

**Best practices** :

Avoid letting users impersonate service accounts that are more privileged than the users themselves.  
Avoid letting users change the allow policies of service accounts that are more privileged than the users themselves.  
Don't let users create or upload service account keys.  
Don't grant access to service accounts at the Google Cloud project or folder level.  
Don't run code from less protected sources on compute resources that have a privileged service account attached.  
Limit shell access to VMs that have a privileged service account attached.  
Limit metadata server access to selected users and processes.  


### Avoid letting users authenticate as service accounts that are more privileged than the users themselves

By impersonating a service account, a user gains access to some or all of the resources the service account can access. If the service account has more extensive access than the user, then it's effectively more privileged than the user.

Granting a user permission to impersonate a more privileged service account can be a way to deliberately let users temporarily elevate their privileges—similar to using the `sudo` tool on Linux, or using process elevation on Windows. Unless you're dealing with a scenario where such temporary elevation of privilege is necessary, it's best to avoid letting users impersonate a more privileged service account.

Users can also indirectly gain a service account's permissions by [attaching it to a resource](https://docs.cloud.google.com/iam/docs/attach-service-accounts) and then running code on that resource. Running code in this way isn't service account impersonation because it only involves one authenticated identity (the service account's). However, it can give a user access that they wouldn't have otherwise.

Permissions that enable a user to impersonate a service account or attach a service account to a resource include the following:

  * `iam.serviceAccounts.getAccessToken`
  * `iam.serviceAccounts.getOpenIdToken`
  * `iam.serviceAccounts.actAs`
  * `iam.serviceAccounts.implicitDelegation`
  * `iam.serviceAccounts.signBlob`
  * `iam.serviceAccounts.signJwt`
  * `iam.serviceAccountKeys.create`
  * `deploymentmanager.deployments.create`
  * `cloudbuild.builds.create`



Roles that contain some of these permissions include (but aren't limited to):

  * Owner (`roles/owner`)
  * Editor (`roles/editor`)
  * Service Account User (`roles/iam.serviceAccountUser`)
  * Service Account Token Creator (`roles/iam.serviceAccountTokenCreator`)
  * Service Account Key Admin (`roles/iam.serviceAccountKeyAdmin`)
  * Service Account Admin (`roles/iam.serviceAccountAdmin`)
  * Workload Identity User (`roles/iam.workloadIdentityUser`)
  * Deployment Manager Editor (`roles/deploymentmanager.editor`)
  * Cloud Build Editor (`roles/cloudbuild.builds.editor`)



Before you assign any of these roles to a user, ask yourself:

  * Which resources inside and outside the current Google Cloud project could the user gain access to by impersonating the service account?
  * Is this level of access justified?
  * Are there sufficient protections in place that control under which circumstances the user can impersonate the service account?



Don't assign the role if you can't confirm all questions. Instead, consider giving the user a different, less privileged service account.

### Avoid letting users change the allow policies of more-privileged service accounts

Which users are allowed to use or impersonate a service account is captured by the service account's allow policy. The allow policy can be modified or extended by users who have the `iam.serviceAccounts.setIamPolicy` permission on the particular service account. Roles that contain that permission include:

  * Owner (`roles/owner`)
  * Security Admin (`roles/iam.securityAdmin`)
  * Service Account Admin (`roles/iam.serviceAccountAdmin`)



Roles that include the `iam.serviceAccounts.setIamPolicy` permission give a user full control over a service account:

  * The user can grant themselves permission to impersonate the service account, which gives the user the ability to access the same resources as the service account.
  * The user can grant other users the same or a similar level of access to the service account.



Before you assign any of these roles to a user, ask yourself which resources inside and outside the current Google Cloud project the user could gain access to by impersonating the service account. Don't let a user [change the allow policy](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access) of a service account if the service account has more privileges than the user.

### Don't let users create or upload service account keys

[Service account keys](https://docs.cloud.google.com/iam/docs/creating-managing-service-account-keys) let applications or users authenticate as a service account. Unlike other forms of service account impersonation, using a service account key doesn't require any previous form of authentication–anyone who possesses a service account key can use it.

The net effect of using a service account key to authenticate is similar to the effect of service account impersonation. If a user has access to a service account key, or give them permission to create a new service account key, the user can authenticate as the service account and access all resources that service account can access.

[Creating](https://docs.cloud.google.com/iam/docs/creating-managing-service-account-keys#creating_service_account_keys) or [uploading](https://docs.cloud.google.com/iam/docs/keys-upload) a service account key requires the `iam.serviceAccountKeys.create` permission, which is included in the Service Account Key Admin (`roles/iam.serviceAccountKeyAdmin`) and Editor (`roles/editor`) roles.

Before you assign any role that includes the `iam.serviceAccountKeys.create` permission to a user, ask yourself which resources inside and outside the current Google Cloud project the user could gain access to by impersonating the service account. Don't let a user create service account keys for service accounts that have more privileges than they do.

If your Google Cloud project doesn't require service account keys at all, apply the [Disable service account key creation](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-service-accounts#disable_service_account_key_creation) and [Disable service account key upload](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-service-accounts#disable_service_account_key_upload) organization policy constraints to the Google Cloud project or the enclosing folder. These constraints prevent all users from creating and uploading service account keys, including those with `iam.serviceAccountKeys.create` permission on a service account.

**Note** : If your organization was created on or after May 3, 2024, these constraints are enforced by default. 

### Don't grant access to service accounts at the Google Cloud project or folder level

Service accounts are resources and part of the [resource hierarchy](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy). You can therefore manage access to service accounts at any of the following levels:

  * The individual service account
  * The enclosing Google Cloud project
  * A folder in the Google Cloud project's ancestry
  * The organization node



Managing access at the Google Cloud project level or a higher level of the resource hierarchy can help reduce administrative overhead, but can also lead to over-granting of privileges. For example, if you grant a user the Service Account Token Creator role in a Google Cloud project, the user can impersonate any service account in the Google Cloud project. Being able to impersonate any service account implies that the user can potentially gain access to all resources that those service accounts can access, including resources outside that Google Cloud project.

To avoid such over-granting, don't manage access to service accounts at the Google Cloud project or folder level. Instead, individually manage access for each service account.

### Don't run code from less protected sources on compute resources that have a privileged service account attached

When you attach a service account to a compute resource, such as a VM instance, processes running on that resource can use the metadata server to [request access tokens and ID tokens](https://docs.cloud.google.com/compute/docs/storing-retrieving-metadata#default). These tokens let the process authenticate as the service account and access resources on its behalf.

By default, access to the metadata server isn't restricted to specific processes or users. Instead, any code that is executed on the compute resource can access the metadata server and obtain an access token. Such code might include:

  * The code of your application.
  * Code submitted by end users, if your application permits any server-side script evaluation.
  * Code read from a remote source repository, if the compute resource is part of a CI/CD system.
  * [Startup and shutdown scripts](https://docs.cloud.google.com/compute/docs/startupscript) served by a Cloud Storage bucket.
  * [Guest policies](https://docs.cloud.google.com/compute/docs/os-config-management/create-guest-policy) distributed by VM Manager.



If code is submitted by users or is read from a remote storage location, you must ensure that it's trustworthy and that the remote storage locations are at least as well secured as the attached service account. If a remote storage location is less well protected than the service account, a bad actor might be able to escalate their privileges. They could do so by injecting malicious code that uses the service account's privileges into that location.

### Limit shell access to VMs that have a privileged service account attached

Some compute resources support interactive access and allow users to obtain shell access to the system. For example:

  * Compute Engine lets you use SSH or RDP to log in to a VM instance.
  * Google Kubernetes Engine lets you use [kubectl exec](https://kubernetes.io/docs/tasks/debug/debug-application/get-shell-running-container/) to run a command or start a shell in a Kubernetes container.



If a VM instance has a privileged service account attached, then any user with shell access to the system can authenticate and access resources as the service account. To prevent users from abusing this capability to escalate their privileges, you must ensure that shell access is at least as well secured as the attached service account.

For Linux instances, you can enforce that SSH access is more restrictive than access to the attached service account by using OS Login: To connect to a VM instance that has OS Login enabled, a user must not only be [allowed to use OS Login](https://docs.cloud.google.com/compute/docs/instances/managing-instance-access#configure_users), but must also have the `iam.serviceAccounts.actAs` permission on the attached service account.

The same level of access control doesn't apply to VM instances that use metadata-based keys or to Windows instances: Publishing an [SSH key to metadata](https://docs.cloud.google.com/compute/docs/instances/adding-removing-ssh-keys) or [requesting Windows credentials](https://docs.cloud.google.com/compute/docs/instances/windows/creating-passwords-for-windows-instances) requires access to the VM instance's metadata and the `iam.serviceAccounts.actAs` permission on the attached service account. However, after the SSH key has been published or the Windows credentials have been obtained, subsequent logins are not subject to any additional IAM permission checks.

Similarly, if a VM instance uses a custom Linux pluggable authentication module for authentication, or is a member of an Active Directory domain, it's possible that users who wouldn't otherwise have permission to authenticate as the service account are allowed to log in. For more information, see [Best practices for running Active Directory on Google Cloud](https://docs.cloud.google.com/compute/docs/instances/windows/best-practices#ad-interference).

Particularly for VM instances that don't use OS Login, consider gating shell access by [Identity-Aware Proxy](https://docs.cloud.google.com/iap/docs/using-tcp-forwarding). Only grant the IAP-Secured Tunnel User role (`roles/iap.tunnelResourceAccessor`) to users who should be allowed to authenticate as the service account attached to the VM instance.

### Limit metadata server access to selected users and processes

When you attach a service account to a VM instance, workloads deployed on the VM can access the metadata server to request tokens for the service accounts. By default, access to the metadata server isn't limited to any specific process or user on the VM. Even processes running as a low-privilege user, such as `nobody` on Linux or `LocalService` on Windows, have full access to the metadata server and can obtain tokens for the service account.

To limit metadata server access to specific users, configure the guest operating system's host firewall to only allow these users to open outbound connections to the metadata server.

On Linux, you can use the `--uid-owner` and `--gid-owner` options to set up an `iptables` rule that only applies to specific users or groups. On Windows, the `Set-NetFirewallSecurityFilter` command lets you customize a firewall rule so that it applies to selected users or groups.

## Protect against information disclosure threats

**Best practices** :

Avoid disclosing confidential information in service account email addresses.  


### Avoid disclosing confidential information in service account email addresses

To grant a service account access to a resource in another Google Cloud project, you can add a role binding to the resource's allow policy. Like the resource itself, the allow policy is part of the other Google Cloud project and its visibility is also controlled by that other Google Cloud project.

Viewing allow policies is typically not considered a privileged operation. Many roles include the required `*.getIamPolicy` permission, including the basic Viewer role.

A user who can view an allow policy can also see the email addresses of principals who have been granted access to the resource. In the case of service accounts, email addresses can provide hints to bad actors.

For example, an allow policy might include a binding for a service account with the email address `jenkins@deployment-project-123.iam.gserviceaccount.com`. To a bad actor, this email address not only reveals that there is a Google Cloud project with ID `deployment-project-123`, but also that the Google Cloud project runs a Jenkins server. By choosing a more generic name such as `deployer@deployment-project-123.iam.gserviceaccount.com`, you avoid disclosing information about the type of software that you're running in `deployment-project-123`.

If you grant a service account access to resources in a Google Cloud project that has less tightly controlled access (such as a sandbox or a development Google Cloud project), make sure that the service account's email address doesn't disclose any information. In particular, don't disclose information that is confidential or that could provide hints to attackers.

## Protect against non-repudiation threats

Whenever you notice suspicious activity affecting one of your resources on Google Cloud, Cloud Audit Logs are an important source of information to find out when the activity happened and which users were involved.

Whenever Cloud Audit Logs indicate that activity was performed by a service account, that information alone might not be sufficient to reconstruct the full chain of events. In these cases, you must also be able to find out which user or application caused the service account to perform the activity.

This section contains best practices that can help you maintain a non-repudiable audit trail.

**Best practices** :

Use service account keys only when there is no viable alternative.  
Enable data access logs for IAM APIs.  
Ensure that CI/CD history can be correlated with Cloud Audit Logs.  
Create custom log entries for individual users of an application.  


### Use service account keys only when there is no viable alternative

If you can't use more secure authentication methods, you might need to create a service account key for the application. However, authenticating with a service account key introduces a non-repudiation threat. Cloud Audit Logs creates a log when a service account modifies a resource, but if the service account is authenticated with a service account key, there is no reliable way to tell who used the key. In comparison, authenticating as a service account by [impersonating the service account with user credentials](https://docs.cloud.google.com/iam/docs/audit-logging/examples-service-accounts#auth-as-service-account) logs the principal who acted as the service account.

We recommend preventing the creation of service account keys by applying the [Disable service account key creation](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-service-accounts#disable_service_account_key_creation) organization policy constraint to the Google Cloud project or the enclosing folder. If you must use service account keys for a scenario that can't be addressed with any of the recommended alternatives, grant an exception to the policy constraint, as narrowly as possible, and review [best practices for managing service account keys](https://docs.cloud.google.com/iam/docs/best-practices-for-managing-service-account-keys).

**Note** : If your organization was created on or after May 3, 2024, these constraints are enforced by default. 

### Enable data access logs for IAM APIs

To help you identify and understand service account impersonation scenarios, services such as Compute Engine include a `serviceAccountDelegationInfo` section in Cloud Audit Logs. This section indicates [whether the service account was being impersonated, and by which user](https://docs.cloud.google.com/iam/docs/audit-logging/examples-service-accounts#auth-short-lived-credentials).

Not all services include impersonation details in their Cloud Audit Logs. To record all impersonation events, you must also [enable data access logs](https://docs.cloud.google.com/logging/docs/audit/configure-data-access) for the following APIs:

  * **Identity and Access Management (IAM) API** in all Google Cloud projects that contain service accounts
  * **Security Token Service API** in all Google Cloud projects that contain workload identity pools



By enabling these logs, you make sure that an entry is added to the Cloud Audit Logs whenever a user requests an access token or an ID token for a service account.

### Ensure that CI/CD history can be correlated with Cloud Audit Logs

Service accounts are commonly used by CI/CD systems to perform deployments after a code change has been successfully verified and approved for deployment. Typically, CI/CD systems maintain a history of events that lead to a deployment. This history might include the IDs of the corresponding code reviews, commits, and pipeline runs, and information about who approved the deployment.

If a deployment modifies any resources on Google Cloud, then these changes are tracked in the [Cloud Audit Logs](https://docs.cloud.google.com/logging/docs/audit) of the respective resources. Cloud Audit Logs contain information about the user or service account that initiated the change. But in a deployment triggered by a CI/CD system, the service account itself is often insufficient to reconstruct the entire chain of events that led to the change.

To establish a consistent audit trail across your CI/CD system and Google Cloud, you must ensure that Cloud Audit Logs records can be correlated with events in the CI/CD system's history. If you encounter an unexpected event in the Cloud Audit Logs, you can then use this correlation to determine whether the change was indeed performed by the CI/CD system, why it was performed, and who approved it.

Ways to establish a correlation between Cloud Audit Logs records and events in the CI/CD system's history include:

  * Log API requests performed by each CI/CD pipeline run.
  * Whenever the API returns an operation ID, record the ID in the CI/CD system's logs.
  * Add a `X-Goog-Request-Reason` [HTTP header](https://docs.cloud.google.com/apis/docs/system-parameters#definitions) to API requests and pass the ID of the CI/CD pipeline run. Terraform can automatically add this header if you specify a [request reason](https://registry.terraform.io/providers/hashicorp/google/latest/docs/guides/provider_reference#request_reason).

Alternatively, embed the information in the `User-Agent` header so that it is captured in Cloud Audit Logs.




To help ensure non-repudiability, configure log files and commit histories so that they are immutable and a bad actor can't retroactively conceal their traces.

### Create custom log entries for individual users of an application

Service accounts are also useful for applications in which a user authenticates with a custom authentication scheme, then indirectly accesses Google Cloud resources. These applications can confirm that the user is authenticated and authorized, then use a service account to authenticate to Google Cloud services and access resources. However, Cloud Audit Logs will log that the service account accessed a resource, not which user was using your application.

To help trace that access back to the user, design application logic to write a custom log entry each time a user accesses a resource and correlate the custom log entries with Cloud Audit Logs.

## What's next

  * Understand [best practices for managing service account keys](https://docs.cloud.google.com/iam/docs/best-practices-for-managing-service-account-keys).
  * Review our [best practices for using service accounts in deployment pipelines](https://docs.cloud.google.com/iam/docs/best-practices-for-using-service-accounts-in-deployment-pipelines).
  * Learn about [best practices for using Workload Identity Federation](https://docs.cloud.google.com/iam/docs/best-practices-for-using-workload-identity-federation).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
