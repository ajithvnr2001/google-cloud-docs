---
url: https://docs.cloud.google.com/identity/docs/how-to/delete-allowlisted-domains/
title: Removing a domain from the allowlist \u00a0|\u00a0 Cloud Identity \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:10:38.801846+00:00
---

# Removing a domain from the allowlist  |  Cloud Identity  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/identity/docs/how-to/delete-allowlisted-domains/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Cloud Identity ](https://docs.cloud.google.com/identity/docs)
  * [ Guides ](https://docs.cloud.google.com/identity/docs/set-up-cloud-identity-admin)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Removing a domain from the allowlist

This page explains how to remove a domain from the allowlist by using the Allowlisted Domains API.

## Before you begin

  * Read the [Allowlisted Domains API overview](https://docs.cloud.google.com/identity/docs/concepts/overview-allowlisted-domains).
  * [Set up the Allowlisted Domains API](https://docs.cloud.google.com/identity/docs/how-to/setup-allowlisted-domains).



## Removing a domain from the allowlist

Use the `delete` method to remove a domain. This mutation is asynchronous and returns a Long-Running Operation (LRO).

###  Python 
    
    
    def delete_allowlisted_domain(service, resource_name):
      """Deletes an allowlisted domain."""
      if not resource_name:
        print('Resource name is missing.')
        return None
    
      try:
        response = (
            service.allowlistedDomains().delete(name=resource_name).execute()
        )
        return response
      except Exception as e:
        print(f'An error occurred during delete: {e}')
        return None
    

## Error Handling

Error Condition | RPC Status Code | Error Message | Troubleshooting / Justification  
---|---|---|---  
**Not authorized to the resource** | `PERMISSION_DENIED (403)` | `"Permission denied for allowlisted domain resource."` | • Ensure the user has the appropriate scope granted.  
• Ensure the user has required permission.  
• Reach out to the contact email to ensure if the project/user has been allowlisted or not.  
**Customer ID not found for the user** | `NOT_FOUND (404)` | `"Customer ID not found for user."` | The logged in user is not linked to a valid domain.  
**An allowlist update is already in progress.** | `FAILED_PRECONDITION (400)` | `"An allowlist update is already in progress. Please wait for it to complete before making another request."` | Wait for any previous mutation (create or delete) operation to complete before initiating a new request.  
**Domain not found in the allowlist** | `NOT_FOUND (404)` | `"Allowlisted domain <domain> not found."` | The provided domain does not exist in the allowlist. It may happen if the domain was not added or already deleted from the allowlist. You can [check audit logs](https://docs.cloud.google.com/identity/docs/how-to/view-allowlisted-domains-audit-logs) to validate if the domain was added/deleted in the last 6 months.  
**Resource name is invalid** | `INVALID_ARGUMENT (400)` | `"Invalid resource name: <resourceName>."` | To resolve the Invalid resource name error, ensure the identifier provided in the DELETE request is correctly formatted and sourced:  
• **Validate resource name format** : The string used for the name parameter must precisely follow the format `allowlistedDomains/UNIQUE_IDENTIFIER`.  
• **Verify source of name** : The resource name is an Output only identifier and should be obtained from a previous successful call to the `allowlistedDomains.list` method for the same customer. Don't construct or guess the resource name.  
  
## Audit Logs

Deletions using the Allowlisted Domains API generate audit log events that can be reviewed by administrators. For more information, see [Viewing audit logs](https://docs.cloud.google.com/identity/docs/how-to/view-allowlisted-domains-audit-logs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
