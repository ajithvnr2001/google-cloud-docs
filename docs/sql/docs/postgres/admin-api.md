---
url: https://docs.cloud.google.com/sql/docs/postgres/admin-api/
title: Use the Cloud SQL Admin API \u00a0|\u00a0 Cloud SQL for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:43:51.280824+00:00
---

# Use the Cloud SQL Admin API  |  Cloud SQL for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/postgres/admin-api/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ PostgreSQL ](https://docs.cloud.google.com/sql/docs/postgres)
  * [ Reference ](https://docs.cloud.google.com/sql/docs/postgres/apis)



Send feedback 

#  Use the Cloud SQL Admin API Stay organized with collections  Save and categorize content based on your preferences. 

[MySQL](https://docs.cloud.google.com/sql/docs/mysql/admin-api "View this page for the MySQL database engine") | PostgreSQL | [SQL Server](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api "View this page for the SQL Server database engine")

Cloud SQL provides a REST API for administering your instances programmatically. The REST API is defined by BackupRuns, Databases, Instances, Flags, Operations, SslCerts, Tiers, and Users resources. Each resource supports methods for accessing and working with it. For example, the Instances resource supports methods such as get, insert, and list. For details of all the resources and their methods, see the [Cloud SQL Admin API Reference](https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest).

**Important:** The Cloud SQL Admin API v1 is now generally available. It is and will continue to be compatible with the v1beta4 version. There is no requirement to migrate from v1beta4 to the v1 Admin API.

When you send requests directly to the Cloud SQL REST API, you must create the correct form of the request, authorize the request as an authenticated user, and process any responses returned. Many of the tasks in this documentation provide API examples using [cURL](http://curl.haxx.se).

For more examples of using the APIs, see the page for the request in the [Cloud SQL Admin API Reference](https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest). Each page has examples calling the API in several programming languages, as well as a request-specific Explorer to help you see what goes into a well-formed request and what to expect in the response.

You are also using the Cloud SQL Admin API, indirectly, when you use any of the following ways of administering instances:

  * [](https://docs.cloud.google.com/sdk)[gcloud CLI](https://docs.cloud.google.com/sdk/gcloud), which contains a command-line interface you can use to work with your instances.

  * One of the [Client Libraries](https://docs.cloud.google.com/sql/docs/postgres/admin-api/libraries), such as for Java, Python, or .NET.

  * [Google Cloud console](https://console.cloud.google.com/), a graphical web interface.




The advantage of using these methods, especially the Google Cloud console, is that they can greatly simplify administering your instances (depending on your use case). If you are just starting out with Cloud SQL, we recommend that you start with one of these tools first before working with the REST API directly.

## Enable the API

To use the Cloud SQL Admin API, you need to enable it:

### Console

  1. **Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=sqladmin&redirect=https%3A//console.cloud.google.com)

  2. Select your project.
  3. Select **Continue**.



### gcloud

  1. Enter the following to display the project IDs for your Google Cloud projects: 
         
         gcloud projects list

  2. Set your default project: 
         
         gcloud config set project YOUR_PROJECT_ID

  3. Enable the Cloud SQL Admin API: 
         
         gcloud services enable sqladmin.googleapis.com




## Authorize requests

Your application needs to identify itself every time it sends a request to the Cloud SQL Admin API, by including an [API key](https://cloud.google.com/docs/authentication/api-keys) with each request.

##  Acquiring and using an API key 

To acquire an API key:

  1. Open the [Credentials page](https://console.cloud.google.com/apis/credentials) in the Google Cloud console.
  2. This API supports two types of credentials. Create whichever credentials are appropriate for your project: 
     * **OAuth 2.0:** Whenever your application requests private user data, it must send an OAuth 2.0 token along with the request. Your application first sends a client ID and, possibly, a client secret to obtain a token. You can generate OAuth 2.0 credentials for web applications, service accounts, or installed applications.

**Note:** Since this API doesn't have any methods that require OAuth 2.0 authorization, you might only need to obtain API keys, which are described below. However, if your application calls other APIs that require user authorization, then you still need OAuth 2.0 credentials.

For more information, see the [OAuth 2.0 documentation](https://developers.google.com/identity/protocols/OAuth2).

     * **API keys:** A request that does not provide an OAuth 2.0 token must send an API key. The key identifies your project and provides API access, quota, and reports.

The API supports several types of restrictions on API keys. If the API key that you need doesn't already exist, then create an API key in the Console by clicking **[Create credentials](https://console.cloud.google.com/apis/credentials) > API key**. You can restrict the key before using it in production by clicking **Restrict key** and selecting one of the **Restrictions**.




To keep your API keys secure, follow the [best practices for securely using API keys](https://cloud.google.com/docs/authentication/api-keys).

After you have an API key, your application can append the query parameter `key=yourAPIKey` to all request URLs.

The API key is safe for embedding in URLs; it doesn't need any encoding.

**Note:** For more information on authorizing requests, see [Authorize Requests](https://docs.cloud.google.com/sql/docs/postgres/admin-api/how-tos/authorizing).

## Permissions

In addition to authorization, the principal must have the required permissions for the API request. For more information, see [IAM permissions in Cloud SQL](https://docs.cloud.google.com/sql/docs/postgres/iam-permissions).

## API examples

You can see examples of using the API with cURL on the **REST v1** and the **REST v1beta4** tabs in the [How-to Guides](https://docs.cloud.google.com/sql/docs/postgres/how-to) for this documentation set.

## Provide JSON data from a file

When you use the API with cURL, you provide property values using the command line. If you are working with sensitive values such as passwords or security keys, providing them on the command line poses a security risk. For increased security, you can create a file containing the JSON data for the API call, and provide the path to the file on the command line.

To provide JSON data to your cURL API call from a file:

  1. Create a file containing everything enclosed in the single quotes for the `--data` field.

Include the curly brackets, but do not include the single quotes.

  2. At the command line, provide the path to the file, preceded by the `@` character, as the `--data` parameter:
         
         --data @<path-to-file>/<filename>

For example, to create a database user, you could create a file named `data.json` with the following content:
         
         {"host": "%", "name": "user1", "password": "abc123"}
         

Then you would use the following cURL command at the command line:
         
         curl --header "Authorization: Bearer ${ACCESS_TOKEN}" \
              --header 'Content-Type: application/json' \
              --data @./data.json \
              -X POST \
              https://www.googleapis.com/sql/v1beta4/projects/myProject/instances/myInstance/users




## Work with long-running API calls

Some API calls, such as object creation, can take some time to complete. Because the API is asynchronous, the call returns immediately, even if the operation is still in progress. If a subsequent API call uses the newly created object, you must wait for the first operation to complete before proceeding.

You can wait programmatically by using the operation resource, which is returned for all insert calls. Provide the value of the `name` property to the [operation get method](https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1beta4/operations/get) and inspect the status of the operation, When the `status` property changes from `PENDING` to `DONE`, you can access the newly created object.

## Cloud SQL and Google APIs Discovery Service

[Google APIs Discovery Service](https://developers.google.com/discovery) is a service that you can use to discover Google APIs. For example, when you use the [Google APIs Explorer ](https://developers.google.com/apis-explorer/) tool, you are using the Discovery Service. In the Discovery Service, Cloud SQL is represented as "sqladmin" (for example: https://www.googleapis.com/discovery/v1/apis/**sqladmin** /v1beta4/sql.operation). This is different than the base path "sql" that you use in requests to the REST API (for example: https://www.googleapis.com/**sql** /v1beta4/projects/example-id/instances).

Some client libraries also use the Discovery Service. In the client creation code, be sure to use "sqladmin" to access the correct discovery document. For more information, see [Client Libraries](https://docs.cloud.google.com/sql/docs/postgres/admin-api/libraries).

## Use VPC Service Controls with the Cloud SQL Admin API

VPC Service Controls let you create a service perimeter around the Cloud SQL Admin API to help mitigate data exfiltration. The service perimeter allows free communication within the perimeter, but blocks all communication across the perimeter.

Before adding VPC Service Controls, it is recommended that you enable private IP and disable public IP on the Cloud SQL instances that you plan to add to the service perimeter. These requirements also apply to clones, read replicas, and failover replicas.

See [Configure VPC Service Controls](https://docs.cloud.google.com/sql/docs/postgres/admin-api/configure-service-controls).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
