---
url: https://docs.cloud.google.com/security-command-center/docs/compliance-manager-configure-vpc-sc/
title: Use Compliance Manager with VPC Service Controls \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:13:56.199685+00:00
---

# Use Compliance Manager with VPC Service Controls  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/compliance-manager-configure-vpc-sc/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Guides ](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview)



Send feedback 

#  Use Compliance Manager with VPC Service Controls Stay organized with collections  Save and categorize content based on your preferences. 

Standard, Premium, and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers) The Security Command Center Enterprise service tier will shut down on May 21, 2027. If your organization uses the Enterprise service tier, then the organization will automatically move to the Premium service tier on or after May 21, 2027. Contact your account representative or a [Google Cloud sales specialist](https://cloud.google.com/contact) if you have questions. 

If you enable Compliance Manager within a VPC Service Controls service perimeter, you must configure [egress and ingress rules](https://docs.cloud.google.com/vpc-service-controls/docs/configuring-ingress-egress-policies).

You can adjust the following sample ingress and egress rules to meet your business requirements.

For information about limitations, see [Supported products and limitations](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_compliance_manager).

**Note:** Audit functionality is exclusive to Premium and Enterprise [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers).

## Before you begin

  1. Make sure that you have the [required roles to configure VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/access-control) at the organization level.

  2. To ensure access to resources that exist in the organization or folders, grant the Compliance Manager Admin (`roles/cloudsecuritycompliance.admin`) role at the organization level.

  3. Make sure that you know the following:

     * The email address for the Cloud Security Compliance service agent (`service-org-`ORGANIZATION_ID`@gcp-sa-csc-hpsa.iam.gserviceaccount.com`).

     * If you also use Audit Manager, the email address for the Audit Manager service agent (`service-org-`RESOURCE_ID`@gcp-sa-audit-manager.iam.gserviceaccount.com`), where RESOURCE_ID is your organization ID, folder ID, or project ID.

     * The email addresses of Compliance Manager and Audit Manager users. These users administer Compliance Manager and Audit Managerand perform activities such as audits.

  4. Verify that the Cloud Security Compliance service agent has the required permissions within the perimeter to complete an audit. For more information, see [Audit your environment with Compliance Manager](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-audit).




## Add ingress and egress rules

  1. Add the following ingress rule:
         
         - ingressFrom:
           identities:
           - user: USER_EMAIL_ADDRESS
           sources:
               - accessLevel: "*"
           ingressTo:
             operations:
               - serviceName: securitycenter.googleapis.com
                 methodSelectors:
                   - method: "*"
             resources: "*"
         

Replace USER_EMAIL_ADDRESS with the email address of the Compliance Manager or Audit Manager user.

  2. Add the following ingress rule to permit Compliance Manager to monitor and audit the resources in your Google Cloud organization:
         
         - ingressFrom:
           identities:
           - user: USER_EMAIL_ADDRESS
           sources:
               - accessLevel: "*"
           ingressTo:
             operations:
               - serviceName: cloudsecuritycompliance.googleapis.com
                 methodSelectors:
                   - method: "*"
               - serviceName: auditmanager.googleapis.com
                 methodSelectors:
                   - method: "*"
             resources: "*"
         

Replace USER_EMAIL_ADDRESS with the email address of the Compliance Manager or Audit Manager user.

  3. Configure the following ingress rule to run audits for a project:
         
         - ingressFrom:
           identities:
           - serviceAccount: COMPLIANCE_MANAGER_SERVICE_ACCOUNT_OR_AUDIT_MANAGER_SERVICE_ACCOUNT
           - user: USER_EMAIL_ADDRESS
           sources:
               - accessLevel: "*"
           ingressTo:
             operations:
               - serviceName: cloudasset.googleapis.com
                 methodSelectors:
                   - method: "*"
             resources: "*"
         

Replace the following:

     * USER_EMAIL_ADDRESS: the email address of the Compliance Manager user.

     * COMPLIANCE_MANAGER_SERVICE_ACCOUNT_OR_AUDIT_MANAGER_SERVICE_ACCOUNT: the email address of the Cloud Security Compliance service agent or the Audit Manager service agent. If Audit Manager is enabled, use the Audit Manager service agent.

  4. Configure the following ingress rule to run audits for a folder:
         
         - ingressFrom:
           identities:
           - serviceAccount: COMPLIANCE_MANAGER_SERVICE_ACCOUNT_OR_AUDIT_MANAGER_SERVICE_ACCOUNT
           - user: USER_EMAIL_ADDRESS
           sources:
               - accessLevel: "*"
           ingressTo:
             operations:
                 - serviceName: "*"
             resources: "*"
         

Replace the following:

     * USER_EMAIL_ADDRESS: the email address of the Compliance Manager user.

     * COMPLIANCE_MANAGER_SERVICE_ACCOUNT_OR_AUDIT_MANAGER_SERVICE_ACCOUNT: the email address of the Cloud Security Compliance service agent or the Audit Manager service agent. If Audit Manager is enabled, use the Audit Manager service agent.

Broad access is required to permit auditing of all the resources in the projects within the folder.

  5. Configure the following ingress rule to run an audit when the enrolled Cloud Storage bucket is _inside_ the perimeter:
         
         - ingressFrom:
           identities:
           - serviceAccount: COMPLIANCE_MANAGER_SERVICE_ACCOUNT_OR_AUDIT_MANAGER_SERVICE_ACCOUNT
           - user: USER_EMAIL_ADDRESS
           sources:
               - accessLevel: "*"
           ingressTo:
             operations:
                 - serviceName: storage.googleapis.com
                   methodSelectors:
                     - method: google.storage.buckets.getIamPolicy
                     - method: google.storage.buckets.testIamPermissions
                     - method: google.storage.objects.getIamPolicy
                     - method: google.storage.buckets.setIamPolicy
                     - method: google.storage.objects.setIamPolicy
                     - method: google.storage.objects.create
                     - method: google.storage.objects.get
           resources: "*"
         

Replace the following:

     * USER_EMAIL_ADDRESS: the email address of the Compliance Manager user.

     * COMPLIANCE_MANAGER_SERVICE_ACCOUNT_OR_AUDIT_MANAGER_SERVICE_ACCOUNT: the email address of the Cloud Security Compliance service agent or the Audit Manager service agent. If Audit Manager is enabled, use the Audit Manager service agent.

  6. Configure the following egress rule to run an audit when the enrolled Cloud Storage bucket is _inside_ the perimeter:
         
         - egressFrom:
           identities:
             - serviceAccount: COMPLIANCE_MANAGER_SERVICE_ACCOUNT_OR_AUDIT_MANAGER_SERVICE_ACCOUNT
             - user: USER_EMAIL_ADDRESS
             sources:
               - accessLevel: "*"
           egressTo:
             operations:
                 - serviceName: storage.googleapis.com
                   methodSelectors:
                     - method: google.storage.buckets.getIamPolicy
                     - method: google.storage.buckets.testIamPermissions
                     - method: google.storage.objects.getIamPolicy
                     - method: google.storage.buckets.setIamPolicy
                     - method: google.storage.objects.setIamPolicy
                     - method: google.storage.objects.create
                     - method: google.storage.objects.get
             resources: "*"
         

Replace the following:

     * USER_EMAIL_ADDRESS: the email address of the Compliance Manager user.

     * COMPLIANCE_MANAGER_SERVICE_ACCOUNT_OR_AUDIT_MANAGER_SERVICE_ACCOUNT: the email address of the Cloud Security Compliance service agent or the Audit Manager service agent. If Audit Manager is enabled, use the Audit Manager service agent.




## What's next

  * [Diagnose issues by using the VPC Service Controls troubleshooter](https://docs.cloud.google.com/vpc-service-controls/docs/troubleshooter) or the [VPC Service Controls violation analyzer](https://docs.cloud.google.com/vpc-service-controls/docs/violation-analyzer).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
