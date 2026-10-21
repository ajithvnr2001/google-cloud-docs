---
url: https://docs.cloud.google.com/run/docs/tutorials/function-sends-query-to-spanner-database/
title: Create a Cloud Run function that returns Spanner results \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T00:15:22.630038+00:00
---

# Create a Cloud Run function that returns Spanner results  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/run/docs/tutorials/function-sends-query-to-spanner-database/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run)



Send feedback 

#  Create a Cloud Run function that returns Spanner results Stay organized with collections  Save and categorize content based on your preferences. 

Cloud Run functions let you build serverless services that query and serve Spanner data over HTTP. In this tutorial, you write and deploy an HTTP-triggered function that retrieves records from a Spanner database.

## Objectives

Write, deploy, and trigger an [HTTP function](https://docs.cloud.google.com/run/docs/write-functions#write-http-functions) that accesses Spanner.

## Costs

This document uses Spanner and Cloud Run, which are billable components of Google Cloud.

  * For information on the cost of using Spanner, see [Spanner pricing](https://cloud.google.com/spanner/pricing).

  * For information on the cost of using Cloud Run, including free invocations, see [Cloud Run pricing](https://cloud.google.com/run/pricing).




## Before you begin

  1. This document assumes you have a Spanner instance named `test-instance` and a database named `example-db` that uses the music application [schema](https://docs.cloud.google.com/spanner/docs/schema-and-data-model#creating-interleaved-tables). For instructions on creating an instance and database with the music application schema, see [Quickstart using the console](https://docs.cloud.google.com/spanner/docs/create-query-database-console) or the tutorials for Getting Started in [Node.js](https://docs.cloud.google.com/spanner/docs/getting-started/nodejs), or [Python](https://docs.cloud.google.com/spanner/docs/getting-started/python).

**Note:** After this step, you should have two tables, [`Singers`](https://docs.cloud.google.com/spanner/docs/schema-and-data-model#creating_a_table) and [`Albums`](https://docs.cloud.google.com/spanner/docs/schema-and-data-model#creating_multiple_tables), in your database with the sample data specified in the music application schema.
  2. Enable the Cloud Run and Cloud Build APIs.

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=cloudrun.googleapis.com,cloudbuild.googleapis.com)

  3. [Install and initialize the gcloud CLI](https://docs.cloud.google.com/sdk/docs).

If you already have the gcloud CLI installed, update it by running the following command:
         
         gcloud components update
         

  4. Prepare your development environment:

###  Node.js 

See the [Node.js setup guide](https://docs.cloud.google.com/nodejs/docs/setup).

###  Python 

See the [Python setup guide](https://docs.cloud.google.com/python/docs/setup).




### Required roles

To get the permissions that you need to deploy Cloud Run services from source, ask your administrator to grant you the following IAM roles: 

  * [Cloud Run Source Developer ](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.sourceDeveloper) (`roles/run.sourceDeveloper`) on your project
  * [Service Usage Consumer ](https://docs.cloud.google.com/iam/docs/roles-permissions/serviceusage#serviceusage.serviceUsageConsumer) (`roles/serviceusage.serviceUsageConsumer`) on the Cloud Run service
  * [Service Account User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`) on the service identity
  * [Spanner Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/spanner#spanner.admin) (`roles/spanner.admin`) on the Spanner instance



For a list of IAM roles and permissions that are associated with Cloud Run, see [Cloud Run IAM roles](https://docs.cloud.google.com/run/docs/reference/iam/roles) and [Cloud Run IAM permissions](https://docs.cloud.google.com/run/docs/reference/iam/permissions). If your Cloud Run service interfaces with Google Cloud APIs, such as Cloud Client Libraries, see the [service identity configuration guide](https://docs.cloud.google.com/run/docs/configuring/services/service-identity). For more information about granting roles, see [deployment permissions](https://docs.cloud.google.com/run/docs/reference/iam/roles#additional-configuration) and [manage access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

#### Roles for the Cloud Build service account

You or your administrator must grant the Cloud Build service account the following IAM role.

#### Click to view required roles for the Cloud Build service account

Cloud Build automatically uses the [Compute Engine default service account](https://docs.cloud.google.com/build/docs/cloud-build-service-account) as the default Cloud Build service account to build your source code and Cloud Run resource, unless you override this behavior. For Cloud Build to build your sources, ask your administrator to grant [Cloud Run Builder](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.builder) (`roles/run.builder`) to the Compute Engine default service account on your project:
    
    
      gcloud projects add-iam-policy-binding PROJECT_ID \
          --member=serviceAccount:PROJECT_NUMBER-compute@developer.gserviceaccount.com \
          --role=roles/run.builder
      

Replace `PROJECT_NUMBER` with your Google Cloud project number, and `PROJECT_ID` with your Google Cloud project ID. For detailed instructions on how to find your project ID, and project number, see [Creating and managing projects](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).

Granting the Cloud Run builder role to the Compute Engine default service account takes a couple of minutes to [propagate](https://docs.cloud.google.com/iam/docs/access-change-propagation).

**Note:**

The [ `iam.automaticIamGrantsForDefaultServiceAccounts` organization policy constraint](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-service-accounts#disable_service_account_default_grants) prevents the Editor role from being automatically granted to default service accounts. If you created your organization after May 3, 2024, this constraint is enforced by default. 

We strongly recommend that you enforce this constraint to disable the automatic role grant. If you disable the automatic role grant, you must decide which roles to grant to the default service accounts, and then [grant these roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access) yourself. 

If the default service account already has the Editor role, we recommend that you replace the Editor role with less permissive roles.To safely modify the service account's roles, use [Policy Simulator](https://docs.cloud.google.com/policy-intelligence/docs/simulate-iam-policies) to see the impact of the change, and then [grant and revoke the appropriate roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

#### Roles for the service identity

You must grant the service identity that you use for the Cloud Run service the following IAM role.

  * Spanner Database Reader (`roles/spanner.databaseReader`)



For more information on granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

## Prepare the application

  1. Clone the sample app repository to your local machine:

###  Node.js 
         
         git clone https://github.com/GoogleCloudPlatform/nodejs-docs-samples.git

Alternatively, you can [download the sample](https://github.com/GoogleCloudPlatform/nodejs-docs-samples/archive/main.zip) as a zip file and extract it.

###  Python 
         
         git clone https://github.com/GoogleCloudPlatform/python-docs-samples.git

Alternatively, you can [download the sample](https://github.com/GoogleCloudPlatform/python-docs-samples/archive/main.zip) as a zip file and extract it.

  2. Change to the directory that contains the Cloud Run functions sample code for accessing Spanner:

###  Node.js 
         
         cd nodejs-docs-samples/functions/spanner

###  Python 
         
         cd python-docs-samples/functions/spanner

  3. Take a look at the sample code:

###  Node.js 
         
         // Imports the Google Cloud client library
         const {Spanner} = require('[@google-cloud/spanner](https://docs.cloud.google.com/nodejs/docs/reference/spanner/latest/overview.html)');
         
         // Imports the functions framework to register your HTTP function
         const functions = require('@google-cloud/functions-framework');
         
         // Instantiates a client
         const spanner = new [Spanner](https://docs.cloud.google.com/nodejs/docs/reference/spanner/latest/spanner/spanner.html)();
         
         // Your Cloud Spanner instance ID
         const instanceId = 'test-instance';
         
         // Your Cloud Spanner database ID
         const databaseId = 'example-db';
         
         /**
          * HTTP Cloud Function.
          *
          * @param {Object} req Cloud Function request context.
          * @param {Object} res Cloud Function response context.
          */
         functions.http('spannerQuickstart', async (req, res) => {
           // Gets a reference to a Cloud Spanner instance and database
           const instance = spanner.instance(instanceId);
           const database = instance.database(databaseId);
         
           // The query to execute
           const query = {
             sql: 'SELECT * FROM Albums',
           };
         
           // Execute the query
           try {
             const results = await database.run(query);
             const rows = results[0].map(row => row.toJSON());
             rows.forEach(row => {
               res.write(
                 `SingerId: ${row.SingerId}, ` +
                   `AlbumId: ${row.AlbumId}, ` +
                   `AlbumTitle: ${row.AlbumTitle}\n`
               );
             });
             res.status(200).end();
           } catch (err) {
             res.status(500).send(`Error querying Spanner: ${err}`);
           }
         });

###  Python 
         
         import functions_framework
         from google.cloud import [spanner](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.services.spanner.html)
         
         instance_id = "test-instance"
         database_id = "example-db"
         
         client = [spanner](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.services.spanner.html).[Client](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.client.Client.html)()
         instance = [client](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.client.html).[instance](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.client.Client.html#google_cloud_spanner_v1_client_Client_instance)(instance_id)
         database = instance.database(database_id)
         
         
         @functions_framework.http
         def spanner_read_data(request):
             query = "SELECT * FROM Albums"
         
             outputs = []
             with database.snapshot() as snapshot:
                 results = snapshot.execute_sql(query)
         
                 for row in results:
                     output = "SingerId: {}, AlbumId: {}, AlbumTitle: {}".format(*row)
                     outputs.append(output)
         
             return "\n".join(outputs)
         
         

The function sends a SQL query to fetch all `Albums` data from your database. The function is executed when you make an HTTP request to the function's endpoint.




## Deploy the function

To deploy the function with an HTTP trigger, run the following command in the `spanner` directory:

###  Node.js 
    
    
    gcloud run deploy nodejs-spanner-function \
        --source . \
        --region REGION \
        --function spannerQuickstart \
        --base-image RUNTIME_ID \
        --log-http

###  Python 
    
    
    gcloud run deploy python-spanner-function \
        --source . \
        --region REGION \
        --function spanner_read_data \
        --base-image RUNTIME_ID \
        --log-http

Replace:

  * REGION with the name of the [Google Cloud region](https://docs.cloud.google.com/run/docs/locations) where you want to deploy your function (for example, `us-west1`).

  * RUNTIME_ID with the appropriate runtime ID (for example, `nodejs22`). See [Supported language runtimes and base images](https://docs.cloud.google.com/run/docs/configuring/services/runtime-base-images).




Function deployment might take up to two minutes.

Note the `url` value returned when your function finishes deploying. You will use it when you trigger the function.

You can view your deployed functions on the [Cloud Run](https://console.cloud.google.com/project/_/run) page in the Google Cloud console. You can also create and edit functions on that page, and get details and diagnostics for your functions.

## Trigger the function

Make an HTTP request to your function:
    
    
    curl URL
    

Replace URL with the URL value returned when your function finishes deploying.

You should see output that shows the results of the SQL query, assuming you worked through a [Getting Started tutorial](https://docs.cloud.google.com/spanner/docs/create-query-database-console) and populated the database:
    
    
    SingerId: 2, AlbumId: 2, AlbumTitle: Forever Hold Your Peace
    SingerId: 1, AlbumId: 2, AlbumTitle: Go, Go, Go
    SingerId: 2, AlbumId: 1, AlbumTitle: Green
    SingerId: 2, AlbumId: 3, AlbumTitle: Terrified
    SingerId: 1, AlbumId: 1, AlbumTitle: Total Junk
    

You can also visit the function's URL in your browser to see the result of your SQL query.

**Success:** You created an HTTP Cloud Run function that returns Spanner results.

## Clean up

To avoid incurring additional charges to your Google Cloud account for the Spanner and Cloud Run functions resources used in this document:

  1. Delete the instance:
         
         gcloud CLI instances delete test-instance
         

  2. Delete the Cloud Run service you deployed in this tutorial:

###  Node.js 
         
         gcloud run services delete nodejs-spanner-function

###  Python 
         
         gcloud run services delete python-spanner-function




## What's next

  * [Learn more about writing Cloud Run functions](https://docs.cloud.google.com/run/docs/write-functions).
  * [Learn more about deploying Cloud Run functions](https://docs.cloud.google.com/run/docs/deploy-functions).
  * [Learn more about triggering Cloud Run functions](https://docs.cloud.google.com/run/docs/function-triggers).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
