---
url: https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/security/
title: Managed Service for Apache Spark on clusters security configuration \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-18T05:42:36.539415+00:00
---

# Managed Service for Apache Spark on clusters security configuration  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/security/

"Managed Service for Apache Spark" is the new name for the product formerly known as "Dataproc on Compute Engine" (cluster deployment) and "Google Cloud Serverless for Apache Spark" (serverless deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Spark ](https://docs.cloud.google.com/managed-spark/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-spark/docs/overview/key-concepts)



Send feedback 

#  Managed Service for Apache Spark on clusters security configuration Stay organized with collections  Save and categorize content based on your preferences. 

When you create a Managed Service for Apache Spark cluster, you can enable [Hadoop Secure Mode](https://hadoop.apache.org/docs/r2.8.0/hadoop-project-dist/hadoop-common/SecureMode.html) via [Kerberos](https://web.mit.edu/kerberos/#what_is) to provide multi-tenancy via user authentication, isolation, and encryption inside a Managed Service for Apache Spark cluster.

**User Authentication and Other Google Cloud Platform Services**. Per-user authentication using Kerberos only applies within the cluster. Interactions with other Google Cloud services, such as Cloud Storage, continue to be authenticated as the service account for the cluster.

**Note:** When `fs.defaultFS` is set to a Cloud Storage location, HDFS requests don't go through the HDFS NameNode, and `authN` and `authZ` are not performed through Kerberos. Therefore, HDFS doesn't require a Kerberos ticket.

## Enable Hadoop Secure Mode using Kerberos

Enabling Kerberos and Hadoop Secure Mode for a cluster will include the [MIT distribution of Kerberos](https://web.mit.edu/kerberos/#what_is) and configure [Apache Hadoop YARN](https://hadoop.apache.org/docs/current/hadoop-yarn/hadoop-yarn-site/YARN.html), [HDFS](https://hadoop.apache.org/docs/current/hadoop-project-dist/hadoop-hdfs/HdfsDesign.html), [Hive](https://hive.apache.org/index.html), [Spark](https://spark.apache.org/), and related components to use it for authentication.

Enabling Kerberos creates an on-cluster [Key Distribution Center (KDC)](https://en.wikipedia.org/wiki/Key_distribution_center), that contains service principals and a root principal. The root principal is the account with administrator permissions to the on-cluster KDC. It can also contain standard user principals or be connected via cross-realm trust to another KDC that contains the user principals.

## Create a Kerberos cluster

Set up your Kerberos root principal password and then create a cluster.

### Set up your Kerberos root principal password

The Kerberos root principal is the account with administrator permissions to the on-cluster KDC. To securely provide the password for The Kerberos root principal, users can encrypt it with a [Key Management Service (KMS)](https://docs.cloud.google.com/kms/docs/encrypt-decrypt) key, and then store it in a [Google Cloud Storage bucket](https://docs.cloud.google.com/storage/docs/creating-buckets) that the cluster [service account](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/service-accounts#service_accounts_in_dataproc) can access. The cluster service account must be granted the `cloudkms.cryptoKeyDecrypter` [IAM role](https://docs.cloud.google.com/kms/docs/reference/permissions-and-roles).

  1. Grant the Cloud KMS CryptoKey Encrypter/Decrypter role to the [cluster service account](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/service-accounts#service_accounts_in_dataproc): 
         
         gcloud projects add-iam-policy-binding project-id \
             --member serviceAccount:project-number-compute@developer.gserviceaccount.com \
             --role roles/cloudkms.cryptoKeyDecrypter
         

  2. Create a key ring: 
         
         gcloud kms keyrings create my-keyring --location global
         

  3. Create a key in the key ring: 
         
         gcloud kms keys create my-key \
             --location global \
             --keyring my-keyring \
             --purpose encryption
         

  4. Encrypt your Kerberos root principal password: 
         
         echo "my-password" | \
           gcloud kms encrypt \
             --location=global \
             --keyring=my-keyring \
             --key=my-key \
             --plaintext-file=- \
             --ciphertext-file=kerberos-root-principal-password.encrypted
         

     1. Upload the encrypted password to a [Cloud Storage bucket](https://docs.cloud.google.com/storage/docs/creating-buckets) in your project. 
        1. **Example** : 
               
               gcloud storage cp kerberos-root-principal-password.encrypted gs://my-bucket
               




### Create the cluster

You can use the Google Cloud CLI, the Dataproc API, or the Google Cloud console to enable Kerberos on clusters that use Managed Service for Apache Spark [image version 1.3](https://docs.cloud.google.com/managed-spark/docs/concepts/versioning/dataproc-release-1.3) and later.

### Google Cloud console

  1. Open the [**Create cluster**](https://console.cloud.google.com/dataproc/clusters/create) page. 
  2. Click **Additional configuration** to expand that section.
  3. Edit **Security**.
  4. In the panel that opens, under **Kerberos** , select **Enable** , then provide the password and key information (see the following sections for additional information).



### gcloud CLI command

To create a Kerberos Managed Service for Apache Spark cluster (image version 1.3 and later), use the [`gcloud dataproc clusters create`](https://docs.cloud.google.com/sdk/gcloud/reference/dataproc/clusters/create) command.
    
    
    gcloud dataproc clusters create cluster-name \
        --region=region \
        --image-version=2.0 \
        --kerberos-root-principal-password-uri=gs://my-bucket/kerberos-root-principal-password.encrypted \
        --kerberos-kms-key=projects/project-id/locations/global/keyRings/my-keyring/cryptoKeys/my-key
    

**Use a YAML (or JSON) config file.** Instead of passing `kerberos-*`flags to the `gcloud` command as shown above, you can place kerberos settings in a YAML (or JSON) config file, then reference the config file to create the kerberos cluster.

  1. Create a config file (see SSL Certificates, Additional Kerberos Settings, and Cross-realm trust for additional config settings that can be included in the file): 
         
         root_principal_password_uri: gs://my-bucket/kerberos-root-principal-password.encrypted
         kms_key_uri: projects/project-id/locations/global/keyRings/mykeyring/cryptoKeys/my-key

  2. Use the following `gcloud` command to create the kerberos cluster: 
         
         gcloud dataproc clusters create cluster-name \
             --region=region \
             --kerberos-config-file=local path to config-file \
             --image-version=2.0
         




**Security Considerations.** Managed Service for Apache Spark discards the decrypted form of the password after adding the root principal to the KDC. For security purposes, after creating the cluster you may decide to delete the password file and the key used to decrypt the secret, and remove the service account from the `kmsKeyDecrypter` role. Don't do this if you plan on scaling the cluster up, which requires the password file and key, and the service account role.

### REST API

Kerberos clusters can be created through the [ClusterConfig.SecurityConfig.KerberosConfig](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/ClusterConfig#kerberosconfig) as part of a [clusters.create](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/projects.regions.clusters/create) request. Set `enableKerberos` to true and set the `rootPrincipalPasswordUri` and `kmsKeyUri` fields.

## OS login

On-cluster KDC management can be performed with the `kadmin` command using the root Kerberos user principal or using `sudo kadmin.local`. [Enable OS Login](https://docs.cloud.google.com/compute/docs/instances/managing-instance-access) to control who can run superuser commands.

## SSL certificates

As part of enabling Hadoop Secure Mode, Managed Service for Apache Spark creates a self-signed certificate to enable cluster SSL encryption. As an alternative, you can provide a certificate for cluster SSL encryption by adding the following settings to the configuration file when you create a kerberos cluster:

  * `ssl:keystore_password_uri`: Location in Cloud Storage of the KMS-encrypted file containing the password to the keystore file.
  * `ssl:key_password_uri`: Location in Cloud Storage of the KMS-encrypted file containing the password to the key in the keystore file.
  * `ssl:keystore_uri`: Location in Cloud Storage of the keystore file containing the wildcard certificate and the private key used by cluster nodes.
  * `ssl:truststore_password_uri`: Location in Cloud Storage of the KMS-encrypted file that contains the password to the truststore file.
  * `ssl:truststore_uri`: Location in Cloud Storage of the trust store file containing trusted certificates.



Sample config file:
    
    
    root_principal_password_uri: gs://my-bucket/kerberos-root-principal-password.encrypted
    kms_key_uri: projects/project-id/locations/global/keyRings/mykeyring/cryptoKeys/my-key
    ssl:
      key_password_uri: gs://bucket/key_password.encrypted
      keystore_password_uri: gs://bucket/keystore_password.encrypted
      keystore_uri: gs://bucket/keystore.jks
      truststore_password_uri: gs://bucket/truststore_password.encrypted
      truststore_uri: gs://bucket/truststore.jks

## Additional Kerberos Settings

To specify a Kerberos realm, create a kerberos cluster with the following property added in the Kerberos configuration file:

  * `realm`: The name of the on-cluster Kerberos realm.



If this property is not set, the hostnames' domain (in uppercase) will be the realm.

To specify the master key of the KDC database, create a kerberos cluster with the following property added in the Kerberos configuration file:

  * `kdc_db_key_uri`: Location in Cloud Storage of the KMS-encrypted file containing the KDC database master key.



If this property is not set, Managed Service for Apache Spark will generate the master key.

To specify the ticket granting ticket's maximum lifetime (in hours), create a kerberos cluster with the following property added in the Kerberos configuration file:

  * `tgt_lifetime_hours`: Max lifetime of the ticket granting ticket in hours.



If this property is not set, Managed Service for Apache Spark will set the ticket granting ticket's lifetime to 10 hours.

## Cross-realm trust

The KDC on the cluster initially contains only the root administrator principal and service principals. You can add user principals manually or establish a cross-realm trust with an external KDC or Active Directory server that holds user principals. [Cloud VPN](https://docs.cloud.google.com/network-connectivity/docs/vpn) or [Cloud Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect) is recommended to connect to an on-premise KDC/Active Directory,.

To create a kerberos cluster that supports cross-realm trust, add the following settings to the Kerberos configuration file when you create a kerberos cluster. Encrypt the shared password with KMS and store it in a Cloud Storage bucket that the cluster service account can access.

  * `cross_realm_trust:admin_server`: hostname or address of the remote admin server
  * `cross_realm_trust:kdc`: hostname or address of the remote KDC
  * `cross_realm_trust:realm`: name of the remote realm to be trusted
  * `cross_realm_trust:shared_password_uri`: Location in Cloud Storage of the KMS-encrypted shared password



Sample config file: 
    
    
    root_principal_password_uri: gs://my-bucket/kerberos-root-principal-password.encrypted
    kms_key_uri: projects/project-id/locations/global/keyRings/mykeyring/cryptoKeys/my-key
    cross_realm_trust:
      admin_server: admin.remote.realm
      kdc: kdc.remote.realm
      realm: REMOTE.REALM
      shared_password_uri: gs://bucket/shared_password.encrypted

To enable cross-realm trust to a remote KDC, follow these steps:

  1. Add the following in the `/etc/krb5.conf` file in the remote KDC: 
         
         [realms]
         DATAPROC.REALM = {
           kdc = MASTER-NAME-OR-ADDRESS
           admin_server = MASTER-NAME-OR-ADDRESS
         }

  2. Create the trust user: 
         
         kadmin -q "addprinc krbtgt/DATAPROC.REALM@REMOTE.REALM"
         

  3. When prompted, enter the user's password. The password should match the contents of the encrypted shared password file




To enable cross-realm trust with Active Directory, run the following commands in a PowerShell as Administrator:

  1. Create a KDC definition in Active Directory. 
         
         ksetup /addkdc DATAPROC.REALM DATAPROC-CLUSTER-MASTER-NAME-OR-ADDRESS
         

  2. Create trust in Active Directory. 
         
         netdom trust DATAPROC.REALM /Domain AD.REALM /add /realm /passwordt:TRUST-PASSWORD
         

The password should match the contents of the encrypted shared password file.



## `dataproc` principal

When you submit a job using the Managed Service for Apache Spark [jobs API](https://docs.cloud.google.com/managed-spark/docs/guides/submit-job#submitting_a_job) to a Managed Service for Apache Spark kerberos cluster, it runs as the `dataproc` kerberos principal from the cluster's kerberos realm.

Multi-tenancy is supported within a Managed Service for Apache Spark kerberos cluster if you [submit a job directly](https://docs.cloud.google.com/managed-spark/docs/guides/submit-job#submit_a_job_directly_on_your_cluster), to the cluster, for example using SSH. However, if the job reads or writes to other Google Cloud services, such as Cloud Storage, the job acts as the [cluster's service account](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/service-accounts).

## Default and custom cluster properties

Hadoop secure mode is configured with [properties in config files](https://hadoop.apache.org/docs/r2.8.0/hadoop-project-dist/hadoop-common/SecureMode.html#Configuration). Managed Service for Apache Spark sets default values for these properties.

You can override the default properties when you create the cluster with the [`gcloud dataproc clusters create`](https://docs.cloud.google.com/sdk/gcloud/reference/dataproc/clusters/create#--properties) `--properties` flag or by calling the [clusters.create](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/projects.regions.clusters/create) API and setting [SoftwareConfig properties](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/ClusterConfig#softwareconfig) (see [cluster properties examples](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/cluster-properties#examples)).

## High-Availability mode

In [High Availability (HA) mode](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/high-availability), a kerberos cluster will have 3 KDCs: one on each master. The KDC running on the "first" master (`$CLUSTER_NAME-m-0`) will be the master KDC and also serve as the admin server. The master KDC's database will be synced to the two replica KDCs at 5 minute intervals through a cron job, and the 3 KDCs will serve read traffic.

Kerberos does not natively support real-time replication or automatic failover if the master KDC is down. To perform a manual failover:

  1. On all KDC machines, in `/etc/krb5.conf`, change `admin_server` to the new master's FQDN (Fully Qualified Domain Name). Remove the old master from the KDC list.
  2. On the new master KDC, set up a cron job to propagate the database.
  3. On the new master KDC, restart the admin_server process (`krb5-admin-server`).
  4. On all KDC machines, restart the KDC process (`krb5-kdc`).



## Network configuration

To make sure that worker nodes can talk to the KDC and Kerberos admin Server running on the master, verify that the [VPC firewall rules](https://docs.cloud.google.com/firewall/docs/firewalls) allow ingress TCP and UDP traffic on port 88 and ingress TCP traffic on port 749 on the master. In High-Availability mode, make sure that VPC firewall rules allow ingress TCP traffic on port 754 on the masters to allow the propagation of changes made to the master KDC. Kerberos requires reverse DNS to be properly set up. Also, for host-based service principal canonicalization, make sure reverse DNS is properly set up for the cluster's network.

## What's next

  * See the [MIT Kerberos documentation](https://web.mit.edu/kerberos/krb5-devel/doc/admin/install_kdc.html).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-16 UTC."],[],[]] 
