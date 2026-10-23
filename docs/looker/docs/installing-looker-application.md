---
url: https://docs.cloud.google.com/looker/docs/installing-looker-application/
title: Installing the Looker application \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:34:50.237625+00:00
---

# Installing the Looker application  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/installing-looker-application/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)



Send feedback 

#  Installing the Looker application Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to install the Looker application for a customer-hosted deployment.

> Hosting the Looker application is independent of where your data resides; data always remains in-database and is not copied to the Looker instance.

## Deployment specifications

If you're going to run Looker on a network that does not connect to the Internet, you may need to set up a proxy server to communicate with the Looker license server or use serverless web services that only make web calls, such as BigQuery.

Install the Looker application on a dedicated machine that meets the following minimum requirements:

  * 1.2 GHz CPU; Looker recommends two or more cores.
  * 8 GB free RAM.
  * 10 GB free disk space.
  * 2 GB [swap file](https://linuxize.com/post/create-a-linux-swap-file/) space.
  * Linux. We use Ubuntu Linux (LTS releases) for our internal Looker hosting, and we recommend it for customers who don't have a Linux preference. However, we support Looker on release versions of all major enterprise Linux distributions, including RedHat, CentOS, and Amazon Linux. Looker is supported only on Linux versions with x64 instruction sets.
  * Java OpenJDK 21. Looker uses OpenJDK (version 21). Looker recommends the JDK, instead of the JRE, to take advantage of the extra troubleshooting tools. In addition, Looker recommends that you transition to new Java updates as they are released. Other versions of Java, Oracle JDK, and OpenJDK are _not_ supported at this time.

If you run Looker directly using the `java -jar` command (instead of using the startup script), you must include these three specific settings: 
        
        --add-opens=java.base/sun.nio.ch=ALL-UNNAMED --add-opens=java.base/java.io=ALL-UNNAMED --add-opens=java.base/java.nio=ALL-UNNAMED

  * `libssl` and a `libcrypt.so` must be present on the system.

  * Locale and Character Encoding: To ensure that Looker correctly processes and displays international characters across all parts of the application, the server environment must be configured to use a UTF-8 locale. This is essential for handling data that contains multi-byte character sets, such as those used in Japanese, Chinese, and many other languages. We recommend setting the following environment variables on the machine or within the container that's running the Looker application:
        
        export LANG=en_US.UTF-8
        export LC_ALL=en_US.UTF-8
        

You can add these commands to your shell profile (for example, `~/.bashrc`, `~/.profile`) or environment configuration files for your deployment. Failure to configure a UTF-8 locale can lead to character encoding issues, where special characters may appear as question marks, boxes, or other incorrect symbols in the Looker UI, downloads, and API responses.

  * You must allow inbound traffic to your Looker instance through TCP port `9999`.

  * If users require API access, you must allow inbound traffic to your Looker instance through TCP port `19999`.

  * If Looker is connecting to AWS Redshift from an AWS VPC private network, you must set the MTU to 1500. For more information about this setting, see the **Configuring the MTU of an instance** section of this [Amazon Web Services article](https://docs.aws.amazon.com/redshift/latest/mgmt/connecting-drop-issues.html#set-mtu). If Looker detects that the MTU setting is greater than 1500 during a database connection test, it displays the following error:
        
        MTU of network interface eth0 is too large (> 1500).
        If Looker instance and Redshift cluster are within the same VPC,
        this warning can be ignored.
        

  * The following TCP keepalive settings. To persist through a reboot these should be set in `/etc/sysctl.conf` or a file in the `/etc/sysctl.d` directory:
        
        net.ipv4.tcp_keepalive_time=200
        net.ipv4.tcp_keepalive_intvl=200
        net.ipv4.tcp_keepalive_probes=5
        

  * A user named `looker` in the group named `looker` to run the Looker application.

  * A ulimit for the `looker` user of `4096` or higher. You can do this by adding the following lines to `/etc/security/limits.conf`:
        
        looker     soft     nofile     4096
        looker     hard     nofile     4096
        

  * Time synchronization through NTP or equivalent.

  * The `/tmp` folder must _not_ be mounted with the noexec option.

  * The `looker` home directory should _not_ be mounted on an NFS volume.

  * Setting the server's time zone to UTC is recommended but not required.

  * Git 2.39.1 or later is required for Looker 23.6 and later.

  * Though not required, [Netcat](http://netcat.sourceforge.net/) can be helpful for troubleshooting network connectivity issues. To install Netcat on, for example, a Ubuntu-based server, a common command is:
        
        sudo apt-get install netcat
        

  * If needed, you can set up a proxy server to handle the HTTP(S) requests that Looker needs to be able to make to 'core' on localhost. To communicate with the Looker local proxy server requires that you add some special arguments in `lookerstart.cfg`: add `http.nonProxyHosts=localhost` to enable access to the Looker localhost without going through the proxy.




To avoid maintenance and resource conflicts, you shouldn't use the Looker server to host other applications.

## Enable ntpd or chronyd

NTP stands for Network Time Protocol. It enables your host's system clock to always maintain the correct time, which Looker needs to function correctly. Looker does not require any particular time synchronization software be used as long as times remain in sync. It is _not_ necessary to run an NTP server; only the NTP client is needed. You may substitute chronyd for NTP.

Consult your OS vendor's documentation for information on enabling ntpd or chronyd.

## Create an encryption key

Looker uses AES-256 Galois/Counter Mode (GCM) encryption to encrypt sensitive data that is stored internally, including:

  * Backups of the Looker internal database
  * Database and service connection information
  * User authentication information
  * User attribute values
  * Customer data that is cached or readied for delivery



For a detailed list of the data that Looker encrypts, open a [support request](http://console.cloud.google.com/support/cases).

Data is encrypted using a unique data key and contains a signed and versioned encryption envelope to ensure verification. This mode requires the use of an external Customer Master Key (CMK). The CMK is used to derive, encrypt, and decrypt the Key Encryption Key (KEK), which in turn is used to derive, encrypt, and decrypt data keys.

Encryption is used only for the Looker internal database and cache. Customer databases are not affected by the Looker encryption in any way. In addition, only static data (data stored on disk) is encrypted in this manner.

Customer-hosted installations can use their own AWS KMS accounts or their own custom key management systems. All data keys and the KEK are encrypted and used internally on the customer-hosted Looker installation. If you're not using AWS KMS, the external CMK should be kept in a safe and permanent location! Losing the CMK after encrypting the internal database can result in the loss of your instance.

### If you are using AWS KMS

If you are using AWS KMS, [create a CMK](https://docs.aws.amazon.com/kms/latest/developerguide/create-keys.html) using either the AWS Management Console or the API.

After you create the CMK, Looker recommends that you [create a new IAM role](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-roles-for-amazon-ec2.html#create-iam-role) that is unique for your CMK and [attach it with your Looker instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-roles-for-amazon-ec2.html#attach-iam-role).

Following is an example of an IAM role that contains the minimum permissions required for your CMK:
    
    
    {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Sid": "VisualEditor0",
                "Effect": "Allow",
                "Action": "kms:GenerateRandom",
                "Resource": "*"
            },
            {
                "Sid": "VisualEditor1",
                "Effect": "Allow",
                "Action": [
                    "kms:Decrypt",
                    "kms:Encrypt",
                    "kms:Generate*",
                ],
                "Resource": "arn:aws:kms:*:*:key/*"
            }
        ]
    }
    

After you create your CMK and new IAM role, set the `AWS_REGION` environment variable to your AWS region and the `LKR_AWS_CMK` environment variable to the alias of your CMK:
    
    
    export AWS_REGION=<AWS_region>
    export LKR_AWS_CMK=alias/<CMK_alias>
    

Optionally, you can also set the `LKR_AWS_CMK_EC` environment variable to set a custom [AWS encryption context](https://docs.aws.amazon.com/kms/latest/developerguide/encryption-context.html). If you don't set this environment variable, Looker will use the default encryption context, the string `Looker_Encryption_Context`.
    
    
    export LKR_AWS_CMK_EC=<My_Encryption_Context>
    

### If you are not using AWS KMS

If you are not using AWS KMS, generate a Base64, 32-byte CMK. You can store the CMK either in an environment variable or in a file:

  * To generate the CMK and store it in an environment variable, you can use the following command to generate the CMK:
        
        openssl rand -base64 32
        

After you generate the CMK, copy it and use the following command to store the CMK in the `LKR_MASTER_KEY_ENV` environment variable (where `<CMK_value>` is the CMK you generated with the previous command):
        
        export LKR_MASTER_KEY_ENV=<CMK_value>
        

  * To generate and store the CMK in a file, you can use the following command (where `<path_to_key_file>` is the path and filename for storing the CMK):
        
        openssl rand -base64 32 > <path_to_key_file>
        

After generating the CMK file, set the key file permissions to current user read-only:
        
        chmod 0400 <path_to_key_file>
        




> After you have generated a CMK, be sure to store it in a safe and permanent location before continuing! Losing the CMK after encrypting the internal database can result in the loss of your instance.

Once you have generated and stored your CMK, set the `LKR_MASTER_KEY_ENV` environment variable:

  * If you are storing your CMK in an environment variable, set the `LKR_MASTER_KEY_ENV` environment variable to the value of the CMK:
        
        export LKR_MASTER_KEY_ENV=<CMK_value>
        

  * If you are storing your CMK in a file, set the `LKR_MASTER_KEY_FILE` environment variable to the path of the CMK file:
        
        export LKR_MASTER_KEY_FILE=<path_to_key_file>
        




> After you have generated a CMK, be sure to store it in a safe and permanent location before continuing! Losing the CMK after encrypting the internal database can result in the loss of your instance.

## Install the Looker application

  1. Create group `looker`.
         
         sudo groupadd looker
         

  2. Create user `looker` and its home directory.
         
         sudo useradd -m  -g looker  looker
         

  3. Switch to the `looker` user; _don't run Looker as root_.
         
         sudo su - looker
         

  4. Create `looker` subdirectory in the home directory.
         
         mkdir ~/looker
         

  5. Change to the `looker` subdirectory.
         
         cd ~/looker
         

  6. Make sure you are in the correct directory.
         
         pwd
         

If your user directories are under `/home`, the output of this command should be `/home/looker/looker`.

  7. Download the chosen Looker JAR files through one of the methods on the [Downloading the Looker JAR files](https://docs.cloud.google.com/looker/docs/downloading-looker-jar-files) documentation page. Ensure that both JAR files are the same version; using different versions of the core and dependency JAR files can cause instability in your Looker installation.

  8. Download the `looker21` startup script at the [looker-open-source GitHub repo](https://github.com/looker-open-source/customer-scripts/tree/main/startup_scripts). If you want Looker to run at system startup, download the [looker_init script](https://github.com/looker-open-source/customer-scripts/blob/main/startup_scripts/looker_init) and use both the `systemd` and the `init` script options.

  9. Move the startup script (named `looker21`) and Looker JAR files (named `looker-x.x.x.jar` and `looker-dependencies-x.x.x.jar`, where `x.x.x` is the version number) to the new `~/looker` directory.

  10. Rename `looker-x.x.x.jar` to `looker.jar` and `looker-dependencies-x.x.x.jar` to `looker-dependencies.jar`. Rename the `looker21` startup script to `looker`.

  11. The startup script automatically determines how much Java memory to allocate to Looker. If you want to customize this value manually, see the [Recommended Java memory settings](https://docs.cloud.google.com/looker/docs/recommended-java-memory-settings) documentation page for more information.

  12. Make the Looker startup script executable (set the permissions to `0750`).
         
         chmod 0750 looker
         

  13. Start the Looker process from shell as the `looker` user.

**Note:** If you want to create a new FIPS 140-2 compliant Looker instance, include the `--fips` [startup option](https://docs.cloud.google.com/looker/docs/startup-options) when you first start the instance. This will put the new instance in FIPS-compliant mode. For more information, see the [Enabling FIPS 140-2 level 1 compliance](https://docs.cloud.google.com/looker/docs/fips-mode) documentation page.
         
         ./looker start
         

  14. For startup flag help, use:
         
         java \
           --add-opens=java.base/sun.nio.ch=ALL-UNNAMED \
           --add-opens=java.base/java.io=ALL-UNNAMED \
           --add-opens=java.base/java.nio=ALL-UNNAMED \
           -jar looker.jar
         

Or, for startup command help, use:
         
         java \
           --add-opens=java.base/sun.nio.ch=ALL-UNNAMED \
           --add-opens=java.base/java.io=ALL-UNNAMED \
           --add-opens=java.base/java.nio=ALL-UNNAMED \
           -jar looker.jar help
         

  15. Open a browser to `https://hostname:9999` where `hostname` is the DNS name of the host running Looker.

You should use `https` in the URL, which will create a security warning that you will need to bypass. This warning will persist until a valid SSL certificate is installed on the server.

  16. Enter the license key obtained from your Looker analyst.

  17. Enter a name, an email, and a password to create your first account.




## Create a DNS record

Add a `looker.[yourdomain].com` DNS record for the server. This step is optional, but recommended.

## Deploying Looker automatically

Looker may be deployed using a configuration management tool such as Ansible or Chef. An example Ansible role for automated deployment is available on the [Configuration management tools](https://docs.cloud.google.com/looker/docs/configuration-management-tools) documentation page.

## Hypervisor tuning

Looker runs as a Java virtual machine. If your Looker instance is on a VMware guest, you may need to do some performance tuning. See the VMware [Java best practices guide](https://blogs.vmware.com/apps/2020/01/java-on-vmware-best-practices.html).

On other virtualization platforms, it may improve performance to reserve the Looker host's memory from the hypervisor. This is not controllable on Amazon EC2; however, for other vendors, you should consult their documentation for more information.

## Setting up an optional MySQL backend database

By default, Looker uses a HyperSQL in-memory database to store its configuration, users, and other data. You can use an external MySQL database, however, to store the Looker internal information. See the [Migrating to MySQL](https://docs.cloud.google.com/looker/docs/migrating-looker-backend-db-to-mysql) documentation page for information about configuring and tuning a MySQL backend database.

## Next steps

After you have installed Looker, you're ready to [configure Looker startup options](https://docs.cloud.google.com/looker/docs/startup-options).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
