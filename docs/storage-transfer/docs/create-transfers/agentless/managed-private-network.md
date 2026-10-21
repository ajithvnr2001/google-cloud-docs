---
url: https://docs.cloud.google.com/storage-transfer/docs/create-transfers/agentless/managed-private-network/
title: Transfer over a Google-managed private network \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:52:57.051430+00:00
---

# Transfer over a Google-managed private network  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage-transfer/docs/create-transfers/agentless/managed-private-network/

  * [ Guides ](https://docs.cloud.google.com/storage-transfer/docs/overview)



#  Transfer over a Google-managed private network Stay organized with collections  Save and categorize content based on your preferences. 

When transferring data from Amazon S3 to Cloud Storage, data typically traverses public internet peering links, where AWS bills standard internet data egress charges. Storage Transfer Service offers a **Google-managed private network** option for transfers from Amazon S3, allowing your data to flow over secure private routing provisioned automatically by Google.

Using a Google-managed private network reduces AWS internet egress costs and simplifies network security by eliminating the need to configure and maintain customer-managed physical interconnects.

## Key benefits

The Google-managed private network option provides the following operational and financial benefits for Amazon S3 transfers:

  * **Reduce internet egress costs** : Transferring from Amazon S3 over the Google-managed private network bypasses standard AWS internet egress rates. You pay no AWS S3 internet egress charges; instead, you pay a predictable per-GiB data processing rate to Google Cloud. See [Pricing](https://docs.cloud.google.com/storage-transfer/pricing) for details. Standard AWS API request charges (such as Amazon S3 `LIST`, `GET`, and `HEAD` operations) still apply according to the AWS pricing schedule.

  * **Eliminate public internet exposure** : Data travels directly over Google-managed private interconnect connection between AWS and Google Cloud. Because packets never traverse public internet routing tables, you eliminate the risk of public interception while simplifying firewall and zero-trust compliance.

  * **Zero infrastructure maintenance** : Unlike a customer-managed private network, you don't need to provision, configure, or pay recurring port fees for physical interconnects (such as Cloud Interconnect or AWS Direct Connect), VPN gateways, or custom DNS routing. Google fully manages the private networking stack end-to-end.

  * **Instant deployment with zero lead time** : Setting up dedicated interconnect circuits can take weeks. With a Google-managed private network, you can begin transferring over private routing immediately, without installing or managing any transfer agents.




## Bandwidth and performance considerations

All Storage Transfer Service jobs across all projects utilizing the Google-managed private network share a common pooled network capacity. During periods of peak global utilization, transfer speeds might experience throttling or increased latency.

Workloads consisting primarily of large objects are impacted more by high pool utilization than workloads consisting primarily of smaller objects. If your workload requires dedicated bandwidth without shared pool contention, consider configuring a [customer-managed private network](https://docs.cloud.google.com/storage-transfer/docs/create-transfers/agentless/customer-managed-private-network).

## Supported AWS regions

The Google-managed private network option is available for agentless transfers from the following Amazon S3 regions:

`ap-east-1`  
`ap-northeast-1`  
`ap-northeast-2`  
`ap-northeast-3`  
`ap-south-1`  
`ap-south-2`  
`ap-southeast-1`  
`ca-central-1`  
`ca-west-1`  
`eu-central-1`  
`eu-central-2`  
|  `eu-north-1`  
`eu-south-1`  
`eu-south-2`  
`eu-west-1`  
`eu-west-2`  
`eu-west-3`  
`us-east-1`  
`us-east-2`  
`us-west-1`  
`us-west-2` |   
---|---|---  
  
## Before you begin

Before creating your transfer, you must configure IAM and source permissions.

### Configure IAM permissions

Follow the instructions in [Agentless transfer permissions](https://docs.cloud.google.com/storage-transfer/docs/iam-cloud) to grant the required Google Cloud permissions.

### Configure access to your S3 bucket

Follow the instructions in [Configure access to a source: Amazon S3](https://docs.cloud.google.com/storage-transfer/docs/source-amazon-s3) to configure access to your data in Amazon S3.

## Create a Google-managed private network transfer

You can enable the Google-managed private network option when creating a new transfer job or when updating an existing Amazon S3 transfer specification using the Google Cloud console or the REST API.

###  Console 

The Google-managed private network option is enabled with a checkbox in the **Choose settings** step of creating a transfer job.

**Tip:** To update an existing transfer job to use the Google-managed private network, select the job, click the **Configuration** tab, and click to edit the **Network** settings.

To create a new job using the Google-managed private network:

  1. Go to the **Storage Transfer Service** page in the Google Cloud console.

[Go to Storage Transfer Service](https://console.cloud.google.com/transfer/)

  2. Click **Create transfer job**. The **Create a transfer job** page is displayed.

  3. Under **Source type** , select **Amazon S3**.

  4. As your **Destination type** select **Google Cloud Storage**.

  5. Select your **Scheduling mode**. _Batch transfers_ execute on a one-time or scheduled basis. _Event-driven transfers_ continuously monitor the source and transfer data when it's added or modified.

To configure an event-driven transfer, follow the instructions at [Event-driven transfers](https://docs.cloud.google.com/storage-transfer/docs/event-driven-transfers).

  6. Click **Next step**.

  7. In the **Bucket or folder name** field, enter the source bucket name.

The bucket name is the name as it appears in the [AWS Management Console](https://console.aws.amazon.com/).

  8. Select your Amazon Web Services (AWS) authentication method. See [Configure access to a source: Amazon S3](https://docs.cloud.google.com/storage-transfer/docs/source-amazon-s3) for details.

     * **Secret resource** : Select this option to use an Amazon credential saved in Secret Manager. Select a secret from the list, or enter one manually in the format `projects/PROJECT_NUMBER/secrets/SECRET_NAME`.

     * **Access key** : Enter your access key in the **Access key ID** field and the secret associated with your access key in the **Secret access key** field.

     * **AWS IAM role for identity federation** : Enter your ARN in the **AWS IAM role ARN** field, with the following syntax:

       * Standard AWS regions:
             
             arn:aws:iam::AWS_ACCOUNT:role/AWS_ROLE_NAME

       * AWS GovCloud regions:
             
             arn:aws-us-gov:iam::AWS_ACCOUNT:role/AWS_ROLE_NAME

Replace the following:

       * `AWS_ACCOUNT`: The AWS account ID with no hyphens.
       * `AWS_ROLE_NAME`: The AWS role name. If your organization uses paths to organize roles, include the path with the role name. For example, `developers/transfer_user`.

For more information on ARNs, see [IAM ARNs](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_identifiers.html#identifiers-arns).

  9. If this is an [event-driven transfer](https://docs.cloud.google.com/storage-transfer/docs/event-driven-transfers), enter the Amazon SQS queue ARN, which takes the following format:

     * Standard AWS regions:
           
           arn:aws:sqs:us-east-1:1234567890:event-queue

     * AWS GovCloud regions:
           
           arn:aws-us-gov:sqs:us-gov-east-1:1234567890:event-queue

  10. Optionally, choose to [filter objects by prefix](https://docs.cloud.google.com/storage-transfer/docs/filtering-objects-from-transfers), by last modified date, or by [storage class](https://docs.cloud.google.com/storage-transfer/docs/filtering-by-storage-class). If you specified a folder as your source location, prefix filters are relative to that folder. For example, if your source is `my-test-bucket/path/`, an include filter of `file` includes all files starting with `my-test-bucket/path/file`.

  11. Click **Next step**.

  12. In the **Bucket or folder** field, enter the destination bucket and (optionally) folder name, or click **Browse** to select a bucket from a list of existing buckets in your current project. To create a new bucket, click ![Bucket icon](https://docs.cloud.google.com/static/storage-transfer/docs/images/bucket_icon.png)**Create new bucket**.

  13. Click **Next step**.

  14. Choose your scheduling options:

Note: The Storage Transfer Service displays transfer job schedules in your local timezone, but it stores those times in Universal Time Coordinated (UTC). If you are affected by Daylight Savings Time (DST), you might experience a transfer job schedule change when DST starts or ends.

     1. From the **Run once** drop-down list, select one of the following:

        * **Run once** : Runs a single transfer, starting at a time that you select.
        * **Run every day** : Runs a transfer daily, starting at a time that you select.

You can enter an optional **End date** , or leave **End date** blank to run the transfer continually.

        * **Run every week** : Runs a transfer weekly, starting at a time that you select.
        * **Run with custom frequency** : Runs a transfer at a frequency that you select. You can choose to repeat the transfer at a regular interval of **Hours** , **Days** , or **Weeks**.

You can enter an optional **End date** , or leave **End date** blank to run the transfer continually.

        * **Run on demand** : Will not trigger a run when this transfer job is created. You'll need to [manually start the job](https://docs.cloud.google.com/storage-transfer/docs/manage-transfers#run-job).
     2. From the **Starting now** drop-down list, select one of the following:

        * **Starting now** : Starts the transfer after you click **Create**.
        * **Starting on** : Starts the transfer on the date and time that you select. Click **Calendar** to display a calendar to select the start date.
  15. Click **Next step**.

  16. Choose settings for the transfer job.

     1. In the **Description** field, enter a description of the transfer. As a best practice, enter a description that is meaningful and unique so that you can tell jobs apart.

     2. Optionally, provide a [manifest](https://docs.cloud.google.com/storage-transfer/docs/manifest) to specify the exact objects to transfer.

     3. Under **Metadata options** , select the desired storage class and time created behavior. See [Metadata preservation](https://docs.cloud.google.com/storage-transfer/docs/metadata-preservation) for details.

     4. Under **When to overwrite** , select one of the following:

        * **Never** : Does not overwrite a destination file if the source file has the same name. The source file is skipped.
        * **If different** : Overwrites destination files if the source file with the same name has different Etags or checksum values.
        * **Always** : Always overwrites destination files when the source file has the same name, even if they're identical.
     5. Under **When to delete** , select one of the following:

        * **Never** : Never delete files from either the source or destination.
        * **Delete files from source after they're transferred** : Delete files from the source after they're transferred to the destination. If a source file isn't transferred, for example because it already exists in the destination, the source file is not deleted.

Important: If you don't have local backup, this option is a non-reversible action.

        * **Delete files from destination if they're not also at source** : If files in the destination Cloud Storage bucket aren't also in the source, then delete the files from the Cloud Storage bucket.

This option ensures that the destination Cloud Storage bucket exactly matches your source.

     6. **Choose network routing options** :

        * Select **Use managed private network**.
     7. Under **Logging options** , select **Enable logging in Cloud Logging** if you want to generate a granular record of the actions performed on each transferred file. Cloud Logging costs apply. See [Log transfer actions](https://docs.cloud.google.com/storage-transfer/docs/transfer-logs) for details.

     8. Optionally, select **Get transfer operation status updates via Cloud Pub/Sub notifications**), select your Pub/Sub topic, and choose which events trigger notifications. See [Pub/Sub notifications](https://docs.cloud.google.com/storage-transfer/docs/pub-sub-transfer) for details.

     9. Under **Choose service account type** , select the identity to use:

        * **Storage Transfer Service service agent** : The default Google-managed service agent is automatically granted access to the source and destination buckets.
        * **User-managed service agent** : Use a custom service account that you have created. Before selecting this option, ensure that your service account has been granted access to the source bucket, the destination bucket, and Pub/Sub. See [Use a user-managed service agent](https://docs.cloud.google.com/storage-transfer/docs/delegate-service-agent-permissions).
  17. Click **Create** to create the transfer job.




###  gcloud CLI 

The gcloud CLI does not support configuring transfers over a Google-managed private network. Use the Google Cloud console or REST API to enable this option.

###  Client libraries 

Storage Transfer Service client libraries don't support configuring transfers over a Google-managed private network. Use the Google Cloud console or REST API to enable this option.

###  REST API 

To configure a transfer using the REST API, set the boolean field `transferSpec.awsS3DataSource.managedPrivateNetwork` to `true` inside your JSON request payload when calling [`transferJobs.create`](https://docs.cloud.google.com/storage-transfer/docs/reference/rest/v1/transferJobs/create) or [`transferJobs.patch`](https://docs.cloud.google.com/storage-transfer/docs/reference/rest/v1/transferJobs/patch).

#### HTTP request
    
    
    POST https://storagetransfer.googleapis.com/v1/transferJobs
    

#### Request body
    
    
    {
      "description": "S3 to Cloud Storage over Google-managed private network",
      "status": "ENABLED",
      "projectId": "PROJECT_ID",
      "transferSpec": {
        "awsS3DataSource": {
          "bucketName": "AWS_SOURCE_NAME",
          "managedPrivateNetwork": true,
          "awsAccessKey": {
            "accessKeyId": "AWS_ACCESS_KEY_ID",
            "secretAccessKey": "AWS_SECRET_ACCESS_KEY"
          }
        },
        "gcsDataSink": {
          "bucketName": "GCS_SINK_NAME"
        },
        "transferOptions": {
          "overwriteWhen": "DIFFERENT",
          "deleteObjectsFromSourceAfterTransfer": false
        }
      }
    }
    

This example uses AWS access credentials to authenticate. See [Configure access to Amazon S3](https://docs.cloud.google.com/storage-transfer/docs/source-amazon-s3) for details on using federated identity or credentials in Secret Manager.

## Monitoring and verifying private network routing

After starting your transfer job, verify that the data is egressing over the Google-managed private network:

  1. **Cloud Logging** : When `transfer-logs` are enabled (`--log-actions=COPY,DELETE,FAILED`), inspect the structured logs for your transfer operation. The connection metadata inside the `COPY` action log confirms successful replication over the private network path.

  2. **Billing verification** : Check your AWS and Google Cloud billing dashboards. On your AWS invoice, you will see zero public internet data transfer out (`DataTransfer-Out-Bytes`) charges for the transferred objects. Instead, the per-GiB data processing fee appears on your Google Cloud invoice under Storage Transfer Service.




## Alternative network routing options

If the Google-managed private network does not meet your workload requirements, Storage Transfer Service supports several other network routing options for Amazon S3:

  * **Public internet routing** : Data transfers across standard public internet peering links between Amazon S3 and Google Cloud. All API commands, authentication headers, and object data streams are end-to-end encrypted in transit using HTTPS with Transport Layer Security (TLS 1.3). Standard AWS internet data egress rates apply. For details, see [Transfer from Amazon S3](https://docs.cloud.google.com/storage-transfer/docs/create-transfers/agentless/s3).

  * **Customer-managed private network** : Data traverses your own pre-configured hybrid connectivity infrastructure (such as Cloud Interconnect, Cloud VPN, or AWS Direct Connect) over private IP addresses. This option gives you full architectural control and dedicated, predictable network bandwidth. For details, see [Transfers over a customer-managed private network](https://docs.cloud.google.com/storage-transfer/docs/create-transfers/agentless/customer-managed-private-network).

  * **Amazon CloudFront CDN routing** : Data is retrieved through an Amazon CloudFront distribution in front of your S3 bucket. Depending on your AWS CloudFront pricing tier and data volume, this can reduce internet egress charges compared to direct public S3 downloads. For details, see [Transfer from S3 via CloudFront](https://docs.cloud.google.com/storage-transfer/docs/s3-cloudfront).




Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
