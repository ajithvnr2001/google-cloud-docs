---
url: https://docs.cloud.google.com/architecture/identity/assessing-onboarding-plans/
title: Assess onboarding plans \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:08:28.252482+00:00
---

# Assess onboarding plans  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/identity/assessing-onboarding-plans/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Assess onboarding plans Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2024-07-11 UTC

[Cloud Identity](https://docs.cloud.google.com/identity) and [Google Workspace](https://workspace.google.com/) let you manage corporate identities and control access to Google services. To take advantage of the features that Cloud Identity and Google Workspace provide, you first have to onboard existing and new identities to Cloud Identity or Google Workspace. Onboarding involves the following steps:

  * Prepare your Cloud Identity or Google Workspace accounts.
  * If you've decided to [use an external identity provider (IdP)](https://docs.cloud.google.com/architecture/identity/reference-architectures#using_an_external_idp), set up federation.
  * Create user accounts for your corporate identities.
  * Consolidate existing user accounts.



This document helps you assess the best order in which to approach these steps.

## Select an onboarding plan

When you select an onboarding plan, consider the following critical decisions:

  * **Select a target architecture.** Most importantly, you have to decide whether you want to make [Google your primary IdP](https://docs.cloud.google.com/architecture/identity/reference-architectures#using_google_as_idp) or whether you prefer to [use an external IdP](https://docs.cloud.google.com/architecture/identity/reference-architectures#using_an_external_idp).

If you have not yet decided, see the [reference architectures overview](https://docs.cloud.google.com/architecture/identity/reference-architectures) to learn more about possible options.

  * **Decide whether to migrate existing consumer accounts.** If you haven't been using Cloud Identity or Google Workspace, it's possible that your organization's employees might be using [consumer accounts](https://docs.cloud.google.com/architecture/identity/overview-google-authentication#consumer_account) to access Google services. If you want to keep these user accounts and their data, you must migrate them to Cloud Identity or Google Workspace.

For details on consumer accounts, how to identify them, and what risk they might pose to your organization, see [Assessing existing user accounts](https://docs.cloud.google.com/architecture/identity/assessing-existing-user-accounts).




If you've decided to [use an external IdP](https://docs.cloud.google.com/architecture/identity/reference-architectures#using_an_external_idp) and to migrate existing consumer accounts, then you have a third decision to make—deciding whether to set up federation first or migrate existing user accounts first. Take the following factors into account:

  * Migrating consumer accounts requires the owner's consent. The more user accounts you have to migrate, the longer it might take to get the consent of all affected account owners.

If you need to migrate 100 or more consumer accounts, consider setting up federation _before_ you migrate the existing consumer accounts. By setting up federation first, you ensure that all new identities and each migrated user account can immediately benefit from single sign-on, two-step verification, and other security features offered by Cloud Identity and Google Workspace. Setting up federation therefore helps you to quickly improve your overall security posture.

However, setting up federation first requires you to configure your identity provider in a way that [still allows existing user accounts to be migrated](https://docs.cloud.google.com/architecture/identity/assessing-consolidation-impact-on-federation). This configuration can increase the complexity of your overall setup.

  * If you need to migrate fewer than 100 consumer accounts, you can expect the process of migrating these user accounts to be reasonably quick. In this case, consider migrating existing user accounts before setting up federation. By completing the user account migration first, you can avoid the extra complexity of having to configure your identity provider in a way that still allows existing user accounts to be migrated.

However, delaying the federation setup might slow down the process of improving your overall security posture.




The following diagram summarizes how to select the best onboarding plan.

![Selecting the best onboarding plan.](https://docs.cloud.google.com/static/architecture/identity/images/onboarding-plan.svg)

This diagram shows the following decision paths to select an onboarding plan:

  * If you're using Google as an IdP, select plan 1.
  * If you aren't using Google as an IdP, and you don't want to migrate existing accounts, select plan 2.
  * Select plan 3 in the following scenario: 
    * You aren't using Google as an IdP.
    * You want to migrate existing accounts.
    * You want to set up federation first.
  * Select plan 4 in the following scenario: 
    * You aren't using Google as an IdP.
    * You want to migrate existing accounts.
    * You don't want to set up federation first.



## Onboarding plans

This section outlines a set of onboarding plans that correspond to the scenarios discussed in the previous section.

### Plan 1: No federation

Consider using this plan if all of the following are true:

  * You want to [use Google as your primary IdP](https://docs.cloud.google.com/architecture/identity/reference-architectures#using_google_as_idp).
  * You might need to migrate existing user accounts to Cloud Identity or Google Workspace.



The following diagram illustrates the process and steps that this plan involves.

![The no federation plan.](https://docs.cloud.google.com/static/architecture/identity/images/no-federation-plan.svg)

  1. Set up the required Cloud Identity or Google Workspace accounts.

To determine the right number of Cloud Identity or Google Workspace accounts to use, see [Best practices for planning accounts and organizations](https://docs.cloud.google.com/architecture/identity/best-practices-for-planning#use_as_few_accounts_as_possible_but_as_many_as_necessary). For details on how to create the accounts and which stakeholders might need to get involved, see [Prepare your Cloud Identity or Google Workspace accounts](https://docs.cloud.google.com/architecture/identity/preparing-your-g-suite-or-cloud-identity-account#process_for_preparing_an_account).

  2. If some of the identities you want to onboard have existing consumer accounts, don't create user accounts in Cloud Identity or Google Workspace for these identities because doing so would result in a conflicting account.

To minimize the risk of inadvertently creating conflicting accounts, start by creating user accounts for only a small, initial set of identities. We recommend that you use the Admin Console to create these accounts instead of using the API or batch upload to create these user accounts because the Admin Console will warn you about an impending creation of a conflicting account.

  3. Start the process of consolidating your existing user accounts. For details on how to accomplish this and which stakeholders might need to get involved, see [Consolidating existing user accounts](https://docs.cloud.google.com/architecture/identity/overview-consolidating-accounts).

**Note:** You can perform steps 2 and 3 in any order or in parallel.
  4. Finally, create user accounts for all remaining identities that you need to onboard. You can create accounts manually using the Admin Console, or if you're onboarding a large number of identities, consider the following alternatives:

     * Create users in batches [by using a CSV file](https://support.google.com/a/answer/40057).
     * Automate user and group creation by using open source tools such as [Google Apps Manager (GAM)](https://github.com/jay0lee/GAM/wiki/GAM3DirectoryCommands).
     * Use the [Directory API](https://developers.google.com/admin-sdk/directory/v1/reference/users/insert).



### Plan 2: Federation without user account consolidation

Consider using this plan if all of the following are true:

  * You want to [use an external IdP](https://docs.cloud.google.com/architecture/identity/reference-architectures#using_an_external_idp).
  * You don't need to migrate any existing user accounts.



The following diagram illustrates the process and steps that this plan involves.

![Federation without user account consolidation.](https://docs.cloud.google.com/static/architecture/identity/images/federation-without-consolidation.svg)

  1. Set up the required Cloud Identity or Google Workspace accounts.

To determine the right number of Cloud Identity or Google Workspace accounts to use, see [Best practices for planning accounts and organizations](https://docs.cloud.google.com/architecture/identity/best-practices-for-planning). For details on how to create the accounts and which stakeholders might need to get involved in this process, see [Prepare your Cloud Identity or Google Workspace accounts](https://docs.cloud.google.com/architecture/identity/preparing-your-g-suite-or-cloud-identity-account#process_for_preparing_an_account).

  2. Set up federation with your external IdP. Typically, this means configuring automatic user account provisioning and setting up single sign-on.

When you configure federation, take into account the recommendations in [Best practices for federating Google Cloud with an external identity provider](https://docs.cloud.google.com/architecture/identity/best-practices-for-federating).

  3. Use your external IdP to create user accounts in Cloud Identity or Google Workspace for all identities that you need to onboard.

  4. Ensure that [the identities in Cloud Identity or Google Workspace are a subset of the identities in your external IdP](https://docs.cloud.google.com/architecture/identity/best-practices-for-federating#make_cloud_identity_or_g_suite_identities_a_subset_of_the_identities_in_your_external_idp). For details, see [Reconciling orphaned managed user accounts](https://docs.cloud.google.com/architecture/identity/reconciling-orphaned-managed-user-accounts).




### Plan 3: Federation with user account consolidation

Consider using this plan if all of the following are true:

  * You want to [use an external IdP](https://docs.cloud.google.com/architecture/identity/reference-architectures#using_an_external_idp).
  * You need to migrate existing user accounts to Cloud Identity or Google Workspace, but want to set up federation first.



This plan lets you start using single sign-on quickly. Any new user accounts that you create in Cloud Identity or Google Workspace are immediately able to use single sign-on, as are existing user accounts after you've migrated them. This integration with an external IdP lets you minimize user account administration—your IdP can handle both identity onboarding and offboarding.

Compared to the delayed federation plan explained in the next section, this plan increases your risk of conflicting accounts or locked-out users. This plan therefore requires careful attention when you set up federation.

The following diagram illustrates the process and steps that this plan involves.

![Federation with user account consolidation.](https://docs.cloud.google.com/static/architecture/identity/images/federation-with-consolidation.svg)

  1. Set up the required Cloud Identity or Google Workspace accounts.

To determine the right number of Cloud Identity or Google Workspace accounts to use, see [Best practices for planning accounts and organizations](https://docs.cloud.google.com/architecture/identity/best-practices-for-planning). For details on how to create the accounts and which stakeholders might need to get involved in this process, see [Prepare your Cloud Identity or Google Workspace accounts](https://docs.cloud.google.com/architecture/identity/preparing-your-g-suite-or-cloud-identity-account#process_for_preparing_an_account).

  2. Set up federation with your external IdP. Typically, this means that you configure automatic user account provisioning and setting up single sign-on.

Because some of the identities you want to onboard have existing consumer accounts that you still need to migrate, make sure that you prevent your external IdP from interfering with your ability to consolidate existing consumer accounts.

For details on how you can configure your external IdP in a way that is safe for account consolidation, see [Assessing user account consolidation impact on federation](https://docs.cloud.google.com/architecture/identity/assessing-consolidation-impact-on-federation).

When you configure federation, take into account the recommendations in [Best practices for federating Google Cloud with an external identity provider](https://docs.cloud.google.com/architecture/identity/best-practices-for-federating).

  3. Use your external IdP to create user accounts in Cloud Identity or Google Workspace for the initial set of identities that you need to onboard.

Be careful to create user accounts only for identities that don't have an existing user account.

  4. Start the process of consolidating your existing user accounts. For details on how to accomplish this and which stakeholders might need to get involved, see [Consolidating existing user accounts](https://docs.cloud.google.com/architecture/identity/overview-consolidating-accounts).

**Note:** You can perform steps 3 and 4 in any order or in parallel.
  5. To make your setup safe for account consolidation, remove any special configuration that you've applied to your federation setup. Because all existing accounts are already migrated at this point, this special configuration is no longer required.

  6. Use your external IdP to create user accounts in Cloud Identity or Google Workspace for all remaining identities that you need to onboard.




### Plan 4: Delayed federation

Consider using this plan if all of the following are true:

  * You want to [use an external IdP](https://docs.cloud.google.com/architecture/identity/reference-architectures#using_an_external_idp).
  * You need to migrate existing user accounts to Cloud Identity or Google Workspace before setting up federation.



This plan is effectively a combination of no federation and federation without user account consolidation, as discussed earlier. A key benefit of this plan over federation _with_ user account consolidation is the lower risk of conflicting accounts or locked-out users. However, because your plan is to eventually use an external IdP for authentication, the approach has the following downsides:

  * You cannot enable single sign-on before all relevant users have been migrated. Depending on the number of unmanaged accounts you're dealing with and how quickly users react to your account transfer requests, this migration might take days or weeks.

  * During the migration, you have to create new user accounts in Cloud Identity or Google Workspace in addition to creating accounts in your external IdP. Similarly, for employees who leave, you must disable or delete their user accounts in Cloud Identity or Google Workspace, and in the external IdP. This redundant administration increases overall effort and can introduce inconsistencies.




The following diagram illustrates the process and steps that this plan involves.

![Delayed federation.](https://docs.cloud.google.com/static/architecture/identity/images/delayed-federation.svg)

  1. Set up the required Cloud Identity or Google Workspace accounts.

To determine the right number of Cloud Identity or Google Workspace accounts to use, see [Best practices for planning accounts and organizations](https://docs.cloud.google.com/architecture/identity/best-practices-for-planning). For details on how to create the accounts and which stakeholders might need to get involved, see [Prepare your Cloud Identity or Google Workspace accounts](https://docs.cloud.google.com/architecture/identity/preparing-your-g-suite-or-cloud-identity-account#process_for_preparing_an_account). If some of the identities you want to onboard have existing consumer accounts, don't create user accounts in Cloud Identity or Google Workspace for these identities because doing so would result in conflicting accounts.

  2. Start by creating user accounts for only a small, initial set of identities. We recommend that you use the Admin Console to create these accounts instead of using the API or batch upload because the Admin Console will warn you about an impending creation of a conflicting account.

  3. Start the process of consolidating your existing user accounts. For details on how to accomplish this and which stakeholders might need to get involved, see [Consolidating existing user accounts](https://docs.cloud.google.com/architecture/identity/overview-consolidating-accounts).

**Note:** You can perform steps 2 and 3 in any order or in parallel.
  4. Set up federation with your external IdP. Typically, this means configuring automatic user account provisioning and setting up single sign-on.

When you configure federation, take into account the recommendations in [Best practices for federating Google Cloud with an external identity provider](https://docs.cloud.google.com/architecture/identity/best-practices-for-federating).

Because all existing accounts are already migrated at this point, you don't need to apply any special configuration to make federation safe for account consolidation.

  5. Use your external IdP to create user accounts in Cloud Identity or Google Workspace for all identities that you need to onboard.




## What's next

  * If you decided to use federation with user account consolidation, proceed by [assessing user account consolidation impact on federation](https://docs.cloud.google.com/architecture/identity/assessing-consolidation-impact-on-federation).
  * Start your onboarding process by [preparing Cloud Identity or Google Workspace accounts](https://docs.cloud.google.com/architecture/identity/preparing-your-g-suite-or-cloud-identity-account).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2024-07-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2024-07-11 UTC."],[],[]] 
