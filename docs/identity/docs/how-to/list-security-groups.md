---
url: https://docs.cloud.google.com/identity/docs/how-to/list-security-groups/
title: Searching for security groups \u00a0|\u00a0 Cloud Identity \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:10:32.152914+00:00
---

# Searching for security groups  |  Cloud Identity  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/identity/docs/how-to/list-security-groups/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Cloud Identity ](https://docs.cloud.google.com/identity/docs)
  * [ Guides ](https://docs.cloud.google.com/identity/docs/set-up-cloud-identity-admin)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Searching for security groups

This page explains how to find all of your security groups with the Cloud Identity Groups API.

**Note:** When a method requires the `customer_id`, you must prepend a "C" to the ID that you can view in the Google Admin console (for example, 'C046psxkn').

###  REST 

To search for all security groups, call [`groups.search()`](https://docs.cloud.google.com/identity/docs/reference/rest/v1/groups/search) with a query string of `labels:cloudidentity.googleapis.com/groups.security`.

###  Python 

The following example shows a helper function to search for security groups using the Python client library:
    
    
    def search_security_groups(service, identity_source_id, pageSize, view):
      # Set the label to search for all Google groups
      searchQuery = "&query=parent=='customers/{customer_id}'&&labels:cloudidentity.googleapis.com/groups.security" \
        + "&pageSize=" + pageSize + "&view=" + view
      try:
        searchGroupsRequest = service.groups().search()
        searchGroupsRequest.uri += searchQuery
        response = searchGroupsRequest.execute()
        print(response)
      except Exception as e:
        print(e)
    
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
