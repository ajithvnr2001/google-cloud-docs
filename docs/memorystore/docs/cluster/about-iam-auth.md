---
url: https://docs.cloud.google.com/memorystore/docs/cluster/about-iam-auth/
title: About IAM authentication \u00a0|\u00a0 Memorystore for Redis Cluster \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:12:26.915008+00:00
---

# About IAM authentication  |  Memorystore for Redis Cluster  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/cluster/about-iam-auth/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Redis Cluster ](https://docs.cloud.google.com/memorystore/docs/cluster)
  * [ Guides ](https://docs.cloud.google.com/memorystore/docs/cluster/memorystore-for-redis-cluster-overview)



Send feedback 

#  About IAM authentication Stay organized with collections  Save and categorize content based on your preferences. 

Memorystore provides the Identity and Access Management (IAM) authentication feature that leverages IAM to help you better manage login access for users and service accounts. IAM-based authentication integrates with Redis AUTH, letting you seamlessly rotate credentials (IAM tokens) without relying on static passwords.

For instructions on setting up IAM authentication for your Memorystore cluster, see [Manage IAM authentication](https://docs.cloud.google.com/memorystore/docs/cluster/manage-iam-auth).

## IAM authentication for Redis

When using IAM authentication, permission to access a Memorystore cluster isn't granted directly to the end user. Instead, permissions are grouped into roles, and roles are granted to principals. For more information, see the [IAM overview](https://docs.cloud.google.com/iam/docs/overview).

**Note:** Memorystore lets you restrict access to a cluster by granting the **roles/redis.dbConnectionUser** role the users you choose. For information about limiting user access on a per-cluster basis, see [Grant access to a group of resources based on resource name prefixes](https://docs.cloud.google.com/iam/docs/configuring-resource-based-access#resource-name-instance). For more information about granting permissions for IAM authentication, see [Grant permissions for IAM authentication](https://docs.cloud.google.com/memorystore/docs/cluster/manage-iam-auth#grant_permissions_for_iam_authentication).

Administrators who authenticate with IAM can use Memorystore IAM authentication to centrally manage access control to their instances using IAM policies. IAM policies involve the following entities:

  * _Principals_. In Memorystore, you can use two types of principals: A user account, and a service account (for applications). Other principal types, such as Google groups, Google Workspace domains, or Cloud Identity domains are not yet supported for IAM authentication. For more information, see [Concepts related to identity](https://docs.cloud.google.com/iam/docs/overview#concepts_related_identity).

  * _Roles_. For Memorystore IAM authentication, a user requires the **redis.clusters.connect** permission to authenticate with a cluster. To get this permission, you can bind the user or service account to the predefined Redis Cluster DB Connection User (**roles/redis.dbConnectionUser**) role. For more information about IAM roles, see [Roles](https://docs.cloud.google.com/iam/docs/overview#roles).

  * _Resources_. The resources that principals access are Memorystore clusters. By default, IAM policy bindings are applied at the project-level, such that principals receive role permissions for all Memorystore instances in the project. However, IAM policy bindings can be restricted to a particular cluster. For instructions, see [Manage permissions for IAM authentication](https://docs.cloud.google.com/memorystore/docs/cluster/manage-iam-auth#manage_permissions_for_iam_authentication).




## Redis AUTH command

The IAM authentication feature uses the Redis AUTH command to integrate with IAM, allowing clients to provide an IAM access token that will be verified by the Memorystore cluster before allowing access to data.

Like every command, the AUTH command is sent unencrypted unless [In Transit Encryption](https://docs.cloud.google.com/memorystore/docs/cluster/about-in-transit-encryption) is enabled.

For an example of what the AUTH command can look like, see [Connecting to a Redis cluster that uses IAM authentication](https://docs.cloud.google.com/memorystore/docs/cluster/manage-iam-auth#connect_to_a_cluster_that_uses_iam_authentication).

### IAM access token time frame

By default, the IAM access token that you retrieve as a part of authentication expires one hour after it's retrieved. Alternatively, when you [generate the access token](https://docs.cloud.google.com/iam/docs/create-short-lived-credentials-direct#create-access), you can extend the token's expiration time for up to 12 hours.

When you establish a new Redis connection, you must present a valid access token by using the `AUTH` command. If the token expires, then you must get a new token to establish new connections. However, if you already authenticated an existing connection, then it continues to work, even if the token expires.

**Note:** We strongly recommend that you [automate access token retrieval](https://docs.cloud.google.com/memorystore/docs/cluster/manage-iam-auth#automate_access_token_retrieval) in your application. You can't hardcode an access token because of its short lifetime.

**Caution** : Google authentication libraries cache access tokens internally. If your application also caches tokens or refreshes them on a fixed schedule, then the authentication library might return an existing token with a short remaining lifespan.

If your application caches this token and attempts to use it after it expires, then new connection handshakes fail with IAM authorization denials.

To avoid authentication failures, see Best practices to avoid token double-caching.

### End an authenticated connection

If you want to end the connection, then use the Redis `CLIENT KILL` command. To find the connection that you want to end, first run `CLIENT LIST`, which returns client connections in order of age. You can then run `CLIENT KILL` to end the connection.

### Enable IAM authentication

Enabling IAM authentication doesn't degrade steady state performance. However, it does affect the rate that you can establish a connection.

Enabling IAM authentication throttles the rate of client connections that are established every second. This is because Google Cloud's IAM authentication must authenticate each new connection. In steady state, an application enables connection pools so this impact is negligible. However, when client applications are refreshed through deployments or bounce processing, there might be an influx of connections established again. If you update your clients gradually and you implement exponential backoffs, then you can absorb this reduced rate.

To view a code sample of how to use IAM authentication, see [IAM authentication and in-transit encryption code sample](https://docs.cloud.google.com/memorystore/docs/cluster/client-library-connection#iam-auth-in-transit-encryption).

## Best practices to avoid token double-caching

To avoid authentication failures caused by token double-caching, follow these best practices:

  * **Fetch tokens on demand** : Use dynamic credential providers or callbacks provided by your client library (such as redis-py, Lettuce, or Jedis) to fetch tokens on demand for new connections.
  * **Inspect expiration timestamps** : If you use a custom refresh schedule, inspect the token's actual expiration timestamp or adjust the auth library's eager-refresh threshold.



## Security and privacy

IAM authentication helps you ensure that your Redis cluster is only accessible by authorized IAM principals. TLS encryption is not provided unless [In Transit Encryption](https://docs.cloud.google.com/memorystore/docs/cluster/about-in-transit-encryption) enabled. For this reason, it is recommended that In Transit Encryption be turned on when using IAM authentication.

## Connect with a Compute Engine VM

If you are using a Compute Engine VM to [Connect to an instance that uses IAM authentication](https://docs.cloud.google.com/memorystore/docs/cluster/manage-iam-auth#connect_to_an_instance_that_uses_iam_authentication) you must enable the following access scopes and APIs for your project:

  * **Cloud Platform API scope**. For instructions on enabling this scope, see [Attach the service account and update the access scope](https://docs.cloud.google.com/compute/docs/instances/change-service-account#changeserviceaccountandscopes). For a description of best practices for this access scope, see [Scopes best practice](https://docs.cloud.google.com/compute/docs/access/service-accounts#scopes_best_practice).

  * **Memorystore for Redis Cluster API**. For a link to enable the API, click the following button:   
[Memorystore for Redis Cluster](https://console.cloud.google.com/apis/library/redis.googleapis.com)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
