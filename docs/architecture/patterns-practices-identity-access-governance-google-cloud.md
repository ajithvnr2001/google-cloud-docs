---
url: https://docs.cloud.google.com/architecture/patterns-practices-identity-access-governance-google-cloud/
title: Patterns and practices for identity and access governance on Google Cloud \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:38:30.943492+00:00
---

# Patterns and practices for identity and access governance on Google Cloud  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/patterns-practices-identity-access-governance-google-cloud/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Patterns and practices for identity and access governance on Google Cloud Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2024-07-11 UTC

There are a number of Google Cloud products and services that you can use to help your organization develop an approach for identity governance and access management for applications and workloads running on Google Cloud. This document is intended for security administrators, operations managers, and enterprise architects who work in customer teams and who want to learn about these tools and controls and how to use them.

This document assumes that you have the following:

  * A Google Cloud project.
  * A user account with administrative access to manage Cloud Identity groups and users. You need this access to run the example procedures in this document.
  * A user account without administrative access to manage Cloud Identity groups and users. You need this account to test some of the controls that you set in the example procedures in this document.

If you don't already have access to a Google Cloud project and administrative access to Cloud Identity, see [Creating a Google Cloud project](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects) and [Setting up Cloud Identity](https://docs.cloud.google.com/identity/docs/set-up-cloud-identity-admin).




## Discover unused accounts and permissions

It's a best practice to remove user accounts when they are no longer needed because unused (orphaned) user accounts and service accounts can pose a security risk. You can use Google Cloud [Policy Intelligence](https://docs.cloud.google.com/policy-intelligence) in the following ways to help your enterprise understand and reduce risk:

  * Helping administrators in your enterprise discover accounts and permissions that aren't being used anymore, for reasons like an employee has left the company or changed roles.
  * Helping to identify service accounts that have been abandoned after the completion of tasks.



### View and apply IAM recommendations

The [Identity and Access Management (IAM) recommender](https://docs.cloud.google.com/iam/docs/recommender-overview) is part of the Policy Intelligence suite of tools and services. It uses machine learning (ML) to make smart access control recommendations to help you identify accounts that no longer need access to Google Cloud resources. You can then review the recommendations and decide whether to apply them. IAM recommender also helps you to maintain the principle of least privilege across all the members in your organization. In addition to providing recommendations, the [Recommender](https://docs.cloud.google.com/recommender/docs/overview) service uses ML to provide detailed [insights](https://docs.cloud.google.com/recommender/docs/insights/using-insights). Insights are findings that highlight notable patterns in resource usage. For example, you can collect additional information about permission usage in your project, identify permissions that aren't being used and are no longer needed, and [identify unused service accounts](https://docs.cloud.google.com/iam/docs/service-account-overview#identify-unused).

It's possible to view and apply IAM recommendations in the Google Cloud console at an enterprise-level scale. In the following example procedure, you use BigQuery to review and rightsize access permissions in your organization. To set up the BigQuery integration, you configure an export of recommendations made by IAM recommender to a BigQuery dataset. This data can then be queried and reviewed using visualization tools such as [Data Studio](https://lookerstudio.google.com/overview) and [Looker](https://docs.cloud.google.com/looker).

### Implementation

  1. In the Google Cloud console, on the project selector page, [select or create a Google Cloud project](https://console.cloud.google.com/projectselector2/home/dashboard?_ga=2.171331176.996626712.1613379397-1723329357.1612296386).

  2. BigQuery is automatically enabled in new projects. To activate BigQuery in a pre-existing project, enable the BigQuery API.

[ Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=bigquery)

  3. Configure the BigQuery Data Transfer Service to pull data from IAM recommender. To learn more, see [Exporting recommendations to BigQuery](https://docs.cloud.google.com/recommender/docs/bq-export/export-recommendations-to-bq).

  4. Go to the BigQuery page.

[ Go to BigQuery](https://console.cloud.google.com/bigquery)

  5. Copy and paste the following query into the **Editor** field:
         
         SELECT
            recommendation_details
         FROM PROJECT_ID.DATASET.TABLE_NAME
         WHERE recommender = "google.iam.policy.Recommender"
         AND recommender_subtype = "REMOVE_ROLE"
         

Replace the following:

     * `PROJECT_ID`: the Google Cloud project ID that you are using to execute this example
     * `DATASET`: the name of the dataset that you selected when setting up the BigQuery Data Transfer Service job.
     * `TABLE_NAME`: the name of the table created by the BigQuery Data Transfer Service job.

You run this query to identify the `recommender_subtype` subtype of IAM Recommender`REMOVE_ROLE` recommendations.

  6. Click **Run**. You use the query result to identify unused roles and rightsize IAM role bindings.

You can save query results to Sheets. To learn more, see [Saving query results to Sheets](https://docs.cloud.google.com/bigquery/docs/writing-results#saving-query-results-to-sheets).




## Give users the ability to request access to resources

Enterprise administrators need the ability to let users request access to resources. Typically, these requests go through an approval process where a designated approver or a group of approvers must approve the request before access is given. [Google Groups](https://docs.cloud.google.com/iam/docs/overview#google_group) lets you apply an access policy to a collection of users, enabling you to follow the policy management best practice of giving access to resources based on group membership. This approach keeps policies relevant as join, move, and leave events occur through group membership changes.

You can give and change access controls for a whole group with Google Groups, instead of giving or changing access controls one at a time for individual users or service accounts. You can also easily add members to and remove members from a Google group instead of updating an IAM policy to add or remove users.

### Set up resource access using Google Groups

You can create and manage a Google group using [Cloud Identity](https://docs.cloud.google.com/identity). Cloud Identity is an identity as a service (IDaaS) solution that manages users and groups. You can also configure Cloud Identity to federate identities between Google and other identity providers, such as [Active Directory](https://docs.cloud.google.com/architecture/identity/federating-gcp-with-active-directory-introduction) and [Azure Active Directory](https://docs.cloud.google.com/architecture/identity/federating-gcp-with-azure-active-directory). [Google Groups](https://docs.cloud.google.com/iam/docs/overview#google_group) also lets a user request membership to a group. This request is routed to group administrators who can then approve or decline that request. To learn more, see [Create a group and choose group settings](https://support.google.com/groups/answer/2464926).

When you create and manage a Google group to give access to Google Cloud resources, make sure to consider the implications of the settings that you select. Although we recommend that you minimize the number of users who can manage the group, we recommend that you set up more than one group administrator to always have access to the group. We also recommend that you restrict group membership to users in your organization.

### Implementation

In this example procedure, you create a Google group and give the viewer group access to a sample Google Cloud project. Members that you add to this group (or that you give access to upon request) are able to view the sample Google Cloud project.

### Create a sample Google group

The following steps assume that you have Cloud Identity configured. To learn more, see [Setting up Cloud Identity](https://docs.cloud.google.com/identity/docs/set-up-cloud-identity-admin). Make sure that you have the permissions that you need to [manage](https://docs.cloud.google.com/iam/docs/groups-in-cloud-console) groups.

  1. In the Google Cloud console, go to the **Groups** page.

[ Go to Groups](https://console.cloud.google.com/iam-admin/groups)

  2. Click **Create**.

  3. Fill in the details for your group.

To add members to the group, click **Add member** , then enter the email address for the member and choose their [Google Groups role](https://support.google.com/groups/answer/2464975).

When you're finished, click **Submit** to create the group.

Group settings can only be managed within Google Groups. To configure group settings, click **Manage this group in Google Groups**. To select who can join the group, in the **Who can join the group** menu, select **Organization users only**.

  4. Click **Create Group**.




### Grant the group access to a Google Cloud project

  1. In the Google Cloud console, on the project selector page, [select or create a Google Cloud project](https://console.cloud.google.com/projectselector2/home/dashboard).
  2. Open Cloud Shell:

[ Go to Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

  3. Run the following command to give the group viewer access to the project:
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
             --member=group:GROUP_EMAIL --role=roles/viewer
         

Replace the following:

     * `GROUP_EMAIL`: the email address of the group you created
     * `PROJECT_ID`: the ID of your Google Cloud project



### Test the user access request process for users in your organization

In the following procedure, you use a test user account to demonstrate the steps that users in your organization use to request access to a Google group.

  1. Sign in to [Google Groups](http://groups.google.com) as a non-administrative user. The group that you created in Create a sample Google group appears under **All Groups**. If the group doesn't appear, use search to find it.
  2. To request access to the group, click **Ask to join group**.

Once access is given, the non-administrative user account that you used to make the request should be able to view the Google Cloud `PROJECT_ID` project that the group has Viewer access to.




## Give time-bound access to Google Cloud resources

There might be situations when users in your enterprise require temporary, short-term access to Google Cloud resources. Short-term access is useful when developers need temporary access to Google Cloud resources to perform certain tasks. Short-term access also offers the following advantages:

  * Reducing administrative overhead.
  * Ensuring that the principle of least privilege and timely access is followed.



Being able to give this type of access is useful for administrators when users need access to resources in emergency situations that require quick and direct intervention. However, it can be difficult to manually track short-term access permissions and ensure that they are removed in a timely manner. IAM conditional access policies let you set temporary (expiring) access to Google Cloud resources using conditional role bindings, helping to reduce this overhead for administrators.

### Use conditional role bindings and group membership expiration

You can add conditional role bindings to new or existing IAM policies to further control access to Google Cloud resources. Some examples of when you might use conditional role bindings to give a user or a group temporary access are as follows:

  * Access to a project that expires after a specified time.
  * Access to a project that recurs every month or quarter.
  * Access to Compute Engine instances to administer tasks such as stopping instances.



When you use Google Groups to give users access to Google Cloud resources, you can use the [group membership expiration feature](https://docs.cloud.google.com/identity/docs/how-to/manage-expirations) to set expirations for group membership using the [Cloud Identity Groups API.](https://docs.cloud.google.com/identity/docs/how-to/setup) When the time that you specify has passed, users are removed from the group automatically.

### Implementation

You can use a conditional role binding to give developers temporary access to administer a specific Compute Engine instance. In this example, the role binding is set to expire on December 31, 2021.

  1. In Cloud Shell, set the following variables:
         
         export INSTANCE=create example-instance-1
         export ZONE=us-west1-b
         export USER=USER_ID_TO_GIVE_TEMPORARY_ACCESS_TO
         

Replace `USER_ID_TO_GIVE_TEMPORARY_ACCESS_TO` with the username of the user in your organization that you want to give temporary access to.

  2. Create a sample Compute Engine instance:
         
         gcloud compute instances create $INSTANCE \
             --zone $ZONE \
             --machine-type g1-small
         

You give temporary access to this instance to a user in your organization in the following steps.

  3. Give the user that you selected temporary access:
         
         gcloud compute instances add-iam-policy-binding $INSTANCE \
             --zone=$ZONE \
             --member="user:$USER" \
             --role='roles/compute.instanceAdmin.v1' \
             --condition='expression=request.time < timestamp("2022-01-01T00:00:00Z"),title=expires_end_of_2021,description=Expires at midnight on 2021-12-31'
         

  4. Retain the Compute Engine instance that you create. You use this instance later in this document in Managing privileged access.

Alternatively, you can delete the `example-instance-1` instance by running the following command:
         
         gcloud compute instances delete $INSTANCE
         




## Log lifecycle events related to identity

If you need to review IAM lifecycle events such as policy changes, service account creation, and service account assignments for auditing, [Cloud Audit Logs](https://docs.cloud.google.com/logging/docs/audit) can help. Administrators can use Cloud Audit Logs to look back at historical data for forensics and analysis. Analyzing audit logs can help you to understand access patterns and access anomalies. Audit log analysis can also be important for the following scenarios:

  * Analyzing permissions and access to resources during a data breach.
  * Analyzing production issues caused by a change in IAM policy, particularly if you want to verify which user or what process made the change.



Cloud Audit Logs stores information about the actions that users take, where the activity occurred, and when. Audit logs are classified as follows:

  * [Admin Activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity) audit logs
  * [Data Access](https://docs.cloud.google.com/logging/docs/audit#data-access) audit logs
  * [System Event](https://docs.cloud.google.com/logging/docs/audit#system-event) audit logs
  * [Policy Denied ](https://docs.cloud.google.com/logging/docs/audit#policy_denied)audit logs



We recommend that you use the following audit logs for identity and access related administrative logging:

  * Admin Activity audit logs
  * Policy Denied audit logs



Admin Activity audit logs store changes made to Google Cloud resources such as projects, Compute Engine instances, and service accounts. The following are examples of events that Admin Activity audit logs store:

  * The creation of a service account.
  * A change in an IAM policy.
  * The download of a service account key.



Policy Denied audit logs record when a user or a service account is denied access to a Google Cloud service due to a security policy violation.

### Set up Cloud Audit Logs for identity lifecycle events

You can view audit logs in the Google Cloud console or query the logs using the [Cloud Logging API](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/entries/list) or the [command-line interface](https://docs.cloud.google.com/logging/docs/api/gcloud-logging#v2_api_commands).

All audit logs have a [retention period](https://docs.cloud.google.com/logging/docs/audit#audit_log_retention). If your enterprise needs to store audit logs for longer than the default retention period, you need to export the logs to BigQuery or other sink destinations by creating a [log sink](https://docs.cloud.google.com/logging/docs/audit#exporting_audit_logs). Exporting logs to BigQuery lets you view a subset of data columns and selected data (over time or other dimensions), and do [aggregate analysis](https://docs.cloud.google.com/architecture/exporting-stackdriver-logging-for-security-and-access-analytics).

### Implementation

The following example procedure shows you how to query Google Cloud project logs to check if any of the following events have occurred:

  * There have been IAM policy changes.
  * New service accounts have been created.
  * New service account keys have been generated.



### View changes to IAM policies

  1. In the Google Cloud console, go to the **Logging** > **Logs Explorer** page.
  2. On the **Logs Explorer** page, select an existing Google Cloud project.
  3. Paste the following query into Query Builder:
         
         logName="projects/<PROJECT>/logs/cloudaudit.googleapis.com%2Factivity" AND
         (resource.type="project" OR resource.type="service_account") AND
         resource.labels.project_id="<PROJECT>" AND
         (protoPayload.methodName="SetIamPolicy" OR
         protoPayload.methodName="google.iam.admin.v1.CreateServiceAccount"
         OR
         protoPayload.methodName="google.iam.admin.v1.CreateServiceAccountKey")
         

Replace `PROJECT` with your Google Cloud project ID.

  4. Click **Run query**.




### View changes to group membership

Changes to Google group membership are tracked in Activity logs. To learn how to access these logs, see [Viewing group membership change logs](https://docs.cloud.google.com/iam/docs/groups-in-cloud-console#view-logs).

## Access certification

The [Policy Analyzer](https://docs.cloud.google.com/asset-inventory/docs/analyzing-iam-policy) can be used to help your enterprise verify that users have the appropriate access rights to Google Cloud resources on a set or periodic basis. This verification is important for compliance and audit purposes. It's also useful for security personnel and auditors to review which users have access to which resource and in what capacity. The Policy Analyzer helps you to identify which identities or principals (users, service accounts, groups, and domains) have access to which Google Cloud resources across the resource hierarchy in your organization. It also helps to identify what the type of access is. Some example questions that the Policy Analyzer can help you answer are as follows:

  * Which users can access a service account.
  * Which users can read data in a BigQuery dataset that contains personally identifiable information (PII).



Policy Analyzer can be used with the following methods:

  * Using the Google Cloud console.
  * Using APIs.
  * [Exporting IAM policies data](https://docs.cloud.google.com/asset-inventory/docs/analyzing-iam-policy-longrunning-bigquery) to BigQuery for asynchronous analysis.



### Use Policy Analyzer to check user access

The following example queries show the type insights that you can gain into user access with the Policy Analyzer:

  * What roles or permissions a principal (user, service account, group, and domain) has; for example, checking what access a former employee has to your production project.
  * Which resources a user has access to; for example, the access a former employee has to your production project resources.
  * Which principals have a certain level of access to a resource; for example, which buckets a specific user can delete in a project.



### Implementation

In the following example procedure, you use the Policy Analyzer to verify the permissions that a user has.

  1. In Cloud Shell, enable the Cloud Asset API for the project:

[ Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=cloudasset.googleapis.com)

  2. Enter the following command to find out which resources a user can access:
         
         gcloud asset analyze-iam-policy --organization="YOUR_ORG_ID" \
             --identity="user:USERNAME_TO_CERTIFY"
         

Make the following replacements:

     * `YOUR_ORG_ID`: your Google Cloud Organization ID
     * `USERNAME_TO_CERTIFY`: the username of the user whose Google Cloud access permissions you want to verify.
  3. Extract the IAM policy data to BigQuery. To learn more, see [Writing policy analysis to BigQuery](https://docs.cloud.google.com/asset-inventory/docs/analyzing-iam-policy-longrunning-bigquery).




## Manage privileged access

Some users in your organization might need privileged access to certain Google Cloud resources to perform administrative tasks. For example, these users might need to manage specific Google Cloud projects, set up project billing and budgets, or administer Compute Engine instances.

Instead of permanently granting users privileged access to resources, you can [let users request just-in-time privileged access](https://docs.cloud.google.com/architecture/manage-just-in-time-privileged-access-to-project). Using just-in-time privileged access management can help you do the following:

  * Reduce the risk of someone accidentally modifying or deleting resources. For example, when users have privileged access only when it's needed, it helps prevent them from running scripts at other times that unintentionally affect resources that they shouldn't be able to change.
  * Create an audit trail that indicates why privileges were activated.
  * Conduct audits and reviews for analyzing past activity.



Alternatively, you can grant privileged access to a service account and allow users to [impersonate the service account](https://docs.cloud.google.com/iam/docs/service-account-impersonation).

### Give privileged access to users

Broadly, management of privileged access to enterprise users in Google Cloud can be summarized as follows:

  * Giving users in the enterprise the ability to request privileged access.
  * Reviewing [Cloud Audit Logs](https://docs.cloud.google.com/logging/docs/audit) to analyze privileged access requests and access patterns. Administrators can review privileged access patterns and detect anomalies using these logs. We recommend that enterprises consider exporting these logs to persist as necessary and appropriate for audit purposes.
  * Ensuring that privileged access either expires automatically or is reviewed periodically.



[Enable 2-step verification](https://support.google.com/cloudidentity/answer/9176657) (also called multi-factor authentication) for all users that have privileged access to resources. You can also create fine-grained, attribute-based access control by using [Access Context Manager](https://docs.cloud.google.com/access-context-manager/docs/overview), which enforces an extra layer of security when privileged access is used. For example, you can have an access level that specifies that users must be on the corporate network when using privileged access to resources.

### Implementation

In this example procedure, you (as an administrator) create a Google group for privileged access to Compute Engine instances. You create a service account in Google Cloud that is given access to administer Compute Engine instances. You associate the group with the service account so that group members are able to impersonate the service account for the period that they are given membership to the privileged group.

### Create a Google group for privileged access

  1. As a Google Cloud administrator, select or create a Google Cloud project.

[ Go to Manage Resources](https://console.cloud.google.com/cloud-resource-manager)

  2. Enable billing for your project. [Enable Billing](https://docs.cloud.google.com/billing/docs/how-to/modify-project)

  3. Follow the steps in Give users the ability to request access to resources to create a new Google group.

Name the group as follows: `elevated-compute-access`




### Create a Google Cloud service account

  1. In Cloud Shell, enable the IAM Service Account Credentials API for the project that you created in [Create a Google group for privileged access](https://docs.cloud.google.com/architecture/patterns-practices-identity-access-governance-google-cloud#create_a_google_group_for_privileged_access).

[ Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=iamcredentials.googleapis.com)

  2. Set the following variables:
         
         export PROJECT_ID=$DEVSHELL_PROJECT_ID
         export PRIV_SERVICE_ACCOUNT_NAME=elevated-compute-access
         export DELEGATE_GROUP=GROUP_EMAIL_ADDRESS
         

Replace `GROUP_EMAIL_ADDRESS` with the full name of the Google group that you created.

  3. Create the service account:
         
         gcloud IAMservice-accounts create $PRIV_SERVICE_ACCOUNT_NAME \
             --description="Elevated compute access" \
             --display-name="Elevated compute access"
         

  4. Give the service account the compute administrator role:
         
         gcloud projects add-iam-policy-binding $PROJECT_ID \
             --member="serviceAccount:$PRIV_SERVICE_ACCOUNT_NAME@$PROJECT_ID.iam.gserviceaccount.com" \
             --role="roles/compute.admin"
         

  5. Give the Google group you created Service Usage consumer access for your project:
         
         gcloud projects add-iam-policy-binding $PROJECT_ID \
             --member="group:$DELEGATE_GROUP" \
             --role="roles/serviceusage.serviceUsageConsumer"
         

This permission lets the Google group members impersonate the service account that you created.

  6. Give the Google group the ability to impersonate the service account you created:
         
         gcloud IAMservice-accounts add-iam-policy-binding
         $PRIV_SERVICE_ACCOUNT_NAME@$PROJECT_ID.iam.gserviceaccount.com --member="group
         :$DELEGATE_GROUP" --role="roles/iam.serviceAccountTokenCreator"
         

  7. Skip this step if you created and retained a sample Compute Engine instance for the procedure in Give time-bound access to Google Cloud resources. You can use the sample instance to run the steps in this example.

Alternatively, use the following command to create a sample Compute Engine instance:
         
         gcloud compute instances create example-instance-1 \
             --zone us-west1-b \
             --machine-type g1-small
         

You use the instances in this example to validate that users who are given membership to the privileged group can access the instance.




### Enable audit logs

Administrators in your enterprise can enable Cloud Audit Logs to make sure that privileged access is logged and available for review and analysis. The procedure in this section shows you how to enable audit logging.

  1. Get the current IAM policies for the project:
         
         gcloud projects get-iam-policy $PROJECT_ID > /tmp/policy.yaml
         

  2. Modify the policy file to enable data access logs for Compute Engine API:
         
         cat <<EOF >> /tmp/policy.yaml
         auditConfigs:
         - auditLogConfigs:
          - logType: ADMIN_READ
          - logType: DATA_READ
          - logType: DATA_WRITE
          service: compute.googleapis.com
         EOF
         

  3. Set the new policy:
         
         gcloud projects set-iam-policy $PROJECT_ID /tmp/policy.yaml
         




### Test impersonation with the non-administrative user account

You can use the non-administrative user account to test the setup by requesting membership to the group and impersonating the service account once membership is given.

The procedure in this section shows you how enterprise users can request privileged access to Google Cloud resources. In this example procedure, the Google Cloud resources are the Compute Engine instances for a Google Cloud project. To demonstrate how users in your organization can impersonate a service account once they are given membership to the group, you request membership to relevant Google groups.

  1. [Sign in](http://groups.google.com) to Google groups with the non-administrative user account and request membership to the `elevated-compute-access` group.
  2. Use the same account to sign in to Google Cloud. You should have access to the group once an administrator approves the request. In this example procedure, it is assumed that your Group Membership request is approved.

**Note:** Group administrators should give expiring membership to users as appropriate to specific business requirements in your enterprise. They must follow the guidance outlined in the [Cloud Identity API documentation](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/groups.memberships#ExpiryDetail). In this document, it's assumed that the user account that you use to set up the Google group in [Create a Google group for privileged access](https://docs.cloud.google.com/architecture/patterns-practices-identity-access-governance-google-cloud#create-a-google-group-for-privileged-access) is the group administrator.
  3. In Cloud Shell, run the following command to set the default project:
         
         gcloud config set project PROJECT_ID
         

Replace `PROJECT_ID` with the project ID that you created earlier in the Create a Google group for privileged access section.

  4. Attempt to list the Compute Engine instances in this project:
         
         gcloud compute instances list
         

You see an error message informing you that your Google Cloud user doesn't have the permission to access Compute Engine resources.

  5. Run the following command:
         
         gcloud compute instances list
         --impersonate-service-account=elevated-compute-access@$PROJECT_ID.iam.gserviceaccount.com
         

This command lists the Compute Engine instances in the project by impersonating the service account that you gained access to when you were given membership to the `elevated-compute-access` Google group.

You see the `example-instance-1` Compute Engine instance that you created with your administrator account.




### Check audit logs

As a Google Cloud administrator, you can access and review the generated audit logs.

  1. Sign in to the Google Cloud console with a user account that has administrative privileges to access audit logs.

  2. In Cloud Logging, enter the following query to review data access logs:
         
         logName="projects/<PROJECT_ID>/logs/cloudaudit.googleapis.com%2Fdata_access"
         AND
         protoPayload.authenticationInfo.principalEmail="elevated-compute-access@PROJECT_ID.iam.gserviceaccount.com"
         

Replace `PROJECT_ID` with your project ID and then run the query.

This query shows you which user in the Google group impersonated the service account to access the Compute Engine instance. It also shows you other relevant details such as when the service account was impersonated and the details of the request headers.

  3. Review the audit log payload, specifically the `protoPayload.authenticationInfo` object in the payload. The username of the user who impersonated the service account is logged as the value of the `principalEmail` key of the `firstPartyPrincipal` object.

  4. As an administrator, you can also review event-threat findings in the Security Command Center dashboard. To learn more about Security Command Center, see [Using Event Threat Detection](https://docs.cloud.google.com/security-command-center/docs/how-to-use-event-threat-detection).




## What's next

  * Learn about [zero trust](https://docs.cloud.google.com/architecture/framework/security/implement-zero-trust).
  * Discover how [Policy Intelligence](https://docs.cloud.google.com/policy-intelligence) offers smart access control for your Google Cloud resources.
  * Read about how you can [troubleshoot policy and access problems on Google Cloud](https://docs.cloud.google.com/vpc/docs/troubleshooting-policy-and-access-problems)
  * Read about best practices for [creating and managing Google Cloud service accounts](https://docs.cloud.google.com/iam/docs/understanding-service-accounts#best_practices).
  * For more reference architectures, diagrams, and best practices, explore the [Cloud Architecture Center](https://docs.cloud.google.com/architecture). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2024-07-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2024-07-11 UTC."],[],[]] 
