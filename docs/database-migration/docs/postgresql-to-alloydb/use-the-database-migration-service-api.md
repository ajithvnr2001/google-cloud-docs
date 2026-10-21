---
url: https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/use-the-database-migration-service-api/
title: Use the Database Migration Service API \u00a0|\u00a0 Database Migration Service for PostgreSQL to AlloyDB \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T11:59:50.167169+00:00
---

# Use the Database Migration Service API  |  Database Migration Service for PostgreSQL to AlloyDB  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/use-the-database-migration-service-api/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ PostgreSQL to AlloyDB ](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb)
  * [ Reference ](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/apis)



Send feedback 

#  Use the Database Migration Service API Stay organized with collections  Save and categorize content based on your preferences. 

  


[MySQL](https://docs.cloud.google.com/database-migration/docs/mysql/use-the-database-migration-service-api "View this page for the MySQL version of Database Migration Service.") | [PostgreSQL](https://docs.cloud.google.com/database-migration/docs/postgres/use-the-database-migration-service-api "View this page for the PostgreSQL version of Database Migration Service.") | PostgreSQL to AlloyDB

  


## Overview

Database Migration Service provides a REST API for administering your connection profiles and migration jobs programmatically. The REST API is defined by resources associated with creating and managing connection profiles and migration jobs. For details about all resources and their methods, see the [Database Migration Service API Reference](https://docs.cloud.google.com/database-migration/docs/reference/rest).

When you send requests directly to the Database Migration Service REST API, you must create the correct form of the request, authorize the request as an authenticated user, and process any responses returned. Many of the tasks in this documentation provide API examples using [cURL](http://curl.haxx.se).

For more examples of using the APIs, see the page for the request in the [Database Migration Service API Reference](https://docs.cloud.google.com/database-migration/docs/reference/rest). Each page has examples calling the API in several programming languages, as well as a request-specific Explorer to help you see what goes into a well-formed request and what to expect in the response.

You're also using the Database Migration Service API, indirectly, when you use any of the following ways of administering instances:

  * [Google Cloud CLI](https://docs.cloud.google.com/sdk): A command-line interface (CLI) that you can use to work with your instances.

  * [Google Cloud console](https://console.cloud.google.com/): A graphical web interface.




The advantage of using these methods, especially the Google Cloud console, is that they can greatly simplify administering your connection profiles and migration jobs (depending on your use case). If you're just starting out with Database Migration Service, then we recommend that you start with one of these tools first before working with the REST API directly.

## Enable the API

To use the Database Migration Service API, you need to enable it:

### Console

  1. [ Enable the Database Migration Service API](https://console.cloud.google.com/apis/library/datamigration.googleapis.com). 
  2. Select your project.
  3. Select **Continue**.



### gcloud

  1. Enter the following to display the project IDs for your Google Cloud projects: 
         
         gcloud projects list

  2. Set your default project: 
         
         gcloud config set project YOUR_PROJECT_ID

  3. Enable the Cloud SQL Admin API: 
         
         gcloud services enable datamigration.googleapis.com




## Permissions

You must have the required permissions to use the Database Migration Service API. These permissions include:

  * Database Migration Admin: With this permission, a user gains access to all resources of Database Migration Service used to manage connection profiles and migration jobs.
  * Database Migration Viewer: With this permission, a user has read-only access to connection profiles and migration jobs in Database Migration Service.
  * Cloud SQL Admin: With this permission, a user can create and manage connection profiles and migration jobs for Cloud SQL in Database Migration Service.



Google Cloud offers Identity and Access Management (IAM), which lets you give more granular access to specific Google Cloud resources and prevents unwanted access to other resources. You can get and set permissions for Database Migration Service using the Google Cloud console, the IAM methods of the API, or the Google Cloud CLI. For more information, see [Granting, changing, and revoking access to resources](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

## Provide JSON data from a file

When you use the API with cURL, you provide property values using the command line. If you're working with sensitive values such as passwords or security keys, providing them on the command line poses a security risk. For increased security, you can create a file containing the JSON data for the API call, and provide the path to the file on the command line.

To provide JSON data to your cURL API call from a file:

  1. Create a file containing everything enclosed in single quotes for the `--data` field.

Include the curly brackets, but don't include the single quotes.

  2. At the command line, provide the path to the file, preceded by the `@` character, as the `--data` parameter:
         
         --data @<path-to-file>/<filename>




## Work with long-running API calls

Some API calls, such as object creation, can take some time to complete. Because the API is asynchronous, the call returns immediately, even if the operation is still in progress. If a subsequent API call uses the newly created object, then you must wait for the first operation to complete before proceeding.

You can use the Database Migration Service API to [manage operations](https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/operations). This includes:

  * [Showing details about an operation](https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/operations/describe)
  * [Listing operations for a region](https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/operations/list)
  * [Deleting an operation](https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/operations/delete)



## Database Migration Service and Google APIs Discovery Service

[Google APIs Discovery Service](https://developers.google.com/discovery) is a service that you can use to discover Google APIs. For example, when you use the [Google APIs Explorer ](https://developers.google.com/apis-explorer/) tool, you're using the Discovery Service. 

In the Discovery Service, Database Migration Service is represented as "datamigration" (for example: https://**datamigration**.googleapis.com/$discovery/rest?version=v1).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-19 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-19 UTC."],[],[]] 

  * ### Products and pricing

    * [ See all products ](https://cloud.google.com/products/)
    * [ Google Cloud pricing ](https://cloud.google.com/pricing/)
    * [ Google Cloud Marketplace ](https://cloud.google.com/marketplace/)
    * [ Contact sales ](https://cloud.google.com/contact/)
  * ### Support

    * [ Community forums ](https://discuss.google.dev/c/google-cloud/14/)
    * [ Support ](https://cloud.google.com/support-hub/)
    * [ Release Notes ](https://docs.cloud.google.com/release-notes)
    * [ System status ](https://status.cloud.google.com)
  * ### Resources

    * [ GitHub ](https://github.com/googlecloudPlatform/)
    * [ Getting Started with Google Cloud ](https://docs.cloud.google.com/docs/get-started/)
    * [ Code samples ](https://docs.cloud.google.com/docs/samples)
    * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture/)
    * [ Training and Certification ](https://cloud.google.com/learn/training/)
    * [ Builders Hub ](https://me.developers.google.com/)
  * ### Engage

    * [ Blog ](https://cloud.google.com/blog/)
    * [ Events ](https://cloud.google.com/events/)
    * [ X (Twitter) ](https://x.com/googlecloud)
    * [ Google Cloud on YouTube ](https://www.youtube.com/googlecloud)
    * [ Google Cloud Tech on YouTube ](https://www.youtube.com/googlecloudplatform)



[ ![Google Developers](https://www.gstatic.com/devrel-devsite/prod/v9ce9cb5b22b62a465ff52c45061a0a6a2d86a80b685e9aa8a182b203fdfbf420/clouddocs/images/lockup-google-for-developers.svg)](https://developers.google.com/)

  * [ Android ](https://developer.android.com/)
  * [ Chrome ](https://developer.chrome.com/)
  * [ Firebase ](https://firebase.google.com/)
  * [ Google AI ](https://ai.google.com/)



  * [ About Google ](https://about.google/)
  * [ Privacy ](https://policies.google.com/privacy)
  * [ Site terms ](https://policies.google.com/terms?hl=en)
  * [ Google Cloud terms ](https://cloud.google.com/product-terms)
  * Manage cookies 
  * [ Our third decade of climate action: join us ](https://cloud.google.com/sustainability)
  * Sign up for the Google Cloud newsletter [ Subscribe ](https://cloud.google.com/newsletter/)



  * English
  * Deutsch
  * Español
  * Español – América Latina
  * Français
  * Indonesia
  * Italiano
  * Português
  * Português – Brasil
  * עברית
  * 中文 – 简体
  * 中文 – 繁體
  * 日本語
  * 한국어


