---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/workforce-identity-federation/
title: Access Backup and DR with Workforce Identity Federation \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:43:49.356587+00:00
---

# Access Backup and DR with Workforce Identity Federation  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/workforce-identity-federation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Reference ](https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/reference)



Send feedback 

#  Access Backup and DR with Workforce Identity Federation Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to configure user access for Backup and DR with Workforce Identity Federation.

[Workforce Identity Federation](https://docs.cloud.google.com/iam/docs/workforce-identity-federation) lets you use an external identity provider (IdP) to authenticate and authorize a workforce—a group of _users_ , such as employees, partners, and contractors—using IAM, so that the users can access Google Cloud services.

If Workforce Identity Federation is configured in your project, users in your workforce can access the following:

  * Backup and DR in [Google Cloud console](https://console.cloud.google)
  * appliance management console



## Set up access to Backup and DR with Workforce Identity Federation

This section describes how to configure access for Workforce Identity Federation users to Backup and DR.

### Configure your identity provider

Use the [Configure Workforce Identity Federation](https://docs.cloud.google.com/iam/docs/configuring-workforce-identity-federation#configure_workforce_identity_federation) guide to configure the Workforce Identity Federation for your identity provider.

### Grant IAM roles to Workforce Identity Federation users

users, so that they can access Backup and DR and the appliance management console to protect workloads:

  * For a list of roles specific to Backup and DR, see [Grant roles to users](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-control).
  * For instructions about assigning these roles to external users, see [Grant IAM roles to principals](https://docs.cloud.google.com/iam/docs/configuring-workforce-identity-federation#grant_roles_to_principals).
  * The formats used for representing Workforce Identity Federation users in IAM policies, see [Represent workforce pool users in IAM policies](https://docs.cloud.google.com/iam/docs/configuring-workforce-identity-federation#representing-workforce-users).



Backup and DR handles Workforce Identity Federation users the same way as Google Account users–instead of an email address, a [principal identifier](https://docs.cloud.google.com/iam/docs/configuring-workforce-identity-federation#representing-workforce-users) is used.

## Access the Backup and DR page in the Google Cloud console

The [Google Cloud Workforce Identity Federation console](https://docs.cloud.google.com/iam/docs/workforce-console-learn-more) provides access to the Backup and DR page.

From the **Backup and DR** page in [Google Cloud Workforce Identity Federation console](https://console.cloud.google), you can deploy the appliance management console, backup/recovery appliances, and view Backup and DR logs. You can also access the appliance management console to back up resources.

## Access the appliance management console

Workforce Identity Federation users access the appliance management console through a different URL than Google-managed users, as follows:

  * The URL for Workforce Identity Federation users is
        
        https://bmc-PROJECT_NUMBER-GENERATED_ID-dot-REGION.backupdr.byoid.googleusercontent.com/
        

  * The URL for Google managed user accounts is
        
        https://bmc-PROJECT_NUMBER-GENERATED_ID-dot-REGION.backupdr.googleusercontent.com/
        




Only users that are authenticated with external identities can access the URL for external identities. If a user visits the URL for external identities while not logged in, they are first redirected to the authentication portal where they specify their workforce pool provider name. Then they are redirected to their identity provider to sign in, and finally they are redirected to the appliance management console.

Workforce Identity Federation users cannot directly access the appliance management console using the URL shared by Google-managed users. To access the appliance management console as a Workforce Identity Federation user, manually update the link to URL for Workforce Identity Federation users.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
