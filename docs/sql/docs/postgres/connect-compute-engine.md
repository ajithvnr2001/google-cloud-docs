---
url: https://docs.cloud.google.com/sql/docs/postgres/connect-compute-engine/
title: Connect from Compute Engine \u00a0|\u00a0 Cloud SQL for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:44:47.092581+00:00
---

# Connect from Compute Engine  |  Cloud SQL for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/postgres/connect-compute-engine/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ PostgreSQL ](https://docs.cloud.google.com/sql/docs/postgres)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/postgres/features)



Send feedback 

#  Connect from Compute Engine Stay organized with collections  Save and categorize content based on your preferences. 

[MySQL](https://docs.cloud.google.com/sql/docs/mysql/connect-compute-engine "View this page for the MySQL database engine") | PostgreSQL | [SQL Server](https://docs.cloud.google.com/sql/docs/sqlserver/connect-compute-engine "View this page for the SQL Server database engine")

This page describes how to use the psql client, installed on a Compute Engine instance, to connect to Cloud SQL.

You can use private IP, public IP, the Cloud SQL Auth Proxy, or the Cloud SQL Auth Proxy Docker image.

**For step-by-step instructions on running a Compute Engine sample web application connected to Cloud SQL,** see the [quickstart for connecting from Compute Engine](https://docs.cloud.google.com/sql/docs/postgres/connect-instance-compute-engine).

## Before you begin

This task does not include instructions for setting up your Compute Engine instance. If you need help with creating and configuring a Compute Engine instance, see the [Compute Engine documentation](https://docs.cloud.google.com/compute/docs/instances/create-start-instance).

Ensure your Compute Engine VM has the proper `scope` to connect using the Cloud SQL Admin API. 

[Configure the service account](https://docs.cloud.google.com/compute/docs/access/create-enable-service-accounts-for-instances#changeserviceaccountandscopes) to have either of the following access scopes: 

  * https://www.googleapis.com/auth/sqlservice.admin
  * https://www.googleapis.com/auth/cloud-platform



If your Compute Engine VM or VPC network restricts outbound traffic, make sure your firewall rules allow outgoing TCP connections on the required destination ports:

  * **Direct connections over private IP, public IP, or Private Service Connect:** Allow outbound TCP connections to the default PostgreSQL port, `5432`, on your Cloud SQL instance's IP address. For direct connections to a [Managed Connection Pooling](https://docs.cloud.google.com/sql/docs/postgres/managed-connection-pooling#ports) server, allow outbound TCP connections to port `6432`. 
  * **Cloud SQL Auth Proxy or Cloud SQL Language Connectors:** Allow outbound TCP connections to port `3307` on your Cloud SQL instance's IP address and port `443` for `sqladmin.googleapis.com` API requests. When using a local TCP socket on the VM, your database client connects to the Cloud SQL Auth Proxy on `127.0.0.1:5432` or the port specified with `--port`.



### Private IP

To connect to Cloud SQL from a Compute Engine instance using private IP, private services access must be set up for your environment and your Cloud SQL instance must be configured to use private IP. Your Compute Engine instance must be in the same region as your Cloud SQL instance, and on the network configured for a private connection. [Learn more](https://docs.cloud.google.com/sql/docs/postgres/configure-private-ip).

### 1\. Configure your instance to use private IP

Use the instructions in [Configuring Private IP Connectivity](https://docs.cloud.google.com/sql/docs/postgres/configure-private-ip).

### 2\. Open a Cloud Shell terminal connection to your Compute Engine instance.

Use the appropriate instructions, depending on the instance's operating system: 

  * For Linux, see [ Connecting to Linux VMs](https://docs.cloud.google.com/compute/docs/instances/connecting-to-instance).
  * For Windows, see [ Connecting to Windows VMs](https://docs.cloud.google.com/compute/docs/instances/connecting-to-windows).



If your Compute Engine instance is running either an RHEL or a CentOS public image, SELinux might block the proxy connection. If this happens, you must configure the SELinux feature to allow the connection. 

For more information about SELinux for RHEL, see [ the RHEL documentation](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/html/selinux_users_and_administrators_guide/index). For more information about SELinux for CentOS, see [the CentOS documentation](https://wiki.centos.org/HowTos/SELinux). 

### 3\. Install the psql client on the Compute Engine instance, if it is not already installed.

### Debian/Ubuntu

Install the psql client from the package manager:
    
    
    sudo apt-get update
    sudo apt-get install postgresql-client

### CentOS/RHEL

Install the psql client from the package manager:
    
    
    sudo yum install postgresql

### openSUSE

Install the psql client from the package manager:
    
    
    sudo zypper install postgresql

### Other platforms

  1. Download the PostgreSQL Core Distribution for your platform from the [PostgreSQL Downloads page](https://www.postgresql.org/download/).   
The Core Distribution includes the psql client. 
  2. Install the PostgreSQL database, following the directions on the download page. 



### 4\. Connect with the psql client.
    
    
    psql -h CLOUD_SQL_PRIVATE_IP_ADDRESS -U USERNAME

You can find the private IP address on the [Cloud SQL instances page](https://console.cloud.google.com/sql/instances/) or by running the following `gcloud` command:
    
    
    gcloud sql instances list

### Public IP

**To connect using public IP:**

### 1\. Add a static IPv4 IP address to the Compute Engine instance, if it does not already have one.

You cannot connect to Compute Engine using IPv6. For information about adding a static IP address, see [ Reserving a new static external IP address](https://docs.cloud.google.com/compute/docs/configure-instance-ip-addresses#reserve_new_static) in the Compute Engine documentation. 

### 2\. Authorize the static IP address of the Compute Engine instance as a network that can connect to your Cloud SQL instance.

For more information, see [Configuring access for public IP connections](https://docs.cloud.google.com/sql/docs/postgres/configure-ip). 

**Note** : Grant authorization only for _static_ IP addresses. Ephemeral IP addresses are temporary; granting them access to your instance creates a security risk because they could be reassigned to a different Compute Engine user later. 

### 3\. Open a Cloud Shell terminal connection to your Compute Engine instance.

Use the appropriate instructions, depending on the instance's operating system: 

  * For Linux, see [ Connecting to Linux VMs](https://docs.cloud.google.com/compute/docs/instances/connecting-to-instance).
  * For Windows, see [ Connecting to Windows VMs](https://docs.cloud.google.com/compute/docs/instances/connecting-to-windows).



If your Compute Engine instance is running either an RHEL or a CentOS public image, SELinux might block the proxy connection. If this happens, you must configure the SELinux feature to allow the connection. 

For more information about SELinux for RHEL, see [ the RHEL documentation](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/html/selinux_users_and_administrators_guide/index). For more information about SELinux for CentOS, see [the CentOS documentation](https://wiki.centos.org/HowTos/SELinux). 

### 4\. Install the psql client on the Compute Engine instance, if it is not already installed.

### Debian/Ubuntu

Install the psql client from the package manager:
    
    
    sudo apt-get update
    sudo apt-get install postgresql-client

### CentOS/RHEL

Install the psql client from the package manager:
    
    
    sudo yum install postgresql

### openSUSE

Install the psql client from the package manager:
    
    
    sudo zypper install postgresql

### Other platforms

  1. Download the PostgreSQL Core Distribution for your platform from the [PostgreSQL Downloads page](https://www.postgresql.org/download/).   
The Core Distribution includes the psql client. 
  2. Install the PostgreSQL database, following the directions on the download page. 



### 5\. Connect with the psql client.
    
    
    psql -h CLOUD_SQL_PUBLIC_IP_ADDR -U USERNAME

You can find the public IP address on the [Cloud SQL instances page](https://console.cloud.google.com/sql/instances/) or by running the following `gcloud` command:
    
    
    gcloud sql instances list

For an example of how to connect using SSL, see [Connecting with SSL](https://docs.cloud.google.com/sql/docs/postgres/connect-admin-ip#connect-ssl). 

### 6\. The psql prompt appears.

### 7\. If you need to keep unused connections alive:

Set the [TCP keepalive](http://tldp.org/HOWTO/TCP-Keepalive-HOWTO/usingkeepalive.html). 

For more information, see [ Communicating between your instances and the Internet](https://docs.cloud.google.com/compute/docs/troubleshooting#communicatewithinternet) in the Compute Engine documentation.

Connections are kept alive automatically for instances.

### Cloud SQL Auth Proxy

**To connect using the Cloud SQL Auth Proxy from Compute Engine:**

### 1\. Enable the Cloud SQL Admin API.

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=sqladmin&redirect=https%3A//console.cloud.google.com)

### 2\. Create a service account.

**Note:** If your Compute Engine instance has either the **Full API access** or **Cloud SQL Admin API** scope, you can skip this step; you do not need to provide a certificate file when you start the Cloud SQL Auth Proxy.If you are connecting from Compute Engine, make sure your VM has the proper `scope` to connect using the Cloud SQL Admin API. 

[ Configure the service account](https://docs.cloud.google.com/compute/docs/access/create-enable-service-accounts-for-instances#changeserviceaccountandscopes) to have either of the following access scopes: 

  * https://www.googleapis.com/auth/sqlservice.admin
  * https://www.googleapis.com/auth/cloud-platform



  1. In the Google Cloud console, go to the **Service accounts** page. 

[Go to Service accounts](https://console.cloud.google.com/iam-admin/serviceaccounts/)

  2. Select the project that contains your Cloud SQL instance. 
  3. Click **Create service account**. 
  4. In the **Service account name** field, enter a descriptive name for the service account. 
  5. Change the **Service account ID** to a unique, recognizable value and then click **Create and continue**. 
  6. Click the **Select a role** field and select one of the following roles: 
     * **Cloud SQL > Cloud SQL Client**
     * **Cloud SQL > Cloud SQL Editor**
     * **Cloud SQL > Cloud SQL Admin**

**Note:** To create a service account with the required permissions, you must have `resourcemanager.projects.setIamPolicy` permission. This permission is included in the Project Owner, Project IAM Admin, and Organization Administrator roles.  
You must also have enabled the Cloud SQL Admin API. If you are using the legacy project roles (Viewer, Editor, Owner), the service account must have at least the Editor role.

  7. Click **Done** to finish creating the service account.
  8. Click the action menu for your new service account and then select **Manage keys**. 
  9. Click the **Add key** drop-down menu and then click **Create new key**. 
  10. Confirm that the key type is JSON and then click **Create**. 

The private key file is downloaded to your machine. You can move it to another location. Keep the key file secure. 




If the Compute Engine instance is in a different project than the Cloud SQL instance, ensure that its service account has the proper permissions in the project that contains the Cloud SQL instance: 

  1. Go to the Compute Engine instances listing in the Google Cloud console.

[Go to the Compute Engine instances listing](https://console.cloud.google.com/compute/instances)

  2. If needed, select the project associated with the Compute Engine instance. 
  3. Select the Compute Engine instance to display its properties. 
  4. In the Compute Engine instance properties, copy the name of the service account.
  5. Go to the **IAM & Admin Projects** page in the Google Cloud console. 

[Go to the IAM & Admin Projects page](https://console.cloud.google.com/iam-admin/iam/project)

  6. Select the project that contains the Cloud SQL instance.
  7. Search for the service account name.
  8. If the service account is already there, and it has a role that includes the `cloudsql.instances.connect` permission, you can proceed to step 4.

The `Cloud SQL Client`, `Cloud SQL Editor` and `Cloud SQL Admin` roles all provide the necessary permission, as do the legacy `Editor` and `Owner` project roles.

  9. Otherwise, add the service account by clicking **Add**.
  10. In the **Add principals** dialog, provide the name of the service account and select a role that include the `cloudsql.instances.connect` permission (any Cloud SQL predefined role other than Viewer will work).

Alternatively, you can use the basic Editor role by selecting **Project > Editor**, but the Editor role includes permissions across Google Cloud. 

If you do not see these roles, your Google Cloud user might not have the `resourcemanager.projects.setIamPolicy` permission. You can check your permissions by going to the [IAM page](https://console.cloud.google.com/iam-admin) in the Google Cloud console and searching for your user id.

  11. Click **Add**. 

You now see the service account listed with the specified role.




### 3\. Open a terminal connection to your Compute Engine instance.

Use the appropriate instructions, depending on the instance's operating system: 

  * For Linux, see [ Connecting to Linux Instances](https://docs.cloud.google.com/compute/docs/instances/connecting-to-instance#gcetools). 
  * For Windows, see [ Connecting to Windows Instances](https://docs.cloud.google.com/compute/docs/instances/connecting-to-windows).



If your Compute Engine instance is running either an RHEL or a CentOS public image, SELinux might block the proxy connection. If this happens, you must configure the SELinux feature to allow the connection. 

For more information about SELinux for RHEL, see [ the RHEL documentation](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/html/selinux_users_and_administrators_guide/index). For more information about SELinux for CentOS, see [the CentOS documentation](https://wiki.centos.org/HowTos/SELinux). 

### 4\. Install the psql client on the Compute Engine instance, if it is not already installed.

### Debian/Ubuntu

Install the psql client from the package manager:
    
    
    sudo apt-get update
    sudo apt-get install postgresql-client

### CentOS/RHEL

Install the psql client from the package manager:
    
    
    sudo yum install postgresql

### openSUSE

Install the psql client from the package manager:
    
    
    sudo zypper install postgresql

### Other platforms

  1. Download the PostgreSQL Core Distribution for your platform from the [PostgreSQL Downloads page](https://www.postgresql.org/download/).   
The Core Distribution includes the psql client. 
  2. Install the PostgreSQL database, following the directions on the download page. 



### 5\. Install the Cloud SQL Auth Proxy on the Compute Engine instance.

Before you begin, you must determine your machine's architecture.

If running on Linux or Mac, you can find this by running the following command:
    
    
      uname -a
      

### Linux 64-bit

  1. Download the Cloud SQL Auth Proxy: 
         
         curl -o cloud-sql-proxy https://storage.googleapis.com/cloud-sql-connectors/cloud-sql-proxy/v2.26.2/cloud-sql-proxy.linux.amd64

  2. Make the Cloud SQL Auth Proxy executable: 
         
         chmod +x cloud-sql-proxy




### Linux 32-bit

  1. Download the Cloud SQL Auth Proxy: 
         
         curl -o cloud-sql-proxy https://storage.googleapis.com/cloud-sql-connectors/cloud-sql-proxy/v2.26.2/cloud-sql-proxy.linux.386

  2. If the `curl` command is not found, run `sudo apt install curl` and repeat the download command.
  3. Make the Cloud SQL Auth Proxy executable: 
         
         chmod +x cloud-sql-proxy




### Windows 64-bit

Right-click <https://storage.googleapis.com/cloud-sql-connectors/cloud-sql-proxy/v2.26.2/cloud-sql-proxy.x64.exe> and select **Save Link As** to download the Cloud SQL Auth Proxy. Rename the file to `cloud-sql-proxy.exe`. 

### Windows 32-bit

Right-click <https://storage.googleapis.com/cloud-sql-connectors/cloud-sql-proxy/v2.26.2/cloud-sql-proxy.x86.exe> and select **Save Link As** to download the Cloud SQL Auth Proxy. Rename the file to `cloud-sql-proxy.exe`. 

### Cloud SQL Auth Proxy Docker image

The Cloud SQL Auth Proxy has different container images, such as `distroless`, `alpine`, and `buster`. The default Cloud SQL Auth Proxy container image uses [`distroless`](https://github.com/GoogleContainerTools/distroless), which contains no shell. If you need a shell or related tools, then download an image based on `alpine` or `buster`. For more information, see [Cloud SQL Auth Proxy Container Images](https://github.com/GoogleCloudPlatform/cloudsql-proxy#container-images).

You can pull the latest image to your local machine using Docker by using the following command:
    
    
    docker pull gcr.io/cloud-sql-connectors/cloud-sql-proxy:2.26.2
    

**Note** : The Cloud SQL Auth Proxy uses a repository that supports the `gcr.io` domain but serves images from Artifact Registry. For more information, see [Transition from Container Registry](https://docs.cloud.google.com/artifact-registry/docs/transition/transition-from-gcr). 

### Other OS

For other operating systems not included here, you can [compile the Cloud SQL Auth Proxy from source](http://github.com/GoogleCloudPlatform/cloudsql-proxy). 

### 6\. Start the Cloud SQL Auth Proxy.

**Note:** If your Compute Engine instance has either the **Full API access** or **Cloud SQL Admin API** scope, you do not need to provide a certificate file when you start the Cloud SQL Auth Proxy.

Depending on your language and environment, you can start the Cloud SQL Auth Proxy using TCP sockets, Unix sockets, or the Cloud SQL Auth Proxy Docker image. The Cloud SQL Auth Proxy binary connects to one or more Cloud SQL instances specified on the command line, and opens a local connection as either TCP or a Unix socket. Other applications and services, such as your application code or database management client tools, can connect to Cloud SQL instances through those TCP or Unix socket connections.

**Warning:** Be careful when binding the Cloud SQL Auth Proxy to an external interface. Anyone with access to that interface/port will be authorized to connect to your instance.

### TCP sockets

For TCP connections, the Cloud SQL Auth Proxy listens on `localhost`(`127.0.0.1`) by default. So, when you specify `--port PORT_NUMBER` for an instance, the local connection is at `127.0.0.1:PORT_NUMBER`.

Alternatively, you can specify a different address for the local connection. For example, here's how to make the Cloud SQL Auth Proxy listen at `0.0.0.0:1234` for the local connection:
    
    
    ./cloud-sql-proxy --address 0.0.0.0 --port 1234 INSTANCE_CONNECTION_NAME

  1. Copy your INSTANCE_CONNECTION_NAME. This can be found on the **Overview** page for your instance in the [Google Cloud console](https://console.cloud.google.com/sql) or by running the following command:
         
         gcloud sql instances describe INSTANCE_NAME --format='value(connectionName)'

For example: myproject:myregion:myinstance.

  2. If the instance has both public and private IP configured, and you want the Cloud SQL Auth Proxy to use the [private IP](https://docs.cloud.google.com/sql/docs/postgres/configure-private-ip) address, you must provide the following option when you start the Cloud SQL Auth Proxy: 
         
         --private-ip

  3. If you are using a service account to authenticate the Cloud SQL Auth Proxy, note the location on your client machine of the private key file that was created when you created the service account.
  4. Start the Cloud SQL Auth Proxy. 

Some possible Cloud SQL Auth Proxy invocation strings:

     * Using Cloud SDK authentication: 
           
           ./cloud-sql-proxy --port 5432 INSTANCE_CONNECTION_NAME

The specified port must not already be in use, for example, by a local database server. 
     * Using a service account and explicitly including the name of the instance connection (recommended for production environments): 
           
           ./cloud-sql-proxy \
           --credentials-file PATH_TO_KEY_FILE INSTANCE_CONNECTION_NAME &

For more information about Cloud SQL Auth Proxy options, see [Options for authenticating the Cloud SQL Auth Proxy](https://docs.cloud.google.com/sql/docs/postgres/connect-auth-proxy#authentication-options). 




### Unix sockets

**Note:** The Cloud SQL Auth Proxy currently does not support Unix sockets on Windows, so this option is only available for Linux and macOS platforms. 

The Cloud SQL Auth Proxy can listen on a Unix socket, which is a Posix standard mechanism for using a folder to manage communication between two processes running on the same host. Advantages to using Unix sockets are improved security and lower latency, however, you cannot access a Unix socket from an external machine.

**Note:** The PostgreSQL standard requires a `.s.PGSQL.5432` suffix in the socket path. Some libraries apply this suffix automatically, but others require you to specify the socket path as follows: 
    
    
      /cloudsql/INSTANCE_CONNECTION_NAME/.s.PGSQL.5432
      

To create and use a Unix socket, the target directory must exist and both the Cloud SQL Auth Proxy and application must have read and write access to it.

  1. Copy your INSTANCE_CONNECTION_NAME. This can be found on the **Overview** page for your instance in the [Google Cloud console](https://console.cloud.google.com/sql) or by running the following command:
         
         gcloud sql instances describe INSTANCE_NAME --format='value(connectionName)'

For example: myproject:myregion:myinstance.

  2. Create the directory where the Cloud SQL Auth Proxy sockets will live: 
         
         sudo mkdir /cloudsql; sudo chmod 777 /cloudsql

  3. If you are using a service account to authenticate the Cloud SQL Auth Proxy, note the location on your client machine of the private key file that was created when you created the service account.
  4. Open a new Cloud Shell terminal window and start the Cloud SQL Auth Proxy. 

Some possible Cloud SQL Auth Proxy invocation strings:

     * Using Google Cloud SDK authentication: 
           
           ./cloud-sql-proxy --unix-socket /cloudsql INSTANCE_CONNECTION_NAME &

     * Using a service account: 
           
           ./cloud-sql-proxy --unix-socket /cloudsql
             --credentials-file PATH_TO_KEY_FILE INSTANCE_CONNECTION_NAME &

Start the Cloud SQL Auth Proxy in its own Cloud Shell terminal so you can monitor its output without it mixing with the output from other programs.

For more information about Cloud SQL Auth Proxy options, see [Options for authenticating the Cloud SQL Auth Proxy](https://docs.cloud.google.com/sql/docs/postgres/connect-auth-proxy#authentication-options). **NOTE:** When using a unix socket to connect to Cloud SQL using the Cloud SQL Auth Proxy, make sure the socket filename's length does not surpass the system's limit. It depends on the system, but it's usually between 91-108 characters. On Linux, the length is usually defined as 108, and you can use the following command to check: 
    
    cat /usr/include/linux/un.h | grep "define UNIX_PATH_MAX"




### Docker

To run the Cloud SQL Auth Proxy in a Docker container, use the Cloud SQL Auth Proxy Docker image available from the [Google Container Registry](https://docs.cloud.google.com/container-registry). 

You can start the Cloud SQL Auth Proxy using either TCP sockets or Unix sockets, with the commands shown below. The options use an INSTANCE_CONNECTION_NAME as the connection string to identify a Cloud SQL instance. You can find the INSTANCE_CONNECTION_NAME on the **Overview** page for your instance in the [Google Cloud console](https://console.cloud.google.com/sql) or by running the following command:
    
    
    gcloud sql instances describe INSTANCE_NAME

For example: `myproject:myregion:myinstance`.

Note: The Cloud SQL Auth Proxy doesn't support listening on Unix domain sockets on Windows.

Depending on your language and environment, you can start the Cloud SQL Auth Proxy using either TCP sockets or Unix sockets. Unix sockets aren't supported for applications written in the Java programming language or for the Windows environment.

### Using TCP sockets
    
    
    docker run -d \
      -v PATH_TO_KEY_FILE:/path/to/service-account-key.json \
      -p 127.0.0.1:5432:5432 \
      gcr.io/cloud-sql-connectors/cloud-sql-proxy:2.26.2 \
      --address 0.0.0.0 --port 5432 \
      --credentials-file /path/to/service-account-key.json INSTANCE_CONNECTION_NAME

If you're using the credentials provided by your Compute Engine instance, don't include the `--credentials-file` parameter and the `-v PATH_TO_KEY_FILE:/path/to/service-account-key.json` line. 

Always specify the `127.0.0.1` prefix in `-p` so that the Cloud SQL Auth Proxy isn't exposed outside the local host. The `--address 0.0.0.0` flag is required to make the port accessible from outside of the Docker container. 

### Using Unix sockets
    
    
    docker run -d -v /cloudsql:/cloudsql \
      -v PATH_TO_KEY_FILE:/path/to/service-account-key.json \
      gcr.io/cloud-sql-connectors/cloud-sql-proxy:2.26.2 \
      --unix-socket /cloudsql \
      --credentials-file /path/to/service-account-key.json INSTANCE_CONNECTION_NAME

If you're using the credentials provided by your Compute Engine instance, don't include the `--credentials-file` parameter and the `-v PATH_TO_KEY_FILE:/path/to/service-account-key.json` line. 

If you're using a container-optimized image, use a writable directory in place of `/cloudsql`, for example: 
    
    
    -v /mnt/stateful_partition/cloudsql:/cloudsql

You can specify more than one instance, separated by spaces. You can also use [Compute Engine metadata](https://docs.cloud.google.com/compute/docs/metadata) to dynamically determine the instances to connect to. [Learn more about the Cloud SQL Auth Proxy parameters.](https://docs.cloud.google.com/sql/docs/postgres/sql-proxy#proxy-startup-options)

### 7\. Start the psql session.

The connection string you use depends on whether you started the Cloud SQL Auth Proxy using a TCP socket or a UNIX socket or Docker.

### TCP sockets

  1. Start the psql client: 
         
         psql "host=127.0.0.1 sslmode=disable dbname=DB_NAME user=USERNAME"

Even though the `sslmode` parameter is set to `disable`, the Cloud SQL Auth Proxy does provide an encrypted connection.

When you connect using TCP sockets, the Cloud SQL Auth Proxy is accessed through `127.0.0.1`.

  2. If prompted, enter the password.
  3. The psql prompt appears. 



### Using Unix sockets

  1. Start the psql client: 
         
         psql "sslmode=disable host=/cloudsql/INSTANCE_CONNECTION_NAME dbname=DB_NAME user=USERNAME"

Even though the `sslmode` parameter is set to `disable`, the Cloud SQL Auth Proxy does provide an encrypted connection.

  2. Enter the password.
  3. The psql prompt appears. 



Need help? For help troubleshooting the proxy, see [Troubleshooting Cloud SQL Auth Proxy connections](https://docs.cloud.google.com/sql/docs/postgres/connect-auth-proxy#troubleshooting), or see our [Cloud SQL Support](https://docs.cloud.google.com/sql/docs/postgres/getting-support) page. 

## What's next

  * Get help [ troubleshooting connection issues](https://docs.cloud.google.com/sql/docs/postgres/connect-auth-proxy#troubleshooting) for the Cloud SQL Auth Proxy.
  * Create [users](https://docs.cloud.google.com/sql/docs/postgres/create-manage-users) and [databases](https://docs.cloud.google.com/sql/docs/postgres/create-manage-databases). 
  * Learn more about [private IP](https://docs.cloud.google.com/sql/docs/postgres/private-ip). 
  * Learn about [ options for connecting to your instance from your application](https://docs.cloud.google.com/sql/docs/postgres/connect-overview#external-connection-methods).
  * Learn about [the psql client](https://www.postgresql.org/docs/current/static/app-psql.html). 
  * Learn about [options for support](https://docs.cloud.google.com/sql/docs/support).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
