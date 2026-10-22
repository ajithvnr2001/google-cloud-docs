---
url: https://docs.cloud.google.com/docs/security/data-loss-prevention/revoking-user-access/
title: Revoke access to a Google Cloud project \u00a0|\u00a0 Security \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:23:52.795799+00:00
---

# Revoke access to a Google Cloud project  |  Security  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/docs/security/data-loss-prevention/revoking-user-access/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Guides ](https://docs.cloud.google.com/docs/security/overview/whitepaper)



Send feedback 

#  Revoke access to a Google Cloud project Stay organized with collections  Save and categorize content based on your preferences. 

This document describes best practices, scenarios, and procedures for revoking a user's access to a Google Cloud project. Because each business has different policies and workloads, we recommend that you use this document to come up with your own policies and procedures that let you revoke access consistently and in a timely manner.

When an employee leaves your company, your engagement with a contractor ends, or a collaborator moves on to other projects, there are a few things you should do to revoke unneeded access to your cloud resources.

Some of these processes are optional. You should determine which of these steps to execute depending on your security needs, products in use, and trust in the person whose access is being revoked.

## Best practices for setting up your project

You can improve your project's ability to efficiently revoke user access by making thoughtful choices at setup time.

### Federate user accounts with your existing identity provider

When you federate user accounts with your existing identity provider, make sure that you propagate user suspension and deletion events. With propagation, when you suspend or remove a user account from your identity provider, the user also loses access to Google Cloud resources.

For more information, see [Best practices for federating Google Cloud with an external identity provider](https://docs.cloud.google.com/architecture/identity/best-practices-for-federating).

For more identity-related best practices, see [Best practices for planning accounts and organizations](https://docs.cloud.google.com/architecture/identity/best-practices-for-planning).

For information about Workforce Identity Federation, see [Workforce Identity Federation](https://docs.cloud.google.com/iam/docs/workforce-identity-federation).

### Consider using Google Groups to manage access to project resources

Google Groups let you organize users based on their team membership, access requirements, or other criteria. After you create Google Groups, you can assign access to Google Cloud projects and resources based on group membership. When a user moves to another team or job function, you can move the user account to another group, which automatically removes the access that was granted by allow policies to the previous group.

Using Google Groups isn't appropriate in all circumstances. For example, you shouldn't use groups that are based only on your business's organization structure to manage access. For best practices on group usage, see [Best practices for using Google Groups](https://docs.cloud.google.com/iam/docs/groups-best-practices).

For more information, see [Managing groups in the Google Cloud console](https://docs.cloud.google.com/iam/docs/groups-in-cloud-console) and [Create a group in your organization](https://support.google.com/cloudidentity/answer/9400082)

### Use OS Login

Use OS Login instead of metadata-based SSH keys so that the user's authorized keys are linked to their Google identity. When you remove a user account, the authorized keys and access to VMs are revoked automatically. For more information, see [Use OS Login to ensure continuous access evaluation against IAM policies](https://docs.cloud.google.com/compute/docs/connect/ssh-best-practices/login-access#use-oslogin).

For instructions, see [Set up OS Login](https://docs.cloud.google.com/compute/docs/oslogin/set-up-oslogin).

### Restrict access from external user accounts

Don't grant external users access to the project because you can't control the lifecycle for these user accounts. To restrict external users, use the [`iam.allowedPolicyMemberDomains`](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-domains) list constraint.

For instructions, see [Restricting identities by domain](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-domains).

### Use authentication proxies with databases

Authentication proxies let you connect the lifecycle of database credentials to the lifecycle of a Google identity. When you suspend or delete a user account in Cloud Identity or Google Workspace, access to databases is automatically revoked.

For more information, see [Cloud SQL Auth proxy](https://docs.cloud.google.com/sql/docs/mysql/sql-proxy) and [AlloyDB for PostgreSQL Auth proxy](https://docs.cloud.google.com/alloydb/docs/auth-proxy/overview).

### Prepare for credential rotation

Design your projects and resources to allow for non-disruptive rotation of project-level credentials. These are secrets tied to the project itself, such as service account keys, OAuth client secrets, and application-specific secrets like database root passwords. For more information, see [Respond to compromised Google Cloud credentials](https://docs.cloud.google.com/docs/security/compromised-credentials).

### Restrict API keys

When creating and managing API keys, restrict the set of web sites, IP addresses, and apps that can use them. A user account with roles like Viewer or [API Keys Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/serviceusage#serviceusage.apiKeysAdmin) can see your project's API keys, so any unrestricted keys must be rotated or deleted in order to revoke billing access. For more information, see [Secure an API key](https://docs.cloud.google.com/docs/authentication/api-keys).

### Monitor access permissions

Carefully tracking access helps mitigate potential access abuse. You can use [IAM role recommender](https://docs.cloud.google.com/policy-intelligence/docs/role-recommendations-overview) to track role usage to help enforce the least privilege principle. In addition, Security Command Center's [Cloud Infrastructure Entitlement Management (CIEM)](https://docs.cloud.google.com/security-command-center/docs/ciem-overview) capabilities let you manage which identities have access to which resources in your deployments and mitigate potential vulnerabilities that result from misconfigurations.

### Use uniform bucket-level access for Cloud Storage

[Uniform bucket-level access](https://docs.cloud.google.com/storage/docs/uniform-bucket-level-access) lets you use IAM alone to manage permissions for your Cloud Storage buckets. Use uniform bucket-level access along with [other access control options](https://docs.cloud.google.com/storage/docs/access-control#additional_access_control_options) to refine who can access the content in your buckets.

### Additional best practices

In addition to the best practices described in this document, review the following best practices:

  * [Best practices for working with service accounts](https://docs.cloud.google.com/iam/docs/best-practices-service-accounts)
  * [Decide the security for your Google Cloud landing zone](https://docs.cloud.google.com/architecture/landing-zones/decide-security)
  * [Verify every access attempt explicitly](https://docs.cloud.google.com/architecture/framework/security/implement-zero-trust#verify_every_access_attempt_explicitly)



## Scenarios for revoking access to Google Cloud projects

If you implemented the best practices listed in Best practices for setting up your project, the following table summarizes how you can revoke access.

Scenario | Revoking access options  
---|---  
An employee leaves your company. | If you set up federation between Cloud Identity or Google Workspace with automatic user provisioning, access revocation can happen automatically.  
  
If you didn't follow best practices and you granted external user identities access to your resources, then you must manually remove the identities from your projects and resources.  
An employee changes their job function. | You remove the employee from the team group.  
A contract engagement ends. | If you set up federation between Cloud Identity or Google Workspace with automatic user provisioning, access revocation can happen automatically.  
  
If you didn't follow best practices and you granted external user identities access to your resources, then you must manually remove the identities from your projects and resources.   
An account was compromised. | For instructions, see [Respond to compromised Google Cloud credentials](https://docs.cloud.google.com/docs/security/compromised-credentials).   
  
## Revoke access

If you've made good choices in project setup, the following processes will be an efficient way to revoke a person's access.

To determine what resources a person has access to, use Policy Analyzer. For instructions, see [Analyze IAM policies](https://docs.cloud.google.com/policy-intelligence/docs/analyze-iam-policies).

### Delete the user account from your identity provider

If the user is leaving your organization, and you've federated Cloud Identity or Google Workspace with your identity provider, with automatic user provisioning, access revocation can happen automatically.

For information about deleting Workforce Identity Federation users, see [Delete Workforce Identity Federation users and their data](https://docs.cloud.google.com/iam/docs/workforce-delete-user-data).

### Revoke workforce user sessions

If you suspect a workforce user's credentials are compromised or if you want to immediately terminate active sessions before the deletion completes, then revoke the user's sessions.

For more information, see [Revoke Workforce Identity Federation user sessions](https://docs.cloud.google.com/iam/docs/workforce-revoke-sessions). 

### Move the account to another group

If the user is changing roles, remove the user account from their current Google Groups. If you've federated Cloud Identity or Google Workspace with your identity provider to manage group membership, access revocation can happen automatically.

For more information, see [Viewing and editing group details](https://docs.cloud.google.com/iam/docs/groups-in-cloud-console#viewing-editing-details).

### Remove the user account from IAM allow policies

To remove a user account from project-level allow policies, do the following:

  1. In the Google Cloud console, go to the **IAM permissions** page.

[IAM permissions](https://console.cloud.google.com/iam-admin)

  2. Select the project that you want to remove a user account from.

  3. Click the checkbox next to the row that contains the user account you want removed from the member list, then click **Remove**.




To verify other locations where the allow policy can be set, including folders, organization, or individual resources, see Verify permissions were removed.

### Rotate project credentials

If the person whose access you are revoking had access to project-level credentials, such as service account keys, OAuth client secrets, or API keys, you must rotate those credentials.

**Note:** If you have applications and services depending on project-level secrets, be sure to update them after rotating credentials.

#### Rotate service account keys

If you use service account keys to authenticate to a service account, you must rotate the keys. In addition, consider if the person might have had access to service account keys somewhere outside of Google Cloud tools, such as your source code repository or application configurations.

**Note:** Service account keys are a security risk if not managed correctly. You should [ choose a more secure alternative to service account keys](https://docs.cloud.google.com/docs/authentication#auth-decision-tree) whenever possible. If you must authenticate with a service account key, you are responsible for the security of the private key and for other operations described by [ Best practices for managing service account keys](https://docs.cloud.google.com/iam/docs/best-practices-for-managing-service-account-keys). If you are prevented from creating a service account key, service account key creation might be disabled for your organization. For more information, see [ Managing secure-by-default organization resources](https://docs.cloud.google.com/resource-manager/docs/secure-by-default-organizations). 

If you acquired the service account key from an external source, you must validate it before use. For more information, see [ Security requirements for externally sourced credentials](https://docs.cloud.google.com/docs/authentication/external/externally-sourced-credentials). 

  1. In the Google Cloud console, go to the **API credentials** page.

[API credentials](https://console.cloud.google.com/apis/credentials)

  2. Click the name of the service account that you want to modify.

  3. Under the **Key** tab, click **Add Key**.

  4. Click **Create new key**.

  5. Choose the **Key type** you want to create. In most situations, **JSON** is recommended, but **P12** is available for backwards compatibility with code that depends on it.

  6. Click **Create**. A file containing the new key will be automatically downloaded through your browser. Deploy this key to any applications that need it.

  7. After confirming the new key works as expected, return to the credentials page and delete the old key associated with that service account.




#### Rotate OAuth client ID secrets

OAuth client ID secrets don't provide any direct access to your project. However, if an attacker knows the OAuth client ID secret, they can spoof your application and request access to your users' Google Accounts from a malicious application.

You might need to rotate OAuth client ID secrets if the person whose access is being revoked ever had access to the secret, including in your source code repository, application configurations, or through IAM roles.

**Note:** These steps break the OAuth clients until you deploy the new client ID secret.

  1. In the Google Cloud console, go to the **API credentials** page.

[API credentials](https://console.cloud.google.com/apis/credentials)

  2. Click the name of the OAuth 2.0 client ID that you want to modify.

  3. On the **Client ID** page, click **Reset secret**.

  4. Click **Reset** in the confirmation dialog to immediately revoke the old secret and set a new one. Note that any active users will need to reauthenticate upon their next request.

  5. Deploy the new secret to any applications that need it.




#### Rotate API keys

API keys don't provide access to your project or your users' data, but they control who Google bills for API requests. A user account with roles like Viewer or [API Keys Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/serviceusage#serviceusage.apiKeysAdmin) can see your project's API keys. If you have any unrestricted keys, you need to delete or regenerate them when revoking someone's access to your project.

  1. In the Google Cloud console, go to the **API credentials** page.

[API credentials](https://console.cloud.google.com/apis/credentials)

  2. Click the name of the API key that you want to modify.

  3. Click **Regenerate key**.

  4. A dialog will display the newly created key. Deploy this key to any applications using the key that you want to replace.

  5. After confirming that your applications are working as expected with the new key, return to the credentials page and delete the old unrestricted key.




### Revoke access to VMs

If the person whose access you are revoking doesn't have login access to any of your project VMs, you can skip this step.

**Note:** If someone has ever had root access to a VM, it's difficult to ensure that their access has been terminated by removing their associated user account. That person might be able to sign in as a different user, use personal public keys to access other accounts, or run processes as other users. The most secure procedure is to recreate VMs from a known good image.

  1. Remove all [project-level SSH keys](https://docs.cloud.google.com/compute/docs/connect/restrict-ssh-keys#remove-project-key) that the person had access to.

  2. On each VM where the person had SSH access, [remove any instance-level keys](https://docs.cloud.google.com/compute/docs/connect/restrict-ssh-keys#remove-instance-key).

  3. Remove the person's account from any VMs they had login access to.

  4. Check for suspicious applications the person might have installed to provide backdoor access to the VM. If you are uncertain about the security of any code running on the VM, recreate it and redeploy the applications you need from source.

  5. Verify that the VM firewall settings haven't been changed from your planned or expected configuration.

  6. If you create new VMs from custom base images, verify that the base images haven't been modified in a way that would compromise the security of new VMs.




### Revoke access to databases

If your project doesn't use Cloud SQL or AlloyDB for PostgreSQL resources, you can skip this step.

To revoke access to a Cloud SQL database, complete the following:

  1. In the Google Cloud console, go to the **SQL instances** page.

[SQL instances](https://console.cloud.google.com/sql/instances)

  2. Click the instance ID of the database you want to revoke access to.

  3. In the left menu, click **Connections**.

  4. Confirm that the list of IP addresses under **Authorized networks** and list of apps under **App Engine authorization** match what you expect. If the person whose access you're trying to revoke has access to networks or applications listed here, they can access this database.

  5. In the left menu, click **Users**.

  6. Delete or change the password for any user accounts that the person had access to. Be sure to update any applications that depend on those user accounts.




To revoke access to an AlloyDB for PostgreSQL database, see [Remove an IAM user or service account from a cluster](https://docs.cloud.google.com/alloydb/docs/manage-iam-authn#delete-user).

### Redeploy App Engine

By default, App Engine apps have access to a service account that is an editor on the associated project. App Engine request handlers can do things like create new VMs and read or modify data in Cloud Storage. Someone with the ability to deploy code to App Engine could use this service account to open a backdoor into your project. If you're concerned about the code integrity of your deployed apps, you might want to redeploy them (including any modules) with a known-good image from your version control system.

### Verify permissions were removed

You can verify permissions at the organization level, the project level, or using Policy Analyzer.

To find resources that a particular user might have access to at the organization level, use the [`search-all-iam-policies` method](https://docs.cloud.google.com/sdk/gcloud/reference/asset/search-all-iam-policies) in Google Cloud CLI. For example, to determine whether a user has access to your resources, run:
    
    
    gcloud asset search-all-iam-policies --scope='organizations/ORGANIZATION_ID --query='policy:IDENTITY'
    

Where:

  * `ORGANIZATION_ID` is your organization number.
  * `IDENTITY` is the user's identity, such as an email address.



To verify permissions on a project, see [Permissions a principal has on a project](https://docs.cloud.google.com/asset-inventory/docs/search-allow-policies#permissions_a_principal_has_on_a_project).

To verify permissions using Policy Analyzer, see [Determine which resources a principal can access](https://docs.cloud.google.com/policy-intelligence/docs/analyze-iam-policies#resource-query).

## What's next

  * See [Respond to compromised Google Cloud credentials](https://docs.cloud.google.com/docs/security/compromised-credentials).

  * Learn more [Best practices for protecting developer credentials](https://docs.cloud.google.com/docs/security/bps-for-protecting-developer-credentials).

  * Create a [deny policy](https://docs.cloud.google.com/iam/docs/deny-overview) to specify which permissions the user can't access any longer.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
