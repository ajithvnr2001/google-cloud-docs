---
url: https://docs.cloud.google.com/database-migration/docs/postgres/use-the-database-migration-service-api/
title: Use the Database Migration Service API \u00a0|\u00a0 Database Migration Service for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T11:59:49.528105+00:00
---

# Use the Database Migration Service API  |  Database Migration Service for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-migration/docs/postgres/use-the-database-migration-service-api/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ PostgreSQL ](https://docs.cloud.google.com/database-migration/docs/postgres)
  * [ API and references ](https://docs.cloud.google.com/database-migration/docs/postgres/use-the-database-migration-service-api)



Send feedback 

#  Use the Database Migration Service API Stay organized with collections  Save and categorize content based on your preferences. 

Database Migration Service provides a REST API for administering your connection profiles and migration jobs programmatically. The REST API is defined by resources associated with creating and managing connection profiles and migration jobs. For details about all resources and their methods, see the [ Database Migration Service API Reference](https://docs.cloud.google.com/database-migration/docs/reference/rest).

When you send requests directly to the Database Migration Service REST API, you must create the correct form of the request, authorize the request as an authenticated user, and process any responses returned. Many of the tasks in this documentation provide API examples using [cURL](http://curl.haxx.se).

For more examples of using the APIs, see the page for the request in the [Database Migration Service API Reference](https://docs.cloud.google.com/database-migration/docs/reference/rest). Each page has examples calling the API in several programming languages, as well as a request-specific Explorer to help you see what goes into a well-formed request and what to expect in the response.

You're also using the Database Migration Service API, indirectly, when you use any of the following ways of administering instances:

  * [Google Cloud CLI](https://docs.cloud.google.com/sdk): A command-line interface (CLI) that you can use to work with your instances.

  * [the Google Cloud console](https://console.cloud.google.com/): A graphical web interface.




The advantage of using these methods, especially the Google Cloud console, is that they can greatly simplify administering your connection profiles and migration jobs (depending on your use case). If you're just starting out with Database Migration Service, then we recommend that you start with one of these tools first before working with the REST API directly.

## Enable the API

To use the Database Migration Service API, you need to enable it:

### Console

  1. [Enable the Database Migration Service API](https://console.cloud.google.com/apis/library/datamigration.googleapis.com). 
  2. Select your project.
  3. Select **Continue**.



### gcloud

  1. Enter the following to display the project IDs for your Google Cloud projects: 
         
         gcloud projects list

  2. Set your default project: 
         
         gcloud config set project YOUR_PROJECT_ID

  3. Enable the Database Migration Service API: 
         
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




### Example: Create a PostgreSQL source connection profile

To create a connection profile for a PostgreSQL source database, create a file named `request.json` with the following content:
    
    
    {
      "displayName": "PostgreSQL source connection profile",
      "postgresql": {
        "host": "198.51.100.1",
        "port": 5432,
        "username": "migration_admin",
        "password": "MIGRATION_PASSWORD",
        "ssl": {
          "type": "SERVER_ONLY",
          "caCertificate": "-----BEGIN CERTIFICATE-----\n...\n-----END CERTIFICATE-----"
        }
      }
    }

Then, send the following cURL request at the command line:
    
    
    curl --header "Authorization: Bearer ${ACCESS_TOKEN}" \
         --header 'Content-Type: application/json' \
         --data @./request.json \
         -X POST \
         "https://datamigration.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/connectionProfiles?connectionProfileId=SOURCE_PROFILE_ID"

### Example: Create a PostgreSQL continuous migration job

To create a continuous migration job for PostgreSQL, create a file named `migration_job.json` with the following content:
    
    
    {
      "displayName": "PostgreSQL continuous migration job",
      "type": "CONTINUOUS",
      "source": "projects/PROJECT_ID/locations/REGION/connectionProfiles/SOURCE_PROFILE_ID",
      "destination": "projects/PROJECT_ID/locations/REGION/connectionProfiles/DESTINATION_PROFILE_ID"
    }

Then, send the following cURL request at the command line:
    
    
    curl --header "Authorization: Bearer ${ACCESS_TOKEN}" \
         --header 'Content-Type: application/json' \
         --data @./migration_job.json \
         -X POST \
         "https://datamigration.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/migrationJobs?migrationJobId=MIGRATION_JOB_ID"

## Work with long-running API calls

Some API calls, such as object creation, can take some time to complete. Because the API is asynchronous, the call returns immediately, even if the operation is still in progress. If a subsequent API call uses the newly created object, then you must wait for the first operation to complete before proceeding.

You can use the Database Migration Service API to [manage operations](https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/operations). This includes:

  * [Showing details about an operation](https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/operations/describe)
  * [Listing operations for a region](https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/operations/list)
  * [Deleting an operation](https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/operations/delete)



## Database Migration Service and Google APIs Discovery Service

[Google APIs Discovery Service](https://developers.google.com/discovery) is a service that you can use to discover Google APIs. For example, when you use the [Google APIs Explorer](https://developers.google.com/apis-explorer/) tool, you're using the Discovery Service.

In the Discovery Service, Database Migration Service is represented as "datamigration" (for example: `https://datamigration.googleapis.com/$discovery/rest?version=v1`).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-19 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-19 UTC."],[],[]] 
