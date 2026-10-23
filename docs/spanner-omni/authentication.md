---
url: https://docs.cloud.google.com/spanner-omni/authentication/
title: Authentication and authorization in Spanner Omni \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:32:23.848224+00:00
---

# Authentication and authorization in Spanner Omni  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spanner-omni/authentication/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Spanner Omni ](https://docs.cloud.google.com/spanner-omni)
  * [ Guides ](https://docs.cloud.google.com/spanner-omni/overview)



Send feedback 

#  Authentication and authorization in Spanner Omni Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how secure Spanner Omni deployments control access through authentication and authorization. You create and manage users, and assign them roles that define their permissions. Users can authenticate using one of the following methods:

  * **Password authentication** : Uses the [OPAQUE](https://datatracker.ietf.org/doc/html/rfc9807) password protocol. This protocol enhances security by providing signed access tokens for subsequent requests.
  * **Client certificate authentication** : Uses certificates signed by the same Certificate Authority (CA) that signed the API server certificates. The certificate's `Common Name` identifies the user.



Authorization in Spanner Omni uses Identity and Access Management (IAM) role and permission names, similar to Spanner. You assign roles to users that grant specific permissions. Spanner Omni IAM differs from Spanner IAM. For example, it doesn't support custom roles and includes specific Spanner Omni permissions.

## Users

In a secure deployment, accessing Spanner Omni APIs requires a user. You can create, update, and delete users using the Spanner Omni CLI. Each Spanner Omni deployment creates a single `admin` user by default with the password `admin`.

**Important:** Change this password immediately after you start Spanner Omni using the following command: `spanner auth update-password admin`

### Create users

Create new users so you can assign different roles and audit usage. The following command assigns a new user the `roles/spanner.databaseUser` role so they can read from and write to a Spanner Omni database.
    
    
    spanner users create USER_NAME --roles=roles/spanner.databaseUser
    

### Delete users

Delete obsolete users from the system:
    
    
    spanner users delete USER_NAME
    

### Update users

Update a user's state and roles. This command overwrites the existing state and roles:
    
    
    spanner users update USER_NAME --roles=NEW_ROLES --state=ACTIVE
    

## Authentication

In a secure deployment, users must sign in before accessing a Spanner Omni deployment.

Spanner Omni provides two mechanisms for authenticating users:

Mechanism | Description  
---|---  
Passwords | Users enter both their username and password.  
Client certificates | Clients use certificates signed by the same Certificate Authority (CA) that signed the API server certificates.  
  
### Passwords

Password authentication requires you to enter your username and password. It works only when TLS is enabled on the server.
    
    
    spanner auth login USER_NAME
    

Spanner Omni uses an implementation of the OPAQUE protocol to avoid sending passwords to the server, which protects the system from Man-in-the-Middle attacks. Spanner Omni stores no passwords on the server, so unintended access to the server doesn't compromise user credentials. After you successfully authenticate, Spanner Omni returns a signed access token. Attach the access token to all further requests. The Spanner Omni CLI stores the access token in `~/.config/spanner/access_token/token.txt`. To maintain the security of your system, don't share this token with others.

By default, the access token has an expiration time of 60 minutes. After 60 minutes elapse, the server does not accept the access token, and you must sign in again. Spanner Omni signs the access token to prevent tampering.

To prevent passwords from appearing where you might view them, such as environment variables or command-line flags, the Spanner Omni CLI commands accept passwords in two ways:

  * Prompts that mask your input.
  * Strings in files. Spanner Omni verifies file permissions are 600, overwrites the files with random data, and deletes them after reading.



For more details, run `spanner auth --help`.

### Client certificates

Client certificate authentication requires clients to use certificates signed by the same Certificate Authority (CA) that signed the API server certificates. Include the username of a valid, active user in the `Common Name` field of the certificate. When performing authorization, the roles you assign determine if you have permissions to perform the requested operation. To attach a client certificate to a request, use the `--ca-certificate-file` and `--client-certificate-directory` flags. The following is an example of listing databases:
    
    
    spanner databases list --ca-certificate-file PATH_TO_CA_CERT --client-certificate-directory PATH_TO_CLIENT_CERT_DIR
    

## Authorization

Spanner Omni uses most of the same [IAM role and permission names](https://docs.cloud.google.com/spanner/docs/iam) as Spanner. When you create a user, you can assign one or more roles to the user. Each role contains one or more permissions.

To list the available roles in Spanner Omni, use the following command:
    
    
    spanner roles list
    

The following are differences between Spanner IAM and Spanner Omni IAM:

  * Spanner Omni doesn't support custom roles.
  * Roles in Spanner Omni don't contain permissions outside the Spanner namespace, such as those not prefixed by `spanner.`.
  * Spanner Omni shares some, but not all, of the permissions used by Spanner.
  * Spanner Omni includes unique permissions not present in Spanner.



To learn about IAM permissions in Spanner Omni, see [IAM overview](https://docs.cloud.google.com/spanner-omni/iam#permissions).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
