---
url: https://docs.cloud.google.com/identity/docs/how-to/list-get-allowlisted-domains/
title: Listing and getting allowlisted domains \u00a0|\u00a0 Cloud Identity \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:10:26.983348+00:00
---

# Listing and getting allowlisted domains  |  Cloud Identity  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/identity/docs/how-to/list-get-allowlisted-domains/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Cloud Identity ](https://docs.cloud.google.com/identity/docs)
  * [ Guides ](https://docs.cloud.google.com/identity/docs/set-up-cloud-identity-admin)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Listing and getting allowlisted domains

This page provides code examples and operational details that demonstrate how to list and retrieve specific domains in the allowlist using the Allowlisted Domains API.

## Before you begin

Perform the following tasks before proceeding with the information on this page:

  * Read the [Allowlisted Domains API overview](https://docs.cloud.google.com/identity/docs/concepts/overview-allowlisted-domains).
  * [Set up the Allowlisted Domains API](https://docs.cloud.google.com/identity/docs/how-to/setup-allowlisted-domains).



## Listing domains in the allowlist

Use the `list` method to fetch all entries. You may optionally provide `pageSize`, `pageToken`, or a `filter` string to narrow results.

###  Python 
    
    
    def list_allowlisted_domains(
        service, page_size=None, page_token=None, domain_filter=None
    ):
      """Lists allowlisted domains."""
      try:
        filter_string = None
        if domain_filter:
          filter_string = f"domain = '{domain_filter}'"
    
        response = (
            service.allowlistedDomains()
            .list(
                pageSize=page_size, pageToken=page_token, filter=filter_string
            )
            .execute()
        )
        return response
      except Exception as e:
        print(f'An error occurred during list: {e}')
        return None
    

**Note:** Filtering only supports exact matches on the domain string (e.g., `filter="domain = 'google.com'"`). No composite conditions are supported.

## Getting a specific domain

Retrieve a specific domain synchronously using its resource name obtained from a previous list operation.

###  Python 
    
    
    def get_allowlisted_domain(service, resource_name):
      """Gets an allowlisted domain."""
      if not resource_name:
        print('Resource name is missing.')
        return None
    
      try:
        response = service.allowlistedDomains().get(name=resource_name).execute()
        return response
      except Exception as e:
        print(f'An error occurred during get: {e}')
        return None
    

## Error Handling

This section describes common error conditions and troubleshooting steps when listing or getting allowlisted domains.

### List Error Handling

Error Condition | RPC Status Code | Error Message | Troubleshooting / Justification  
---|---|---|---  
**Not authorized to the resource** | `PERMISSION_DENIED (403)` | `"Permission denied for allowlisted domain resource."` | • Ensure the user has the appropriate scope granted.  
• Ensure the user has required permission.  
• Reach out to the contact email to ensure if the project/user has been allowlisted or not.  
**Customer ID not found for the user** | `NOT_FOUND (404)` | `"Customer ID not found for user."` | The logged in user is not linked to a valid domain.  
**List has been mutated during pagination** | `ABORTED` | `"List has been mutated. Please restart pagination."` | The underlying list of domains was modified (mutated) while you were paginating; you must restart the `allowlistedDomains.list` operation from the first page. Consider fetching the complete list at once if there are ongoing mutations in parallel.  
**Invalid domain filter value provided** | `INVALID_ARGUMENT (400)` | `"Invalid domain filter value provided. Error: <Error message>."` | Double check the domain provided in the filter parameter of the list request to ensure it is not empty or syntactically invalid.  
Invalid filter parameters provided cases:  
The `allowlistedDomains.list` operation failed due to an invalid syntax or unsupported operation passed in the filter. The error message will explain the exact use case. Please ensure following format is used to call the API:  
`GET https://cloudidentity.googleapis.com/v1/allowlistedDomains?filter="domain = 'google.com'"`  
**Invalid filter expression** | `INVALID_ARGUMENT (400)` | `"Invalid filter expression: %s."` | Incorrect filter expression passed in the request.  
**Composite conditions not supported** | `INVALID_ARGUMENT (400)` | `"Composite conditions (AND, OR, NOT) are not supported in the filter."` | The filter does not support composite conditions; only single-condition filtering is allowed.  
**Only '=' operator is supported** | `INVALID_ARGUMENT (400)` | `"Only '=' operator is supported in the filter."` | Use the equality operator (`=`) for all filter expressions. Any other operations are not supported.  
**Only 'domain' field is supported** | `INVALID_ARGUMENT (400)` | `"Only 'domain' field is supported in the filter."` | The filter must target the domain field (e.g., `domain = 'example.com'`). Any other fields are not supported.  
**RHS has invalid member value / should be string** | `INVALID_ARGUMENT (400)` | `"RHS of filter expression has invalid member value."`  
`"RHS of filter expression should be a string."` | The right-hand side (RHS) value of the filter expression must be a string (the domain name).  
**Page size is negative** | `INVALID_ARGUMENT (400)` | `"Page size cannot be negative."` | Ensure the `pageSize` parameter is a non-negative integer.  
**Invalid page token** | `INVALID_ARGUMENT (400)` | `"Invalid page token."` | The error indicates the token is malformed or expired. Ensure you are using the exact, unmodified token provided by the `nextPageToken` field from the immediate previous list response. If validation fails, omit the `pageToken` parameter to restart pagination from the first page.  
  
### Get Error Handling

Error Condition | RPC Status Code | Error Message | Troubleshooting / Justification  
---|---|---|---  
**Not authorized to the resource** | `PERMISSION_DENIED (403)` | `"Permission denied for allowlisted domain resource."` | • Ensure the user has the appropriate scope granted.  
• Ensure the user has required permission.  
• Reach out to the contact email to ensure if the project/user has been allowlisted or not.  
**Customer ID not found for the user** | `NOT_FOUND (404)` | `"Customer ID not found for user."` | The logged in user is not linked to a valid domain.  
**Domain not found in the allowlist** | `NOT_FOUND (404)` | `"Allowlisted domain <domain> not found"` | The provided domain does not exist in the allowlist.  
**Resource name is invalid** | `INVALID_ARGUMENT (400)` | `"Invalid resource name: <resourceName>."` | **Validate resource ame Format** : The string used for the name parameter must precisely follow the format `allowlistedDomains/UNIQUE_IDENTIFIER`.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
