---
url: https://docs.cloud.google.com/sql/docs/postgres/client-side-encryption/
title: About client-side encryption \u00a0|\u00a0 Cloud SQL for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:53:12.636626+00:00
---

# About client-side encryption  |  Cloud SQL for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/postgres/client-side-encryption/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ PostgreSQL ](https://docs.cloud.google.com/sql/docs/postgres)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/postgres/features)



Send feedback 

#  About client-side encryption Stay organized with collections  Save and categorize content based on your preferences. 

[MySQL](https://docs.cloud.google.com/sql/docs/mysql/client-side-encryption "View this page for the MySQL database engine") | PostgreSQL | [SQL Server](https://docs.cloud.google.com/sql/docs/sqlserver/client-side-encryption "View this page for the SQL Server database engine")

This page describes how to implement client-side encryption on Cloud SQL.

## Overview

Client-side encryption is the act of encrypting data before writing it to Cloud SQL. You can encrypt Cloud SQL data in a manner that only your application can decrypt.

To enable client-side encryption you have the following options:

  1. Using an encryption key stored in the Cloud Key Management Service (Cloud KMS).
  2. Using an encryption key stored locally in your application.



In this document, we describe how to use the first option, which provides the most seamless key management option. We create an encryption key in Cloud KMS and implement [envelope encryption](https://docs.cloud.google.com/kms/docs/envelope-encryption) using [Tink](https://github.com/tink-crypto), Google's open source cryptographic library.

### Why do you need client-side encryption?

You need client-side encryption if you want to protect Cloud SQL data at the column level. Imagine you have a table of names and credit card numbers. You want to grant a user access to this table, but you don't want them to view the credit card numbers. You can encrypt the numbers using client-side encryption. As long as the user is not granted access to the encryption key in Cloud KMS, they can't read the credit card information.

You can also restrict access at the [instance](https://docs.cloud.google.com/sql/docs/postgres/instance-access-control#instanceaccess) or [database](https://docs.cloud.google.com/sql/docs/postgres/instance-access-control#MySQLaccess) level.

### Create keys using Cloud KMS

Cloud KMS lets you create and manage keys on Google Cloud.

Cloud KMS supports many different key types. For client-side encryption, you need to create a [symmetric key](https://docs.cloud.google.com/kms/docs/creating-keys).

To give your application access to the key in Cloud KMS, you need to grant the service account that your application uses with the `cloudkms.cryptoKeyEncrypterDecrypter` role. In [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud), you use the following command to do this:
    
    
    gcloud kms keys add-iam-policy-binding key \
    --keyring=key-ring \
    --location=location \
    --member=serviceAccount:service-account-name@example.domain.com \
    --role=roles/cloudkms.cryptoKeyEncrypterDecrypter

While you can use the KMS key to directly [encrypt data](https://docs.cloud.google.com/kms/docs/encrypt-decrypt), here we use a more flexible solution called _envelope encryption_. This allows us to encrypt messages longer than 64KB, which is the maximum message size that the Cloud Key Management Service API can support.

### Cloud KMS envelope encryption

In envelope encryption, the KMS key acts as a key encrypting key (KEK). That is, it is used to encrypt data encryption keys (DEK) which in turn are used to encrypt actual data.

After creating a KEK in Cloud KMS, to encrypt each message you need to:

  * Generate a data encryption key (DEK) locally.
  * Use this DEK locally to encrypt the message.
  * Call Cloud KMS to encrypt (wrap) the DEK with the KEK.
  * Store the encrypted data and the wrapped DEK.



Instead of implementing envelope encryption from scratch, in this document we use Tink.

### Tink

Tink is a multi-language, cross-platform library that provides high-level cryptographic APIs. To encrypt data with Tink's envelope encryption, you provide Tink with a key URI pointing to your KEK in Cloud KMS, and credentials that allow Tink to use the KEK. Tink generates the DEK, encrypts the data, wraps the DEK and returns a single ciphertext with the encrypted data and wrapped DEK.

Tink supports envelope encryption in C++, Java, Go, and Python using the AEAD API:
    
    
    public interface Aead{
      byte[] encrypt(final byte[] plaintext, final byte[] associatedData)
      throws…
      byte[] decrypt(final byte[] ciphertext, final byte[] associatedData)
      throws…
    }
    

Besides the normal message/ciphertext argument, the encrypt and decrypt methods support optional associated data. This argument can be used to tie the ciphertext to a piece of data. For example, suppose you have a database with a field `user-id` and a field `encrypted-medical-history`. In this case, the field `user-id` should probably be used as associated data when encrypting the medical history. This ensures that an attacker cannot move medical history from one user to another. It is also used to verify that you have the correct row of data when you run a query.

## Samples

In this section, we'll walk through sample code for a voter information database that uses client-side encryption. The sample code shows how to:

  * Create a database table and connection pool
  * Set up Tink for envelope encryption
  * Encrypt and decrypt data using Tink's envelope encryption with a KEK in Cloud KMS



### Before you begin

  1. Create a Cloud SQL Instance by following these [instructions](https://docs.cloud.google.com/sql/docs/postgres/create-instance). Note the connection string, database user, and database password that you create.

  2. Create a database for your application by following these [instructions](https://docs.cloud.google.com/sql/docs/postgres/create-manage-databases). Note the database name.

  3. Create a KMS key for your application by following these [instructions](https://docs.cloud.google.com/kms/docs/creating-keys). Copy the resource name of your created key.

  4. Create a service account with the 'Cloud SQL Client' permissions by following these [instructions](https://docs.cloud.google.com/sql/docs/postgres/connect-external-app#4_if_required_by_your_authentication_method_create_a_service_account).

  5. Add the 'Cloud KMS CryptoKey Encrypter/Decrypter' permission for the key to your service account by following these [instructions](https://docs.cloud.google.com/kms/docs/iam).




### Create a connection pool and create a new table in the database

### Java
    
    
    import com.zaxxer.hikari.HikariConfig;
    import com.zaxxer.hikari.HikariDataSource;
    import java.security.GeneralSecurityException;
    import java.sql.Connection;
    import java.sql.PreparedStatement;
    import java.sql.SQLException;
    import javax.sql.DataSource;
    
    public class CloudSqlConnectionPool {
    
      public static DataSource createConnectionPool(String dbUser, String dbPass, String dbName,
          String instanceConnectionName) throws GeneralSecurityException {
        HikariConfig config = new HikariConfig();
        config.setJdbcUrl(String.format("jdbc:postgresql:///%s", dbName));
        config.setUsername(dbUser); // e.g. "root", "postgres"
        config.setPassword(dbPass); // e.g. "my-password"
        config.addDataSourceProperty("socketFactory", "com.google.cloud.sql.postgres.SocketFactory");
        config.addDataSourceProperty("cloudSqlInstance", instanceConnectionName);
        DataSource pool = new HikariDataSource(config);
        return pool;
      }
    
      public static void createTable(DataSource pool, String tableName) throws SQLException {
        // Safely attempt to create the table schema.
        try (Connection conn = pool.getConnection()) {
          String stmt = String.format("CREATE TABLE IF NOT EXISTS %s ( "
              + "vote_id SERIAL NOT NULL, time_cast timestamp NOT NULL, team CHAR(6) NOT NULL,"
              + "voter_email BYTEA, PRIMARY KEY (vote_id) );", tableName);
          try (PreparedStatement createTableStatement = conn.prepareStatement(stmt);) {
            createTableStatement.execute();
          }
        }
      }
    }

### Python
    
    
    import sqlalchemy
    
    
    def init_tcp_connection_engine(
        db_user: str, db_pass: str, db_name: str, db_host: str
    ) -> sqlalchemy.engine.base.Engine:
        """
        Creates a connection to the database using tcp socket.
        """
        # Remember - storing secrets in plaintext is potentially unsafe. Consider using
        # something like https://cloud.google.com/secret-manager/docs/overview to help keep
        # secrets secret.
    
        # Extract host and port from db_host
        host_args = db_host.split(":")
        db_hostname, db_port = host_args[0], int(host_args[1])
    
        pool = sqlalchemy.create_engine(
            # Equivalent URL:
            # postgresql+pg8000://<db_user>:<db_pass>@<db_host>:<db_port>/<db_name>
            sqlalchemy.engine.url.URL.create(
                drivername="postgresql+pg8000",
                username=db_user,  # e.g. "my-database-user"
                password=db_pass,  # e.g. "my-database-password"
                host=db_hostname,  # e.g. "127.0.0.1"
                port=db_port,  # e.g. 5432
                database=db_name,  # e.g. "my-database-name"
            ),
        )
        print("Created TCP connection pool")
        return pool
    
    
    def init_unix_connection_engine(
        db_user: str,
        db_pass: str,
        db_name: str,
        instance_connection_name: str,
        db_socket_dir: str,
    ) -> sqlalchemy.engine.base.Engine:
        """
        Creates a connection to the database using unix socket.
        """
        # Remember - storing secrets in plaintext is potentially unsafe. Consider using
        # something like https://cloud.google.com/secret-manager/docs/overview to help keep
        # secrets secret.
    
        pool = sqlalchemy.create_engine(
            # Equivalent URL:
            # mpostgresql+pg8000://<db_user>:<db_pass>@/<db_name>?unix_socket=<socket_path>/<cloud_sql_instance_name>
            sqlalchemy.engine.url.URL.create(
                drivername="postgresql+pg8000",
                username=db_user,  # e.g. "my-database-user"
                password=db_pass,  # e.g. "my-database-password"
                database=db_name,  # e.g. "my-database-name"
                query={
                    "unix_sock": "{}/{}/.s.PGSQL.5432".format(
                        db_socket_dir, instance_connection_name  # e.g. "/cloudsql"
                    )  # i.e "<PROJECT-NAME>:<INSTANCE-REGION>:<INSTANCE-NAME>"
                },
            ),
        )
        print("Created Unix socket connection pool")
        return pool
    
    
    def init_db(
        db_user: str,
        db_pass: str,
        db_name: str,
        table_name: str,
        instance_connection_name: str = None,
        db_socket_dir: str = None,
        db_host: str = None,
    ) -> sqlalchemy.engine.base.Engine:
        """Starts a connection to the database and creates voting table if it doesn't exist."""
    
        if db_host:
            db = init_tcp_connection_engine(db_user, db_pass, db_name, db_host)
        else:
            db = init_unix_connection_engine(
                db_user, db_pass, db_name, instance_connection_name, db_socket_dir
            )
    
        # Create tables (if they don't already exist)
        with db.connect() as conn:
            conn.execute(
                f"CREATE TABLE IF NOT EXISTS {table_name} "
                "( vote_id SERIAL NOT NULL, time_cast timestamp NOT NULL, "
                "team VARCHAR(6) NOT NULL, voter_email BYTEA, "
                "PRIMARY KEY (vote_id) );"
            )
    
        print(f"Created table {table_name} in db {db_name}")
        return db
    
    

### Initialize an envelope AEAD primitive with Tink

### Java
    
    
    import com.google.crypto.tink.Aead;
    import com.google.crypto.tink.KmsClient;
    import com.google.crypto.tink.aead.AeadConfig;
    import com.google.crypto.tink.aead.AeadKeyTemplates;
    import com.google.crypto.tink.aead.KmsEnvelopeAead;
    import com.google.crypto.tink.integration.gcpkms.GcpKmsClient;
    import java.security.GeneralSecurityException;
    
    public class CloudKmsEnvelopeAead {
    
      public static Aead get(String kmsUri) throws GeneralSecurityException {
        AeadConfig.register();
    
        // Create a new KMS Client
        KmsClient client = new GcpKmsClient().withDefaultCredentials();
    
        // Create an AEAD primitive using the Cloud KMS key
        Aead gcpAead = client.getAead(kmsUri);
    
        // Create an envelope AEAD primitive.
        // This key should only be used for client-side encryption to ensure authenticity and integrity
        // of data.
        return new KmsEnvelopeAead(AeadKeyTemplates.AES128_GCM, gcpAead);
      }
    }

### Python
    
    
    import logging
    
    import tink
    from tink import aead
    from tink.integration import gcpkms
    
    logger = logging.getLogger(__name__)
    
    
    def init_tink_env_aead(key_uri: str, credentials: str) -> tink.aead.KmsEnvelopeAead:
        """
        Initiates the Envelope AEAD object using the KMS credentials.
        """
        aead.register()
    
        try:
            gcp_client = gcpkms.GcpKmsClient(key_uri, credentials)
            gcp_aead = gcp_client.get_aead(key_uri)
        except tink.TinkError as e:
            logger.error("Error initializing GCP client: %s", e)
            raise e
    
        # Create envelope AEAD primitive using AES256 GCM for encrypting the data
        # This key should only be used for client-side encryption to ensure authenticity and integrity
        # of data.
        key_template = aead.aead_key_templates.AES256_GCM
        env_aead = aead.KmsEnvelopeAead(key_template, gcp_aead)
    
        print(f"Created envelope AEAD Primitive using KMS URI: {key_uri}")
    
        return env_aead
    
    

### Encrypt data and insert it into the database

### Java
    
    
    import com.google.crypto.tink.Aead;
    import java.security.GeneralSecurityException;
    import java.sql.Connection;
    import java.sql.PreparedStatement;
    import java.sql.SQLException;
    import java.sql.Timestamp;
    import java.util.Date;
    import javax.sql.DataSource;
    
    public class EncryptAndInsertData {
    
      public static void main(String[] args) throws GeneralSecurityException, SQLException {
        // Saving credentials in environment variables is convenient, but not secure - consider a more
        // secure solution such as Cloud Secret Manager to help keep secrets safe.
        String dbUser = System.getenv("DB_USER"); // e.g. "root", "postgres"
        String dbPass = System.getenv("DB_PASS"); // e.g. "mysupersecretpassword"
        String dbName = System.getenv("DB_NAME"); // e.g. "votes_db"
        String instanceConnectionName =
            System.getenv("INSTANCE_CONNECTION_NAME"); // e.g. "project-name:region:instance-name"
        String kmsUri = System.getenv("CLOUD_KMS_URI"); // e.g. "gcp-kms://projects/...path/to/key
        // Tink uses the "gcp-kms://" prefix for paths to keys stored in Google Cloud KMS. For more
        // info on creating a KMS key and getting its path, see
        // https://cloud.google.com/kms/docs/quickstart
    
        String team = "TABS";
        String tableName = "votes";
        String email = "hello@example.com";
    
        // Initialize database connection pool and create table if it does not exist
        // See CloudSqlConnectionPool.java for setup details
        DataSource pool =
            CloudSqlConnectionPool.createConnectionPool(dbUser, dbPass, dbName, instanceConnectionName);
        CloudSqlConnectionPool.createTable(pool, tableName);
    
        // Initialize envelope AEAD
        // See CloudKmsEnvelopeAead.java for setup details
        Aead envAead = CloudKmsEnvelopeAead.get(kmsUri);
    
        encryptAndInsertData(pool, envAead, tableName, team, email);
      }
    
      public static void encryptAndInsertData(
          DataSource pool, Aead envAead, String tableName, String team, String email)
          throws GeneralSecurityException, SQLException {
    
        try (Connection conn = pool.getConnection()) {
          String stmt =
              String.format(
                  "INSERT INTO %s (team, time_cast, voter_email) VALUES (?, ?, ?);", tableName);
          try (PreparedStatement voteStmt = conn.prepareStatement(stmt); ) {
            voteStmt.setString(1, team);
            voteStmt.setTimestamp(2, new Timestamp(new Date().getTime()));
    
            // Use the envelope AEAD primitive to encrypt the email, using the team name as
            // associated data. This binds the encryption of the email to the team name, preventing
            // associating an encrypted email in one row with a team name in another row.
            byte[] encryptedEmail = envAead.encrypt(email.getBytes(), team.getBytes());
            voteStmt.setBytes(3, encryptedEmail);
    
            // Finally, execute the statement. If it fails, an error will be thrown.
            voteStmt.execute();
            System.out.println(String.format("Successfully inserted row into table %s", tableName));
          }
        }
      }
    }

### Python
    
    
    import datetime
    import logging
    import os
    
    import sqlalchemy
    import tink
    
    from .cloud_kms_env_aead import init_tink_env_aead
    from .cloud_sql_connection_pool import init_db
    
    
    logger = logging.getLogger(__name__)
    
    
    def main() -> None:
        """
        Connects to the database, encrypts and inserts some data.
        """
        db_user = os.environ["DB_USER"]  # e.g. "root", "postgres"
        db_pass = os.environ["DB_PASS"]  # e.g. "mysupersecretpassword"
        db_name = os.environ["DB_NAME"]  # e.g. "votes_db"
    
        # Set if connecting using TCP:
        db_host = os.environ["DB_HOST"]  # e.g. "127.0.0.1"
    
        # Set if connecting using Unix sockets:
        db_socket_dir = os.environ.get("DB_SOCKET_DIR", "/cloudsql")
    
        instance_connection_name = os.environ["INSTANCE_CONNECTION_NAME"]
        # e.g. "project-name:region:instance-name"
    
        credentials = os.environ.get("GOOGLE_APPLICATION_CREDENTIALS", "")
        key_uri = "gcp-kms://" + os.environ["GCP_KMS_URI"]
        # e.g. "gcp-kms://projects/...path/to/key
        # Tink uses the "gcp-kms://" prefix for paths to keys stored in Google
        # Cloud KMS. For more info on creating a KMS key and getting its path, see
        # https://cloud.google.com/kms/docs/quickstart
    
        table_name = "votes"
        team = "TABS"
        email = "hello@example.com"
    
        env_aead = init_tink_env_aead(key_uri, credentials)
        db = init_db(
            db_user,
            db_pass,
            db_name,
            table_name,
            instance_connection_name,
            db_socket_dir,
            db_host,
        )
    
        encrypt_and_insert_data(db, env_aead, table_name, team, email)
    
    
    def encrypt_and_insert_data(
        db: sqlalchemy.engine.base.Engine,
        env_aead: tink.aead.KmsEnvelopeAead,
        table_name: str,
        team: str,
        email: str,
    ) -> None:
        """
        Inserts a vote into the database with email address previously encrypted using
        a KmsEnvelopeAead object.
        """
        time_cast = datetime.datetime.now(tz=datetime.timezone.utc)
        # Use the envelope AEAD primitive to encrypt the email, using the team name as
        # associated data. Encryption with associated data ensures authenticity
        # (who the sender is) and integrity (the data has not been tampered with) of that
        # data, but not its secrecy. (see RFC 5116 for more info)
        encrypted_email = env_aead.encrypt(email.encode(), team.encode())
        # Verify that the team is one of the allowed options
        if team != "TABS" and team != "SPACES":
            logger.error(f"Invalid team specified: {team}")
            return
    
        # Preparing a statement before hand can help protect against injections.
        stmt = sqlalchemy.text(
            f"INSERT INTO {table_name} (time_cast, team, voter_email)"
            " VALUES (:time_cast, :team, :voter_email)"
        )
    
        # Using a with statement ensures that the connection is always released
        # back into the pool at the end of statement (even if an error occurs)
        with db.connect() as conn:
            conn.execute(stmt, time_cast=time_cast, team=team, voter_email=encrypted_email)
        print(f"Vote successfully cast for '{team}' at time {time_cast}!")
    
    

### Query the database and decrypt the stored data

### Java
    
    
    import com.google.crypto.tink.Aead;
    import java.security.GeneralSecurityException;
    import java.sql.Connection;
    import java.sql.PreparedStatement;
    import java.sql.ResultSet;
    import java.sql.SQLException;
    import java.sql.Timestamp;
    import javax.sql.DataSource;
    
    public class QueryAndDecryptData {
    
      public static void main(String[] args) throws GeneralSecurityException, SQLException {
        // Saving credentials in environment variables is convenient, but not secure - consider a more
        // secure solution such as Cloud Secret Manager to help keep secrets safe.
        String dbUser = System.getenv("DB_USER"); // e.g. "root", "postgres"
        String dbPass = System.getenv("DB_PASS"); // e.g. "mysupersecretpassword"
        String dbName = System.getenv("DB_NAME"); // e.g. "votes_db"
        String instanceConnectionName =
            System.getenv("INSTANCE_CONNECTION_NAME"); // e.g. "project-name:region:instance-name"
        String kmsUri = System.getenv("CLOUD_KMS_URI"); // e.g. "gcp-kms://projects/...path/to/key
        // Tink uses the "gcp-kms://" prefix for paths to keys stored in Google Cloud KMS. For more
        // info on creating a KMS key and getting its path, see
        // https://cloud.google.com/kms/docs/quickstart
    
        String tableName = "votes123";
    
        // Initialize database connection pool and create table if it does not exist
        // See CloudSqlConnectionPool.java for setup details
        DataSource pool =
            CloudSqlConnectionPool.createConnectionPool(dbUser, dbPass, dbName, instanceConnectionName);
        CloudSqlConnectionPool.createTable(pool, tableName);
    
        // Initialize envelope AEAD
        // See CloudKmsEnvelopeAead.java for setup details
        Aead envAead = CloudKmsEnvelopeAead.get(kmsUri);
    
        // Insert row into table to test
        // See EncryptAndInsert.java for setup details
        EncryptAndInsertData.encryptAndInsertData(
            pool, envAead, tableName, "SPACES", "hello@example.com");
    
        queryAndDecryptData(pool, envAead, tableName);
      }
    
      public static void queryAndDecryptData(DataSource pool, Aead envAead, String tableName)
          throws GeneralSecurityException, SQLException {
    
        try (Connection conn = pool.getConnection()) {
          String stmt =
              String.format(
                  "SELECT team, time_cast, voter_email FROM %s ORDER BY time_cast DESC LIMIT 5",
                  tableName);
          try (PreparedStatement voteStmt = conn.prepareStatement(stmt); ) {
            ResultSet voteResults = voteStmt.executeQuery();
    
            System.out.println("Team\tTime Cast\tEmail");
            while (voteResults.next()) {
              String team = voteResults.getString(1);
              Timestamp timeCast = voteResults.getTimestamp(2);
    
              // Postgres pads CHAR fields with spaces. These will need to be removed before
              // decrypting.
              String aad = voteResults.getString(1).trim();
    
              // Use the envelope AEAD primitive to encrypt the email, using the team name as
              // associated data. This binds the encryption of the email to the team name, preventing
              // associating an encrypted email in one row with a team name in another row.
              String email = new String(envAead.decrypt(voteResults.getBytes(3), aad.getBytes()));
    
              System.out.println(String.format("%s\t%s\t%s", team, timeCast, email));
            }
          }
        }
      }
    }

### Python
    
    
    import os
    
    import sqlalchemy
    import tink
    
    from .cloud_kms_env_aead import init_tink_env_aead
    from .cloud_sql_connection_pool import init_db
    from .encrypt_and_insert_data import encrypt_and_insert_data
    
    
    def main() -> None:
        """
        Connects to the database, inserts encrypted data and retrieves encrypted data.
        """
        db_user = os.environ["DB_USER"]  # e.g. "root", "postgres"
        db_pass = os.environ["DB_PASS"]  # e.g. "mysupersecretpassword"
        db_name = os.environ["DB_NAME"]  # e.g. "votes_db"
    
        # Set if connecting using TCP:
        db_host = os.environ["DB_HOST"]  # e.g. "127.0.0.1"
    
        # Set if connecting using Unix sockets:
        db_socket_dir = os.environ.get("DB_SOCKET_DIR", "/cloudsql")
    
        instance_connection_name = os.environ["INSTANCE_CONNECTION_NAME"]
        # e.g. "project-name:region:instance-name"
    
        credentials = os.environ.get("GOOGLE_APPLICATION_CREDENTIALS", "")
        key_uri = "gcp-kms://" + os.environ["GCP_KMS_URI"]
        # e.g. "gcp-kms://projects/...path/to/key
        # Tink uses the "gcp-kms://" prefix for paths to keys stored in Google
        # Cloud KMS. For more info on creating a KMS key and getting its path, see
        # https://cloud.google.com/kms/docs/quickstart
    
        table_name = "votes"
        team = "TABS"
        email = "hello@example.com"
    
        env_aead = init_tink_env_aead(key_uri, credentials)
        db = init_db(
            db_user,
            db_pass,
            db_name,
            table_name,
            instance_connection_name,
            db_socket_dir,
            db_host,
        )
    
        encrypt_and_insert_data(db, env_aead, table_name, team, email)
        query_and_decrypt_data(db, env_aead, table_name)
    
    
    def query_and_decrypt_data(
        db: sqlalchemy.engine.base.Engine,
        env_aead: tink.aead.KmsEnvelopeAead,
        table_name: str,
    ) -> list[tuple[str]]:
        """
        Retrieves data from the database and decrypts it using the KmsEnvelopeAead object.
        """
        with db.connect() as conn:
            # Execute the query and fetch all results
            recent_votes = conn.execute(
                f"SELECT team, time_cast, voter_email FROM {table_name} "
                "ORDER BY time_cast DESC LIMIT 5"
            ).fetchall()
    
            print("Team\tEmail\tTime Cast")
            output = []
    
            for row in recent_votes:
                team = row[0]
    
                # Postgres pads CHAR fields with spaces. These will need to be removed before
                # decrypting.
                aad = team.rstrip()
    
                # Use the envelope AEAD primitive to decrypt the email, using the team name as
                # associated data. Encryption with associated data ensures authenticity
                # (who the sender is) and integrity (the data has not been tampered with) of that
                # data, but not its secrecy. (see RFC 5116 for more info)
                email = env_aead.decrypt(row[2], aad.encode()).decode()
                time_cast = row[1]
    
                # Print recent votes
                print(f"{team}\t{email}\t{time_cast}")
                output.append((team, email, time_cast))
        return output
    
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
