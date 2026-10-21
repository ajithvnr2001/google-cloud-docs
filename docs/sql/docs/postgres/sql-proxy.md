---
url: https://docs.cloud.google.com/sql/docs/postgres/sql-proxy/
title: About the Cloud SQL Auth Proxy \u00a0|\u00a0 Cloud SQL for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:29:24.685665+00:00
---

# About the Cloud SQL Auth Proxy  |  Cloud SQL for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/postgres/sql-proxy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ PostgreSQL ](https://docs.cloud.google.com/sql/docs/postgres)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/postgres/features)



Send feedback 

#  About the Cloud SQL Auth Proxy Stay organized with collections  Save and categorize content based on your preferences. 

[MySQL](https://docs.cloud.google.com/sql/docs/mysql/sql-proxy "View this page for the MySQL database engine") | PostgreSQL | [SQL Server](https://docs.cloud.google.com/sql/docs/sqlserver/sql-proxy "View this page for the SQL Server database engine")

This page summarizes the Cloud SQL Auth Proxy and describes how to use it to establish authorized, encrypted, and secured connections to your instances.

**For step-by-step instructions on using the Cloud SQL Auth Proxy,** follow the link for your environment:

  * [Quickstart for using the Cloud SQL Auth Proxy](https://docs.cloud.google.com/sql/docs/postgres/quickstart-proxy-test)
  * [How to connect using the Cloud SQL Auth Proxy](https://docs.cloud.google.com/sql/docs/postgres/connect-auth-proxy)
  * [How to connect using the Cloud SQL Auth Proxy from GKE](https://docs.cloud.google.com/sql/docs/postgres/connect-kubernetes-engine)



You do not need to use the Cloud SQL Auth Proxy or configure SSL to connect to Cloud SQL from [App Engine standard environment](https://docs.cloud.google.com/sql/docs/postgres/connect-app-engine-standard) or [App Engine flexible environment](https://docs.cloud.google.com/sql/docs/postgres/connect-app-engine-flexible).

## Benefits of the Cloud SQL Auth Proxy

The **Cloud SQL Auth Proxy** is a Cloud SQL connector that provides secure access to your instances without a need for [Authorized networks](https://docs.cloud.google.com/sql/docs/postgres/configure-ip) or for [configuring SSL](https://docs.cloud.google.com/sql/docs/postgres/configure-ssl-instance).

The Cloud SQL Auth Proxy and [other Cloud SQL Connectors](https://docs.cloud.google.com/sql/docs/postgres/connect-connectors) have the following benefits:

  * **Secure connections:** The Cloud SQL Auth Proxy automatically encrypts traffic to and from the database using TLS 1.3 with the cipher selection determined by [Go's rules](https://go.dev/blog/tls-cipher-suites). SSL certificates are used to verify client and server identities, and are independent of database protocols; you won't need to manage SSL certificates.
  * **Easier connection authorization:** The Cloud SQL Auth Proxy uses IAM permissions to control who and what can connect to your Cloud SQL instances. Thus, the Cloud SQL Auth Proxy handles authentication with Cloud SQL, removing the need to provide static IP addresses. 
  * **IAM database authentication**. Optionally, the Cloud SQL Auth Proxy supports an automatic refresh of OAuth 2.0 access tokens. For information about this functionality, see [Cloud SQL IAM database authentication](https://docs.cloud.google.com/sql/docs/postgres/authentication). 



The Cloud SQL Auth Proxy does not provide a new connectivity path; it relies on existing IP connectivity. To connect to a Cloud SQL instance using [private IP](https://docs.cloud.google.com/sql/docs/postgres/private-ip), the Cloud SQL Auth Proxy must be on a resource with access to the same VPC network as the instance.

If you're using the Java, Python, or Go languages, then [connect with the corresponding connector](https://docs.cloud.google.com/sql/docs/postgres/connect-connectors) instead of with the Cloud SQL Auth proxy.

## Limitations

You can't use the Cloud SQL Auth Proxy if you're using [context-aware access](https://docs.cloud.google.com/iap/docs/cloud-iap-context-aware-access-howto) and IAM database authentication. When you try to login to the instance, IAM authentication fails.

## How the Cloud SQL Auth Proxy works

The Cloud SQL Auth Proxy works by having a local client running in the local environment. Your application communicates with the Cloud SQL Auth Proxy with the standard database protocol used by your database.

The Cloud SQL Auth Proxy uses a secure tunnel to communicate with its companion process running on the server. Each connection established through the Cloud SQL Auth Proxy creates one connection to the Cloud SQL instance.

When an application connects to Cloud SQL Auth Proxy, it checks whether an existing connection between it and the target Cloud SQL instance is available. If a connection does not exist, it calls Cloud SQL Admin APIs to obtain an ephemeral SSL certificate and uses it to connect to Cloud SQL. Ephemeral SSL certificates expire in approximately an hour. Cloud SQL Auth Proxy refreshes these certificates before they expire.

**Note:** You must allow outgoing (or egress) TCP connections to ports `443` and `3307`.

  * Cloud SQL Connectors call APIs through the `sqladmin.googleapis.com` domain name. This domain name doesn't have a fixed IP address. Therefore, you must allow all egress TCP connections on port `443`. (Port `443` is the standard HTTPS port. Whenever you go to a website or make an API request, the secure connection goes through port `443` of the IP address to which the website or endpoint resolves.)
  * While Cloud SQL Connectors can listen on any port, they create outgoing (or egress) connections to your Cloud SQL instance only on port `3307`. If your client machine has an outbound firewall policy, then make sure it allows outgoing connections to port `3307` on your Cloud SQL instance's IP address. For more information, see [Options for authenticating Cloud SQL Connectors](https://docs.cloud.google.com/sql/docs/postgres/connect-auth-proxy#authentication-options).



For more information about these ports, see [Log in with automatic IAM database authentication](https://docs.cloud.google.com/sql/docs/postgres/iam-logins#log-in-with-automatic). 

The Cloud SQL Auth Proxy doesn't provide [connection pooling](https://docs.cloud.google.com/sql/docs/postgres/manage-connections#pools), but can be paired with other connection pooling to increase efficiency.

**Note:** The connection between the client applications and the Cloud SQL Auth Proxy client on the client machine is not encrypted. We recommend that you run the proxy on the same machine that contains your workload.

The following diagram shows how the Cloud SQL Auth Proxy connects to Cloud SQL:

![Diagram of the Cloud SQL Auth Proxy connecting from client software to SQL instance](https://docs.cloud.google.com/static/sql/images/proxyconnection.svg)

## Requirements for using the Cloud SQL Auth Proxy

To use the Cloud SQL Auth Proxy, you must meet the following requirements:

  * The Cloud SQL Admin API must be enabled.
  * You must provide the Cloud SQL Auth Proxy with [Google Cloud authentication credentials](https://docs.cloud.google.com/sql/docs/postgres/connect-auth-proxy#authentication-options).
  * You must provide the Cloud SQL Auth Proxy with a valid database user account and password.
  * The instance must either have a public IPv4 address, or be configured to use [private IP](https://docs.cloud.google.com/sql/docs/postgres/private-ip).

The public IP address does not need to be accessible to any external address (it does not need to be added as an authorized network address).




If the Cloud SQL instance to which you're connecting is using [shared certificate authority (CA)](https://docs.cloud.google.com/sql/docs/postgres/authorize-ssl#shared-regional-ca) for its `serverCaMode` setting, then on the client side, you must use Cloud SQL Auth Proxy version 2.13.0 or later.

If the Cloud SQL instance to which you're connecting is using [customer-managed CA](https://docs.cloud.google.com/sql/docs/postgres/authorize-ssl#customer-managed-ca) for its `serverCaMode` setting, then on the client side, you must use Cloud SQL Auth Proxy version 2.14.3 or later.

When an instance uses customer-managed CA as its server CA mode, you can configure the instance with a [custom DNS name](https://docs.cloud.google.com/sql/docs/postgres/configure-ssl-instance#custom-dns-name). You provide the custom DNS name in the custom subject alternative name (SAN) field of the server certificate.

After you set up a custom DNS name for the instance, you can connect to the instance from Cloud SQL Language Connectors using the DNS name.

## Download and install the Cloud SQL Auth Proxy

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




### macOS 64-bit

  1. Download the Cloud SQL Auth Proxy: 
         
         curl -o cloud-sql-proxy https://storage.googleapis.com/cloud-sql-connectors/cloud-sql-proxy/v2.26.2/cloud-sql-proxy.darwin.amd64

  2. Make the Cloud SQL Auth Proxy executable: 
         
         chmod +x cloud-sql-proxy




### Mac M1

  1. Download the Cloud SQL Auth Proxy: 
         
         curl -o cloud-sql-proxy https://storage.googleapis.com/cloud-sql-connectors/cloud-sql-proxy/v2.26.2/cloud-sql-proxy.darwin.arm64
           

  2. Make the Cloud SQL Auth Proxy executable: 
         
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

**Note:** For Cloud SQL Auth Proxy version 2.17.1 and later, the Cloud SQL Auth Proxy Windows binaries are digitally signed with a Google certificate.

## Cloud SQL Auth Proxy startup options

When you start the Cloud SQL Auth Proxy, you provide it with the following information:

  * What Cloud SQL instances to establish connections to
  * Where it will listen for data coming from your application to be sent to Cloud SQL
  * Where it will find the credentials it will use to authenticate your application to Cloud SQL
  * If required, which IP address type to use.



The Cloud SQL Auth Proxy startup options you provide determine whether it will listen on a TCP port or on a Unix socket. If it is listening on a Unix socket, it creates the socket at the location you choose; usually, the /cloudsql/ directory. For TCP, the Cloud SQL Auth Proxy listens on `localhost` by default.

Run the `cloud-sql-proxy` executable with the argument `--help` to view the complete list of startup options.

**Note:** The Cloud SQL Auth Proxy does not support Unix sockets on Windows. Linux-based operating systems have a maximum socket path length of 108 characters. If the total length of the path exceeds this length, you cannot connect.

You can install the Cloud SQL Auth Proxy anywhere in your local environment. The location of the Cloud SQL Auth Proxy binaries does not impact where it listens for data from your application.

For more information about how to start the Cloud SQL Auth Proxy, see [Start the Cloud SQL Auth Proxy](https://docs.cloud.google.com/sql/docs/postgres/connect-auth-proxy#start-proxy).

## Use a service account for authentication

The Cloud SQL Auth Proxy requires authenticating as a Cloud SQL IAM identity to authorize your connections to a Cloud SQL instance.

The advantage of using a service account for this purpose is that you can create a credential file specifically for the Cloud SQL Auth Proxy, and it is explicitly and permanently linked to the Cloud SQL Auth Proxy as long as it is running. For this reason, using a service account is the recommended method for production instances not running on a Compute Engine instance.

The credential file can be duplicated in a system image if you need to invoke the Cloud SQL Auth Proxy from multiple machines.

To use this method, you must create and manage the credential file. Only users with the `resourcemanager.projects.setIamPolicy` permission (such as project owners) can create the service account. If your Google Cloud user does not have this permission, you must have someone else create the service account for you, or use another method to authenticate the Cloud SQL Auth Proxy.

Learn how to [ Create a service account](https://docs.cloud.google.com/sql/docs/postgres/connect-auth-proxy#create-service-account).

### Required permissions for service accounts

When you use a service account to provide the credentials for the Cloud SQL Auth Proxy, you must create it with sufficient permissions. If you are using the finer-grained [Identity Access and Management](https://docs.cloud.google.com/sql/docs/postgres/iam-roles) (IAM) roles to manage your Cloud SQL permissions, you must give the service account a role that includes the `cloudsql.instances.connect` permission. The predefined Cloud SQL roles that include this permission are:

  * Cloud SQL Client
  * Cloud SQL Editor
  * Cloud SQL Admin



If you are using the legacy project roles (Viewer, Editor, Owner), the service account must have at least the Editor role.

## Keep the Cloud SQL Auth Proxy up to date

Google occasionally releases new versions of the Cloud SQL Auth Proxy. You can see what the current version is by checking the [Cloud SQL Auth Proxy GitHub releases page](https://github.com/GoogleCloudPlatform/cloudsql-proxy/releases).

**Note:** you must be running version 1.12 or later to connect using [private IP](https://docs.cloud.google.com/sql/docs/postgres/private-ip).

## API usage

The Cloud SQL Auth Proxy issues requests to the Cloud SQL Admin API. These requests count against the API quota for your project.

The highest API usage occurs when you start the Cloud SQL Auth Proxy. While the Cloud SQL Auth Proxy is running, it issues 2 API calls per hour per connected instance.

## Cloud SQL Auth Proxy parameters and flags

The Cloud SQL Auth Proxy accepts several flags and parameters when it is started. These options determine where and how the Cloud SQL Auth Proxy creates the sockets it uses for communicating with Cloud SQL, and how it authenticates.

For help with Cloud SQL Auth Proxy options, see the following information:

  * [Options for authenticating the Cloud SQL Auth Proxy](https://docs.cloud.google.com/sql/docs/postgres/connect-auth-proxy#authentication-options)
  * [Example Cloud SQL Auth Proxy invocations](https://docs.cloud.google.com/sql/docs/postgres/connect-auth-proxy#invocations)
  * [Cloud SQL Auth Proxy GitHub page](https://github.com/GoogleCloudPlatform/cloudsql-proxy)
  * The Cloud SQL Auth Proxy help, displayed with `./cloud-sql-proxy --help`



## Use the Cloud SQL Auth Proxy in a production environment

When you are using the Cloud SQL Auth Proxy in a production environment, there are some steps you can take to ensure that the Cloud SQL Auth Proxy provides the required availability for your application.

### Ensure that the Cloud SQL Auth Proxy is run as a persistent service

If the Cloud SQL Auth Proxy process is stopped, all existing connections through it are dropped, and your application cannot create any more connections to the Cloud SQL instance with the Cloud SQL Auth Proxy. To prevent this scenario, be sure to run the Cloud SQL Auth Proxy as a persistent service, so that if the Cloud SQL Auth Proxy exits for any reason, it is automatically restarted. This can be accomplished by using a service such as `systemd`, `upstart`, or `supervisor`. For the Windows operating system, run the Cloud SQL Auth Proxy as a Windows Service. In general, make sure the Cloud SQL Auth Proxy has the same uptime requirements as your application process.

**Note:** The Cloud SQL Auth Proxy is a Windows executable but is not a Windows Service. There are several tools available that can wrap a regular application binary as a service.

### How many copies of the Cloud SQL Auth Proxy your application needs

There is no need to create a proxy process for every application process; many application processes can share a single Cloud SQL Auth Proxy process. Run one Cloud SQL Auth Proxy client process per workstation or virtual machine.

If you are using auto-scaling for virtual machines, ensure that the Cloud SQL Auth Proxy is included in your virtual machine configuration, so that whenever a new virtual machine is started, it has its own Cloud SQL Auth Proxy process.

It is up to you to manage how many connections your application requires, whether by limiting or pooling the connections. The Cloud SQL Auth Proxy does not place any limitations on new connection rates or persistent connection count.

### Reduce Cloud SQL Auth Proxy output

If you need to reduce the size of the Cloud SQL Auth Proxy log, you can do so by setting `--quiet` when you start the Cloud SQL Auth Proxy. Keep in mind, however, that doing so reduces the effectiveness of the Cloud SQL Auth Proxy output in diagnosing connection issues.

### How failover affects the Cloud SQL Auth Proxy

If you are running the Cloud SQL Auth Proxy on an instance configured for High Availability, and a failover occurs, connections through the Cloud SQL Auth Proxy are affected the same way as connections over IP: all existing connections are lost, and the application must establish new connections. However, no manual intervention is required; the application can continue using the same connection strings it was before.

If you're connecting to an instance that has a write endpoint, then you can connect to the instance using the write endpoint DNS name instead of the IP address. Using the write endpoint name lets the Cloud SQL Auth Proxy connect to the new primary instance in the event of a switchover or replica failover operation. For more information, see [Connect database clients to instances using the Cloud SQL Auth Proxy or Cloud SQL Language Connectors](https://docs.cloud.google.com/sql/docs/mysql/connect-to-instance-using-write-endpoint#connect-with-proxy-or-connectors)

### Keep the Cloud SQL Auth Proxy Docker image up to date

The Cloud SQL Auth Proxy Docker image is based on a specific version of the Cloud SQL Auth Proxy. When a new version of the Cloud SQL Auth Proxy becomes available, pull the new version of the Cloud SQL Auth Proxy Docker image to keep your environment up to date. You can see the current version of the Cloud SQL Auth Proxy by checking the [ Cloud SQL Auth Proxy GitHub releases page](https://github.com/GoogleCloudPlatform/cloudsql-proxy/releases).

### How to enforce use of the Cloud SQL Auth Proxy

You can enforce the use of the Cloud SQL Auth Proxy in Cloud SQL instance connections using [ConnectorEnforcement](https://cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances#ConnectorEnforcement). With connector enforcement, direct database connection are rejected.

To use connector enforcement, you use the `ConnectorEnforcement` field in the `instances` API.

If you're using a [Private Service Connect-enabled instance](https://docs.cloud.google.com/sql/docs/postgres/about-private-service-connect), then there's a limitation. If the instance has connector enforcement enabled, then you can't create read replicas for the instance. Similarly, if the instance has read replicas, then you can't enable connector enforcement for the instance.

For more information about how to enforce using only the Cloud SQL Auth Proxy or Cloud SQL Language Connectors to connect to an instance, see [Enforce the use of the Cloud SQL Auth Proxy](https://docs.cloud.google.com/sql/docs/postgres/connect-auth-proxy#enforce).

## About the Cloud SQL Proxy Operator

Cloud SQL Proxy Operator is an open-source Kubernetes operator that automates connecting workloads in a GKE cluster to Cloud SQL databases. The Cloud SQL Auth Proxy Operator utilizes a custom resource AuthProxyWorkload that specifies the Cloud SQL Auth Proxy configuration for a specific workload. The Cloud SQL Auth Proxy Operator reads this resource and adds a Cloud SQL Auth Proxy container with the required configuration to the appropriate workloads.

When you install the operator in your GKE cluster and configure your workloads and Cloud SQL instances, the Cloud SQL Auth Proxy Operator automatically configures the Cloud SQL Auth Proxy and connects the GKE workloads to your Cloud SQL instances.

Cloud SQL Auth Proxy Operator also checks the status of the Cloud SQL Auth Proxy. If the Cloud SQL Auth Proxy is unable to connect, the Cloud SQL Auth Proxy Operator outputs debugging information, and provides you with guidance to troubleshoot and repair common configuration issues.

For more information, see [Connect using the Cloud SQL Proxy Operator](https://docs.cloud.google.com/sql/docs/postgres/connect-proxy-operator).

## What's next

  * [Learn more about the Cloud SQL Auth Proxy](https://github.com/GoogleCloudPlatform/cloudsql-proxy).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
