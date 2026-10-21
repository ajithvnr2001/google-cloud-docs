---
url: https://docs.cloud.google.com/data-fusion/docs/how-to/connect-to-cloud-sql-source/
title: Connect to a Cloud SQL-MySQL source \u00a0|\u00a0 Cloud Data Fusion \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:58:25.441165+00:00
---

# Connect to a Cloud SQL-MySQL source  |  Cloud Data Fusion  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-fusion/docs/how-to/connect-to-cloud-sql-source/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Data Fusion ](https://docs.cloud.google.com/data-fusion/docs)
  * [ Guides ](https://docs.cloud.google.com/data-fusion/docs/create-data-pipeline)



Send feedback 

#  Connect to a Cloud SQL-MySQL source Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to connect a private Cloud Data Fusion instance to a private Cloud SQL instance that hosts a MySQL database. A similar setup works for Postgres and SQL Server instances. Public connections are possible.

**Note:** [VPC peering](https://docs.cloud.google.com/data-fusion/docs/how-to/create-private-ip#set-up-vpc-peering) is used to connect the Cloud Data Fusion network to your project's VPC. You can connect the Cloud SQL network to your project's VPC using VPC peering or VPN.  
This page assumes that you're using VPC peering to connect the Cloud SQL network to your project's VPC. If you're using VPN, then don't perform the tasks described on this page. To establish the connection, you can use the internal IP address of the Cloud SQL instance in Cloud Data Fusion.

**Recommended** : For security reasons, use private instances of Cloud SQL and Cloud Data Fusion.

## Create private instances in Cloud Data Fusion and Cloud SQL

To connect to a private Cloud SQL instance from a private Cloud Data Fusion instance, you use a proxy Compute Engine VM. A proxy is required because the Cloud SQL network is not directly peered with the Cloud Data Fusion network, and transitive peers cannot communicate with each other (see the [VPC Network Peering overview](https://docs.cloud.google.com/vpc/docs/vpc-peering)).

To create the private instances, follow these steps:

  1. If you don't already have one, [create a private Cloud Data Fusion instance](https://docs.cloud.google.com/data-fusion/docs/how-to/create-private-ip). This includes:

     1. Setting up a VPC network
     2. Allocating an IP range
  2. [Create a private Cloud SQL instance](https://docs.cloud.google.com/sql/docs/mysql/create-instance) in the same VPC network as your Cloud Data Fusion instance.

  3. After the instance is created, go to the Cloud SQL **Instances** page and expand the **Instance details**. In the **Connect to this instance** section, copy the IP and the connection name.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql/instances)




## Create a private Compute Engine VM

To create the VM, you can enter the following commands in [Cloud Shell](https://docs.cloud.google.com/shell) or another environment where the [Google Cloud SDK](https://docs.cloud.google.com/sdk/docs) is installed.

The commands create a VM with both internal and public IP addresses (`--no-address` isn't specified in the sample VM creation command) so that the VM can access the Container Registry to get the proxy image. You can use internal IPs, but you also must [enable Private Google Access](https://docs.cloud.google.com/vpc/docs/configure-private-google-access) for the subnet where the VM is located.

  1. Export the following environmental variables:
         
         export PROJECT=CUSTOMER_PROJECT
         export REGION=VM_REGION
         export ZONE=`gcloud compute zones list --filter="name=${REGION}" --limit 1 --uri --project=${PROJECT}| sed 's/.*\///'`
         export NETWORK=CUSTOMER_VPC_NETWORK_NAME
         export SUBNET=CUSTOMER_VPC_SUBNET_NAME
         export INSTANCE_NAME=COMPUTE_ENGINE_VM_NAME
         export SQL_CONN=SQL_INSTANCE_CONNECTION_NAME
         export CDF_IP_RANGE=CLOUD_DATA_FUSION_IP_RANGE
         export VM_IMAGE=$(gcloud compute images list --project=$PROJECT --filter=family:cos-stable --format='value(selfLink.scope())' --limit=1)
         export SQL_PORT=DB_PORT # MySQL 3306 # PostgreSQL 5432 # SQLServer 1433
         

Replace the following:

     * `CUSTOMER_PROJECT`: Your project's name
     * `VM_REGION`: The region where the Compute Engine VM is located
     * `CUSTOMER_VPC_NETWORK_NAME`: Your network's name
     * `CUSTOMER_VPC_SUBNET_NAME`: Your subnetwork's name
     * `COMPUTE_ENGINE_VM_NAME`: The name of the Compute Engine VM
     * `SQL_INSTANCE_CONNECTION_NAME`: The connection name from the previous step
     * `CLOUD_DATA_FUSION_IP_RANGE`: The IP address range
     * `DB_PORT`: The port number of the Cloud SQL database
  2. Create a firewall rule to allow Cloud Data Fusion ingress traffic with the following gcloud CLI command:
         
         gcloud compute firewall-rules create allow-private-cdf \
         --allow=tcp:22,tcp:${SQL_PORT} \
         --source-ranges=$CDF_IP_RANGE --network=$NETWORK --project=$PROJECT
         

  3. Create the VM with the following gcloud CLI command:
         
         gcloud compute --project=${PROJECT} instances create ${INSTANCE_NAME} \
         --zone=${ZONE} \
         --machine-type=g1-small \
         --subnet=${SUBNET} \
         --metadata=startup-script="docker run -d -p 0.0.0.0:${SQL_PORT}:${SQL_PORT} gcr.io/cloudsql-docker/gce-proxy:latest /cloud_sql_proxy -instances=${SQL_CONN}=tcp:0.0.0.0:${SQL_PORT}" \
         --maintenance-policy=MIGRATE \
         --scopes=https://www.googleapis.com/auth/cloud-platform \
         --image=${VM_IMAGE} \
         --image-project=cos-cloud
         

  4. Get the VM internal IP with the following gcloud CLI command:
         
         export IP=`gcloud compute \
         --project=${PROJECT} instances describe ${INSTANCE_NAME} \
         --zone ${ZONE} | grep "networkIP" | awk '{print $2}'`
         

  5. Promote the VM internal IP to a static IP with the following gcloud CLI command:
         
         gcloud compute --project=${PROJECT} addresses create mysql-proxy \
         --addresses ${IP} --region ${REGION} --subnet ${SUBNET}
         

  6. Get the IP to be used in Cloud Data Fusion MySQL JDBC connection string when you set up the connection:
         
         echo ${IP}
         




After the VM is created with a static IP, use the IP as the host or enter it in the JDBC connection string to access the MySQL database from Cloud Data Fusion.

## Access MySQL from within Cloud Data Fusion

Before you can connect to the MySQL instance from the Cloud Data Fusion instance, install the MySQL JDBC driver from the Cloud Data Fusion Hub (or directly from [MySQL community downloads](https://dev.mysql.com/downloads/file/?id=462850)).

**Note:** In this case, use the general MySQL driver instead of Cloud SQL-MySQL driver.

Enter the connection details for your MySQL database in Cloud Data Fusion. You can enter the details and test the connection on the **Wrangler** page.

### Optional: Other ways to connect to MySQL

You can access MySQL in the following ways in Cloud Data Fusion:

  * On the **Studio** page, click the MySQL source plugin and enter the connection details.
  * On the **Studio** page, instead use the Database source plugin, which has similar properties (**Connection string** , **Username** , **Password** , and **Connection Arguments**).

**Note:** Unlike the MySQL plugins, the Database plugin isn't designed specifically for MySQL connections. You must understand the JDBC string format to add the connection details.



## Other connections

Although connecting private instances is recommended, the following connections are possible:

  * A public Cloud Data Fusion instance to a public Cloud SQL instance (by using a public Cloud SQL proxy or allowlisting the `0.0.0.0/0` range in an authorized network). See the [public IP connection option](https://cloud.google.com/sql/docs/mysql/connect-overview#public_ip) for Cloud SQL.
  * A private Cloud Data Fusion instance and public Cloud SQL instance (by using a public Cloud SQL proxy in an authorized network).
  * A public Cloud Data Fusion instance and a private Cloud SQL instance.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
