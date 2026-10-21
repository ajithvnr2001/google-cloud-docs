---
url: https://docs.cloud.google.com/docs/enterprise/advanced-production/
title: Create an Advanced production foundation \u00a0|\u00a0 Get started \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:24:02.490803+00:00
---

# Create an Advanced production foundation  |  Get started  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/docs/enterprise/advanced-production/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Get started ](https://docs.cloud.google.com/docs/get-started)
  * [ Guides ](https://docs.cloud.google.com/docs/overview)



Send feedback 

#  Create an Advanced production foundation Stay organized with collections  Save and categorize content based on your preferences. 

A **foundation** includes fundamental settings that help you organize, manage, and maintain Google Cloud resources. Create an **Advanced production foundation** to control detailed settings in each phase of the Google Cloud Setup process, including detailed security settings and networking settings.

This document outlines steps and background information to help you configure an advanced production foundation, including the following phases:

  * Establish your organization, administrators, and billing: Set up the top-level node of your hierarchy, create initial administrator users and assign access, and connect your payment method.

  * Create an initial architecture: Select an initial folder and project structure, apply security settings, configure logging and monitoring, and set up your network.

  * Deploy your settings: Your initial architecture choices are compiled in Terraform configuration files. You can deploy through the Google Cloud console, or download the files to customize and iterate using your own workflow. After you deploy, choose a support plan.




****

## Establish your organization, administrators, and billing

###  Organization 

An organization resource in Google Cloud represents your business, and serves as the top level node of your hierarchy. To create your organization, you set up a Google identity service and associate it with your domain. When you complete this process, an organization resource is automatically created.

For an overview of the organization resource, see the following:

  * [Manage organization resources](https://docs.cloud.google.com/resource-manager/docs/creating-managing-organization).
  * [Best practices for planning accounts and organizations](https://docs.cloud.google.com/architecture/identity/best-practices-for-planning).



### Who performs this task

The following two administrators perform this task:

  * An identity administrator responsible for assigning role-based access. You assign this person as the Cloud Identity super administrator. For more information about the super administrator user, see [Prebuilt administrator roles](https://support.google.com/cloudidentity/answer/2405986).

  * A domain administrator with access to the company's domain host. This person edits your domain settings, such as DNS configurations, as part of the domain verification process.




### What you do in this task

  * If you haven't already, set up Cloud Identity, where you create a [managed user account](https://docs.cloud.google.com/architecture/identity/overview-google-authentication#managed_user_account) for your super administrator user.
  * Link Cloud Identity to your domain (such as _example.com_).
  * Verify your domain. This process creates the root node of your resource hierarchy, known as the [organization resource](https://docs.cloud.google.com/resource-manager/docs/creating-managing-organization).



### Why we recommend this task

You must configure the following as part of your Google Cloud foundation:

  * A Google identity service to centrally manage identities.
  * An organization resource to establish the root of your hierarchy and access control.



### Google identity service options

You use one or both of the following Google identity services to administer credentials for Google Cloud users:

  * Cloud Identity: Centrally manages users and groups. You can federate identities between Google and other identity providers. For more information, see [Overview of Cloud Identity](https://docs.cloud.google.com/identity/docs/overview).
  * Google Workspace: Manages users and groups, and provides access to productivity and collaboration products like Gmail and Google Drive. For more information, see [Google Workspace](http://workspace.google.com).



For detailed information about identity planning, see [Planning the onboarding process for your corporate identities](https://docs.cloud.google.com/architecture/identity/overview-assess-and-plan).

### Before you begin

To understand how to manage a super administrator account, see [Super administrator account best practices](https://docs.cloud.google.com/resource-manager/docs/super-admin-best-practices).

### Configure an identity provider and verify your domain

The steps you complete in this task depend on whether you are a new or existing customer. Identify the option that fits your needs:

  * **New customer** : Set up Cloud Identity, verify your domain, and create your organization.

  * **Existing Google Workspace customer** : Use Google Workspace as your identity provider for users who access Google Workspace and Google Cloud. If you plan to create users who only access Google Cloud, enable Cloud Identity.

  * **Existing Cloud Identity customer** : Verify your domain, make sure your organization was created, and confirm that Cloud Identity is enabled.




### New customer

### New Customer: Set up Cloud Identity and create your organization

To create your organization resource, you first set up Cloud Identity, which helps you manage users and groups that access Google Cloud resources.

In this task, you set up Cloud Identity [free edition](https://support.google.com/cloudidentity/answer/7295541).You can enable Cloud Identity premium edition after you complete your initial setup. For more information, see [Compare Cloud Identity features and editions](https://support.google.com/cloudidentity/answer/7431902).

  1. Identify the person who serves as the Cloud Identity administrator (also known as the super administrator) in your organization

Record the administrator's username in the following format: admin-_name_ @example.com. For example, admin-maria@example.com. Specify this username when you create your first administrator user.

  2. To complete the setup process and create the super administrator account, go to the [Cloud Identity signup page](https://workspace.google.com/signup/gcpidentity/welcome).

If you get an error when you set up the administrator account, see ['Google Account already exists' error](https://support.google.com/a/answer/1275816).




#### Verify your domain and create your organization resource

Cloud Identity requires you to verify that you are your domain owner. Once the verification is complete, your Google Cloud [organization resource](https://docs.cloud.google.com/resource-manager/docs/creating-managing-organization) is automatically created for you.

  1. Make sure you created a super administrator account when you configured your identity provider.

  2. Verify your domain in Cloud Identity. As you complete the verification process, note the following:

     * When prompted, don't click Create new users. You will create new users in a later task.
     * If you are unable sign up your domain, see [Can't sign up my domain for a Google service](https://support.google.com/a/answer/80610).
     * The verification may require several hours to process.

For steps to verify your domain, see [Verify your domain](https://support.google.com/cloudidentity/answer/7331243).

  3. When you finish the domain verification steps, click **Set up Google Cloud console now**.

  4. Sign in to the Google Cloud console as the super administrator user using the email address you specified. For example, admin-maria@example.com.

  5. Go to **Google Cloud Setup: Organization**. Your organization is created automatically.

[Go to Organization](https://console.cloud.google.com/cloud-setup/organization)

  6. Select your organization from the **Select from** drop-down list at the top of the page.




#### Request additional Cloud Identity user licenses

Cloud Identity free edition includes an allotment of user licenses. For steps to view and request licenses, see [Your Cloud Identity free edition user cap](https://support.google.com/cloudidentity/answer/7295541).

### Workspace customer

### Existing Google Workspace customer: Verify your domain and enable Cloud Identity

If you are an existing Google Workspace customer, verify your domain, make sure that your organization resource is automatically created, and optionally enable Cloud Identity.

  1. To verify your domain in Google Workspace, see [Verify your domain](https://support.google.com/a/answer/60216). As you complete the verification process, note the following:

     * When prompted, don't click Create new users. You will create new users in a later task.
     * If you are unable sign up your domain, see [Can't sign up my domain for a Google service](https://support.google.com/a/answer/80610).
     * The verification may require several hours to process.
  2. Sign in to the Google Cloud console as the super administrator user.

  3. Go to **Google Cloud Setup: Organization**.

[Go to Organization](https://console.cloud.google.com/cloud-setup/organization)

  4. Select **I'm a current Google Workspace customer**.

  5. Make sure that your organization name is displayed in the **Organization** list.

  6. If you want to create users who access Google Cloud, but don't receive Google Workspace licenses, do the following.

     1. In Google Workspace, [Enable Cloud Identity](https://support.google.com/cloudidentity/answer/7384506).

     2. When you set up Cloud Identity, [Disable automatic Google Workspace licensing](https://support.google.com/cloudidentity/answer/7338389).




### Cloud Identity customer

### Existing Cloud Identity customer: Verify your domain

If you are an existing Cloud Identity customer, make sure you have verified your domain, and that your organization resource was automatically created.

  1. To make sure that you have verified your domain, see [Verify your domain](https://support.google.com/cloudidentity/answer/7331243). As you complete the verification process, note the following:

     * When prompted, don't click Create new users. You will create new users in a later task.
     * If you are unable sign up your domain, see [Can't sign up my domain for a Google service](https://support.google.com/a/answer/80610).
     * The verification may require several hours to process.
  2. Sign in to the Google Cloud console as the super administrator user.

  3. Go to **Google Cloud Setup: Organization**.

[Go to Organization](https://console.cloud.google.com/cloud-setup/organization)

  4. Select **I'm a current Cloud Identity customer**.

  5. Make sure that your organization name is displayed in the **Organization** list.

  6. Make sure that Cloud Identity is enabled in [Google Admin console: Subscriptions](https://admin.google.com/ac/billing/subscriptions). Sign in as a super administrator user.




### What's next

Create groups and add members.

###  Users and groups 

In this task, you set up identities, users, and groups to manage access to Google Cloud resources.

For more information on access management on Google Cloud, see the following:

  * [Identity and Access Management (IAM) overview](https://docs.cloud.google.com/iam/docs/overview).
  * For best practices, see [Use IAM securely](https://docs.cloud.google.com/iam/docs/using-iam-securely).



### Who performs this task

You can perform this task if you have one of the following:

  * The Google Workspace or Cloud Identity super administrator that you created in the Organization task.
  * One of the following IAM roles: 
    * Organization Administrator (`roles/resourcemanager.organizationAdmin`).
    * Workforce Identity Pool Admin (`roles/iam.workforcePoolAdmin`).



### What you do in this task

  * Connect to Cloud Identity or your external identity provider (IdP).

  * Create administrative groups and users that will perform the remainder of the Google Cloud Setup steps. You grant access to these groups in a later task.




### Why we recommend this task

This task helps you implement the following security best practices:

  * [Principle of least privilege](https://en.wikipedia.org/wiki/Principle_of_least_privilege): Give users the minimum permissions required to perform their role, and remove access as soon as it is no longer needed.

  * [Role-based access control (RBAC)](https://en.wikipedia.org/wiki/Role-based_access_control): Assign permissions to groups of users according to their job role. Do not add permissions to individual user accounts.




You can use groups to efficiently apply IAM roles to a collection of users. This practice helps you simplify access management.

### Select an identity provider

You can use one of the following to manage users and groups, and connect them to Google Cloud:

  * _Google Workspace or Cloud Identity_ : You create and manage users and groups in Google Workspace or Cloud Identity. You can choose to synchronize with your external identity provider later.
  * _Your external identity provider, such as Microsoft Entra ID or Okta_ : You create and manage users and groups in your external identity provider. You then connect your provider to Google Cloud to enable single-sign-on.



To select your identity provider, do the following:

  1. Sign in to the Google Cloud console as one of the users you identified in Who performs this task.

  2. Go to **Google Cloud Setup: Users & groups**.

[Go to Users & groups](https://console.cloud.google.com/cloud-setup/users-groups)

  3. Review the task details and click **Continue identity setup**.

  4. On the **Select your identity provider** page, select one of the following to begin a guided setup:

     * **Use Google to centrally manage Google Cloud users** : Use Google Workspace or Cloud Identity to provision and manage users and groups as a super administrator of your verified domain. You can later synchronize with your external identity provider.
     * **Microsoft Entra ID (Azure AD)** : Use OpenID Connect to configure a connection to Microsoft Entra ID.
     * **Okta** : Use OpenID Connect to configure a connection to Okta.
     * **OpenID Connect** : Use the OpenID protocol to connect to a compatible identity provider.
     * **SAML** : Use the SAML protocol to connect to a compatible identity provider.
     * **Skip setting up an external IdP for now** : If you have an external identity provider and you're not ready to connect it to Google Cloud, You can create users and groups in Google Workspace or Cloud Identity.
  5. Click **Continue**.

  6. See one of the following for next steps:

     * Create users and groups in Cloud Identity
     * Connect your external identity provider to Google Cloud



### Create users and groups in Cloud Identity

If you don't have an existing identity provider, or if you're not ready to connect your identity provider to Google Cloud, you can create and manager users and groups in Cloud Identity or Google Workspace. To create users and groups, you do the following:

  * Create a group for each recommended administrative function, including organization, billing, and network administration.
  * Create [managed user](https://docs.cloud.google.com/architecture/identity/overview-google-authentication#managed_user_account) accounts for administrators.
  * Assign users to administrative groups that correspond to their responsibilities.



#### Before you begin

  * Find and migrate users that already have Google Accounts. For detailed information, see [Add users with unmanaged accounts](https://support.google.com/a/topic/7042002).

  * You must be a super administrator.




#### Create administrative groups

A group is a named collection of Google Accounts and service accounts. Each group has a unique email address, such as _gcp-billing-admins@example.com_. You create groups to manage users and apply IAM roles at scale.

The following groups are recommended to help you administer your organization's core functions and complete the Google Cloud Setup process.

**Group** | **Description**  
---|---  
`gcp-organization-admins` | Administer all organization resources. Assign this role only to your most trusted users.   
`gcp-billing-admins` | Set up billing accounts and monitor usage.   
`gcp-network-admins` | Create Virtual Private Cloud networks, subnets, and firewall rules.   
`gcp-hybrid-connectivity-admins` | Create network devices such as Cloud VPN instances and Cloud Router.   
`gcp-logging-monitoring-admins` | Use all Cloud Logging and Cloud Monitoring features.   
`gcp-logging-monitoring-viewers` | Read-only access to a subset of logs and monitoring data.   
`gcp-security-admins`  
| Establishing and managing security policies for the entire organization, including access management and [organization constraint policies](https://docs.cloud.google.com/resource-manager/docs/organization-policy/org-policy-constraints). See the [Google Cloud enterprise foundations blueprint](https://docs.cloud.google.com/architecture/security-foundations) for more information about planning your Google Cloud security infrastructure.   
`gcp-developers` | Design, code, and test applications.   
`gcp-devops` | Create or manage end-to-end pipelines that support continuous integration and delivery, monitoring, and system provisioning.   
  
To create administrative groups, do the following:

  1. Select Google as your provider.

  2. On the **Create Groups** page, review the list of recommended administrative groups, and then do one of the following:

     * To create all recommended groups, click **Create all groups**.
     * If you want to create a subset of the recommended groups, click **Create** in the chosen rows.
  3. Click **Continue**.




#### Create administrative users

We recommend that you initially add users who complete organizational, networking, billing, and other setup procedures. You can add other users after you complete the Google Cloud Setup process.

To add administrative users who perform Google Cloud Setup tasks, do the following:

  1. Migrate [consumer accounts](https://docs.cloud.google.com/architecture/identity/overview-google-authentication#consumer_account) to [managed user accounts](https://docs.cloud.google.com/architecture/identity/overview-google-authentication#managed_user_account) controlled by Cloud Identity. For detailed steps, see the following:

     * [Migrating consumer accounts](https://docs.cloud.google.com/architecture/identity/migrating-consumer-accounts).
     * [Add users with unmanaged accounts](https://support.google.com/a/topic/7042002).
  2. Sign in to [Google Admin console](https://admin.google.com/) using a super administrator account.

  3. Use one of the following options to add users:

     * To bulk add users, see [Add or update multiple users from a CSV file](https://support.google.com/cloudidentity/answer/40057).
     * To add users individually, see [Add an account for a new user](https://support.google.com/cloudidentity/answer/33310).
  4. When you're done adding users, return to **Google Cloud Setup: Users & groups (Create users)**.

  5. Click **Continue**.




#### Add administrative users to groups

Add the users you created to administrative groups that correspond to their duties.

  1. Make sure you created administrative users.
  2. In **Google Cloud Setup: Users & groups (Add users to groups)**, review the step details.

  3. In each **Group** row, do the following:

     1. Click **Add members**.
     2. Enter the user's email address.
     3. From the **Group role** drop-down list, select the user's group permission settings. For more information, see [Set who can view, post, and moderate](https://support.google.com/groups/answer/2464975).

Each member inherits all IAM roles you grant to a group, regardless of the group role you select.

     4. To add another user to this group, click **Add another member** and repeat these steps. We recommend that you add more than one member to each group.

     5. When you're done adding users to this group, click **Save**.

  4. When you're done with all groups, click **Confirm users & groups**.

  5. If you want to federate your identity provider into Google Cloud, see the following:

     * [Reference architectures: using an external IdP](https://docs.cloud.google.com/architecture/identity/reference-architectures#using_an_external_idp).
     * To automatically provision users and enable single sign-on, see the following: 
       * [Federate Cloud Identity with Active Directory](https://docs.cloud.google.com/architecture/identity/federating-gcp-with-active-directory-introduction).
       * [Federate Cloud Identity with Microsoft Entra ID](https://docs.cloud.google.com/architecture/identity/federating-gcp-with-azure-active-directory).
     * To sync Active Directory users and groups to Google Cloud, use [Directory Sync](https://support.google.com/a/topic/10343447) or [Google Cloud Directory Sync](https://support.google.com/a/answer/106368). 
       * For a comparison, see [Compare Directory Sync with GCDS](https://support.google.com/a/answer/10342938).



### Connect your external identity provider to Google Cloud

You can use your existing identity provider to create and manage groups and users. You configure single sign-on to Google Cloud by setting up workforce identity federation with your external identity provider. For key concepts of this process, see [Workforce Identity Federation](https://docs.cloud.google.com/iam/docs/workforce-identity-federation).

To connect your external identity provider, you complete a guided setup that includes the following steps:

  1. _Create a workforce pool_ : A workforce identity pool helps you manage identities and their access to resources. You enter the following details in a human-readable format. 
     * **Workforce pool ID** : A globally unique identifier used in IAM.
     * **Provider ID** : A name for your provider, which users will specify when they log in to Google Cloud.
  2. _Configure Google Cloud in your provider_ : The guided setup includes specific steps for your provider.
  3. _Enter your provider's workforce pool details_ : To add your provider as a trusted authority to assert identities, retrieve details from your provider and add them to Google Cloud:
  4. _Configure an initial set of administrative groups_ : The guided setup includes specific steps for your provider. You assign groups in your provider and establish a connection to Google Cloud. For a detailed description of each group, see Create administrative groups.
  5. _Assign users to each group_ : We recommend that you assign more than one user to each group.



For background information on the connection process for each provider, see the following:

  * [Configure Workforce Identity Federation with Azure AD and sign in users](https://docs.cloud.google.com/iam/docs/workforce-sign-in-azure-ad).
  * [Configure Workforce Identity Federation with Okta and sign in users](https://docs.cloud.google.com/iam/docs/workforce-sign-in-okta)
  * For other providers that support OIDC or SAML, see [Configure Workforce Identity Federation](https://docs.cloud.google.com/iam/docs/configuring-workforce-identity-federation)



### What's next

Assign permissions to your administrator groups.

###  Administrative access 

In this task, you use Identity and Access Management (IAM) to assign collections of permissions to groups of administrators at the organization level. This process gives administrators central visibility and control over every cloud resource that belongs to your organization.

For an overview of Identity and Access Management in Google Cloud, see [IAM overview](https://docs.cloud.google.com/iam/docs/overview).

### Who performs this task

To perform this task, you must be one of the following:

  * A super administrator user.
  * A user with the Organization Administrator role (`roles/resourcemanager.organizationAdmin`).



### What you do in this task

  * Review a list of default roles assigned to each administrator group that you created in the Users and groups task.

  * If you want to customize a group, you can do the following:

    * Add or remove roles.
    * If you do not plan to use a group, you can delete it.



### Why we recommend this task

You must explicitly grant all administrative roles for your organization. This task helps you implement the following security best practices:

  * [Principle of least privilege](https://en.wikipedia.org/wiki/Principle_of_least_privilege): Give users the minimum permissions required to perform their jobs, and remove access as soon as it is no longer needed.

  * [Role-based access control (RBAC)](https://en.wikipedia.org/wiki/Role-based_access_control): Assign permissions to groups of users according to their jobs. Do not grant roles to individual user accounts.




### Before you begin

Complete the following tasks:

  * Create a super administrator user and your organization in the Organization task.
  * Add users and create groups in the Users and groups task.



### Grant access to administrator groups

To grant appropriate access to each administrator group that you created in the Users and groups task, review the default roles that are assigned to each group. You can add or remove roles to customize each group's access.

  1. Make sure that you are logged in to the Google Cloud console as a super administrator user.

Alternatively, you can sign in as a user with the Organization Administrator role (`roles/resourcemanager.organizationAdmin`).

  2. Go to **Google Cloud Setup: Administrative access**.

[Go to Administrative access](https://console.cloud.google.com/cloud-setup/administrator)

  3. Select your organization name from the **Select from** drop-down list at the top of the page.

  4. Review the task overview and click **Continue administrative access**.

  5. Review the groups in the **Group (Principal)** column that you created in the Users & groups task.

**Note:** If you don't plan to use a group, you can delete it.
  6. For each group, review the default **IAM roles**. You can add or remove roles assigned to each group to fit the unique needs of your organization.

Each role contains multiple permissions that allow users to perform relevant tasks. For more information about the permissions in each role, see [IAM basic and predefined roles reference](https://docs.cloud.google.com/iam/docs/roles-permissions).

  7. When you are ready to assign roles to each group, click **Save and grant access**.




## What's next

Set up billing.

###  Billing 

In this task, you set up a billing account to pay for Google Cloud resources. To do this, you associate one of the following with your organization.

  * An existing Cloud Billing account. If you don't have access to the account, you can request access from your billing account administrator.

  * A new Cloud Billing account.


**Tip:** We recommend a single billing account for your organization.

For more information on billing, see the [Cloud Billing documentation](https://docs.cloud.google.com/billing/docs).

### Who performs this task

A person in the `gcp-billing-admins@YOUR_DOMAIN` group that you created in the Users and groups task.

### What you do in this task

  * Create or use an existing self-serve Cloud Billing account.
  * Decide whether to transition from a self-serve account to an invoiced account.
  * Set up a Cloud Billing account and payment method.



### Why we recommend this task

Cloud Billing accounts are linked to one or more Google Cloud projects and are used to pay for the resources you use, such as virtual machines, networking, and storage.

### Determine your billing account type

The billing account that you associate with your organization is one of the following types.

  * _Self-serve (or online)_ : Sign up online using a credit or debit card. We recommend this option if you are a small business or individual. When you sign up online for a billing account, your account is automatically set up as a self-serve account.

  * _Invoiced (or offline)_. If you already have a self-serve billing account, you might be eligible to apply for invoiced billing if your business meets [eligibility requirements](https://docs.cloud.google.com/billing/docs/how-to/invoiced-billing).




You cannot create an invoiced account online, but you can apply to convert a self-serve account to an invoiced account.

For more information, see [Cloud Billing account types](https://docs.cloud.google.com/billing/docs/concepts#billing_account_types).

### Before you begin

Complete the following tasks:

  * Create a super administrator user and your organization in the Organization task.
  * Add users and create groups in the Users and groups task.
  * Assign IAM roles to groups in the Administrative access task.



### Set up the billing account

Now that you have chosen a billing account type, associate the billing account with your organization. When you complete this process, you can use your billing account to pay for Google Cloud resources.

  1. Sign in to the Google Cloud console as a user from the `gcp-billing-admins@YOUR_DOMAIN` group.

  2. Go to **Google Cloud Setup: Billing**.

[Go to Billing](https://console.cloud.google.com/cloud-setup/billing)

  3. Review the task overview, and then click **Continue billing**.

  4. Select one of the following billing account options:

### Create a new account

If your organization does not have an existing account, create a new account.

     1. Select **I want to create a new billing account**.
     2. Click **Continue**.
     3. Select the billing account type you want to create. For detailed steps, see the following:

        * To create a new self-serve account, see [Create a new self-serve Cloud Billing account](https://docs.cloud.google.com/billing/docs/how-to/create-billing-account).
        * To transition an existing self-serve account to invoiced billing, see [Apply for monthly invoiced billing](https://docs.cloud.google.com/billing/docs/how-to/invoiced-billing).
     4. Verify that your billing account was created:

        1. If you created an invoiced account, wait up to 5 business days to receive email confirmation.

        2. Go to the [Billing page](https://console.cloud.google.com/billing).

        3. Select your organization from the **Select from** list at the top of the page. If the account was created successfully, it is displayed in the billing account list.

### Use my existing account

If you have an existing billing account, you can associate it with your organization.

     1. Select **I identified a billing account from this list that I would like to use to complete the setup steps**.
     2. From the **Billing** drop-down list, select the account you want to associate with your organization.
     3. Click **Continue**.
     4. Review the details and click **Confirm billing account**.

### Use another user's account

If another user has access to an existing billing account, you can ask that user to associate the billing account with your organization, or the user can give you access to complete the association.

     1. Select **I want to use a billing account that's managed by another Google user account**.
     2. Click **Continue**.
     3. Enter the billing account administrator's email address.
     4. Click **Contact administrator**.
     5. Wait for the billing account administrator to contact you with further instructions.




### What's next

Create a resource hierarchy and assign access.

## Create an initial architecture

###  Hierarchy and access 

In this task, you set up your resource hierarchy by creating and assigning access to the following resources:

[**Folders**](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy#folders)
    

Provide a grouping mechanism and isolation boundaries between projects. For example, folders can represent departments in your organization such as finance or retail.

The environment folders, such as `Production`, in your resource hierarchy are [configured for application management](https://docs.cloud.google.com/resource-manager/docs/manage-applications). You can define and manage applications in these folders.

[**Projects**](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy#projects)
    

Contain your Google Cloud resources, such as virtual machines, databases and storage buckets. Each of the environment folders also contains a [management project](https://docs.cloud.google.com/resource-manager/docs/manage-applications#management-project), which helps you manage access, billing, observability and other administrative functions for your applications.

For design considerations and best practices to organize your resources in projects, see [Decide a resource hierarchy for your Google Cloud landing zone](https://docs.cloud.google.com/architecture/landing-zones/decide-resource-hierarchy).

### Who performs this task

A person in the `gcp-organization-admins@YOUR_DOMAIN` group that you created in the Users and groups task can perform this task.

### What you do in this task

  * Create an initial hierarchy structure that includes folders and projects.
  * Set IAM policies to control access to your folders and projects.



### Why we recommend this task

Creating a structure for folders and projects helps you manage Google Cloud resources and applications. You can use the structure to assign access based on the way your organization operates. For example, you might organize and provide access based on your organization's unique collection of geographic regions, subsidiary structures, or accountability frameworks.

### Plan the resource hierarchy

Your resource hierarchy helps you create boundaries, and share resources across your organization for common tasks. You create your hierarchy using one of the following initial configurations, based on your organization structure:

  * _Simple environment-oriented_ :

    * Isolate environments like `Non-Production` and `Production`.
    * Implement distinct policies, regulatory requirements, and access controls in each environment folder.
    * Good for small companies with centralized environments.
  * _Simple team-oriented_ :

    * Isolate teams like `Development` and `QA`.
    * Isolate access to resources using child environment folders under each team folder.
    * Good for small companies with autonomous teams.
  * _Environment-oriented_ :

    * Prioritize the isolation of environments like `Non-Production` and `Production`.
    * Under each environment folder, isolate business units.
    * Under each business unit, isolate teams.
    * Good for large companies with centralized environments.
  * _Business unit-oriented_ :

    * Prioritize the isolation of business units like `Human Resources` and `Engineering` to help ensure that users can only access the resources and data they need.
    * Under each business unit, isolate teams.
    * Under each team, isolate environments.
    * Good for large companies with autonomous teams.



Each configuration has a `Common` folder for projects that contain shared resources. This might include logging and monitoring projects.

### Before you begin

Complete the following tasks:

  * Create a super administrator user and your organization in the Organization task.
  * Add users and create groups in the Users and groups task.
  * Assign IAM roles to groups in the Administrative access task.
  * Create or link a billing account in the Billing task.



### Configure initial folders and projects

Select the resource hierarchy that represents your organization structure.

**Important:** If you already have existing folders and projects in your organization, the new resource hierarchy you create appears alongside your existing resources. If there are existing resources that are identical to resources in the proposed hierarchy, they are automatically merged.

To configure initial folders and projects, do the following:

  1. Sign in to the Google Cloud console as a user from the `gcp-organization-admins@YOUR_DOMAIN` group you created in the Users and groups task.

  2. Select your organization from the **Select from** drop-down list at the top of the page.

  3. Go to **Google Cloud Setup: Hierarchy & access**.

[Go to Hierarchy & access](https://console.cloud.google.com/cloud-setup/hierarchy-and-access)

  4. Review the task overview, and then click **Start** next to **Resource hierarchy**.

  5. Select a starting configuration.

  6. Click **Continue and configure**.

  7. Customize your resource hierarchy to reflect your organizational structure. For example, you can customize the following:

     * Folder names.
     * Service projects for each team. To grant access to service projects, you can create the following:

       * A group for each service project.
       * Users in each group.

For an overview of service projects, see [Shared VPC](https://docs.cloud.google.com/vpc/docs/shared-vpc).

     * Projects required for monitoring, logging, and networking.

     * Custom projects.

  8. Click **Continue**.

  9. Grant access to your folders and projects.




### Grant access to your folders and projects

In the Administrative access task, you granted administrative access to groups at the organization level. In this task, you configure access to groups that interact with your newly configured folders and projects.

**Tip:** We recommend that you implement the principle of least privilege by granting the least amount of access that's necessary to resources at each level.

Projects, folders, and organizations each have their own IAM policies, which are inherited through the resource hierarchy:

  * _Organization_ : Policies apply to all folders and projects in the organization.
  * _Folder_ : Policies apply to projects and other folders within the folder.
  * _Project_ : Policies apply only to that project and its resources.



Update the [IAM policies](https://docs.cloud.google.com/iam/docs/overview#iam_policy) for your folders and projects:

  1. In the **Configure access control** section of [**Hierarchy & access**](https://console.cloud.google.com/cloud-setup/hierarchy-and-access), grant your groups access to your folders and projects:

     1. In the table, review the list of recommended IAM roles granted to each group for each resource.

     2. If you want to modify the roles assigned to each group, click **Edit** in the desired row.

For more information about each role, see [IAM basic and predefined roles](https://docs.cloud.google.com/iam/docs/understanding-roles).

  2. Click **Continue**.

  3. Review your changes and click **Confirm draft configuration**.




### Configure billing for management projects

After you deploy your configuration, you must configure billing for each management project. The billing account is required to pay for APIs that have associated costs. For more information, see [Link a billing account for the management project](https://docs.cloud.google.com/resource-manager/docs/manage-applications#billing).

### What's next

Configure security settings.

###  Security 

In this task, you configure security settings and products to help protect your organization.

**Important:** The policies you apply in this task are a first step in configuring security. Your organization's unique challenges require you to perform security audits, understand the attack surface for your architecture, and so on.

### Who performs this task

You must have one of the following to complete this task:

  * The Organization Administrator role (`roles/resourcemanager.organizationAdmin`).
  * Membership in one of the following groups that you created in the Users and groups task: 
    * `gcp-organization-admins@<your-domain>.com`
    * `gcp-security-admins@<your-domain>.com`



### What you do in this task

Apply recommended organization policies based on the following categories:

  * Access management.
  * Service account behavior.
  * VPC network configuration.
  * Cloud KMS with Autokey—only available for the [Advanced production foundation option](https://docs.cloud.google.com/docs/enterprise/cloud-setup#select-foundation-option).



You also enable Security Command Center to centralize vulnerability and threat reporting.

Additionally, we recommend that you configure [Essential Contacts](https://docs.cloud.google.com/resource-manager/docs/managing-notification-contacts) to help security and operational teams receive critical alerts.

### Why we recommend this task

Applying recommended organization policies helps you limit user actions that don't align with your security posture.

Enabling Security Command Center helps you create a central location to analyze vulnerabilities and threats.

Enforcing and automating [Cloud KMS with Autokey](https://docs.cloud.google.com/kms/docs/kms-autokey) helps you use customer-managed encryption keys (CMEKs) consistently to protect your resources.

### Before you begin

Complete the following tasks:

  * Create a super administrator user and your organization in the Organization task.
  * Add users and create groups in the Users and groups task.
  * Assign IAM roles to groups in the Administrative access task.



### Start the security task

  1. Sign in to the Google Cloud console with a user you identified in Who performs this task.

  2. Select your organization from the **Select from** drop-down at the top of the page.

  3. Go to **Google Cloud Setup: Security**.

[Go to Security](https://console.cloud.google.com/cloud-setup/security)

  4. Review the task overview, and then click **Start Security**.




### Centralize vulnerability and threat reporting

To centralize vulnerability and threat reporting services, enable Security Command Center. This helps you strengthen your security posture and mitigate risks. For more information, see [Security Command Center overview](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview).

  1. On the **Google Cloud Setup: Security** page, make sure that the **Enable Security Command Center: Standard** checkbox is enabled.

This task enables the free Standard tier. You can upgrade to the Premium version at a later time. For more information, see [Security Command Center service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers).

  2. Click **Apply SCC settings**.




### Apply recommended organization policies

Organization policies apply at the organization level, and are inherited by folders and projects. In this task, review and apply the list of recommended policies. You can modify organization policies at any time. For more information, see [Introduction to the Organization Policy Service](https://docs.cloud.google.com/resource-manager/docs/organization-policy/overview).

  1. Review the list of recommended organization policies. If you don't want to apply a recommended policy, click its checkbox to remove it.

For a detailed explanation of each organization policy, see [Organization policy constraints](https://docs.cloud.google.com/resource-manager/docs/organization-policy/org-policy-constraints).

  2. Click **Confirm organization policy configurations**.




The organization policies that you select are applied when you deploy your configuration in a later task.

### Enforce and automate customer encryption keys

Cloud KMS with Autokey lets developers in your organization create symmetric encryption keys when required to protect your Google Cloud resources. You can configure Cloud KMS with Autokey if you selected the [Advanced production foundation option](https://docs.cloud.google.com/docs/enterprise/cloud-setup#select-foundation-option).

**Note:** Cloud KMS with Autokey includes a free allotment of active key versions. You might incur costs as your resource utilization increases. For pricing details, see [Cloud KMS pricing](https://cloud.google.com/kms/pricing).

  1. Review the description of Cloud KMS with Autokey, and then for **Use Cloud KMS with Autokey and apply organizational policies** , click **Yes (recommended)**.
  2. Click **Confirm key management configuration**.



The following configurations are applied when you deploy your configuration in a later task:

  * Set up an Autokey project in each environment folder of your hierarchy.
  * Enable Cloud KMS with Autokey on the environment folders.
  * Require the use of customer managed encryption keys (CMEKs) for resources created in each environment folder.
  * Restrict each folder to only use Cloud KMS keys in the Autokey project for that folder.



### Configure organizational notification contacts

You can configure organizational notification contacts to make sure that security and operational alerts reach the correct team.

To help the appropriate teams receive these critical alerts promptly, configure custom contacts using [Essential Contacts](https://docs.cloud.google.com/resource-manager/docs/managing-notification-contacts).

### What's next

Central logging and monitoring.

###  Central logging and monitoring 

In this task, you configure the following:

  * Central logging to help you analyze and gain insights from logs for all projects in your organization.
  * Central monitoring to help you visualize metrics across all projects created in this setup.



### Who performs this task

To set up logging and monitoring, you must have one of the following:

  * The Logging Admin (`roles/logging.admin`) and Monitoring Admin (`roles/monitoring.admin`) roles.
  * Membership in one of the following groups that you created in the Users and groups task: 
    * `gcp-organization-admins@YOUR_DOMAIN`
    * `gcp-security-admins@YOUR_DOMAIN`
    * `gcp-logging-monitoring-admins@YOUR_DOMAIN`



### What you do in this task

You do the following in this task:

  * Centrally organize logs that are created in projects across your organization to help with security, auditing, and compliance.
  * Configure a central monitoring project to have access to monitoring metrics across the projects you created in this setup.



### Why we recommend this task

Log storage and retention simplifies analysis and preserves your audit trail. Central monitoring gives you a view of metrics in one place.

### Before you begin

Complete the following tasks:

  * Create a super administrator user and your organization in the Organization task.
  * Add users and create groups in the Users and groups task.
  * Assign IAM roles to groups in the Administrative access task.
  * Create or link a billing account in the Billing task.
  * Set up your hierarchy and assign access in the Hierarchy and access task.



### Centrally organize logging

Cloud Logging helps you store, search, analyze, monitor, and alert on log data and events from Google Cloud. You can also collect and process logs from your applications, on-premises resources, and other clouds. We recommend that you use Cloud Logging to consolidate logs into a single log bucket.

**Note:** Cloud Logging includes a free monthly allotment. You might incur costs as your resource utilization increases. For pricing details, see [Cloud Logging pricing summary](https://cloud.google.com/stackdriver/pricing).

For more information, see the following:

  * For an overview, see [Routing and storage overview](https://docs.cloud.google.com/logging/docs/routing/overview).
  * For information on logging on-premises resources, see [Logging on-premises resources with BindPlane](https://docs.cloud.google.com/architecture/logging-on-premises-resources-with-bindplane).
  * For steps to change the log filter after you deploy your configuration, see [Inclusion filters](https://docs.cloud.google.com/logging/docs/routing/overview#inclusion-filters).



To store your log data in a central log bucket, do the following:

  1. Sign in to the Google Cloud console as a user that you identified in Who performs this task.

  2. Select your organization from the **Select from** drop-down list at the top of the page.

  3. Go to **Google Cloud Setup: Central logging and monitoring**.

[Go to Central logging and monitoring](https://console.cloud.google.com/cloud-setup/logging)

  4. Review the task overview and click **Start central logging & monitoring**.

  5. Review the task details.

  6. To route logs to a central log bucket, ensure that **Store organization-level audit logs in a logs bucket** is selected.

  7. Expand **Route logs to a Logging log bucket** and do the following:

     1. In the **Log bucket name** field, enter a name for the central log bucket.

     2. From the **Log bucket region** list, select the region where your log data is stored.

For more information, see [Log bucket locations](https://docs.cloud.google.com/logging/docs/region-support#buckets-locations).

     3. By default logs are stored for 30 days. We recommend that large enterprises store logs for 365 days. To customize the retention period, enter the number of days in the **Retention period** field.

Logs stored for longer than 30 days incur a retention cost. For more information, see [Cloud Logging pricing summary](https://cloud.google.com/stackdriver/pricing).




### Export logs outside of Google Cloud

If you want to export logs to a destination outside of Google Cloud, you can export using Pub/Sub. For example, if you use multiple cloud providers, you might decide to export log data from each cloud provider to a third-party tool.

You can filter the logs you export to meet your unique needs and requirements. For example, you might choose to limit the types of logs you export to control costs or to reduce noise in your data.

For more information about exporting logs, see the following:

  * For an overview, see [What is Pub/Sub?](https://docs.cloud.google.com/pubsub/docs/overview)
  * For pricing information, see the following: 
    * [Pub/Sub pricing](https://cloud.google.com/pubsub/pricing).
    * [Best practices for Cloud Audit Logs: Pricing](https://docs.cloud.google.com/logging/docs/audit/best-practices#pricing).
  * For information on streaming to Splunk, see [Stream logs from Google Cloud to Splunk](https://docs.cloud.google.com/architecture/stream-logs-from-google-cloud-to-splunk).



To export logs, do the following:

  1. Click **Stream your logs to other applications, other repositories, or third parties**.

  2. In the **Pub/Sub topic ID** field, enter an identifier for the topic that contains your exported logs. For information on subscribing to a topic, see [Pull subscriptions](https://docs.cloud.google.com/pubsub/docs/pull).

  3. To select logs to export, do the following:

     1. For information about each log type, see [Understand Cloud Audit Logs](https://docs.cloud.google.com/logging/docs/audit/best-practices#understand-audit-logs).

     2. To prevent one of the following recommended logs from being exported, click the **Inclusion filter** list and clear the log checkbox:

        * **Cloud Audit logs: Admin Activity** : API calls or actions that modify resource configuration or metadata.
        * **Cloud Audit logs: System Event** : Google Cloud actions that modify resource configuration.
        * **Access Transparency** : Actions that Google personnel take when accessing customer content.
     3. Select the following additional logs to export them:

        * **Cloud Audit logs: Data Access** : API calls that read resource configuration or metadata, and user-driven API calls that create, modify, or read user-provided resource data.
        * **Cloud Audit logs: Policy Denied** : Google Cloud service access denials to user or service accounts, based on security policy violations.
     4. The logs you select in this step are exported only if they are enabled in your projects or resources. For steps to change the log filter for your projects and resources after you deploy your configuration, see [Inclusion filters](https://docs.cloud.google.com/logging/docs/routing/overview#inclusion-filters).

     5. Click **OK**.

  4. Click **Continue to Monitoring**.




### Set up central monitoring

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Central monitoring helps you analyze system health, performance, and security for multiple projects. In this task, you add the projects that you created during the Hierarchy and access task to a scoping project. You can then monitor those projects from the scoping project. After you complete Cloud setup, you can configure other projects to be monitored by the scoping project.

For more information, see [Metrics scope overview](https://docs.cloud.google.com/monitoring/settings).

To set up central monitoring, do the following:

  1. To configure projects created during Google Cloud Setup for central monitoring, ensure that **Use central monitoring** is selected.

Projects that you created during Google Cloud Setup are added to the [metrics scope](https://docs.cloud.google.com/monitoring/settings) of the listed **Scoping project**.

  2. Cloud Monitoring includes a free monthly allotment. For more information, see [Cloud Monitoring pricing summary](https://cloud.google.com/stackdriver/pricing#monitoring-pricing-summary).

  3. For steps to configure projects that you create outside of Google Cloud Setup, see the following:

     * [Configure a metrics scope](https://docs.cloud.google.com/monitoring/settings/multiple-projects).
     * [Monitored project limits](https://docs.cloud.google.com/monitoring/quotas#workspace_limits).



### Complete the configuration

To complete the logging and monitoring task, do the following:

  1. Click **Confirm Configuration**.

  2. Review your logging and monitoring configuration details. Your configuration isn't deployed until you deploy your settings in a later task.




### What's next

Set up your initial networking configuration.

###  VPC networks 

In this task, you set up your initial networking configuration, which you can scale as your needs change.

### Virtual Private Cloud architecture

A [Virtual Private Cloud (VPC)](https://docs.cloud.google.com/vpc/docs/overview) network is a virtual version of a physical network that is implemented inside of Google's production network. A VPC network is a global resource that consists of regional [subnetworks (subnets)](https://docs.cloud.google.com/vpc/docs/subnets).

VPC networks provide networking capabilities to your Google Cloud resources such as Compute Engine virtual machine instances, GKE containers, and App Engine flexible environment instances.

[Shared VPC](https://docs.cloud.google.com/vpc/docs/shared-vpc) connects resources from multiple projects to a common VPC network so that they can communicate with each other using the network's internal IP addresses. The following diagram shows the basic architecture of a Shared VPC network with attached service projects.

![Shared VPC architecture](https://ssl.gstatic.com/pantheon/images/gettingstarted/onboarding/networking_v2/shared_vpc_education_diagram.svg)

When you use Shared VPC, you designate a host project and attach one or more service projects to it. Virtual Private Cloud networks in the host project are called Shared VPC networks.

The example diagram has production and non-production host projects, which each contain a Shared VPC network. You can use a host project to centrally manage the following:

  * Routes
  * Firewalls
  * VPN connections
  * Subnets



A service project is any project that's attached to a host project. You can share subnets, including secondary ranges, between host and service projects.

In this architecture, each Shared VPC network contains public and private subnets:

  * The public subnet can be used by internet-facing instances for external connectivity.
  * The private subnet can be used by internal-facing instances that are not allocated public IP addresses.



In this task, you create an initial network configuration based on the example diagram.

### Who performs this task

You need one of the following to perform this task:

  * The `roles/compute.networkAdmin` role.
  * Inclusion in the `gcp-network-admins@YOUR_DOMAIN` group that you created in the Users and groups task.



### What you do in this task

Create an initial network configuration, including the following:

  * Create multiple host projects to reflect your development environments.
  * Create a Shared VPC network in each host project to allow distinct resources to share the same network.
  * Create distinct subnets in each Shared VPC network to provide network access to service projects.



### Why we recommend this task

Distinct teams can use Shared VPC to connect to a common, centrally-managed VPC network.

## Before you begin

Complete the following tasks:

  * Create a super administrator user and your organization in the Organization task.
  * Add users and create groups in the Users and groups task.
  * Assign IAM roles to groups in the Administrative access task.
  * Create or link a billing account in the Billing task.
  * Set up your hierarchy and assign access in the Hierarchy and access task.



### Configure your network architecture

Create your initial network configuration with two host projects to segment non-production and production workloads. Each host project contains a Shared VPC network, which can be used by multiple service projects. You configure network details and then deploy a configuration file in a later task.

To configure your initial network, do the following.

  1. Sign in to the Google Cloud console as a user from the `gcp-organization-admins@YOUR_DOMAIN` group that you created in the Users and groups task.

  2. Select your organization from the **Select an organization** drop-down list at the top of the page.

  3. Go to **Google Cloud Setup: Networking**.

[Go to Networking](https://console.cloud.google.com/cloud-setup/networking)

  4. Review the default network architecture.

  5. To edit the network name, do the following:

     1. Click more_vert **Actions**
     2. Select **Edit network name**.
     3. In the **Network name** field, enter lowercase letters, numbers, or hyphens. The network name cannot exceed 25 characters.
     4. Click **Save**.



#### Modify firewall details

The default firewall rules on the host project are based on recommended best practices. You can choose to disable one or more of the default firewall rules. For general information on firewall rules, see [VPC firewall rules](https://docs.cloud.google.com/firewall/docs/firewalls).

To modify firewall settings, do the following:

  1. Click more_vert **Actions**.

  2. Select **Edit firewall rules**.

  3. For detailed information about each default firewall rule, see [Pre-populated rules in the default network](https://docs.cloud.google.com/firewall/docs/firewalls#more_rules_default_vpc).

  4. To disable a firewall rule, clear its corresponding checkbox.

  5. To disable **Firewall Rules Logging** , click **Off**.

By default, traffic to and from Compute Engine instances are logged for auditing purposes. This process incurs costs. For more information, see [VPC firewall rules logging overview](https://docs.cloud.google.com/firewall/docs/vpc-firewall-rules-logging-overview).

  6. Click **Save**.




#### Modify subnet details

Each VPC network contains at least one subnet, which is a regional resource with an associated IP address range. In this multi-regional configuration, you must have at least two subnets with non-overlapping IP ranges.

For more information, see [Subnets](https://docs.cloud.google.com/vpc/docs/subnets).

Each subnet is configured using recommend best practices. If you want to customize each subnet, do the following:

  1. Click more_vert **Actions**
  2. Select **Edit subnets**.
  3. In the **Name** field, enter lowercase letters, numbers, or hyphens. The subnet name cannot exceed 25 characters.
  4. From the **Region** drop-down, select a region that is close to your point of service.

We recommend a different region for each subnet. You can't change the region after you deploy your configuration. For information about choosing a region, see [Regional resources](https://docs.cloud.google.com/compute/docs/regions-zones/global-regional-zonal-resources#regionalresources).

  5. In the **IP address range** field, enter a range in CIDR notation— for example, 10.0.0.0/24.

The range you enter must not overlap with other subnets in this network. For information on valid ranges, see [IPv4 subnet ranges](https://docs.cloud.google.com/vpc/docs/vpc#manually_created_subnet_ip_ranges).

**Note:** To expand the primary IPv4 range of an existing subnet, reduce the prefix length. For example, to expand 10.0.0.0/24, use 10.0.0.0/20.
  6. Repeat these steps for Subnet 2.

  7. To configure additional subnets in this network, click **Add subnet** and repeat these steps.

  8. Click **Save**.




Your subnets are automatically configured according to best practices. If you want to modify the configuration, in the **Google Cloud Setup: VPC Networks** page, do the following:

  1. To turn off VPC Flow Logs, from the **Flow logs** column, select **Off**.

When flow logs are on, each subnet records network flows that you can analyze for security, expenses optimization, and other purposes. For more information, see [Use VPC Flow Logs](https://docs.cloud.google.com/vpc/docs/using-flow-logs).

VPC Flow Logs incur costs. For more information, see [Virtual Private Cloud pricing](https://cloud.google.com/vpc/pricing).

  2. To turn off Private Google Access, from the **Private access** column, select **Off**.

When Private Google Access is on, VM instances that don't have external IP addresses can reach Google APIs and services. For more information, see [Private Google Access](https://docs.cloud.google.com/vpc/docs/private-google-access).

  3. To turn on Cloud NAT, from the **Cloud NAT** column, select **On**.

When Cloud NAT is on, certain resources can create outbound connections to the internet. For more information, see [Cloud NAT overview](https://docs.cloud.google.com/nat/docs/overview).

Cloud NAT incurs costs. For more information, see [Virtual Private Cloud pricing](https://cloud.google.com/vpc/pricing).

  4. Click **Continue to link service projects**.




### Link service projects to your host projects

A service project is any project that has been attached to a host project. This attachment allows the service project to participate in Shared VPC. Each service project can be operated and administered by different departments or teams to create a separation of responsibilities.

For more information about connection multiple projects to a common VPC network, see [Shared VPC overview](https://docs.cloud.google.com/vpc/docs/shared-vpc).

To link service projects to your host projects and complete the configuration, do the following:

  1. For each subnet in the **Shared VPC networks** table, select a service project to connect. To do this, select from the **Select a project** drop-down in the **Service project** column.

You can connect a service project to multiple subnets.

  2. Click **Continue to Review**.

  3. Review your configuration, and make changes.

You can make edits until you deploy your configuration file.

  4. Click **Confirm draft configuration**. Your network configuration is added to your configuration file.

Your network is not deployed until you deploy your configuration file in a later task.




### What's next

Set up hybrid connectivity, which helps you connect on-premises servers or other cloud providers to Google Cloud.

###  Hybrid connectivity 

In this task, you establish connections between your peer (on-premises or other cloud) networks and your Google Cloud networks, as in the following diagram.

![Shared VPC networks with individual regions that are connected to a peer network through HA VPN tunnels](https://www.gstatic.com/pantheon/images/gettingstarted/onboarding/hybrid_connectivity/education_page_diagram_v2.svg)

This process creates an HA VPN, which is a high-availability (HA) solution that you can quickly create to transmit data over the public internet.

After you deploy your Google Cloud configuration, we recommend creating a more robust connection using [Cloud Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview).

For more information on connections between peer networks and Google Cloud, see the following:

  * [Cloud VPN overview](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/overview)
  * [Choosing a Network Connectivity product](https://docs.cloud.google.com/network-connectivity/docs/how-to/choose-product)



### Who performs this task

You must have the Organization Administrator role (`roles/resourcemanager.organizationAdmin`).

### What you do in this task

Create low-latency, high-availability connections between your VPC networks and your on-premises or other cloud networks. You configure the following components:

  * _Google Cloud HA VPN gateway_ : A regional resource that has two interfaces, each with its own IP address. You specify the IP stack type, which determines whether IPv6 traffic is supported in your connection. For background information, see [HA VPN](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/overview#ha-vpn).
  * _Peer VPN gateway_ : The gateway on your peer network, to which the Google Cloud HA VPN gateway connects. You enter external IP addresses that your peer gateway uses to connect to Google Cloud. For background information, see [Configure the peer VPN gateway](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/configuring-peer-gateway).
  * _Cloud Router_ : Uses Border Gateway Protocol (BGP) to dynamically exchange routes between your VPC and peer networks. You assign an Autonomous System Number (ASN) as an identifier for your Cloud Router, and specify the ASN that your peer router uses. For background information, see [Create a Cloud Router to connect a VPC network to a peer network](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/create-router-vpc-network).
  * _VPN tunnels_ : Connect the Google Cloud gateway to the peer gateway. You specify the Internet Key Exchange (IKE) protocol to use to establish the tunnel. You can enter your own previously generated IKE key or generate and copy a new key. For background information, see [Configure IKE](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/configuring-peer-gateway#configure_ike).



### Why we recommend this task

An HA VPN provides a secure and highly available connection between your existing infrastructure and Google Cloud.

## Before you begin

Complete the following tasks:

  * Create a super administrator user and your organization in the Organization task.
  * Add users and create groups in the Users and groups task.
  * Assign IAM roles to groups in the Administrative access task.
  * Create or link a billing account in the Billing task.
  * Set up your hierarchy and assign access in the Hierarchy and access task.
  * Configure your network in the VPC networks task.



Collect the following information from your peer network administrator:

  * _Your peer VPN gateway name_ : The gateway to which your Cloud VPN connects.
  * _Peer interface IP address 0_ : An external IP address on your peer network gateway.
  * _Peer interface IP address 1_ : A second external address, or you can reuse IP address 0 if your peer network only has a single external IP address.
  * _Peer Autonomous System Number (ASN)_ : A unique identifier assigned to your peer network router.
  * _Cloud Router ASN_ : A unique identifier that you will assign to your Cloud Router.
  * _Internet Key Exchange (IKE) keys_ : Keys you use to establish two VPN tunnels with your peer VPN gateway. If you don't have existing keys, you can generate them during this setup and then apply them to your peer gateway.



### Configure your connections

Do the following to connect your VPC networks to your peer networks:

  1. Sign in as a user with the Organization Administrator role.

  2. Select your organization from the **Select from** drop-down list at the top of the page.

  3. Go to **Google Cloud Setup: Hybrid connectivity**.

[Go to Hybrid connectivity](https://console.cloud.google.com/cloud-setup/hybrid-connectivity)

  4. Review the task details by doing the following:

     1. Review the task overview and click **Start hybrid connectivity**.

     2. Click each tab to learn about hybrid connectivity and click **Continue**.

     3. See what to expect in each task step and click **Continue**.

     4. Review the peer gateway configuration information that you need to collect and click **Continue**.

  5. In the **Hybrid connections** area, identify the VPC networks that you want to connect, based on your business needs.

  6. In the row for the first network you chose, click **Configure**.

  7. In the **Configuration overview** area, read the description and click **Next**.

  8. In the **Google Cloud HA VPN gateway** area, do the following:

     1. In the **Cloud VPN gateway name** field, enter up to 60 characters using lowercase letters, numbers, and hyphens.

     2. In the **VPN tunnel inner IP stack type** area, select one of the following stack types:

        * **IPv4 and IPv6 (recommended)** : Can support both IPv4 and IPv6 traffic. We recommend this setting if you plan to allow IPv6 traffic in your tunnel.
        * **IPv4** : Can only support IPv4 traffic.

The stack type determines the type of traffic that is allowed in the tunnel between your VPC network and your peer network. You cannot modify the stack type after you create the gateway. For background information, see the following:

        * [IPv6 support](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/overview#ipv6-support)
        * [Stack types and BGP sessions](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/overview#ha-vpn-stack-types)
     3. Click **Next**.

  9. In the **Peer VPN gateway** area, do the following:

     1. In the **Peer VPN gateway name** field, enter the name provided by your peer network administrator. You can enter up to 60 characters using lowercase letters, numbers, and hyphens.

     2. In the **Peer interface IP address 0** field, enter the peer gateway interface external IP address provided by your peer network administrator.

     3. In the **Peer interface IP address 1** field, do one of the following:

        * If your peer gateway has a second interface, enter its IP address.
        * If your peer gateway only has a single interface, enter the same address you entered in **Peer interface IP address 0**.

For background information, see [Configure the peer VPN gateway](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/configuring-peer-gateway).

     4. Click **Next**.

  10. In the **Cloud Router** area, do the following:

     1. In the **Cloud router ASN** field, enter the Autonomous System Number you want to assign to your Cloud Router, as provided by your peer network administrator. For background information, see [Create a Cloud Router](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/create-router-vpc-network#create_a).

     2. In the **Peer router ASN** field, enter your peer network router's Autonomous System Number, as provided by your peer network administrator.

  11. In the **VPN tunnel 0** area, do the following:

     1. In the **Tunnel 0 name** field, enter up to 60 characters using lowercase letters, numbers, and hyphens.

     2. In the **IKE version** area, select one of the following:

        * **IKEv2 - recommended** : Supports IPv6 traffic.
        * **IKEv1** : Use this setting if you do not plan to allow IPv6 traffic in the tunnel.

For background information, see [Configure VPN tunnels](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/configuring-peer-gateway#configure_vpn_tunnels).

     3. In the **IKE pre-shared key** field, enter the key you use in your peer gateway configuration, as provided by your peer network administrator. If you don't have an existing key, you can click **Generate and copy** , and then give the key to your peer network administrator.

**Note:** If you forget the key that you generate in this step, you can find it after you deploy. The key is stored in the **gcp-internal-cloud-setup** folder in the **Hybrid Connectivity Project** project. For steps to access a key using Secret Manager, see [List secrets and view secret details](https://docs.cloud.google.com/secret-manager/docs/view-secret-details).
  12. In the **VPN tunnel 1** area, repeat the previous step to apply settings for the second tunnel. You configure this tunnel for redundancy and additional throughput.

  13. Click **Save**.

  14. Repeat these steps for any other VPC networks that you want to connect to your peer network.




## After you deploy

After you deploy your Google Cloud Setup configuration, complete the following steps to ensure that your network connection is complete:

  1. Work with your peer network administrator to align your peer network with your hybrid connectivity settings. After you deploy, specific instructions are provided for your peer network, including the following:

     * Tunnel settings.
     * Firewall settings.
     * IKE settings.
  2. Validate the network connections you created. For example, you can use Network Intelligence Center to check connectivity between networks. For more information, see [Connectivity Tests overview](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/concepts/overview).

  3. If your business needs require a more robust connection, use Cloud Interconnect. For more information, see [Choosing a Network Connectivity product](https://docs.cloud.google.com/network-connectivity/docs/how-to/choose-product).




## What's next

Deploy your configuration, which includes settings for your hierarchy and access, logging, network, and hybrid connectivity.

## Deploy your settings

###  Deploy or download 

As you complete the Google Cloud Setup process, your settings from the following tasks are compiled into Terraform configuration files:

  * Hierarchy and access
  * Security
  * Central logging and monitoring
  * VPC networks
  * Hybrid connectivity



To apply your settings, you review your selections and choose a deployment method.

### Who performs this task

A person in the `gcp-organization-admins@YOUR_DOMAIN` group that you created in the Users and groups task.

### What you do in this task

Deploy configuration files to apply your setup settings.

### Why we recommend this task

You must deploy configuration files to apply the settings you selected.

### Before you begin

You must complete the following tasks:

  * Create a super administrator user and your organization in the Organization task.
  * Add users and create groups in the Users and groups task.
  * Assign IAM roles to groups in the Administrative access task.
  * Create or link a billing account in the Billing task.
  * Set up your hierarchy and assign access in the Hierarchy and access task.



The following tasks are recommended:

  * Strengthen your security posture by setting up cost-free services in the Security task.
  * Consolidate log data in a single location and monitor all projects from a single project in the Central logging and monitoring task.
  * Configure your initial network in the VPC networks task.
  * Connect peer networks to Google Cloud in the Hybrid connectivity task.



### Review your configuration details

Do the following to make sure that your configuration settings are complete:

  1. Sign in to the Google Cloud console as a user from the `gcp-organization-admins@YOUR_DOMAIN` group that you created in the Users and groups task.

  2. Select your organization from the **Select from** drop-down list at the top of the page.

  3. Go to **Google Cloud Setup: Deploy or download**.

[Go to Deploy or Download](https://console.cloud.google.com/cloud-setup/download)

  4. Review the configuration settings you selected. Click each of the following tabs and review your settings:

     * **Resource hierarchy & access**
     * **Security**
     * **Logging & monitoring**
     * **VPC networks**
     * **Hybrid connectivity**



### Deploy your configuration

Now that you have reviewed your configuration details, use one of the following options:

  * **Deploy directly from the console** : Use this option if you don't have an existing Terraform deployment workflow, and want a simple deployment method. You can deploy using this method only once.

  * **Download and deploy the Terraform file** : Use this option if you want to automate resource management using a Terraform deployment workflow. You can download and deploy using this method multiple times.




Deploy using one of the following options:

### Deploy directly

If you don't have an existing Terraform workflow and want a simple one-time deployment, you can deploy directly from the console.

**Warning:** If you plan to deploy using your own Terraform workflow in the future, don't click Deploy directly.

  1. Click **Deploy directly**.

  2. Wait several minutes for the deployment to complete.

  3. If the deployment fails, do the following:

     1. To reattempt the deployment, click **Retry Process**.
     2. If the deployment fails after multiple attempts, you can contact an administrator for help. To do this, click **Contact organization administrator**.



### Download and deploy

If you want to iterate on your deployment using your Terraform deployment workflow, download and deploy configuration files.

  1. To download your configuration file, click **Download as Terraform**.

  2. The package you download contains Terraform configuration files based on the settings you selected in the following tasks:

     * **Hierarchy & access**
     * **Security**
     * **Central logging & monitoring**
     * **VPC networks**
     * **Hybrid connectivity**

If you only want to deploy configuration files that are relevant to your responsibilities, you can avoid downloading irrelevant files. To do this, clear the check boxes for the configuration files that you don't need.

  3. Click **Download**. A `terraform.tar.gz` package that includes the selected files is downloaded to your local file system.

  4. For detailed deployment steps, see [Deploy your foundation using Terraform downloaded from the console](https://docs.cloud.google.com/docs/enterprise/deploy-foundation-using-terraform-from-console).




### What's next

Choose a support plan.

###  Support 

In this task, you choose a support plan that fits your business needs.

### Who performs this task

A person in the `gcp-organization-admins@YOUR_DOMAIN` group created in the Users and groups task.

### What you do in this task

Choose a support plan based on your company's needs.

### Why we recommend this task

A premium support plan provides business-critical support to quickly resolve issues with help from experts at Google Cloud.

### Choose a support option

You automatically get free Basic Support, which includes access to the following resources:

  * [Documentation](https://docs.cloud.google.com/docs)
  * [Community support and discussions](https://docs.cloud.google.com/support/docs/community)
  * [Support for billing issues](https://docs.cloud.google.com/support/billing)



We recommend that enterprise customers sign up for [Premium Support](https://docs.cloud.google.com/support/docs/premium), which offers one-on-one technical support with Google support engineers. To compare support plans, see [Google Cloud customer care](https://docs.cloud.google.com/support).

### Before you begin

Complete the following tasks:

  * Create a super administrator user and your organization in the Organization task.
  * Add users and create groups in the Users and groups task.
  * Assign IAM roles to groups in the Administrative access task.



### Enable support

Identify and select a support option.

  1. Review and select a support plan. For more information, see [Google Cloud Customer Care](https://docs.cloud.google.com/support#support-plans).

  2. Sign in to the Google Cloud console with a user from the `gcp-organization-admins@<your-domain>.com` group that you created in the Users and groups task.

  3. Go to **Google Cloud Setup: Support**.

[Go to Support](https://console.cloud.google.com/cloud-setup/support)

  4. Review the task details and click **View support offerings** to select a support option.

  5. After you set up your support option, go back to the **Google Cloud Setup: Support** page and click **Mark task as completed**.




### What's next

Now that you have completed the Google Cloud Setup, you are ready to extend your initial setup, deploy prebuilt solutions, and migrate your existing workflows. For more information, see [Extend your initial setup and start building](https://docs.cloud.google.com/docs/enterprise/manage-foundation).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-16 UTC."],[],[]] 
