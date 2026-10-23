---
url: https://docs.cloud.google.com/alloydb/docs/connect-laptop/
title: Connect from your laptop \u00a0|\u00a0 AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:44:20.520302+00:00
---

# Connect from your laptop  |  AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/docs/connect-laptop/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)
  * [ Guides ](https://docs.cloud.google.com/alloydb/docs/overview)



Send feedback 

#  Connect from your laptop Stay organized with collections  Save and categorize content based on your preferences. 

To explore AlloyDB for PostgreSQL or work in a local development environment, you can establish a secure connection from your laptop or local workstation to an AlloyDB instance by using the AlloyDB Auth Proxy over a public IP address.

## Before you begin

Before you connect from your laptop, complete the following prerequisites:

  * [Install and initialize the gcloud CLI](https://docs.cloud.google.com/sdk/docs/install-sdk). Use the gcloud CLI to authenticate your commands and retrieve instance details.
  * [Install the `psql` command-line tool](https://docs.cloud.google.com/alloydb/docs/install-psql). Use the `psql` client tool as your PostgreSQL terminal database client.
  * [Download the Auth Proxy client](https://docs.cloud.google.com/alloydb/docs/auth-proxy/connect#install). Use the Auth Proxy client to create a secure tunnel to your AlloyDB instance.
  * Configure required roles.



### Required roles

To connect from your laptop, grant your Identity and Access Management (IAM) principal (user account or service account) the following predefined roles:

  * AlloyDB Client (`roles/alloydb.client`)
  * Service Usage Consumer (`roles/serviceusage.serviceUsageConsumer`)



## Enable public IP on your AlloyDB instance

The most straightforward way to connect from your laptop is to enable public IP on your AlloyDB instance. You can enable public IP when you create an instance or you update an existing instance to enable it.

### Console

  1. Go to the **Clusters** page in the Google Cloud console.

[Go to Clusters](https://console.cloud.google.com/alloydb/clusters)

  2. To view cluster details, click a cluster in the **Resource Name**.

  3. In **Instances in your cluster** , locate the instance you want to connect to.

  4. Click more_vert **Instance actions** and then click **Edit**.

  5. In **Connectivity** , select **Enable Public IP**.

  6. To save your changes, click **Update instance**.




### gcloud

Use the [`gcloud alloydb instances update`](https://docs.cloud.google.com/sdk/gcloud/reference/alloydb/instances/update) command to enable public IP on your instance:
    
    
    gcloud alloydb instances update INSTANCE_ID \
        --cluster=CLUSTER_ID \
        --region=REGION_ID \
        --assign-inbound-public-ip=ASSIGN_IPV4
    

Replace the following:

  * `INSTANCE_ID`: the ID of the AlloyDB instance.
  * `CLUSTER_ID`: the ID of the cluster.
  * `REGION_ID`: the region where the cluster is located.



## Retrieve the instance connection URI

When you start the Auth Proxy client, you must identify your instance using its unique connection URI. Retrieve the connection URI using the gcloud CLI [`alloydb instances describe`](https://docs.cloud.google.com/sdk/gcloud/reference/alloydb/instances/describe) command on your laptop terminal.
    
    
    gcloud alloydb instances describe INSTANCE_ID \
        --cluster=CLUSTER_ID \
        --region=REGION_ID \
        --format="value(name)"
    

The command returns the connection URI, which is formatted similar to the following:
    
    
    projects/myproject/locations/us-central1/clusters/mycluster/instances/myprimary
    

## Start the AlloyDB Auth Proxy with public IP

Now that you have the instance connection URI, start the Auth Proxy client using your laptop terminal. Use the `--public-ip` flag to instruct the AlloyDB Auth Proxy to connect over the public IP network path.
    
    
    ./alloydb-auth-proxy CONNECTION_URI --public-ip
    

Replace `CONNECTION_URI` with the instance connection URI that you obtained in Retrieve the instance connection URI.

When the AlloyDB Auth Proxy starts successfully, the terminal shows that the AlloyDB Auth Proxy is listening for local TCP connections on port `5432`:
    
    
    Authorizing with Application Default Credentials
    Listening on 127.0.0.1:5432
    The proxy has started successfully and is ready for new connections!
    

## Connect to the database using `psql`

While the AlloyDB Auth Proxy is running, open a separate terminal window on your laptop to connect to the database.

Run the `psql` client tool, targeting the local listener address `127.0.0.1` and port `5432`:
    
    
    psql -h 127.0.0.1 -U postgres -d postgres
    

When prompted, enter the password of the `postgres` database user.

The `psql` command connects to the Auth Proxy client, which forwards your connection through a secure tunnel to your AlloyDB instance. The `psql` command shows a prompt, confirming that your laptop is securely connected to the AlloyDB instance:
    
    
    psql (18.2 (Debian 18.2-1), server 16.11)
    Type "help" for help.
    
    postgres=>
    

## What's next

  * [Connection overview](https://docs.cloud.google.com/alloydb/docs/connection-overview)
  * [Choose a connectivity option](https://docs.cloud.google.com/alloydb/docs/choose-alloydb-connectivity)
  * [Connect using Public IP](https://docs.cloud.google.com/alloydb/docs/connect-public-ip)
  * [Best practices for using the AlloyDB AlloyDB Auth Proxy](https://docs.cloud.google.com/alloydb/docs/auth-proxy/best-practices)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
