---
url: https://docs.cloud.google.com/appengine/docs/standard/using-cloud-storage/
title: Use Cloud Storage \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:30:15.019343+00:00
---

# Use Cloud Storage  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/using-cloud-storage/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Guides ](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine)



Send feedback 

#  Use Cloud Storage Stay organized with collections  Save and categorize content based on your preferences. 

If your app needs to read and write files during runtime, or serve files such as movies, images or other static content, we recommend you use a [Cloud Storage](https://docs.cloud.google.com/storage/docs) bucket.

App Engine creates a default bucket when you create an app. This bucket provides the first 5GB of storage for free and includes a free quota for Cloud Storage I/O operations. You can [create other Cloud Storage buckets](https://docs.cloud.google.com/storage/docs/creating-buckets), but only the default bucket includes the first 5GB of storage for free.

## Using Cloud Storage with App Engine

To use a Cloud Storage bucket from an App Engine app:

  1. [View the names of the existing buckets](https://docs.cloud.google.com/storage/docs/listing-buckets) in your App Engine project. You'll specify these names when you upload or download data from Cloud Storage.

We recommend that you store the names of your Cloud Storage buckets in your app's [environment variables](https://docs.cloud.google.com/appengine/docs/standard/reference/app-yaml#environment_variables) instead of hard coding them into your app.

  2. In your app, declare Cloud Storage as a dependency by doing the following:

### Go

Using the `go get cloud.google.com/go/storage` command. Alternatively, you can declare dependencies in your app's `go.mod` file. Learn more [about specifying dependencies](https://docs.cloud.google.com/appengine/docs/standard/go/specifying-dependencies).

Use the Google Cloud Client Library to [upload](https://docs.cloud.google.com/storage/docs/uploading-objects) or [download](https://docs.cloud.google.com/storage/docs/downloading-objects) data from your buckets.

For information about serving static content, see [Storing and Serving Static Files](https://docs.cloud.google.com/appengine/docs/standard/serving-static-files).

### Java

[Add the library to your app's dependencies file](https://docs.cloud.google.com/storage/docs/reference/libraries#client-libraries-install-java).

Use the Google Cloud Client Library to [upload](https://docs.cloud.google.com/storage/docs/uploading-objects) or [download](https://docs.cloud.google.com/storage/docs/downloading-objects) data from your buckets.

For information about serving static content, see [Storing and Serving Static Files](https://docs.cloud.google.com/appengine/docs/standard/serving-static-files).

### Node.js

In `app.yaml`, add your project ID to the `GOOGLE_CLOUD_PROJECT` environment value. Then set the `GCLOUD_STORAGE_BUCKET` environment value to the name of the Cloud Storage bucket you created previously.

Add `@google-cloud/storage` to your app's `package.json` file. Learn more [about specifying dependencies](https://docs.cloud.google.com/appengine/docs/standard/nodejs/specifying-dependencies).

Use the Google Cloud Client Library to [upload](https://docs.cloud.google.com/storage/docs/uploading-objects) or [download](https://docs.cloud.google.com/storage/docs/downloading-objects) data from your buckets.

For information about serving static content, see [Storing and Serving Static Files](https://docs.cloud.google.com/appengine/docs/standard/serving-static-files).

See the [`README.md` file](https://github.com/GoogleCloudPlatform/nodejs-docs-samples/blob/master/appengine/storage/standard/README.md) for instructions on running and testing locally.

### PHP

Add `google/cloud-storage` to your app's `composer.json` file and running `composer install` from your app's directory. Learn more [about specifying dependencies](https://docs.cloud.google.com/appengine/docs/standard/php-gen2/specifying-dependencies).

[Register `Google\Cloud\Storage\StorageClient` as the stream wrapper](https://googleapis.github.io/google-cloud-php/#/docs/google-cloud/v0.122.0/storage/storageclient?method=registerStreamWrapper) for your app. Then use the `gs` protocol to read and write files.

See an [example of registering and using the stream wrapper](https://github.com/googleapis/google-cloud-php/tree/master/Storage#stream-wrapper).

As an alternative, you can [use the Google Cloud client library directly](https://docs.cloud.google.com/storage/docs/reference/libraries).

### Python

Add `google-cloud-storage` to your app's `requirements.txt` file. Learn more [about specifying dependencies](https://docs.cloud.google.com/appengine/docs/standard/python3/specifying-dependencies).

Use the Google Cloud Client Library to [upload](https://docs.cloud.google.com/storage/docs/uploading-objects) or [download](https://docs.cloud.google.com/storage/docs/downloading-objects) data from your buckets.

For information about serving static content, see [Storing and Serving Static Files](https://docs.cloud.google.com/appengine/docs/standard/serving-static-files).

### Ruby

Add `google-cloud-storage` to your app's `Gemfile`. Learn more [about specifying dependencies](https://docs.cloud.google.com/appengine/docs/standard/ruby/specifying-dependencies).

Use the Google Cloud Client Library to [upload](https://docs.cloud.google.com/storage/docs/uploading-objects) or [download](https://docs.cloud.google.com/storage/docs/downloading-objects) data from your buckets.

For information about serving static content, see [Storing and Serving Static Files](https://docs.cloud.google.com/appengine/docs/standard/serving-static-files).




### Using the default bucket

When you create an app, App Engine creates a default bucket that provides the first 5GB of storage for free. The default bucket also includes a free quota for Cloud Storage I/O operations. See Pricing, quotas, and limits for details. You will be charged for storage over the 5GB limit.

The name of the default bucket is in the following format: 
    
    
    project-id.appspot.com
    

App Engine also creates a bucket that it uses for temporary storage when it deploys new versions of your app. This bucket, named `staging.project-id.appspot.com`, is for use by App Engine only. Apps can't interact with this bucket.

### Set bucket permissions

The service account that's associated with your app needs permissions to read and write to buckets in your project. To learn which permissions are required, see [IAM roles for Cloud Storage](https://docs.cloud.google.com/storage/docs/access-control/iam-roles).

Typically, the service account that's associated with your app is the [default App Engine service account](https://docs.cloud.google.com/appengine/docs/standard/configure-service-accounts).

Depending on your organization policy configuration, the default service account might automatically be granted the [Editor role](https://docs.cloud.google.com/iam/docs/roles-overview#basic) on your project. We strongly recommend that you disable the automatic role grant by [ enforcing the `iam.automaticIamGrantsForDefaultServiceAccounts` organization policy constraint](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-service-accounts#disable_service_account_default_grants). If you created your organization after May 3, 2024, this constraint is enforced by default. 

If you disable the automatic role grant, you must decide which roles to grant to the default service accounts, and then [grant these roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access) yourself. 

If the default service account already has the Editor role, we recommend that you replace the Editor role with less permissive roles.To safely modify the service account's roles, use [Policy Simulator](https://docs.cloud.google.com/policy-intelligence/docs/simulate-iam-policies) to see the impact of the change, and then [grant and revoke the appropriate roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

For information about allowing other users, apps, or projects to access a bucket and its contents, see [Setting bucket permissions](https://docs.cloud.google.com/storage/docs/access-control/using-iam-permissions).

## Using Cloud Storage with the local development server

The App Engine local development server doesn't emulate Cloud Storage, so all Cloud Storage requests must be sent over the Internet to an actual Cloud Storage bucket.

## Pricing, quotas, and limits

There are no bandwidth charges associated with Cloud Storage client library calls to Cloud Storage. However, there are [operations charges](https://cloud.google.com/storage/pricing#operations-pricing). In addition, the calls count against your [URL fetch quota](https://docs.cloud.google.com/appengine/docs/quotas#UrlFetch) as the library uses the URL Fetch service to interact with Cloud Storage.

Notice that Cloud Storage is a pay-to-use service; you will be charged according to the Cloud Storage [price sheet](https://cloud.google.com/storage/pricing).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
