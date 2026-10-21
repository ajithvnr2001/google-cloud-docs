---
url: https://docs.cloud.google.com/storage/docs/direct-connectivity/
title: gRPC direct connectivity \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:52:28.060010+00:00
---

# gRPC direct connectivity  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/direct-connectivity/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Guides ](https://docs.cloud.google.com/storage/docs/discover-object-storage-console)



Send feedback 

#  gRPC direct connectivity Stay organized with collections  Save and categorize content based on your preferences. 

Direct connectivity lets supported Google Cloud client libraries make authenticated gRPC network connections directly to Cloud Storage, which reduces latency and connection overhead. When you use gRPC with direct connectivity, client library requests bypass [Google Front Ends (GFEs)](https://docs.cloud.google.com/docs/security/infrastructure/design#google-frontend-service) and are routed straight to Cloud Storage.

Direct connectivity is only available for requests made from Compute Engine virtual machines (VMs).

## Requirements for direct connectivity

Direct connectivity is enabled by default when you use supported Cloud Storage client libraries to connect to Cloud Storage, but becomes available only if the following conditions are all met:

  * The Compute Engine VMs interacting with Cloud Storage must have an [attached service account](https://docs.cloud.google.com/compute/docs/instances/change-service-account), even if the service account has no permissions. The service account is used to represent the Compute Engine VM in the [Application Layer Transport Security](https://docs.cloud.google.com/security/encryption-in-transit/application-layer-transport-security) handshake process.

  * The Compute Engine VMs interacting with a Cloud Storage bucket must be co-located with the bucket. For example, if the bucket is in `us-central1`, the VM can be located in `us-central1-a`. If the bucket is in a multi-region or dual-region, the VM must be located in a region that makes up the multi-region or dual-region. For example, if a bucket is located in the `us` multi-region, the VM can be located in `us-east4-c`.

For more information about bucket locations, see [Locations](https://docs.cloud.google.com/storage/docs/locations).

  * Your [routes](https://docs.cloud.google.com/vpc/docs/configure-private-google-access#config-routing-custom) and [firewall rules](https://docs.cloud.google.com/vpc/docs/configure-private-google-access#config-firewall) allow IPv4 traffic to reach `34.126.0.0/18` and IPv6 traffic to reach `2001:4860:8040::/42`. Avoid restricting the destination ports in the firewall rules, as all ports are used for serving. In addition, traffic must be allowed to reach the endpoints `storage.googleapis.com:443` and `directpath-pa.googleapis.com:443`.

To learn how to check whether a connection can be made to these endpoints, see Check network configurations. For information about setting up routes, see [Configure routes](https://docs.cloud.google.com/vpc-service-controls/docs/set-up-private-connectivity#configure-routes).

  * Cloud Storage client libraries have specific credential requirements in order to authenticate applications to Cloud Storage and have direct connectivity be available:

    * The Java client library requires either user account credentials or service account credentials.

    * The C++ client library requires service account credentials.

    * The Go client library requires service account credentials. Versions before 1.52.0 require the [default service account](https://docs.cloud.google.com/iam/docs/service-account-types#default) credentials of the VM accessing your bucket.

To view the name of the account that your VM uses to authenticate to Cloud Storage, use the `gcloud auth list` command:
    
    gcloud auth list --filter=status:ACTIVE --format="value(account)"
    

If you're using the Go client library and need to check if the Google account being used to authenticate matches your VM's default service account, use the `gcloud compute instances describe` command:
    
    gcloud compute instances describe INSTANCE_NAME --format='yaml(serviceAccounts)'
    

Replace `INSTANCE_NAME` with the name of your instance.

For more information about authentication, see [Overview of Google identity management](https://docs.cloud.google.com/architecture/identity/overview-google-authentication).




## Check connectivity by using the Google Cloud CLI

The Google Cloud CLI can test the diagnostics of direct connectivity on your bucket by issuing a `GET` call to the bucket using `gcloud storage buckets describe gs://example-bucket`. This section describes how to perform a diagnostic test for direct connectivity by using the Google Cloud CLI.

### Before you begin

  1. Make sure you have the `storage.buckets.get` IAM permission on the bucket, which can be [granted](https://docs.cloud.google.com/storage/docs/access-control/using-iam-permissions) using the Storage Legacy Bucket Reader (`roles/storage.legacyBucketReader`) role.

  2. The `gcloud alpha storage diagnose` command is only available in the Google Cloud CLI version 531.0.0 or later. To use this command, we recommend [upgrading to the latest Google Cloud CLI version](https://docs.cloud.google.com/sdk/gcloud/reference/components/update).




### Run the diagnosis

To check whether direct connectivity is available, run [`gcloud alpha storage diagnose`](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/storage/diagnose) with the argument `--test-type=DIRECT_CONNECTIVITY`:
    
    
    gcloud alpha storage diagnose --test-type=DIRECT_CONNECTIVITY gs://BUCKET_NAME
    

Replace the following:

  * `BUCKET_NAME`: the name of your bucket. For example, `my-bucket`.



If a connection can be made, you receive a response similar to the following:
    
    
    Using my-bucket bucket for the diagnostic tests.
    Bucket location : US
    Bucket storage class : STANDARD
    Running diagnostic: Direct Connectivity Diagnostic...
    WARNING: This diagnostic is experimental. The output may change, and checks may be added or removed at any time. Please do not rely on the diagnostic being present.
    Finished running diagnostic: Direct Connectivity Diagnostic
    Generating diagnostic report...
    NAME
    Direct Connectivity Diagnostic
        ┌────────────────────────────┬─────────────────────────────────────────────────────────────────────────┬──────────┐
        │            NAME            │                           PAYLOAD_DESCRIPTION                           │  RESULT  │
        ├────────────────────────────┼─────────────────────────────────────────────────────────────────────────┼──────────┤
        │ Direct Connectivity Call   │ Able to get bucket metadata using Direct Connectivity network path.     │ Success. │
        └────────────────────────────┴─────────────────────────────────────────────────────────────────────────┴──────────┘
    

## Check network configurations

If you encounter an `Unable to connect to Traffic Director` error while checking for direct connectivity using the Google Cloud CLI, use the following instructions to ensure that your network configurations allow traffic to pass from your VMs to the required endpoints.

Direct connectivity requires a service hosted at `directpath-pa.googleapis.com:443` and at `storage.googleapis.com:443`. To check whether a connection can be made to the service, make a curl call to `directpath-pa.googleapis.com:443` or `storage.googleapis.com:443`. For example:
    
    
    curl directpath-pa.googleapis.com:443
    

If a connection can be made, you receive an empty response without errors:
    
    
    curl: (52) Empty reply from server
    

If a connection cannot be made, you receive an error similar to the following:
    
    
    curl: (56) Recv failure: Connection reset by peer
    

## Limitations

Direct connectivity doesn't support Private Service Connect.

## Troubleshooting

This section provides details and solutions for errors that can occur when using gRPC direct connectivity.

### Too many open files

**Issue** : When using gRPC direct connectivity, your application might maintain a higher number of simultaneous connections to Cloud Storage than REST APIs. In environments with high parallelism, this can exceed the operating system's file descriptor limit, resulting in a `too many open files` error. This error might occur when you're using the Google Cloud CLI.

**Solution** : To resolve this issue, choose one of the following methods:

  * Set the maximum number of open files for your process by using `ulimit -n $(ulimit -Hn)`.

  * Decrease the number of simultaneous tasks allowed by using the `gcloud config set` command with the `storage/process_count` and `storage/thread_count` properties. We recommend a maximum value of 12 tasks. For details, see the [`gcloud config set` reference](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). Note that decreasing the number of simultaneous tasks allowed reduces parallelism and might impact performance.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
