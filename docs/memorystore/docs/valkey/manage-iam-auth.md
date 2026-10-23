---
url: https://docs.cloud.google.com/memorystore/docs/valkey/manage-iam-auth/
title: Manage IAM authentication \u00a0|\u00a0 Memorystore for Valkey \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:45:58.707910+00:00
---

# Manage IAM authentication  |  Memorystore for Valkey  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/valkey/manage-iam-auth/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Valkey ](https://docs.cloud.google.com/memorystore/docs/valkey)
  * [ Guides ](https://docs.cloud.google.com/memorystore/docs/valkey/product-overview)



Send feedback 

#  Manage IAM authentication Stay organized with collections  Save and categorize content based on your preferences. 

This page provides instructions on common tasks for the IAM authentication feature for Memorystore for Valkey. For more details on the feature, see [About IAM authentication](https://docs.cloud.google.com/memorystore/docs/valkey/about-iam-auth).

## Create an instance with IAM authentication

To create a Memorystore for Valkey instance that uses IAM authentication, run the `create` command:
    
    
    gcloud memorystore instances create INSTANCE_ID --region=REGION_ID --network=NETWORK --node-type=NODE_TYPE --shard-count=SHARD_COUNT --authorization-mode=iam-auth
    

Replace the following:

  * INSTANCE_ID is the ID of the Memorystore for Valkey instance you're creating. Your instance ID must be 1 to 63 characters and use only lowercase letters, numbers, or hyphens. It must start with a lowercase letter and end with a lowercase letter or number.

  * REGION_ID is the region where you want the instance placed.

  * NETWORK is the network used to create your instance. It must use the format: `projects/NETWORK_PROJECT_ID/global/networks/NETWORK_ID`. The network ID used here must match the network ID used by the service connection policy. Otherwise, the `create` operation fails. For more details, see [Networking](https://docs.cloud.google.com/memorystore/docs/valkey/networking).

  * NODE_TYPE is the [node type](https://docs.cloud.google.com/memorystore/docs/valkey/instance-node-specification#choose-node-type) for the instance.

**Caution** : We recommend that you use the `shared-core-nano` node type only for development or testing purposes because this node type has no SLA. If you run Memorystore for Valkey in a production environment, then we recommend using another node type.
  * SHARD_COUNT determines the number of shards in your instance. Shard count determines the total memory capacity for storing instance data. To see more details about instance specification, see [Instance and node specification](https://docs.cloud.google.com/memorystore/docs/valkey/instance-node-specification).




## Grant permissions for IAM authentication

To grant an IAM access, grant the principal the `roles/memorystore.dbConnectionUser` role using the [Grant IAM role instructions](https://docs.cloud.google.com/iam/docs/grant-role-console#grant_an_iam_role).

By default, granting a principal the `roles/memorystore.dbConnectionUser` role allows the principal to access all instances in your project.

**Note:** For instructions on limiting user access on a per-instance basis, see [Grant access to a group of resources based on resource name prefixes](https://docs.cloud.google.com/iam/docs/configuring-resource-based-access#resource-name-instance). When granting limited access for your instance, use the `resource.name` attribute and the following format for the instance name - `projects/PROJECT/locations/REGION/instances/INSTANCE_NAME`.

### Create a limited IAM Admin role for an instance

You might want to create a role that can modify instance connection IAM permissions without granting full IAM administrator access. This can be done by creating a limited IAM administrator for the `roles/memorystore.dbConnectionUser` role. For more details, visit [Create limited IAM admins](https://docs.cloud.google.com/iam/docs/setting-limits-on-granting-roles#limited-admins-example).

## Connect to an instance that uses IAM authentication

  1. If you don't already have a Compute Engine VM that uses the same authorized network as your Valkey instance, create one and connect to it by following [Quickstart Using a Linux VM](https://docs.cloud.google.com/compute/docs/create-linux-vm-instance).

  2. For your project, enable the Cloud Platform API scope. For more information about enabling this access scope, see [Attach the service account and update the access scope](https://docs.cloud.google.com/compute/docs/instances/change-service-account#changeserviceaccountandscopes). For more information about best practices for this scope, see [Scopes best practice](https://docs.cloud.google.com/compute/docs/access/service-accounts#scopes_best_practice).

  3. For your project, enable the Memorystore for Valkey API. 

[Memorystore for Valkey API](https://console.cloud.google.com/apis/library/memorystore.googleapis.com)

  4. Install `valkey-cli` on the Compute Engine VM by following the instructions at [Install Valkey](https://valkey.io/topics/installation/).

  5. Run the following command to retrieve an access token for your IAM user:
         
         gcloud auth print-access-token
         

Access tokens expire in one hour. For more information, see [IAM access token timeframe](https://docs.cloud.google.com/memorystore/docs/valkey/about-iam-auth#iam_access_token_time_frame).

  6. Connect to your instance's discovery endpoint:
         
         valkey-cli -h NETWORK_ADDRESS -p PORT -a ACCESS_TOKEN -c
         

Replace the following:

     * NETWORK_ADDRESS: the instance's network address. To view the network address, see [View instance information](https://docs.cloud.google.com/memorystore/docs/valkey/view-instance-information).

     * PORT: the instance's port number. To view the port number, see [View instance information](https://docs.cloud.google.com/memorystore/docs/valkey/view-instance-information).

     * ACCESS_TOKEN: the access token that you retrieved in the previous step.

If you specify a username, then you must use either the `default` username or the IAM principal email address. Also, authenticated connections remain valid after the token expires. For more information, see [IAM access token timeframe](https://docs.cloud.google.com/memorystore/docs/valkey/about-iam-auth#iam_access_token_time_frame).

If you enable in-transit encryption on the instance, then you must append the Transport Layer Security (TLS) flags. For example:
    
    valkey-cli -h NETWORK_ADDRESS -p PORT -a ACCESS_TOKEN -c --tls --cacert /tmp/server_ca.pem
    

**Important** : If you have a Cluster Mode Disabled instance, then don't use the `-c` flag.
  7. Optional: If you have a Cluster Mode Enabled instance, then run the `CLUSTER SHARDS` command to view your node topology. Note one of the node's IP addresses and port numbers.

If you have a Cluster Mode Disabled instance, then you can skip this step.

  8. To use `valkey-cli` to authenticate and connect to your node, use the following command:
         
         valkey-cli -h NODE_IP_ADDRESS -p NODE_PORT -a ACCESS_TOKEN -c
         

Replace the following:

     * NODE_IP_ADDRESS: the node's IP address that you noted in the previous step
     * NODE_PORT: the node's port number that you noted in the previous step
     * ACCESS_TOKEN: the IAM access token that you retrieved earlier in this procedure
  9. To verify that you have an authenticated connection to your node, run a Valkey `SET` and `GET` command.

  10. [Delete the Compute Engine VM](https://docs.cloud.google.com/compute/docs/create-linux-vm-instance#clean-up) that you used to connect to the instance. This helps you avoid incurring charges to your Cloud Billing account.




## Automate access token retrieval

We strongly recommend that you automate access token retrieval in your application. Because of the short lifetime of an access token, it's difficult to hardcode the token.

  1. **(Optional)** If you haven't already, create a service account for your application (see [Creating and managing a service account](https://docs.cloud.google.com/iam/docs/creating-managing-service-accounts)).
         
         gcloud iam service-accounts create SA_NAME \
             --description="DESCRIPTION" \
             --display-name="DISPLAY_NAME"
         

Replace the following:

     * SA_NAME is the name of the service account.
     * DESCRIPTION is an optional description of the service account.
     * DISPLAY_NAME is a service account name to display in the Google Cloud console.
  2. Grant your service account the `memorystore.dbConnectionUser` role on your project.
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
         --member="serviceAccount:SA_NAME@PROJECT_ID.iam.gserviceaccount.com" \
         --role=roles/"ROLE_NAME"
         

Replace the following:

     * PROJECT_ID: the project ID.
     * SA_NAME: the name of the service account.
     * ROLE_NAME: a role name. For this example: `memorystore.dbConnectionUser`.
  3. Authenticate your application as the given service account. See [service accounts](https://docs.cloud.google.com/docs/authentication#service-accounts) for more information.

For code samples that show how you can authenticate your application using popular client libraries, see [Client library code samples](https://docs.cloud.google.com/memorystore/docs/valkey/client-library-code-samples).




## Code sample to connect to an instance that uses IAM authentication

To view a Valkey-compatible code sample on how to set up a client library to connect to an instance that uses IAM authentication, see [Code sample for both IAM authentication and in-transit encryption](https://docs.cloud.google.com/memorystore/docs/valkey/client-library-code-samples#iam_auth_and_in_transit_encryption).

## Troubleshoot error messages with IAM authentication

Error message | Recommended action | Description  
---|---|---  
` -WRONGPASS invalid username-password pair or user is disabled ` | Verify the access token provided to the Memorystore for Valkey server and ensure that the matching ACL user is enabled. | The IAM principal lacks the required permissions, the access token that you provided is invalid, or the matching ACL user is disabled. Verify that the access token isn't expired and that you retrieved the token by following the instructions in [Connect to an instance that uses IAM authentication](https://docs.cloud.google.com/memorystore/docs/valkey/manage-iam-auth#connect_to_an_instance_that_uses_iam_authentication). If you recently changed the IAM permissions, then the permissions might take a few minutes to propagate.  
` -NOAUTH Authentication required ` | Check that the application is configured to provide an IAM access token to the Memorystore for Valkey server. | The application isn't providing an access token to the Memorystore for Valkey server. Verify that the application is configured to provide an access token and that you retrieved the access token by following the instructions in [Connect to an instance that uses IAM authentication](https://docs.cloud.google.com/memorystore/docs/valkey/manage-iam-auth#connect_to_an_instance_that_uses_iam_authentication).  
` -ERR (ERR_IAM_EXHAUSTED) Memorystore IAM authentication backend quota exceeded. ` | Retry with exponential backoff. | The IAM backend is overloaded and returned a quota exceeded error to the Memorystore for Valkey server.To prevent further connection failures, we recommend that applications retry this error with exponential backoff.  
` -ERR (ERR_IAM_OTHER) Memorystore IAM authentication backend error. ` | Verify the username or retry with exponential backoff. | This error occurs for the following reasons:

  * The username that you provided isn't valid. You can use the `default` username, omit the username, or use the IAM principal email address.
  * The IAM backend returned a transient error to the Memorystore for Valkey server.

If the username is valid, then we recommend that your application attempts to retry this error with exponential backoff to prevent further connection failures.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
