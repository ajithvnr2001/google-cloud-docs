---
url: https://docs.cloud.google.com/storage/docs/delete-ip-filtering-rules/
title: Delete IP filtering rules on a bucket \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:31:41.937352+00:00
---

# Delete IP filtering rules on a bucket  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/delete-ip-filtering-rules/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Guides ](https://docs.cloud.google.com/storage/docs/discover-object-storage-console)



Send feedback 

#  Delete IP filtering rules on a bucket Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to delete individual or multiple [bucket IP filtering](https://docs.cloud.google.com/storage/docs/ip-filtering-overview) rules while keeping IP filtering enabled on a bucket. Deleting rules removes the network access granted by the rules being removed.

## Required roles

To get the required permissions for deleting the IP filtering rules on a bucket, ask your administrator to grant you the Storage Admin (`roles/storage.admin`) role on the bucket. This role contains the permissions required to delete bucket IP filtering rules.

To see the exact permissions that are required, expand the **Required permissions** section:

#### Required permissions

  * `storage.buckets.update`
  * `storage.buckets.setIpFilter`



You can also get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles). You might be able to get these permissions with other predefined roles as well. To see which roles are associated with which permissions, refer to [IAM roles for Cloud Storage](https://docs.cloud.google.com/iam/docs/understanding-roles).

For instructions on granting roles for buckets, see [Set and manage IAM policies on buckets](https://docs.cloud.google.com/storage/docs/access-control/using-iam-permissions).

## Delete IP filtering rules on a bucket

### Console

  1. In the Google Cloud console, go to the Cloud Storage **Buckets** page.

[Go to Buckets](https://console.cloud.google.com/storage/browser)

  2. In the list of buckets, click the name of the bucket you want to update.

  3. On the **Bucket details** page, click the **Configuration** tab.

  4. In the **Permissions** section, navigate to **IP filtering**. Then, click edit **Edit IP filtering configuration**.

The **IP filtering** page displays all the configured IP filtering rules.

  5. Select the checkbox of each rule you want to delete.

**Note:** You can't delete the last remaining rule while IP filtering is enabled. To remove all rules, you must first [disable IP filtering](https://docs.cloud.google.com/storage/docs/disable-ip-filtering) on the bucket.
  6. Click **Delete**.

  7. To confirm that you want to delete the rule, type `DELETE` in the **DELETE** field.

  8. Click **Delete**.




A notification message confirms the rule deletion.

### gcloud

  1. To view the bucket's IP filtering configuration and save it to a JSON file, run the [`gcloud storage buckets describe`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/buckets/describe) command in your development environment:
         
         gcloud storage buckets describe gs://BUCKET_NAME --format="json(ipFilter)" > JSON_FILE_NAME

Where:

     * `BUCKET_NAME` is the name of your bucket.

     * `JSON_FILE_NAME` is the name of the JSON file that contains the settings for the bucket.

  2. Edit the JSON file to remove the specific IP ranges or VPC network sources you want to delete from the `publicNetworkSource.allowedIpCidrRanges` list or the `vpcNetworkSources` list.

The following example shows how to update the JSON file to delete the public IP range `192.0.2.0/24`:
         
         // Original configuration (Before deletion)
             {
               "publicNetworkSource": {
                 "allowedIpCidrRanges": ["192.0.2.0/24", "203.0.113.0/24"]
               },
               // ... other settings ...
             }
           
         
         // Updated configuration (After deletion - '192.0.2.0/24' is excluded)
             {
               "publicNetworkSource": {
                 "allowedIpCidrRanges": ["203.0.113.0/24"]
               },
               // ... other settings ...
             }
           

  3. To apply the updated configuration, run the [`gcloud storage buckets update`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/buckets/update) command in your development environment:
         
         gcloud storage buckets update gs://BUCKET_NAME --ip-filter-file=JSON_FILE_NAME

Where

     * `BUCKET_NAME` is the name of your bucket.

     * `JSON_FILE_NAME` is the name of the JSON file that contains the settings for the bucket.




### JSON API

  1. Have gcloud CLI [installed and initialized](https://docs.cloud.google.com/sdk/docs/install), which lets you generate an access token for the `Authorization` header.

  2. To get the bucket's metadata, including the `ipFilter` configuration, use the `GET` request:
         
         curl -X GET -H "Authorization: Bearer $(gcloud auth print-access-token)" "https://storage.googleapis.com/storage/v1/b/BUCKET_NAME"

  3. Create a JSON file and copy the `ipFilter` object from the output of the `GET` request into this file.

  4. Edit the JSON file to remove the specific IP ranges or VPC network sources you want to delete from the `publicNetworkSource.allowedIpCidrRanges` list or the `vpcNetworkSources` list.

  5. Use [`cURL`](http://curl.haxx.se/) to call the [JSON API](https://docs.cloud.google.com/storage/docs/json_api) with a [PATCH bucket](https://docs.cloud.google.com/storage/docs/json_api/v1/buckets/patch) request, providing the modified `ipFilter` object:
         
         curl -X PATCH --data-binary JSON_FILE_NAME \
          -H "Authorization: Bearer $(gcloud auth print-access-token)" \
          -H "Content-Type: application/json" \
          "https://storage.googleapis.com/storage/v1/b/BUCKET_NAME?project=PROJECT_ID"

Where:

     * `JSON_FILE_NAME` is the name of the JSON file that contains the IP filtering settings for the bucket.
     * `BUCKET_NAME` is the name of your bucket.
     * `PROJECT_ID` is the ID of the project your bucket is associated with.



## What's next

  * [List bucket IP filtering rules](https://docs.cloud.google.com/storage/docs/list-ip-filter).
  * [Disable bucket IP filtering rules](https://docs.cloud.google.com/storage/docs/disable-ip-filtering).



##  Try it for yourself 

If you're new to Google Cloud, create an account to evaluate how Cloud Storage performs in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 

[ Try Cloud Storage free ](https://console.cloud.google.com/freetrial)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
