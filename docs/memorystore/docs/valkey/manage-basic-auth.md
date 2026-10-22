---
url: https://docs.cloud.google.com/memorystore/docs/valkey/manage-basic-auth/
title: Secure access to your instances by using basic token-based authentication \u00a0|\u00a0 Memorystore for Valkey \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:11:27.951172+00:00
---

# Secure access to your instances by using basic token-based authentication  |  Memorystore for Valkey  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/valkey/manage-basic-auth/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Valkey ](https://docs.cloud.google.com/memorystore/docs/valkey)
  * [ Guides ](https://docs.cloud.google.com/memorystore/docs/valkey/product-overview)



Send feedback 

#  Secure access to your instances by using basic token-based authentication Stay organized with collections  Save and categorize content based on your preferences. 

In addition to [Identity and Access Management (IAM) authentication](https://docs.cloud.google.com/memorystore/docs/valkey/about-iam-auth), you can use basic token-based authentication to secure access to your Memorystore for Valkey instances. As a lightweight solution, basic token-based authentication lets clients verify their identities within your applications by using their tokens.

Basic token-based authentication has minimal resource requirements and a low resource overhead. In addition, if your current workloads on either Memorystore for Redis or your on-premises applications already use basic token-based authentication, then this feature facilitates a smooth transition when you migrate to Memorystore for Valkey.

## Benefits

By using basic token-based authentication, you gain the following benefits:

  * **Flexibility** : for new and existing instances, enable authentication at any time. When you enable basic token-based authentication, your instances are secure. For all new connections, users must supply an authentication token to authenticate into your instances.
  * **Zero-downtime rotation** : rotate user tokens without causing downtime to your applications.
  * **Compatibility** : the `default` superuser maintains the same privileges that are granted to this user. Basic token-based authentication adds an extra layer of protection. This ensures backward compatibility when you migrate your workloads from Memorystore for Redis into Memorystore for Valkey.



## Authentication modes

Basic token-based authentication supports two primary authentication modes:

  * **Simple authentication** : a straightforward method where a user sends an authentication token to authenticate themselves as the `default` user
  * **Multi-user authentication** : manage multiple users to authenticate access to your instances



## Best practices

For security purposes, we recommend that you use the following best practices for basic token-based authentication:

  * **Rotate user tokens** : use a rotation policy for user tokens.
  * **Use Secret Manager** : don't hardcode a user's basic token-based authentication credentials in your application code. Instead, store them in [Secret Manager](https://docs.cloud.google.com/secret-manager/docs) and retrieve them at runtime.

Secret Manager provides a centralized, encrypted vault for user credentials, which eliminates secret sprawl and reduces the operational overhead of managing credentials manually. It enforces access controls by using IAM and generates audit logs automatically. This ensures compliance and prevents credential exposure.

  * **Combine basic token-based authentication with Transport Layer Security (TLS)** : when you use basic token-based authentication, we recommend that you enable [in-transit encryption](https://docs.cloud.google.com/memorystore/docs/valkey/about-in-transit-encryption). This ensures that usernames and authentication tokens aren't sent in plain text over the network.




## Before you begin

Before you begin to secure your instances by using basic token-based authentication, complete the prerequisites in this section.

### Verify client support for basic token-based authentication

To confirm that your client applications can support basic token-based authentication, ensure that the applications can use the `AUTH` command.

The `default` user authenticates to your client applications by using the following command:
    
    
    AUTH TOKEN
    

For this command, TOKEN is the default user's authentication token.

All other users authenticate by using the following command:
    
    
    AUTH USERNAME TOKEN
    

For this command, USERNAME and TOKEN are the user's username and authentication token.

For more information about the `AUTH` command, see [AUTH](https://valkey.io/commands/auth/) in the Valkey documentation.

### Use the Google Cloud console, Google Cloud CLI, and APIs

To use the Google Cloud console, gcloud CLI, and APIs, do the following:

  1. In the Google Cloud console, on the project selector page, select or [create a Google Cloud project](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects).

[Go to the project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  2. Make sure that billing is enabled for your project. Learn how to [check if billing is enabled on a project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled).
  3. [Install](https://docs.cloud.google.com/sdk/docs/install) and [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the Google Cloud CLI (gcloud CLI).

**Note:** If you installed the gcloud CLI, then make sure you have the latest version by running `gcloud components update`. To access the Memorystore for Valkey gcloud CLI commands, you need at least gcloud CLI version `489.0.0`.

  4. Enable the Memorystore for Valkey API.   
[Memorystore for Valkey API](https://console.cloud.google.com/apis/library/memorystore.googleapis.com)
  5. Enable the Network Connectivity API.   
[Network Connectivity API](https://console.cloud.google.com/apis/library/networkconnectivity.googleapis.com)
  6. Enable the Service Consumer Management API.   
[Service Consumer Management API](https://console.cloud.google.com/apis/library/serviceconsumermanagement.googleapis.com)



### Grant roles

To configure basic token-based authentication or view authentication tokens for your instances, you need the Memorystore Admin (`roles/memorystore.admin`) IAM role in your Google Cloud project. For more information about granting this role, see [Access control](https://docs.cloud.google.com/memorystore/docs/valkey/access-control).

## Manage basic token-based authentication for instances

Memorystore for Valkey supports the following actions to manage basic token-based authentication for instances:

  * Create an instance with basic token-based authentication
  * Enable basic token-based authentication for an instance
  * Create a basic token-based authentication user for an instance
  * List basic token-based authentication users for an instance
  * View information about a basic token-based authentication user
  * Delete a basic token based authentication user from an instance



### Create an instance with basic token-based authentication

By creating an instance with basic token-based authentication, you have a lightweight and widely supported method to restrict a user's access to the instance.

You can create the instance by using either the Google Cloud console or the [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud).

### Console

To create an instance and enable basic token-based authentication for it, see [Create instances](https://docs.cloud.google.com/memorystore/docs/valkey/create-instances).

**Important** : After you enable basic token-based authentication for the instance, the following conditions apply:

  * You can manage up to 1,000 local users.
  * You can't deactivate or change this authentication mode.
  * Memorystore for Valkey creates the `default` user and generates an authentication token for the user automatically.



### gcloud

To create an instance and enable basic token-based authentication for it, use the [`gcloud memorystore instances create`](https://docs.cloud.google.com/sdk/gcloud/reference/memorystore/instances/create) command.
    
    
    gcloud memorystore instances create INSTANCE_ID \
    --location=REGION \
    --authorization-mode=token-auth
    

Make the following replacements:

  * INSTANCE_ID: the ID of the instance that you want to create to use basic token-based authentication
  * REGION: the region where you want the instance to be located



**Important** : After you enable basic token-based authentication for the instance, the following conditions apply:

  * You can manage up to 1,000 local users.
  * You can't deactivate or change this authentication mode.
  * Memorystore for Valkey creates the `default` user and generates an authentication token for the user automatically.



### Enable basic token-based authentication for an instance

By enabling basic token-based authentication for an instance, you have a lightweight and widely supported method to restrict a user's access to the instance.

The `default` user can authenticate to the instance by using just their token. All other users authenticate by using a standard username and token. For more information, see Verify client support for basic token-based authentication.

Enabling basic token-based authentication might cause downtime for applications that try to create new connections because Memorystore for Valkey requires authenticated requests. Although existing connections remain unaffected, to utilize basic token-based authentication for any subsequent connection attempts to the instance, you must update your applications. For more information, see Connect to an instance by using basic token-based authentication.

You can enable basic token-based authentication for an instance by using either the Google Cloud console or the [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud).

### Console

  1. In the Google Cloud console, go to the **Memorystore for Valkey** page.

[Memorystore for Valkey](https://console.cloud.google.com/memorystore/valkey/instances)

  2. Click the instance for which you want to enable basic token-based authentication.

  3. On the **Instance at a glance** page, scroll to the **Security** card.

  4. Next to the **Auth Mode** field, click **Edit** (_edit_).

If either **IAM Auth** or **Token Auth** appear next to the field, then you already enabled IAM authentication or basic token-based authentication for the instance.

  5. In the **Auth Mode** dialog, select the **Token Auth** option, and then click **Update instance**.




**Important** : After you enable basic token-based authentication for the instance, the following conditions apply:

  * Memorystore for Valkey creates the `default` user and generates an authentication token for the user automatically.
  * Existing connections aren't impacted. However, new client connections require users to authenticate to access your applications.
  * You can manage up to 1,000 local users.
  * You can't deactivate or change this authentication mode.



### gcloud

To enable basic token-based authentication, use the [`gcloud memorystore instances update`](https://docs.cloud.google.com/sdk/gcloud/reference/memorystore/instances/update) command.
    
    
    gcloud memorystore instances update INSTANCE_ID \
    --location=REGION \
    --authorization-mode=token-auth
    

Make the following replacements:

  * INSTANCE_ID: the ID of the instance for which you want to enable basic token-based authentication
  * REGION: the region where the instance is located



**Important** : After you enable basic token-based authentication for the instance, the following conditions apply:

  * Memorystore for Valkey creates the `default` user and generates an authentication token for the user automatically.
  * Existing connections aren't impacted. However, new client connections require users to authenticate to access your applications.
  * You can manage up to 1,000 local users.
  * You can't deactivate or change this authentication mode.



### Create a basic token-based authentication user for an instance

By creating a basic token-based authentication user for an instance, you configure the instance to allow multi-user authentication. After the user logs in initially, this authentication mode acts as a secure and revocable credential for new connections. The user can continue to use the authentication token until either they delete it or the user is removed.

You can create a basic token-based authentication user by using either the Google Cloud console or the [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud).

### Console

  1. In the Google Cloud console, go to the **Memorystore for Valkey** page.

[Memorystore for Valkey](https://console.cloud.google.com/memorystore/valkey/instances)

  2. Click the instance for which you want to create a basic token-based authentication user.

  3. In the navigation drawer, click the **Users** menu item.

If this menu item doesn't appear in the drawer, then you haven't created an instance with basic authentication or enabled basic token-based authentication for the instance.

  4. On the **Users** page, click **Add user**.

  5. In the **Add user** dialog, enter an ID for the user, and then click **Add**.




**Important** : You can't delete the `default` user. When you either create an instance with basic token-based authentication or enable basic token-based authentication for the instance, Memorystore for Valkey creates this user automatically.

When a basic token-based authentication user (including the `default` user) is created, Memorystore for Valkey creates an authentication token for the user automatically.

### gcloud

To create the user, use the [`gcloud memorystore instances create-token-auth-user`](https://docs.cloud.google.com/sdk/gcloud/reference/memorystore/instances/create-token-auth-user) command.
    
    
    gcloud memorystore instances create-token-auth-user INSTANCE_ID \
    --location=REGION \
    --token-auth-user=USERNAME
    

Make the following replacements:

  * INSTANCE_ID: the ID of the instance for which you want to create a basic token-based authentication user
  * REGION: the region where the instance is located
  * USERNAME: the username of the user



**Important** : You can't delete the `default` user. When you either create an instance with basic token-based authentication or enable basic token-based authentication for the instance, Memorystore for Valkey creates this user automatically.

When a basic token-based authentication user (including the `default` user) is created, Memorystore for Valkey creates an authentication token for the user automatically.

### List basic token-based authentication users for an instance

You can retrieve a list of basic token-based authentication users for an instance by using either the Google Cloud console or the [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud).

### Console

  1. In the Google Cloud console, go to the **Memorystore for Valkey** page.

[Memorystore for Valkey](https://console.cloud.google.com/memorystore/valkey/instances)

  2. Click the instance for which you want to retrieve a list of basic token-based authentication users.

  3. In the navigation drawer, click the **Users** menu item. On the **Users** page, a list of basic token-based authentication users is displayed.

If the **Users** menu item doesn't appear in the navigation drawer, then you haven't created an instance with basic authentication or enabled basic token-based authentication for the instance.




### gcloud

To list the users, use the [`gcloud memorystore instances token-auth-users list`](https://docs.cloud.google.com/sdk/gcloud/reference/memorystore/instances/token-auth-users/list) command.
    
    
    gcloud memorystore instances token-auth-users list \
    --instance=INSTANCE_ID \
    --location=REGION
    

Make the following replacements:

  * INSTANCE_ID: the ID of the instance for which you want to retrieve a list of basic token-based authentication users
  * REGION: the region where the instance is located



### View information about a basic token-based authentication user

You can view information about a basic token-based authentication user by using the [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud).

To view information about the user, use the [`gcloud memorystore instances token-auth-users describe`](https://docs.cloud.google.com/sdk/gcloud/reference/memorystore/instances/token-auth-users/describe) command.
    
    
    gcloud memorystore instances token-auth-users describe USERNAME \
    --instance=INSTANCE_ID \
    --location=REGION
    

Make the following replacements:

  * USERNAME: the username of the basic token-based authentication user about which you want to view information
  * INSTANCE_ID: the ID of the instance to which the user can authenticate
  * REGION: the region where the instance is located



### Delete a basic token based authentication user from an instance

By deleting a basic token-based authentication user from an instance, you revoke the user's access rights to the instance.

**Important** : You can't delete the `default` user from the instance.

You can delete a basic token-based authentication user from an instance by using either the Google Cloud console or the [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud).

### Console

  1. In the Google Cloud console, go to the **Memorystore for Valkey** page.

[Memorystore for Valkey](https://console.cloud.google.com/memorystore/valkey/instances)

  2. Click the instance from which you want to delete a basic token-based authentication user.

  3. In the navigation drawer, click the **Users** menu item.

If the menu item doesn't appear in the drawer, then you haven't created an instance with basic authentication or enabled basic token-based authentication for the instance.

  4. On the **Users** page, next to the ID of the user that you want to delete, click **Actions** (_more_vert_).

  5. From the menu that appears, select **Remove user**.

  6. In the **Delete user?** dialog, enter the ID of the user, and then click **Delete**. Memorystore for Valkey deletes the user and all authentication tokens that are associated with the user.

  7. Optional: For the user that you're deleting, Memorystore for Valkey doesn't end existing connections. To end these connections, run the following command on all nodes in the instance:
         
         CLIENT KILL USER USERNAME
         




### gcloud

To delete the user, use the [`gcloud memorystore instances token-auth-users delete`](https://docs.cloud.google.com/sdk/gcloud/reference/memorystore/instances/token-auth-users/delete) command.
    
    
    gcloud memorystore instances token-auth-users delete USERNAME \
    --instance=INSTANCE_ID \
    --location=REGION
    

Make the following replacements:

  * USERNAME: the username of the basic token-based authentication user
  * INSTANCE_ID: the ID of the instance from which you want to delete the user
  * REGION: the region where the instance is located



For the user that you're deleting, Memorystore for Valkey also deletes all authentication tokens that are associated with the user. Also, Memorystore for Valkey doesn't end existing connections. To end these connections, run the following command on all nodes in the instance:
    
    
    CLIENT KILL USER USERNAME
    

## Manage basic token-based authentication for users

Memorystore for Valkey supports the following actions to manage basic token-based authentication for users:

  * Create an authentication token for a user
  * List authentication tokens for a user
  * View information about authentication tokens for a user
  * Delete an authentication token from a user



### Create an authentication token for a user

When you create a basic token-based authentication user for an instance, Memorystore for Valkey creates an authentication token for the user automatically. However, you can create an additional authentication token for the user. By doing so, you can rotate the user's existing token without causing downtime to your applications.

**Important** : Users can have up to two authentication tokens. Having two tokens lets you rotate the user tokens for your applications with no downtime.

You can create an authentication token for a user by using either the Google Cloud console or the [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud).

### Console

  1. In the Google Cloud console, go to the **Memorystore for Valkey** page.

[Memorystore for Valkey](https://console.cloud.google.com/memorystore/valkey/instances)

  2. Click the instance that has a user for which you want to create an authentication token.

  3. In the navigation drawer, click the **Users** menu item.

If the menu item doesn't appear in the drawer, then you haven't created an instance with basic authentication or enabled basic token-based authentication for the instance.

  4. On the **Users** page, next to the ID of the user for which you want to create an authentication token, click **Actions** (_more_vert_).

  5. From the menu that appears, select **Add auth token**.

  6. In the **Add auth token** dialog, click **Add**.

If a user already has two authentication tokens, then before you can create another token for the user, you must delete an existing token.




### gcloud

To create the token, use the [`gcloud memorystore instances token-auth-users create-auth-token`](https://docs.cloud.google.com/sdk/gcloud/reference/memorystore/instances/token-auth-users/create-auth-token) command.
    
    
    gcloud memorystore instances token-auth-users create-auth-token USERNAME \
    --instance=INSTANCE_ID \
    --location=REGION
    

Make the following replacements:

  * USERNAME: the username of the user for which you want to create an authentication token
  * INSTANCE_ID: the ID of the instance that the user can access by using the token
  * REGION: the region where the instance is located



If a user already has two authentication tokens, then before you can create another token for the user, you must delete an existing token.

### List authentication tokens for a user

You can retrieve a list of authentication tokens for a user by using the [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud).

To list the tokens, use the [`gcloud memorystore instances token-auth-users auth-tokens list`](https://docs.cloud.google.com/sdk/gcloud/reference/memorystore/instances/token-auth-users/auth-tokens/list) command.
    
    
    gcloud memorystore instances token-auth-users auth-tokens list \
    --token-auth-user=USERNAME \
    --instance=INSTANCE_ID \
    --location=REGION
    

Make the following replacements:

  * USERNAME: the username of the user to which the authentication tokens belong
  * INSTANCE_ID: the ID of the instance that the user can access by using the authentication tokens
  * REGION: the region where the instance is located



### View information about authentication tokens for a user

You can view information about authentication tokens for a user by using either the Google Cloud console or the [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud).

### Console

  1. In the Google Cloud console, go to the **Memorystore for Valkey** page.

[Memorystore for Valkey](https://console.cloud.google.com/memorystore/valkey/instances)

  2. Click the instance that has a user's authentication tokens about which you want to view information.

  3. In the navigation drawer, click the **Users** menu item.

If the menu item doesn't appear in the drawer, then you haven't created an instance with basic authentication or enabled basic token-based authentication for the instance.

  4. On the **Users** page, next to the ID of the user, click **Actions** (_more_vert_).

  5. From the menu that appears, select **View auth tokens**. In the **Auth tokens** dialog, the following information is displayed:

     * The user's ID.
     * The number of authentication tokens that the user has (one or two).
     * The version of each authentication token, along with the date and time of when Memorystore for Valkey created each version. Every time you create an authentication token for a user, Memorystore for Valkey creates an incremental version of the token.
     * The authentication tokens.
  6. Optional: To obtain a user's authentication token so that you can use it to connect to an instance, click **Copy** (_content_copy_) next to a token, and then paste the token into a text editor.

  7. Click **Done**.




### gcloud

To view the information, use the [`gcloud memorystore instances token-auth-users auth-tokens describe`](https://docs.cloud.google.com/sdk/gcloud/reference/memorystore/instances/token-auth-users/auth-tokens/describe) command.
    
    
    gcloud memorystore instances token-auth-users auth-tokens describe AUTH_TOKEN \
    --instance=INSTANCE_ID \
    --location=REGION \
    --token-auth-user=USERNAME
    

Make the following replacements:

  * AUTH_TOKEN: the name of the authentication token about which you want to view information
  * INSTANCE_ID: the ID of the instance that the user can access by using the token
  * REGION: the region where the instance is located
  * USERNAME: the username of the user to which the authentication token belongs



### Delete an authentication token from a user

Deleting an authentication token from a user is a critical security action that invalidates the token.

**Important** : If this is the only authentication token for the user, then you can't delete it. If you want to rotate the token, then you must create an additional token for the user before you can delete the original token.

You can delete an authentication token from a user by using either the Google Cloud console or the [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud).

### Console

  1. In the Google Cloud console, go to the **Memorystore for Valkey** page.

[Memorystore for Valkey](https://console.cloud.google.com/memorystore/valkey/instances)

  2. Click the instance that has a user from which you want to delete an authentication token.

  3. In the navigation drawer, click the **Users** menu item.

If the menu item doesn't appear in the drawer, then you haven't created an instance with basic authentication or enabled basic token-based authentication for the instance.

  4. On the **Users** page, next to the ID of the user from which you want to delete an authentication token, click **Actions** (_more_vert_).

  5. From the menu that appears, select **Delete auth token**.

  6. In the **Delete Auth Token?** dialog, do the following:

     1. From the **Auth token** menu, select the authentication token that you want to delete.
     2. In the **Auth token ID** field, enter the version number of the token (for example, `version-1`).
     3. Click **Delete**.



### gcloud

To delete the token, use the [`gcloud memorystore instances token-auth-users auth-tokens delete`](https://docs.cloud.google.com/sdk/gcloud/reference/memorystore/instances/token-auth-users/auth-tokens/delete) command.
    
    
    gcloud memorystore instances token-auth-users auth-tokens delete AUTH_TOKEN \
    --instance=INSTANCE_ID \
    --location=REGION \
    --token-auth-user=USERNAME
    

Make the following replacements:

  * AUTH_TOKEN: the name of the authentication token that you want to delete from the user
  * INSTANCE_ID: the ID of the instance that you want to prevent the user from accessing by deleting the token
  * REGION: the region where the instance is located
  * USERNAME: the username of the user that has a token that you want to delete



## Connect to an instance by using basic token-based authentication

You can use the following methods to connect to an instance by using basic token-based authentication:

  * **Uniform Resource Identifier (URI) string** : this single, formatted string is used for convenience because all necessary connection information (for example, the user's username and authentication token, and the instance's IP address and hostname) is contained in one string.
  * **Flags** : this method is better suited for individual command-line tool usage, scripting, or environments where the configuration is broken down into separate environment variables by using multiple, separate arguments.



In the following sections, each connection method is explained.

### Use a URI string

To connect from a Compute Engine VM or a [supported environment](https://docs.cloud.google.com/memorystore/docs/valkey/supported-environments) by using a URI string, use the following command:
    
    
    valkey-cli -u
    redis://USERNAME:TOKEN@IP_ADDRESS:PORT
    

Make the following replacements:

  * USERNAME: the username of the user that's attempting to connect to the instance.
  * TOKEN: the user's authentication token.

If you provide an incorrect or invalid token, then you can't connect to the instance. Memorystore for Valkey creates an entry for this action in the Data Access audit log. You can view the log to detect security threats or troubleshoot connection issues that are caused by an expired or improperly formatted token. For more information about viewing the Data Access audit log, see [View logs](https://docs.cloud.google.com/memorystore/docs/valkey/audit-logging#viewing_logs).

  * IP_ADDRESS: the IP address of the instance.

  * PORT: the port number that's reserved for the instance.




If you enable in-transit encryption on the instance, then you must use the secure protocol (`rediss://`) and append the TLS flags. For example:
    
    
    valkey-cli -u
    rediss://USERNAME:TOKEN@IP_ADDRESS:PORT --tls --cacert /tmp/server_ca.pem
    

### Use flags

To connect from a Compute Engine VM or a [supported environment](https://docs.cloud.google.com/memorystore/docs/valkey/supported-environments) by using flags, use the following command:
    
    
    valkey-cli --user USERNAME -a TOKEN -h IP_ADDRESS -p PORT
    

Make the following replacements:

  * USERNAME: the username of the user that's attempting to connect to the instance.
  * TOKEN: the user's authentication token.

If you provide an incorrect or invalid token, then you can't connect to the instance. Memorystore for Valkey creates an entry for this action in the Data Access audit log. You can view the log to detect security threats or troubleshoot connection issues that are caused by an expired or improperly formatted token. For more information about viewing the Data Access audit log, see [View logs](https://docs.cloud.google.com/memorystore/docs/valkey/audit-logging#viewing_logs).

  * IP_ADDRESS: the IP address of the instance.

  * PORT: the port number that's reserved for the instance.




If you enable in-transit encryption on the instance, then you must append the TLS flags. For example:
    
    
    valkey-cli --user USERNAME -a TOKEN -h IP_ADDRESS -p PORT --tls --cacert /tmp/server_ca.pem
    

## Rotate a user's authentication token with zero downtime

To rotate a user's authentication token without causing downtime to your applications, do the following:

  1. **Create an additional authentication token for the user**: Memorystore for Valkey generates a second, valid token. Both tokens are valid.
  2. **Update your applications** : update your applications to use the new token.
  3. **Delete the authentication token for the user**: Memorystore for Valkey removes the first token. The user can use only the second token to authenticate into your applications.



## Access logs for basic token-based authentication

Memorystore for Valkey generates Admin Activity and Data Access audit logs for operations that are associated with authentication tokens and users. For more information about these audit logs, see [Monitor access using audit logs](https://docs.cloud.google.com/memorystore/docs/valkey/audit-logging).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
