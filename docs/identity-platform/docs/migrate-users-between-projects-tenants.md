---
url: https://docs.cloud.google.com/identity-platform/docs/migrate-users-between-projects-tenants/
title: Migrating users between projects and tenants \u00a0|\u00a0 Identity Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T01:49:22.354522+00:00
---

# Migrating users between projects and tenants  |  Identity Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/identity-platform/docs/migrate-users-between-projects-tenants/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Identity Platform ](https://docs.cloud.google.com/identity-platform/docs)
  * [ Guides ](https://docs.cloud.google.com/identity-platform/docs/how-to)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Migrating users between projects and tenants

This document explains how to migrate users from an existing Identity Platform project to a different one. It also shows how to migrate users from a non-tenant project to a tenant, or migrate users between tenants.

## Before you begin

  * [Install the Admin SDK](https://docs.cloud.google.com/identity-platform/docs/install-admin-sdk).



## Configuring service account keys

Before you can migrate user accounts, you need service account keys for both the source and target projects. The service accounts must be granted at least the IAM Editor role (`roles/editor`) to access the users and their hashed passwords from the source project. See the [IAM documentation](https://docs.cloud.google.com/iam/docs) to learn more about creating service accounts, granting permissions, and obtaining keys.

After downloading the keys, use them to instantiate two `auth` instances.
    
    
    var admin = require('firebase-admin');
    
    var sourceApp = admin.initializeApp({
      credential: admin.credential.cert('source-project-service-account.json'),
    }, 'source-app');
    
    var targetApp = admin.initializeApp({
      credential: admin.credential.cert('target-project-service-account.json'),
    }, 'target-app');
    
    var authFrom = sourceApp.auth();
    var authTo = targetApp.auth();
    

If your access control policies don't allow the use of multiple service accounts in a single workload, you can still use the example code from this document, but you'll need to download all users from the source project to a storage system first, then upload them to the target project in a separate workload.

## Migrating users between projects

To migrate users, call the `admin.auth().listUsers` method, which returns a a paginated list of users. You can then call `admin.auth().importUsers()` to upload them to the target project.

A maximum of 1000 users can be downloaded or uploaded at a time.

For password users, you need to supply the hash config for password hashing. You can retrieve the hash config by navigating to the [Identity Platform Users page](https://console.cloud.google.com/customer-identity/users) in the Google Cloud console, and then clicking **Import Users**.

The following example shows how to migrate users:
    
    
    function migrateUsers(userImportOptions, nextPageToken) {
     var pageToken;
     authFrom.listUsers(1000, nextPageToken)
       .then(function(listUsersResult) {
        var users = [];
        listUsersResult.users.forEach(function(user) {
          var modifiedUser = user.toJSON();
          // Convert to bytes.
          if (user.passwordHash) {
           modifiedUser.passwordHash = Buffer.from(user.passwordHash, 'base64');
           modifiedUser.passwordSalt = Buffer.from(user.passwordSalt, 'base64');
          }
          // Delete tenant ID if available. This will be set automatically.
          delete modifiedUser.tenantId;
          users.push(modifiedUser);
        });
        // Save next page token.
        pageToken = listUsersResult.pageToken;
        // Upload current chunk.
        return authTo.importUsers(users, userImportOptions);
       })
       .then(function(results) {
        results.errors.forEach(function(indexedError) {
           console.log('Error importing user ' + indexedError.index);
         });
         // Continue if there is another page.
         if (pageToken) {
             migrateUsers(userImportOptions, pageToken);
         }
       })
       .catch(function(error) {
         console.log('Error importing users:', error);
       });
    }
    var userImportOptions = {
     hash: {
       algorithm: 'SCRYPT',
       // The following parameters can be obtained from the "Users" page in the
       // Cloud console. The key must be a byte buffer.
       key: Buffer.from('base64-secret', 'base64'),
       saltSeparator: Buffer.from('base64SaltSeparator', 'base64'),
       rounds: 8,
       memoryCost: 14
     }
    };
    
    migrateUsers(userImportOptions);
    

For more information, see the [Admin SDK API reference](https://firebase.google.com/docs/auth/admin/import-users).

## Migrating users to a tenant

Migrating users from a non-tenant project to a tenant is almost exactly the same as migrating users between projects.

Assuming the tenant belongs to a different project than the source Identity Platform project, use the same code as before, but call `admin.auth().tenantManager().authForTenant()` on the target app instance and set the target tenant ID before calling `importUsers()`.
    
    
    var authTo = targetApp.auth().tenantManager().authForTenant('tenant');
    

## Migrating users between tenants

Migrating users between tenants is very similar to migrating users between projects, with two key differences:

  1. You'll need to delete the tenant ID from users of the old tenant before uploading them to the new tenant. Skipping this step will result in tenant ID mismatch errors.

  2. Call `admin.auth().tenantManager().authForTenant()` to set the tenant ID on the source and target tenants.
         
         // Migrate from tenant1 to tenant2 in same project.
         var authFrom = admin.auth().tenantManager().authForTenant('tenant1');
         var authTo = admin.auth().tenantManager().authForTenant('tenant2');
         




The rest of the code is the same.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
