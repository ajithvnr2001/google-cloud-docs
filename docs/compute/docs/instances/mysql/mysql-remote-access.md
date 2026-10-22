---
url: https://docs.cloud.google.com/compute/docs/instances/mysql/mysql-remote-access/
title: Setting up client access over private IP address to MySQL on Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:49:12.347221+00:00
---

# Setting up client access over private IP address to MySQL on Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instances/mysql/mysql-remote-access/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Setting up client access over private IP address to MySQL on Compute Engine Stay organized with collections  Save and categorize content based on your preferences. 

This tutorial walks you through the process of running a MySQL database on a private network in Google Cloud to allow secure, remote access to the database by using [Compute Engine](https://docs.cloud.google.com/compute).

Use this tutorial if you want to install your own MySQL database on Compute Engine, but want to restrict access to only authorized MySQL clients also running on Compute Engine. You might want to manage your own MySQL instance instead of using the [managed service](https://docs.cloud.google.com/sql), due to cross-region instances, advanced usage of parameters, and specific performance needs.

This tutorial describes how to configure your MySQL server app to accept remote traffic from a MySQL client that is installed on a Compute Engine instance on the same private network.

For information about how to choose the right MySQL deployment option, see [How to install MySQL on Compute Engine](https://docs.cloud.google.com/solutions/setup-mysql).

This tutorial assumes that you are familiar with the following:

  * Basic Linux commands
  * Ubuntu-server 18.04
  * MySQL 5.7
  * Compute Engine



## Architecture

In this tutorial, you deploy two Compute Engine instances. One instance is the server and the other instance is the client as depicted in the following diagram:

![Architecture of two deployed instances](https://docs.cloud.google.com/static/architecture/images/mysql-remote-access-architecture.png)

## Objectives

  * Create a Compute Engine instance and install MySQL server.
  * Create a Compute Engine instance and install MySQL client.
  * Configure MySQL server for remote access.
  * Remove public access to the MySQL server.
  * Connect remotely to MySQL.
  * Create a VPC Service Controls firewall rule.



## Costs

In this document, you use the following billable components of Google Cloud: 

  * Compute Engine
  * Cloud Storage



To generate a cost estimate based on your projected usage, use the [pricing calculator](https://docs.cloud.google.com/products/calculator). 

New Google Cloud users might be eligible for a [free trial](https://docs.cloud.google.com/free). 

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. Enable the Compute Engine API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=compute)

  5. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  6. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  7. Enable the Compute Engine API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=compute)




{# disableFinding(cleaning-up) }

When you finish this tutorial, you can avoid continued billing by deleting the resources you created. See Cleaning up for more detail.

## Creating Compute Engine instances

Create two instances for MySQL—a client and a server instance.

### Create a Compute Engine client instance

* Create a Compute Engine instance. Configure the instance as follows: 

  * Name the instance `my-client`. 
  * Set the `--zone` flag to the [zone](https://docs.cloud.google.com/compute/docs/zones#available) in which you want to create your instance. 
  * Set the `--image-project` flag to `ubuntu-os-cloud`. 
  * Set the `--image-family` flag to `ubuntu-1804-lts`. 
  * Set the `--scopes` flag to `https://www.googleapis.com/auth/cloud-platform`. 


    
    
    gcloud compute instances create my-client --zone=ZONE --image-project=ubuntu-os-cloud --image-family=ubuntu-1804-lts --scopes=https://www.googleapis.com/auth/cloud-platform

### Create a Compute Engine server instance

* Create a Compute Engine instance. Configure the instance as follows: 

  * Name the instance `my-server`. 
  * Set the `--zone` flag to the [zone](https://docs.cloud.google.com/compute/docs/zones#available) in which you want to create your instance. 
  * Set the `--image-project` flag to `ubuntu-os-cloud`. 
  * Set the `--image-family` flag to `ubuntu-1804-lts`. 
  * Set the `--scopes` flag to `https://www.googleapis.com/auth/cloud-platform`. 


    
    
    gcloud compute instances create my-server --zone=ZONE --image-project=ubuntu-os-cloud --image-family=ubuntu-1804-lts --scopes=https://www.googleapis.com/auth/cloud-platform

## Installing MySQL client

The following steps describe how to install MySQL on a Compute Engine instance.

  1. To connect to the `my-client` instance, use the `ssh` command. 
  2. Update the `apt-get` package manager. 
         
         sudo apt-get update
         

**Note:** If you receive an error `Could not get lock /var/lib/dpkg/lock`, wait another minute for the boot processes to complete and try again.
  3. Install the MySQL client package. 
         
         sudo apt-get -y install mysql-client-5.7




## Installing MySQL server

The following steps describe how to install MySQL on a Compute Engine instance.

  1. To connect to the `my-server` instance, use the `ssh` command. 
  2. Update the `apt-get` package manager. 
         
         sudo apt-get update
         

**Note:** If you receive an error, "Could not get lock /var/lib/dpkg/lock'", wait another minute for the boot processes to complete and try again.
  3. Install the MySQL server package. 
         
         sudo apt-get -y install mysql-server-5.7




### Improve MySQL installation security

You must establish a root password for MySQL and perform basic security maintenance on your MySQL server configuration. For more information, see the MySQL documentation for [`mysql_secure_installation`](https://dev.mysql.com/doc/refman/5.0/en/mysql-secure-installation.html).

  1. In the SSH session to your `my-server` instance, use the following command to improve the security of your MySQL installation.
         
         sudo mysql_secure_installation
         

  2. Press `enter` to skip setting up the `VALIDATE PASSWORD` plugin.

  3. Enter a new root password twice.

  4. To remove anonymous users, enter `Y` and press `enter`.

  5. To prevent remote root login, enter `Y` and press `enter`.

  6. To remove the test database, enter `Y` and press `enter`.

  7. To reload the privilege tables, enter `Y` and press `enter`.




## Configuring the MySQL server

Before you can remotely connect to the MySQL server, you need to configure it to listen on its internal IP address. Then, you create a non-root user account for the MySQL client to connect to the server.

All MySQL client commands must include certain command-line flags (for example, to authenticate). The MySQL commands in this section include the following flags: `--user` for the username, `-p` for the password, and `-e` to execute the given statement and immediately quit. For more information, see the [MySQL 5.7 command options reference](https://dev.mysql.com/doc/refman/5.7/en/mysql-command-options.html).

  1. In Cloud Shell, use SSH to connect to the `my-server` instance.

  2. Update the `/etc/mysql/mysql.conf.d/mysqld.cnf` configuration file with the following information:
         
         LOCAL_IP=$(curl  http://metadata.google.internal/computeMetadata/v1/instance/network-interfaces/0/ip \
             -H "Metadata-Flavor: Google")
         sudo sed -i "s|bind-address.*|bind-address = $LOCAL_IP|" /etc/mysql/mysql.conf.d/mysqld.cnf
         

  3. Restart the MySQL service to apply the changes to the running server.
         
         sudo service mysql restart
         

  4. Verify that the server is running locally. Replace `[ROOT_PASSWORD]` with the MySQL server root password you established in a previous step.
         
         sudo mysql --user=root -p[ROOT_PASSWORD] -e "show databases"
         

The output appears similar to the following:
         
         +--------------------+
         | Database           |
         +--------------------+
         | information_schema |
         | mysql              |
         | performance_schema |
         | sys                |
         +--------------------+
         




### Create a MySQL user

Remotely connecting as the root user was disabled with the preceding `mysql_secure_installation` command. You need to create a new user with the necessary permissions to allow remote connections.

  1. In Cloud Shell, create an environment variable for the `my-client` internal IP address.
         
         CLIENT_IP=$(gcloud compute instances describe my-client \
             --zone=ZONE \
             --format='value(networkInterfaces[0].networkIP)')
         

  2. Create a new MySQL user with a password. Replace `[MY_PASSWORD]` with your password, `[ROOT_PASSWORD]` with your MySQL root user password.
         
         sudo mysql -uroot -p[ROOT_PASSWORD] \
             -e "CREATE USER 'TESTUSER'@'${CLIENT_IP}' IDENTIFIED BY '[MY_PASSWORD]';"
         

  3. Grant the new MySQL user permission to log on to the server from the internal IP address of `my-client`.
         
         sudo mysql -uroot -p[ROOT_PASSWORD] -e \
             "GRANT ALL PRIVILEGES ON *.* TO 'TESTUSER'@'${CLIENT_IP}' \
             IDENTIFIED BY '[MY_PASSWORD]';"
         




### Remove the external IP address for `my-server`

The `my-server` instance doesn't need an external IP address because the client can access `my-server` through an internal IP address.

  * To remove the external IP address, update the configuration settings in Cloud Shell. Replace `[ZONE]` with your Google Cloud zone.
        
        gcloud compute instances delete-access-config my-server \
            --access-config-name "external-nat" \
            --zone="ZONE"
        




## Verifying remote access from client to server instance

The following steps describe how to connect to the MySQL server on `my-server` from your `my-client` instance.

  1. In Cloud Shell, use SSH to connect to `my-client` instance.
  2. Test your connection by listing the databases.
         
         sudo mysql --host=my-server --user=TESTUSER \
             --password=[MY_PASSWORD] -e "SHOW DATABASES;"
         

Output appears similar to the following:
         
         +--------------------+
         | Database           |
         +--------------------+
         | information_schema |
         | mysql              |
         | performance_schema |
         | sys                |
         +--------------------+
         




These steps verify that your MySQL client can successfully connect to the MySQL server over the internal IP address.

## Firewall considerations in production environments

The default network configuration in Google Cloud includes a firewall rule, `default-allow-internal`, that allows internal traffic between Compute Engine instances on a wide range of ports, including the MySQL port, port `3306`. In non-default environments with an established security footprint, you might need to create a firewall rule to allow your `my-client` instance to communicate with your `my-server` instance over the network. Otherwise, the two instances can't talk to each other.

You can base firewall rules on IP address ranges or tags. IP address ranges are useful if you want to grant access to a wide range of internal IP addresses. Alternatively, if you want to grant access to specific instances on your network, tags provide a more flexible solution. Tags make it easier to add new clients without granting access to a wide range of IP addresses. You need only assign the appropriate tag to the new MySQL client instance. For example, you can create a new firewall rule that allows traffic from all client instances that are tagged with `mysql-client`.

To support firewall rules using tags, you can assign the appropriate tags to the `my-client` and `my-server` VMs in Cloud Shell.
    
    
    gcloud compute instances add-tags my-client --tags mysql-client --zone=ZONE
    
    gcloud compute instances add-tags my-server --tags mysql-server --zone=ZONE
    

### Add a new firewall rule

The following steps describe how to create a new firewall rule to enable instances with the `my-client` tag to communicate with instances that have the `my-server` tag by using port `3306`.

  * In Cloud Shell, create a firewall rule to allow communications from `mysql-client` to `mysql-server`.
        
        gcloud compute firewall-rules create "mysql-remote-access" \
            --allow tcp:3306 --source-tags "mysql-client" \
            --target-tags "mysql-server"
        




You can now connect to MySQL from `my-client`.

## Access considerations from external clients

This tutorial covers access from MySQL clients to MySQL servers both running on Compute Engine. It is beyond the scope of this tutorial to allow access from a client not running on Compute Engine. If you need to allow non-Compute Engine access, modify the following:

  * Add an external IP address to `my-server` to allow external connectivity.
  * Add the source IP address of your external client to the firewall rules.
  * Modify the `TESTUSER` account, or create a user account, that is bound to the source IP address of your external client.



## Clean up

To avoid incurring charges to your Google Cloud account for the resources used in this tutorial, you can either delete the project or delete the instances.

### Delete the project

The easiest way to eliminate billing is to delete the project that you created for the tutorial. 

To delete the project: 

**Caution** : Deleting a project has the following effects: 
     * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
     * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 

If you plan to explore multiple architectures, tutorials, or quickstarts, reusing projects can help you avoid exceeding project quota limits. 

  1. In the Google Cloud console, go to the **Manage resources** page. 

[Go to Manage resources](https://console.cloud.google.com/iam-admin/projects)

  2. In the project list, select the project that you want to delete, and then click **Delete**. 
  3. In the dialog, type the project ID, and then click **Shut down** to delete the project. 



### Delete instances

To delete a Compute Engine instance: 

  1. In the Google Cloud console, go to the **VM instances** page. 

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. Select the checkbox for your `my-server` instance. 
  3. To delete the instance, click more_vert **More actions** , click **Delete** , and then follow the instructions. 



## What's next

  * Read about [high availability for MySQL](https://dev.mysql.com/doc/refman/5.6/en/ha-overview.html).
  * Read about [How to set up MySQL on Compute Engine](https://docs.cloud.google.com/solutions/setup-mysql).
  * [Configure Cloud Logging for MySQL logs.](https://docs.cloud.google.com/monitoring/agent/plugins/mysql)
  * Explore [Cloud SQL](https://docs.cloud.google.com/sql).

  * Explore reference architectures, diagrams, and best practices about Google Cloud. Take a look at our [Cloud Architecture Center](https://docs.cloud.google.com/architecture). 




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
