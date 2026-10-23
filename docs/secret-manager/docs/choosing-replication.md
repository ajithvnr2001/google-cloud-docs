---
url: https://docs.cloud.google.com/secret-manager/docs/choosing-replication/
title: Choose a secret replication policy \u00a0|\u00a0 Secret Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:34:08.244088+00:00
---

# Choose a secret replication policy  |  Secret Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/secret-manager/docs/choosing-replication/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Secret Manager ](https://docs.cloud.google.com/secret-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/secret-manager/docs/overview)



Send feedback 

#  Choose a secret replication policy Stay organized with collections  Save and categorize content based on your preferences. 

This page describes secret replication policies in Secret Manager. A replication policy lets you choose the locations where you store your secret payload data. You can configure each secret with either automatic replication or user-managed replication when you create a secret. The locations in the replication policy can't be updated.

Regardless of the replication policy you select, Secret Manager ensures [strong consistency](https://en.wikipedia.org/wiki/Strong_consistency) of your data. Replication is a synchronous process. Secret Manager immediately makes the data available across all configured replicas when a secret is created or updated.

## Automatic secret replication policy

A secret with an automatic replication policy has its payload data replicated without restriction. This is the simplest configuration and is recommended for most users. When creating a secret using the Google Cloud CLI or the web UI, this is the default replication policy.

When you choose automatic replication, Secret Manager replicates the secret across multiple regions globally. Google Cloud manages the distribution of your data across these regions to ensure high availability. Automatic replication provides robust protection against single-region failures without requiring manual configuration.

For [billing purposes](https://docs.cloud.google.com/secret-manager/pricing), a secret with an automatic replication policy is considered to be stored in a single location.

For purposes of [resource location organization policy](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations) evaluation, a secret with an automatic replication policy can only be created if resource creation in `global` is allowed.

## User-managed secret replication policy

A secret with a user-managed replication policy has its payload data replicated to a user configured set of locations. The secret can be replicated to any number of [supported locations](https://docs.cloud.google.com/secret-manager/docs/locations). This may be useful if there are requirements around where the secret payload data can be stored.

If you configure replication to multiple regions and one or more regions experience an outage, the create or update action fails. This ensures that your data remains consistent. Secret Manager returns an error message confirming the failure.

For [billing purposes](https://docs.cloud.google.com/secret-manager/pricing), each location in the user-managed replication policy is considered a separate location.

For purposes of [resource location organization policy](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations) evaluation, a secret with a user-managed replication policy can only be created if resource creation is allowed in all the selected locations.

## What's next

  * Learn more about [editing a secret](https://docs.cloud.google.com/secret-manager/docs/edit-secrets).
  * Learn more about [managing access to secrets](https://docs.cloud.google.com/secret-manager/docs/manage-access-to-secrets).
  * Learn more about [setting up rotation policies](https://docs.cloud.google.com/secret-manager/docs/secret-rotation).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
