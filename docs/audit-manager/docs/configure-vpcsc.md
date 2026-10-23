---
url: https://docs.cloud.google.com/audit-manager/docs/configure-vpcsc/
title: Configure VPC Service Controls for Audit Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:19:08.926640+00:00
---

# Configure VPC Service Controls for Audit Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/audit-manager/docs/configure-vpcsc/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Audit Manager ](https://docs.cloud.google.com/audit-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/audit-manager/docs/overview)



Send feedback 

#  Configure VPC Service Controls for Audit Manager Stay organized with collections  Save and categorize content based on your preferences. 

Google Cloud VPC Service Controls lets you set up a service perimeter to guard against data exfiltration. Configure Audit Manager with [VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview) so that Audit Manager can access resources and services outside its service perimeter.

## Before you begin

  1. Make sure that you have the [required roles to configure VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/access-control) at the organization level.
  2. Make sure that you have the following information, depending on whether you are enrolling a resource or running an audit in Audit Manager. 
     1. **When you enroll a resource for auditing** : the Google Cloud user account that you specified when you set up Audit Manager.
     2. **When you run an audit** : the [Audit Manager service agent](https://docs.cloud.google.com/audit-manager/docs/enroll-resource) that was created automatically when you enroll a resource for auditing.



## Limitations

  * You can't use a perimeter to protect folder level or organization level Audit Manager resources. To manage Audit Manager permissions at the folder or organization level, we recommend using IAM. For more information, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).



## Configure the ingress and egress rules

Configure ingress and egress rules based on the service perimeter configuration. For more information, see [Service perimeter overview](https://docs.cloud.google.com/vpc-service-controls/docs/service-perimeters).

You may have to [configure the ingress and egress rules](https://docs.cloud.google.com/vpc-service-controls/docs/configuring-ingress-egress-policies) when you perform the following actions:

  1. Enroll a resource for auditing
  2. Run an audit



### Configure ingress and egress rules when you enroll a resource for auditing

You can [enroll an organization, a folder, or a project as a resource for auditing](https://docs.cloud.google.com/audit-manager/docs/enroll-resource) in Audit Manager.

You must configure ingress or egress rules when any of the following resources are not within the same service perimeter:

  * the Audit Manager service agent
  * the Cloud Storage bucket configured as the destination to store the audit data
  * the services involved in the audit process



The Cloud Storage methods in the following samples are required. You can adjust the following sample ingress and egress rules to meet your business requirements.

Complete the following tasks for the Google Cloud user account that you specified when you set up Audit Manager.

  1. Configure the following ingress rule:
         
         - ingressFrom:
             identities:
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

     * USER_EMAIL_ADDRESS: the email address that you specified when you set up Audit Manager
  2. Configure the following egress rule:
         
         - egressFrom:
            identities:
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

     * USER_EMAIL_ADDRESS: the email address that you specified when you set up Audit Manager



### Configure the ingress and egress rules when you run an audit

You can [run an audit](https://docs.cloud.google.com/audit-manager/docs/run-audit) against a framework.

Configure the following ingress or egress rules when the folder or project that is being audited and the enrolled Cloud Storage bucket are in different service perimeters.

The Cloud Storage methods in the following samples are required. You can adjust the following sample ingress and egress rules to meet your business requirements.

#### Configure the ingress rule when you run an audit for folders

Configure the following ingress rule when you run an audit for a folder and the enrolled Cloud Storage bucket or one of the projects within the folder is _inside_ the perimeter.

Complete this task for the Audit Manager service account.
    
    
    - ingressFrom:
        identities:
        - serviceAccount: SA_EMAIL_ADDRESS
        - user: USER_EMAIL_ADDRESS
        sources:
            - accessLevel: "*"
      ingressTo:
        operations:
            - serviceName: "*"
        resources: "*"
    

Replace the following:

  * SA_EMAIL_ADDRESS: the email address of the Audit Manager service account
  * USER_EMAIL_ADDRESS: the email address that you specified when you set up Audit Manager



#### Configure the ingress rule when the enrolled Cloud Storage bucket is inside a service perimeter

Configure the following ingress rule if the audit is run for a project and the enrolled Cloud Storage bucket is _inside_ a service perimeter.

Complete this task for the Audit Manager service account.
    
    
    - ingressFrom:
        identities:
        - serviceAccount: SA_EMAIL_ADDRESS
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

  * SA_EMAIL_ADDRESS: the email address of the Audit Manager service account
  * USER_EMAIL_ADDRESS: the email address that you specified when you set up Audit Manager



#### Configure the egress rule when the enrolled Cloud Storage bucket is outside a service perimeter

Configure the following egress rule if the audit is run for a project within a service perimeter and the enrolled Cloud Storage bucket is _outside_ the perimeter.

Complete this task for the project that contains the Cloud Storage bucket.
    
    
    - egressFrom:
       identities:
          - serviceAccount: SA_EMAIL_ADDRESS
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

  * SA_EMAIL_ADDRESS: the email address of the Audit Manager service account
  * USER_EMAIL_ADDRESS: the email address that you specified when you set up Audit Manager



If you encounter issues with VPC Service Controls, use the VPC Service Controls violation analyzer to debug and analyse the issue. For more information, see [Diagnose an access denial using unique ID in violation analyzer](https://docs.cloud.google.com/vpc-service-controls/docs/troubleshooter).

## What's next

  * Learn more about [VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview).
  * See the Audit Manager entry in the [VPC Service Controls supported products table](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_audit_manager).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
