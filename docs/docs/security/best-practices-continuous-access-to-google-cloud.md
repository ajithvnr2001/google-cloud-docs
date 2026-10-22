---
url: https://docs.cloud.google.com/docs/security/best-practices-continuous-access-to-google-cloud/
title: Ensure continuous access to Google Cloud \u00a0|\u00a0 Security \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:24:26.244103+00:00
---

# Ensure continuous access to Google Cloud  |  Security  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/docs/security/best-practices-continuous-access-to-google-cloud/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Guides ](https://docs.cloud.google.com/docs/security/overview/whitepaper)



Send feedback 

#  Ensure continuous access to Google Cloud Stay organized with collections  Save and categorize content based on your preferences. 

This document provides recommendations to help you maintain continuous access to Google Cloud resources. Business continuity aims to ensure that your organization can maintain essential operations, even during disruptions like outages or disasters. This goal includes continued employee access when critical services and infrastructure are unavailable.

This document is intended for security or reliability professionals who are responsible for Identity and Access Management (IAM) and for the maintenance of secure access to Google Cloud. This document assumes that you're already familiar with Cloud Identity, Google Workspace, and IAM management.

To help you prepare for outages and ensure continuous access, this document outlines the following recommended steps. You can implement all or some of these steps, but we recommend the following order:

  1. **Set up emergency access.** Enable last-resort access to Google Cloud resources.

We recommend that you set up emergency access for all of your Google Cloud organizations, regardless of your individual business continuity requirements.

  2. **Provide authentication alternatives for critical users.** If your organization uses [single sign-on (SSO)](https://docs.cloud.google.com/architecture/identity/single-sign-on), any disruption that affects your external identity provider (IdP) can affect employees. Users might be unable to authenticate and use Google Cloud.

To reduce the overall impact of an IdP disruption on your organization, provide an authentication alternative for business-critical users to continue to access Google Cloud resources.

  3. **Use a backup IdP.** To let all users access Google Cloud resources during an IdP disruption, you can maintain a fallback IdP.

A fallback IdP can help to further minimize the impact of a disruption, but this option might not be cost-effective for every organization.




The following sections describe these recommended steps and best practices.

## Set up emergency access

The purpose of emergency access is to enable last-resort access to Google Cloud resources and prevent situations in which you might lose access entirely.

Emergency access users are characterized by the following properties:

  * They're users that you create in your Cloud Identity or Google Workspace account.
  * They have the [super admin privilege](https://support.google.com/a/answer/2405986), which provides users with sufficient access to resolve any misconfiguration that affects your Cloud Identity, Google Workspace, or Google Cloud resources.
  * They're not associated with a specific employee in the organization. Therefore, they're exempt from the [Joiner, Mover, and Leaver (JML)](https://bok.idpro.org/article/id/84/#event-trigger) lifecycle of regular user accounts.
  * They're exempt from SSO.



The following sections describe the recommended best practices to follow when you manage and secure emergency access users.

### Create emergency access users for every environment

For Google Cloud environments that host production workloads, emergency access is critical. For Google Cloud environments that are used for testing or staging purposes, a loss of access can still be disruptive.

To ensure continuous access to all of your Google Cloud environments, create and maintain emergency access users in Cloud Identity or Google Workspace for each environment.

### Ensure emergency access redundancy

A single emergency access user is a single point of failure. In this scenario, a broken security key, a lost password, or an account suspension can disrupt access to an account. To mitigate this risk, you can create more than one emergency access user for each Cloud Identity or Google Workspace account.

Emergency access users are highly privileged, so don't create too many of them. For most organizations, we recommend a minimum of two and a maximum of five emergency access users for each Cloud Identity or Google Workspace account.

### Use a separate organizational unit for emergency access users

Emergency access users require a special configuration and they aren't subject to the JML lifecycle that you might follow for other user accounts.

To keep emergency access users separate from regular user accounts, use a dedicated organizational unit (OU) for emergency access users. A separate OU lets you apply custom configurations to only emergency users.

### Use FIDO security keys for 2-Step Verification

Use [Fast IDentity Online (FIDO)](https://fidoalliance.org/) security keys for 2-Step Verification.

Because emergency access users are highly privileged users in your Cloud Identity or Google Workspace account, you must protect these users by using 2-Step Verification.

Among the 2-Step Verification methods that Cloud Identity and Google Workspace support, we recommend that you use FIDO security keys. This method provides protection against phishing and strong security. To ensure that all of your emergency access users use FIDO security keys for 2-Step Verification, do the following:

  * In the OU that contains your emergency access users, [configure 2-Step Verification](https://support.google.com/a/answer/175197) to allow only security keys as the authentication method.
  * For all emergency access users, enable 2-Step Verification.
  * For each emergency access user, enroll two or more FIDO security keys.



When you enroll multiple keys for each user, you help mitigate the risk of losing access due to a broken security key. You also increase the likelihood that the user can access at least one of the keys in an emergency.

It's acceptable to use the same set of security keys for multiple emergency access users. However, it's better to use different security keys for each emergency access user.

### Use physical security controls to protect credentials and security keys

When you store the credentials and security keys of emergency access users, you must balance strong protection with availability during an emergency:

  * Prevent unauthorized personnel from being able to access emergency access user credentials. Emergency access users must use these credentials only in an emergency.
  * Ensure that authorized personnel can access the credentials with minimal delay during an emergency.



We recommend that you don't rely on a software-based password manager. Instead, it's better to rely on physical security controls to protect the credentials and security keys of emergency access users.

When you choose which physical security controls to apply, consider the following:

  * **Improve availability:**
    * Store copies of passwords in multiple physical locations, such as in multiple security vaults in different offices.
    * Enroll multiple security keys for each emergency access user, and store the keys in several relevant office locations.
  * **Improve security:** Store the password and security keys in different locations.



### Avoid automation for password rotation

It might seem beneficial to automate the password rotation for emergency access users. However, this automation might increase the risk of a security compromise. Emergency access users have super admin privileges. To rotate the password of a super-admin user, automation tools or scripts must also have super-admin privileges. This requirement can cause the tools to be attractive targets for attackers.

To ensure that you don't weaken your overall security posture, don't use automation to rotate the passwords.

### Use strong passwords

To help protect emergency access users, make sure that they use a [long and strong password](https://support.google.com/accounts/answer/32040). To enforce a minimum level of password complexity, use a dedicated OU as described earlier, and implement [password requirements](https://support.google.com/a/answer/139399).

Unless you rotate passwords manually, [disable password expiration](https://support.google.com/a/answer/139399) for all of the emergency access users.

### Exclude an emergency access user from access policies

During an emergency, context-aware access policies might cause a situation where even an emergency access user can't access certain resources. To mitigate this risk, [exclude at least one emergency access user](https://docs.cloud.google.com/architecture/secure-apps-resources-using-context-aware-access/best-practices#exempt-emergency-access-users-in-access-levels) from all of the access levels in your access policies.

These exemptions help you ensure that at least one of your emergency access users has continuous access to resources. In the event of an emergency or a misconfigured context-aware access policy, these emergency access users can maintain their access.

### Set up alerts for emergency access user events

Any emergency access user activity outside of an emergency event likely indicates suspicious behavior. To be notified about any events related to activity from emergency access users, [create a reporting rule](https://support.google.com/a/answer/9908423) in the Google Admin console. When you create a reporting rule, you can set conditions such as the following:

  * **Data source:** User log events
  * **Attributes in the _Condition builder_ tab:** The attributes and operators that are used to create a filter for the OU with your emergency access users and the events

For example, you can set attributes and operators to create a filter that's similar to the following conditional statements:
        
        Actor organizational unit Is /Privileged
        
        AND
        
        (Event Is Successful login OR Event Is Failed login OR Event Is Account
        password change)
        

  * **Threshold:** Every 1 hour when count > 0

  * **Action:** Send email notifications

  * **Email recipients:** Select a group that contains the relevant members of your security team




## Provide authentication alternatives for critical users

If your organization uses SSO to let employees authenticate to Google services, then the availability of your third-party IdP becomes critical. Any disruption to your IdP can prevent employees from accessing essential tools and resources.

Although emergency access helps you ensure continuous administrative access, it doesn't address the needs of employees during an IdP outage.

To reduce the potential effect of an IdP interruption, you can configure your Cloud Identity or Google Workspace account to use an authentication fallback for critical users. You can use the following fallback plan:

  * During normal operations, you let users authenticate by using SSO.
  * During an IdP outage, you selectively disable SSO for these critical users and let them authenticate by using Google sign-in credentials, which you provision in advance.

**Note:** To selectively disable SSO for privileged users, a user must have super admin privileges. This action might also [require multi-party approval](https://support.google.com/a/answer/13790448).

The following sections describe the recommended best practices when you let critical users authenticate during external IdP outages.

### Focus on privileged users

For critical users to authenticate during an IdP outage, the users must have valid Google sign-in credentials like the following:

  * A password with a security key for second-factor authentication.
  * A passkey.



When you provision Google sign-in credentials for users who normally use SSO, you might increase the operational overhead and user friction in the following ways:

  * You might not be able to synchronize user passwords automatically, depending on your IdP. Therefore, you might have to ask users to set a password manually.
  * You might need to request that users register a passkey or enroll in 2-Step Verification. This step isn't usually required for SSO users.



To balance the benefits of uninterrupted access to Google services with the extra overhead, focus on privileged and business-critical users. These users are more likely to benefit significantly from uninterrupted access, and they might be only a fraction of your overall user base.

### Enable post-SSO verification for privileged users

When you provision alternative authentication for privileged users, an unintended result might be additional overhead. To help offset this overhead, you can also enable post-SSO verification for these users.

By default, when you set up SSO for your users, they aren't required to perform 2-Step Verification. Although this practice is convenient, a compromised IdP introduces risk. Any user who doesn't have post-SSO verification enabled can become a target for [credential forgery attacks](https://attack.mitre.org/techniques/T1606/002/).

[Post-SSO verification](https://support.google.com/a/answer/6002699) helps you mitigate the potential effect of an IdP compromise because users must perform 2-Step Verification after each SSO attempt. If you provision Google sign-in credentials for privileged users, post-SSO verification can help improve the security posture of these user accounts without additional overhead.

### Use a separate OU for privileged users

Privileged users who can authenticate during external IdP outages require a special configuration. This configuration differs from the configuration for regular users and for emergency access users.

To help you keep privileged users separate from these other user accounts, use a dedicated OU for privileged users. This separate OU helps you apply custom policies such as post-SSO verification to only these privileged users.

A separate OU also helps you selectively disable SSO for privileged users during an IdP outage. To disable SSO for the OU, you can [modify the SSO profile assignments](https://support.google.com/a/answer/12032922).

## Use a backup IdP

When you provide authentication alternatives for critical users during IdP outages, you help reduce the effect of that IdP outage on your organization. However, this mitigation strategy might not be sufficient to maintain full operational capacity. Many users might still be unable to access essential applications and services.

To further reduce the potential effect of an IdP outage, you can fail over to a backup IdP. You can use the following backup plan:

  * During normal operations, you let users authenticate by using SSO and your primary IdP.
  * During an IdP outage, you change the SSO configuration of your Cloud Identity or Google Workspace account to switch to the backup IdP.



The backup IdP doesn't need to be from the same vendor. When you create a backup IdP, use a configuration that matches the configuration of your primary IdP. To ensure that the backup IdP lets all of your users authenticate and access Google services, the backup IdP must use an up-to-date copy of the primary IdP's user base.

A backup IdP can help provide comprehensive contingency access. However, you must weigh these advantages against the additional risks that a backup IdP might introduce. These potential risks include the following:

  * If the backup IdP has weaker security than the primary IdP, the overall security posture of your Google Cloud environment might also be weaker during a failover.
  * If the primary IdP and backup IdP differ in [how they issue SAML assertions](https://docs.cloud.google.com/architecture/identity/single-sign-on), the IdP might put users at risk of spoofing attacks.

**Note:** To change the SSO configuration to switch to the backup IdP, a user must have super admin privileges. This action might also [require multi-party approval](https://support.google.com/a/answer/13790448).

The following sections describe the recommended best practices when you use a backup IdP for contingency access.

### Create a separate SAML profile for the backup IdP

Cloud Identity and Google Workspace let you create multiple SAML profiles. Each SAML profile can refer to a different SAML IdP.

To minimize the amount of work that's required to fail over to the backup IdP, prepare a SAML profile for the backup IdP in advance:

  * Create separate SAML profiles for your primary IdP and for your backup IdP.
  * Configure [SSO profile assignments](https://support.google.com/a/answer/12032922) to assign only the primary IdP's SAML profile during normal operations.
  * Modify SSO profile assignments to use the backup IdP's SAML profile during an IdP outage. Don't change the individual SAML profile settings.



### Use an existing on-premises IdP

You don't need to provision an additional IdP to serve as the backup. Instead, check whether you can use an existing on-premises IdP for this purpose. For example, your organization might use Active Directory as its authoritative identity source and [Active Directory Federation Services (AD FS) for SSO](https://docs.cloud.google.com/architecture/identity/federating-gcp-with-active-directory-configuring-single-sign-on). In this scenario, you might be able to use AD FS as the backup IdP.

This reuse approach can help you limit cost and maintenance overhead.

### Prepare the backup IdP to handle the required load

When you switch authentication to the backup IdP, it must handle all of the authentication requests that your primary IdP normally handles.

When you deploy and size a backup IdP, remember that the number of expected requests depends on the following factors:

  * The number of users in your Cloud Identity or Google Workspace account.
  * The configured [Google Cloud session length](https://support.google.com/a/answer/9368756).



For example, if the session length is between 8 and 24 hours, the authentication requests might spike during the morning hours when employees begin their workday.

### Test the failover procedure periodically

To help ensure that the SSO failover process works reliably, you must periodically verify the process. When you test the failover procedure, do the following:

  * Manually modify the [SSO profile assignment](https://support.google.com/a/answer/12032922) of one or more OUs or groups to use the backup IdP.
  * Verify that SSO with the backup IdP works as expected.
  * Verify that signing certificates are up to date.



## What's next

  * Review the [security best practices for administrator accounts](https://support.google.com/a/answer/9011373).
  * Learn more about [best practices for federating Google Cloud with an external identity provider](https://docs.cloud.google.com/architecture/identity/best-practices-for-federating).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
