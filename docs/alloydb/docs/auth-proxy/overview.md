---
url: https://docs.cloud.google.com/alloydb/docs/auth-proxy/overview/
title: About the AlloyDB Auth Proxy \u00a0|\u00a0 AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:43:16.147507+00:00
---

# About the AlloyDB Auth Proxy  |  AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/docs/auth-proxy/overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)
  * [ Guides ](https://docs.cloud.google.com/alloydb/docs/overview)



Send feedback 

#  About the AlloyDB Auth Proxy Stay organized with collections  Save and categorize content based on your preferences. 

The AlloyDB Auth Proxy is a connector that lets you establish authorized, encrypted connections to your AlloyDB for PostgreSQL databases without managing SSL certificates or configuring firewall rules. For a step-by-step guide to using the Auth Proxy, see [Connect using the AlloyDB Auth Proxy](https://docs.cloud.google.com/alloydb/docs/auth-proxy/connect).

## Benefits of using the AlloyDB Auth Proxy

The Auth Proxy provides the following advantages over connecting clients directly to AlloyDB databases:

  * **Identity and Access Management (IAM)-based connection authorization**. The Auth Proxy uses the credentials and permissions of an IAM principal to authorize connections to AlloyDB instances.

  * **Automated IAM authentication**. The Auth Proxy can automatically authenticate database users based on the IAM principal running the proxy.

  * **Secure, encrypted communication**. The Auth Proxy automatically creates, uses, and maintains a mutual TLS (mTLS) 1.3 connection using a 256-bit AES cipher between your client and an AlloyDB instance to verify client and server identities and encrypt data traffic.




For more information about connecting to AlloyDB instances, see [Connection overview](https://docs.cloud.google.com/alloydb/docs/connection-overview).

## How the AlloyDB Auth Proxy works

The AlloyDB Auth Proxy runs as a local client process (`alloydb-auth-proxy`) in your application environment and listens for connections on `localhost` (by default on TCP port `5432`) or on a local Unix domain socket. Your application connects to this local listener by using standard PostgreSQL drivers and wire protocols, while the Auth Proxy client forwards traffic over an encrypted tunnel (mTLS 1.3 with a 256-bit AES cipher) to its companion Auth Proxy server process running on the AlloyDB instance. Each connection established through the Auth Proxy creates one connection to the AlloyDB instance.

When an application connects to the Auth Proxy, the proxy checks whether an existing connection to the target AlloyDB instance is available. If a connection doesn't exist, the proxy calls the AlloyDB API to obtain an ephemeral SSL certificate and uses it to establish the mTLS tunnel to the instance. Ephemeral SSL certificates expire in 24 hours, and the Auth Proxy refreshes them automatically before they expire.

The Auth Proxy calls the AlloyDB API through the domain name `alloydb.googleapis.com` over HTTPS. As a result, your firewall must allow outbound TCP connections on port `443` (HTTPS) from the client machine.

While the Auth Proxy can listen locally on any port, it creates outbound connections to your AlloyDB instance only on TCP port `5433`. If your client host has an outbound firewall, it must allow connections to port `5433` on your AlloyDB instance's IP address and to port `443` for all IP addresses.

You can use the Auth Proxy across all AlloyDB network connectivity paths:

  * **Private services access (default)** : Connects to the instance's internal IP address within a peered Virtual Private Cloud (VPC) network.
  * **Private Service Connect** : Connects through a [Private Service Connect endpoint and private DNS record](https://docs.cloud.google.com/alloydb/docs/configure-private-service-connect#configure-dns) when you pass the `--psc` flag.
  * **Public IP** : Connects to the instance's public IP address when you pass the `--public-ip` flag. Because the Auth Proxy authenticates and encrypts connections by using IAM and mTLS on port `5433`, you don't need to add your client's IP address to [Authorized external networks](https://docs.cloud.google.com/alloydb/docs/connect-public-ip) when connecting through the Auth Proxy.



## How the AlloyDB Auth Proxy authenticates and authorizes connections

To authorize a client's connection to an AlloyDB instance, the Auth Proxy client authenticates to Google Cloud using IAM principal credentials on the client, and then validates that the IAM principal has the AlloyDB Client (`roles/alloydb.client`) and Service Usage Consumer (`roles/serviceusage.serviceUsageConsumer`) IAM roles.

By default, the Auth Proxy client uses [Application Default Credentials](https://docs.cloud.google.com/docs/authentication/application-default-credentials) (ADC) to locate client credentials. This provides a unified, standard way for applications to authenticate automatically without editing or hardcoding configuration values.

### Standard authentication

For standard development and production setups, you don't need to configure custom credentials or flags. The Auth Proxy client automatically resolves credentials using standard environment paths. Depending on the environment you use to run the Auth Proxy client, it locates credentials from the following sources:

  * **Local development**. When you develop locally, you can authenticate using your personal or corporate Google user account. The Auth Proxy client automatically detects and uses these credentials. This is the recommended approach for local development, avoiding the need to download service account key files locally. For end-to-end instructions on setting up a local development environment, see [Connect from your laptop](https://docs.cloud.google.com/alloydb/docs/connect-laptop) and [Install the `psql` command-line tool](https://docs.cloud.google.com/alloydb/docs/install-psql).

  * **Google-managed environments**. When you run your application on a Google Cloud service—such as Compute Engine instances, Google Kubernetes Engine, Cloud Run, Cloud Run functions, or App Engine—credentials from the attached service account are automatically provided by the environment's metadata server. The Auth Proxy client automatically discovers and uses these credentials without extra configuration.

    * If the compute resource is in the same project as the AlloyDB instance, the default service account typically has the necessary permissions to authenticate.
    * If the compute resource and the AlloyDB instance are in different projects, you must add the compute resource's service account to the project containing the AlloyDB instance and grant it the required roles.



### Override credentials

In specific scenarios—such as testing, running outside of Google Cloud, or when you want to bypass standard environment credentials—you can override the credentials using one of the following methods:

  * **A service account key**. Supply the key either through the `GOOGLE_APPLICATION_CREDENTIALS` environment variable or the `--credentials-file` flag. Service account keys are a security risk if they aren't managed correctly, so prefer one of the standard sources when you can.

  * **An existing OAuth 2.0 access token**. Supply the token through the `--token` flag.

  * **gcloud CLI credentials**. Supply these credentials through the `--gcloud-auth` flag. We don't recommend this flag. Run `gcloud auth application-default login` instead.




For more information about how to configure these credentials on the client, see [Connect using the AlloyDB Auth Proxy](https://docs.cloud.google.com/alloydb/docs/auth-proxy/connect#make-credentials-available). For general information about Google Cloud's approach to authentication, see [Authentication overview](https://docs.cloud.google.com/docs/authentication).

## What's next

  * [Connect using the AlloyDB Auth Proxy](https://docs.cloud.google.com/alloydb/docs/auth-proxy/connect).
  * [Connect from your laptop](https://docs.cloud.google.com/alloydb/docs/connect-laptop).
  * [Install the `psql` command-line tool](https://docs.cloud.google.com/alloydb/docs/install-psql).
  * [Explore the Google Cloud GitHub repository for the AlloyDB Auth Proxy](https://github.com/GoogleCloudPlatform/alloydb-auth-proxy).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
