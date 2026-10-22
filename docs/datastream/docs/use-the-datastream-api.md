---
url: https://docs.cloud.google.com/datastream/docs/use-the-datastream-api/
title: Use the Datastream API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:42:00.869979+00:00
---

# Use the Datastream API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/datastream/docs/use-the-datastream-api/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Datastream ](https://docs.cloud.google.com/datastream/docs)
  * [ Reference ](https://docs.cloud.google.com/datastream/docs/reference/rest)



Send feedback 

#  Use the Datastream API Stay organized with collections  Save and categorize content based on your preferences. 

Datastream provides a REST API for administering your private connectivity configurations, connection profiles, and streams programmatically. The REST API is defined by resources associated with creating and managing private connectivity configurations, connection profiles, and streams. For details about all resources and their methods, see the [Datastream API Reference](https://docs.cloud.google.com/datastream/docs/reference/rest).

The v1 version of the Datastream API is now generally available. If you're using the v1alpha1 version of this API, then we strongly recommend migrating to the v1 version. The v1alpha1 version will be deprecated by the end of 2022.

When you send requests directly to the Datastream REST API, you must create the correct form of the request, authorize the request as an authenticated user, and process any responses returned. Many of the tasks in this documentation provide API examples using [cURL](http://curl.haxx.se).

For more examples of using the APIs, see the page for the request in the [Datastream API Reference](https://docs.cloud.google.com/datastream/docs/reference/rest). Each page has examples calling the API in several programming languages, as well as a request-specific Explorer to help you see what goes into a well-formed request and what to expect in the response.

You're also using the Datastream API, indirectly, when you use any of the following ways of administering instances:

  * [Google Cloud CLI](https://docs.cloud.google.com/sdk): A command-line interface (CLI) that you can use to work with your instances.

  * [Google Cloud console](https://console.cloud.google.com/): A graphical web interface.




The advantage of using these methods, especially the Google Cloud console, is that they can greatly simplify administering your private connectivity configurations, connection profiles, and streams (depending on your use case). If you're just starting out with Datastream, then we recommend that you start with one of these tools first before working with the REST API directly.

## Enable the API

To use the Datastream API, you need to enable it:

### Console

  1. [Enable the Datastream API](https://console.cloud.google.com/apis/enableflow?apiid=datastream.googleapis.com). 
  2. Select your project.
  3. Select **Continue**.



### gcloud

  1. Enter the following to display the project IDs for your Google Cloud projects: 
         
         gcloud projects list

  2. Set your default project: 
         
         gcloud config set project YOUR_PROJECT_ID

  3. Enable the Datastream API: 
         
         gcloud services enable datastream.googleapis.com




## Permissions

You must have the required permissions to use the Datastream API. These permissions include:

  * Datastream Admin: With this permission, a user gains access to all resources of Datastream used to manage private connectivity configurations, connection profiles, and streams.
  * Datastream Viewer: With this permission, a user has read-only access to private connectivity configurations, connection profiles, and streams in Datastream.



Google Cloud offers Identity and Access Management (IAM), which lets you give more granular access to specific Google Cloud resources and prevents unwanted access to other resources. You can get and set permissions for Datastream using the Google Cloud Console, the IAM methods of the API, or the Google Cloud SDK. For more information, see [Granting, changing, and revoking access to resources](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

## API examples

You can see examples of using the Datastream API with cURL in the following pages of the Datastream documentation:

  * [Manage private connectivity configurations](https://docs.cloud.google.com/datastream/docs/manage-private-connectivity-configurations)
  * [Manage connection profiles](https://docs.cloud.google.com/datastream/docs/manage-connection-profiles)
  * [Manage streams](https://docs.cloud.google.com/datastream/docs/manage-streams)



## Provide JSON data from a file

When you use the API with cURL, you provide property values using the command line. If you're working with sensitive values such as passwords or security keys, then providing them on the command line poses a security risk. For increased security, you can create a file containing the JSON data for the API call, and provide the path to the file on the command line.

To provide JSON data to your cURL API call from a file:

  1. Create a file containing everything enclosed in single quotes for the `--data` field.

Include the curly brackets, but don't include the single quotes.

  2. At the command line, provide the path to the file, preceded by the `@` character, as the `--data` parameter:
         
         --data @<path-to-file>/<filename>

For example, to create a connection profile for a MySQL source, you could create a file named `request.json` with the following content:
         
         {
           "displayName": "my MySQL connection profile",
           "mysql": {
             "host": "10.11.12.13",
             "port": 3306,
             "username": "myusername",
             "password": "mypassword"
           }
         }
         

Then, you would use the following cURL command at the command line:
         
         curl --header "Authorization: Bearer ${ACCESS_TOKEN}" \
              --header 'Content-Type: application/json' \
              --data @./request.json \
              -X POST \
              https://datastream.googleapis.com/v1/projects/myProject/locations/myLocation/connectionProfiles?connectionProfileId=myMySQLconnectionprofile




## Work with long-running API calls

Some API calls, such as object creation, can take some time to complete. Because the API is asynchronous, the call returns immediately, even if the operation is still in progress. If a subsequent API call uses the newly created object, then you must wait for the first operation to complete before proceeding.

You can use the Datastream API to [manage operations](https://docs.cloud.google.com/sdk/gcloud/reference/beta/datastream/operations). This includes:

  * [Showing details about an operation](https://docs.cloud.google.com/sdk/gcloud/reference/beta/datastream/operations/describe)
  * [Listing operations for a region](https://docs.cloud.google.com/sdk/gcloud/reference/beta/datastream/operations/list)
  * [Deleting an operation](https://docs.cloud.google.com/sdk/gcloud/reference/beta/datastream/operations/delete)



## Datastream and Google APIs Discovery Service

[Google APIs Discovery Service](https://developers.google.com/discovery) is a service that you can use to discover Google APIs. For example, when you use the [Google APIs Explorer ](https://developers.google.com/apis-explorer/) tool, you're using the Discovery Service. 

In the Discovery Service, Datastream is represented as "datastream" (for example: https://**datastream**.googleapis.com/$discovery/rest?version=v1).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
