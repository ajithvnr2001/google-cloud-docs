---
url: https://docs.cloud.google.com/memorystore/docs/cluster/manage-iam-auth/
title: Manage IAM authentication \u00a0|\u00a0 Memorystore for Redis Cluster \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:26:24.991223+00:00
---

# Manage IAM authentication  |  Memorystore for Redis Cluster  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/cluster/manage-iam-auth/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Redis Cluster ](https://docs.cloud.google.com/memorystore/docs/cluster)
  * [ Guides ](https://docs.cloud.google.com/memorystore/docs/cluster/memorystore-for-redis-cluster-overview)



Send feedback 

#  Manage IAM authentication Stay organized with collections  Save and categorize content based on your preferences. 

This page provides instructions on common tasks for the IAM authentication feature for Memorystore for Redis Cluster. For more details on the feature, see [About IAM authentication](https://docs.cloud.google.com/memorystore/docs/cluster/about-iam-auth).

## Create an instance with IAM authentication

To create a Memorystore for Redis Cluster instance that uses IAM authentication, run the `create` command:
    
    
    gcloud redis clusters create INSTANCE_ID --region=REGION_ID --network=NETWORK --node-type=NODE_TYPE --shard-count=SHARD_COUNT --auth-mode=iam-auth
    

Replace the following:

  * INSTANCE_ID is the ID of the Memorystore for Redis Cluster instance you're creating. Your instance ID must be 1 to 63 characters and use only lowercase letters, numbers, or hyphens. It must start with a lowercase letter and end with a lowercase letter or number.

  * REGION_ID is the region where you want the instance placed.

**Note:** You can only create instances in the [supported regions](https://docs.cloud.google.com/memorystore/docs/cluster/locations) for Memorystore for Redis Cluster. Not all of the regions currently supported by Memorystore for Redis are available for Memorystore for Redis Cluster. The `gcloud redis regions list` commands shows supported regions for Memorystore for Redis, not Memorystore for Redis Cluster.
  * NETWORK is the network used to create your instance. It must use the format: `projects/NETWORK_PROJECT_ID/global/networks/NETWORK_ID`. The network ID used here must match the network ID used by the service connection policy. Otherwise, the `create` operation fails. For more details, see [Networking](https://docs.cloud.google.com/memorystore/docs/cluster/networking).

  * NODE_TYPE is the [node type](https://docs.cloud.google.com/memorystore/docs/cluster/cluster-node-specification#choose_a_node_type) for the cluster.

**Caution** : We recommend that you use the `redis-shared-core-nano` node type only for development or testing purposes because this node type has no SLA. If you run Memorystore for Redis Cluster in a production environment, then we recommend using another node type.
  * SHARD_COUNT determines the number of shards in your instance. Shard count determines the total memory capacity for storing cluster data. To see more details about cluster specification, see [Cluster and node specification](https://docs.cloud.google.com/memorystore/docs/cluster/cluster-node-specification).




## Grant permissions for IAM authentication

To grant IAM access, use the instructions in [Grant an IAM role](https://docs.cloud.google.com/iam/docs/grant-role-console#grant_an_iam_role) to grant the `roles/redis.dbConnectionUser` role to the principal. The _principal_ is an identity that you can grant access to resources in Google Cloud. For example, a principal can be a service account that can access your Google Cloud project.

By default, granting a principal the `roles/redis.dbConnectionUser` role allows the principal to access all instances in your project.

**Note:** For instructions on limiting user access on a per-instance basis, see [Grant access to a group of resources based on resource name prefixes](https://docs.cloud.google.com/iam/docs/configuring-resource-based-access#resource-name-instance). When granting limited access for your instance, use the `resource.name` attribute and the following format for the instance name - `projects/PROJECT/locations/REGION/clusters/INSTANCE_NAME`.

### Create a limited IAM admin role for an instance

You might want to create a role that can modify instance connection IAM permissions without granting full IAM admin access. This can be done by creating a limited IAM admin for the `roles/redis.dbConnectionUser` role. For more details, visit [Create limited IAM admins](https://docs.cloud.google.com/iam/docs/setting-limits-on-granting-roles#limited-admins-example).

## Connect to an instance that uses IAM authentication

  1. If you don't already have a Compute Engine VM that uses the same authorized network as your Redis cluster, create one and connect to it by following [Quickstart Using a Linux VM](https://docs.cloud.google.com/compute/docs/create-linux-vm-instance).

  2. For your project, use the [`gcloud compute instances set-service-account`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/set-service-account) command to set a service account and enable the Cloud Platform API scope for your Compute Engine VM.
         
         gcloud compute instances set-service-account VM_NAME \
         --service-account=SERVICE_ACCOUNT_EMAIL \
         --scopes=SCOPE
         

Make the following replacements:

     * VM_NAME: the name of your Compute Engine VM
     * SERVICE_ACCOUNT_EMAIL: the email address of your service account
     * SCOPE: the Cloud Platform API scope for the VM (`cloud-platform`)

For example, the following command assigns the `my-sa-123@my-project-123.iam.gserviceaccount.com` service account to a VM called `example-VM` and sets the access scope on that VM to the Cloud Platform API:
    
    gcloud compute instances set-service-account example-VM \
    --service-account=my-sa-123@my-project-123.iam.gserviceaccount.com \
    --scopes=cloud-platform
    

For more information about enabling this access scope, see [Attach the service account and update the access scope](https://docs.cloud.google.com/compute/docs/instances/change-service-account#gcloud_1). For more information about best practices for this scope, see [Scopes best practice](https://docs.cloud.google.com/compute/docs/access/service-accounts#scopes_best_practice).

  3. For your project, enable the Memorystore for Redis API. 

[Memorystore for Redis API](https://console.cloud.google.com/apis/library/redis.googleapis.com)

  4. Install `redis-cli` on the Compute Engine VM by running the following command from the Compute Engine SSH terminal:
         
         sudo apt-get install redis-tools
         

  5. Run the following command to retrieve an access token for your IAM user:
         
         gcloud auth print-access-token
         

Access tokens expire in one hour. For more information, see [IAM access token timeframe](https://docs.cloud.google.com/memorystore/docs/cluster/about-iam-auth#iam_access_token_time_frame).

  6. Connect to your instance's discovery endpoint:
         
         redis-cli -h NETWORK_ADDRESS -p PORT -a ACCESS_TOKEN -c
         

Replace the following:

     * NETWORK_ADDRESS: the instance's network address. To view the network address, see [View cluster information](https://docs.cloud.google.com/memorystore/docs/cluster/view-instance-information).

     * PORT: the instance's port number. To view the port number, see [View cluster information](https://docs.cloud.google.com/memorystore/docs/cluster/view-instance-information).

     * ACCESS_TOKEN: the access token that you retrieved in the previous step.

If you specify a username, then you must use either the `default` username or the IAM principal email address. Also, authenticated connections remain valid after the token expires. For more information, see [IAM access token timeframe](https://docs.cloud.google.com/memorystore/docs/cluster/about-iam-auth#iam_access_token_time_frame).

If you enable in-transit encryption on the cluster, then you must append the Transport Layer Security (TLS) flags. For example:
    
    redis-cli -h NETWORK_ADDRESS -p PORT -a ACCESS_TOKEN -c --tls --cacert /tmp/server_ca.pem
    

  7. Run the `CLUSTER SHARDS` command to view your cluster topology. Note one of the node's IP addresses and port numbers.

  8. To use `redis-cli` to authenticate and connect to your node, use the following command:
         
         redis-cli -h NODE_IP_ADDRESS -p NODE_PORT -a ACCESS_TOKEN -c
         

Replace the following:

     * NODE_IP_ADDRESS: the node's IP address that you noted in the previous step
     * NODE_PORT: the node's port number that you noted in the previous step
     * ACCESS_TOKEN: the IAM access token that you retrieved earlier in this procedure
  9. To verify that you have an authenticated connection to your node, run a Redis `SET` and `GET` command.

  10. [Delete the Compute Engine VM](https://docs.cloud.google.com/compute/docs/create-linux-vm-instance#clean-up) that you used to connect to the cluster. This helps you avoid incurring charges to your Cloud Billing account.




## Automate access token retrieval

**Note:** We strongly recommend that you automate access token retrieval in your application. Because of the short lifetime of an access token, it's difficult to hardcode the token.

For a code sample that shows how you can authenticate your application by using popular client libraries, see [IAM authentication client library code sample](https://docs.cloud.google.com/memorystore/docs/cluster/client-library-connection#iam_authentication_client_library_code_sample).

  1. **(Optional)** If you haven't already, create a service account for your application (see [Creating and managing a service account](https://docs.cloud.google.com/iam/docs/creating-managing-service-accounts)).
         
         gcloud iam service-accounts create SA_NAME \
             --description="DESCRIPTION" \
             --display-name="DISPLAY_NAME"
         

Replace the following:

     * SA_NAME is the name of the service account.
     * DESCRIPTION is an optional description of the service account.
     * DISPLAY_NAME is a service account name to display in the Google Cloud console.
  2. Grant your service account the `redis.dbConnectionUser` role on your project.
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
         --member="serviceAccount:SA_NAME@PROJECT_ID.iam.gserviceaccount.com" \
         --role=roles/"ROLE_NAME"
         

Replace the following:

     * PROJECT_ID: the project ID.
     * SA_NAME: the name of the service account.
     * ROLE_NAME: a role name. For this example: `redis.dbConnectionUser`.
  3. Authenticate your application as the given service account. For more information, see [Service accounts](https://docs.cloud.google.com/docs/authentication#service-accounts).




## Code sample for connecting to an instance that uses IAM authentication

You can view a [code sample](https://docs.cloud.google.com/memorystore/docs/cluster/client-library-connection#iam_authentication_client_library_code_sample) that shows you how you can authenticate your application by using popular client libraries. In addition, you can see how to use this code sample to connect to an instance that uses IAM authentication.

## Troubleshooting error messages with IAM authentication

Error message | Recommended action | Description  
---|---|---  
` -WRONGPASS invalid username-password pair or user is disabled ` | Verify the access token provided to the Memorystore for Redis Cluster server and ensure that the matching ACL user is enabled. | The IAM principal lacks the required permissions, the access token that you provided is invalid, or the matching ACL user is disabled. Verify that the access token isn't expired and that you retrieved the token by following the instructions in [Connect to an instance that uses IAM authentication](https://docs.cloud.google.com/memorystore/docs/cluster/manage-iam-auth#connect_to_an_instance_that_uses_iam_authentication). If you recently changed the IAM permissions, then the permissions might take a few minutes to propagate.  
` -NOAUTH Authentication required ` | Check that the application is configured to provide an IAM access token to the Memorystore for Redis Cluster server. | The application isn't providing an access token to the Memorystore for Redis Cluster server. Verify that the application is configured to provide an access token and that you retrieved the access token by following the instructions in [Connect to an instance that uses IAM authentication](https://docs.cloud.google.com/memorystore/docs/cluster/manage-iam-auth#connect_to_an_instance_that_uses_iam_authentication).  
` -ERR (ERR_IAM_EXHAUSTED) Memorystore IAM authentication backend quota exceeded. ` | Retry with exponential backoff. | The IAM backend is overloaded and returned a quota exceeded error to the Memorystore for Redis Cluster server.To prevent further connection failures, we recommend that applications retry this error with exponential backoff.  
` -ERR (ERR_IAM_OTHER) Memorystore IAM authentication backend error. ` | Verify the username or retry with exponential backoff. | This error occurs for the following reasons:

  * The username that you provided isn't valid. You can use the `default` username, omit the username, or use the IAM principal email address.
  * The IAM backend returned a transient error to the Memorystore for Redis Cluster server.

If the username is valid, then we recommend that your application attempts to retry this error with exponential backoff to prevent further connection failures.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
