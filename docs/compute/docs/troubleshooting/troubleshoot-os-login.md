---
url: https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshoot-os-login/
title: Troubleshooting OS Login \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:09:27.665386+00:00
---

# Troubleshooting OS Login  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshoot-os-login/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Troubleshooting OS Login Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to troubleshoot OS Login using the metadata server. For information about setting up OS Login or for step-by-step instructions, see [Setting up OS Login](https://docs.cloud.google.com/compute/docs/instances/managing-instance-access).

You can query the metadata server from within a Compute Engine instance. For more information, see [Storing and retrieving instance metadata](https://docs.cloud.google.com/compute/docs/storing-retrieving-metadata).

## Before you begin

  * If you haven't already, set up [authentication](https://docs.cloud.google.com/compute/docs/authentication). Authentication verifies your identity for access to Google Cloud services and APIs. To run code or samples from a local development environment, you can authenticate to Compute Engine by selecting one of the following options: 

Select the tab for how you plan to use the samples on this page:

### Console

When you use the Google Cloud console to access Google Cloud services and APIs, you don't need to set up authentication. 

### gcloud

    1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. After installation, [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the Google Cloud CLI by running the following command: 
           
           gcloud init

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
    2. [ Set a default region and zone](https://docs.cloud.google.com/compute/docs/gcloud-compute#set_default_zone_and_region_in_your_local_client).

### REST

To use the REST API samples on this page in a local development environment, you use the credentials you provide to the gcloud CLI. 

[Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

For more information, see [Authenticate for using REST](https://docs.cloud.google.com/docs/authentication/rest) in the Google Cloud authentication documentation. 




## Common error messages

The following are examples of common errors you might encounter when you use OS Login.

### Cannot find name for group

On some compute instances that use OS Login, you might receive the following error message after the connection is established:
    
    
    /usr/bin/id: cannot find name for group ID 123456789

Ignore this error message. This error doesn't affect your compute instances.

### Failure getting groups

You might see logs similar to the following when you create compute instances:
    
    
    Dec 10 22:31:05 instance-1 google_oslogin_nss_cache[381]: oslogin_cache_refresh[381]: Refreshing group entry cache
    Dec 10 22:31:05 instance-1 google_oslogin_nss_cache[381]: oslogin_cache_refresh[381]: Failure getting groups, quitting
    

These logs indicate that your organization doesn't have OS Login Linux groups configured. Ignore these messages.

### Failed precondition

You might see an error similar to the following when you connect to the compute instance using SSH:
    
    
    ERROR: (gcloud.compute.ssh) FAILED_PRECONDITION: The specified username or UID is not unique within given system ID.
    

This error occurs when OS Login attempts to generate a username that already exists within an organization. This is common when a user account is deleted and a new user with the same email address is created shortly after. After a user account is deleted, it takes up to 48 hours to remove the user's POSIX information.

To resolve this issue, do one of the following:

  * [Restore the deleted account](https://support.google.com/cloudidentity/answer/1397578).
  * Remove the account's [POSIX information](https://docs.cloud.google.com/compute/docs/oslogin/manage-oslogin-in-an-org#modify-users) before deleting the account.



### OS Login profile size limit exceeded

You might see one of the following errors when you connect to a Linux compute instance using SSH or use SCP to transfer files:
    
    
    ERROR: (gcloud.compute.ssh) FAILED_PRECONDITION: Login profile size exceeds 32 KiB. Delete profile values to make additional space.
    
    
    
    ERROR: (gcloud.compute.scp) INVALID_ARGUMENT: Login profile size exceeds 32 KiB. Delete profile values to make additional space.
    

**Note:** The error might start with either `FAILED_PRECONDITION` or `INVALID_ARGUMENT`.

OS Login stores user information, including SSH public keys, in a POSIX account that has a size limit of 32 KiB per user. If your OS Login profile exceeds this limit, or if you have more than 64 SSH keys in your profile, you can't add additional SSH keys to it, which prevents you from connecting to VMs using SSH.

**Caution:** Don't remove your OS Login profile (POSIX account) to reduce profile size. Removing and recreating your profile creates a new UID and might cause file permission issues on your VMs.

To resolve these errors, do the following:

  1. Check the size of your OS Login profile. To check your profile's size, export your profile to a temporary JSON file and check the file size by running the following command:
         
         gcloud compute os-login describe-profile --format="json" | wc
         

If the size is close to or exceeds 32 KiB, you must remove unused SSH keys.

  2. Review your OS Login profile to identify any unused SSH keys:
         
         gcloud compute os-login describe-profile
         

The output is similar to the following:
         
         name: '00000000000000'
         posixAccounts:
         ...
         sshPublicKeys:
          ...:
            fingerprint: ...
            key: |
              ssh-rsa AAAAB3NzaC1yc2...
            name: ...
          ...
         

  3. Remove any unused keys by using the [`gcloud compute os-login ssh-keys remove` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/os-login/ssh-keys/remove):
         
         gcloud compute os-login ssh-keys remove --key=KEY
         

Replace `KEY` with the fingerprint of the key or the complete SSH public key string.




Alternatively, to avoid generating new keys when connecting to VMs, you can do one of the following:

  * Reuse an existing key-pair by specifying the `--ssh-key-file` flag with the `gcloud compute ssh` command:
        
        gcloud compute ssh VM_NAME --ssh-key-file=PATH_TO_PRIVATE_KEY
        

  * If you frequently connect to VMs using SSH with the gcloud CLI CLI, create a default SSH key-pair named `google_compute_engine` in your `.ssh/` directory. The gcloud CLI command line uses this key-pair if it exists and doesn't generate a new one on each connection. To generate a default key-pair, run:
        
        ssh-keygen -t rsa -f ~/.ssh/google_compute_engine -C USERNAME -b 2048
        

Then add the public key to your OS Login profile:
        
        gcloud compute os-login ssh-keys add --key-file=~/.ssh/google_compute_engine.pub
        




#### Cloud Build

If you use Cloud Build and your service account's OS Login profile exceeds the 32 KiB limit, you might encounter SSH connection failures and see the following error message: `Login profile size exceeds 32 KiB...`. To resolve this issue, you can configure Cloud Build to [use user-specified service accounts](https://docs.cloud.google.com/build/docs/securing-builds/configure-user-specified-service-accounts) instead of the default Cloud Build service account.

To prevent this issue from occurring in the future, [add an expiry time for SSH keys](https://docs.cloud.google.com/compute/docs/connect/add-ssh-keys#os-login). Expired keys are automatically removed from your login profile 48 hours after they expire, or when you add a new key to your profile.

### HTTP response code: 429

You might see the following error when you attempt to connect to a compute instance using SSH:
    
    
    Failed to validate organization user USERNAME has login permission, got HTTP response code: 429
    

This issue is caused by the metadata server rate limit of 100 queries per second per compute instance. This limit can't be adjusted. To resolve this issue, wait a few seconds, then retry the connection.

To prevent this issue in the future, try the following:

  * Implement a retry mechanism in the application code. For more information, see: 
    * [Exponential Backoff](https://docs.cloud.google.com/memorystore/docs/redis/exponential-backoff)
    * [Retry Strategy](https://docs.cloud.google.com/storage/docs/retry-strategy)
  * Re-use existing SSH connections.
  * Send commands in batches to reduce SSH connections and OS Login metadata queries.



## Default OS Login metadata entries

Compute Engine defines a set of default metadata entries that serves OS Login information. Default metadata is always defined and set by the server. Default metadata keys are case sensitive.

The following table describes the entries you can query.

Relative to `http://metadata.google.internal/computeMetadata/v1/`  
---  
Metadata entry | Description  
`project/attributes/enable-oslogin` |  Checks if OS Login is enabled on the current Google Cloud project.   
`instance/attributes/enable-oslogin` |  Checks if OS Login is enabled on the current compute instance.   
`oslogin/users/` |  Retrieves profile information for OS Login users. You can pass query parameters such as `username`, `uid`, `pagesize` and `pagetoken`.   
`oslogin/authorize/` |  Retrieves login or administrative level permission settings for an OS Login user. To check a permission, you must specify the `policy` query parameter. The value of the policy parameter must be set to either `login` (to check for login permission) or `adminLogin` (to check for sudo access).   
  
## Checking if OS Login is configured

[Use the Google Cloud console or Google Cloud CLI to query metadata](https://docs.cloud.google.com/compute/docs/metadata/querying-metadata#console-gcloud) to determine if OS Login is enabled. OS Login is enabled when the `enable-oslogin` metadata key is set to `TRUE` in project or instance metadata. If both instance and project metadata are set, the value set in instance metadata takes precedence.

## Viewing OS Login users

To view the profile information for multiple users, you can specify the `pagesize` parameter. Replace the `pagesize` with the required numeric value.
    
    
    curl "http://metadata.google.internal/computeMetadata/v1/oslogin/users?pagesize=PAGE_SIZE" -H "Metadata-Flavor: Google"
    

The output might contain a page token, which can be used in subsequent calls to list more users.

For example, to set the `pagesize` to `1`, run the following command:
    
    
    curl "http://metadata.google.internal/computeMetadata/v1/oslogin/users?pagesize=1" -H "Metadata-Flavor: Google"
    

To obtain the next user, set the `pagesize` to `1` and the `pagetoken` to the page token from the previous command's output.
    
    
    curl "http://metadata.google.internal/computeMetadata/v1/oslogin/users?pagesize=1&pagetoken=PAGE_TOKEN" -H "Metadata-Flavor: Google"
    

On most distributions, you can also run the Unix command `getent passwd` to retrieve the password entries for organization users.

## Viewing a specific OS Login user

To view the profile information for a specific user on your compute instance, run the following command:
    
    
    curl "http://metadata.google.internal/computeMetadata/v1/oslogin/users?username=USERNAME" -H "Metadata-Flavor: Google"
    

Replace `USERNAME` with the username of the user that you want to query.

For example, you can perform a request to look up the user `user_example_com`. The following command and output show added formatting for improved readability.
    
    
    curl "http://metadata.google.internal/computeMetadata/v1/oslogin/users?username=user_example_com" -H "Metadata-Flavor: Google"

The output is similar to the following:
    
    
    {
        "loginProfiles": [{
            "name": "12345678912345",
            "posixAccounts": [{
                "primary": true,
                "username": "user_example_com",
                "uid": "123451",
                "gid": "123451",
                "homeDirectory": "/home/user_example_com",
                "operatingSystemType": "LINUX"
            }],
            "sshPublicKeys": {
                "204c4b4fb...": {
                    "key": "ssh-rsa AAAAB3Nz...",
                    "fingerprint": "204c4b4fb..."
                }
            }
        }]
    }

On most distributions, you can also run Unix commands such as `getent passwd username` or `getent passwd uid` to retrieve profile information.

To retrieve the SSH keys for a user, you can also run `/usr/bin/google_authorized_keys USERNAME`. If no keys are returned, the user might not have the required permissions to sign in to the compute instance.

## Checking login permissions

To view login and administrative level permissions, you must provide the `policy=login&email=LOGIN_NAME` query parameters.

  1. Query the user profile to get the value of the `name` field:
         
         curl "http://metadata.google.internal/computeMetadata/v1/oslogin/users?username=user_example_com" -H "Metadata-Flavor: Google"

  2. In the output, take note of the `name`.

  3. Run the following `login` command using the value of `name`:
         
         curl "http://metadata.google.internal/computeMetadata/v1/oslogin/authorize?policy=login&email=LOGIN_NAME" -H "Metadata-Flavor: Google"
         




For example, you can query the login permissions for the user `user_example_com` that was viewed in the previous section:
    
    
    curl "http://metadata.google.internal/computeMetadata/v1/oslogin/authorize?policy=login&email=12345678912345" -H "Metadata-Flavor: Google"

The command output indicates the user is authorized to sign in to the compute instance:
    
    
    {"success":true}

**Note:** If a user is granted the `roles/compute.osLogin` access role and the authorization output returns `{"success" : false}`, this indicates that the user might be missing the `roles/iam.serviceAccountUser` permission for the service account associated with the compute instance. For more information, see [Granting OS Login IAM roles ](https://docs.cloud.google.com/compute/docs/instances/managing-instance-access#grant-iam-roles).

## Checking if your compute instance has a service account

You can query the metadata server to find the service account associated with your compute instance. Sign in to your compute instance and run the following command:
    
    
    curl "http://metadata.google.internal/computeMetadata/v1/instance/service-accounts/" -H "Metadata-Flavor: Google"

The output is similar to the following:
    
    
    12345-sa@developer.gserviceaccount.com/
    default/
    

If no service account is found, the output is blank.

## What's next

  * Learn more about [OS Login](https://docs.cloud.google.com/compute/docs/oslogin).
  * Learn how [SSH connections to Linux instances](https://docs.cloud.google.com/compute/docs/instances/ssh) work on Compute Engine.
  * For step-by-step instructions, review one of the following: 
    * [Setting up OS Login](https://docs.cloud.google.com/compute/docs/instances/managing-instance-access).
    * [Setting up OS Login with 2-step verification](https://docs.cloud.google.com/compute/docs/oslogin/setup-two-factor-authentication)
  * Review [Managing OS Login in an organization](https://docs.cloud.google.com/compute/docs/oslogin/manage-oslogin-in-an-org)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
