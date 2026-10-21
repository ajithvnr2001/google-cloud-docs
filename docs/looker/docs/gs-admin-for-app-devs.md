---
url: https://docs.cloud.google.com/looker/docs/gs-admin-for-app-devs/
title: Getting started with embedding \u2014 administering users \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T21:14:30.883021+00:00
---

# Getting started with embedding — administering users  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/gs-admin-for-app-devs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Getting started with embedding — administering users Stay organized with collections  Save and categorize content based on your preferences. 

To create a signed embed URL, you are required to identify the models and permissions that are available to each embed user and, optionally, supply user attribute data for embed users. This document provides a quick overview of what these elements are in Looker.

## Models

[Models](https://docs.cloud.google.com/looker/docs/lookml-project-files#model_files) determine which data your embed users can access.

Each LookML model consists of a single database connection, and one or more Explores. Each Explore determines which database tables and fields are available to the model, how they are joined, and how they are presented to the user. It is common for multiple models to connect to a single database, which determines which data different sets of users can access. For example, users in the Sales department might need access to different data than users in the Purchasing department. In that case, you could provide two models, each one curated for a single use case.

In a signed embed URL, or when using the `create_sso_embed_url` API endpoint, you specify which models an embed user can access by listing them by name. For example:
    
    
    [
      "model_one",
      "model_two"
    ]
    

At least one model value is required in a signed embed URL.

## Permissions

Permissions determine what your embed users can do in Looker.

Every function in Looker requires permission to perform. For example, a user who does not have the `access_data` permission will not be able to view any data. A user who has the `access_data` permission, but not the `save_content` permission, will be able to view content but will not be able to make and save changes to content.

In a signed embed URL, or when using the `create_sso_embed_url` API endpoint, you specify which permissions an embed user has by listing them by name. For example:
    
    
    [
      "access_data",
      "see_looks"
    ]
    

At least one permission is required in a signed embed URL. You can view the list of permissions that are supported by signed embed on the [Signed embedding](https://docs.cloud.google.com/looker/docs/signed-embedding#permissions) documentation page.

## User attributes

[User attributes](https://docs.cloud.google.com/looker/docs/admin-panel-users-user-attributes) are a method to provide metadata about your embed users. They consist of name and value pairs.

Every user in Looker has several default user attributes, such as `first_name`, `last_name`, and `locale`. Looker admins can also create custom user attributes in various data types. For example, you may have an application where the data that's presented to the embed user varies based on the company they are associated with. In that case, you might create a custom `company` user attribute that accepts various values that grant or limit data access. You'd next assign the appropriate value to each embed user to limit data access at the user level.

In a signed embed URL, or when using the `create_sso_embed_url` API endpoint, you specify which user attributes are assigned to an embed user by listing each name and value pair. For example:
    
    
    {
      "vendor_id" : "17",
      "company" : "altostrat.com"
    }
    

User attributes are optional in a signed embed URL.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
