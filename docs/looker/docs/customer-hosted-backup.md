---
url: https://docs.cloud.google.com/looker/docs/customer-hosted-backup/
title: Exporting data from a customer-hosted Looker instance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:42:53.635097+00:00
---

# Exporting data from a customer-hosted Looker instance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/customer-hosted-backup/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Exporting data from a customer-hosted Looker instance Stay organized with collections  Save and categorize content based on your preferences. 

Admins of customer-hosted Looker instances may consider migrating to a Looker-hosted environment primarily to trade the overhead of infrastructure administration for increased convenience, enhanced feature availability, and managed reliability. Using a Looker-hosted instance greatly reduces the effort required to install, configure, and maintain the Looker application, because all necessary IT functions that are related to the Looker application are handled for you.

Migrating a customer-hosted instance to a Looker-hosted environment involves these main steps:

  1. **Intake and setup** : You open a ticket with the Looker team and complete the Looker On-Prem Migration questionnaire. The Looker team creates a new hosted instance based on your responses to the questionnaire.
  2. **Encryption** : Looker SREs generate a GnuPG (GPG) key pair and share the public key with you.
  3. **Export** : You stop your Looker instance and export its data (database, file system, and customer-managed key (CMK)).
  4. **Data transit and import** : The Looker team imports the backup into the Looker-hosted instance and verifies it.



This page describes how to perform the tasks required for **Step 3: Export** :

  * Evaluate the performance and size of your instance's file system and database
  * Back up, encrypt, and generate a checksum of the data that will be sent from the Looker file system
  * Back up, encrypt, and generate a checksum of the data that will be sent from the Looker database schema
  * Create, encrypt, and generate a checksum of the CMK key file
  * Validate your backup artifacts
  * Hand off your backup files for migration

**Note:** You may need to modify the scripts on this page for your environment.

## Before you begin

Before you can use the scripts on this page to back up your instance's data, you must make sure that your Looker instance, database, and encryption configuration fulfill migration requirements.

### Required configurations

The following Looker and database versions are required in order to run the scripts that are described on this page:

  * Your Looker instance must be running a [supported Looker release version](https://docs.cloud.google.com/looker/docs/officially-supported-releases).
  * Your instance must use a database that is compatible with MySQL version 8.0.0 or later, so the exported database schema file can be consumed by Looker.



If you're using AWS KMS, migrate to Looker's AES-256 GCM encryption by following the steps that are described on [Changing Looker's encryption keys](https://docs.cloud.google.com/looker/docs/changing-encryption-keys) documentation page.

To ensure proper data storage and character display, your database collation must be set to `utf8mb4` (recommended) or `utf8`. Using other collations may result in data corruption or errors when saving special characters.

## Evaluate your instance for migration

To determine if your customer-hosted Looker instance can be migrated to a Looker-hosted Looker (original) instance, you must evaluate the size and performance of your instance's database and file system. This evaluation also assesses whether your source environment can handle the data extraction that happens during the backup generation process. This information helps the Looker team allocate enough resources for the target Looker-hosted instance.

To perform the evaluation, you must clone the GitHub repository that contains Looker's script for evaluating a Looker instance's compute usage and file system performance. This script relies on the [Go Looker SDK](https://github.com/looker-open-source/sdk-codegen/tree/main/go) and is available in the [Looker O2C Migration Evaluation](https://github.com/looker-open-source/looker-o2c-migration-tool) repository on GitHub.

The following sections will describe what steps you need to complete to run the script that evaluates your instance, which include the following tasks:

  1. Clone the repository that contains the script.
  2. Generate API credentials.
  3. Execute the command to check compute usage.
  4. Execute the command to check file system performance.



### Install evaluation tools

Install the following tools, languages, and SDKs on the machine where you will be backing up your Looker instance data:

  1. [Git](https://git-scm.com/install/)
  2. [Go programming language](https://go.dev/doc/install)
  3. [Go Looker SDK](https://github.com/looker-open-source/sdk-codegen/tree/main/go)



### Clone the Looker O2C Migration Evaluation repository

To clone the repository that contains the evaluation script, run the following command from the home directory of the user who will execute the analysis and backup:
    
    
    git clone https://github.com/looker-open-source/looker-o2c-migration-tool.git
    

### Generate API credentials

The evaluation script uses the Looker SDK to retrieve data, acting as an API client that sends requests over the network to your Looker server. The admin user who runs the script must have a Looker API client ID and client secret. To generate [API credentials](https://docs.cloud.google.com/looker/docs/admin-panel-users-users#api_keys) for your Looker admin account, follow these steps:

  1. Navigate to the **Users** page in the **Admin** panel.
  2. Select **Edit** for your account.
  3. On the account's details page, locate the **API3 Keys** section and select **Edit Keys**.
  4. Select **New API Key**.
  5. Looker will display a **Client ID** and **Client Secret**. Copy these values and save them in a secure location.



### Generate compute usage information

To use the migration evaluation script to return information about the compute usage of your instance, run the following command on a machine that has a direct network connection to the Looker application's API endpoint:
    
    
    cd looker-o2c-migration-tool
    go run main.go --client-id API_CLIENT_ID --client-secret API_CLIENT_SECRET --looker-instance-address LOOKER_INSTANCE_ADDRESS --output-csv-path OUTPUT_CSV_PATH --ssl=SSL
    

Replace the following:

  * `API_CLIENT_ID`: Your client ID from the previous step.
  * `API_CLIENT_SECRET`: Your client secret from the previous step.
  * `LOOKER_INSTANCE_ADDRESS`: The address of your Looker instance, including the protocol.
  * `OUTPUT_CSV_PATH`: The path for the CSV output, such as `/content/compute_usage_info.csv`.
  * `SSL`: Whether the connection between your machine and the Looker instance should use an SSL certificate. Its value is `true` by default.



This command outputs a CSV file with the usage details of the Looker instance.

### Generate file system performance information

This script shows the size and file count of individual model-related directories, along with a disk write speed test. It assumes that Looker is installed in the home directory of a user with the username `looker`, as described on the [Installing the Looker application](https://docs.cloud.google.com/looker/docs/installing-looker-application) documentation page.

To use the migration evaluation script to return information about the file system performance of your instance, run the following command on the machine where your Looker instance is hosted:
    
    
    cd looker-o2c-migration-tool
    go run main.go --file-system-evaluation --output-csv-path OUTPUT_CSV_PATH
    

Replace the following:

  * `OUTPUT_CSV_PATH`: The path for the CSV output, such as /content/fs_perf_info.csv



This command outputs a CSV file with the file system performance of the Looker instance.

## Prepare your instance for backup

Prepare to back up your instance data by installing the packages and dependencies that are required to run the scripts that are described on this page. You can also set some environment variables to simplify your command writing.

### Install and verify dependencies

When installing the dependencies that are required for backing up your Looker instance data, use the package manager that is standard for your Linux distribution. The following versions correspond to the packages provided in **Debian 12 (Bookworm)** and represent the minimum version of each required package.

Install the following packages on the machine where you will be backing up your Looker instance data:

  1. `bash 5.2.15`

  2. `gpg` `2.2.40` (GnuPG) – The backup generation process uses `gpg` to encrypt the database and file system backups before they are shared with the Looker team.

  3. `libgcrypt 1.10.2`

  4. `Gpg-agent 2.2.40` (GnuPG)

  5. `GNU tar 1.34`

  6. `gzip 1.12`

  7. `md5sum 9.1` (GNU coreutils)

  8. `GNU grep 3.11` (with support for PCRE2 10.42 2022-12-11 or later)

  9. `GNU sed 4.9`

  10. `mariadb-client-core` (must connect to your MySQL 8.X)




As an example, run the following commands to install the necessary packages on a Debian-based Linux system:
    
    
    sudo apt-get update
    sudo apt-get install -y \
        bash \
        gnupg \
        libgcrypt20 \
        gnupg-agent \
        tar \
        gzip \
        coreutils \
        grep \
        sed \
        mariadb-client-core
    

### Define variables

The following commands define some variables that will be used throughout the backup generation process. Configure them on any terminal where you plan to execute any further commands.

#### Environment variable: Set backup directory path

The following command will set the path for the backup directory where the files will be created. Run these commands on any terminal where you plan to perform the directory-specific backup generation tasks:
    
    
    BACKUP_DIRECTORY="DIRECTORY_PATH"
    BACKUP_DIRECTORY="${BACKUP_DIRECTORY%/}"
    

Replace the following:

  * `DIRECTORY_PATH`: The path where the backup files will be created. Make sure this directory is large enough to hold the backup. Don't include the path's leading `/`.

**Warning:** Don't set the backup directory path as the root directory.

#### Environment variable: Set source path for file system backup

The variable definition for the file system backup's source path assumes that `looker` is the username for the user who installed the Looker application and that the installation took place on the user's home directory, as described on the [Installing the Looker application](https://docs.cloud.google.com/looker/docs/installing-looker-application) documentation page. You must modify the variable if you installed Looker in a different directory. Set this variable on the terminal where you will execute the Looker file system backup:
    
    
      LOOKER_USER="looker"
      ROOT_LOOKER_FS_DIRECTORY="$(getent passwd "$LOOKER_USER" | cut -d: -f 6)"
    

#### Environment variable: Define new Looker instance

Define variables to represent the name and unique ID of the instance that you'll import into. The Looker team provides you with the values for these variables.
    
    
    export luid='LOOKER_HOSTED_INSTANCE_ID'
    export customer='LOOKER_HOSTED_INSTANCE_NAME'
    

Replace the following:

  * `LOOKER_HOSTED_INSTANCE_ID`: The unique identifier of the Looker instance that you'll migrate to
  * `LOOKER_HOSTED_INSTANCE_NAME`: The name of the new Looker instance that you'll migrate to



#### Environment variable: Encryption key

The following command will install a public GPG key on your instance. Configure it on any terminal where you will execute your instance's backup commands (the Looker will provide you with the value for this variable):
    
    
    base64_encryption_key="BASE64_ENCRYPTION_KEY"
    

Replace the following:

  * `BASE64_ENCRYPTION_KEY`: The encryption key that the backup script uses to encrypt your backups. The Looker team provides you with the value for this variable.



#### Generate a public encryption key

The following command will install a public `pgp` key on your instance. The backup scripts use this key to encrypt your backup. Configure it on any terminal where you will execute the commands to back up your instance.
    
    
    echo -n "${base64_encryption_key}" | base64 -d | gpg --import
    

## Back up your instance data

Run the following commands to securely package the critical components of your instance's file system and database schema so that they can be transferred and restored to a new Looker-hosted Looker (original) instance. The script will perform the backup, using `md5sum` to verify and validate the integrity of the backup. Lastly, it encrypts the backup using GnuPG before exporting the results in MD5 file format.

### Back up your instance's file system data

Run these commands from the directory where you want to export the backup data and in the same terminal where you set your environment variables. Select the tab for the type of Looker-hosted instance that you plan to migrate to.

### Looker (original)

Run this command to ensure that any custom Git server-side hooks used for data validation or workflow automation are included in the backup:
    
    
    cd "${BACKUP_DIRECTORY}"
    
    function findHookPath() {
    rootPath=$1
    
    find \
        ${rootPath}/models{-user-*,}/*/.git/config \
        -maxdepth 0 \
        -type f \
        -xtype f \
      | xargs -I {} grep hooksPath {} \
      | sort \
      | uniq \
      | sed -r -e 's/^.+hooksPath = //g' \
      | xargs -I {} dirname {} \
      | sort \
      | uniq \
      | sed -r -e "s#\.\.\/\.\.\/#${rootPath}/#g"
    
    }
    
    hooksPath=$(findHookPath "${ROOT_LOOKER_FS_DIRECTORY}" | sort | uniq | head -1)
    

Run this command to list all necessary directories and back them up:
    
    
    time find "${ROOT_LOOKER_FS_DIRECTORY}" \
      -maxdepth 1 \
      -type d \
      \( \
             -name marketplace \
          -o -name bare_models \
          -o -name deploy_keys \
          -o -name models \
          -o -name remote_dependencies \
          -o -name models-self-service \
          -o -name "models-user-*" \
          -o -wholename "${hooksPath}" \
      \) | tar \
      --gzip \
      --create \
      --file="${customer}_looker_fs_backup.tar.gz" \
      --files-from=-
    

Run this command to take a "fingerprint" of the backup before encryption:
    
    
    time md5sum "${customer}_looker_fs_backup.tar.gz" > "${customer}_fs_backup.md5"
    

Run this command to encrypt the backup:
    
    
    time gpg --encrypt --yes \
      --output "${customer}_looker_fs_backup.tar.gz.enc" \
      --recipient "looker-devops+migration-${luid}@google.com" \
      "${customer}_looker_fs_backup.tar.gz"
    

Run this command to take another "fingerprint" after encryption:
    
    
    time md5sum "${customer}_looker_fs_backup.tar.gz.enc" >> "${customer}_fs_backup.md5"
    

The checksum helps Looker verify the integrity of your data backup.

### Looker (Google Cloud core)

Run this command to ensure that any custom Git server-side hooks used for data validation or workflow automation are included in the backup:
    
    
    cd "${BACKUP_DIRECTORY}"
    
    function findHookPath() {
    rootPath=$1
    
    find \
        ${rootPath}/models{-user-*,}/*/.git/config \
        -maxdepth 0 \
        -type f \
        -xtype f \
      | xargs -I {} grep hooksPath {} \
      | sort \
      | uniq \
      | sed -r -e 's/^.+hooksPath = //g' \
      | xargs -I {} dirname {} \
      | sort \
      | uniq \
      | sed -r -e "s#\.\.\/\.\.\/#${rootPath}/#g"
    
    }
    
    hooksPath=$(findHookPath "${ROOT_LOOKER_FS_DIRECTORY}" | sort | uniq | head -1)
    

Run this command to list all necessary directories and back them up:
    
    
    time find "${ROOT_LOOKER_FS_DIRECTORY}" \
      -maxdepth 1 \
      -type d \
      \( \
             -name marketplace \
          -o -name bare_models \
          -o -name deploy_keys \
          -o -name models \
          -o -name remote_dependencies \
          -o -name models-self-service \
          -o -name "models-user-looker" \
          -o -wholename "${hooksPath}" \
      \) | tar \
      --gzip \
      --create \
      --file="${customer}_looker_fs_backup.tar.gz" \
      --files-from=-
    

Run this command to take a "fingerprint" of the backup before encryption:
    
    
    time md5sum "${customer}_looker_fs_backup.tar.gz" > "${customer}_fs_backup.md5"
    

Run this command to encrypt the backup:
    
    
    time gpg --encrypt --yes \
      --output "${customer}_looker_fs_backup.tar.gz.enc" \
      --recipient "looker-devops+migration-${luid}@google.com" \
      "${customer}_looker_fs_backup.tar.gz"
    

Run this command to take another "fingerprint" after encryption:
    
    
    time md5sum "${customer}_looker_fs_backup.tar.gz.enc" >> "${customer}_fs_backup.md5"
    

The checksum helps Looker verify the integrity of your data backup.

This script produces the following files for the file system portion of the migration:

  1. `${customer}_looker_fs_backup.tar.gz.enc`: The encrypted, compressed file system backup.
  2. `${customer}_fs_backup.md5`: The file that contains the checksums for verification.



### Back up your instance database schema

**Note:** Run these commands in the same terminal where you set your environment variables.

These commands prepare your environment for backing up your Looker instance database schema by creating a temporary configuration file that allows migration tools to connect to your Looker instance's internal database. Rather than passing sensitive data like usernames and hostnames into the commands directly, this script writes them into the configuration file, which tools like `mysqldump` and `mysql` can read.

Run the following command to create the temporary configuration file and set various settings:
    
    
    export database_name="DATABASE_SCHEMA_NAME"
    temporary_cnf_file="$(mktemp --tmpdir=. --suffix .cnf)"
    echo "[client]
    host=DATABASE_HOST
    port=DATABASE_PORT
    user=DATABASE_USER
    password=PASSWORD
    
    [mariadb-dump]
    no-sandbox
    
    [mysql]
    no-auto-rehash
    
    [mysqldump]
    no-tablespaces
    loose_set-gtid-purged=OFF
    single-transaction
    quick
    max_allowed_packet=1G
    ignore-table=${database_name}.LookerQ_LookerBQ_ACTIVEMQ_ACKS
    ignore-table=${database_name}.LookerQ_LookerBQ_ACTIVEMQ_LOCK
    ignore-table=${database_name}.LookerQ_LookerBQ_ACTIVEMQ_MSGS
    
    [Server-specific settings - mostly for mysqld/mariadbd processes]
    max_allowed_packet = 1024M
    " > ${temporary_cnf_file}
    

Replace the following:

  * `DATABASE_HOST`: The DNS or IP of the Looker database.
  * `DATABASE_PORT`: The database port.
  * `DATABASE_USER`: The database username to execute the export.
  * `PASSWORD`: The plaintext value for the password of the user who will execute the export. Looker won't check this password. However, if you would prefer to omit the plaintext password requirement, you can leave this variable blank, and the system will force prompt you for your password when you run backup commands.
  * `DATABASE_SCHEMA_NAME`: The name of your database or schema.



If your database requires a SSL certificate for connection, add the following paths to the temporary configuration file:

Set the path to the Certificate Authority (CA) file:
    
    
    ssl-ca=/etc/mysql/certs/ca.pem
    

Set the path to the client SSL certificate:
    
    
    ssl-cert=/etc/mysql/certs/client-cert.pem
    

Set the path to the client SSL private key:
    
    
    ssl-key=/etc/mysql/certs/client-key.pem
    

For MySQL databases, require an SSL and verify the server certificate:
    
    
    loose-ssl-mode=VERIFY_CA
    

For MariaDB databases, require an SSL and verify the server certificate:
    
    
    loose-ssl-verify-server-cert=ON
    

Run the following commands to perform, encrypt, and verify your database schema backup.

**Warning:** DON'T add any of the following parameters to the backup commands: 

  * `--skip-lock-tables`: This parameter may produce an inconsistent backup.
  * `--skip-opt`: This parameter disables the `--extended-insert` parameter, which will slow down the restore process.
  * `--routines`: Looker will reject your backup.
  * `--triggers`: Looker will reject your backup.
  * `--set-gtid-purged=ON`: This parameter will disrupt the restore process.



Navigate to the directory where you want to store your backup:
    
    
    cd "${BACKUP_DIRECTORY}"
    

Run this command to back up your database:
    
    
    time mysqldump \
        --defaults-file="${temporary_cnf_file}" \
        "${database_name}" \
      | gzip > "${customer}_looker_db_backup.sql.gz"
    
    

Run this command to take a "fingerprint" of your backup before encryption:
    
    
    time md5sum "${customer}_looker_db_backup.sql.gz" >> "${customer}_db_backup.md5"
    

Run this command to encrypt your backup:
    
    
    time gpg --encrypt --yes \
        --output "${customer}_looker_db_backup.sql.gz.enc" \
        --recipient "looker-devops+migration-${luid}@google.com" \
        "${customer}_looker_db_backup.sql.gz"
    

Run this command to take another "fingerprint" after encryption:
    
    
    time md5sum "${customer}_looker_db_backup.sql.gz.enc" >> "${customer}_db_backup.md5"
    

This script produces the following files for the database schema portion of the migration:

  1. `${customer}_looker_db_backup.sql.gz.enc`: The encrypted, compressed database schema backup.
  2. `${customer}_db_backup.md5`: The file that contains the checksums for verification.



### Encrypt your customer-managed encryption key (CMK)

The following commands will validate, format, and encrypt the CMK. Without this encryption, a migrated database can't be decrypted in the new Looker environment.

**Caution:** The next CMK command needs to be run only once on the machine that hosts your internal database or the machine that hosts the Looker instance but not on both.

First set a variable with your current CMK, which should be in base64 format:
    
    
    CMK="CUSTOMER_CMK_KEY"
    

Replace the following:

  * `CUSTOMER_CMK_KEY`: The value of your CMK



Then run the following commands to generate a CMK key file, generate the checksum of the decrypted CMK, encrypt the CMK file, and generate the checksum of the encrypted CMK:
    
    
    echo -n "${CMK}" > "${customer}_looker_cmk_key"
    
    time md5sum "${customer}_looker_cmk_key" >> "${customer}_cmk_key.md5"
    
    time gpg --encrypt --yes \
      --output "${customer}_looker_cmk_key.enc" \
      --recipient "looker-devops+migration-${luid}@google.com" \
      "${customer}_looker_cmk_key"
    
    time md5sum "${customer}_looker_cmk_key.enc" >> "${customer}_cmk_key.md5"
    

This script produces the following files for the CMK portion of the migration:

  * `${customer}_looker_cmk_key.enc`: The encrypted CMK file
  * `${BACKUP_DIRECTORY}/${customer}_cmk_key.md5`: The file that contains the checksums for verification



## Prepare your migration files

The scripts that you have run up to this point have produced the following files:

  * `compute_usage_info.csv`: The CSV file that contains information about the compute usage of your instance
  * `fs_perf_info.csv`: The CSV file that contains information about the file system performance of your instance
  * `${customer}_looker_fs_backup.tar.gz.enc`: The encrypted, compressed file system backup
  * `${customer}_fs_backup.md5`: The file that contains the checksums for verification
  * `${customer}_looker_db_backup.sql.gz.enc`: The encrypted, compressed database schema backup
  * `${customer}_db_backup.md5`: The file that contains the checksums for verification
  * `${customer}_cmk_key.md5`: The file that contains the checksums for verification
  * `${customer}_looker_cmk_key.enc`: The encrypted CMK file



To combine the MD5 files into a single file called `${customer}_backup.md5`, run the following command in your backup directory:
    
    
    cat \
        "${customer}_db_backup.md5" \
        "${customer}_fs_backup.md5" \
        "${customer}_cmk_key.md5" \
      | sort | uniq \
      > "${customer}_backup.md5"
    

## Validate your backup artifacts

To ensure that your backup files are complete, secure, and ready for migration, use the Looker On-Prem Data Verifier tool. This tool performs a comprehensive validation, including checking MD5 checksums, GPG encryption keys, database structure, and CMK validity.

### Install the validation tool

To run the validation tool, you must have [Go](https://go.dev/doc/install) and [GnuPG](https://gnupg.org/download/) installed on your machine.

To clone the repository and build the tool, run the following commands:
    
    
    git clone https://github.com/looker-open-source/customer-scripts.git
    cd customer-scripts/onprem-data-verifier
    go build -o onprem-verifier main.go
    

### Run the validation tool

The tool operates on the directory containing your backup files. Ensure all required files (four encrypted artifacts and three decrypted artifacts) are in your ${BACKUP_DIRECTORY} before running the tool.

Run the following command to validate your artifacts:
    
    
    ./onprem-verifier \
      --backupDir "${BACKUP_DIRECTORY}" \
      --customerName "${customer}" \
      --luid "${luid}"
    

Upon success, the tool generates a `metadata.json` file. You must include this file when you hand off your backup artifacts to the Looker team.

## Hand off your files

At the end of the backup and encryption process, you should have the following files:

  * `${customer}_looker_db_backup.sql.gz.enc`
  * `${customer}_looker_fs_backup.tar.gz.enc`
  * `${customer}_looker_cmk_key.enc`
  * `${customer}_backup.md5`
  * `metadata.json`
  * `compute_usage_info.csv`
  * `fs_perf_info.csv`



Deliver these files to your Looker team for import into a Looker-hosted instance.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
