---
url: https://docs.cloud.google.com/spanner/docs/use-cmek/
title: Secure a database with customer-managed encryption keys (CMEK) \u00a0|\u00a0 Spanner \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:32:36.871472+00:00
---

# Secure a database with customer-managed encryption keys (CMEK)  |  Spanner  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spanner/docs/use-cmek/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Spanner ](https://docs.cloud.google.com/spanner/docs)
  * [ Guides ](https://docs.cloud.google.com/spanner/docs/create-query-database-console)



Send feedback 

#  Secure a database with customer-managed encryption keys (CMEK) Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to use manually-created customer-managed encryption keys (CMEK) for Spanner.

To learn more about CMEK, see the [Customer-managed encryption keys (CMEK) overview](https://docs.cloud.google.com/spanner/docs/cmek).

## Create a CMEK-enabled database

  1. Create a key in Cloud Key Management Service (Cloud KMS). You can use the following key types that have different [protection levels](https://docs.cloud.google.com/kms/docs/protection-levels) in Spanner:

     * [Cloud Key Management Service keys](https://docs.cloud.google.com/kms/docs/protection-levels#software)
     * [Cloud HSM keys](https://docs.cloud.google.com/kms/docs/hsm#create-a-key)
     * [Cloud External Key Manager keys](https://docs.cloud.google.com/kms/docs/ekm)

The key must be in the same location as your Spanner instance. For example, if your Spanner instance configuration is in `us-west1`, then your [Cloud KMS key ring location](https://docs.cloud.google.com/kms/docs/locations) must also be `us-west1`.

Not every Spanner [multi-region instance configuration](https://docs.cloud.google.com/spanner/docs/instance-configurations#configs-multi-region) has a corresponding Cloud KMS key ring location. For Spanner databases in [custom, dual-region, or multi-region instance configurations](https://docs.cloud.google.com/spanner/docs/instance-configurations#configuration), you can use multiple regional (single-region) Cloud KMS keys to protect your database. For example:

     * If your Spanner database is in the multi-region instance configuration `nam14`, then you can create Cloud KMS keys in `us-east4`, `northamerica-northeast1`, and `us-east1`.
     * If your database is in a custom instance configuration that uses `nam3` as the base instance configuration with an additional read-only replica in `us-central2`, then you can create Cloud KMS keys in `us-east4`, `us-east1`, `us-central1`, and `us-central2`.
**Note:** Protecting a CMEK database with a mix of Cloud KMS multi-region and single-region keys is not supported.

Optional: To see a list of the replica locations in your Spanner instance configuration, use the [`gcloud spanner instances get-locations`](https://docs.cloud.google.com/sdk/gcloud/reference/spanner/instances/get-locations) command:
    
    gcloud spanner instances get-locations <var>INSTANCE_ID</var>
    

For more information, see the following resources:

     * [Cloud KMS locations](https://docs.cloud.google.com/kms/docs/locations)
     * [Spanner locations](https://docs.cloud.google.com/spanner/docs/instance-configurations)
  2. Grant Spanner access to the key.

     1. In Cloud Shell, create and display the service agent, or display it if the account already exists:
            
            gcloud beta services identity create --service=spanner.googleapis.com \
                --project=PROJECT_ID

If you're prompted to install the **gcloud Beta Commands** component, type `Y`. After installation, the command is automatically restarted.

The [`gcloud services identity`](https://docs.cloud.google.com/sdk/gcloud/reference/beta/services/identity/create) command creates or gets the [service agent](https://docs.cloud.google.com/iam/docs/service-account-types#service-agent) that Spanner can use to access the Cloud KMS key on your behalf.

The service account ID is formatted like an email address:
            
            Service identity created: service-xxx@gcp-sa-spanner.iam.gserviceaccount.com
            

     2. Grant the [Cloud KMS CryptoKey Encrypter/Decrypter](https://docs.cloud.google.com/kms/docs/reference/permissions-and-roles#predefined)(`cloudkms.cryptoKeyEncrypterDecrypter`) role to the service account for each region (`--location`) in your Spanner instance configuration. To do so, run the [`gcloud kms keys add-iam-policybinding`](https://docs.cloud.google.com/sdk/gcloud/reference/kms/keys/add-iam-policy-binding) command:
            
            gcloud kms keys add-iam-policy-binding KMS_KEY \
                --location KMS_KEY_LOCATION \
                --keyring KMS_KEY_RING \
                --project=PROJECT_ID \
                --member serviceAccount:service-xxx@gcp-sa-spanner.iam.gserviceaccount.com \
                --role roles/cloudkms.cryptoKeyEncrypterDecrypter

Here's an example output:
            
            Updated IAM policy for key [KMS_KEY]
            

If you're using multiple Cloud KMS keys to protect your database, run the `gcloud kms keys add-iam-policybinding` command for all the your keys.

This role ensures that the service account has permission to both encrypt and decrypt with the Cloud KMS key. For more information, see [Cloud KMS permissions and roles](https://docs.cloud.google.com/kms/docs/reference/permissions-and-roles).

  3. Create the database and specify your Cloud KMS key.


**Note:** You can't use the Google Cloud console to create a database in a custom, dual-region, or multi-region instance configuration that uses multiple Cloud KMS keys. You must use the gcloud CLI or client libraries to do so.

### Console

Use the console to create databases in regional instance configurations.

  1. In the Google Cloud console, go to the **Instances** page.

[Go to Spanner Instances](https://console.cloud.google.com/spanner/instances)

  2. Click the instance where you want to create a database.

  3. Click **Create database** and fill out the required fields.

  4. Click **Show encryption options**.

  5. Select **Cloud KMS key**.

  6. Select a key from the drop-down list.

The list of keys is limited to the current Google Cloud project. To use a key from a different Google Cloud project, create the database using gcloud CLI instead of the Google Cloud console.

Once the database is created, you can verify that the database is CMEK-enabled by viewing the **Database overview** page.

![Screenshot that shows the encryption type and key of a database](https://docs.cloud.google.com/static/spanner/docs/images/cmek-show-key.png)




###  gcloud 

To create a CMEK-enabled database in a regional, custom, or multi-region instance configuration, run the [`gcloud spanner databases create`](https://docs.cloud.google.com/sdk/gcloud/reference/spanner/databases/create) command:
    
    
    gcloud spanner databases create DATABASE \
      --project=SPANNER_PROJECT_ID \
      --instance=INSTANCE_ID \
      --ddl="CREATE TABLE Users (Id INT64 NOT NULL, FirstName STRING(100) NOT NULL, LastName STRING(100) NOT NULL,) PRIMARY KEY (Id)" \
      --kms-project=KMS_PROJECT_ID \
      --kms-location=KMS_KEY_LOCATION \
      --kms-keyring=KMS_KEYRING \
      --kms-keys=KMS_KEY_1[, KMS_KEY_2 ... ]

To verify that a database is CMEK-enabled, run the [`gcloud spanner databases describe`](https://docs.cloud.google.com/sdk/gcloud/reference/spanner/databases/describe) command:
    
    
    gcloud spanner databases describe DATABASE \
      --project=SPANNER_PROJECT_ID \
      --instance=INSTANCE_ID

CMEK-enabled databases include a field for `encryptionConfig`, as shown in the following example output:
    
    
    encryptionConfig:
      kmsKeyNames:projects/my-kms-project/locations/eur5/keyRings/my-kms-key-ring/cryptoKeys/my-kms-key
      name: projects/my-spanner-project/instances/my-instance/databases/my-db
    state: READY
    

###  Client libraries 

### C#

To create a CMEK-enabled database in a regional instance configuration:
    
    
    using [Google.Cloud.Spanner.Admin.Database.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.html);
    using [Google.Cloud.Spanner.Common.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Common.V1/latest/Google.Cloud.Spanner.Common.V1.html);
    using System;
    using System.Threading.Tasks;
    
    public class CreateDatabaseWithEncryptionKeyAsyncSample
    {
        public async Task<Database> CreateDatabaseWithEncryptionKeyAsync(string projectId, string instanceId, string databaseId, [CryptoKeyName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.CryptoKeyName.html) kmsKeyName)
        {
            // Create a DatabaseAdminClient instance that can be used to execute a
            // CreateDatabaseRequest with custom encryption configuration options.
            [DatabaseAdminClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.DatabaseAdminClient.html) databaseAdminClient = [DatabaseAdminClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.DatabaseAdminClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.DatabaseAdminClient.html#Google_Cloud_Spanner_Admin_Database_V1_DatabaseAdminClient_Create)();
            // Define create table statement for table #1.
            var createSingersTable =
                @"CREATE TABLE Singers (
                    SingerId INT64 NOT NULL,
                    FirstName STRING(1024),
                    LastName STRING(1024),
                    ComposerInfo BYTES(MAX)
                ) PRIMARY KEY (SingerId)";
            // Define create table statement for table #2.
            var createAlbumsTable =
                @"CREATE TABLE Albums (
                    SingerId INT64 NOT NULL,
                    AlbumId INT64 NOT NULL,
                    AlbumTitle STRING(MAX)
                ) PRIMARY KEY (SingerId, AlbumId),
                INTERLEAVE IN PARENT Singers ON DELETE CASCADE";
    
            // Create the CreateDatabase request with encryption configuration and execute it.
            var request = new [CreateDatabaseRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.CreateDatabaseRequest.html)
            {
                ParentAsInstanceName = [InstanceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Common.V1/latest/Google.Cloud.Spanner.Common.V1.InstanceName.html).[FromProjectInstance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Common.V1/latest/Google.Cloud.Spanner.Common.V1.InstanceName.html#Google_Cloud_Spanner_Common_V1_InstanceName_FromProjectInstance_System_String_System_String_)(projectId, instanceId),
                CreateStatement = $"CREATE DATABASE `{databaseId}`",
                ExtraStatements = { createSingersTable, createAlbumsTable },
                EncryptionConfig = new [EncryptionConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.EncryptionConfig.html)
                {
                    KmsKeyNameAsCryptoKeyName = kmsKeyName,
                },
            };
            var operation = await databaseAdminClient.[CreateDatabaseAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.DatabaseAdminClient.html#Google_Cloud_Spanner_Admin_Database_V1_DatabaseAdminClient_CreateDatabaseAsync_Google_Cloud_Spanner_Admin_Database_V1_CreateDatabaseRequest_Google_Api_Gax_Grpc_CallSettings_)(request);
    
            // Wait until the operation has finished.
            Console.WriteLine("Waiting for the operation to finish.");
            var completedResponse = await operation.PollUntilCompletedAsync();
            if (completedResponse.IsFaulted)
            {
                Console.WriteLine($"Error while creating database: {completedResponse.Exception}");
                throw completedResponse.Exception;
            }
    
            var database = completedResponse.Result;
            Console.WriteLine($"Database {database.Name} created with encryption key {database.[EncryptionConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.EncryptionConfig.html).KmsKeyName}");
    
            return database;
        }
    }

To create a CMEK-enabled database in a multi-region instance configuration:
    
    
    using [Google.Cloud.Spanner.Admin.Database.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.html);
    using [Google.Cloud.Spanner.Common.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Common.V1/latest/Google.Cloud.Spanner.Common.V1.html);
    using System;
    using System.Collections.Generic;
    using System.Threading.Tasks;
    
    public class CreateDatabaseWithMultiRegionEncryptionAsyncSample
    {
        public async Task<Database> CreateDatabaseWithMultiRegionEncryptionAsync(string projectId, string instanceId, string databaseId, IEnumerable<CryptoKeyName> kmsKeyNames)
        {
            // Create a DatabaseAdminClient instance that can be used to execute a
            // CreateDatabaseRequest with custom encryption configuration options.
            [DatabaseAdminClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.DatabaseAdminClient.html) databaseAdminClient = [DatabaseAdminClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.DatabaseAdminClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.DatabaseAdminClient.html#Google_Cloud_Spanner_Admin_Database_V1_DatabaseAdminClient_Create)();
            // Define create table statement for table #1.
            var createSingersTable =
                @"CREATE TABLE Singers (
                    SingerId INT64 NOT NULL,
                    FirstName STRING(1024),
                    LastName STRING(1024),
                    ComposerInfo BYTES(MAX)
                ) PRIMARY KEY (SingerId)";
            // Define create table statement for table #2.
            var createAlbumsTable =
                @"CREATE TABLE Albums (
                    SingerId INT64 NOT NULL,
                    AlbumId INT64 NOT NULL,
                    AlbumTitle STRING(MAX)
                 ) PRIMARY KEY (SingerId, AlbumId),
                 INTERLEAVE IN PARENT Singers ON DELETE CASCADE";
    
            // Create the CreateDatabase request with encryption configuration and execute it.
            var request = new [CreateDatabaseRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.CreateDatabaseRequest.html)
            {
                ParentAsInstanceName = [InstanceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Common.V1/latest/Google.Cloud.Spanner.Common.V1.InstanceName.html).[FromProjectInstance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Common.V1/latest/Google.Cloud.Spanner.Common.V1.InstanceName.html#Google_Cloud_Spanner_Common_V1_InstanceName_FromProjectInstance_System_String_System_String_)(projectId, instanceId),
                CreateStatement = $"CREATE DATABASE `{databaseId}`",
                ExtraStatements = { createSingersTable, createAlbumsTable },
                EncryptionConfig = new [EncryptionConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.EncryptionConfig.html)
                {
                    KmsKeyNamesAsCryptoKeyNames = { kmsKeyNames },
                },
            };
            var operation = await databaseAdminClient.[CreateDatabaseAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.DatabaseAdminClient.html#Google_Cloud_Spanner_Admin_Database_V1_DatabaseAdminClient_CreateDatabaseAsync_Google_Cloud_Spanner_Admin_Database_V1_CreateDatabaseRequest_Google_Api_Gax_Grpc_CallSettings_)(request);
    
            // Wait until the operation has finished.
            Console.WriteLine("Waiting for the operation to finish.");
            var completedResponse = await operation.PollUntilCompletedAsync();
            if (completedResponse.IsFaulted)
            {
                Console.WriteLine($"Error while creating database: {completedResponse.Exception}");
                throw completedResponse.Exception;
            }
    
            var database = completedResponse.Result;
            Console.WriteLine($"Database {database.Name} created with encryption keys {string.Join(", ", kmsKeyNames)}");
    
            return database;
        }
    }

### C++

To create a CMEK-enabled database in a regional instance configuration:
    
    
    void CreateDatabaseWithEncryptionKey(
        google::cloud::spanner_admin::DatabaseAdminClient client,
        std::string const& project_id, std::string const& instance_id,
        std::string const& database_id,
        google::cloud::KmsKeyName const& encryption_key) {
      google::cloud::spanner::Database database(project_id, instance_id,
                                                database_id);
      google::spanner::admin::database::v1::CreateDatabaseRequest request;
      request.set_parent(database.instance().FullName());
      request.set_create_statement("CREATE DATABASE `" + database.database_id() +
                                   "`");
      request.add_extra_statements(R"""(
          CREATE TABLE Singers (
              SingerId   INT64 NOT NULL,
              FirstName  STRING(1024),
              LastName   STRING(1024),
              SingerInfo BYTES(MAX),
              FullName   STRING(2049)
                  AS (ARRAY_TO_STRING([FirstName, LastName], " ")) STORED
          ) PRIMARY KEY (SingerId))""");
      request.add_extra_statements(R"""(
          CREATE TABLE Albums (
              SingerId     INT64 NOT NULL,
              AlbumId      INT64 NOT NULL,
              AlbumTitle   STRING(MAX)
          ) PRIMARY KEY (SingerId, AlbumId),
              INTERLEAVE IN PARENT Singers ON DELETE CASCADE)""");
      request.mutable_encryption_config()->set_kms_key_name(
          encryption_key.FullName());
      auto db = client.CreateDatabase(request).get();
      if (!db) throw std::move(db).status();
      std::cout << "Database " << db->name() << " created";
      std::cout << " using encryption key " << encryption_key.FullName();
      std::cout << ".\n";
    }

To create a CMEK-enabled database in a multi-region instance configuration:
    
    
    void CreateDatabaseWithMRCMEK(
        google::cloud::spanner_admin::DatabaseAdminClient client,
        std::string const& project_id, std::string const& instance_id,
        std::string const& database_id,
        std::vector<google::cloud::KmsKeyName> const& encryption_keys) {
      google::cloud::spanner::Database database(project_id, instance_id,
                                                database_id);
      google::spanner::admin::database::v1::CreateDatabaseRequest request;
      request.set_parent(database.instance().FullName());
      request.set_create_statement("CREATE DATABASE `" + database.database_id() +
                                   "`");
      request.add_extra_statements(R"""(
          CREATE TABLE Singers (
              SingerId   INT64 NOT NULL,
              FirstName  STRING(1024),
              LastName   STRING(1024),
              SingerInfo BYTES(MAX),
              FullName   STRING(2049)
                  AS (ARRAY_TO_STRING([FirstName, LastName], " ")) STORED
          ) PRIMARY KEY (SingerId))""");
      request.add_extra_statements(R"""(
          CREATE TABLE Albums (
              SingerId     INT64 NOT NULL,
              AlbumId      INT64 NOT NULL,
              AlbumTitle   STRING(MAX)
          ) PRIMARY KEY (SingerId, AlbumId),
              INTERLEAVE IN PARENT Singers ON DELETE CASCADE)""");
      for (google::cloud::KmsKeyName const& encryption_key : encryption_keys) {
        request.mutable_encryption_config()->add_kms_key_names(
            encryption_key.FullName());
      }
      auto db = client.CreateDatabase(request).get();
      if (!db) throw std::move(db).status();
      std::cout << "Database " << db->name() << " created";
      PrintKmsKeys(encryption_keys);
    }

### Go

To create a CMEK-enabled database in a regional instance configuration:
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    	"regexp"
    
    	database "cloud.google.com/go/spanner/admin/database/apiv1"
    	adminpb "cloud.google.com/go/spanner/admin/database/apiv1/databasepb"
    )
    
    func createDatabaseWithCustomerManagedEncryptionKey(ctx context.Context, w io.Writer, db, kmsKeyName string) error {
    	// db = `projects/<project>/instances/<instance-id>/database/<database-id>`
    	// kmsKeyName = `projects/<project>/locations/<location>/keyRings/<key_ring>/cryptoKeys/<kms_key_name>`
    	matches := regexp.MustCompile("^(.+)/databases/(.+)$").FindStringSubmatch(db)
    	if matches == nil || len(matches) != 3 {
    		return fmt.Errorf("createDatabaseWithCustomerManagedEncryptionKey: invalid database id %q", db)
    	}
    	instanceName := matches[1]
    	databaseId := matches[2]
    
    	adminClient, err := database.NewDatabaseAdminClient(ctx)
    	if err != nil {
    		return fmt.Errorf("createDatabaseWithCustomerManagedEncryptionKey.NewDatabaseAdminClient: %w", err)
    	}
    	defer adminClient.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/spanner/latest/admin/database/apiv1.html#cloud_google_com_go_spanner_admin_database_apiv1_DatabaseAdminClient_Close)()
    
    	// Create a database with tables using a Customer Managed Encryption Key
    	req := adminpb.CreateDatabaseRequest{
    		Parent:          instanceName,
    		CreateStatement: "CREATE DATABASE `" + databaseId + "`",
    		ExtraStatements: []string{
    			`CREATE TABLE Singers (
    				SingerId   INT64 NOT NULL,
    				FirstName  STRING(1024),
    				LastName   STRING(1024),
    				SingerInfo BYTES(MAX)
    			) PRIMARY KEY (SingerId)`,
    			`CREATE TABLE Albums (
    				SingerId     INT64 NOT NULL,
    				AlbumId      INT64 NOT NULL,
    				AlbumTitle   STRING(MAX)
    			) PRIMARY KEY (SingerId, AlbumId),
    			INTERLEAVE IN PARENT Singers ON DELETE CASCADE`,
    		},
    		EncryptionConfig: &adminpb.EncryptionConfig{KmsKeyName: kmsKeyName},
    	}
    	op, err := adminClient.CreateDatabase(ctx, &req)
    	if err != nil {
    		return fmt.Errorf("createDatabaseWithCustomerManagedEncryptionKey.CreateDatabase: %w", err)
    	}
    	dbObj, err := op.Wait(ctx)
    	if err != nil {
    		return fmt.Errorf("createDatabaseWithCustomerManagedEncryptionKey.Wait: %w", err)
    	}
    	fmt.Fprintf(w, "Created database [%s] using encryption key %q\n", dbObj.Name, dbObj.EncryptionConfig.KmsKeyName)
    	return nil
    }
    

To create a CMEK-enabled database in a multi-region instance configuration:
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	database "cloud.google.com/go/spanner/admin/database/apiv1"
    	adminpb "cloud.google.com/go/spanner/admin/database/apiv1/databasepb"
    )
    
    // createDatabaseWithCustomerManagedMultiRegionEncryptionKey creates a new database with tables using a Customer Managed Multi-Region Encryption Key.
    func createDatabaseWithCustomerManagedMultiRegionEncryptionKey(ctx context.Context, w io.Writer, projectID, instanceID, databaseID string, kmsKeyNames []string) error {
    	// projectID = `my-project`
    	// instanceID = `my-instance`
    	// databaseID = `my-database`
    	// kmsKeyNames := []string{"projects/my-project/locations/locations/<location1>/keyRings/<keyRing>/cryptoKeys/<keyId>",
    	//	 "projects/my-project/locations/locations/<location2>/keyRings/<keyRing>/cryptoKeys/<keyId>",
    	//	 "projects/my-project/locations/locations/<location3>/keyRings/<keyRing>/cryptoKeys/<keyId>",
    	// }
    
    	adminClient, err := database.NewDatabaseAdminClient(ctx)
    	if err != nil {
    		return fmt.Errorf("createDatabaseWithCustomerManagedMultiRegionEncryptionKey.NewDatabaseAdminClient: %w", err)
    	}
    	defer adminClient.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/spanner/latest/admin/database/apiv1.html#cloud_google_com_go_spanner_admin_database_apiv1_DatabaseAdminClient_Close)()
    
    	// Create a database with tables using a Customer Managed Multi-Region Encryption Key
    	req := adminpb.CreateDatabaseRequest{
    		Parent:          fmt.Sprintf("projects/%s/instances/%s", projectID, instanceID),
    		CreateStatement: "CREATE DATABASE `" + databaseID + "`",
    		ExtraStatements: []string{
    			`CREATE TABLE Singers (
    				SingerId   INT64 NOT NULL,
    				FirstName  STRING(1024),
    				LastName   STRING(1024),
    				SingerInfo BYTES(MAX)
    			) PRIMARY KEY (SingerId)`,
    			`CREATE TABLE Albums (
    				SingerId     INT64 NOT NULL,
    				AlbumId      INT64 NOT NULL,
    				AlbumTitle   STRING(MAX)
    			) PRIMARY KEY (SingerId, AlbumId),
    			INTERLEAVE IN PARENT Singers ON DELETE CASCADE`,
    		},
    		EncryptionConfig: &adminpb.EncryptionConfig{KmsKeyNames: kmsKeyNames},
    	}
    	op, err := adminClient.CreateDatabase(ctx, &req)
    	if err != nil {
    		return fmt.Errorf("createDatabaseWithCustomerManagedMultiRegionEncryptionKey.CreateDatabase: %w", err)
    	}
    	dbObj, err := op.Wait(ctx)
    	if err != nil {
    		return fmt.Errorf("createDatabaseWithCustomerManagedMultiRegionEncryptionKey.Wait: %w", err)
    	}
    	fmt.Fprintf(w, "Created database [%s] using multi-region encryption keys %q\n", dbObj.Name, dbObj.EncryptionConfig.GetKmsKeyNames())
    	return nil
    }
    

### Java

To create a CMEK-enabled database in a regional instance configuration:
    
    
    import com.google.cloud.spanner.[Spanner](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.Spanner.html);
    import com.google.cloud.spanner.[SpannerExceptionFactory](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.SpannerExceptionFactory.html);
    import com.google.cloud.spanner.[SpannerOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.SpannerOptions.html);
    import com.google.cloud.spanner.admin.database.v1.[DatabaseAdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.admin.database.v1.DatabaseAdminClient.html);
    import com.google.common.collect.ImmutableList;
    import com.google.spanner.admin.database.v1.[CreateDatabaseRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.CreateDatabaseRequest.html);
    import com.google.spanner.admin.database.v1.[Database](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.Database.html);
    import com.google.spanner.admin.database.v1.[EncryptionConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.EncryptionConfig.html);
    import com.google.spanner.admin.database.v1.[InstanceName](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.InstanceName.html);
    import java.util.concurrent.ExecutionException;
    import java.util.concurrent.TimeUnit;
    import java.util.concurrent.TimeoutException;
    
    public class CreateDatabaseWithEncryptionKey {
    
      static void createDatabaseWithEncryptionKey() {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "my-project";
        String instanceId = "my-instance";
        String databaseId = "my-database";
        String kmsKeyName =
            "projects/" + projectId + "/locations/<location>/keyRings/<keyRing>/cryptoKeys/<keyId>";
    
        try ([Spanner](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.Spanner.html) spanner =
            [SpannerOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.SpannerOptions.html).newBuilder().setProjectId(projectId).build().getService();
            [DatabaseAdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.admin.database.v1.DatabaseAdminClient.html) adminClient = spanner.[createDatabaseAdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.Spanner.html#com_google_cloud_spanner_Spanner_createDatabaseAdminClient__)()) {
          createDatabaseWithEncryptionKey(
              adminClient,
              projectId,
              instanceId,
              databaseId,
              kmsKeyName);
        }
      }
    
      static void createDatabaseWithEncryptionKey([DatabaseAdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.admin.database.v1.DatabaseAdminClient.html) adminClient,
          String projectId, String instanceId, String databaseId, String kmsKeyName) {
        [InstanceName](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.InstanceName.html) instanceName = [InstanceName](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.InstanceName.html).of(projectId, instanceId);
        [CreateDatabaseRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.CreateDatabaseRequest.html) request = [CreateDatabaseRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.CreateDatabaseRequest.html).newBuilder()
            .setParent(instanceName.[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.InstanceName.html#com_google_spanner_admin_database_v1_InstanceName_toString__)())
            .[setCreateStatement](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.CreateDatabaseRequest.Builder.html#com_google_spanner_admin_database_v1_CreateDatabaseRequest_Builder_setCreateStatement_java_lang_String_)("CREATE DATABASE `" + databaseId + "`")
            .setEncryptionConfig([EncryptionConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.EncryptionConfig.html).newBuilder().setKmsKeyName(kmsKeyName).build())
            .[addAllExtraStatements](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.CreateDatabaseRequest.Builder.html#com_google_spanner_admin_database_v1_CreateDatabaseRequest_Builder_addAllExtraStatements_java_lang_Iterable_java_lang_String__)(
                ImmutableList.of(
                    "CREATE TABLE Singers ("
                        + "  SingerId   INT64 NOT NULL,"
                        + "  FirstName  STRING(1024),"
                        + "  LastName   STRING(1024),"
                        + "  SingerInfo BYTES(MAX)"
                        + ") PRIMARY KEY (SingerId)",
                    "CREATE TABLE Albums ("
                        + "  SingerId     INT64 NOT NULL,"
                        + "  AlbumId      INT64 NOT NULL,"
                        + "  AlbumTitle   STRING(MAX)"
                        + ") PRIMARY KEY (SingerId, AlbumId),"
                        + "  INTERLEAVE IN PARENT Singers ON DELETE CASCADE"
                ))
            .build();
        try {
          System.out.println("Waiting for operation to complete...");
          [Database](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.Database.html) createdDatabase =
              adminClient.[createDatabaseAsync](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.admin.database.v1.DatabaseAdminClient.html#com_google_cloud_spanner_admin_database_v1_DatabaseAdminClient_createDatabaseAsync__org_jspecify_annotations_Nullable_com_google_spanner_admin_database_v1_InstanceName_java_lang_String_)(request).get(120, TimeUnit.SECONDS);
    
          System.out.printf(
              "Database %s created with encryption key %s%n",
              createdDatabase.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.Database.html#com_google_spanner_admin_database_v1_Database_getName__)(),
              createdDatabase.[getEncryptionConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.Database.html#com_google_spanner_admin_database_v1_Database_getEncryptionConfig__)().getKmsKeyName()
          );
        } catch (ExecutionException e) {
          // If the operation failed during execution, expose the cause.
          throw [SpannerExceptionFactory](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.SpannerExceptionFactory.html).[asSpannerException](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.SpannerExceptionFactory.html#com_google_cloud_spanner_SpannerExceptionFactory_asSpannerException_java_lang_Throwable_)(e.getCause());
        } catch (InterruptedException e) {
          // Throw when a thread is waiting, sleeping, or otherwise occupied,
          // and the thread is interrupted, either before or during the activity.
          throw [SpannerExceptionFactory](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.SpannerExceptionFactory.html).[propagateInterrupt](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.SpannerExceptionFactory.html#com_google_cloud_spanner_SpannerExceptionFactory_propagateInterrupt_java_lang_InterruptedException_)(e);
        } catch (TimeoutException e) {
          // If the operation timed out propagates the timeout
          throw [SpannerExceptionFactory](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.SpannerExceptionFactory.html).[propagateTimeout](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.SpannerExceptionFactory.html#com_google_cloud_spanner_SpannerExceptionFactory_propagateTimeout_java_util_concurrent_TimeoutException_)(e);
        }
      }
    }

To create a CMEK-enabled database in a multi-region instance configuration:
    
    
    import com.google.cloud.spanner.[Spanner](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.Spanner.html);
    import com.google.cloud.spanner.[SpannerExceptionFactory](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.SpannerExceptionFactory.html);
    import com.google.cloud.spanner.[SpannerOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.SpannerOptions.html);
    import com.google.cloud.spanner.admin.database.v1.[DatabaseAdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.admin.database.v1.DatabaseAdminClient.html);
    import com.google.common.collect.ImmutableList;
    import com.google.spanner.admin.database.v1.[CreateDatabaseRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.CreateDatabaseRequest.html);
    import com.google.spanner.admin.database.v1.[Database](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.Database.html);
    import com.google.spanner.admin.database.v1.[EncryptionConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.EncryptionConfig.html);
    import com.google.spanner.admin.database.v1.[InstanceName](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.InstanceName.html);
    import java.util.concurrent.ExecutionException;
    import java.util.concurrent.TimeUnit;
    import java.util.concurrent.TimeoutException;
    
    public class CreateDatabaseWithMultiRegionEncryptionKey {
    
      static void createDatabaseWithEncryptionKey() {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "my-project";
        String instanceId = "my-instance";
        String databaseId = "my-database";
        String[] kmsKeyNames =
            new String[] {
              "projects/" + projectId + "/locations/<location1>/keyRings/<keyRing>/cryptoKeys/<keyId>",
              "projects/" + projectId + "/locations/<location2>/keyRings/<keyRing>/cryptoKeys/<keyId>",
              "projects/" + projectId + "/locations/<location3>/keyRings/<keyRing>/cryptoKeys/<keyId>"
            };
        try ([Spanner](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.Spanner.html) spanner =
                [SpannerOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.SpannerOptions.html).newBuilder().setProjectId(projectId).build().getService();
            [DatabaseAdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.admin.database.v1.DatabaseAdminClient.html) adminClient = spanner.[createDatabaseAdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.Spanner.html#com_google_cloud_spanner_Spanner_createDatabaseAdminClient__)()) {
          createDatabaseWithMultiRegionEncryptionKey(
              adminClient, projectId, instanceId, databaseId, kmsKeyNames);
        }
      }
    
      static void createDatabaseWithMultiRegionEncryptionKey(
          [DatabaseAdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.admin.database.v1.DatabaseAdminClient.html) adminClient,
          String projectId,
          String instanceId,
          String databaseId,
          String[] kmsKeyNames) {
        [InstanceName](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.InstanceName.html) instanceName = [InstanceName](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.InstanceName.html).of(projectId, instanceId);
        [CreateDatabaseRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.CreateDatabaseRequest.html) request =
            [CreateDatabaseRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.CreateDatabaseRequest.html).newBuilder()
                .setParent(instanceName.[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.InstanceName.html#com_google_spanner_admin_database_v1_InstanceName_toString__)())
                .[setCreateStatement](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.CreateDatabaseRequest.Builder.html#com_google_spanner_admin_database_v1_CreateDatabaseRequest_Builder_setCreateStatement_java_lang_String_)("CREATE DATABASE `" + databaseId + "`")
                .setEncryptionConfig(
                    [EncryptionConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.EncryptionConfig.html).newBuilder()
                        .addAllKmsKeyNames(ImmutableList.copyOf(kmsKeyNames))
                        .build())
                .[addAllExtraStatements](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.CreateDatabaseRequest.Builder.html#com_google_spanner_admin_database_v1_CreateDatabaseRequest_Builder_addAllExtraStatements_java_lang_Iterable_java_lang_String__)(
                    ImmutableList.of(
                        "CREATE TABLE Singers ("
                            + "  SingerId   INT64 NOT NULL,"
                            + "  FirstName  STRING(1024),"
                            + "  LastName   STRING(1024),"
                            + "  SingerInfo BYTES(MAX)"
                            + ") PRIMARY KEY (SingerId)",
                        "CREATE TABLE Albums ("
                            + "  SingerId     INT64 NOT NULL,"
                            + "  AlbumId      INT64 NOT NULL,"
                            + "  AlbumTitle   STRING(MAX)"
                            + ") PRIMARY KEY (SingerId, AlbumId),"
                            + "  INTERLEAVE IN PARENT Singers ON DELETE CASCADE"))
                .build();
        try {
          System.out.println("Waiting for operation to complete...");
          [Database](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.Database.html) createdDatabase =
              adminClient.[createDatabaseAsync](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.admin.database.v1.DatabaseAdminClient.html#com_google_cloud_spanner_admin_database_v1_DatabaseAdminClient_createDatabaseAsync__org_jspecify_annotations_Nullable_com_google_spanner_admin_database_v1_InstanceName_java_lang_String_)(request).get(120, TimeUnit.SECONDS);
    
          System.out.printf(
              "Database %s created with encryption keys %s%n",
              createdDatabase.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.Database.html#com_google_spanner_admin_database_v1_Database_getName__)(), createdDatabase.[getEncryptionConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.Database.html#com_google_spanner_admin_database_v1_Database_getEncryptionConfig__)().getKmsKeyNamesList());
        } catch (ExecutionException e) {
          // If the operation failed during execution, expose the cause.
          throw [SpannerExceptionFactory](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.SpannerExceptionFactory.html).[asSpannerException](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.SpannerExceptionFactory.html#com_google_cloud_spanner_SpannerExceptionFactory_asSpannerException_java_lang_Throwable_)(e.getCause());
        } catch (InterruptedException e) {
          // Throw when a thread is waiting, sleeping, or otherwise occupied,
          // and the thread is interrupted, either before or during the activity.
          throw [SpannerExceptionFactory](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.SpannerExceptionFactory.html).[propagateInterrupt](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.SpannerExceptionFactory.html#com_google_cloud_spanner_SpannerExceptionFactory_propagateInterrupt_java_lang_InterruptedException_)(e);
        } catch (TimeoutException e) {
          // If the operation timed out propagates the timeout
          throw [SpannerExceptionFactory](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.SpannerExceptionFactory.html).[propagateTimeout](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.SpannerExceptionFactory.html#com_google_cloud_spanner_SpannerExceptionFactory_propagateTimeout_java_util_concurrent_TimeoutException_)(e);
        }
      }
    }

**Note:** The old client library interface code samples for Java are archived in [GitHub](https://github.com/googleapis/google-cloud-java/tree/main/java-spanner/samples/snippets/src/main/java/com/example/spanner/admin/archived). 

### Node.js

To create a CMEK-enabled database in a regional instance configuration:
    
    
    // Imports the Google Cloud client library
    const {Spanner, protos} = require('[@google-cloud/spanner](https://docs.cloud.google.com/nodejs/docs/reference/spanner/latest/overview.html)');
    
    /**
     * TODO(developer): Uncomment the following lines before running the sample.
     */
    // const projectId = 'my-project-id';
    // const instanceId = 'my-instance';
    // const databaseId = 'my-database';
    // const keyName =
    //   'projects/my-project-id/my-region/keyRings/my-key-ring/cryptoKeys/my-key';
    
    // creates a client
    const spanner = new [Spanner](https://docs.cloud.google.com/nodejs/docs/reference/spanner/latest/spanner/spanner.html)({
      projectId: projectId,
    });
    
    // Gets a reference to a Cloud Spanner Database Admin Client object
    const databaseAdminClient = spanner.[getDatabaseAdminClient](https://docs.cloud.google.com/nodejs/docs/reference/spanner/latest/spanner/spanner.html)();
    
    // Creates a database
    const [operation] = await databaseAdminClient.createDatabase({
      createStatement: 'CREATE DATABASE `' + databaseId + '`',
      parent: databaseAdminClient.instancePath(projectId, instanceId),
      encryptionConfig:
        (protos.google.spanner.admin.database.v1.[EncryptionConfig](https://docs.cloud.google.com/nodejs/docs/reference/spanner-api/latest/spanner-api/protos.google.spanner.admin.database.v1.encryptionconfig.html) = {
          kmsKeyName: keyName,
        }),
    });
    
    console.log(`Waiting for operation on ${databaseId} to complete...`);
    await operation.promise();
    
    console.log(`Created database ${databaseId} on instance ${instanceId}.`);
    
    // Get encryption key
    const [metadata] = await databaseAdminClient.getDatabase({
      name: databaseAdminClient.databasePath(projectId, instanceId, databaseId),
    });
    
    console.log(
      `Database encrypted with key ${metadata.encryptionConfig.kmsKeyName}.`,
    );

To create a CMEK-enabled database in a multi-region instance configuration:
    
    
    /**
     * TODO(developer): Uncomment the following lines before running the sample.
     */
    // const projectId = 'my-project-id';
    // const instanceId = 'my-instance';
    // const databaseId = 'my-database';
    // const kmsKeyNames =
    //   'projects/my-project-id/my-region/keyRings/my-key-ring/cryptoKeys/my-key1,projects/my-project-id/my-region/keyRings/my-key-ring/cryptoKeys/my-key2';
    
    // Imports the Google Cloud client library
    const {Spanner, protos} = require('[@google-cloud/spanner](https://docs.cloud.google.com/nodejs/docs/reference/spanner/latest/overview.html)');
    
    // creates a client
    const spanner = new [Spanner](https://docs.cloud.google.com/nodejs/docs/reference/spanner/latest/spanner/spanner.html)({
      projectId: projectId,
    });
    
    // Gets a reference to a Cloud Spanner Database Admin Client object
    const databaseAdminClient = spanner.[getDatabaseAdminClient](https://docs.cloud.google.com/nodejs/docs/reference/spanner/latest/spanner/spanner.html)();
    
    async function createDatabaseWithMultipleKmsKeys() {
      // Creates a database
      const [operation] = await databaseAdminClient.createDatabase({
        createStatement: 'CREATE DATABASE `' + databaseId + '`',
        parent: databaseAdminClient.instancePath(projectId, instanceId),
        encryptionConfig:
          (protos.google.spanner.admin.database.v1.[EncryptionConfig](https://docs.cloud.google.com/nodejs/docs/reference/spanner-api/latest/spanner-api/protos.google.spanner.admin.database.v1.encryptionconfig.html) = {
            kmsKeyNames: kmsKeyNames.split(','),
          }),
      });
    
      console.log(`Waiting for operation on ${databaseId} to complete...`);
      await operation.promise();
    
      console.log(`Created database ${databaseId} on instance ${instanceId}.`);
    
      // Get encryption key
      const [metadata] = await databaseAdminClient.getDatabase({
        name: databaseAdminClient.databasePath(projectId, instanceId, databaseId),
      });
    
      console.log(
        `Database encrypted with keys ${metadata.encryptionConfig.kmsKeyNames}.`,
      );
    }
    createDatabaseWithMultipleKmsKeys();

**Note:** The old client library interface code samples for Node.js are archived in [GitHub](https://github.com/googleapis/nodejs-spanner/tree/main/samples/archived). 

### PHP

To create a CMEK-enabled database in a regional instance configuration:
    
    
    use Google\Cloud\Spanner\Admin\Database\V1\Client\DatabaseAdminClient;
    use Google\Cloud\Spanner\Admin\Database\V1\CreateDatabaseRequest;
    use Google\Cloud\Spanner\Admin\Database\V1\EncryptionConfig;
    
    /**
     * Creates an encrypted database with tables for sample data.
     * Example:
     * ```
     * create_database_with_encryption_key($projectId, $instanceId, $databaseId, $kmsKeyName);
     * ```
     *
     * @param string $projectId The Google Cloud project ID.
     * @param string $instanceId The Spanner instance ID.
     * @param string $databaseId The Spanner database ID.
     * @param string $kmsKeyName The KMS key used for encryption.
     */
    function create_database_with_encryption_key(
        string $projectId,
        string $instanceId,
        string $databaseId,
        string $kmsKeyName
    ): void {
        $databaseAdminClient = new DatabaseAdminClient();
        $instanceName = DatabaseAdminClient::instanceName($projectId, $instanceId);
    
        $createDatabaseRequest = new CreateDatabaseRequest();
        $createDatabaseRequest->setParent($instanceName);
        $createDatabaseRequest->setCreateStatement(sprintf('CREATE DATABASE `%s`', $databaseId));
        $createDatabaseRequest->setExtraStatements([
            'CREATE TABLE Singers (
                SingerId     INT64 NOT NULL,
                FirstName    STRING(1024),
                LastName     STRING(1024),
                SingerInfo   BYTES(MAX)
            ) PRIMARY KEY (SingerId)',
            'CREATE TABLE Albums (
                SingerId     INT64 NOT NULL,
                AlbumId      INT64 NOT NULL,
                AlbumTitle   STRING(MAX)
            ) PRIMARY KEY (SingerId, AlbumId),
            INTERLEAVE IN PARENT Singers ON DELETE CASCADE'
        ]);
    
        if (!empty($kmsKeyName)) {
            $encryptionConfig = new EncryptionConfig();
            $encryptionConfig->setKmsKeyName($kmsKeyName);
            $createDatabaseRequest->setEncryptionConfig($encryptionConfig);
        }
    
        $operationResponse = $databaseAdminClient->createDatabase($createDatabaseRequest);
        printf('Waiting for operation to complete...' . PHP_EOL);
        $operationResponse->pollUntilComplete();
    
        if ($operationResponse->operationSucceeded()) {
            $database = $operationResponse->getResult();
            printf(
                'Created database %s on instance %s with encryption key %s' . PHP_EOL,
                $databaseId,
                $instanceId,
                $database->getEncryptionConfig()->getKmsKeyName()
            );
        } else {
            $error = $operationResponse->getError();
            printf('Failed to create encrypted database: %s' . PHP_EOL, $error->getMessage());
        }
    }

To create a CMEK-enabled database in a multi-region instance configuration:
    
    
    use Google\Cloud\Spanner\Admin\Database\V1\Client\DatabaseAdminClient;
    use Google\Cloud\Spanner\Admin\Database\V1\CreateDatabaseRequest;
    use Google\Cloud\Spanner\Admin\Database\V1\EncryptionConfig;
    
    /**
     * Creates a MR CMEK database with tables for sample data.
     * Example:
     * ```
     * create_database_with_mr_cmek($projectId, $instanceId, $databaseId, $kmsKeyNames);
     * ```
     *
     * @param string $projectId The Google Cloud project ID.
     * @param string $instanceId The Spanner instance ID.
     * @param string $databaseId The Spanner database ID.
     * @param string[] $kmsKeyNames The KMS keys used for encryption.
     */
    function create_database_with_mr_cmek(
        string $projectId,
        string $instanceId,
        string $databaseId,
        array $kmsKeyNames
    ): void {
        $databaseAdminClient = new DatabaseAdminClient();
        $instanceName = DatabaseAdminClient::instanceName($projectId, $instanceId);
    
        $createDatabaseRequest = new CreateDatabaseRequest();
        $createDatabaseRequest->setParent($instanceName);
        $createDatabaseRequest->setCreateStatement(sprintf('CREATE DATABASE `%s`', $databaseId));
        $createDatabaseRequest->setExtraStatements([
            'CREATE TABLE Singers (
                SingerId     INT64 NOT NULL,
                FirstName    STRING(1024),
                LastName     STRING(1024),
                SingerInfo   BYTES(MAX)
            ) PRIMARY KEY (SingerId)',
            'CREATE TABLE Albums (
                SingerId     INT64 NOT NULL,
                AlbumId      INT64 NOT NULL,
                AlbumTitle   STRING(MAX)
            ) PRIMARY KEY (SingerId, AlbumId),
            INTERLEAVE IN PARENT Singers ON DELETE CASCADE'
        ]);
    
        if (!empty($kmsKeyNames)) {
            $encryptionConfig = new EncryptionConfig();
            $encryptionConfig->setKmsKeyNames($kmsKeyNames);
            $createDatabaseRequest->setEncryptionConfig($encryptionConfig);
        }
    
        $operationResponse = $databaseAdminClient->createDatabase($createDatabaseRequest);
        printf('Waiting for operation to complete...' . PHP_EOL);
        $operationResponse->pollUntilComplete();
    
        if ($operationResponse->operationSucceeded()) {
            $database = $operationResponse->getResult();
            printf(
                'Created database %s on instance %s with encryption keys %s' . PHP_EOL,
                $databaseId,
                $instanceId,
                print_r($database->getEncryptionConfig()->getKmsKeyNames(), true)
            );
        } else {
            $error = $operationResponse->getError();
            printf('Failed to create encrypted database: %s' . PHP_EOL, $error->getMessage());
        }
    }

**Note:** The old client library interface code samples for PHP are archived in [GitHub](https://github.com/GoogleCloudPlatform/php-docs-samples/tree/main/spanner/src/admin/archived). 

### Python

To create a CMEK-enabled database in a regional instance configuration:
    
    
    def create_database_with_encryption_key(instance_id, database_id, kms_key_name):
        """Creates a database with tables using a Customer Managed Encryption Key (CMEK)."""
        from google.cloud.spanner_admin_database_v1 import [EncryptionConfig](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.EncryptionConfig.html)
        from google.cloud.spanner_admin_database_v1.types import spanner_database_admin
    
        spanner_client = spanner.Client()
        database_admin_api = spanner_client.database_admin_api
    
        request = spanner_database_admin.[CreateDatabaseRequest](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.CreateDatabaseRequest.html)(
            parent=database_admin_api.instance_path(spanner_client.project, instance_id),
            create_statement=f"CREATE DATABASE `{database_id}`",
            extra_statements=[
                """CREATE TABLE Singers (
                SingerId     INT64 NOT NULL,
                FirstName    STRING(1024),
                LastName     STRING(1024),
                SingerInfo   BYTES(MAX)
            ) PRIMARY KEY (SingerId)""",
                """CREATE TABLE Albums (
                SingerId     INT64 NOT NULL,
                AlbumId      INT64 NOT NULL,
                AlbumTitle   STRING(MAX)
            ) PRIMARY KEY (SingerId, AlbumId),
            INTERLEAVE IN PARENT Singers ON DELETE CASCADE""",
            ],
            encryption_config=EncryptionConfig(kms_key_name=kms_key_name),
        )
    
        operation = database_admin_api.create_database(request=request)
    
        print("Waiting for operation to complete...")
        database = operation.result(OPERATION_TIMEOUT_SECONDS)
    
        print(
            "Database {} created with encryption key {}".format(
                database.name, database.encryption_config.kms_key_name
            )
        )
    
    

To create a CMEK-enabled database in a multi-region instance configuration:
    
    
    def create_database_with_multiple_kms_keys(instance_id, database_id, kms_key_names):
        """Creates a database with tables using multiple KMS keys(CMEK)."""
        from google.cloud.spanner_admin_database_v1 import [EncryptionConfig](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.EncryptionConfig.html)
        from google.cloud.spanner_admin_database_v1.types import spanner_database_admin
    
        spanner_client = spanner.Client()
        database_admin_api = spanner_client.database_admin_api
    
        request = spanner_database_admin.[CreateDatabaseRequest](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.CreateDatabaseRequest.html)(
            parent=database_admin_api.instance_path(spanner_client.project, instance_id),
            create_statement=f"CREATE DATABASE `{database_id}`",
            extra_statements=[
                """CREATE TABLE Singers (
                SingerId     INT64 NOT NULL,
                FirstName    STRING(1024),
                LastName     STRING(1024),
                SingerInfo   BYTES(MAX)
            ) PRIMARY KEY (SingerId)""",
                """CREATE TABLE Albums (
                SingerId     INT64 NOT NULL,
                AlbumId      INT64 NOT NULL,
                AlbumTitle   STRING(MAX)
            ) PRIMARY KEY (SingerId, AlbumId),
            INTERLEAVE IN PARENT Singers ON DELETE CASCADE""",
            ],
            encryption_config=EncryptionConfig(kms_key_names=kms_key_names),
        )
    
        operation = database_admin_api.create_database(request=request)
    
        print("Waiting for operation to complete...")
        database = operation.result(OPERATION_TIMEOUT_SECONDS)
    
        print(
            "Database {} created with multiple KMS keys {}".format(
                database.name, database.encryption_config.kms_key_names
            )
        )
    
    

**Note:** The old client library interface code samples for Python are archived in [GitHub](https://github.com/googleapis/python-spanner/tree/main/samples/samples/archived). 

### Ruby

To create a CMEK-enabled database in a regional instance configuration:
    
    
    # project_id  = "Your Google Cloud project ID"
    # instance_id = "Your Spanner instance ID"
    # database_id = "Your Spanner database ID"
    # kms_key_name = "Database eencryption KMS key"
    
    require "google/cloud/spanner"
    require "google/cloud/spanner/admin/database"
    
    database_admin_client = Google::Cloud::Spanner::Admin::Database.database_admin
    
    instance_path = database_admin_client.instance_path project: project_id, instance: instance_id
    
    db_path = database_admin_client.database_path project: project_id,
                                                  instance: instance_id,
                                                  database: database_id
    
    job = database_admin_client.create_database parent: instance_path,
                                                create_statement: "CREATE DATABASE `#{database_id}`",
                                                extra_statements: [
                                                  "CREATE TABLE Singers (
                                       SingerId     INT64 NOT NULL,
                                       FirstName    STRING(1024),
                                       LastName     STRING(1024),
                                       SingerInfo   BYTES(MAX)
                                     ) PRIMARY KEY (SingerId)",
    
                                                  "CREATE TABLE Albums (
                                       SingerId     INT64 NOT NULL,
                                       AlbumId      INT64 NOT NULL,
                                       AlbumTitle   STRING(MAX)
                                     ) PRIMARY KEY (SingerId, AlbumId),
                                     INTERLEAVE IN PARENT Singers ON DELETE CASCADE"
                                                ],
                                                encryption_config: { kms_key_name: kms_key_name }
    
    puts "Waiting for create database operation to complete"
    
    job.wait_until_done!
    database = database_admin_client.get_database name: db_path
    
    puts "Database #{database_id} created with encryption key #{database.encryption_config.kms_key_name}"
    

To create a CMEK-enabled database in a multi-region instance configuration:
    
    
    # project_id  = "Your Google Cloud project ID"
    # instance_id = "Your Spanner instance ID"
    # database_id = "Your Spanner database ID"
    # kms_key_names = ["key1", "key2", "key3"]
    
    require "google/cloud/spanner"
    require "google/cloud/spanner/admin/database"
    
    database_admin_client = Google::Cloud::Spanner::Admin::Database.database_admin
    
    instance_path = database_admin_client.instance_path(
      project: project_id, instance: instance_id
    )
    
    encryption_config = {
      kms_key_names: kms_key_names
    }
    
    db_path = database_admin_client.database_path(
      project: project_id,
      instance: instance_id,
      database: database_id
    )
    
    job = database_admin_client.create_database(
      parent: instance_path,
      create_statement: "CREATE DATABASE `#{database_id}`",
      extra_statements: [
        <<~STATEMENT,
          CREATE TABLE Singers (
            SingerId    INT64 NOT NULL,
            FirstName   STRING(1024),
            LastName    STRING(1024),
            SingerInfo  BYTES(MAX)
          ) PRIMARY KEY (SingerId)
        STATEMENT
        <<~STATEMENT
          CREATE TABLE Albums (
            SingerId    INT64 NOT NULL,
            AlbumId     INT64 NOT NULL,
            AlbumTitle  STRING(MAX)
          ) PRIMARY KEY (SingerId, AlbumId),
          INTERLEAVE IN PARENT Singers
          ON DELETE CASCADE
        STATEMENT
      ],
      encryption_config: encryption_config
    )
    
    puts "Waiting for create database operation to complete"
    
    job.wait_until_done!
    database = database_admin_client.get_database name: db_path
    
    puts "Database #{database_id} created with encryption key " \
         "#{database.encryption_config.kms_key_names}"
    

## View the key versions in use

The database's [`encryption_info`](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases#Database.FIELDS.encryption_info) field shows information about key versions.

When a database's key version changes, the change isn't immediately propagated to `encryption_info`. There might be a delay before the change is reflected in this field.

### Console

  1. In the Google Cloud console, go to the **Instances** page.

[Go to Instances](https://console.cloud.google.com/spanner/instances)

  2. Click the instance containing the database you want to view.

  3. Click the database.

Encryption information is displayed on the **Database details** page.

![Screenshot of the encryption information that is displayed on the Database details page.](https://docs.cloud.google.com/static/spanner/docs/images/cmek-show-key.png)




###  gcloud 

You can get a database's `encryption_info` by running the [`gcloud spanner databases describe`](https://docs.cloud.google.com/sdk/gcloud/reference/spanner/databases/describe) or [`gcloud spanner databases list`](https://docs.cloud.google.com/sdk/gcloud/reference/spanner/databases/list) command. For example:
    
    
    gcloud spanner databases describe DATABASE \
        --project=SPANNER_PROJECT_ID \
        --instance=INSTANCE_ID

Here's an example output:
    
    
    name: projects/my-project/instances/test-instance/databases/example-db
    encryptionInfo:
    - encryptionType: CUSTOMER_MANAGED_ENCRYPTION
      kmsKeyVersion: projects/my-kms-project/locations/my-kms-key1-location/keyRings/my-kms-key-ring1/cryptoKeys/my-kms-key1/cryptoKeyVersions/1
    - encryptionType: CUSTOMER_MANAGED_ENCRYPTION
      kmsKeyVersion: projects/my-kms-project/locations/my-kms-key2-location/keyRings/my-kms-key-ring2/cryptoKeys/my-kms-key2/cryptoKeyVersions/1
    

## Disable the key

**Warning:** We strongly recommend against disabling only a subset of keys in a CMEK-enabled database that uses multiple keys. It might cause uncertain behavior. It's better to disable all keys in the database.

  1. Disable the key version(s) that are in use by following [these instructions](https://docs.cloud.google.com/kms/docs/enable-disable#disable) for each key version.

  2. Wait for the change to take effect. Disabling a key can take [up to three hours to propagate](https://docs.cloud.google.com/kms/docs/consistency).

  3. To confirm that the database is no longer accessible, execute a query in the CMEK-disabled database:
         
         gcloud spanner databases execute-sql DATABASE \
             --project=SPANNER_PROJECT_ID \
             --instance=INSTANCE_ID \
             --sql='SELECT * FROM Users'

The following error message appears: `KMS key required by the Spanner resource is not accessible.`




## Enable the key

  1. Enable the key versions that are in use by the database by following [these instructions](https://docs.cloud.google.com/kms/docs/enable-disable#enable) for each key version.

  2. Wait for the change to take effect. Enabling a key can take up to three hours to propagate.

  3. To confirm that the database is no longer accessible, execute a query in the CMEK-enabled database:
         
         gcloud spanner databases execute-sql DATABASE \
             --project=SPANNER_PROJECT_ID \
             --instance=INSTANCE_ID \
             --sql='SELECT * FROM Users'

If the change has taken effect, the command executes successfully.




## Back up a database

**Note:** You can't use the Google Cloud console to specify multiple Cloud KMS keys when creating a backup in a custom, dual-region or multi-region instance configuration. You must use the gcloud CLI or client libraries to do so.

You can use [Spanner backups](https://docs.cloud.google.com/spanner/docs/backup) to create backups of your databases. By default, Spanner backups created from a database use the same [encryption configuration](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.backups/create#CreateBackupEncryptionConfig) as the database itself. You can optionally specify a different encryption configuration for a backup.

### Console

Use the console to create backups in regional instance configurations.

  1. In the Google Cloud console, go to the **Instances** page.

[Go to Spanner Instances](https://console.cloud.google.com/spanner/instances)

  2. Click the instance name that contains the database that you want to back up.

  3. Click the database.

  4. In the navigation pane, click **Backup/Restore**.

  5. In the **Backups** tab, click **Create backup**.

  6. Enter a backup name and select an expiration date.

  7. Optional: Click **Show encryption options**.

a. If you want to use a different encryption configuration for your backup, click the slider next to **Use existing encryption**.

a. Select **Cloud KMS key**.

a. Select a key from the drop-down list.

The list of keys is limited to the current Google Cloud project. To use a key from a different Google Cloud project, create the database using gcloud CLI instead of the Google Cloud console.

  8. Click **Create**.




The **Backups** table displays encryption information for each backup.

![Screenshot of the Backups table showing the encryption information for each backup](https://docs.cloud.google.com/static/spanner/docs/images/cmek-backup-table.png)

###  gcloud 

To create a CMEK-enabled backup in a regional, custom, or multi-region instance configuration, run the [`gcloud spanner backups create`](https://docs.cloud.google.com/sdk/gcloud/reference/spanner/backups/create) command:
    
    
    gcloud spanner backups create BACKUP \
        --project=SPANNER_PROJECT_ID \
        --instance=INSTANCE_ID \
        --database=DATABASE  \
        --retention-period=RETENTION_PERIOD  \
        --encryption-type=customer_managed_encryption \
        --kms-project=KMS_PROJECT_ID \
        --kms-location=KMS_KEY_LOCATION \
        --kms-keyring=KMS_KEY_RING \
        --kms-keys=KMS_KEY_1[, KMS_KEY_2 ... ]
        --async

To verify that the backup created is CMEK encrypted:
    
    
    gcloud spanner backups describe BACKUP \
        --project=SPANNER_PROJECT_ID \
        --instance=INSTANCE_ID

###  Client libraries 

### C#

To create a CMEK-enabled backup in a regional instance configuration:
    
    
    using [Google.Cloud.Spanner.Admin.Database.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.html);
    using [Google.Cloud.Spanner.Common.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Common.V1/latest/Google.Cloud.Spanner.Common.V1.html);
    using [Google.Protobuf.WellKnownTypes](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.html);
    using System;
    using System.Threading.Tasks;
    
    public class CreateBackupWithEncryptionKeyAsyncSample
    {
        public async Task<Backup> CreateBackupWithEncryptionKeyAsync(string projectId, string instanceId, string databaseId, string backupId, [CryptoKeyName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.CryptoKeyName.html) kmsKeyName)
        {
            // Create a DatabaseAdminClient instance.
            [DatabaseAdminClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.DatabaseAdminClient.html) databaseAdminClient = [DatabaseAdminClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.DatabaseAdminClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.DatabaseAdminClient.html#Google_Cloud_Spanner_Admin_Database_V1_DatabaseAdminClient_Create)();
    
            // Create the CreateBackupRequest with encryption configuration.
            [CreateBackupRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.CreateBackupRequest.html) request = new [CreateBackupRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.CreateBackupRequest.html)
            {
                ParentAsInstanceName = [InstanceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Common.V1/latest/Google.Cloud.Spanner.Common.V1.InstanceName.html).[FromProjectInstance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Common.V1/latest/Google.Cloud.Spanner.Common.V1.InstanceName.html#Google_Cloud_Spanner_Common_V1_InstanceName_FromProjectInstance_System_String_System_String_)(projectId, instanceId),
                BackupId = backupId,
                Backup = new [Backup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.Backup.html)
                {
                    DatabaseAsDatabaseName = [DatabaseName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Common.V1/latest/Google.Cloud.Spanner.Common.V1.DatabaseName.html).[FromProjectInstanceDatabase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Common.V1/latest/Google.Cloud.Spanner.Common.V1.DatabaseName.html#Google_Cloud_Spanner_Common_V1_DatabaseName_FromProjectInstanceDatabase_System_String_System_String_System_String_)(projectId, instanceId, databaseId),
                    ExpireTime = DateTime.UtcNow.AddDays(14).[ToTimestamp](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.TimeExtensions.html#Google_Protobuf_WellKnownTypes_TimeExtensions_ToTimestamp_System_DateTime_)(),
                },
                EncryptionConfig = new [CreateBackupEncryptionConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.CreateBackupEncryptionConfig.html)
                {
                    EncryptionType = [CreateBackupEncryptionConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.CreateBackupEncryptionConfig.html).[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.CreateBackupEncryptionConfig.Types.html).[EncryptionType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.CreateBackupEncryptionConfig.Types.EncryptionType.html).[CustomerManagedEncryption](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.CreateBackupEncryptionConfig.Types.EncryptionType.html#Google_Cloud_Spanner_Admin_Database_V1_CreateBackupEncryptionConfig_Types_EncryptionType_CustomerManagedEncryption),
                    KmsKeyNameAsCryptoKeyName = kmsKeyName,
                },
            };
            // Execute the CreateBackup request.
            var operation = await databaseAdminClient.[CreateBackupAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.DatabaseAdminClient.html#Google_Cloud_Spanner_Admin_Database_V1_DatabaseAdminClient_CreateBackupAsync_Google_Cloud_Spanner_Admin_Database_V1_CreateBackupRequest_Google_Api_Gax_Grpc_CallSettings_)(request);
    
            Console.WriteLine("Waiting for the operation to finish.");
    
            // Poll until the returned long-running operation is complete.
            var completedResponse = await operation.PollUntilCompletedAsync();
            if (completedResponse.IsFaulted)
            {
                Console.WriteLine($"Error while creating backup: {completedResponse.Exception}");
                throw completedResponse.Exception;
            }
    
            var backup = completedResponse.Result;
            Console.WriteLine($"Backup {backup.Name} of size {backup.[SizeBytes](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.Backup.html#Google_Cloud_Spanner_Admin_Database_V1_Backup_SizeBytes)} bytes " +
                          $"was created at {backup.CreateTime} " +
                          $"using encryption key {kmsKeyName}");
            return backup;
        }
    }

To create a CMEK-enabled backup in a multi-region instance configuration:
    
    
    using [Google.Cloud.Spanner.Admin.Database.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.html);
    using [Google.Cloud.Spanner.Common.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Common.V1/latest/Google.Cloud.Spanner.Common.V1.html);
    using [Google.Protobuf.WellKnownTypes](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.html);
    using System;
    using System.Collections.Generic;
    using System.Threading.Tasks;
    
    public class CreateBackupWithMultiRegionEncryptionAsyncSample
    {
        public async Task<Backup> CreateBackupWithMultiRegionEncryptionAsync(string projectId, string instanceId, string databaseId, string backupId, IEnumerable<CryptoKeyName> kmsKeyNames)
        {
            // Create a DatabaseAdminClient instance.
            [DatabaseAdminClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.DatabaseAdminClient.html) databaseAdminClient = [DatabaseAdminClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.DatabaseAdminClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.DatabaseAdminClient.html#Google_Cloud_Spanner_Admin_Database_V1_DatabaseAdminClient_Create)();
    
            // Create the CreateBackupRequest with encryption configuration.
            [CreateBackupRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.CreateBackupRequest.html) request = new [CreateBackupRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.CreateBackupRequest.html)
            {
                ParentAsInstanceName = [InstanceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Common.V1/latest/Google.Cloud.Spanner.Common.V1.InstanceName.html).[FromProjectInstance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Common.V1/latest/Google.Cloud.Spanner.Common.V1.InstanceName.html#Google_Cloud_Spanner_Common_V1_InstanceName_FromProjectInstance_System_String_System_String_)(projectId, instanceId),
                BackupId = backupId,
                Backup = new [Backup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.Backup.html)
                {
                    DatabaseAsDatabaseName = [DatabaseName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Common.V1/latest/Google.Cloud.Spanner.Common.V1.DatabaseName.html).[FromProjectInstanceDatabase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Common.V1/latest/Google.Cloud.Spanner.Common.V1.DatabaseName.html#Google_Cloud_Spanner_Common_V1_DatabaseName_FromProjectInstanceDatabase_System_String_System_String_System_String_)(projectId, instanceId, databaseId),
                    ExpireTime = DateTime.UtcNow.AddDays(14).[ToTimestamp](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.TimeExtensions.html#Google_Protobuf_WellKnownTypes_TimeExtensions_ToTimestamp_System_DateTime_)(),
                },
                EncryptionConfig = new [CreateBackupEncryptionConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.CreateBackupEncryptionConfig.html)
                {
                    EncryptionType = [CreateBackupEncryptionConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.CreateBackupEncryptionConfig.html).[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.CreateBackupEncryptionConfig.Types.html).[EncryptionType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.CreateBackupEncryptionConfig.Types.EncryptionType.html).[CustomerManagedEncryption](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.CreateBackupEncryptionConfig.Types.EncryptionType.html#Google_Cloud_Spanner_Admin_Database_V1_CreateBackupEncryptionConfig_Types_EncryptionType_CustomerManagedEncryption),
                    KmsKeyNamesAsCryptoKeyNames = { kmsKeyNames },
                },
            };
            // Execute the CreateBackup request.
            var operation = await databaseAdminClient.[CreateBackupAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.DatabaseAdminClient.html#Google_Cloud_Spanner_Admin_Database_V1_DatabaseAdminClient_CreateBackupAsync_Google_Cloud_Spanner_Admin_Database_V1_CreateBackupRequest_Google_Api_Gax_Grpc_CallSettings_)(request);
    
            Console.WriteLine("Waiting for the operation to finish.");
    
            // Poll until the returned long-running operation is complete.
            var completedResponse = await operation.PollUntilCompletedAsync();
            if (completedResponse.IsFaulted)
            {
                Console.WriteLine($"Error while creating backup: {completedResponse.Exception}");
                throw completedResponse.Exception;
            }
    
            var backup = completedResponse.Result;
            Console.WriteLine($"Backup {backup.Name} of size {backup.[SizeBytes](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.Backup.html#Google_Cloud_Spanner_Admin_Database_V1_Backup_SizeBytes)} bytes was created with encryption keys {string.Join(", ", kmsKeyNames)} at {backup.CreateTime}");
            return backup;
        }
    }

### C++

To create a CMEK-enabled backup in a regional instance configuration:
    
    
    void CreateBackupWithEncryptionKey(
        google::cloud::spanner_admin::DatabaseAdminClient client,
        std::string const& project_id, std::string const& instance_id,
        std::string const& database_id, std::string const& backup_id,
        google::cloud::spanner::Timestamp expire_time,
        google::cloud::spanner::Timestamp version_time,
        google::cloud::KmsKeyName const& encryption_key) {
      google::cloud::spanner::Database database(project_id, instance_id,
                                                database_id);
      google::spanner::admin::database::v1::CreateBackupRequest request;
      request.set_parent(database.instance().FullName());
      request.set_backup_id(backup_id);
      request.mutable_backup()->set_database(database.FullName());
      *request.mutable_backup()->mutable_expire_time() =
          expire_time.get<google::protobuf::Timestamp>().value();
      *request.mutable_backup()->mutable_version_time() =
          version_time.get<google::protobuf::Timestamp>().value();
      request.mutable_encryption_config()->set_encryption_type(
          google::spanner::admin::database::v1::CreateBackupEncryptionConfig::
              CUSTOMER_MANAGED_ENCRYPTION);
      request.mutable_encryption_config()->set_kms_key_name(
          encryption_key.FullName());
      auto backup = client.CreateBackup(request).get();
      if (!backup) throw std::move(backup).status();
      std::cout
          << "Backup " << backup->name() << " of " << backup->database()
          << " of size " << backup->size_bytes() << " bytes as of "
          << google::cloud::spanner::MakeTimestamp(backup->version_time()).value()
          << " was created at "
          << google::cloud::spanner::MakeTimestamp(backup->create_time()).value()
          << " using encryption key " << encryption_key.FullName() << ".\n";
    }

To create a CMEK-enabled backup in a multi-region instance configuration:
    
    
    void CreateBackupWithMRCMEK(
        google::cloud::spanner_admin::DatabaseAdminClient client,
        BackupIdentifier dst, std::string const& database_id,
        google::cloud::spanner::Timestamp expire_time,
        google::cloud::spanner::Timestamp version_time,
        std::vector<google::cloud::KmsKeyName> const& encryption_keys) {
      google::cloud::spanner::Database database(dst.project_id, dst.instance_id,
                                                database_id);
      google::spanner::admin::database::v1::CreateBackupRequest request;
      request.set_parent(database.instance().FullName());
      request.set_backup_id(dst.backup_id);
      request.mutable_backup()->set_database(database.FullName());
      *request.mutable_backup()->mutable_expire_time() =
          expire_time.get<google::protobuf::Timestamp>().value();
      *request.mutable_backup()->mutable_version_time() =
          version_time.get<google::protobuf::Timestamp>().value();
      request.mutable_encryption_config()->set_encryption_type(
          google::spanner::admin::database::v1::CreateBackupEncryptionConfig::
              CUSTOMER_MANAGED_ENCRYPTION);
      for (google::cloud::KmsKeyName const& encryption_key : encryption_keys) {
        request.mutable_encryption_config()->add_kms_key_names(
            encryption_key.FullName());
      }
      auto backup = client.CreateBackup(request).get();
      if (!backup) throw std::move(backup).status();
      std::cout
          << "Backup " << backup->name() << " of " << backup->database()
          << " of size " << backup->size_bytes() << " bytes as of "
          << google::cloud::spanner::MakeTimestamp(backup->version_time()).value()
          << " was created at "
          << google::cloud::spanner::MakeTimestamp(backup->create_time()).value();
      PrintKmsKeys(encryption_keys);
    }

### Go

To create a CMEK-enabled backup in a regional instance configuration:
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    	"regexp"
    	"time"
    
    	database "cloud.google.com/go/spanner/admin/database/apiv1"
    	adminpb "cloud.google.com/go/spanner/admin/database/apiv1/databasepb"
    	pbt "github.com/golang/protobuf/ptypes/timestamp"
    )
    
    func createBackupWithCustomerManagedEncryptionKey(ctx context.Context, w io.Writer, db, backupID, kmsKeyName string) error {
    	// db = `projects/<project>/instances/<instance-id>/database/<database-id>`
    	// backupID = `my-backup-id`
    	// kmsKeyName = `projects/<project>/locations/<location>/keyRings/<key_ring>/cryptoKeys/<kms_key_name>`
    	matches := regexp.MustCompile("^(.+)/databases/(.+)$").FindStringSubmatch(db)
    	if matches == nil || len(matches) != 3 {
    		return fmt.Errorf("createBackupWithCustomerManagedEncryptionKey: invalid database id %q", db)
    	}
    	instanceName := matches[1]
    
    	adminClient, err := database.NewDatabaseAdminClient(ctx)
    	if err != nil {
    		return fmt.Errorf("createBackupWithCustomerManagedEncryptionKey.NewDatabaseAdminClient: %w", err)
    	}
    	defer adminClient.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/spanner/latest/admin/database/apiv1.html#cloud_google_com_go_spanner_admin_database_apiv1_DatabaseAdminClient_Close)()
    
    	expireTime := time.Now().AddDate(0, 0, 14)
    	// Create a backup for a database using a Customer Managed Encryption Key
    	req := adminpb.CreateBackupRequest{
    		Parent:   instanceName,
    		BackupId: backupID,
    		Backup: &adminpb.Backup{
    			Database:   db,
    			ExpireTime: &pbt.Timestamp{Seconds: expireTime.Unix(), Nanos: int32(expireTime.Nanosecond())},
    		},
    		EncryptionConfig: &adminpb.CreateBackupEncryptionConfig{
    			KmsKeyName:     kmsKeyName,
    			EncryptionType: adminpb.CreateBackupEncryptionConfig_CUSTOMER_MANAGED_ENCRYPTION,
    		},
    	}
    	op, err := adminClient.CreateBackup(ctx, &req)
    	if err != nil {
    		return fmt.Errorf("createBackupWithCustomerManagedEncryptionKey.CreateBackup: %w", err)
    	}
    	// Wait for backup operation to complete.
    	backup, err := op.Wait(ctx)
    	if err != nil {
    		return fmt.Errorf("createBackupWithCustomerManagedEncryptionKey.Wait: %w", err)
    	}
    
    	// Get the name, create time, backup size and encryption key from the backup.
    	backupCreateTime := time.Unix(backup.CreateTime.Seconds, int64(backup.CreateTime.Nanos))
    	fmt.Fprintf(w,
    		"Backup %s of size %d bytes was created at %s using encryption key %s\n",
    		backup.Name,
    		backup.SizeBytes,
    		backupCreateTime.Format(time.RFC3339),
    		kmsKeyName)
    	return nil
    }
    

To create a CMEK-enabled backup in a multi-region instance configuration:
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    	"time"
    
    	database "cloud.google.com/go/spanner/admin/database/apiv1"
    	adminpb "cloud.google.com/go/spanner/admin/database/apiv1/databasepb"
    	pbt "github.com/golang/protobuf/ptypes/timestamp"
    )
    
    // createBackupWithCustomerManagedMultiRegionEncryptionKey creates a backup for a database using a Customer Managed Multi-Region Encryption Key.
    func createBackupWithCustomerManagedMultiRegionEncryptionKey(ctx context.Context, w io.Writer, projectID, instanceID, databaseID, backupID string, kmsKeyNames []string) error {
    	// projectID = `my-project`
    	// instanceID = `my-instance`
    	// databaseID = `my-database`
    	// backupID = `my-backup-id`
    	// kmsKeyNames := []string{"projects/my-project/locations/locations/<location1>/keyRings/<keyRing>/cryptoKeys/<keyId>",
    	//	 "projects/my-project/locations/locations/<location2>/keyRings/<keyRing>/cryptoKeys/<keyId>",
    	//	 "projects/my-project/locations/locations/<location3>/keyRings/<keyRing>/cryptoKeys/<keyId>",
    	// }
    
    	adminClient, err := database.NewDatabaseAdminClient(ctx)
    	if err != nil {
    		return fmt.Errorf("createBackupWithCustomerManagedMultiRegionEncryptionKey.NewDatabaseAdminClient: %w", err)
    	}
    	defer adminClient.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/spanner/latest/admin/database/apiv1.html#cloud_google_com_go_spanner_admin_database_apiv1_DatabaseAdminClient_Close)()
    
    	expireTime := time.Now().AddDate(0, 0, 14)
    	// Create a backup for a database using a Customer Managed Encryption Key
    	req := adminpb.CreateBackupRequest{
    		Parent:   fmt.Sprintf("projects/%s/instances/%s", projectID, instanceID),
    		BackupId: backupID,
    		Backup: &adminpb.Backup{
    			Database:   fmt.Sprintf("projects/%s/instances/%s/databases/%s", projectID, instanceID, databaseID),
    			ExpireTime: &pbt.Timestamp{Seconds: expireTime.Unix(), Nanos: int32(expireTime.Nanosecond())},
    		},
    		EncryptionConfig: &adminpb.CreateBackupEncryptionConfig{
    			KmsKeyNames:    kmsKeyNames,
    			EncryptionType: adminpb.CreateBackupEncryptionConfig_CUSTOMER_MANAGED_ENCRYPTION,
    		},
    	}
    	op, err := adminClient.CreateBackup(ctx, &req)
    	if err != nil {
    		return fmt.Errorf("createBackupWithCustomerManagedMultiRegionEncryptionKey.CreateBackup: %w", err)
    	}
    	// Wait for backup operation to complete.
    	backup, err := op.Wait(ctx)
    	if err != nil {
    		return fmt.Errorf("createBackupWithCustomerManagedMultiRegionEncryptionKey.Wait: %w", err)
    	}
    
    	// Get the name, create time, backup size and encryption key from the backup.
    	backupCreateTime := time.Unix(backup.CreateTime.Seconds, int64(backup.CreateTime.Nanos))
    	fmt.Fprintf(w,
    		"Backup %s of size %d bytes was created at %s using multi-region encryption keys %q\n",
    		backup.Name,
    		backup.SizeBytes,
    		backupCreateTime.Format(time.RFC3339),
    		kmsKeyNames)
    	return nil
    }
    

### Java

To create a CMEK-enabled backup in a regional instance configuration:
    
    
    import com.google.cloud.spanner.[Spanner](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.Spanner.html);
    import com.google.cloud.spanner.[SpannerExceptionFactory](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.SpannerExceptionFactory.html);
    import com.google.cloud.spanner.[SpannerOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.SpannerOptions.html);
    import com.google.cloud.spanner.admin.database.v1.[DatabaseAdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.admin.database.v1.DatabaseAdminClient.html);
    import com.google.protobuf.[Timestamp](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html);
    import com.google.spanner.admin.database.v1.[Backup](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.Backup.html);
    import com.google.spanner.admin.database.v1.[BackupName](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.BackupName.html);
    import com.google.spanner.admin.database.v1.[CreateBackupEncryptionConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.CreateBackupEncryptionConfig.html);
    import com.google.spanner.admin.database.v1.[CreateBackupEncryptionConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.CreateBackupEncryptionConfig.html).EncryptionType;
    import com.google.spanner.admin.database.v1.[CreateBackupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.CreateBackupRequest.html);
    import com.google.spanner.admin.database.v1.[DatabaseName](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.DatabaseName.html);
    import com.google.spanner.admin.database.v1.[InstanceName](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.InstanceName.html);
    import java.util.concurrent.ExecutionException;
    import java.util.concurrent.TimeUnit;
    import java.util.concurrent.TimeoutException;
    import org.threeten.bp.LocalDateTime;
    import org.threeten.bp.OffsetDateTime;
    
    public class CreateBackupWithEncryptionKey {
    
      static void createBackupWithEncryptionKey() {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "my-project";
        String instanceId = "my-instance";
        String databaseId = "my-database";
        String backupId = "my-backup";
        String kmsKeyName =
            "projects/" + projectId + "/locations/<location>/keyRings/<keyRing>/cryptoKeys/<keyId>";
    
        try ([Spanner](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.Spanner.html) spanner =
            [SpannerOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.SpannerOptions.html).newBuilder().setProjectId(projectId).build().getService();
            [DatabaseAdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.admin.database.v1.DatabaseAdminClient.html) adminClient = spanner.[createDatabaseAdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.Spanner.html#com_google_cloud_spanner_Spanner_createDatabaseAdminClient__)()) {
          createBackupWithEncryptionKey(
              adminClient,
              projectId,
              instanceId,
              databaseId,
              backupId,
              kmsKeyName);
        }
      }
    
      static Void createBackupWithEncryptionKey([DatabaseAdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.admin.database.v1.DatabaseAdminClient.html) adminClient,
          String projectId, String instanceId, String databaseId, String backupId, String kmsKeyName) {
        // Set expire time to 14 days from now.
        final [Timestamp](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html) expireTime =
            [Timestamp](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html).newBuilder().setSeconds(TimeUnit.MILLISECONDS.toSeconds((
                System.currentTimeMillis() + TimeUnit.DAYS.toMillis(14)))).build();
        final [BackupName](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.BackupName.html) backupName = [BackupName](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.BackupName.html).of(projectId, instanceId, backupId);
        [Backup](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.Backup.html) backup = [Backup](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.Backup.html).newBuilder()
            .setName(backupName.[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.BackupName.html#com_google_spanner_admin_database_v1_BackupName_toString__)())
            .setDatabase([DatabaseName](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.DatabaseName.html).of(projectId, instanceId, databaseId).toString())
            .setExpireTime(expireTime).build();
    
        final [CreateBackupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.CreateBackupRequest.html) request =
            [CreateBackupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.CreateBackupRequest.html).newBuilder()
                .setParent([InstanceName](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.InstanceName.html).of(projectId, instanceId).toString())
                .setBackupId(backupId)
                .setBackup(backup)
                .setEncryptionConfig(
                    [CreateBackupEncryptionConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.CreateBackupEncryptionConfig.html).newBuilder()
                        .setEncryptionType(EncryptionType.CUSTOMER_MANAGED_ENCRYPTION)
                        .setKmsKeyName(kmsKeyName).build()).build();
        try {
          System.out.println("Waiting for operation to complete...");
          backup = adminClient.[createBackupAsync](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.admin.database.v1.DatabaseAdminClient.html#com_google_cloud_spanner_admin_database_v1_DatabaseAdminClient_createBackupAsync__org_jspecify_annotations_Nullable_com_google_spanner_admin_database_v1_InstanceName_com_google_spanner_admin_database_v1_Backup_java_lang_String_)(request).get(1200, TimeUnit.SECONDS);
        } catch (ExecutionException e) {
          // If the operation failed during execution, expose the cause.
          throw [SpannerExceptionFactory](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.SpannerExceptionFactory.html).[asSpannerException](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.SpannerExceptionFactory.html#com_google_cloud_spanner_SpannerExceptionFactory_asSpannerException_java_lang_Throwable_)(e.getCause());
        } catch (InterruptedException e) {
          // Throw when a thread is waiting, sleeping, or otherwise occupied,
          // and the thread is interrupted, either before or during the activity.
          throw [SpannerExceptionFactory](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.SpannerExceptionFactory.html).[propagateInterrupt](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.SpannerExceptionFactory.html#com_google_cloud_spanner_SpannerExceptionFactory_propagateInterrupt_java_lang_InterruptedException_)(e);
        } catch (TimeoutException e) {
          // If the operation timed out propagates the timeout
          throw [SpannerExceptionFactory](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.SpannerExceptionFactory.html).[propagateTimeout](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.SpannerExceptionFactory.html#com_google_cloud_spanner_SpannerExceptionFactory_propagateTimeout_java_util_concurrent_TimeoutException_)(e);
        }
        System.out.printf(
            "Backup %s of size %d bytes was created at %s using encryption key %s%n",
            [backup](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.Database.html#com_google_cloud_spanner_Database_backup_com_google_cloud_spanner_Backup_).[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.Backup.html#com_google_spanner_admin_database_v1_Backup_getName__)(),
            [backup](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.Database.html#com_google_cloud_spanner_Database_backup_com_google_cloud_spanner_Backup_).[getSizeBytes](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.Backup.html#com_google_spanner_admin_database_v1_Backup_getSizeBytes__)(),
            LocalDateTime.ofEpochSecond(
                [backup](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.Database.html#com_google_cloud_spanner_Database_backup_com_google_cloud_spanner_Backup_).[getCreateTime](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.Backup.html#com_google_spanner_admin_database_v1_Backup_getCreateTime__)().getSeconds(),
                [backup](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.Database.html#com_google_cloud_spanner_Database_backup_com_google_cloud_spanner_Backup_).[getCreateTime](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.Backup.html#com_google_spanner_admin_database_v1_Backup_getCreateTime__)().getNanos(),
                OffsetDateTime.now().getOffset()),
            kmsKeyName
        );
    
        return null;
      }
    }

To create a CMEK-enabled backup in a multi-region instance configuration:
    
    
    import com.google.cloud.spanner.[Spanner](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.Spanner.html);
    import com.google.cloud.spanner.[SpannerExceptionFactory](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.SpannerExceptionFactory.html);
    import com.google.cloud.spanner.[SpannerOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.SpannerOptions.html);
    import com.google.cloud.spanner.admin.database.v1.[DatabaseAdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.admin.database.v1.DatabaseAdminClient.html);
    import com.google.common.collect.ImmutableList;
    import com.google.protobuf.[Timestamp](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html);
    import com.google.spanner.admin.database.v1.[Backup](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.Backup.html);
    import com.google.spanner.admin.database.v1.[BackupName](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.BackupName.html);
    import com.google.spanner.admin.database.v1.[CreateBackupEncryptionConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.CreateBackupEncryptionConfig.html);
    import com.google.spanner.admin.database.v1.[CreateBackupEncryptionConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.CreateBackupEncryptionConfig.html).EncryptionType;
    import com.google.spanner.admin.database.v1.[CreateBackupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.CreateBackupRequest.html);
    import com.google.spanner.admin.database.v1.[DatabaseName](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.DatabaseName.html);
    import com.google.spanner.admin.database.v1.[InstanceName](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.InstanceName.html);
    import java.util.concurrent.ExecutionException;
    import java.util.concurrent.TimeUnit;
    import java.util.concurrent.TimeoutException;
    import org.threeten.bp.LocalDateTime;
    import org.threeten.bp.OffsetDateTime;
    
    public class CreateBackupWithMultiRegionEncryptionKey {
    
      static void createBackupWithMultiRegionEncryptionKey() {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "my-project";
        String instanceId = "my-instance";
        String databaseId = "my-database";
        String backupId = "my-backup";
        String[] kmsKeyNames =
            new String[] {
              "projects/" + projectId + "/locations/<location1>/keyRings/<keyRing>/cryptoKeys/<keyId>",
              "projects/" + projectId + "/locations/<location2>/keyRings/<keyRing>/cryptoKeys/<keyId>",
              "projects/" + projectId + "/locations/<location3>/keyRings/<keyRing>/cryptoKeys/<keyId>"
            };
    
        try ([Spanner](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.Spanner.html) spanner =
                [SpannerOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.SpannerOptions.html).newBuilder().setProjectId(projectId).build().getService();
            [DatabaseAdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.admin.database.v1.DatabaseAdminClient.html) adminClient = spanner.[createDatabaseAdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.Spanner.html#com_google_cloud_spanner_Spanner_createDatabaseAdminClient__)()) {
          createBackupWithMultiRegionEncryptionKey(
              adminClient, projectId, instanceId, databaseId, backupId, kmsKeyNames);
        }
      }
    
      static Void createBackupWithMultiRegionEncryptionKey(
          [DatabaseAdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.admin.database.v1.DatabaseAdminClient.html) adminClient,
          String projectId,
          String instanceId,
          String databaseId,
          String backupId,
          String[] kmsKeyNames) {
        // Set expire time to 14 days from now.
        final [Timestamp](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html) expireTime =
            [Timestamp](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html).newBuilder()
                .setSeconds(
                    TimeUnit.MILLISECONDS.toSeconds(
                        (System.currentTimeMillis() + TimeUnit.DAYS.toMillis(14))))
                .build();
        final [BackupName](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.BackupName.html) backupName = [BackupName](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.BackupName.html).of(projectId, instanceId, backupId);
        [Backup](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.Backup.html) backup =
            [Backup](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.Backup.html).newBuilder()
                .setName(backupName.[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.BackupName.html#com_google_spanner_admin_database_v1_BackupName_toString__)())
                .setDatabase([DatabaseName](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.DatabaseName.html).of(projectId, instanceId, databaseId).toString())
                .setExpireTime(expireTime)
                .build();
    
        final [CreateBackupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.CreateBackupRequest.html) request =
            [CreateBackupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.CreateBackupRequest.html).newBuilder()
                .setParent([InstanceName](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.InstanceName.html).of(projectId, instanceId).toString())
                .setBackupId(backupId)
                .setBackup(backup)
                .setEncryptionConfig(
                    [CreateBackupEncryptionConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.CreateBackupEncryptionConfig.html).newBuilder()
                        .setEncryptionType(EncryptionType.CUSTOMER_MANAGED_ENCRYPTION)
                        .addAllKmsKeyNames(ImmutableList.copyOf(kmsKeyNames))
                        .build())
                .build();
        try {
          System.out.println("Waiting for operation to complete...");
          backup = adminClient.[createBackupAsync](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.admin.database.v1.DatabaseAdminClient.html#com_google_cloud_spanner_admin_database_v1_DatabaseAdminClient_createBackupAsync__org_jspecify_annotations_Nullable_com_google_spanner_admin_database_v1_InstanceName_com_google_spanner_admin_database_v1_Backup_java_lang_String_)(request).get(1200, TimeUnit.SECONDS);
        } catch (ExecutionException e) {
          // If the operation failed during execution, expose the cause.
          throw [SpannerExceptionFactory](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.SpannerExceptionFactory.html).[asSpannerException](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.SpannerExceptionFactory.html#com_google_cloud_spanner_SpannerExceptionFactory_asSpannerException_java_lang_Throwable_)(e.getCause());
        } catch (InterruptedException e) {
          // Throw when a thread is waiting, sleeping, or otherwise occupied,
          // and the thread is interrupted, either before or during the activity.
          throw [SpannerExceptionFactory](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.SpannerExceptionFactory.html).[propagateInterrupt](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.SpannerExceptionFactory.html#com_google_cloud_spanner_SpannerExceptionFactory_propagateInterrupt_java_lang_InterruptedException_)(e);
        } catch (TimeoutException e) {
          // If the operation timed out propagates the timeout
          throw [SpannerExceptionFactory](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.SpannerExceptionFactory.html).[propagateTimeout](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.SpannerExceptionFactory.html#com_google_cloud_spanner_SpannerExceptionFactory_propagateTimeout_java_util_concurrent_TimeoutException_)(e);
        }
        System.out.printf(
            "Backup %s of size %d bytes was created at %s using encryption keys %s%n",
            [backup](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.Database.html#com_google_cloud_spanner_Database_backup_com_google_cloud_spanner_Backup_).[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.Backup.html#com_google_spanner_admin_database_v1_Backup_getName__)(),
            [backup](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.Database.html#com_google_cloud_spanner_Database_backup_com_google_cloud_spanner_Backup_).[getSizeBytes](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.Backup.html#com_google_spanner_admin_database_v1_Backup_getSizeBytes__)(),
            LocalDateTime.ofEpochSecond(
                [backup](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.Database.html#com_google_cloud_spanner_Database_backup_com_google_cloud_spanner_Backup_).[getCreateTime](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.Backup.html#com_google_spanner_admin_database_v1_Backup_getCreateTime__)().getSeconds(),
                [backup](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.Database.html#com_google_cloud_spanner_Database_backup_com_google_cloud_spanner_Backup_).[getCreateTime](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.Backup.html#com_google_spanner_admin_database_v1_Backup_getCreateTime__)().getNanos(),
                OffsetDateTime.now().getOffset()),
            ImmutableList.copyOf(kmsKeyNames));
    
        return null;
      }
    }

**Note:** The old client library interface code samples for Java are archived in [GitHub](https://github.com/googleapis/google-cloud-java/tree/main/java-spanner/samples/snippets/src/main/java/com/example/spanner/admin/archived). 

### Node.js

To create a CMEK-enabled backup in a regional instance configuration:
    
    
    // Imports the Google Cloud client library
    const {Spanner, protos} = require('[@google-cloud/spanner](https://docs.cloud.google.com/nodejs/docs/reference/spanner/latest/overview.html)');
    const {PreciseDate} = require('[@google-cloud/precise-date](https://docs.cloud.google.com/nodejs/docs/reference/precise-date/latest/overview.html)');
    
    /**
     * TODO(developer): Uncomment the following lines before running the sample.
     */
    // const projectId = 'my-project-id';
    // const instanceId = 'my-instance';
    // const databaseId = 'my-database';
    // const backupId = 'my-backup';
    // const keyName =
    //   'projects/my-project-id/my-region/keyRings/my-key-ring/cryptoKeys/my-key';
    
    // Creates a client
    const spanner = new [Spanner](https://docs.cloud.google.com/nodejs/docs/reference/spanner/latest/spanner/spanner.html)({
      projectId: projectId,
    });
    
    // Gets a reference to a Cloud Spanner Database Admin Client object
    const databaseAdminClient = spanner.[getDatabaseAdminClient](https://docs.cloud.google.com/nodejs/docs/reference/spanner/latest/spanner/spanner.html)();
    
    // Creates a new backup of the database
    try {
      console.log(
        `Creating backup of database ${databaseAdminClient.databasePath(
          projectId,
          instanceId,
          databaseId,
        )}.`,
      );
    
      // Expire backup 14 days in the future
      const expireTime = Date.now() + 1000 * 60 * 60 * 24 * 14;
    
      // Create a backup of the state of the database at the current time.
      const [operation] = await databaseAdminClient.createBackup({
        parent: databaseAdminClient.instancePath(projectId, instanceId),
        backupId: backupId,
        backup: (protos.google.spanner.admin.database.v1.[Backup](https://docs.cloud.google.com/nodejs/docs/reference/spanner-api/latest/spanner-api/protos.google.spanner.admin.database.v1.backup-class.html) = {
          database: databaseAdminClient.databasePath(
            projectId,
            instanceId,
            databaseId,
          ),
          expireTime: [Spanner](https://docs.cloud.google.com/nodejs/docs/reference/spanner/latest/spanner/spanner.html).[timestamp](https://docs.cloud.google.com/nodejs/docs/reference/spanner/latest/spanner/spanner.html)(expireTime).[toStruct](https://docs.cloud.google.com/nodejs/docs/reference/precise-date/latest/precise-date/precisedate.html)(),
          name: databaseAdminClient.backupPath(projectId, instanceId, backupId),
        }),
        encryptionConfig: {
          encryptionType: 'CUSTOMER_MANAGED_ENCRYPTION',
          kmsKeyName: keyName,
        },
      });
    
      console.log(
        `Waiting for backup ${databaseAdminClient.backupPath(
          projectId,
          instanceId,
          backupId,
        )} to complete...`,
      );
      await operation.promise();
    
      // Verify backup is ready
      const [backupInfo] = await databaseAdminClient.getBackup({
        name: databaseAdminClient.backupPath(projectId, instanceId, backupId),
      });
      if (backupInfo.state === 'READY') {
        console.log(
          `Backup ${backupInfo.name} of size ` +
            `${backupInfo.sizeBytes} bytes was created at ` +
            `${new [PreciseDate](https://docs.cloud.google.com/nodejs/docs/reference/precise-date/latest/precise-date/precisedate.html)(backupInfo.createTime).[toISOString](https://docs.cloud.google.com/nodejs/docs/reference/precise-date/latest/precise-date/precisedate.html)()} ` +
            `using encryption key ${backupInfo.encryptionInfo.kmsKeyVersion}`,
        );
      } else {
        console.error('ERROR: Backup is not ready.');
      }
    } catch (err) {
      console.error('ERROR:', err);
    } finally {
      // Close the spanner client when finished.
      // The databaseAdminClient does not require explicit closure. The closure of the Spanner client will automatically close the databaseAdminClient.
      spanner.close();
    }

To create a CMEK-enabled backup in a multi-region instance configuration:
    
    
    /**
     * TODO(developer): Uncomment the following lines before running the sample.
     */
    // const projectId = 'my-project-id';
    // const instanceId = 'my-instance';
    // const databaseId = 'my-database';
    // const backupId = 'my-backup';
    // const kmsKeyNames =
    //   'projects/my-project-id/my-region/keyRings/my-key-ring/cryptoKeys/my-key1,
    //   'projects/my-project-id/my-region/keyRings/my-key-ring/cryptoKeys/my-key2';
    
    // Imports the Google Cloud client library
    const {Spanner, protos} = require('[@google-cloud/spanner](https://docs.cloud.google.com/nodejs/docs/reference/spanner/latest/overview.html)');
    const {PreciseDate} = require('[@google-cloud/precise-date](https://docs.cloud.google.com/nodejs/docs/reference/precise-date/latest/overview.html)');
    
    // Creates a client
    const spanner = new [Spanner](https://docs.cloud.google.com/nodejs/docs/reference/spanner/latest/spanner/spanner.html)({
      projectId: projectId,
    });
    
    // Gets a reference to a Cloud Spanner Database Admin Client object
    const databaseAdminClient = spanner.[getDatabaseAdminClient](https://docs.cloud.google.com/nodejs/docs/reference/spanner/latest/spanner/spanner.html)();
    async function createBackupWithMultipleKmsKeys() {
      // Creates a new backup of the database
      try {
        console.log(
          `Creating backup of database ${databaseAdminClient.databasePath(
            projectId,
            instanceId,
            databaseId,
          )}.`,
        );
    
        // Expire backup 14 days in the future
        const expireTime = Date.now() + 1000 * 60 * 60 * 24 * 14;
    
        // Create a backup of the state of the database at the current time.
        const [operation] = await databaseAdminClient.createBackup({
          parent: databaseAdminClient.instancePath(projectId, instanceId),
          backupId: backupId,
          backup: (protos.google.spanner.admin.database.v1.[Backup](https://docs.cloud.google.com/nodejs/docs/reference/spanner-api/latest/spanner-api/protos.google.spanner.admin.database.v1.backup-class.html) = {
            database: databaseAdminClient.databasePath(
              projectId,
              instanceId,
              databaseId,
            ),
            expireTime: [Spanner](https://docs.cloud.google.com/nodejs/docs/reference/spanner/latest/spanner/spanner.html).[timestamp](https://docs.cloud.google.com/nodejs/docs/reference/spanner/latest/spanner/spanner.html)(expireTime).[toStruct](https://docs.cloud.google.com/nodejs/docs/reference/precise-date/latest/precise-date/precisedate.html)(),
            name: databaseAdminClient.backupPath(projectId, instanceId, backupId),
          }),
          encryptionConfig: {
            encryptionType: 'CUSTOMER_MANAGED_ENCRYPTION',
            kmsKeyNames: kmsKeyNames.split(','),
          },
        });
    
        console.log(
          `Waiting for backup ${databaseAdminClient.backupPath(
            projectId,
            instanceId,
            backupId,
          )} to complete...`,
        );
        await operation.promise();
    
        // Verify backup is ready
        const [backupInfo] = await databaseAdminClient.getBackup({
          name: databaseAdminClient.backupPath(projectId, instanceId, backupId),
        });
    
        const kmsKeyVersions = backupInfo.encryptionInformation
          .map(encryptionInfo => encryptionInfo.kmsKeyVersion)
          .join(', ');
    
        if (backupInfo.state === 'READY') {
          console.log(
            `Backup ${backupInfo.name} of size ` +
              `${backupInfo.sizeBytes} bytes was created at ` +
              `${new [PreciseDate](https://docs.cloud.google.com/nodejs/docs/reference/precise-date/latest/precise-date/precisedate.html)(backupInfo.createTime).[toISOString](https://docs.cloud.google.com/nodejs/docs/reference/precise-date/latest/precise-date/precisedate.html)()} ` +
              `using encryption key ${kmsKeyVersions}`,
          );
        } else {
          console.error('ERROR: Backup is not ready.');
        }
      } catch (err) {
        console.error('ERROR:', err);
      } finally {
        // Close the spanner client when finished.
        // The databaseAdminClient does not require explicit closure. The closure of the Spanner client will automatically close the databaseAdminClient.
        spanner.close();
      }
    }
    createBackupWithMultipleKmsKeys();

**Note:** The old client library interface code samples for Node.js are archived in [GitHub](https://github.com/googleapis/nodejs-spanner/tree/main/samples/archived). 

### PHP

To create a CMEK-enabled backup in a regional instance configuration:
    
    
    use Google\Cloud\Spanner\Admin\Database\V1\Backup;
    use \Google\Cloud\Spanner\Admin\Database\V1\Backup\State;
    use Google\Cloud\Spanner\Admin\Database\V1\Client\DatabaseAdminClient;
    use Google\Cloud\Spanner\Admin\Database\V1\CreateBackupEncryptionConfig;
    use Google\Cloud\Spanner\Admin\Database\V1\CreateBackupRequest;
    use Google\Cloud\Spanner\Admin\Database\V1\GetBackupRequest;
    use Google\Protobuf\Timestamp;
    
    /**
     * Create an encrypted backup.
     * Example:
     * ```
     * create_backup_with_encryption_key($projectId, $instanceId, $databaseId, $backupId, $kmsKeyName);
     * ```
     *
     * @param string $projectId The Google Cloud project ID.
     * @param string $instanceId The Spanner instance ID.
     * @param string $databaseId The Spanner database ID.
     * @param string $backupId The Spanner backup ID.
     * @param string $kmsKeyName The KMS key used for encryption.
     */
    function create_backup_with_encryption_key(
        string $projectId,
        string $instanceId,
        string $databaseId,
        string $backupId,
        string $kmsKeyName
    ): void {
        $databaseAdminClient = new DatabaseAdminClient();
        $instanceFullName = DatabaseAdminClient::instanceName($projectId, $instanceId);
        $databaseFullName = DatabaseAdminClient::databaseName($projectId, $instanceId, $databaseId);
        $expireTime = new Timestamp();
        $expir>eTime-setSeconds((new \DateTime('+14 da>ys'))-getTimestamp());
        $request = new CreateBackupRequest([
            'par>ent' = $instanceFullName,
            'backup>_id' = $backupId,
            'encryption_con>fig' = new CreateBackupEncryptionConfig([
                'kms_key_n>ame' = $kmsKeyName,
                'encryption_t>ype' = CreateBackupEncryptionConfig\EncryptionType::CUSTOMER_MANAGED_ENCRYPTION
            ]),
            'bac>kup' = new Backup([
                'datab>ase' = $databaseFullName,
                'expire_t>ime' = $expireTime
            ])
        ]);
    
        $operation = $databaseAdminC>lient-createBackup($request);
    
        print('Waiting for operation to complete...' . PHP_EOL);
        $oper>ation-pollUntilComplete();
    
        $request = new GetBackupRequest();
        $re>quest-setName($databaseAdminC>lient-backupName($projectId, $instanceId, $backupId));
        $info = $databaseAdminC>lient-getBackup($request);
        if (State::name(>$info-getState()) == 'READY') {
            printf(
                'Backup %s of size %d bytes was created at %d using encryption key %s' . PHP_EOL,
                basename(>$info-getName()),
                >$info-getSizeBytes(),
                >$info-getCreateT>ime()-getSeconds(),
                >$info-getEncryptionI>nfo()-getKmsKeyVersion()
            );
        } else {
            print('Backup is not ready!' . PHP_EOL);
        }
    }

To create a CMEK-enabled backup in a multi-region instance configuration:
    
    
    use Google\Cloud\Spanner\Admin\Database\V1\Backup;
    use \Google\Cloud\Spanner\Admin\Database\V1\Backup\State;
    use Google\Cloud\Spanner\Admin\Database\V1\Client\DatabaseAdminClient;
    use Google\Cloud\Spanner\Admin\Database\V1\CreateBackupEncryptionConfig;
    use Google\Cloud\Spanner\Admin\Database\V1\CreateBackupRequest;
    use Google\Cloud\Spanner\Admin\Database\V1\GetBackupRequest;
    use Google\Protobuf\Timestamp;
    
    /**
     * Create a CMEK backup.
     * Example:
     * ```
     * create_backup_with_mr_cmek($projectId, $instanceId, $databaseId, $backupId, $kmsKeyNames);
     * ```
     *
     * @param string $projectId The Google Cloud project ID.
     * @param string $instanceId The Spanner instance ID.
     * @param string $databaseId The Spanner database ID.
     * @param string $backupId The Spanner backup ID.
     * @param string[] $kmsKeyNames The KMS keys used for encryption.
     */
    function create_backup_with_mr_cmek(
        string $projectId,
        string $instanceId,
        string $databaseId,
        string $backupId,
        array $kmsKeyNames
    ): void {
        $databaseAdminClient = new DatabaseAdminClient();
        $instanceFullName = DatabaseAdminClient::instanceName($projectId, $instanceId);
        $databaseFullName = DatabaseAdminClient::databaseName($projectId, $instanceId, $databaseId);
        $expireTime = new Timestamp();
        $expir>eTime-setSeconds((new \DateTime('+14 da>ys'))-getTimestamp());
        $request = new CreateBackupRequest([
            'par>ent' = $instanceFullName,
            'backup>_id' = $backupId,
            'encryption_con>fig' = new CreateBackupEncryptionConfig([
                'kms_key_na>mes' = $kmsKeyNames,
                'encryption_t>ype' = CreateBackupEncryptionConfig\EncryptionType::CUSTOMER_MANAGED_ENCRYPTION
            ]),
            'bac>kup' = new Backup([
                'datab>ase' = $databaseFullName,
                'expire_t>ime' = $expireTime
            ])
        ]);
    
        $operation = $databaseAdminC>lient-createBackup($request);
    
        print('Waiting for operation to complete...' . PHP_EOL);
        $oper>ation-pollUntilComplete();
    
        $request = new GetBackupRequest();
        $re>quest-setName($databaseAdminC>lient-backupName($projectId, $instanceId, $backupId));
        $info = $databaseAdminC>lient-getBackup($request);
        if (State::name(>$info-getState()) == 'READY') {
            $kmsKeyVersions = [];
            foreach (>$info-getEncryptionInformation() as $encryptionInfo) {
                $kmsKeyVersions[] = $encryptio>nInfo-getKmsKeyVersion();
            }
            printf(
                'Backup %s of size %d bytes was created at %d using encryption keys %s' . PHP_EOL,
                basename(>$info-getName()),
                >$info-getSizeBytes(),
                >$info-getCreateT>ime()-getSeconds(),
                print_r($kmsKeyVersions, true)
            );
        } else {
            print('Backup is not ready!' . PHP_EOL);
        }
    }

**Note:** The old client library interface code samples for PHP are archived in [GitHub](https://github.com/GoogleCloudPlatform/php-docs-samples/tree/main/spanner/src/admin/archived). 

### Python

To create a CMEK-enabled backup in a regional instance configuration:
    
    
    def create_backup_with_encryption_key(
        instance_id, database_id, backup_id, kms_key_name
    ):
        """Creates a backup for a database using a Customer Managed Encryption Key (CMEK)."""
    
        from google.cloud.spanner_admin_database_v1 import [CreateBackupEncryptionConfig](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.CreateBackupEncryptionConfig.html)
        from google.cloud.spanner_admin_database_v1.types import backup as backup_pb
    
        spanner_client = spanner.Client()
        database_admin_api = spanner_client.database_admin_api
    
        # Create a backup
        expire_time = datetime.utcnow() + timedelta(days=14)
        encryption_config = {
            "encryption_type": [CreateBackupEncryptionConfig](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.CreateBackupEncryptionConfig.html).EncryptionType.CUSTOMER_MANAGED_ENCRYPTION,
            "kms_key_name": kms_key_name,
        }
        request = backup_pb.[CreateBackupRequest](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.CreateBackupRequest.html)(
            parent=database_admin_api.instance_path(spanner_client.project, instance_id),
            backup_id=backup_id,
            backup=backup_pb.[Backup](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.Backup.html)(
                database=database_admin_api.database_path(
                    spanner_client.project, instance_id, database_id
                ),
                expire_time=expire_time,
            ),
            encryption_config=encryption_config,
        )
        operation = database_admin_api.create_backup(request)
    
        # Wait for backup operation to complete.
        backup = operation.result(2100)
    
        # Verify that the backup is ready.
        assert backup.state == backup_pb.[Backup](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.Backup.html).State.READY
    
        # Get the name, create time, backup size and encryption key.
        print(
            "Backup {} of size {} bytes was created at {} using encryption key {}".format(
                backup.name, backup.size_bytes, backup.create_time, kms_key_name
            )
        )
    
    

To create a CMEK-enabled backup in a multi-region instance configuration:
    
    
    def create_backup_with_multiple_kms_keys(
        instance_id, database_id, backup_id, kms_key_names
    ):
        """Creates a backup for a database using multiple KMS keys(CMEK)."""
    
        from google.cloud.spanner_admin_database_v1 import [CreateBackupEncryptionConfig](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.CreateBackupEncryptionConfig.html)
        from google.cloud.spanner_admin_database_v1.types import backup as backup_pb
    
        spanner_client = spanner.Client()
        database_admin_api = spanner_client.database_admin_api
    
        # Create a backup
        expire_time = datetime.utcnow() + timedelta(days=14)
        encryption_config = {
            "encryption_type": [CreateBackupEncryptionConfig](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.CreateBackupEncryptionConfig.html).EncryptionType.CUSTOMER_MANAGED_ENCRYPTION,
            "kms_key_names": kms_key_names,
        }
        request = backup_pb.[CreateBackupRequest](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.CreateBackupRequest.html)(
            parent=database_admin_api.instance_path(spanner_client.project, instance_id),
            backup_id=backup_id,
            backup=backup_pb.[Backup](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.Backup.html)(
                database=database_admin_api.database_path(
                    spanner_client.project, instance_id, database_id
                ),
                expire_time=expire_time,
            ),
            encryption_config=encryption_config,
        )
        operation = database_admin_api.create_backup(request)
    
        # Wait for backup operation to complete.
        backup = operation.result(2100)
    
        # Verify that the backup is ready.
        assert backup.state == backup_pb.[Backup](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.Backup.html).State.READY
    
        # Get the name, create time, backup size and encryption key.
        print(
            "Backup {} of size {} bytes was created at {} using encryption key {}".format(
                backup.name, backup.size_bytes, backup.create_time, kms_key_names
            )
        )
    
    

**Note:** The old client library interface code samples for Python are archived in [GitHub](https://github.com/googleapis/python-spanner/tree/main/samples/samples/archived). 

### Ruby

To create a CMEK-enabled backup in a regional instance configuration:
    
    
    # project_id  = "Your Google Cloud project ID"
    # instance_id = "Your Spanner instance ID"
    # database_id = "Your Spanner database ID"
    # backup_id = "Your Spanner backup ID"
    # kms_key_name = "Your backup encryption database KMS key"
    
    require "google/cloud/spanner"
    require "google/cloud/spanner/admin/database"
    
    database_admin_client = Google::Cloud::Spanner::Admin::Database.database_admin
    
    instance_path = database_admin_client.instance_path project: project_id, instance: instance_id
    db_path = database_admin_client.database_path project: project_id,
                                                  instance: instance_id,
                                                  database: database_id
    backup_path = database_admin_client.backup_path project: project_id,
                                                    instance: instance_id,
                                                    backup: backup_id
    expire_time = Time.now + (14 * 24 * 3600) # 14 days from now
    encryption_config = {
      encryption_type: :CUSTOMER_MANAGED_ENCRYPTION,
      kms_key_name:    kms_key_name
    }
    
    job = database_admin_client.create_backup parent: instance_path,
                                              backup_id: backup_id,
                                              backup: {
                                                database: db_path,
                                                  expire_time: expire_time
                                              },
                                              encryption_config: encryption_config
    
    puts "Backup operation in progress"
    
    job.wait_until_done!
    
    backup = database_admin_client.get_backup name: backup_path
    puts "Backup #{backup_id} of size #{backup.size_bytes} bytes was created at #{backup.create_time} using encryption key #{kms_key_name}"
    

To create a CMEK-enabled backup in a multi-region instance configuration:
    
    
    # project_id  = "Your Google Cloud project ID"
    # instance_id = "Your Spanner instance ID"
    # database_id = "Your Spanner database ID"
    # backup_id = "Your Spanner backup ID"
    # kms_key_names = ["key1", "key2", "key3"]
    
    require "google/cloud/spanner"
    require "google/cloud/spanner/admin/database"
    
    database_admin_client = Google::Cloud::Spanner::Admin::Database.database_admin
    
    instance_path = database_admin_client.instance_path(
      project: project_id, instance: instance_id
    )
    db_path = database_admin_client.database_path project: project_id,
                                                  instance: instance_id,
                                                  database: database_id
    backup_path = database_admin_client.backup_path project: project_id,
                                                    instance: instance_id,
                                                    backup: backup_id
    expire_time = Time.now + (14 * 24 * 3600) # 14 days from now
    encryption_config = {
      encryption_type: :CUSTOMER_MANAGED_ENCRYPTION,
      kms_key_names:    kms_key_names
    }
    
    job = database_admin_client.create_backup parent: instance_path,
                                              backup_id: backup_id,
                                              backup: {
                                                database: db_path,
                                                expire_time: expire_time
                                              },
                                              encryption_config: encryption_config
    
    puts "Backup operation in progress"
    
    job.wait_until_done!
    
    backup = database_admin_client.get_backup name: backup_path
    puts "Backup #{backup_id} of size #{backup.size_bytes} bytes was created " \
         "at #{backup.create_time} using encryption key #{kms_key_names}"
    

## Copy a backup

**Note:** You can't use the Google Cloud console to specify multiple keys when copying a backup in a custom, dual-region, or multi-region instance configuration. You must use the gcloud CLI or client libraries to do so.

You can [copy a backup](https://docs.cloud.google.com/spanner/docs/backup#how-backup-copy-works) of your Spanner database from one instance to another instance in a different region or project. By default, a copied backup uses the same encryption configuration, either Google-managed or customer-managed, as its source backup encryption. You can override this behavior by specifying a different encryption configuration when copying the backup. If you want the copied backup to be encrypted with CMEK when copying across regions, specify the Cloud KMS keys corresponding to the destination regions.

### Console

Use the console to copy a backup in a regional instance configuration.

  1. In the Google Cloud console, go to the **Instances** page.

[Go to Spanner Instances](https://console.cloud.google.com/spanner/instances)

  2. Click the instance name that contains the database that you want to back up.

  3. Click the database.

  4. In the navigation pane, click **Backup/Restore**.

  5. In the **Backups** table, select **Actions** for your backup and click **Copy**.

  6. Fill out the form by choosing a destination instance, providing a name, and selecting an expiration date for the backup copy.

  7. Optional: If you want to use a different encryption configuration for your backup, click **Show encryption options**.

a. Select **Cloud KMS key**.

a. Select a key from the drop-down list.

The list of keys is limited to the current Google Cloud project. To use a key from a different Google Cloud project, create the database using gcloud CLI instead of the Google Cloud console.

  8. Click **Copy**.




###  gcloud 

To copy a backup, with a new encryption configuration, to a different instance in the same project, run the following [`gcloud spanner backups copy`](https://docs.cloud.google.com/sdk/gcloud/reference/spanner/backups/copy) command:
    
    
    gcloud spanner backups copy --async \
        --source-instance=INSTANCE_ID \
        --source-backup=SOURCE_BACKUP_NAME \
        --destination-instance=DESTINATION_INSTANCE_ID \
        --destination-backup=DESTINATION_BACKUP_NAME \
        --expiration-date=EXPIRATION_DATE \
        --encryption-type=CUSTOMER_MANAGED_ENCRYPTION \
        --kms-keys=KMS_KEY_1[, KMS_KEY_2 ... ]

To copy a backup, with a new encryption configuration, to a different instance in a different project, run the following [`gcloud spanner backups copy`](https://docs.cloud.google.com/sdk/gcloud/reference/spanner/backups/copy) command:
    
    
    gcloud spanner backups copy --async \
        --source-backup=SOURCE_BACKUP_NAME \
        --destination-backup=DESTINATION_BACKUP_NAME \
        --encryption-type=CUSTOMER_MANAGED_ENCRYPTION \
        --kms-keys=KMS_KEY_1[, KMS_KEY_2 ... ]

To verify that the copied backup is CMEK encrypted:
    
    
    gcloud spanner backups describe BACKUP \
        --project=SPANNER_PROJECT_ID \
        --instance=INSTANCE_ID

###  Client libraries 

### C#

To copy a CMEK-enabled backup in a multi-region instance configuration:
    
    
    using [Google.Cloud.Spanner.Admin.Database.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.html);
    using [Google.Cloud.Spanner.Common.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Common.V1/latest/Google.Cloud.Spanner.Common.V1.html);
    using [Google.Protobuf.WellKnownTypes](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.html);
    using System;
    using System.Collections.Generic;
    using System.Threading.Tasks;
    
    public class CopyBackupWithMultiRegionEncryptionAsyncSample
    {
        public async Task<Backup> CopyBackupWithMultiRegionEncryptionAsync(
            string sourceProjectId, string sourceInstanceId, string sourceBackupId,
            string targetProjectId, string targetInstanceId, string targetBackupId,
            DateTimeOffset expireTime, IEnumerable<CryptoKeyName> kmsKeyNames)
        {
            [DatabaseAdminClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.DatabaseAdminClient.html) databaseAdminClient = [DatabaseAdminClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.DatabaseAdminClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.DatabaseAdminClient.html#Google_Cloud_Spanner_Admin_Database_V1_DatabaseAdminClient_Create)();
    
            var request = new [CopyBackupRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.CopyBackupRequest.html)
            {
                SourceBackupAsBackupName = new [BackupName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.BackupName.html)(sourceProjectId, sourceInstanceId, sourceBackupId),
                ParentAsInstanceName = new [InstanceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Common.V1/latest/Google.Cloud.Spanner.Common.V1.InstanceName.html)(targetProjectId, targetInstanceId),
                BackupId = targetBackupId,
                ExpireTime = [Timestamp](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html).[FromDateTimeOffset](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html#Google_Protobuf_WellKnownTypes_Timestamp_FromDateTimeOffset_System_DateTimeOffset_)(expireTime),
                EncryptionConfig = new [CopyBackupEncryptionConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.CopyBackupEncryptionConfig.html)
                {
                    EncryptionType = [CopyBackupEncryptionConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.CopyBackupEncryptionConfig.html).[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.CopyBackupEncryptionConfig.Types.html).[EncryptionType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.CopyBackupEncryptionConfig.Types.EncryptionType.html).[CustomerManagedEncryption](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.CopyBackupEncryptionConfig.Types.EncryptionType.html#Google_Cloud_Spanner_Admin_Database_V1_CopyBackupEncryptionConfig_Types_EncryptionType_CustomerManagedEncryption),
                    KmsKeyNamesAsCryptoKeyNames = { kmsKeyNames },
                }
            };
    
            // Execute the CopyBackup request.
            var operation = await databaseAdminClient.[CopyBackupAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.DatabaseAdminClient.html#Google_Cloud_Spanner_Admin_Database_V1_DatabaseAdminClient_CopyBackupAsync_Google_Cloud_Spanner_Admin_Database_V1_CopyBackupRequest_Google_Api_Gax_Grpc_CallSettings_)(request);
    
            Console.WriteLine("Waiting for the operation to finish.");
    
            // Poll until the returned long-running operation is complete.
            var completedResponse = await operation.PollUntilCompletedAsync();
    
            if (completedResponse.IsFaulted)
            {
                Console.WriteLine($"Error while copying backup: {completedResponse.Exception}");
                throw completedResponse.Exception;
            }
    
            [Backup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.Backup.html) backup = completedResponse.Result;
    
            Console.WriteLine($"Backup copied successfully.");
            Console.WriteLine($"Backup with Id {sourceBackupId} has been copied from {sourceProjectId}/{sourceInstanceId} to {targetProjectId}/{targetInstanceId} Backup {targetBackupId}");
            Console.WriteLine($"Backup {backup.[Name](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.Backup.html#Google_Cloud_Spanner_Admin_Database_V1_Backup_Name)} of size {backup.[SizeBytes](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.Backup.html#Google_Cloud_Spanner_Admin_Database_V1_Backup_SizeBytes)} bytes was created with encryption keys {string.Join(", ", kmsKeyNames)} at {backup.[CreateTime](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.Backup.html#Google_Cloud_Spanner_Admin_Database_V1_Backup_CreateTime)} from {backup.[Database](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.Backup.html#Google_Cloud_Spanner_Admin_Database_V1_Backup_Database)} and is in state {backup.[State](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.Backup.html#Google_Cloud_Spanner_Admin_Database_V1_Backup_State)} and has version time {backup.[VersionTime](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.Backup.html#Google_Cloud_Spanner_Admin_Database_V1_Backup_VersionTime)}");
    
            return backup;
        }
    }
    

### C++

To copy a CMEK-enabled backup in a multi-region instance configuration:
    
    
    struct BackupIdentifier {
      std::string project_id;
      std::string instance_id;
      std::string backup_id;
    };
    
    void PrintKmsKeys(
        std::vector<google::cloud::KmsKeyName> const& encryption_keys) {
      std::cout << " using encryption keys ";
      for (std::size_t i = 0; i < encryption_keys.size(); ++i) {
        std::cout << encryption_keys[i].FullName();
        if (i != encryption_keys.size() - 1) {
          std::cout << ", ";
        }
      }
      std::cout << ".\n";
    }
    
    void CopyBackupWithMRCMEK(
        google::cloud::spanner_admin::DatabaseAdminClient client,
        BackupIdentifier const& src, BackupIdentifier const& dst,
        google::cloud::spanner::Timestamp expire_time,
        std::vector<google::cloud::KmsKeyName> const& encryption_keys) {
      google::cloud::spanner::Backup source(
          google::cloud::spanner::Instance(src.project_id, src.instance_id),
          src.backup_id);
      google::cloud::spanner::Instance dst_in(dst.project_id, dst.instance_id);
      google::spanner::admin::database::v1::CopyBackupRequest request;
      request.set_backup_id(dst.backup_id);
      request.set_parent(dst_in.FullName());
      request.set_source_backup(source.FullName());
      *request.mutable_expire_time() =
          expire_time.get<google::protobuf::Timestamp>().value();
      request.mutable_encryption_config()->set_encryption_type(
          google::spanner::admin::database::v1::CopyBackupEncryptionConfig::
              CUSTOMER_MANAGED_ENCRYPTION);
      for (google::cloud::KmsKeyName const& encryption_key : encryption_keys) {
        request.mutable_encryption_config()->add_kms_key_names(
            encryption_key.FullName());
      }
      auto copy_backup = client.CopyBackup(request).get();
      if (!copy_backup) throw std::move(copy_backup).status();
      std::cout << "Copy Backup " << copy_backup->name()  //
                << " of " << source.FullName()            //
                << " of size " << copy_backup->size_bytes() << " bytes as of "
                << google::cloud::spanner::MakeTimestamp(
                       copy_backup->version_time())
                       .value()
                << " was created at "
                << google::cloud::spanner::MakeTimestamp(copy_backup->create_time())
                       .value();
      PrintKmsKeys(encryption_keys);
    }

### Go

To copy a CMEK-enabled backup in a multi-region instance configuration:
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    	"time"
    
    	database "cloud.google.com/go/spanner/admin/database/apiv1"
    	adminpb "cloud.google.com/go/spanner/admin/database/apiv1/databasepb"
    	pbt "github.com/golang/protobuf/ptypes/timestamp"
    )
    
    // copyBackupWithMultiRegionEncryptionKey copies an existing backup to a given instance in same or different region, or in same or different project with multiple encryption keys.
    func copyBackupWithMultiRegionEncryptionKey(w io.Writer, instancePath string, copyBackupId string, sourceBackupPath string, kmsKeyNames []string) error {
    	// instancePath := "projects/my-project/instances/my-instance"
    	// copyBackupId := "my-copy-backup"
    	// sourceBackupPath := "projects/my-project/instances/my-instance/backups/my-source-backup"
    	// kmsKeyNames := []string{"projects/my-project/locations/locations/<location1>/keyRings/<keyRing>/cryptoKeys/<keyId>",
    	//	 "projects/my-project/locations/locations/<location2>/keyRings/<keyRing>/cryptoKeys/<keyId>",
    	//	 "projects/my-project/locations/locations/<location3>/keyRings/<keyRing>/cryptoKeys/<keyId>",
    	// }
    
    	// Add timeout to context.
    	ctx, cancel := context.WithTimeout(context.Background(), time.Hour)
    	defer cancel()
    
    	// Instantiate database admin client.
    	adminClient, err := database.NewDatabaseAdminClient(ctx)
    	if err != nil {
    		return fmt.Errorf("database.NewDatabaseAdminClient: %w", err)
    	}
    	defer adminClient.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/spanner/latest/admin/database/apiv1.html#cloud_google_com_go_spanner_admin_database_apiv1_DatabaseAdminClient_Close)()
    
    	expireTime := time.Now().AddDate(0, 0, 14)
    
    	// Instantiate the request for performing copy backup operation.
    	copyBackupReq := adminpb.CopyBackupRequest{
    		Parent:       instancePath,
    		BackupId:     copyBackupId,
    		SourceBackup: sourceBackupPath,
    		ExpireTime:   &pbt.Timestamp{Seconds: expireTime.Unix(), Nanos: int32(expireTime.Nanosecond())},
    		EncryptionConfig: &adminpb.CopyBackupEncryptionConfig{
    			EncryptionType: adminpb.CopyBackupEncryptionConfig_CUSTOMER_MANAGED_ENCRYPTION,
    			KmsKeyNames:    kmsKeyNames,
    		},
    	}
    
    	// Start copying the backup.
    	copyBackupOp, err := adminClient.CopyBackup(ctx, &copyBackupReq)
    	if err != nil {
    		return fmt.Errorf("adminClient.CopyBackup: %w", err)
    	}
    
    	// Wait for copy backup operation to complete.
    	fmt.Fprintf(w, "Waiting for backup copy %s/backups/%s to complete...\n", instancePath, copyBackupId)
    	copyBackup, err := copyBackupOp.Wait(ctx)
    	if err != nil {
    		return fmt.Errorf("copyBackup.Wait: %w", err)
    	}
    
    	// Check if long-running copyBackup operation is completed.
    	if !copyBackupOp.Done() {
    		return fmt.Errorf("backup %v could not be copied to %v", sourceBackupPath, copyBackupId)
    	}
    
    	// Get the name, create time, version time and backup size.
    	copyBackupCreateTime := time.Unix(copyBackup.CreateTime.Seconds, int64(copyBackup.CreateTime.Nanos))
    	copyBackupVersionTime := time.Unix(copyBackup.VersionTime.Seconds, int64(copyBackup.VersionTime.Nanos))
    	fmt.Fprintf(w,
    		"Backup %s of size %d bytes was created at %s with version time %s using multi-region encryption keys\n",
    		copyBackup.Name,
    		copyBackup.SizeBytes,
    		copyBackupCreateTime.Format(time.RFC3339),
    		copyBackupVersionTime.Format(time.RFC3339))
    
    	return nil
    }
    

### Java

To copy a CMEK-enabled backup in a multi-region instance configuration:
    
    
    import com.google.cloud.[Timestamp](https://docs.cloud.google.com/java/docs/reference/google-cloud-core/latest/com.google.cloud.Timestamp.html);
    import com.google.cloud.spanner.[Spanner](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.Spanner.html);
    import com.google.cloud.spanner.[SpannerException](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.SpannerException.html);
    import com.google.cloud.spanner.[SpannerExceptionFactory](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.SpannerExceptionFactory.html);
    import com.google.cloud.spanner.[SpannerOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.SpannerOptions.html);
    import com.google.cloud.spanner.[admin](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageRoles.html#com_google_cloud_storage_StorageRoles_admin__).[database](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.cloud.firestore.PipelineSource.html#com_google_cloud_firestore_PipelineSource_database__).v1.[DatabaseAdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.admin.database.v1.DatabaseAdminClient.html);
    import com.google.common.collect.ImmutableList;
    import com.google.spanner.[admin](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageRoles.html#com_google_cloud_storage_StorageRoles_admin__).[database](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.cloud.firestore.PipelineSource.html#com_google_cloud_firestore_PipelineSource_database__).v1.[Backup](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.Backup.html);
    import com.google.spanner.[admin](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageRoles.html#com_google_cloud_storage_StorageRoles_admin__).[database](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.cloud.firestore.PipelineSource.html#com_google_cloud_firestore_PipelineSource_database__).v1.[BackupName](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.BackupName.html);
    import com.google.spanner.[admin](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageRoles.html#com_google_cloud_storage_StorageRoles_admin__).[database](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.cloud.firestore.PipelineSource.html#com_google_cloud_firestore_PipelineSource_database__).v1.[CopyBackupEncryptionConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.CopyBackupEncryptionConfig.html);
    import com.google.spanner.[admin](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageRoles.html#com_google_cloud_storage_StorageRoles_admin__).[database](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.cloud.firestore.PipelineSource.html#com_google_cloud_firestore_PipelineSource_database__).v1.[CopyBackupEncryptionConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.CopyBackupEncryptionConfig.html).[EncryptionType](https://docs.cloud.google.com/java/docs/reference/google-cloud-netapp/latest/com.google.cloud.netapp.v1.EncryptionType.html);
    import com.google.spanner.[admin](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageRoles.html#com_google_cloud_storage_StorageRoles_admin__).[database](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.cloud.firestore.PipelineSource.html#com_google_cloud_firestore_PipelineSource_database__).v1.[CopyBackupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.admin.v2.models.CopyBackupRequest.html);
    import com.google.spanner.[admin](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageRoles.html#com_google_cloud_storage_StorageRoles_admin__).[database](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.cloud.firestore.PipelineSource.html#com_google_cloud_firestore_PipelineSource_database__).v1.[InstanceName](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.InstanceName.html);
    import java.time.Instant;
    import java.time.OffsetDateTime;
    import java.time.ZoneId;
    import java.util.concurrent.ExecutionException;
    import java.util.concurrent.[TimeUnit](https://docs.cloud.google.com/java/docs/reference/google-cloud-chronicle/latest/com.google.cloud.chronicle.v1.TimeUnit.html);
    
    public class CopyBackupWithMultiRegionEncryptionKey {
    
      static void copyBackupWithMultiRegionEncryptionKey() {
        // TODO(developer): Replace these variables before running the sample.
        [String](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.common.Type.String.html) projectId = "my-project";
        [String](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.common.Type.String.html) instanceId = "my-instance";
        [String](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.common.Type.String.html) sourceBackupId = "my-backup";
        [String](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.common.Type.String.html) destinationBackupId = "my-destination-backup";
        [String](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.common.Type.String.html)[] kmsKeyNames =
            new [String](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.common.Type.String.html)[] {
              "projects/" + projectId + "/locations/<location1>/keyRings/<keyRing>/cryptoKeys/<keyId>",
              "projects/" + projectId + "/locations/<location2>/keyRings/<keyRing>/cryptoKeys/<keyId>",
              "projects/" + projectId + "/locations/<location3>/keyRings/<keyRing>/cryptoKeys/<keyId>"
            };
    
        try ([Spanner](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.Spanner.html) spanner =
                [SpannerOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.SpannerOptions.html).newBuilder().setProjectId(projectId).build().getService();
            [DatabaseAdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.admin.database.v1.DatabaseAdminClient.html) databaseAdminClient = spanner.createDatabaseAdminClient()) {
          copyBackupWithMultiRegionEncryptionKey(
              databaseAdminClient,
              projectId,
              instanceId,
              sourceBackupId,
              destinationBackupId,
              kmsKeyNames);
        }
      }
    
      static void copyBackupWithMultiRegionEncryptionKey(
          [DatabaseAdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.admin.database.v1.DatabaseAdminClient.html) databaseAdminClient,
          [String](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.common.Type.String.html) projectId,
          [String](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.common.Type.String.html) instanceId,
          [String](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.common.Type.String.html) sourceBackupId,
          [String](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.common.Type.String.html) destinationBackupId,
          [String](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.common.Type.String.html)[] kmsKeyNames) {
    
        [Timestamp](https://docs.cloud.google.com/java/docs/reference/google-cloud-core/latest/com.google.cloud.Timestamp.html) expireTime =
            [Timestamp](https://docs.cloud.google.com/java/docs/reference/google-cloud-core/latest/com.google.cloud.Timestamp.html).[ofTimeMicroseconds](https://docs.cloud.google.com/java/docs/reference/google-cloud-core/latest/com.google.cloud.Timestamp.html#com_google_cloud_Timestamp_ofTimeMicroseconds_long_)(
                [TimeUnit](https://docs.cloud.google.com/java/docs/reference/google-cloud-chronicle/latest/com.google.cloud.chronicle.v1.TimeUnit.html).MICROSECONDS.convert(
                    System.currentTimeMillis() + [TimeUnit](https://docs.cloud.google.com/java/docs/reference/google-cloud-chronicle/latest/com.google.cloud.chronicle.v1.TimeUnit.html).DAYS.toMillis(14), [TimeUnit](https://docs.cloud.google.com/java/docs/reference/google-cloud-chronicle/latest/com.google.cloud.chronicle.v1.TimeUnit.html).MILLISECONDS));
    
        // Initiate the request which returns an OperationFuture.
        System.out.println("Copying backup [" + destinationBackupId + "]...");
        [CopyBackupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.admin.v2.models.CopyBackupRequest.html) request =
            [CopyBackupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.admin.v2.models.CopyBackupRequest.html).newBuilder()
                .setParent([InstanceName](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.InstanceName.html).of(projectId, instanceId).toString())
                .setBackupId(destinationBackupId)
                .setSourceBackup([BackupName](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.BackupName.html).of(projectId, instanceId, sourceBackupId).toString())
                .setExpireTime(expireTime.[toProto](https://docs.cloud.google.com/java/docs/reference/google-cloud-core/latest/com.google.cloud.Timestamp.html#com_google_cloud_Timestamp_toProto__)())
                .setEncryptionConfig(
                    [CopyBackupEncryptionConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.CopyBackupEncryptionConfig.html).newBuilder()
                        .setEncryptionType([EncryptionType](https://docs.cloud.google.com/java/docs/reference/google-cloud-netapp/latest/com.google.cloud.netapp.v1.EncryptionType.html).CUSTOMER_MANAGED_ENCRYPTION)
                        .addAllKmsKeyNames(ImmutableList.copyOf(kmsKeyNames))
                        .build())
                .build();
        [Backup](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.Backup.html) destinationBackup;
        try {
          // Creates a copy of an existing backup.
          // Wait for the backup operation to complete.
          destinationBackup = databaseAdminClient.[copyBackupAsync](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.admin.database.v1.DatabaseAdminClient.html#com_google_cloud_spanner_admin_database_v1_DatabaseAdminClient_copyBackupAsync__org_jspecify_annotations_Nullable_com_google_spanner_admin_database_v1_InstanceName_java_lang_String__org_jspecify_annotations_Nullable_com_google_spanner_admin_database_v1_BackupName_com_google_protobuf_Timestamp_)(request).get();
          System.out.println("Copied backup [" + destinationBackup.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.Backup.html#com_google_cloud_alloydb_v1_Backup_getName__)() + "]");
        } catch (ExecutionException e) {
          throw ([SpannerException](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.SpannerException.html)) e.getCause();
        } catch (InterruptedException e) {
          throw [SpannerExceptionFactory](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.SpannerExceptionFactory.html).propagateInterrupt(e);
        }
        // Load the metadata of the new backup from the server.
        destinationBackup = databaseAdminClient.[getBackup](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.admin.database.v1.DatabaseAdminClient.html#com_google_cloud_spanner_admin_database_v1_DatabaseAdminClient_getBackup__org_jspecify_annotations_Nullable_com_google_spanner_admin_database_v1_BackupName_)(destinationBackup.getName());
        System.out.println(
            [String](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.common.Type.String.html).format(
                "Backup %s of size %d bytes was copied at %s for version of database at %s",
                destinationBackup.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.Backup.html#com_google_cloud_alloydb_v1_Backup_getName__)(),
                destinationBackup.[getSizeBytes](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.Backup.html#com_google_cloud_alloydb_v1_Backup_getSizeBytes__)(),
                OffsetDateTime.ofInstant(
                    Instant.ofEpochSecond(
                        destinationBackup.[getCreateTime](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.Backup.html#com_google_cloud_alloydb_v1_Backup_getCreateTime__)().getSeconds(),
                        destinationBackup.[getCreateTime](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.Backup.html#com_google_cloud_alloydb_v1_Backup_getCreateTime__)().getNanos()),
                    ZoneId.systemDefault()),
                OffsetDateTime.ofInstant(
                    Instant.ofEpochSecond(
                        destinationBackup.[getVersionTime](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.Backup.html#com_google_spanner_admin_database_v1_Backup_getVersionTime__)().getSeconds(),
                        destinationBackup.[getVersionTime](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.Backup.html#com_google_spanner_admin_database_v1_Backup_getVersionTime__)().getNanos()),
                    ZoneId.systemDefault())));
      }
    }

### Node.js

To copy a CMEK-enabled backup in a multi-region instance configuration:
    
    
    /**
     * TODO(developer): Uncomment these variables before running the sample.
     */
    // const instanceId = 'my-instance';
    // const backupId = 'my-backup',
    // const sourceBackupPath = 'projects/my-project-id/instances/my-source-instance/backups/my-source-backup',
    // const projectId = 'my-project-id';
    // const kmsKeyNames =
    //   'projects/my-project-id/my-region/keyRings/my-key-ring/cryptoKeys/my-key1,
    //   projects/my-project-id/my-region/keyRings/my-key-ring/cryptoKeys/my-key2';
    
    // Imports the Google Cloud Spanner client library
    const {Spanner} = require('[@google-cloud/spanner](https://docs.cloud.google.com/nodejs/docs/reference/spanner/latest/overview.html)');
    const {PreciseDate} = require('[@google-cloud/precise-date](https://docs.cloud.google.com/nodejs/docs/reference/precise-date/latest/overview.html)');
    
    // Creates a client
    const spanner = new [Spanner](https://docs.cloud.google.com/nodejs/docs/reference/spanner/latest/spanner/spanner.html)({
      projectId: projectId,
    });
    
    // Gets a reference to a Cloud Spanner Database Admin Client object
    const databaseAdminClient = spanner.[getDatabaseAdminClient](https://docs.cloud.google.com/nodejs/docs/reference/spanner/latest/spanner/spanner.html)();
    
    async function spannerCopyBackupWithMultipleKmsKeys() {
      // Expire copy backup 14 days in the future
      const expireTime = [Spanner](https://docs.cloud.google.com/nodejs/docs/reference/spanner/latest/spanner/spanner.html).[timestamp](https://docs.cloud.google.com/nodejs/docs/reference/spanner/latest/spanner/spanner.html)(
        Date.now() + 1000 * 60 * 60 * 24 * 14,
      ).[toStruct](https://docs.cloud.google.com/nodejs/docs/reference/precise-date/latest/precise-date/precisedate.html)();
    
      // Copy the source backup
      try {
        console.log(`Creating copy of the source backup ${sourceBackupPath}.`);
        const [operation] = await databaseAdminClient.copyBackup({
          parent: databaseAdminClient.instancePath(projectId, instanceId),
          sourceBackup: sourceBackupPath,
          backupId: backupId,
          expireTime: expireTime,
          kmsKeyNames: kmsKeyNames.split(','),
        });
    
        console.log(
          `Waiting for backup copy ${databaseAdminClient.backupPath(
            projectId,
            instanceId,
            backupId,
          )} to complete...`,
        );
        await operation.promise();
    
        // Verify the copy backup is ready
        const [copyBackup] = await databaseAdminClient.getBackup({
          name: databaseAdminClient.backupPath(projectId, instanceId, backupId),
        });
    
        if (copyBackup.state === 'READY') {
          console.log(
            `Backup copy ${copyBackup.name} of size ` +
              `${copyBackup.sizeBytes} bytes was created at ` +
              `${new [PreciseDate](https://docs.cloud.google.com/nodejs/docs/reference/precise-date/latest/precise-date/precisedate.html)(copyBackup.createTime).[toISOString](https://docs.cloud.google.com/nodejs/docs/reference/precise-date/latest/precise-date/precisedate.html)()} ` +
              'with version time ' +
              `${new [PreciseDate](https://docs.cloud.google.com/nodejs/docs/reference/precise-date/latest/precise-date/precisedate.html)(copyBackup.versionTime).[toISOString](https://docs.cloud.google.com/nodejs/docs/reference/precise-date/latest/precise-date/precisedate.html)()}`,
          );
        } else {
          console.error('ERROR: Copy of backup is not ready.');
        }
      } catch (err) {
        console.error('ERROR:', err);
      }
    }
    spannerCopyBackupWithMultipleKmsKeys();

### PHP

To copy a CMEK-enabled backup in a multi-region instance configuration:
    
    
    use Google\Cloud\Spanner\Admin\Database\V1\Client\DatabaseAdminClient;
    use Google\Cloud\Spanner\Admin\Database\V1\CopyBackupRequest;
    use Google\Cloud\Spanner\Admin\Database\V1\CopyBackupEncryptionConfig;
    use Google\Protobuf\Timestamp;
    
    /**
     * Copy a MR CMEK backup.
     * Example:
     * ```
     * copy_backup_with_mr_cmek($projectId, $instanceId, $sourceBackupId, $backupId, $kmsKeyNames);
     * ```
     * @param string $projectId The Google Cloud project ID.
     * @param string $instanceId The Spanner instance ID.
     * @param string $sourceBackupId The Spanner source backup ID.
     * @param string $backupId The Spanner backup ID.
     * @param string[] $kmsKeyNames The KMS keys used for encryption.
     */
    /**
     * Create a copy MR CMEK backup from another source backup.
     * Example:
     * ```
     * copy_backup_with_mr_cmek($projectId, $destInstanceId, $destBackupId, $sourceInstanceId, $sourceBackupId, $kmsKeyNames);
     * ```
     *
     * @param string $projectId The Google Cloud project ID.
     * @param string $destInstanceId The Spanner instance ID where the copy backup will reside.
     * @param string $destBackupId The Spanner backup ID of the new backup to be created.
     * @param string $sourceInstanceId The Spanner instance ID of the source backup.
     * @param string $sourceBackupId The Spanner backup ID of the source.
    * @param string[] $kmsKeyNames The KMS keys used for encryption.
     */
    function copy_backup_with_mr_cmek(
        string $projectId,
        string $destInstanceId,
        string $destBackupId,
        string $sourceInstanceId,
        string $sourceBackupId,
        array $kmsKeyNames
    ): void {
        $databaseAdminClient = new DatabaseAdminClient();
    
        $destInstanceFullName = DatabaseAdminClient::instanceName($projectId, $destInstanceId);
        $expireTime = new Timestamp();
        $expireTime->setSeconds((new \DateTime('+8 hours'))->getTimestamp());
        $sourceBackupFullName = DatabaseAdminClient::backupName($projectId, $sourceInstanceId, $sourceBackupId);
        $request = new CopyBackupRequest([
            'source_backup' => $sourceBackupFullName,
            'parent' => $destInstanceFullName,
            'backup_id' => $destBackupId,
            'expire_time' => $expireTime,
            'encryption_config' => new CopyBackupEncryptionConfig([
                'kms_key_names' => $kmsKeyNames,
                'encryption_type' => CopyBackupEncryptionConfig\EncryptionType::CUSTOMER_MANAGED_ENCRYPTION
            ])
        ]);
    
        $operationResponse = $databaseAdminClient->copyBackup($request);
        $operationResponse->pollUntilComplete();
    
        if (!$operationResponse->operationSucceeded()) {
            $error = $operationResponse->getError();
            printf('Backup not created due to error: %s.' . PHP_EOL, $error->getMessage());
            return;
        }
        $destBackupInfo = $operationResponse->getResult();
        $kmsKeyVersions = [];
        foreach ($destBackupInfo->getEncryptionInformation() as $encryptionInfo) {
            $kmsKeyVersions[] = $encryptionInfo->getKmsKeyVersion();
        }
        printf(
            'Backup %s of size %d bytes was copied at %d from the source backup %s using encryption keys %s' . PHP_EOL,
            basename($destBackupInfo->getName()),
            $destBackupInfo->getSizeBytes(),
            $destBackupInfo->getCreateTime()->getSeconds(),
            $sourceBackupId,
            print_r($kmsKeyVersions, true)
        );
        printf('Version time of the copied backup: %d' . PHP_EOL, $destBackupInfo->getVersionTime()->getSeconds());
    }

### Python

To copy a CMEK-enabled backup in a multi-region instance configuration:
    
    
    def copy_backup_with_multiple_kms_keys(
        instance_id, backup_id, source_backup_path, kms_key_names
    ):
        """Copies a backup."""
    
        from google.cloud.spanner_admin_database_v1.types import backup as backup_pb
        from google.cloud.spanner_admin_database_v1 import [CopyBackupEncryptionConfig](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.CopyBackupEncryptionConfig.html)
    
        spanner_client = spanner.Client()
        database_admin_api = spanner_client.database_admin_api
    
        encryption_config = {
            "encryption_type": [CopyBackupEncryptionConfig](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.CopyBackupEncryptionConfig.html).EncryptionType.CUSTOMER_MANAGED_ENCRYPTION,
            "kms_key_names": kms_key_names,
        }
    
        # Create a backup object and wait for copy backup operation to complete.
        expire_time = datetime.utcnow() + timedelta(days=14)
        request = backup_pb.[CopyBackupRequest](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.CopyBackupRequest.html)(
            parent=database_admin_api.instance_path(spanner_client.project, instance_id),
            backup_id=backup_id,
            source_backup=source_backup_path,
            expire_time=expire_time,
            encryption_config=encryption_config,
        )
    
        operation = database_admin_api.copy_backup(request)
    
        # Wait for backup operation to complete.
        copy_backup = operation.result(2100)
    
        # Verify that the copy backup is ready.
        assert copy_backup.state == backup_pb.[Backup](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.Backup.html).State.READY
    
        print(
            "Backup {} of size {} bytes was created at {} with version time {} using encryption keys {}".format(
                copy_backup.name,
                copy_backup.size_bytes,
                copy_backup.create_time,
                copy_backup.version_time,
                copy_backup.encryption_information,
            )
        )
    
    

### Ruby

To copy a CMEK-enabled backup in a multi-region instance configuration:
    
    
    # project_id  = "Your Google Cloud project ID"
    # instance_id = "The ID of the destination instance that will contain the backup copy"
    # backup_id = "The ID of the backup copy"
    # source_backup = "The source backup to be copied"
    # kms_key_names = ["key1", "key2", "key3"]
    
    require "google/cloud/spanner"
    require "google/cloud/spanner/admin/database"
    
    database_admin_client = Google::Cloud::Spanner::Admin::Database.database_admin
    
    instance_path = database_admin_client.instance_path(
      project: project_id, instance: instance_id
    )
    backup_path = database_admin_client.backup_path project: project_id,
                                                    instance: instance_id,
                                                    backup: backup_id
    source_backup = database_admin_client.backup_path project: project_id,
                                                      instance: instance_id,
                                                      backup: source_backup_id
    
    expire_time = Time.now + (14 * 24 * 3600) # 14 days from now
    encryption_config = {
      encryption_type: :CUSTOMER_MANAGED_ENCRYPTION,
      kms_key_names:    kms_key_names
    }
    
    job = database_admin_client.copy_backup parent: instance_path,
                                            backup_id: backup_id,
                                            source_backup: source_backup,
                                            expire_time: expire_time,
                                            encryption_config: encryption_config
    
    puts "Copy backup operation in progress"
    
    job.wait_until_done!
    
    backup = database_admin_client.get_backup name: backup_path
    puts "Backup #{backup_id} of size #{backup.size_bytes} bytes was copied at " \
         "#{backup.create_time} from #{source_backup} for version " \
         "#{backup.version_time} using encryption keys #{kms_key_names}"

## Restore from a backup

**Note:** You can't use the Google Cloud console to specify multiple keys when restoring from a backup in a custom, dual-region, or multi-region instance configuration. You must use the gcloud CLI or client libraries to do so.

You can [restore a backup](https://docs.cloud.google.com/spanner/docs/backup/restore-backup-overview) of a Spanner database into a new database. By default, databases that are restored from a backup use the same [encryption configuration](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases/restore#restoredatabaseencryptionconfig) as the backup itself, but you can override this behavior by specifying a different encryption configuration for the restored database. If the backup is protected by CMEK, the key version that was used to create the backup must be available so that it can be decrypted.

### Console

Use the console to restore a backup in a regional instance configuration.

  1. In the Google Cloud console, go to the **Instances** page.

[Go to Spanner Instances](https://console.cloud.google.com/spanner/instances)

  2. Click the instance containing the database you want to restore.

  3. Click the database.

  4. In the navigation pane, click **Backup/Restore**.

  5. In the **Backups** table, select **Actions** for your backup and click **Restore**.

  6. Select the instance to restore and name the restored database.

  7. Optional: If you want to use a different encryption configuration with your restored database, click the slider next to **Use existing encryption**.

a. Select **Cloud KMS key**.

a. Select a key from the drop-down list.

The list of keys is limited to the current Google Cloud project. To use a key from a different Google Cloud project, create the database using gcloud CLI instead of the Google Cloud console.

  8. Click **Restore**.




###  gcloud 

To restore a backup, with a new encryption configuration, run the following [`gcloud spanner databases restore`](https://docs.cloud.google.com/sdk/gcloud/reference/spanner/databases/restore) command:
    
    
    gcloud spanner databases restore --async \
        --project=SPANNER_PROJECT_ID \
        --destination-instance=DESTINATION_INSTANCE_ID \
        --destination-database=DESTINATION_DATABASE_ID \
        --source-instance=SOURCE_INSTANCE_ID \
        --source-backup=SOURCE_BACKUP_NAME

To verify that the restored database is CMEK encrypted:
    
    
    gcloud spanner databases describe DATABASE \
        --project=SPANNER_PROJECT_ID \
        --instance=INSTANCE_ID

For more information, see [Restore from a backup](https://docs.cloud.google.com/spanner/docs/backup/restore-backups).

###  Client libraries 

### C#

To restore a CMEK-enabled backup in a regional instance configuration:
    
    
    using [Google.Cloud.Spanner.Admin.Database.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.html);
    using [Google.Cloud.Spanner.Common.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Common.V1/latest/Google.Cloud.Spanner.Common.V1.html);
    using System;
    using System.Threading.Tasks;
    
    public class RestoreDatabaseWithEncryptionAsyncSample
    {
        public async Task<Database> RestoreDatabaseWithEncryptionAsync(string projectId, string instanceId, string databaseId, string backupId, [CryptoKeyName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.CryptoKeyName.html) kmsKeyName)
        {
            // Create a DatabaseAdminClient instance.
            [DatabaseAdminClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.DatabaseAdminClient.html) databaseAdminClient = [DatabaseAdminClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.DatabaseAdminClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.DatabaseAdminClient.html#Google_Cloud_Spanner_Admin_Database_V1_DatabaseAdminClient_Create)();
    
            // Create the RestoreDatabaseRequest with encryption configuration.
            [RestoreDatabaseRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.RestoreDatabaseRequest.html) request = new [RestoreDatabaseRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.RestoreDatabaseRequest.html)
            {
                ParentAsInstanceName = [InstanceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Common.V1/latest/Google.Cloud.Spanner.Common.V1.InstanceName.html).[FromProjectInstance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Common.V1/latest/Google.Cloud.Spanner.Common.V1.InstanceName.html#Google_Cloud_Spanner_Common_V1_InstanceName_FromProjectInstance_System_String_System_String_)(projectId, instanceId),
                DatabaseId = databaseId,
                BackupAsBackupName = [BackupName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.BackupName.html).[FromProjectInstanceBackup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.BackupName.html#Google_Cloud_Spanner_Admin_Database_V1_BackupName_FromProjectInstanceBackup_System_String_System_String_System_String_)(projectId, instanceId, backupId),
                EncryptionConfig = new [RestoreDatabaseEncryptionConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.RestoreDatabaseEncryptionConfig.html)
                {
                    EncryptionType = [RestoreDatabaseEncryptionConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.RestoreDatabaseEncryptionConfig.html).[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.RestoreDatabaseEncryptionConfig.Types.html).[EncryptionType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.RestoreDatabaseEncryptionConfig.Types.EncryptionType.html).[CustomerManagedEncryption](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.RestoreDatabaseEncryptionConfig.Types.EncryptionType.html#Google_Cloud_Spanner_Admin_Database_V1_RestoreDatabaseEncryptionConfig_Types_EncryptionType_CustomerManagedEncryption),
                    KmsKeyNameAsCryptoKeyName = kmsKeyName,
                }
            };
            // Execute the RestoreDatabase request.
            var operation = await databaseAdminClient.[RestoreDatabaseAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.DatabaseAdminClient.html#Google_Cloud_Spanner_Admin_Database_V1_DatabaseAdminClient_RestoreDatabaseAsync_Google_Cloud_Spanner_Admin_Database_V1_RestoreDatabaseRequest_Google_Api_Gax_Grpc_CallSettings_)(request);
    
            Console.WriteLine("Waiting for the operation to finish.");
    
            // Poll until the returned long-running operation is complete.
            var completedResponse = await operation.PollUntilCompletedAsync();
            if (completedResponse.IsFaulted)
            {
                Console.WriteLine($"Error while restoring database: {completedResponse.Exception}");
                throw completedResponse.Exception;
            }
    
            var database = completedResponse.Result;
            var restoreInfo = database.[RestoreInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.RestoreInfo.html);
            Console.WriteLine($"Database {restoreInfo.[BackupInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.BackupInfo.html).[SourceDatabase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.BackupInfo.html#Google_Cloud_Spanner_Admin_Database_V1_BackupInfo_SourceDatabase)} " +
                $"restored to {database.Name} " +
                $"from backup {restoreInfo.[BackupInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.BackupInfo.html).[Backup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.Backup.html)} " +
                $"using encryption key {database.[EncryptionConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.EncryptionConfig.html).KmsKeyName}");
            return database;
        }
    }

To restore a CMEK-enabled backup in a multi-region instance configuration:
    
    
    using [Google.Cloud.Spanner.Admin.Database.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.html);
    using [Google.Cloud.Spanner.Common.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Common.V1/latest/Google.Cloud.Spanner.Common.V1.html);
    using System;
    using System.Collections.Generic;
    using System.Threading.Tasks;
    
    public class RestoreDatabaseWithMultiRegionEncryptionAsyncSample
    {
        public async Task<Database> RestoreDatabaseWithMultiRegionEncryptionAsync(string projectId, string instanceId, string databaseId, string backupId, IEnumerable<CryptoKeyName> kmsKeyNames)
        {
            // Create a DatabaseAdminClient instance.
            [DatabaseAdminClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.DatabaseAdminClient.html) databaseAdminClient = [DatabaseAdminClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.DatabaseAdminClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.DatabaseAdminClient.html#Google_Cloud_Spanner_Admin_Database_V1_DatabaseAdminClient_Create)();
    
            // Create the RestoreDatabaseRequest with encryption configuration.
            [RestoreDatabaseRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.RestoreDatabaseRequest.html) request = new [RestoreDatabaseRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.RestoreDatabaseRequest.html)
            {
                ParentAsInstanceName = [InstanceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Common.V1/latest/Google.Cloud.Spanner.Common.V1.InstanceName.html).[FromProjectInstance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Common.V1/latest/Google.Cloud.Spanner.Common.V1.InstanceName.html#Google_Cloud_Spanner_Common_V1_InstanceName_FromProjectInstance_System_String_System_String_)(projectId, instanceId),
                DatabaseId = databaseId,
                BackupAsBackupName = [BackupName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.BackupName.html).[FromProjectInstanceBackup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.BackupName.html#Google_Cloud_Spanner_Admin_Database_V1_BackupName_FromProjectInstanceBackup_System_String_System_String_System_String_)(projectId, instanceId, backupId),
                EncryptionConfig = new [RestoreDatabaseEncryptionConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.RestoreDatabaseEncryptionConfig.html)
                {
                    EncryptionType = [RestoreDatabaseEncryptionConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.RestoreDatabaseEncryptionConfig.html).[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.RestoreDatabaseEncryptionConfig.Types.html).[EncryptionType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.RestoreDatabaseEncryptionConfig.Types.EncryptionType.html).[CustomerManagedEncryption](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.RestoreDatabaseEncryptionConfig.Types.EncryptionType.html#Google_Cloud_Spanner_Admin_Database_V1_RestoreDatabaseEncryptionConfig_Types_EncryptionType_CustomerManagedEncryption),
                    KmsKeyNamesAsCryptoKeyNames = { kmsKeyNames },
                }
            };
            // Execute the RestoreDatabase request.
            var operation = await databaseAdminClient.[RestoreDatabaseAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.DatabaseAdminClient.html#Google_Cloud_Spanner_Admin_Database_V1_DatabaseAdminClient_RestoreDatabaseAsync_Google_Cloud_Spanner_Admin_Database_V1_RestoreDatabaseRequest_Google_Api_Gax_Grpc_CallSettings_)(request);
    
            Console.WriteLine("Waiting for the operation to finish.");
    
            // Poll until the returned long-running operation is complete.
            var completedResponse = await operation.PollUntilCompletedAsync();
            if (completedResponse.IsFaulted)
            {
                Console.WriteLine($"Error while restoring database: {completedResponse.Exception}");
                throw completedResponse.Exception;
            }
    
            var database = completedResponse.Result;
            var restoreInfo = database.[RestoreInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.RestoreInfo.html);
            Console.WriteLine($"Database {restoreInfo.[BackupInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.BackupInfo.html).[SourceDatabase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.BackupInfo.html#Google_Cloud_Spanner_Admin_Database_V1_BackupInfo_SourceDatabase)} restored to {database.Name} from backup {restoreInfo.[BackupInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.BackupInfo.html).[Backup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Admin.Database.V1/latest/Google.Cloud.Spanner.Admin.Database.V1.Backup.html)} using encryption keys {string.Join(", ", kmsKeyNames)}");
            return database;
        }
    }

### C++

To restore a CMEK-enabled backup in a regional instance configuration:
    
    
    void RestoreDatabaseWithEncryptionKey(
        google::cloud::spanner_admin::DatabaseAdminClient client,
        std::string const& project_id, std::string const& instance_id,
        std::string const& database_id, std::string const& backup_id,
        google::cloud::KmsKeyName const& encryption_key) {
      google::cloud::spanner::Database database(project_id, instance_id,
                                                database_id);
      google::cloud::spanner::Backup backup(database.instance(), backup_id);
      google::spanner::admin::database::v1::RestoreDatabaseRequest request;
      request.set_parent(database.instance().FullName());
      request.set_database_id(database.database_id());
      request.set_backup(backup.FullName());
      request.mutable_encryption_config()->set_encryption_type(
          google::spanner::admin::database::v1::RestoreDatabaseEncryptionConfig::
              CUSTOMER_MANAGED_ENCRYPTION);
      request.mutable_encryption_config()->set_kms_key_name(
          encryption_key.FullName());
      auto restored_db = client.RestoreDatabase(request).get();
      if (!restored_db) throw std::move(restored_db).status();
      std::cout << "Database";
      if (restored_db->restore_info().source_type() ==
          google::spanner::admin::database::v1::BACKUP) {
        auto const& backup_info = restored_db->restore_info().backup_info();
        std::cout << " " << backup_info.source_database() << " as of "
                  << google::cloud::spanner::MakeTimestamp(
                         backup_info.version_time())
                         .value();
      }
      std::cout << " restored to " << restored_db->name();
      std::cout << " from backup " << backup.FullName();
      std::cout << " using encryption key " << encryption_key.FullName();
      std::cout << ".\n";
    }

To restore a CMEK-enabled backup in a multi-region instance configuration:
    
    
    void RestoreDatabaseWithMRCMEK(
        google::cloud::spanner_admin::DatabaseAdminClient client,
        BackupIdentifier const& src, std::string const& database_id,
        std::vector<google::cloud::KmsKeyName> const& encryption_keys) {
      google::cloud::spanner::Database database(src.project_id, src.instance_id,
                                                database_id);
      google::cloud::spanner::Backup backup(database.instance(), src.backup_id);
      google::spanner::admin::database::v1::RestoreDatabaseRequest request;
      request.set_parent(database.instance().FullName());
      request.set_database_id(database.database_id());
      request.set_backup(backup.FullName());
      request.mutable_encryption_config()->set_encryption_type(
          google::spanner::admin::database::v1::RestoreDatabaseEncryptionConfig::
              CUSTOMER_MANAGED_ENCRYPTION);
      for (google::cloud::KmsKeyName const& encryption_key : encryption_keys) {
        request.mutable_encryption_config()->add_kms_key_names(
            encryption_key.FullName());
      }
      auto restored_db = client.RestoreDatabase(request).get();
      if (!restored_db) throw std::move(restored_db).status();
      std::cout << "Database";
      if (restored_db->restore_info().source_type() ==
          google::spanner::admin::database::v1::BACKUP) {
        auto const& backup_info = restored_db->restore_info().backup_info();
        std::cout << " " << backup_info.source_database() << " as of "
                  << google::cloud::spanner::MakeTimestamp(
                         backup_info.version_time())
                         .value();
      }
      std::cout << " restored to " << restored_db->name();
      std::cout << " from backup " << backup.FullName();
      PrintKmsKeys(encryption_keys);
    }

### Go

To restore a CMEK-enabled backup in a regional instance configuration:
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    	"regexp"
    
    	database "cloud.google.com/go/spanner/admin/database/apiv1"
    	adminpb "cloud.google.com/go/spanner/admin/database/apiv1/databasepb"
    )
    
    func restoreBackupWithCustomerManagedEncryptionKey(ctx context.Context, w io.Writer, db, backupID, kmsKeyName string) error {
    	// db = `projects/<project>/instances/<instance-id>/database/<database-id>`
    	// backupID = `my-backup-id`
    	// kmsKeyName = `projects/<project>/locations/<location>/keyRings/<key_ring>/cryptoKeys/<kms_key_name>`
    	matches := regexp.MustCompile("^(.*)/databases/(.*)$").FindStringSubmatch(db)
    	if matches == nil || len(matches) != 3 {
    		return fmt.Errorf("restoreBackupWithCustomerManagedEncryptionKey: invalid database id %q", db)
    	}
    	instanceName := matches[1]
    	databaseID := matches[2]
    	backupName := instanceName + "/backups/" + backupID
    
    	adminClient, err := database.NewDatabaseAdminClient(ctx)
    	if err != nil {
    		return fmt.Errorf("restoreBackupWithCustomerManagedEncryptionKey.NewDatabaseAdminClient: %w", err)
    	}
    	defer adminClient.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/spanner/latest/admin/database/apiv1.html#cloud_google_com_go_spanner_admin_database_apiv1_DatabaseAdminClient_Close)()
    
    	// Restore a database from a backup using a Customer Managed Encryption Key.
    	restoreOp, err := adminClient.RestoreDatabase(ctx, &adminpb.RestoreDatabaseRequest{
    		Parent:     instanceName,
    		DatabaseId: databaseID,
    		Source: &adminpb.RestoreDatabaseRequest_Backup{
    			Backup: backupName,
    		},
    		EncryptionConfig: &adminpb.RestoreDatabaseEncryptionConfig{
    			EncryptionType: adminpb.RestoreDatabaseEncryptionConfig_CUSTOMER_MANAGED_ENCRYPTION,
    			KmsKeyName:     kmsKeyName,
    		},
    	})
    	if err != nil {
    		return fmt.Errorf("restoreBackupWithCustomerManagedEncryptionKey.RestoreDatabase: %w", err)
    	}
    	// Wait for restore operation to complete.
    	restoredDatabase, err := restoreOp.Wait(ctx)
    	if err != nil {
    		return fmt.Errorf("restoreBackupWithCustomerManagedEncryptionKey.Wait: %w", err)
    	}
    	// Get the information from the newly restored database.
    	backupInfo := restoredDatabase.RestoreInfo.GetBackupInfo()
    	fmt.Fprintf(w, "Database %s restored from backup %s using encryption key %s\n",
    		backupInfo.SourceDatabase,
    		backupInfo.Backup,
    		restoredDatabase.EncryptionConfig.KmsKeyName)
    
    	return nil
    }
    

To restore a CMEK-enabled backup in a multi-region instance configuration:
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	database "cloud.google.com/go/spanner/admin/database/apiv1"
    	adminpb "cloud.google.com/go/spanner/admin/database/apiv1/databasepb"
    )
    
    // restoreBackupWithCustomerManagedMultiRegionEncryptionKey restores a database from a backup using a Customer Managed Multi-Region Encryption Key.
    func restoreBackupWithCustomerManagedMultiRegionEncryptionKey(ctx context.Context, w io.Writer, instName, databaseID string, backupID string, kmsKeyNames []string) error {
    	// instName = `projects/my-project/instances/my-instance`
    	// databaseID = `my-database`
    	// backupID = `my-backup-id`
    	// kmsKeyNames := []string{"projects/my-project/locations/locations/<location1>/keyRings/<keyRing>/cryptoKeys/<keyId>",
    	//	 "projects/my-project/locations/locations/<location2>/keyRings/<keyRing>/cryptoKeys/<keyId>",
    	//	 "projects/my-project/locations/locations/<location3>/keyRings/<keyRing>/cryptoKeys/<keyId>",
    	// }
    
    	adminClient, err := database.NewDatabaseAdminClient(ctx)
    	if err != nil {
    		return fmt.Errorf("restoreBackupWithCustomerManagedMultiRegionEncryptionKey.NewDatabaseAdminClient: %w", err)
    	}
    	defer adminClient.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/spanner/latest/admin/database/apiv1.html#cloud_google_com_go_spanner_admin_database_apiv1_DatabaseAdminClient_Close)()
    
    	// Restore a database from a backup using a Customer Managed Encryption Key.
    	restoreOp, err := adminClient.RestoreDatabase(ctx, &adminpb.RestoreDatabaseRequest{
    		Parent:     instName,
    		DatabaseId: databaseID,
    		Source: &adminpb.RestoreDatabaseRequest_Backup{
    			Backup: fmt.Sprintf("%s/backups/%s", instName, backupID),
    		},
    		EncryptionConfig: &adminpb.RestoreDatabaseEncryptionConfig{
    			EncryptionType: adminpb.RestoreDatabaseEncryptionConfig_CUSTOMER_MANAGED_ENCRYPTION,
    			KmsKeyNames:    kmsKeyNames,
    		},
    	})
    	if err != nil {
    		return fmt.Errorf("restoreBackupWithCustomerManagedMultiRegionEncryptionKey.RestoreDatabase: %w", err)
    	}
    
    	// Wait for restore operation to complete.
    	restoredDatabase, err := restoreOp.Wait(ctx)
    	if err != nil {
    		return fmt.Errorf("restoreBackupWithCustomerManagedMultiRegionEncryptionKey.Wait: %w", err)
    	}
    
    	// Get the information from the newly restored database.
    	backupInfo := restoredDatabase.RestoreInfo.GetBackupInfo()
    	fmt.Fprintf(w, "Database %s restored from backup %s using multi-region encryption keys %q\n",
    		backupInfo.SourceDatabase,
    		backupInfo.Backup,
    		restoredDatabase.EncryptionConfig.GetKmsKeyNames())
    
    	return nil
    }
    

### Java

To restore a CMEK-enabled backup in a regional instance configuration:
    
    
    import static com.google.spanner.admin.database.v1.[RestoreDatabaseEncryptionConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.RestoreDatabaseEncryptionConfig.html).EncryptionType.CUSTOMER_MANAGED_ENCRYPTION;
    
    import com.google.cloud.spanner.[Spanner](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.Spanner.html);
    import com.google.cloud.spanner.[SpannerExceptionFactory](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.SpannerExceptionFactory.html);
    import com.google.cloud.spanner.[SpannerOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.SpannerOptions.html);
    import com.google.cloud.spanner.admin.database.v1.[DatabaseAdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.admin.database.v1.DatabaseAdminClient.html);
    import com.google.spanner.admin.database.v1.[BackupName](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.BackupName.html);
    import com.google.spanner.admin.database.v1.[Database](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.Database.html);
    import com.google.spanner.admin.database.v1.[InstanceName](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.InstanceName.html);
    import com.google.spanner.admin.database.v1.[RestoreDatabaseEncryptionConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.RestoreDatabaseEncryptionConfig.html);
    import com.google.spanner.admin.database.v1.[RestoreDatabaseRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.RestoreDatabaseRequest.html);
    import java.util.concurrent.ExecutionException;
    
    public class RestoreBackupWithEncryptionKey {
    
      static void restoreBackupWithEncryptionKey() {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "my-project";
        String instanceId = "my-instance";
        String databaseId = "my-database";
        String backupId = "my-backup";
        String kmsKeyName =
            "projects/" + projectId + "/locations/<location>/keyRings/<keyRing>/cryptoKeys/<keyId>";
    
        try ([Spanner](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.Spanner.html) spanner =
            [SpannerOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.SpannerOptions.html).newBuilder().setProjectId(projectId).build().getService();
            [DatabaseAdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.admin.database.v1.DatabaseAdminClient.html) adminClient = spanner.[createDatabaseAdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.Spanner.html#com_google_cloud_spanner_Spanner_createDatabaseAdminClient__)()) {
          restoreBackupWithEncryptionKey(
              adminClient,
              projectId,
              instanceId,
              backupId,
              databaseId,
              kmsKeyName);
        }
      }
    
      static Void restoreBackupWithEncryptionKey([DatabaseAdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.admin.database.v1.DatabaseAdminClient.html) adminClient,
          String projectId, String instanceId, String backupId, String restoreId, String kmsKeyName) {
        [RestoreDatabaseRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.RestoreDatabaseRequest.html) request =
            [RestoreDatabaseRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.RestoreDatabaseRequest.html).newBuilder()
                .setParent([InstanceName](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.InstanceName.html).of(projectId, instanceId).toString())
                .[setDatabaseId](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.RestoreDatabaseRequest.Builder.html#com_google_spanner_admin_database_v1_RestoreDatabaseRequest_Builder_setDatabaseId_java_lang_String_)(restoreId)
                .setBackup([BackupName](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.BackupName.html).of(projectId, instanceId, backupId).toString())
                .setEncryptionConfig([RestoreDatabaseEncryptionConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.RestoreDatabaseEncryptionConfig.html).newBuilder()
                    .setEncryptionType(CUSTOMER_MANAGED_ENCRYPTION).setKmsKeyName(kmsKeyName)).build();
        [Database](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.Database.html) database;
        try {
          System.out.println("Waiting for operation to complete...");
          database = adminClient.[restoreDatabaseAsync](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.admin.database.v1.DatabaseAdminClient.html#com_google_cloud_spanner_admin_database_v1_DatabaseAdminClient_restoreDatabaseAsync__org_jspecify_annotations_Nullable_com_google_spanner_admin_database_v1_InstanceName_java_lang_String__org_jspecify_annotations_Nullable_com_google_spanner_admin_database_v1_BackupName_)(request).get();
          ;
        } catch (ExecutionException e) {
          // If the operation failed during execution, expose the cause.
          throw [SpannerExceptionFactory](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.SpannerExceptionFactory.html).[asSpannerException](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.SpannerExceptionFactory.html#com_google_cloud_spanner_SpannerExceptionFactory_asSpannerException_java_lang_Throwable_)(e.getCause());
        } catch (InterruptedException e) {
          // Throw when a thread is waiting, sleeping, or otherwise occupied,
          // and the thread is interrupted, either before or during the activity.
          throw [SpannerExceptionFactory](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.SpannerExceptionFactory.html).[propagateInterrupt](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.SpannerExceptionFactory.html#com_google_cloud_spanner_SpannerExceptionFactory_propagateInterrupt_java_lang_InterruptedException_)(e);
        }
    
        System.out.printf(
            "Database %s restored to %s from backup %s using encryption key %s%n",
            database.[getRestoreInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.Database.html#com_google_spanner_admin_database_v1_Database_getRestoreInfo__)().getBackupInfo().getSourceDatabase(),
            database.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.Database.html#com_google_spanner_admin_database_v1_Database_getName__)(),
            database.[getRestoreInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.Database.html#com_google_spanner_admin_database_v1_Database_getRestoreInfo__)().getBackupInfo().getBackup(),
            database.[getEncryptionConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.Database.html#com_google_spanner_admin_database_v1_Database_getEncryptionConfig__)().getKmsKeyName()
        );
        return null;
      }
    }

To restore a CMEK-enabled backup in a multi-region instance configuration:
    
    
    import static com.google.spanner.admin.database.v1.[RestoreDatabaseEncryptionConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.RestoreDatabaseEncryptionConfig.html).EncryptionType.CUSTOMER_MANAGED_ENCRYPTION;
    
    import com.google.cloud.spanner.[Spanner](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.Spanner.html);
    import com.google.cloud.spanner.[SpannerExceptionFactory](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.SpannerExceptionFactory.html);
    import com.google.cloud.spanner.[SpannerOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.SpannerOptions.html);
    import com.google.cloud.spanner.admin.database.v1.[DatabaseAdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.admin.database.v1.DatabaseAdminClient.html);
    import com.google.common.collect.ImmutableList;
    import com.google.spanner.admin.database.v1.[BackupName](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.BackupName.html);
    import com.google.spanner.admin.database.v1.[Database](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.Database.html);
    import com.google.spanner.admin.database.v1.[InstanceName](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.InstanceName.html);
    import com.google.spanner.admin.database.v1.[RestoreDatabaseEncryptionConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.RestoreDatabaseEncryptionConfig.html);
    import com.google.spanner.admin.database.v1.[RestoreDatabaseRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.RestoreDatabaseRequest.html);
    import java.util.concurrent.ExecutionException;
    
    public class RestoreBackupWithMultiRegionEncryptionKey {
    
      static void restoreBackupWithMultiRegionEncryptionKey() {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "my-project";
        String instanceId = "my-instance";
        String databaseId = "my-database";
        String backupId = "my-backup";
        String[] kmsKeyNames =
            new String[] {
              "projects/" + projectId + "/locations/<location1>/keyRings/<keyRing>/cryptoKeys/<keyId>",
              "projects/" + projectId + "/locations/<location2>/keyRings/<keyRing>/cryptoKeys/<keyId>",
              "projects/" + projectId + "/locations/<location3>/keyRings/<keyRing>/cryptoKeys/<keyId>"
            };
    
        try ([Spanner](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.Spanner.html) spanner =
                [SpannerOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.SpannerOptions.html).newBuilder().setProjectId(projectId).build().getService();
            [DatabaseAdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.admin.database.v1.DatabaseAdminClient.html) adminClient = spanner.[createDatabaseAdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.Spanner.html#com_google_cloud_spanner_Spanner_createDatabaseAdminClient__)()) {
          restoreBackupWithMultiRegionEncryptionKey(
              adminClient, projectId, instanceId, backupId, databaseId, kmsKeyNames);
        }
      }
    
      static Void restoreBackupWithMultiRegionEncryptionKey(
          [DatabaseAdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.admin.database.v1.DatabaseAdminClient.html) adminClient,
          String projectId,
          String instanceId,
          String backupId,
          String restoreId,
          String[] kmsKeyNames) {
        [RestoreDatabaseRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.RestoreDatabaseRequest.html) request =
            [RestoreDatabaseRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.RestoreDatabaseRequest.html).newBuilder()
                .setParent([InstanceName](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.InstanceName.html).of(projectId, instanceId).toString())
                .[setDatabaseId](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.RestoreDatabaseRequest.Builder.html#com_google_spanner_admin_database_v1_RestoreDatabaseRequest_Builder_setDatabaseId_java_lang_String_)(restoreId)
                .setBackup([BackupName](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.BackupName.html).of(projectId, instanceId, backupId).toString())
                .setEncryptionConfig(
                    [RestoreDatabaseEncryptionConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.RestoreDatabaseEncryptionConfig.html).newBuilder()
                        .setEncryptionType(CUSTOMER_MANAGED_ENCRYPTION)
                        .addAllKmsKeyNames(ImmutableList.copyOf(kmsKeyNames)))
                .build();
        [Database](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.Database.html) database;
        try {
          System.out.println("Waiting for operation to complete...");
          database = adminClient.[restoreDatabaseAsync](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.admin.database.v1.DatabaseAdminClient.html#com_google_cloud_spanner_admin_database_v1_DatabaseAdminClient_restoreDatabaseAsync__org_jspecify_annotations_Nullable_com_google_spanner_admin_database_v1_InstanceName_java_lang_String__org_jspecify_annotations_Nullable_com_google_spanner_admin_database_v1_BackupName_)(request).get();
          ;
        } catch (ExecutionException e) {
          // If the operation failed during execution, expose the cause.
          throw [SpannerExceptionFactory](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.SpannerExceptionFactory.html).[asSpannerException](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.SpannerExceptionFactory.html#com_google_cloud_spanner_SpannerExceptionFactory_asSpannerException_java_lang_Throwable_)(e.getCause());
        } catch (InterruptedException e) {
          // Throw when a thread is waiting, sleeping, or otherwise occupied,
          // and the thread is interrupted, either before or during the activity.
          throw [SpannerExceptionFactory](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.SpannerExceptionFactory.html).[propagateInterrupt](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.SpannerExceptionFactory.html#com_google_cloud_spanner_SpannerExceptionFactory_propagateInterrupt_java_lang_InterruptedException_)(e);
        }
    
        System.out.printf(
            "Database %s restored to %s from backup %s using encryption keys %s%n",
            database.[getRestoreInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.Database.html#com_google_spanner_admin_database_v1_Database_getRestoreInfo__)().getBackupInfo().getSourceDatabase(),
            database.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.Database.html#com_google_spanner_admin_database_v1_Database_getName__)(),
            database.[getRestoreInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.Database.html#com_google_spanner_admin_database_v1_Database_getRestoreInfo__)().getBackupInfo().getBackup(),
            database.[getEncryptionConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.Database.html#com_google_spanner_admin_database_v1_Database_getEncryptionConfig__)().getKmsKeyNamesList());
        return null;
      }
    }

**Note:** The old client library interface code samples for Java are archived in [GitHub](https://github.com/googleapis/google-cloud-java/tree/main/java-spanner/samples/snippets/src/main/java/com/example/spanner/admin/archived). 

### Node.js

To restore a CMEK-enabled backup in a regional instance configuration:
    
    
    // Imports the Google Cloud client library and precise date library
    const {Spanner} = require('[@google-cloud/spanner](https://docs.cloud.google.com/nodejs/docs/reference/spanner/latest/overview.html)');
    
    /**
     * TODO(developer): Uncomment the following lines before running the sample.
     */
    // const projectId = 'my-project-id';
    // const instanceId = 'my-instance';
    // const databaseId = 'my-database';
    // const backupId = 'my-backup';
    // const keyName =
    //   'projects/my-project-id/my-region/keyRings/my-key-ring/cryptoKeys/my-key';
    
    // Creates a client
    const spanner = new [Spanner](https://docs.cloud.google.com/nodejs/docs/reference/spanner/latest/spanner/spanner.html)({
      projectId: projectId,
    });
    
    // Gets a reference to a Cloud Spanner Database Admin Client object
    const databaseAdminClient = spanner.[getDatabaseAdminClient](https://docs.cloud.google.com/nodejs/docs/reference/spanner/latest/spanner/spanner.html)();
    
    // Restore the database
    console.log(
      `Restoring database ${databaseAdminClient.databasePath(
        projectId,
        instanceId,
        databaseId,
      )} from backup ${backupId}.`,
    );
    const [restoreOperation] = await databaseAdminClient.restoreDatabase({
      parent: databaseAdminClient.instancePath(projectId, instanceId),
      databaseId: databaseId,
      backup: databaseAdminClient.backupPath(projectId, instanceId, backupId),
      encryptionConfig: {
        encryptionType: 'CUSTOMER_MANAGED_ENCRYPTION',
        kmsKeyName: keyName,
      },
    });
    
    // Wait for restore to complete
    console.log('Waiting for database restore to complete...');
    await restoreOperation.promise();
    
    console.log('Database restored from backup.');
    const [metadata] = await databaseAdminClient.getDatabase({
      name: databaseAdminClient.databasePath(projectId, instanceId, databaseId),
    });
    console.log(
      `Database ${metadata.restoreInfo.backupInfo.sourceDatabase} was restored ` +
        `to ${databaseId} from backup ${metadata.restoreInfo.backupInfo.backup} ` +
        `using encryption key ${metadata.encryptionConfig.kmsKeyName}.`,
    );

To restore a CMEK-enabled backup in a multi-region instance configuration:
    
    
    /**
     * TODO(developer): Uncomment the following lines before running the sample.
     */
    // const projectId = 'my-project-id';
    // const instanceId = 'my-instance';
    // const databaseId = 'my-database';
    // const backupId = 'my-backup';
    // const kmsKeyNames =
    //   'projects/my-project-id/my-region/keyRings/my-key-ring/cryptoKeys/my-key1,
    //   projects/my-project-id/my-region/keyRings/my-key-ring/cryptoKeys/my-key2';
    
    // Imports the Google Cloud client library and precise date library
    const {Spanner} = require('[@google-cloud/spanner](https://docs.cloud.google.com/nodejs/docs/reference/spanner/latest/overview.html)');
    
    // Creates a client
    const spanner = new [Spanner](https://docs.cloud.google.com/nodejs/docs/reference/spanner/latest/spanner/spanner.html)({
      projectId: projectId,
    });
    
    // Gets a reference to a Cloud Spanner Database Admin Client object
    const databaseAdminClient = spanner.[getDatabaseAdminClient](https://docs.cloud.google.com/nodejs/docs/reference/spanner/latest/spanner/spanner.html)();
    
    async function restoreBackupWithMultipleKmsKeys() {
      // Restore the database
      console.log(
        `Restoring database ${databaseAdminClient.databasePath(
          projectId,
          instanceId,
          databaseId,
        )} from backup ${backupId}.`,
      );
      const [restoreOperation] = await databaseAdminClient.restoreDatabase({
        parent: databaseAdminClient.instancePath(projectId, instanceId),
        databaseId: databaseId,
        backup: databaseAdminClient.backupPath(projectId, instanceId, backupId),
        encryptionConfig: {
          encryptionType: 'CUSTOMER_MANAGED_ENCRYPTION',
          kmsKeyNames: kmsKeyNames.split(','),
        },
      });
    
      // Wait for restore to complete
      console.log('Waiting for database restore to complete...');
      await restoreOperation.promise();
    
      console.log('Database restored from backup.');
      const [metadata] = await databaseAdminClient.getDatabase({
        name: databaseAdminClient.databasePath(projectId, instanceId, databaseId),
      });
      console.log(
        `Database ${metadata.restoreInfo.backupInfo.sourceDatabase} was restored ` +
          `to ${databaseId} from backup ${metadata.restoreInfo.backupInfo.backup} ` +
          `using encryption key ${metadata.encryptionConfig.kmsKeyNames}.`,
      );
    }
    restoreBackupWithMultipleKmsKeys();

**Note:** The old client library interface code samples for Node.js are archived in [GitHub](https://github.com/googleapis/nodejs-spanner/tree/main/samples/archived). 

### PHP

To restore a CMEK-enabled backup in a regional instance configuration:
    
    
    use Google\Cloud\Spanner\Admin\Database\V1\Client\DatabaseAdminClient;
    use Google\Cloud\Spanner\Admin\Database\V1\RestoreDatabaseEncryptionConfig;
    use Google\Cloud\Spanner\Admin\Database\V1\RestoreDatabaseRequest;
    
    /**
     * Restore a database from a backup.
     * Example:
     * ```
     * restore_backup_with_encryption_key($projectId, $instanceId, $databaseId, $backupId, $kmsKeyName);
     * ```
     * @param string $projectId The Google Cloud project ID.
     * @param string $instanceId The Spanner instance ID.
     * @param string $databaseId The Spanner database ID.
     * @param string $backupId The Spanner backup ID.
     * @param string $kmsKeyName The KMS key used for encryption.
     */
    function restore_backup_with_encryption_key(
        string $projectId,
        string $instanceId,
        string $databaseId,
        string $backupId,
        string $kmsKeyName
    ): void {
        $databaseAdminClient = new DatabaseAdminClient();
        $instanceFullName = DatabaseAdminClient::instanceName($projectId, $instanceId);
        $backupFullName = DatabaseAdminClient::backupName($projectId, $instanceId, $backupId);
        $request = new RestoreDatabaseRequest([
            'parent' => $instanceFullName,
            'database_id' => $databaseId,
            'backup' => $backupFullName,
            'encryption_config' => new RestoreDatabaseEncryptionConfig([
                'kms_key_name' => $kmsKeyName,
                'encryption_type' => RestoreDatabaseEncryptionConfig\EncryptionType::CUSTOMER_MANAGED_ENCRYPTION
            ])
        ]);
    
        // Create restore operation
        $operation = $databaseAdminClient->restoreDatabase($request);
    
        print('Waiting for operation to complete...' . PHP_EOL);
        $operation->pollUntilComplete();
    
        // Reload new database and get restore info
        $database = $operation->operationSucceeded() ? $operation->getResult() : null;
        $restoreInfo = $database->getRestoreInfo();
        $backupInfo = $restoreInfo->getBackupInfo();
        $sourceDatabase = $backupInfo->getSourceDatabase();
        $sourceBackup = $backupInfo->getBackup();
        $encryptionConfig = $database->getEncryptionConfig();
        printf(
            'Database %s restored from backup %s using encryption key %s' . PHP_EOL,
            $sourceDatabase, $sourceBackup, $encryptionConfig->getKmsKeyName()
        );
    }

To restore a CMEK-enabled backup in a multi-region instance configuration:
    
    
    use Google\Cloud\Spanner\Admin\Database\V1\Client\DatabaseAdminClient;
    use Google\Cloud\Spanner\Admin\Database\V1\RestoreDatabaseEncryptionConfig;
    use Google\Cloud\Spanner\Admin\Database\V1\RestoreDatabaseRequest;
    
    /**
     * Restore a MR CMEK database from a backup.
     * Example:
     * ```
     * restore_backup_with_mr_cmek($projectId, $instanceId, $databaseId, $backupId, $kmsKeyNames);
     * ```
     * @param string $projectId The Google Cloud project ID.
     * @param string $instanceId The Spanner instance ID.
     * @param string $databaseId The Spanner database ID.
     * @param string $backupId The Spanner backup ID.
     * @param string[] $kmsKeyNames The KMS keys used for encryption.
     */
    function restore_backup_with_mr_cmek(
        string $projectId,
        string $instanceId,
        string $databaseId,
        string $backupId,
        array $kmsKeyNames
    ): void {
        $databaseAdminClient = new DatabaseAdminClient();
        $instanceFullName = DatabaseAdminClient::instanceName($projectId, $instanceId);
        $backupFullName = DatabaseAdminClient::backupName($projectId, $instanceId, $backupId);
        $request = new RestoreDatabaseRequest([
            'parent' => $instanceFullName,
            'database_id' => $databaseId,
            'backup' => $backupFullName,
            'encryption_config' => new RestoreDatabaseEncryptionConfig([
                'kms_key_names' => $kmsKeyNames,
                'encryption_type' => RestoreDatabaseEncryptionConfig\EncryptionType::CUSTOMER_MANAGED_ENCRYPTION
            ])
        ]);
    
        // Create restore operation
        $operation = $databaseAdminClient->restoreDatabase($request);
    
        print('Waiting for operation to complete...' . PHP_EOL);
        $operation->pollUntilComplete();
    
        // Reload new database and get restore info
        $database = $operation->operationSucceeded() ? $operation->getResult() : null;
        $restoreInfo = $database->getRestoreInfo();
        $backupInfo = $restoreInfo->getBackupInfo();
        $sourceDatabase = $backupInfo->getSourceDatabase();
        $sourceBackup = $backupInfo->getBackup();
        $encryptionConfig = $database->getEncryptionConfig();
        printf(
            'Database %s restored from backup %s using encryption keys %s' . PHP_EOL,
            $sourceDatabase, $sourceBackup, print_r($encryptionConfig->getKmsKeyNames(), true)
        );
    }

**Note:** The old client library interface code samples for PHP are archived in [GitHub](https://github.com/GoogleCloudPlatform/php-docs-samples/tree/main/spanner/src/admin/archived). 

### Python

To restore a CMEK-enabled backup in a regional instance configuration:
    
    
    def restore_database_with_encryption_key(
        instance_id, new_database_id, backup_id, kms_key_name
    ):
        """Restores a database from a backup using a Customer Managed Encryption Key (CMEK)."""
        from google.cloud.spanner_admin_database_v1 import (
            [RestoreDatabaseEncryptionConfig](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.RestoreDatabaseEncryptionConfig.html),
            [RestoreDatabaseRequest](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.RestoreDatabaseRequest.html),
        )
    
        spanner_client = spanner.Client()
        database_admin_api = spanner_client.database_admin_api
    
        # Start restoring an existing backup to a new database.
        encryption_config = {
            "encryption_type": [RestoreDatabaseEncryptionConfig](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.RestoreDatabaseEncryptionConfig.html).EncryptionType.CUSTOMER_MANAGED_ENCRYPTION,
            "kms_key_name": kms_key_name,
        }
    
        request = RestoreDatabaseRequest(
            parent=database_admin_api.instance_path(spanner_client.project, instance_id),
            database_id=new_database_id,
            backup=database_admin_api.backup_path(
                spanner_client.project, instance_id, backup_id
            ),
            encryption_config=encryption_config,
        )
        operation = database_admin_api.restore_database(request)
    
        # Wait for restore operation to complete.
        db = operation.result(1600)
    
        # Newly created database has restore information.
        restore_info = db.restore_info
        print(
            "Database {} restored to {} from backup {} with using encryption key {}.".format(
                restore_info.backup_info.source_database,
                new_database_id,
                restore_info.backup_info.backup,
                db.encryption_config.kms_key_name,
            )
        )
    
    

To restore a CMEK-enabled backup in a multi-region instance configuration:
    
    
    def restore_database_with_multiple_kms_keys(
        instance_id, new_database_id, backup_id, kms_key_names
    ):
        """Restores a database from a backup using a Customer Managed Encryption Key (CMEK)."""
        from google.cloud.spanner_admin_database_v1 import (
            [RestoreDatabaseEncryptionConfig](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.RestoreDatabaseEncryptionConfig.html),
            [RestoreDatabaseRequest](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.RestoreDatabaseRequest.html),
        )
    
        spanner_client = spanner.Client()
        database_admin_api = spanner_client.database_admin_api
    
        # Start restoring an existing backup to a new database.
        encryption_config = {
            "encryption_type": [RestoreDatabaseEncryptionConfig](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.RestoreDatabaseEncryptionConfig.html).EncryptionType.CUSTOMER_MANAGED_ENCRYPTION,
            "kms_key_names": kms_key_names,
        }
    
        request = RestoreDatabaseRequest(
            parent=database_admin_api.instance_path(spanner_client.project, instance_id),
            database_id=new_database_id,
            backup=database_admin_api.backup_path(
                spanner_client.project, instance_id, backup_id
            ),
            encryption_config=encryption_config,
        )
        operation = database_admin_api.restore_database(request)
    
        # Wait for restore operation to complete.
        db = operation.result(1600)
    
        # Newly created database has restore information.
        restore_info = db.restore_info
        print(
            "Database {} restored to {} from backup {} with using encryption key {}.".format(
                restore_info.backup_info.source_database,
                new_database_id,
                restore_info.backup_info.backup,
                db.encryption_config.kms_key_names,
            )
        )
    
    

**Note:** The old client library interface code samples for Python are archived in [GitHub](https://github.com/googleapis/python-spanner/tree/main/samples/samples/archived). 

### Ruby

To restore a CMEK-enabled backup in a regional instance configuration:
    
    
    # project_id  = "Your Google Cloud project ID"
    # instance_id = "Your Spanner instance ID"
    # database_id = "Your Spanner database ID of where to restore"
    # backup_id = "Your Spanner backup ID"
    # kms_key_name = "Your backup encryption database KMS key"
    
    require "google/cloud/spanner"
    require "google/cloud/spanner/admin/database"
    
    database_admin_client = Google::Cloud::Spanner::Admin::Database.database_admin
    
    instance_path = database_admin_client.instance_path project: project_id, instance: instance_id
    
    db_path = database_admin_client.database_path project: project_id,
                                                  instance: instance_id,
                                                  database: database_id
    
    backup_path = database_admin_client.backup_path project: project_id,
                                                    instance: instance_id,
                                                    backup: backup_id
    
    encryption_config = {
      encryption_type: :CUSTOMER_MANAGED_ENCRYPTION,
      kms_key_name:    kms_key_name
    }
    job = database_admin_client.restore_database parent: instance_path,
                                                 database_id: database_id,
                                                 backup: backup_path,
                                                 encryption_config: encryption_config
    
    puts "Waiting for restore backup operation to complete"
    
    job.wait_until_done!
    database = database_admin_client.get_database name: db_path
    restore_info = database.restore_info
    puts "Database #{restore_info.backup_info.source_database} was restored to #{database_id} from backup #{restore_info.backup_info.backup} using encryption key #{database.encryption_config.kms_key_name}"
    

To restore a CMEK-enabled backup in a multi-region instance configuration:
    
    
    # project_id  = "Your Google Cloud project ID"
    # instance_id = "Your Spanner instance ID"
    # database_id = "Your Spanner database ID of where to restore"
    # backup_id = "Your Spanner backup ID"
    # kms_key_names = ["key1", "key2", "key3"]
    
    require "google/cloud/spanner"
    require "google/cloud/spanner/admin/database"
    
    database_admin_client = Google::Cloud::Spanner::Admin::Database.database_admin
    
    instance_path = database_admin_client.instance_path(
      project: project_id, instance: instance_id
    )
    
    db_path = database_admin_client.database_path project: project_id,
                                                  instance: instance_id,
                                                  database: database_id
    
    backup_path = database_admin_client.backup_path project: project_id,
                                                    instance: instance_id,
                                                    backup: backup_id
    
    encryption_config = {
      encryption_type: :CUSTOMER_MANAGED_ENCRYPTION,
      kms_key_names:    kms_key_names
    }
    job = database_admin_client.restore_database(
      parent: instance_path,
      database_id: database_id,
      backup: backup_path,
      encryption_config: encryption_config
    )
    
    puts "Waiting for restore backup operation to complete"
    
    job.wait_until_done!
    database = database_admin_client.get_database name: db_path
    restore_info = database.restore_info
    puts "Database #{restore_info.backup_info.source_database} was restored " \
         "to #{database_id} from backup #{restore_info.backup_info.backup} " \
         "using encryption key #{database.encryption_config.kms_key_names}"
    

## View audit logs for the Cloud KMS key

  1. Make sure that [logging is enabled ](https://docs.cloud.google.com/logging/docs/audit/configure-data-access#config-console-enable) for the Cloud KMS API in your project.

  2. In the Google Cloud console, go to **Logs Explorer**.

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

  3. Limit the log entries to your Cloud KMS key by adding the following lines to the Query builder:
         
         resource.type="cloudkms_cryptokey"
         resource.labels.location="KMS_KEY_LOCATION"
         resource.labels.key_ring_id="KMS_KEY_RING_ID"
         resource.labels.crypto_key_id="KMS_KEY_ID"
         

Under normal operations, encrypt and decrypt actions are logged with `INFO` severity. These entries are logged as the zones in your Spanner instance poll the Cloud KMS key about every five minutes.

If Spanner fails to access the key, the operations are logged as `ERROR`.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
