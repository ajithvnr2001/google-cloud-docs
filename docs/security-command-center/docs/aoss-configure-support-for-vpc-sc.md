---
url: https://docs.cloud.google.com/security-command-center/docs/aoss-configure-support-for-vpc-sc/
title: Configure Assured OSS support for VPC Service Controls \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:38:03.458327+00:00
---

# Configure Assured OSS support for VPC Service Controls  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/aoss-configure-support-for-vpc-sc/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Guides ](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview)



Send feedback 

#  Configure Assured OSS support for VPC Service Controls Stay organized with collections  Save and categorize content based on your preferences. 

Premium and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers) (requires [organization-level activation](https://docs.cloud.google.com/security-command-center/docs/activate-scc-overview#overview_of_organization-level_activation)) The Security Command Center Enterprise service tier will shut down on May 21, 2027. If your organization uses the Enterprise service tier, then the organization will automatically move to the Premium service tier on or after May 21, 2027. Contact your account representative or a [Google Cloud sales specialist](https://cloud.google.com/contact) if you have questions. 

If you enable Assured Open Source Software (Assured OSS) within a VPC Service Controls service perimeter, you must configure egress rules.

This document applies to the premium tier of Assured OSS only.

For more information, see [Configuring egress policies](https://docs.cloud.google.com/vpc-service-controls/docs/configuring-ingress-egress-policies).

## Before you begin

  1. Make sure that you have the [required roles to configure VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/access-control) at the organization level.

  2. Make sure that you know the following information:

     * The service account that you used to set up Assured OSS.
     * The [Artifact Registry service agent](https://docs.cloud.google.com/artifact-registry/docs/ar-service-account) that was created automatically when you set up Assured OSS.
     * The user account that set up Assured OSS.



## Configure the egress rule when downloading binaries

Complete this task for your Artifact Registry repositories and for the Google Cloud resources that initiate downloads (for example, Compute Engine VMs).

Configure the following egress rule:
    
    
    - egressFrom:
        identities:
        - serviceAccount: ASSURED_OSS_EMAIL_ADDRESS
        - serviceAccount: ARTIFACT_REPOSITORY_EMAIL_ADDRESS
        - serviceAccount: OTHER_SERVICE_ACCOUNT_EMAIL_ADDRESS
        - USER_GROUP
      egressTo:
        operations:
        - methodSelectors:
          - method: artifactregistry.googleapis.com/GoRead
          - method: artifactregistry.googleapis.com/MavenRead
          - method: artifactregistry.googleapis.com/NPMRead
          - method: artifactregistry.googleapis.com/PythonRead
          serviceName: artifactregistry.googleapis.com
        resources:
        - projects/855934472549
        - projects/107114433875
    

Replace the following:

  * ASSURED_OSS_EMAIL_ADDRESS: the email address of the service account that you specified when you set up Assured OSS.

  * ARTIFACT_REGISTRY_EMAIL_ADDRESS: the email address of the Artifact Registry service agent.

  * OTHER_SERVICE_ACCOUNT_EMAIL_ADDRESS: the email addresses of other service accounts that require access to the open source packages.

  * USER_GROUP: the groups that require access to the open source packages. For example, `group:my-group@example.com` or `user:alex@example.com`.




## Configure the egress rule when accessing security metadata from the Assured OSS bucket

Complete this task for the user account and service account that you used to set up Assured OSS.

Configure the following egress rule:
    
    
    - egressFrom:
        identities:
        - serviceAccount: ASSURED_OSS_EMAIL_ADDRESS
        - user: ASSURED_OSS_USER_EMAIL_ADDRESS
      egressTo:
        operations:
        - methodSelectors:
          - method: google.storage.objects.get
          - method: google.storage.objects.list
          serviceName: storage.googleapis.com
        resources:
        - projects/107114433875
    

Replace the following:

  * ASSURED_OSS_EMAIL_ADDRESS: the email address of the service account that you specified when you set up Assured OSS.

  * ASSURED_OSS_USER_EMAIL_ADDRESS: the email address of the user account that you used to set up Assured OSS.




## Configure the egress rule when setting up Pub/Sub notifications

Complete this task to set up [Pub/Sub notifications for Assured OSS](https://docs.cloud.google.com/assured-open-source-software/docs/use-notifications).

Create the following egress rule:
    
    
    - egressFrom:
        - serviceAccount: ASSURED_OSS_EMAIL_ADDRESS
        - user: ASSURED_OSS_USER_EMAIL_ADDRESS
      egressTo:
        operations:
        - methodSelectors:
          - method: Subscriber.CreateSubscription
          serviceName: pubsub.googleapis.com
        resources:
        - projects/107114433875
    

Replace the following:

  * ASSURED_OSS_EMAIL_ADDRESS: the email address of the service account that you specified when you set up Assured OSS.

  * ASSURED_OSS_USER_EMAIL_ADDRESS: the email address of the user account that you used to set up Assured OSS.




After you configure the subscription, you can remove this egress rule.

## What's next

  * Learn more about [configuring egress policies](https://docs.cloud.google.com/vpc-service-controls/docs/configuring-ingress-egress-policies).

  * [Enable Security Command Center with VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_security_command_center).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
