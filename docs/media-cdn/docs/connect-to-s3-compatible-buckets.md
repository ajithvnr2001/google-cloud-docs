---
url: https://docs.cloud.google.com/media-cdn/docs/connect-to-s3-compatible-buckets/
title: Use a private Amazon S3-compatible bucket as an origin \u00a0|\u00a0 Media CDN \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:53:54.806339+00:00
---

# Use a private Amazon S3-compatible bucket as an origin  |  Media CDN  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/media-cdn/docs/connect-to-s3-compatible-buckets/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Media CDN ](https://docs.cloud.google.com/media-cdn/docs)
  * [ Guides ](https://docs.cloud.google.com/media-cdn/docs/overview)



Send feedback 

#  Use a private Amazon S3-compatible bucket as an origin Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to connect Media CDN to private Amazon S3-compatible buckets by using Amazon Simple Storage Service (Amazon S3) and [AWS Signature Version 4](https://docs.aws.amazon.com/AmazonS3/latest/API/sig-v4-authenticating-requests.html). Media CDN does not support AWS Signature Version 4a.

Media CDN supports AWS Signature Version 4 to authenticate origin requests. You can use this feature to connect Media CDN to your private Amazon S3-compatible buckets to ensure that your content is shared only with Media CDN. You can also enable client authentication for greater defense in depth. For more information, see [Use signed requests](https://docs.cloud.google.com/media-cdn/docs/signed-requests).

**Note:** This feature supports only the `GET`, `HEAD`, and `OPTIONS` HTTP methods.

## Before you begin

Verify that you have the following resources:

  * A private Amazon S3 bucket that follows the [naming rules](https://docs.aws.amazon.com/AmazonS3/latest/userguide/bucketnamingrules.html).

  * A dedicated AWS IAM user account to access the preceding private Amazon S3 bucket. Ensure that the bucket grants the `s3:getObject` permission to the AWS IAM user account. For more information about configuring access to your Amazon S3 bucket, see [Identity and access management in Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-access-control.html).

  * The AWS access key ID and the AWS secret access key for the dedicated AWS IAM user account. For more information, see [Managing access keys for IAM users](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html).

  * If you haven't used Secret Manager before, configure [Secret Manager](https://docs.cloud.google.com/secret-manager/docs/configuring-secret-manager).




## Create a service agent for Media CDN

To create a service agent for Media CDN, use the [`gcloud beta services identity create` command](https://docs.cloud.google.com/sdk/gcloud/reference/beta/services/identity/create).

###  gcloud 
    
    
    gcloud beta services identity create \
        --project PROJECT_ID \
        --service=networkservices.googleapis.com
    
    

Replace `PROJECT_ID` with your project ID.

For more information, see [Trigger service agent creation](https://docs.cloud.google.com/iam/docs/create-service-agents#create).

## Store access keys in Secret Manager

Follow these steps to [create a secret](https://docs.cloud.google.com/secret-manager/docs/creating-and-accessing-secrets#add-secret-version) in Secret Manager.

###  Console 

  1. In the Google Cloud console, go to the **Secret Manager** page.

[Go to Secret Manager](https://console.cloud.google.com/security/secret-manager)

  2. On the **Secret Manager** page, click **Create secret**.

  3. In the **Secret details** section, complete the following:

     1. In the **Name** field, enter a name for the secret—for example `aws-access-key-id`.

     2. In the **Secret value** section, skip the **Upload file** field.

     3. In the **Secret value** field, enter the AWS secret access key.

  4. Skip the remaining sections.

  5. Click **Create secret**.




###  gcloud 

Ensure that you're using [version 402.0.0 or later of the Google Cloud CLI](https://docs.cloud.google.com/sdk/docs/install). On Compute Engine or Google Kubernetes Engine (GKE), you must [authenticate with the cloud-platform scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes).
    
    
    gcloud secrets create SECRET_NAME \
        --replication-policy="automatic" \
        --data-file="PATH_TO_AWS_SECRET_ACCESS_KEY"
    

Replace the following:

  * `SECRET_NAME`: the name for your secret, such as `aws-access-key-id`
  * `PATH_TO_AWS_SECRET_ACCESS_KEY`: the path to your AWS secret access key value



For information about adding secret versions, see [Add a secret version](https://docs.cloud.google.com/secret-manager/docs/creating-and-accessing-secrets#add-secret-version).

## Grant the Secret Manager Access role

Follow these steps to grant the [Secret Manager Secret Accessor role](https://docs.cloud.google.com/iam/docs/roles-permissions/secretmanager#secretmanager.secretAccessor) (`roles/secretmanager.secretAccessor`) to the Media CDN service account.

###  Console 

  1. In the Google Cloud console, go to the **Secret Manager** page.

[Go to Secret Manager](https://console.cloud.google.com/security/secret-manager)

  2. Select the secret.
  3. Select **Permissions** , and then select **Grant access**. The **Grant access** dialog appears.
  4. In the **Add principals** section, enter the Media CDN service account in the **New principals** field as follows:  
`service-PROJECT_NUMBER@gcp-sa-mediaedgefill.iam.gserviceaccount.com`

Replace `PROJECT_NUMBER` with your project number.

  5. In the **Assign roles** section, for **Select a role** , select **Secret Manager** , and then select **Secret Manager Secret Accessor**.
  6. Click **Save**.



###  gcloud 
    
    
    gcloud secrets add-iam-policy-binding \
    projects/PROJECT_NUMBER/secrets/SECRET_NAME \
        --member="serviceAccount:service-PROJECT_NUMBER@gcp-sa-mediaedgefill.iam.gserviceaccount.com" \
        --role="roles/secretmanager.secretAccessor"
    

Replace the following:

  * `PROJECT_NUMBER`: your project number
  * `SECRET_NAME`: the name for your secret



## Configure Media CDN to authenticate to your external origin bucket

### Console

  1. In the Google Cloud console, go to the **Media CDN** page.

[Go to Media CDN](https://console.cloud.google.com/net-services/media-cdn)

  2. Click the **Origins** tab.

  3. Click the name of the origin that you want to configure.

The **Edge Cache origin details** page opens.

  4. Click the **Edit** button.

  5. For **Origin address** , choose **Specify an FQDN or IP address** , and then enter the FQDN or IP address.

  6. In the **Private origin authentication** section, select **Authenticate Media CDN's request to this origin with AWS signature version 4**.

  7. Specify the following information:

     * **Key ID** : your AWS access key ID with read permissions to your origin
     * **Reference a secret** : the ID of your access key in [Secret Manager](https://docs.cloud.google.com/secret-manager/docs/creating-and-accessing-secrets) and its version. You can select an existing ID, enter an ID manually, or create a new ID and select it.
**Note:** If the service account does not have permissions to access the selected secret, a prompt appears. Click **Grant** to grant the Secret Manager Secret Accessor role to the service account.
     * **Region** : the region that your Amazon S3 bucket is located in, such as `us-east-1`
  8. For **Protocol** , select **HTTPS**.

  9. Click **Update origin**.




###  gcloud 

  1. To export the current configuration of your service to a YAML file, run the [`gcloud edge-cache services export` command](https://docs.cloud.google.com/sdk/gcloud/reference/edge-cache/services/export):
         
         gcloud edge-cache services export SERVICE_NAME \
             --destination=FILENAME.yaml
         

Replace the following:

     * `SERVICE_NAME`: the name of the Media CDN service
     * `FILENAME`: the name of the YAML file
  2. In Cloud Shell, use a text editor to edit the YAML file.

  3. Update the YAML file so that it has the following lines:
         
         name: ORIGIN_NAME
         originAddress: "S3_BUCKET_NAME.s3.S3_REGION.amazonaws.com"
         protocol: HTTPS
         awsV4Authentication:
           accessKeyId: "AWS_ACCESS_KEY_ID"
           secretAccessKeyVersion: "projects/PROJECT_NUMBER/secrets/SECRET_NAME/versions/SECRET_VERSION"
           originRegion: "S3_REGION"
         

Replace the following:

     * `ORIGIN_NAME`: a name that you set for this origin
     * `S3_BUCKET_NAME`: the name of your Amazon S3 bucket
     * `S3_REGION`: the region that your Amazon S3 bucket is located in, such as `us-east-1`
     * `AWS_ACCESS_KEY_ID`: your AWS access key ID with read permissions to your origin
     * `PROJECT_NUMBER`: your project number
     * `SECRET_NAME`: the ID of your access key in [Secret Manager](https://docs.cloud.google.com/secret-manager/docs/creating-and-accessing-secrets)
     * `SECRET_VERSION`: the secret version to use
  4. Configure host and path rewrites for requests to your origin. For example, to map all requests with a path prefix of `/vod/`, configure a `hostRewrite` that corresponds to the `originAddress` listed in your `EdgeCacheService`'s YAML file. The following code sample shows how to use `hostRewrite`:
         
         name: SERVICE_NAME
         routeRules:
           - priority: 1
           - description: ROUTE_DESCRIPTION
             origin: ORIGIN_NAME
             matchRules:
             - prefixMatch: "/vod/"
             routeAction:
               urlRewrite:
                 hostRewrite: "S3_BUCKET_NAME.s3.S3_REGION.amazonaws.com"
                 pathPrefixRewrite: "/"
               cdnPolicy:
                 cacheMode: CACHE_ALL_STATIC
                 defaultTtl: 3600s
         

Replace `SERVICE_NAME` with the name of your `EdgeCacheService`.

For more information, see [Use third-party storage backends](https://docs.cloud.google.com/media-cdn/docs/routing#third-party-buckets).

  5. Save the YAML file.

  6. To update your configuration, import the YAML file.
         
         gcloud edge-cache origins import ORIGIN_NAME \
             --source=FILENAME.yaml
         




After you configure Media CDN to authenticate to your external bucket, Media CDN generates an HTTP authorization header for all requests to your header. All query parameters are removed from the signature calculation and request to your origin.

Your origin might append additional headers to your responses. To remove the response headers before serving to clients, see [Set custom headers](https://docs.cloud.google.com/media-cdn/docs/custom-headers#set-custom-headers). For more information about configuring origins, see [Origin connectivity and shielding](https://docs.cloud.google.com/media-cdn/docs/origins).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
