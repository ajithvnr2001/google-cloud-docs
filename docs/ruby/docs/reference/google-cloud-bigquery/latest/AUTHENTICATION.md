---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery/latest/AUTHENTICATION/
title: Authentication \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:12:54.033241+00:00
---

# Authentication  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery/latest/AUTHENTICATION/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Authentication Stay organized with collections  Save and categorize content based on your preferences. 

1.64.0 (latest)  1.63.1  1.62.0  1.61.1  1.60.0  1.59.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.0  1.53.0  1.52.1  1.51.1  1.50.0  1.49.1  1.48.1  1.47.0  1.46.1  1.45.0  1.44.2  1.43.1  1.42.0  1.41.0  1.40.0  1.39.0  1.38.1 

In general, the google-cloud-bigquery library uses [Service Account](https://cloud.google.com/iam/docs/creating-managing-service-accounts) credentials to connect to Google Cloud services. When running on Google Cloud Platform (GCP), including Google Compute Engine (GCE), Google Kubernetes Engine (GKE), Google App Engine (GAE), Google Cloud Functions (GCF) and Cloud Run, the credentials will be discovered automatically. When running on other environments, the Service Account credentials can be specified by providing the path to the [JSON keyfile](https://cloud.google.com/iam/docs/managing-service-account-keys) for the account (or the JSON itself) in environment variables. Additionally, Cloud SDK credentials can also be discovered automatically, but this is only recommended during development.

## Project and Credential Lookup

The google-cloud-bigquery library aims to make authentication as simple as possible, and provides several mechanisms to configure your system without providing **Project ID** and **Service Account Credentials** directly in code.

**Project ID** is discovered in the following order:

  1. Specify project ID in method arguments
  2. Specify project ID in configuration
  3. Discover project ID in environment variables
  4. Discover GCE project ID



**Credentials** are discovered in the following order:

Warning

If you accept a credential configuration (JSON file or Hash) from an external source for authentication to Google Cloud, you must validate it before providing it to a Google API client library. Providing an unvalidated credential configuration to Google APIs can compromise the security of your systems and data.

  1. Specify credentials in method arguments
  2. Specify credentials in configuration
  3. Discover credentials path in environment variables
  4. Discover credentials JSON in environment variables
  5. Discover credentials file in the Cloud SDK's path
  6. Discover GCE credentials



### Google Cloud Platform environments

When running on Google Cloud Platform (GCP), including Google Compute Engine (GCE), Google Kubernetes Engine (GKE), Google App Engine (GAE), Google Cloud Functions (GCF) and Cloud Run, the **Project ID** and **Credentials** and are discovered automatically. Code should be written as if already authenticated.

### Environment Variables

The **Project ID** and **Credentials JSON** can be placed in environment variables instead of declaring them directly in code. Each service has its own environment variable, allowing for different service accounts to be used for different services. (See the READMEs for the individual service gems for details.) The path to the **Credentials JSON** file can be stored in the environment variable, or the **Credentials JSON** itself can be stored for environments such as Docker containers where writing files is difficult or not encouraged.

The environment variables that BigQuery checks for project ID are:

  1. `BIGQUERY_PROJECT`
  2. `GOOGLE_CLOUD_PROJECT`



The environment variables that BigQuery checks for credentials are configured on [Google::Cloud::Bigquery::Credentials](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery/latest/Google-Cloud-Bigquery-Credentials "Google::Cloud::Bigquery::Credentials \(class\)"):

  1. `BIGQUERY_CREDENTIALS` \- Path to JSON file, or JSON contents
  2. `BIGQUERY_KEYFILE` \- Path to JSON file, or JSON contents
  3. `GOOGLE_CLOUD_CREDENTIALS` \- Path to JSON file, or JSON contents
  4. `GOOGLE_CLOUD_KEYFILE` \- Path to JSON file, or JSON contents
  5. `GOOGLE_APPLICATION_CREDENTIALS` \- Path to JSON file


    
    
    require "google/cloud/bigquery"
    
    ENV["BIGQUERY_PROJECT"]     = "my-project-id"
    ENV["BIGQUERY_CREDENTIALS"] = "path/to/keyfile.json"
    
    bigquery = Google::Cloud::Bigquery.new

### Configuration

The **Project ID** and the path to the **Credentials JSON** file can be configured instead of placing them in environment variables or providing them as arguments.
    
    
    require "googleauth"
    require "google/cloud/bigquery"
    
    credentials = ::Google::Auth::ServiceAccountCredentials.make_creds(
      json_key_io: ::File.open("/path/to/keyfile.json")
    )
    
    Google::Cloud::Bigquery.configure do |config|
      config.project_id  = "my-project-id"
      config.credentials = credentials
    end
    
    bigquery = Google::Cloud::Bigquery.new

### Cloud SDK

This option allows for an easy way to authenticate during development. If credentials are not provided in code or in environment variables, then Cloud SDK credentials are discovered.

To configure your system for this, simply:

  1. [Download and install the Cloud SDK](https://cloud.google.com/sdk)
  2. Authenticate using OAuth 2.0 `$ gcloud auth login`
  3. Write code as if already authenticated.



**NOTE:** This is _not_ recommended for running in production. The Cloud SDK _should_ only be used during development.

## Creating a Service Account

Google Cloud requires a **Project ID** and **Service Account Credentials** to connect to the APIs. You will use the **Project ID** and **JSON key file** to connect to most services with google-cloud-bigquery.

If you are not running this client on Google Compute Engine, you need a Google Developers service account.

  1. Visit the [Google Cloud Console](https://console.cloud.google.com/project).
  2. Create a new project or click on an existing project.
  3. Activate the menu in the upper left and select **APIs & Services**. From here, you will enable the APIs that your application requires.

_Note: You may need to enable billing in order to use these services._

  4. Select **Credentials** from the side navigation.

Find the "Create credentials" drop down near the top of the page, and select "Service account" to be guided through downloading a new JSON key file.

If you want to re-use an existing service account, you can easily generate a new key file. Just select the account you wish to re-use click the pencil tool on the right side to edit the service account, select the **Keys** tab, and then select **Add Key**.

The key file you download will be used by this library to authenticate API requests and should be stored in a secure location.




## Troubleshooting

If you're having trouble authenticating you can ask for help by following the [Troubleshooting Guide](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery/latest/TROUBLESHOOTING "Troubleshooting Guide").

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-11 UTC."],[],[]] 
