---
url: https://docs.cloud.google.com/identity/docs/how-to/create-allowlisted-domains/
title: Adding a domain to the allowlist \u00a0|\u00a0 Cloud Identity \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:10:36.893963+00:00
---

# Adding a domain to the allowlist  |  Cloud Identity  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/identity/docs/how-to/create-allowlisted-domains/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Cloud Identity ](https://docs.cloud.google.com/identity/docs)
  * [ Guides ](https://docs.cloud.google.com/identity/docs/set-up-cloud-identity-admin)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Adding a domain to the allowlist

This page explains how to add a domain to the allowlist by using the Allowlisted Domains API.

## Before you begin

  * Read the [Allowlisted Domains API overview](https://docs.cloud.google.com/identity/docs/concepts/overview-allowlisted-domains).
  * [Set up the Allowlisted Domains API](https://docs.cloud.google.com/identity/docs/how-to/setup-allowlisted-domains).



## Key considerations

  * **Immutable design** : Because domain names cannot be modified, updates must be performed by deleting the existing entry and creating a new one.
  * **Throughput** : The system supports a quota of roughly 1 Query Per Second (QPS) shared across all domains for any unique customer account.
  * **Capacity** : Administrators can add a maximum of 5,000 domains for any single customer account.



## Adding a domain to the allowlist

Use the `create` method to add a new entry. This mutation is asynchronous and returns a Long-Running Operation (LRO).

###  Python 
    
    
    def create_allowlisted_domain(service, domain_name):
      """Creates an allowlisted domain."""
      try:
        payload = {'domain': domain_name}
        response = service.allowlistedDomains().create(body=payload).execute()
        return response
      except Exception as e:
        print(f'An error occurred during create: {e}')
        return None
    

## Error Handling

Error Condition | RPC Status Code | Error Message | Troubleshooting / Justification  
---|---|---|---  
**Not authorized to the resource** | `PERMISSION_DENIED (403)` | `"Permission denied for allowlisted domain resource."` | • Ensure the user has the appropriate scope granted.  
• Ensure the user has required permission.  
• Reach out to the contact email to ensure if the project/user has been allowlisted or not.  
**Customer ID not found for the user** | `NOT_FOUND (404)` | `"Customer ID not found for user."` | The logged in user is not linked to a valid domain.  
**An allowlist update is already in progress.** | `FAILED_PRECONDITION (400)` | `"An allowlist update is already in progress. Please wait for it to complete before making another request."` | Wait for previous mutations to get complete.  
**Domain limit in the allowlist has been reached.** | `FAILED_PRECONDITION (400)` | `"Allowlisted domain limit has been reached."` | The maximum capacity of 5,000 domains has been reached for the customer account; no more domains can be added.  
**Domain name empty** | `INVALID_ARGUMENT (400)` | `"Domain name cannot be empty."` | Double check the domain passed to the create request. It shouldn't be empty.  
**Domain name invalid** | `INVALID_ARGUMENT (400)` | `"Invalid domain name: <domain>."` | The domain name provided in the request is malformed or invalid. This error typically occurs in one of the following scenarios:  
• **Syntactic invalidity** : The domain name does not conform to the required formatting standards.  
• **Restricted domains** : The following specific domains are restricted and cannot be added to the allowlist:  
• `aol.com`  
• `gmail.com`  
• `hotmail.com`  
• `mail.ru`  
• `outlook.com`  
• `web.de`  
• `yahoo.com`  
• `yandex.com`  
• `yandex.ru`  
  
## Audit Logs

Creations using the Allowlisted Domains API generate audit log events that can be reviewed by administrators. For more information, see [Viewing audit logs](https://docs.cloud.google.com/identity/docs/how-to/view-allowlisted-domains-audit-logs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
