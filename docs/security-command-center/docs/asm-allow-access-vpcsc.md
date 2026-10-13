---
url: https://docs.cloud.google.com/security-command-center/docs/asm-allow-access-vpcsc/
title: Use Mandiant Attack Surface Management with VPC Service Controls \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:14:16.064593+00:00
---

# Use Mandiant Attack Surface Management with VPC Service Controls  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/asm-allow-access-vpcsc/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Guides ](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview)



Send feedback 

#  Use Mandiant Attack Surface Management with VPC Service Controls Stay organized with collections  Save and categorize content based on your preferences. 

Enterprise (Deprecated) [service tier](https://docs.cloud.google.com/security-command-center/docs/service-tiers) (not available if [data residency controls](https://docs.cloud.google.com/security-command-center/docs/data-residency-support) are enabled) The Security Command Center Enterprise service tier will shut down on May 21, 2027. If your organization uses the Enterprise service tier, then the organization will automatically move to the Premium service tier on or after May 21, 2027. Contact your account representative or a [Google Cloud sales specialist](https://cloud.google.com/contact) if you have questions. 

This document describes how to add ingress rules to allow Mandiant Attack Surface Management within VPC Service Controls perimeters. To restrict services in projects that you want Mandiant Attack Surface Management to monitor if your organization uses VPC Service Controls, perform this task. For more information about Mandiant Attack Surface Management, see [Mandiant Attack Surface Management overview](https://docs.cloud.google.com/security-command-center/docs/concepts-security-sources#mandiant-asm).

## Required roles

To get the permissions that you need to use Mandiant Attack Surface Management within VPC Service Controls perimeters. , ask your administrator to grant you the [Access Context Manager Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/accesscontextmanager#accesscontextmanager.policyEditor) (`roles/accesscontextmanager.policyEditor`) IAM role on your organization. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Create the ingress rules

To allow Mandiant Attack Surface Management in Security Command Center within VPC Service Controls perimeters, add the required ingress rules in those perimeters. Perform these steps for each perimeter that you want Mandiant Attack Surface Management to monitor.

For more information, see [Updating ingress and egress policies for a service perimeter](https://docs.cloud.google.com/vpc-service-controls/docs/configuring-ingress-egress-policies#console).

### Console

#### Navigate to the service perimeter

  1. In the Google Cloud console, go to the **VPC Service Controls** page.

[Go to VPC Service Controls](https://console.cloud.google.com/projectselector2/security/service-perimeter?supportedpurview=organizationId)

  2. Select your organization.
  3. In the drop-down list, select the access policy that contains the service perimeter that you want to grant access to.

The service perimeters associated with the access policy appear in the list.

  4. Click the name of the service perimeter that you want to update.

To find the service perimeter you need to modify, you can check your logs for entries that show `RESOURCES_NOT_IN_SAME_SERVICE_PERIMETER` violations. In those entries, check the `servicePerimeterName` field: 
         
         accessPolicies/ACCESS_POLICY_ID/servicePerimeters/SERVICE_PERIMETER_NAME

  5. Click edit **Edit**.



#### Add an ingress rule

  1. Click **Ingress policy**.
  2. Click **Add an ingress rule**.
  3. In the **From** section, set the following details:

     1. For **Identities > Identity**, select **Select identities & groups**.
     2. Click **Add identities**.
     3. Enter the email address that identifies the Attack Surface Management Service Agent. This address has the following format: 
            
            service-org-ORGANIZATION_ID@gcp-sa-asm-hpsa.iam.gserviceaccount.com

Replace `ORGANIZATION_ID` with your organization ID.

     4. Select the service agent or press `ENTER`, and then click **Add identities**. 
  4. In the **To** section, set the following details:

     1. For **Resources > Projects**, select **All projects**.
     2. For **Operations or IAM roles** , select **Select operations**. 
     3. Click **Add operations** , and then add the following operations:

        * Add the **cloudasset.googleapis.com** service. 
          1. Click **All methods**.
          2. Click **Add all methods**.
        * Add the **cloudresourcemanager.googleapis.com** service. 
          1. Click **All methods**.
          2. Click **Add all methods**.
        * Add the **dns.googleapis.com** service. 
          1. Click **All methods**.
          2. Click **Add all methods**.
  5. Click **Save**.



### gcloud

**Warning:** The `--set-ingress-policies` and `--set-egress-policies` flags replace all existing ingress or egress policies in the perimeter. If you have existing policies, you must retrieve them first, add the new policy to the appropriate ingress or egress YAML file, and then run the update command. 

  1. If a quota project isn't already set, then set it. Choose a project that has the Access Context Manager API enabled. 
         
         gcloud config set billing/quota_project QUOTA_PROJECT_ID

Replace `QUOTA_PROJECT_ID` with the ID of the project that you want to use for billing and quota. 

  2. Create a file named `ingress-rule.yaml` with the following contents:
         
         - ingressFrom:
             identities:
             - serviceAccount:service-org-ORGANIZATION_ID@gcp-sa-asm-hpsa.iam.gserviceaccount.com
             sources:
             - accessLevel: '*'
           ingressTo:
             operations:
             - serviceName: cloudasset.googleapis.com
               methodSelectors:
               - method: '*'
             - serviceName: cloudresourcemanager.googleapis.com
               methodSelectors:
               - method: '*'
             - serviceName: dns.googleapis.com
               methodSelectors:
               - method: '*'
             resources:
             - '*'

Replace `ORGANIZATION_ID` with your organization ID.

  3. Add the ingress rule to the perimeter:
         
         gcloud access-context-manager perimeters update PERIMETER_NAME \
             --set-ingress-policies=ingress-rule.yaml

Replace the following:

     * `PERIMETER_NAME`: the name of the perimeter. For example, `accessPolicies/1234567890/servicePerimeters/example_perimeter`. 

To find the service perimeter you need to modify, you can check your logs for entries that show `RESOURCES_NOT_IN_SAME_SERVICE_PERIMETER` violations. In those entries, check the `servicePerimeterName` field: 
           
           accessPolicies/ACCESS_POLICY_ID/servicePerimeters/SERVICE_PERIMETER_NAME




For more information, see [Ingress and egress rules](https://docs.cloud.google.com/vpc-service-controls/docs/ingress-egress-rules). 

## What's next

  * Learn more about [Mandiant Attack Surface Management](https://docs.cloud.google.com/security-command-center/docs/concepts-security-sources#mandiant-asm).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
