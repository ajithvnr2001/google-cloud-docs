---
url: https://docs.cloud.google.com/identity/docs/how-to/retrieve-list-posix-groups/
title: Retrieving and listing POSIX groups \u00a0|\u00a0 Cloud Identity \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:43:21.080482+00:00
---

# Retrieving and listing POSIX groups  |  Cloud Identity  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/identity/docs/how-to/retrieve-list-posix-groups/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Cloud Identity ](https://docs.cloud.google.com/identity/docs)
  * [ Guides ](https://docs.cloud.google.com/identity/docs/set-up-cloud-identity-admin)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Retrieving and listing POSIX groups

**Caution:** POSIX groups are [deprecated](https://docs.cloud.google.com/identity/docs/deprecations). As of September 26, 2024, you can no longer create new POSIX groups. For more information, see [POSIX groups deprecation](https://docs.cloud.google.com/identity/docs/deprecations/posix-groups).

This document explains how to retrieve and list POSIX groups.

**Preview**

This product is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

**Note:** You must use the beta version of the Cloud Identity Groups API to retrieve and list POSIX groups.

## Retrieving members of POSIX groups

You can retrieve group information using the Google group name, POSIX group name, POSIX group ID, or email.

### Retrieving a POSIX group by group name

The following sample shows how to retrieve a POSIX group using the group name:

###  REST 

To retrieve a POSIX group by name, call the [`groups.get()` method](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/groups/get) with the resource name of the group.
    
    
    GET "https://cloudidentity.googleapis.com/v1beta1/groups/GROUP_RESOURCE_NAME"
    

Replace the following:

  * `GROUP_RESOURCE_NAME`: the resource name of the Google group. To find a group's resource name, run the [`gcloud identity groups describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/identity/groups/describe)



###  Python 

The following example shows how to retrieve a POSIX group by name using the Python client library:
    
    
    def get_posix_group_by_name(name):
      service = build_service()
      response = service.groups().get(name=name).execute()
      return response
    

### Retrieving a POSIX group by POSIX group name

The following sample shows how to retrieve group information the POSIX group name:

###  REST 

To search for a POSIX group by POSIX group name, call the [`groups.search()` method](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/groups/search) with the following query string:
    
    
    query=parent=='customers/CUSTOMER_ID' && 'cloudidentity.googleapis.com/groups.posix' in labels && posix_groups.exists(pg, pg.name=='POSIX_NAME')
    

Replace `POSIX_NAME` with the name you want to assign to the POSIX group.

The following is a `GET` request using the query:
    
    
    GET "https://cloudidentity.googleapis.com/v1beta1/groups:search?query=parent=='customers/CUSTOMER_ID'%26%26'cloudidentity.googleapis.com/groups.posix'%20in%20labels%26%26posix_groups.exists(pg,pg.name=='POSIX_GROUP_NAME')&view=VIEW"
    

Replace the following:

  * `CUSTOMER_ID`: the customer ID for your organization. To find the customer ID run the [`gcloud organizations list` command](https://docs.cloud.google.com/sdk/gcloud/reference/organizations/list)
  * `POSIX_NAME`: the name you want to assign to the POSIX group
  * `VIEW`: either `FULL` or `BASIC`



###  Python 

The following example shows how to retrieve a POSIX group by POSIX group name using the Python client library:
    
    
    def get_posix_group_by_posix_name((service, customer_id, posix_group_name, page_size, view):
      # Set the label to search for a POSIX group
      searchQuery = ("&query=parent=='customers/{customer_id}' "
             "&& 'cloudidentity.googleapis.com/groups.posix' in labels "
             "&& posix_groups.exists(pg, pg.name=='{posix_group_name}')"
             "?pageSize={page_size}&view={view}".format(
                 customer_id=customer_id, posix_group_name=posix_group_name,
                 page_size=page_size, view=view))
      try:
        searchGroupsRequest = service.groups().search()
        searchGroupsRequest.uri += searchQuery
        response = searchGroupsRequest.execute()
        print response
      except Exception as e:
        print e
    

### Retrieving a POSIX group by POSIX group ID

The following sample shows how to retrieve group information using the group ID:

###  REST 

To search for a POSIX group by ID, call the [`groups.search()` method](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/groups/search) with the following query string:
    
    
    query=parent=='customers/CUSTOMER_ID' && 'cloudidentity.googleapis.com/groups.posix' in labels && posix_groups.exists(pg, pg.gid==GIDu)
    

Replace the following:

  * `CUSTOMER_ID`: the customer ID for your organization. To find the customer ID run the [`gcloud organizations list` command](https://docs.cloud.google.com/sdk/gcloud/reference/organizations/list)
  * `GROUP_ID`: the group ID (GID) you want to assign to the POSIX group



The following is a `GET` request using the query:
    
    
    GET "https://cloudidentity.googleapis.com/v1beta1/groups:search?query=parent=='customers/CUSTOMER_ID'%26%26'cloudidentity.googleapis.com/groups.posix'%20in%20labels%26%26posix_groups.exists(pg,pg.gid==GROUP_IDu)&view=VIEW"
    

Replace the following:

  * `CUSTOMER_ID`: the customer ID for your organization. To find the customer ID run the [`gcloud organizations list` command](https://docs.cloud.google.com/sdk/gcloud/reference/organizations/list)
  * `GROUP_ID`: the group ID (GID) you want to assign to the POSIX group
  * `VIEW`: either `FULL` or `BASIC`



###  Python 

The following example shows how to retrieve a POSIX group by group ID using the Python client library:
    
    
    def get_posix_group_by_gid(service, customer_id, posix_group_id, page_size, view):
      # Set the label to search for a POSIX group
      searchQuery = ("&query=parent=='customers/{customer_id}' "
             "&& 'cloudidentity.googleapis.com/groups.posix' in labels "
             "&& posix_groups.exists(pg, pg.gid=={posix_group_id}u)"
             "?pageSize={page_size}&view={view}".format(
                 customer_id=customer_id, posix_group_id=posix_group_id,
                 page_size=page_size, view=view))
      try:
        searchGroupsRequest = service.groups().search()
        searchGroupsRequest.uri += searchQuery
        response = searchGroupsRequest.execute()
        print response
      except Exception as e:
        print e
    

### Retrieving a POSIX group by email

The following sample shows how to retrieve group information using the group email:

###  gcloud 

Use the [`gcloud beta identity groups describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/beta/identity/groups/describe) to list all POSIX groups in an organization:
    
    
    gcloud beta identity groups describe EMAIL_ADDRESS
    

Replace `EMAIL_ADDRESS` with the email address of the group being searched.

###  REST 

To retrieve a POSIX group by email do the following:

  1. Call the [`groups.lookup()` method](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/groups/lookup) with the group email address:
         
         GET "https://cloudidentity.googleapis.com/v1beta1/groups:lookup?groupKey.id=EMAIL_ADDRESS"
         

Note the resource name of the group returned.

  2. Call the [`groups.get()` method](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/groups/get) with the resource name of the group:
         
         GET "https://cloudidentity.googleapis.com/v1beta1/groups/GROUP_RESOURCE_NAME"
         




###  Python 

The following example shows how to retrieve a POSIX group by email using the Python client library:
    
    
    def get_posix_group_by_email(email):
      service = build_service()
    
      # First we use the email to get the groups name calling lookup()
      lookup_group_name_request = service.groups().lookup()
      param = "&groupKey.id=" + email
      lookup_group_name_request.uri += param
      lookup_group_name_response = lookup_group_name_request.execute()
      name = lookup_group_name_response.get("name")
    
      # Then we can call get() by passing in the group's name
      response = service.groups().get(name=name).execute()
      return response
    

## Listing POSIX groups

The following examples show how to list all POSIX groups in your organization:

###  gcloud 

Use the [`gcloud identity groups search` command](https://docs.cloud.google.com/sdk/gcloud/reference/identity/groups/search) to list all POSIX groups in an organization:
    
    
    gcloud identity groups search \
        --labels=cloudidentity.googleapis.com/groups.posix \
        --organization=ORGANIZATION
    

Replace `ORGANIZATION` with the organization ID for the group being searched.

###  REST 

To search for all POSIX groups, call the [`groups.search()` method](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/groups/search) with the following query string:
    
    
    query=parent=='customers/CUSTOMER_ID' && 'cloudidentity.googleapis.com/groups.posix' in labels
    

Replace `CUSTOMER_ID` with the customer ID for your organization. To find the customer ID run the [`gcloud organizations list` command](https://docs.cloud.google.com/sdk/gcloud/reference/organizations/list).

The following is a `GET` request using the query:
    
    
    GET "https://cloudidentity.googleapis.com/v1beta1/groups:search?query=parent=='customers/CUSTOMER_ID'%26%26'cloudidentity.googleapis.com/groups.posix'%20in%20labels&view=VIEW"
    

Replace the following:

  * `CUSTOMER_ID`: the customer ID for your organization. To find the customer ID run the [`gcloud organizations list` command](https://docs.cloud.google.com/sdk/gcloud/reference/organizations/list)
  * `GROUP_ID`: the group ID (GID) you want to assign to the POSIX group
  * `VIEW`: either `FULL` or `BASIC`



###  Python 

The following example shows a helper function to search for POSIX groups using the Python client library:
    
    
    def search_posix_groups(service, customer_id, page_size, view):
      # Set the label to search for all POSIX groups
      searchQuery = ("&query=parent=='customers/{customer_id}' "
             "&& 'cloudidentity.googleapis.com/groups.posix' in labels "
             "?pageSize={page_size}&view={view}".format(
                 customer_id=customer_id, page_size=page_size, view=view))
      try:
        searchGroupsRequest = service.groups().search()
        searchGroupsRequest.uri += searchQuery
        response = searchGroupsRequest.execute()
        print response
      except Exception as e:
        print e
    
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
