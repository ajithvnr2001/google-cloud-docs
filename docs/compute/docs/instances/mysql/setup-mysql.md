---
url: https://docs.cloud.google.com/compute/docs/instances/mysql/setup-mysql/
title: Install MySQL on Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:49:44.301056+00:00
---

# Install MySQL on Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instances/mysql/setup-mysql/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Install MySQL on Compute Engine Stay organized with collections  Save and categorize content based on your preferences. 

To manually install MySQL on a Compute Engine instance that you've created, complete the following steps.

For an overview of several options for setting up MySQL on Compute Engine, see [MySQL on Compute Engine](https://docs.cloud.google.com/compute/docs/instances/mysql/discover-mysql). To learn which Compute Engine offerings are appropriate for MySQL, see [Configure MySQL on Compute Engine](https://docs.cloud.google.com/compute/docs/instances/mysql/mysql-workloads).

## Before you begin

  * Use the Google Cloud console to [turn on the Compute Engine API](https://console.cloud.google.com/apis/library/compute.googleapis.com).
  * Install the [Google Cloud CLI](https://docs.cloud.google.com/sdk/docs)
  * Configure your workspace to make commands less verbose. Substitute your project's values for PROJECT_ID, REGION, and ZONE in the following commands. For the full list of zones, see [Available regions & zones](https://docs.cloud.google.com/compute/docs/regions-zones/regions-zones#available).
        
        gcloud config set project PROJECT_ID
        gcloud config set compute/region REGION
        gcloud config set compute/zone ZONE
        


**Important:** This tutorial uses Compute Engine, which is a billable component of Google Cloud. Use the [Pricing Calculator](https://cloud.google.com/products/calculator/) to generate a cost estimate based on your projected usage. New Google Cloud users may be eligible for a [free trial](https://cloud.google.com/free/).

## Create a Compute Engine instance and establish an SSH connection

Create a Compute Engine instance for MySQL and establish an SSH connection to the newly created instance. The default operating system is Debian version 10. If you prefer to use a different operating system for this tutorial, you can choose from the options described on the [public images](https://docs.cloud.google.com/compute/docs/images) page in the Compute Engine documentation.

###  Console 

### Create the Compute Engine instance

To create the Compute Engine instance in the [Google Cloud console](https://console.cloud.google.com/), do the following:

  1. In the Google Cloud console, go to the **Compute Engine VM instances** page.

[Go to Compute Engine VM instances](https://console.cloud.google.com/compute/instances).

  2. Select your newly created project and click **Continue**.

  3. Click **Create instance** (**New instance** if you have existing instances). Name the instance **mysql-test**.

  4. [Select your performance level and size your disk](https://docs.cloud.google.com/compute/docs/instances/mysql/mysql-workloads#hyperdisk).

  5. To specify an operating system other than the default value, in the **Boot disk** section, click **Change** to configure the properties for the boot disk. In the **Public images** tab, select an operating system and then click **Save**.

  6. To conform with security best practices, create your instance without an external IP address.

Expand **Advance options** and expand **Networking**. Under **Network interfaces** , expand the **default** interface, and in the **External IPv4 address** menu, select **None**.

**Note:** Your instance will need to reach public package repositories during the MySQL installation. To allow internet access, configure Cloud NAT to manage network address translation.
  7. Click **Create**.




### Set up network address translation

To set up and manage network address translation with Cloud NAT, do the following:

  1. In the Google Cloud console, go to the **Cloud NAT** page.

[Go to Cloud NAT](https://console.cloud.google.com/net-services/nat/list)

  2. Click **Get started** or **Create Cloud NAT gateway**.

  3. For **Gateway name** , enter `nat-simple-configuration`.

  4. To select the Cloud Router, in the **Select Cloud Router** section, do the following:

     1. For **Network** , select **default**.
     2. For **Region** , select the region that you specified for your VM.
     3. For **Cloud Router** , select **Create new router**.

In the **Create a router** dialog that appears, provide a **Name** for the router—for example, `nat-router-simple-configuration`—and click **Create**.

  5. Click **Advanced configurations**.

  6. In the **Logging** section, select **Translation and errors**. This setting configures Cloud NAT to send all logs to Cloud Logging.

  7. Click **Create**.




### Establish an SSH connection to the VM

To establish an SSH connection, do the following:

  1. On the **VM instances** page, find your new VM instance in the list.

  2. In the **Connect** column for that VM, click **SSH**. The SSH terminal opens in a browser window.




###  gcloud 

  1. To create a Compute Engine instance, use the `gcloud compute instances create` command. To specify the operating system, add the `--image-family` parameter followed by the [image family](https://docs.cloud.google.com/compute/docs/images/image-families-best-practices#how-to-use) or the `--image` parameter followed by the image name for a specific image version. For example, to use the most recent image from the Debian 10 family, add `--image-family debian-10`. When using public images, the [image project](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/create#--image-project) must be provided using the `--image-project` parameter.
         
         gcloud compute instances create \
             --image-family debian-10 \
             --image-project debian-cloud \
             --no-address \
           mysql-test
         

**Note:** To conform with security best practices, the `--no-address` option creates this instance without an external IP address. However, your instance will need to reach public package repositories during the MySQL installation. To allow internet access, configure Cloud NAT to manage network address translation.
  2. Create a Cloud Router.
         
         gcloud compute routers create nat-router-simple-configuration \
             --network=default
         

  3. Set up and manage network address translation with Cloud NAT.
         
         gcloud compute routers nats create nat-simple-configuration \
             --router=nat-router-simple-configuration \
             --auto-allocate-nat-external-ips \
             --nat-all-subnet-ip-ranges \
             --enable-logging
         

  4. Connect to the instance using `ssh`.
         
         gcloud compute ssh \
             --tunnel-through-iap \
             mysql-test
         

The SSH connection is made using TCP forwarding that is handled by [Identity-Aware Proxy (IAP)](https://docs.cloud.google.com/iap/docs/tcp-forwarding-overview).

**Note:** Depending on your VPC network configuration or organization policies, it may be necessary to [prepare your project for IAP TCP forwarding](https://docs.cloud.google.com/iap/docs/using-tcp-forwarding).



## Install MySQL

The following steps describe how to install MySQL on your Compute Engine instance.

###  Debian 10+ 

**These instructions install MySQL 8 or 5.7.**

Versions 10 and later of Debian contain MariaDB instead of MySQL as part of its package management system. MariaDB maintains compatibility with the MySQL protocol, but has an independently evolving feature set. For more details, see [MariaDB versus MySQL](https://mariadb.com/database-topics/mariadb-vs-mysql/).

To install MySQL, download the release package and manually install using the `dpkg` command.

  1. Install the `wget` dependency.
         
         sudo apt-get install -y wget
         

  2. Download the MySQL Community Server release package.
         
         export DEB_FILE=mysql-apt-config_0.8.20-1_all.deb
         cd /tmp
         curl -L --output ${DEB_FILE} \
              https://dev.mysql.com/get/${DEB_FILE}
         

  3. Verify the integrity of the release package file.
         
         cat > ${DEB_FILE}.md5 << EOL
         799bb0aefb93d30564fa47fc5d089aeb ${DEB_FILE}
         EOL
         md5sum --check ${DEB_FILE}.md5
         

The authenticity and integrity of the file are verified if you see the following output:
         
         mysql-apt-config_0.8.20-1_all.deb: OK
         

  4. After you've verified the file, add the MySQL package to the local package repository.
         
         sudo dpkg -i ${DEB_FILE}
         

You're prompted to confirm the installation options including the MySQL version.

  5. With the top **MySQL Server & Cluster** menu option selected, press **Return** and then use the arrow keys to choose a server version.

This guide expects you to choose either MySQL 8.0 or 5.7. Press **Return** on your keyboard after you have selected the version.

  6. When you are satisfied with the options selected in the configuration menu, use the arrow keys to select `Ok` in the menu and presss **Return** on your keyboard.

  7. Update the package cache.
         
         sudo apt-get update
         

If you receive a GPG error similar to _The following signatures couldn't be verified because the public key is not available: NO_PUBKEY 467B942D3A79BD29_ , import the missing GPG key(s) with a command that follows this pattern:
         
         sudo apt-key adv \
             --keyserver keyserver.ubuntu.com \
             --recv-keys 467B942D3A79BD29
         

In the demonstrative error message, the missing public key is `467B942D3A79BD29`; provide this value with the `--recv-keys` option.

Repeat the command to update the package cache.

  8. Install MySQL. The installation process starts the MySQL service for you.
         
         sudo apt-get -y install mysql-community-server
         

You are prompted to provide some details for the installation such as the root password.




###  Debian 9 

**These instructions install MySQL 8 or 5.7.**

By Default, some versions of Debian, such as Debian 9, install MariaDB as the default MySQL server. MariaDB is designed to be largely compatible with MySQL and can be invoked using the same commands. For details on how MariaDB differs from standard MySQL, see [Moving from MySQL to MariaDB in Debian 9](https://mariadb.com/kb/en/library/moving-from-mysql-to-mariadb-in-debian-9/).

To install MySQL, follow these instructions:

  1. Download the MySQL Community Server release package.
         
         export DEB_FILE=mysql-apt-config_0.8.17-1_all.deb
         cd /tmp
         curl -L --output ${DEB_FILE} \
              https://dev.mysql.com/get/${DEB_FILE}
         

  2. Verify the integrity of the release package file.
         
         cat > ${DEB_FILE}.md5 << EOL
         9e393c991311ead61dcc8313aab8e230 ${DEB_FILE}
         EOL
         md5sum --check ${DEB_FILE}.md5
         

The authenticity and integrity of the file are verified if you see the following output.
         
         mysql-apt-config_0.8.17-1_all.deb: OK
         

  3. After you have verified the file, add the MySQL package to the local package repository.
         
         sudo dpkg -i ${DEB_FILE}
         

You are prompted to confirm the installation options including the MySQL version.

  4. With the top **MySQL Server & Cluster** menu option selected, press **Return** and then use the arrow keys to choose a server version.

This guide expects you to choose either MySQL 8.0 or 5.7. Press **Return** on your keyboard after you have selected the version.

  5. When you are satisfied with the options selected in the configuration menu, use the arrow keys to select `Ok` in the menu and presss **Return** on your keyboard.

  6. Update the package cache.
         
         sudo apt-get update
         

If you receive a GPG error similar to _The following signatures couldn't be verified because the public key is not available: NO_PUBKEY 467B942D3A79BD29_ , import the missing GPG key(s) with a command that follows this pattern:
         
         sudo apt-key adv \
             --keyserver keyserver.ubuntu.com \
             --recv-keys 467B942D3A79BD29
         

In the demonstrative error message, the missing public key is `467B942D3A79BD29`; provide this value with the `--recv-keys` option.

Repeat the command to update the package cache.

  7. Install MySQL. The installation process starts the MySQL service for you.
         
         sudo apt-get -y install mysql-community-server
         




###  Ubuntu 

For **Ubuntu 1804 and earlier** these instructions install **MySQL 5.7**.   
For **Ubuntu 2004 and later** these instructions install **MySQL 8**.

  1. Update the `apt-get` package manager.
         
         sudo apt-get update
         

  2. Install MySQL. The installation process starts the MySQL service for you.
         
         sudo apt-get -y install mysql-server
         

  3. By default in Ubuntu distributions, mysql authenticates the `root` user with the `auth_socket` plugin. Run this query to verify this default configuration:
         
         echo "SELECT user, authentication_string, plugin, host
                 FROM mysql.user WHERE user='root' ;" \
              | sudo mysql -t -u root
         

The output shows that the `root` user connecting from `localhost` will use the `auth_socket` plugin:
         
         +------+-----------------------+-------------+-----------+
         | user | authentication_string | plugin      | host      |
         +------+-----------------------+-------------+-----------+
         | root |                       | auth_socket | localhost |
         +------+-----------------------+-------------+-----------+
         

  4. Change this setting, and change the root password to one that is difficult to guess:
         
         export PASSWORD=`uuidgen`; echo "Root password is : $PASSWORD"
         echo "ALTER USER 'root'@'localhost'
               IDENTIFIED WITH mysql_native_password BY '$PASSWORD'" \
               | sudo mysql -u root
         

The output contains the new root password:
         
         Root password is : 25fe2177-778a-414f-b80e-5fb8c8671de3
         




###  CentOS or RHEL 7 

**These instructions install MySQL 8.**

Version 7 of CentOS and RHEL contain MariaDB instead of MySQL as part of its package management system. To install MySQL, you must first update the package manager.

  1. Download the MySQL Community Server release package.
         
         export RPM_FILE=mysql80-community-release-el7-4.noarch.rpm
         cd /tmp
         curl -L --output ${RPM_FILE} \
              https://dev.mysql.com/get/${RPM_FILE}
         

  2. Verify the integrity of the release package file.
         
         cat > ${RPM_FILE}.md5 << EOL
         8b55d5fc443660fab90f9dc328a4d9ad ${RPM_FILE}
         EOL
         md5sum --check ${RPM_FILE}.md5
         

The authenticity and integrity of the file are verified if you see the following output.
         
         mysql80-community-release-el7-4.noarch.rpm: OK
         

  3. Update the package manager to include MySQL.
         
         sudo rpm -Uvh ${RPM_FILE}
         

  4. Install MySQL.
         
         sudo yum -y install mysql-community-server
         

  5. Start MySQL server.
         
         sudo /usr/bin/systemctl start mysqld
         

  6. Obtain the temporary root password from server logs
         
         sudo cat /var/log/mysqld.log | grep -i 'temporary password'
         




###  Rocky Linux or RHEL 8 

**These instructions install MySQL 8.**

Version 8 of Rocky Linux, CentOS Stream, and RHEL contain MariaDB instead of MySQL as part of its package management system. To install MySQL, you must first update the package manager.

  1. Download the MySQL Community Server release package.
         
         export RPM_FILE=mysql80-community-release-el8-2.noarch.rpm
         cd /tmp
         curl -L --output ${RPM_FILE} \
              https://dev.mysql.com/get/${RPM_FILE}
         

  2. Verify the integrity of the release package file.
         
         cat > ${RPM_FILE}.md5 << EOL
         0ba3feb1c9ee35d30e5ae683accaf54b ${RPM_FILE}
         EOL
         md5sum --check ${RPM_FILE}.md5
         

The authenticity and integrity of the file are verified if you see the following output.
         
         mysql80-community-release-el8-2.noarch.rpm: OK
         

  3. Update the package manager to include MySQL.
         
         sudo rpm -iUvh ${RPM_FILE}
         

  4. Install MySQL. During the installation, disable the AppStream repository, so that the installation will use the community server.
         
         sudo yum module disable -y mysql
         sudo yum install -y \
             --disablerepo=appstream \
           mysql-community-server
         

  5. Start MySQL server.
         
         sudo /usr/bin/systemctl start mysqld
         

  6. Obtain the temporary root password from server logs
         
         sudo cat /var/log/mysqld.log | grep -i 'temporary password'
         




## Improve MySQL installation security

To improve the security of your MySQL installation, run the `mysql_secure_installation` command. If you didn't set a password during the installation process, create a password in this step. For more information about this command, see the MySQL documentation for [mysql_secure_installation](https://dev.mysql.com/doc/refman/5.0/en/mysql-secure-installation.html).
    
    
    sudo mysql_secure_installation
    

## Connect to MySQL

The following steps describe how to connect to MySQL from your `mysql-test` instance.

###  MySQL 8.0 

  1. Connect to MySQL using the MySQL client.
         
         sudo mysql -u root -p
         

**Note:** In most cases, you should use a non-root user account to access your MySQL database. For details on adding a user account, see [Adding User Accounts](https://dev.mysql.com/doc/refman/8.0/en/creating-accounts.html) in the MySQL documentation.

When you connect to MySQL, the prompt changes to `mysql>`.

You can then run MySQL commands. For example, the following command shows the threads running, including the current connection.
         
         mysql> SHOW processlist;
         
         +----+-----------------+-----------+------+---------+------+------------------------+------------------+
         | Id | User            | Host      | db   | Command | Time | State                  | Info             |
         +----+-----------------+-----------+------+---------+------+------------------------+------------------+
         |  5 | event_scheduler | localhost | NULL | Daemon  | 1889 | Waiting on empty queue | NULL             |
         | 14 | root            | localhost | NULL | Query   |    0 | init                   | show processlist |
         +----+-----------------+-----------+------+---------+------+------------------------+------------------+
         2 rows in set (0.00 sec)

You can use the following command to generate a list of users.
         
         mysql> SELECT User, Host, authentication_string FROM mysql.user;
         
         +------------------+-----------+------------------------------------------------------------------------+
         | User             | Host      | authentication_string                                                  |
         +------------------+-----------+------------------------------------------------------------------------+
         | mysql.infoschema | localhost | $A$005$THISISACOMBINATIONOFINVALIDSALTANDPASSWORDTHATMUSTNEVERBRBEUSED |
         | mysql.session    | localhost | $A$005$THISISACOMBINATIONOFINVALIDSALTANDPASSWORDTHATMUSTNEVERBRBEUSED |
         | mysql.sys        | localhost | $A$005$THISISACOMBINATIONOFINVALIDSALTANDPASSWORDTHATMUSTNEVERBRBEUSED |
         | root             | localhost | $A$005$,BS{G+*#cVYxb6x40q0aFS5dp2/Kz6u2vennR5qe0eBKVA/6VW5B            |
         +------------------+-----------+------------------------------------------------------------------------+
         4 rows in set (0.00 sec)

  2. When you are done running commands, use the `exit` command to quit out of the MySQL client, and then use `exit` again to sign out of the Compute Engine instance.
         
         mysql> exit
         
         Bye




###  MySQL 5.7 

  1. Connect to MySQL using the MySQL client.
         
         sudo mysql -u root -p
         

**Note:** In most cases, you should use a non-root user account to access your MySQL database. For details on adding a user account, see [Adding User Accounts](https://dev.mysql.com/doc/refman/8.0/en/creating-accounts.html) in the MySQL documentation.

When you connect to MySQL, the prompt changes to `mysql>`.

You can then run MySQL commands. For example, the following command shows the threads running, including the current connection.
         
         mysql> SHOW processlist;
         
         +----+------+-----------+------+---------+------+-------+------------------+
         | Id | User | Host      | db   | Command | Time | State | Info             |
         +----+------+-----------+------+---------+------+-------+------------------+
         | 51 | root | localhost | NULL | Query   |    0 | NULL  | show processlist |
         +----+------+-----------+------+---------+------+-------+------------------+
         1 row in set (0.00 sec)

You can use the following command to generate a list of users.
         
         mysql> SELECT User, Host, authentication_string FROM mysql.user;
         
         +---------------+-----------+-------------------------------------------+
         | User          | Host      | authentication_string                     |
         +---------------+-----------+-------------------------------------------+
         | root          | localhost | *A047B05AAB007B33F8F2BD1FD404661D167D6348 |
         | mysql.session | localhost | *THISISNOTAVALIDPASSWORDTHATCANBEUSEDHERE |
         | mysql.sys     | localhost | *THISISNOTAVALIDPASSWORDTHATCANBEUSEDHERE |
         +---------------+-----------+-------------------------------------------+
         3 rows in set (0.00 sec)

  2. When you are done running commands, use the `exit` command to quit out of the MySQL client, and then use `exit` again to sign out of the Compute Engine instance.
         
         mysql> exit
         
         Bye




## What's next

  * For more information about MySQL, see the [official MySQL documentation](https://dev.mysql.com/doc).
  * Explore the [wide variety of development stacks](https://docs.cloud.google.com/marketplace/?q=mysql) on Cloud Marketplace that use MySQL.
  * If your requirements include high availability and scalability, consider the following options: 
    * Install [MySQL Cluster](https://www.mysql.com/products/cluster/) on Compute Engine for high availability and scalability through shared-nothing clustering and auto-sharding.
    * Click to deploy [Percona](https://docs.cloud.google.com/marketplace/?q=percona), an open source solution for MySQL clustering, from Cloud Marketplace.
    * Install [Vitess](http://vitess.io/), the open source solution which has served all YouTube database traffic since 2011. Vitess is well-suited for applications that run in containers. For information about using Vitess in a containerized environment, see [Running Vitess on Kubernetes](http://vitess.io/getting-started/).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
