---
url: https://docs.cloud.google.com/looker/docs/best-practices/how-to-change-the-looker-instance-url/
title: How to change the URL of a Looker instance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:44:01.495847+00:00
---

# How to change the URL of a Looker instance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/best-practices/how-to-change-the-looker-instance-url/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Best Practices ](https://docs.cloud.google.com/looker/docs/best-practices/home)



Send feedback 

#  How to change the URL of a Looker instance Stay organized with collections  Save and categorize content based on your preferences. 

Admins can customize the name of the domain or hostname in the URL for a Looker instance. 

Looker-hosted instance URLs take these forms:
    
    
    https://<hostname>.<subdomain>.<domain>.com

or
    
    
    http://<hostname>.<subdomain>.<domain>.com

Admins of Looker-hosted instances can modify each component of the instance URL (except for the subdomain, if present, which may be determined by the region where the instance is hosted), but some changes or additions may incur additional costs or require [embedded analytics](https://looker.com/product/embedded-analytics). Contact a [Google Cloud sales specialist](https://cloud.google.com/contact) to discuss the options available for your Looker deployment. 

In addition to these elective changes, the instance URL may also be affected if your deployment: 

  * Migrates from legacy hosting on Amazon EC2 to next-generation hosting on Google Cloud or Amazon Elastic Kubernetes Service (EKS) 
  * Migrates from customer-hosted to Looker-hosted
  * Migrates from Looker (original) to [Looker (Google Cloud core)](https://docs.cloud.google.com/looker/docs/looker-core-overview)
  * Changes its AWS EC2 hosted region (which may change the subdomain, if present) 



## What should I be aware of before initiating a URL change?

Your instance can use only one `cloud.looker.com` domain at a time. To make your Looker instance accessible from multiple URLs, you must configure a custom domain. To configure a custom domain for a Looker-hosted (original) instance, see [Configure custom domains for Looker-hosted instances](https://docs.cloud.google.com/looker/docs/looker-hosted-custom-domain). To configure a custom domain for a Looker (Google Cloud core) instance, see [Set up a custom domain for a Looker (Google Cloud core) instance that uses public connections](https://docs.cloud.google.com/looker/docs/looker-core-custom-domain). 

In most cases, if the instance URL is changing, a Looker admin must update the **Host URL** field on the **Settings** page in the **Admin** panel with the new URL. If an instance URL is changing because of a migration from Looker (original) to Looker (Google Cloud core), the **Host URL** option is not available in Looker (Google Cloud core), and that step isn't necessary. 

If your instance uses an authentication method like [SAML](https://docs.cloud.google.com/looker/docs/admin-panel-authentication-saml) or [LDAP](https://docs.cloud.google.com/looker/docs/admin-panel-authentication-ldap), you must point the identity provider configuration to the new URL, or your users may get locked out. 

There could be a momentary service interruption associated with making a change to the instance URL. Depending on your deployment, updating the host URL may result in the following breaking changes. 

Instance change | Example | Type of change | Breaking change  
---|---|---|---  
Migrating from legacy hosting on Amazon EC2 to next-generation hosting on Google Cloud or Amazon EKS  |  `company.looker.com` to `company.cloud.looker.com` | Changes subdomain |  Users and embed users must update their bookmarks within seven days, or their bookmarks will break. Both URLs will work for seven days after the change.  If using the [Slack integration](https://docs.cloud.google.com/looker/docs/scheduling-slack) for data deliveries, any deliveries sent by users who are not already logged into Slack won't be delivered. Existing schedules and ad hoc deliveries sent by users who are already authenticated into the Slack workspace won't be affected.   
Migrating from customer-hosted to Looker-hosted |  `company.instance.com` to `company.cloud.looker.com` | Changes domain |  Users and embed users must update their bookmarks, or their bookmarks will break. How long the customer-hosted instance URL operates is up to the discretion of the company.  If using the [Slack integration](https://docs.cloud.google.com/looker/docs/scheduling-slack) for data deliveries, any deliveries sent by users who are not already logged into Slack won't be delivered. Existing schedules and ad hoc deliveries sent by users who are already authenticated into the Slack workspace won't be affected.   
Migrating from Looker (original) to Looker (Google Cloud core) |  `company.looker.com` to `hostname.looker.app` | Changes domain |  Bookmarks to Looker (original) instances that use the `looker.com` domain cannot be preserved after migration to Looker (Google Cloud core). Users and embed users must update their bookmarks, or their bookmarks will break. If moving from a [custom URL for Looker (original)](https://docs.cloud.google.com/looker/docs/admin-panel-general-settings#host_url) (that doesn't use the `looker.com` domain) to the same [custom domain for Looker (Google Cloud core)](https://docs.cloud.google.com/looker/docs/looker-core-custom-domain), bookmarks should migrate without breaking.  There is a small set of [feature differences](https://docs.cloud.google.com/looker/docs/looker-core-feature-differences) between Looker (original) and Looker (Google Cloud core). Review these differences to ensure that the features in Looker (Google Cloud core) meet your ongoing needs. See the [migration documentation](https://docs.cloud.google.com/looker/docs/looker-core-self-service-migration#finalize-setup) for more information about migrating from Looker (original) to Looker (Google Cloud core).   
Changing AWS EC2 hosted regions |  `company.au.looker` to `company.jp.looker.com` | Changes subdomain |  Users and embed users must update their bookmarks within seven days, or their bookmarks will break. Both URLs will work for seven days after the change.  If using the [Slack integration](https://docs.cloud.google.com/looker/docs/scheduling-slack) for data deliveries, any deliveries sent by users who are not already logged into Slack won't be delivered. Existing schedules and ad hoc deliveries sent by users who are already authenticated into the Slack workspace won't be affected.   
Switching the order of the domain |  `example.looker.com` to `looker.example.com` | Changes domain |  Both instance URLs will work indefinitely. If using the [Slack integration](https://docs.cloud.google.com/looker/docs/scheduling-slack) for data deliveries, any deliveries sent by users who are not already logged into Slack won't be delivered. Existing schedules and ad hoc deliveries sent by users who are already authenticated into the Slack workspace won't be affected.   
Switching to a custom domain |  `example.looker.com` to `example.custom.com` | Changes domain |  Both instance URLs will work indefinitely. If using the [Slack integration](https://docs.cloud.google.com/looker/docs/scheduling-slack) for data deliveries, any deliveries sent by users who are not already logged into Slack won't be delivered. Existing schedules and ad hoc deliveries sent by users who are already authenticated into the Slack workspace won't be affected.   
Changing from one Looker host to another |  `company1.cloud.looker.com` to `company2.cloud.looker.com` | Changes domain |  Users and embed users must update their bookmarks within seven days, or their bookmarks will break. Both URLs will work for seven days after the change.  If using the [Slack integration](https://docs.cloud.google.com/looker/docs/scheduling-slack) for data deliveries, any deliveries sent by users who are not already logged into Slack won't be delivered. Existing schedules and ad hoc deliveries sent by users who are already authenticated into the Slack workspace won't be affected.  Hostnames for Looker instances may contain only alphanumeric characters and must be 6 characters or longer. This means that they can't have dashes, such as: customer-dev.looker.com.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
