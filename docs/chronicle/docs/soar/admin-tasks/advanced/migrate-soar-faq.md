---
url: https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/advanced/migrate-soar-faq/
title: Frequently Asked Questions on SOAR migration \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:59:59.609367+00:00
---

# Frequently Asked Questions on SOAR migration  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/advanced/migrate-soar-faq/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Frequently Asked Questions on SOAR migration

Supported in:

Google SecOps  [ SOAR ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-soar-toc)

Get answers to common questions about the SOAR migration process. Find solutions to frequent issues and best practices for a successful transition.

### Migration scope and impact

**Q: Why is this migration necessary?**

We're modernizing the SOAR infrastructure by migrating to Google Cloud. This critical upgrade provides key benefits, including enhanced reliability, improved security, greater compliance, and more granular access control. It also gives access to Agentic AI capabilities through Model Context Protocol (MCP) integration.

The migration provides the following: 

  * Enhances SOAR's reliability and monitoring capabilities by utilizing Google's best-in-class API layer. This layer provides a leading API solution with advanced features for quota management, auditing, and observability.
  * Unlocks Role-Based Access Control (RBAC) for features and data throughout the entire platform.
  * Provides higher compliance functionality, such as VPC Service Controls, Data Residency, and Customer-Managed Encryption Keys (CMEK).



**Q: What's the scope of the migration?**

The migration involves the following components:

  * Migrating SOAR project to a customer owned Google Cloud project. 
  * Migrating SOAR authentication and permissions to Google Cloud IAM.
  * Migrating SOAR APIs to Chronicle API.
  * Migrating remote agents authentication infrastructure.



**Q: What are the immediate changes after the migration?**

Immediately following the migration, you'll experience several key changes:

  * **GCP Project Ownership** : Your SOAR project will migrate from Google's ownership to your customer-owned Google Cloud project.
  * **Authentication** : 
    * Unified SecOps customers: No change. Authentication will continue to be managed by Google Cloud IAM.
    * SOAR Standalone customers: Authentication will now be managed by Google Cloud IAM. For users using SAML, this means adopting Workforce Identity Federation, and the SAML configuration will no longer be stored and managed within the SOAR system itself, leading to stronger security controls.
  * **RBAC** : User permissions will become more granular and managed using IAM. Environments and SOC roles will continue to be managed within the SOAR module using Identity Provider (IdP) groups.
  * **Audit Logging** : Audit logs will be more detailed and managed within **Cloud Audit Logs **.
  * **New URL (SOAR only)** : SOAR standalone users will receive a new URL (new domain) for accessing SOAR.



**Q: How are customers / partners being notified of this migration?**

An in-product pop up is displayed for all customers and partners which includes the migration date and a link to a form to fill out. They will be prompted to confirm their migration date and time slot.

**Q: Will our infrastructure costs change as a result of SOAR being bound to our Google Cloud project?**

No, your costs won't be impacted. You shouldn't experience any change on the frontend. No new resources will run in your project, so there are no associated costs.

**Q: How do we connect our project to SOAR?**

Google will migrate your SOAR project to your Google Cloud project. If you are a Unified SecOps customer, we already have your Google Cloud project ID. If you are a SOAR standalone customer, you will need to share your Google Cloud project ID with us.

**Q: For customers who already have a Google SecOps deployment, should we use the same project ID as SIEM, or do we need a separate project?**

For a unified Google SecOps deployment (one SIEM, one SOAR), you should use the existing Google Cloud project ID associated with your SIEM. This allows for unified management of administrative flows, such as RBAC and logs.

**Q: For Google SecOps instances with special considerations such as VPC Service Controls (VPC-SC), what steps are needed?**

To enable the migration, you'll need to define both Ingress and Egress rules within your VPC-SC policy. If your Google Cloud Project has VPC SC, contact the Support team for detailed guidance on these specific rules. 

There are two API features that are not supported using VPC-SC:

  * Webhooks
  * Playbook Approval links



**Q: How can I check that the migration has been successful?**

Check for successful completion by going to **SOAR Settings > License Management**. After Stage 1, it will say **Google.com** after the system version number. After Stage 2 migration of SOAR permissions to IAM roles , it will say both **Google.com** and **CloudIAM Enabled** after the system version number.

### Downtime and continuity

**Q: Is there any downtime during the migration, and what is its impact?**

Yes. The expected downtime is as follows:

  * Up to 2 hours for SOAR standalone customers.
  * Up to 1.5 hours for Google SecOps customers. 



During this period, you won't be able to sign in to the platform. SOAR services (including ingestion, playbooks, jobs) will be paused but SIEM services will continue running in the background. 

**Q: Will data generated during the downtime be automatically ingested once SOAR services resume?**

Yes. Once the system is back online, ingestion and playbooks will resume and process any alerts that were generated or ingested during the downtime.

**Q: What happens to playbooks that are running when downtime begins?**

The playbook service will be turned off before the migration begins, some running playbooks may fail and will either need to be restarted manually or will resume after the migration is complete.

**Q: Is there a rollback or contingency plan if something goes wrong during the migration?**

Yes. The migration process keeps your existing SOAR instance fully intact (though turned off). If the migration process doesn't complete successfully, we can switch back to your existing instance and remove the new one. This rollback process takes up to 30 minutes. We'll perform extensive testing and close monitoring, with on-call staff on standby to ensure successful migration.

If you experience access issues after migration, you likely have an incorrect authentication setup. You will need to coordinate with your Identity, IDP, or Google Cloud administrator to use the [troubleshooting guide](https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/advanced/soar-pre-validation) for identification and resolution. If the problem persists or if it is unrelated to access, open a [Support ticket](https://console.cloud.google.com/support) to document the concern and monitor its resolution.

**Q: When can I migrate to the new SOAR Endpoints v1 in Chronicle API?**

You can migrate to the new SOAR endpoints v1 in Chronicle API from mid January, 2026. 

The legacy SOAR API and API Keys will be deprecated and no longer function after March 31, 2027. To ensure a smooth transition, follow these two mandatory steps:

  1. You must first complete the migration of SOAR Permission Groups to Cloud IAM.
  2. Update your existing scripts and integrations to replace the legacy SOAR API endpoints with the corresponding Chronicle API endpoints.



### Authentication and permissions

**Q: How do I migrate my SOAR permission groups and permissions?**

You will use a migration script in your Google Cloud console to migrate existing permission groups to IAM custom roles. The script also assigns custom roles to users (for Cloud Identity customers) or to IdP groups (for Workforce Identity Federation customers). 

**Q: What if I prefer not to migrate custom permission groups and only use predefined roles?**

You can opt out of the automated migration and manually map IdP groups to Cloud IAM roles instead.

**Q: We're a SOAR standalone customer with a custom SAML provider with manual authentication. If we change this to IdP groups for IdP mapping, what's the impact on existing user accounts?**

Assuming your existing users match one of the groups and permissions are mapped correctly, there shouldn't be any impact on your pre-existing user accounts. However, if users aren't mapped to groups, they won't be able to sign in. If permissions are mapped differently, users will receive new permissions based on the new mapping.

**Q: Are there specific prerequisites for MSSPs using multiple identity providers?**

Customers who have configured multiple identity providers on the SOAR external authentication page, should define Workforce Identity Federation for authentication and create a separate Workforce Pool for each provider. Each provider is associated with a different subdomain. For more information, read [MSSP migration guide](https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/advanced/migrate-soar-mssp-instance).

**Q: How do I authenticate to the Chronicle API?**

Follow the instructions in [Authenticate to Chronicle API](https://docs.cloud.google.com/chronicle/docs/reference/authentication).

**Q: What are the new IPs required to access the new SOAR API?**

It's not required to allow list any IP addresses to access Chronicle API. Optionally, you can allow list the range of IP addresses indicated [here](https://www.gstatic.com/ipranges/goog.json) and [here](https://www.gstatic.com/ipranges/cloud.json).

### Logging and monitoring

**Q: We completed the first stage of migration, but we don't see logs in Cloud Audit Logs Logs.**

Logs are stored in the SOAR platform after the completion of the first migration stage. Logs become available in your Google Cloud project after the completion of the second migration stage.

**Q: Will customers sending SOAR data to a Managed BigQuery (BQ) instance still be able to access this BigQuery data after the migration?**

Yes. The existing managed BigQuery will continue working.

### Logistics and support

**Q: Can I choose a different time slot for the migration?**

No. Migrating outside of the suggested time slots isn't possible. 

**Q: Will we receive real-time status updates during the migration?**

You'll receive an email notification at both the start and end of the migration process.

**Q: Who should we contact if an issue arises post-migration?**

If you experience access issues after migration, the authentication setup is likely incorrect. You will need to coordinate with your Identity, IDP, or Google Cloud administrator to use the [troubleshooting guide](https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/advanced/soar-pre-validation) for identification and resolution. If the problem persists or if it is unrelated to access, open a [Support ticket](https://console.cloud.google.com/support) to document the concern and monitor its resolution.

## Migrate SOAR permissions groups to IAM

The following section addresses common issues encountered during and after migrating permissions to IAM.

### Migration tool and script issues

**Q: Why can't I see or load the migration script in the Google Cloud Console?**

There are two possible reasons for this:

  * **Missing permissions** : The migration tool requires your user account to have sufficient permissions in both the Google Cloud and the Google SecOps instance. Make sure you're logged in with an account that has the required IAM roles in Google Cloud and is also a recognized user in Google SecOps SOAR. Using different accounts for Google Cloud and SOAR can cause authorization failures. If you have the required permissions and still cannot load the migration script, open a [Support ticket](https://console.cloud.google.com/support).

  * **SIEM doesn't use Cloud IAM** : If you are a Google SecOps unified customer, make sure that you are using IAM to manage roles and permissions for the SIEM side of the platform. For more information, refer to [legacy RBAC to Feature RBAC migration guide](https://docs.cloud.google.com/chronicle/docs/administration/migrate-from-legacy-rbac-to-feature-rbac).




**Q I'm getting an error while trying to run the migration scripts. What should I do?**

  * **Error - "Group does not exist"** : When using the `add-iam-policy-binding commands`, make sure you are using the full group email address (for example, `your-group@example.com`) for the `--member` flag, not just the short group name.

  * **Errors related to pre-existing roles** : Conflicts may occur when binding to a principal which already has conditional bindings. To resolve this, rerun the script and make sure to select **None** instead of **Specify a new condition**.




### Access issues post migration

**Q: Why am I getting a "403 Forbidden" error when trying to access certain pages or features (such as Playbooks or IDE) after the IAM migration?**

A 403 error after migration might indicate that the Google Cloud IAM role assigned to your user is missing permissions required by the SOAR side of the Google SecOps platform. This is common if you are using custom IAM roles.

Check the [Google SecOps roles and permissions](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle). Make sure that your custom IAM role includes all the permissions needed to access the required SOAR features.

Optionally, examine your browser's developer tools to identify specific API calls returning a 403 error. The response payload documents the missing permission, and a notification banner also appears within the interface detailing the required access.

If none of these solutions help, open a [Support ticket](https://console.cloud.google.com/support).

### Permissions and roles

**Q: I performed the IAM migration manually without using the provided tool, and now I have permission issues. How can I fix this?**

Manual IAM migration can sometimes result in missing necessary permissions for SOAR roles. We highly recommend using the provided migration script to ensure all required permissions are set up correctly. If you still plan to perform manual migration, carefully review [Google SecOps IAM permissions](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle) to create the custom roles with the needed permissions. 

**Q: Some users seem to have more permissions in SOAR than expected after migration. Why is this happening?**

This can happen if users or groups were already assigned to predefined Chronicle broad Google Cloud roles before the migration. After you complete the migration, Chronicle predefined roles (such as `chronicle.apiAdmin`) will automatically include SOAR permissions. For example, the Chronicle API Admin role will now include SOAR Admin permissions.

To ensure least-privilege access, follow these steps:

  1. Review your predefined roles in [IAM Roles](https://console.cloud.google.com/iam-admin/roles) page, including Chronicle API Admin, to identify all assigned principals (users and groups).
  2. Confirm that only users requiring SOAR permissions are assigned to these roles.
  3. To limit SOAR access for specific principals, remove them from the predefined roles and assign them to a custom role that explicitly excludes SOAR administrator permissions.



**Q: The migration was successful but I can still see the Permissions Groups column in the Group Mapping page. Why?**

After a successful migration, the **Permissions Groups** column in still displayed in the **Group Mapping** page for backwards compatibility. Do not delete these assignments. The column will be removed by November 30, 2026 without any customer impact.

### Best practices

  * **Use the Migration script** : Whenever possible, use the official migration script in Google Cloud to handle the transition from SOAR permission groups to IAM roles.
  * **Review IAM Permissions** : Familiarize yourself with the required Google Cloud IAM permissions for different SOAR functions and roles.
  * **Test Thoroughly** : After migration, test access for different user roles and personas to ensure everything works as expected.
  * **Contact Support** : For any persistent errors or unexpected behavior, contact [Support](https://console.cloud.google.com/support) and provide as much detail as possible.



**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
