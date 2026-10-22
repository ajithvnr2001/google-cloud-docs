---
url: https://docs.cloud.google.com/database-migration/docs/mysql/use-the-database-migration-service-api/
title: Use the Database Migration Service API \u00a0|\u00a0 Database Migration Service for MySQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:43:34.044029+00:00
---

# Use the Database Migration Service API  |  Database Migration Service for MySQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-migration/docs/mysql/use-the-database-migration-service-api/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ MySQL ](https://docs.cloud.google.com/database-migration/docs/mysql)
  * [ API and references ](https://docs.cloud.google.com/database-migration/docs/mysql/use-the-database-migration-service-api)



Send feedback 

#  Use the Database Migration Service API Stay organized with collections  Save and categorize content based on your preferences. 

Database Migration Service provides a REST API for administering your connection profiles and migration jobs programmatically. The REST API is defined by resources associated with creating and managing connection profiles and migration jobs. For details about all resources and their methods, see the [ Database Migration Service API Reference](https://docs.cloud.google.com/database-migration/docs/reference/rest).

When you send requests directly to the Database Migration Service REST API, you must create the correct form of the request, authorize the request as an authenticated user, and process any responses returned. Many of the tasks in this documentation provide API examples using [ curl](http://curl.haxx.se).

For more examples of using the APIs, see the page for the request in the [ Database Migration Service API Reference](https://docs.cloud.google.com/database-migration/docs/reference/rest). Each page has examples calling the API in several programming languages, as well as a request-specific Explorer to help you see what goes into a well-formed request and what to expect in the response.

You're also using the Database Migration Service API, indirectly, when you use any of the following ways of administering instances:

  * [ Google Cloud CLI](https://docs.cloud.google.com/sdk): A command-line interface (CLI) that you can use to work with your instances.

  * [ Google Cloud console](https://console.cloud.google.com/): A graphical web interface.




The advantage of using these methods, especially the Google Cloud console, is that they can greatly simplify administering your connection profiles and migration jobs (depending on your use case). If you're just starting out with Database Migration Service, then we recommend that you start with one of these tools first before working with the REST API directly.

## Enable the API

To use the Database Migration Service API, you need to enable it:

### Console

  1. [ Enable the Database Migration Service API](https://console.cloud.google.com//apis/library/datamigration.googleapis.com). 
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



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
