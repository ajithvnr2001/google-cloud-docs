---
url: https://docs.cloud.google.com/identity/docs/concepts/overview-allowlisted-domains/
title: Allowlisted Domains API overview \u00a0|\u00a0 Cloud Identity \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:43:24.537035+00:00
---

# Allowlisted Domains API overview  |  Cloud Identity  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/identity/docs/concepts/overview-allowlisted-domains/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Cloud Identity ](https://docs.cloud.google.com/identity/docs)
  * [ Guides ](https://docs.cloud.google.com/identity/docs/set-up-cloud-identity-admin)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Allowlisted Domains API overview

The Cloud Identity Allowlisted Domains API lets workspace administrators programmatically modify or view the [allowlisted domains](https://knowledge.workspace.google.com/admin/domains/allow-external-sharing-with-only-trusted-domains) for a Google Workspace domain.

With the Allowlisted Domains API, you can do the following:

  * Add a domain to the allowlist
  * Remove a domain from the allowlist
  * List the domains in the allowlist
  * Get a specific domain from the allowlist



## Limitations

  * **No bulk operations** : Bulk creation or deletion is not supported using a single API call.
  * **Concurrency** : Concurrent mutations for the same customer aren't supported. Each mutation operation returns a long-running operation (LRO), wait for the existing LRO for the customer to finish before starting a new mutation.
  * **Pagination aborts** : In the event of any domain mutations, ongoing paginated list operations will be aborted with an `ABORTED` error. Pagination must be restarted from the beginning.
  * **Scope** : Initial support for the API is restricted to direct customers. Reseller-managed workflows are not supported.



## What's next

  * To set up Cloud Identity, see [Setting up Cloud Identity](https://docs.cloud.google.com/identity/docs/set-up-cloud-identity-admin).
  * To set up the Allowlisted Domains API, refer to [Setting up the Allowlisted Domains API](https://docs.cloud.google.com/identity/docs/how-to/setup-allowlisted-domains).
  * To add a domain to the allowlist, refer to [Adding a domain to the allowlist](https://docs.cloud.google.com/identity/docs/how-to/create-allowlisted-domains).
  * To list and retrieve domains, refer to [Listing and getting allowlisted domains](https://docs.cloud.google.com/identity/docs/how-to/list-get-allowlisted-domains).
  * To remove a domain from the allowlist, refer to [Removing a domain from the allowlist](https://docs.cloud.google.com/identity/docs/how-to/delete-allowlisted-domains).
  * To view audit logs, refer to [Viewing audit logs](https://docs.cloud.google.com/identity/docs/how-to/view-allowlisted-domains-audit-logs).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
