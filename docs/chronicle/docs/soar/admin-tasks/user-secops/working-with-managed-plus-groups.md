---
url: https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/user-secops/working-with-managed-plus-groups/
title: Work with Managed and Managed-Plus user groups \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T12:01:13.424454+00:00
---

# Work with Managed and Managed-Plus user groups  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/user-secops/working-with-managed-plus-groups/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Work with Managed and Managed-Plus user groups

Supported in:

Google SecOps  [ SOAR ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-soar-toc)

This document outlines the Managed and Managed-plus user groups, which are specifically designed for the end customers of a Managed Security Service Provider (MSSP). These user types offer a flexible level of platform access, acting as a hybrid between the collaborator and full user roles.

## Explore the managed user types

This section defines the managed user types and how they offer a flexible level of platform access, acting as a hybrid between the collaborator and full user roles.

### Managed user

The Managed user role is ideal for MSSPs who want to operate a hybrid SOC in collaboration with their customers. A Managed user has full case management capabilities within their own environment, similar to an MSSP analyst.

### Managed-Plus user

A Managed-Plus user has all the same permissions as a Managed user, with the added ability to build and edit playbooks within their own environment.

Managed-Plus users can view playbooks running in their environment, including those configured for **All environments** playbooks. However, they can't edit playbooks if they don't have permissions for all environments associated with that playbook. For example, a user with permissions only for the "North England" environment would be able to view, but not edit, a playbook running across "North England," "South England," and "East England." Furthermore, this user wouldn't even see that the playbook is running on the "South England" and "East England" environments.

The MSSP is responsible for managing the Content Hub, configuring integrations and agents, and customizing actions in the Integrated Development Environment (IDE) for the Managed-plus user.

## Create a Managed or Managed-Plus user group

The high-level steps to add a new managed or managed-plus user are the same as that of adding other types of users:

  1. Make sure you've purchased the Enterprise license, which gives you access to unlimited users.
  2. Create a new Managed or Managed-Plus permissions group or use the predefined Managed or Managed-Plus group.



For more information, see [Work with permission groups](https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/permissions/working-with-permission-groups).

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
