---
url: https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/authentication-kafka-mtls/
title: Configure mTLS authentication \u00a0|\u00a0 Managed Service for Apache Kafka \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:28:12.170739+00:00
---

# Configure mTLS authentication  |  Managed Service for Apache Kafka  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/authentication-kafka-mtls/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Kafka ](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/overview)



Send feedback 

#  Configure mTLS authentication Stay organized with collections  Save and categorize content based on your preferences. 

You can configure your Managed Service for Apache Kafka cluster to authenticate Kafka clients using mutual TLS (mTLS). This method uses client certificates from Certificate Authority Service (CA Service) as the basis for authentication. This option provides an alternative to the default SASL mechanism that uses Identity and Access Management (IAM) principals.

When you use mTLS, authorization must be configured using Kafka ACLs. For foundational concepts, see the following documents:

  * [CA Service overview](https://docs.cloud.google.com/certificate-authority-service/docs/ca-service-overview)

  * [Authentication for Kafka clients](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/authn-types-kafka)

  * [Access control with IAM and Kafka ACLs](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/access-control)




## Before you begin

Before you configure mTLS authentication, complete the following:

  * **Confirm cluster eligibility.** Verify that you have an existing Managed Service for Apache Kafka cluster created after June 24, 2025. Only these clusters support mTLS authentication. To verify your cluster's creation date, use the [`gcloud managed-kafka clusters describe`](https://docs.cloud.google.com/sdk/gcloud/reference/managed-kafka/clusters/describe) command or [view the cluster's details page](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/view-cluster#view-cluster) in the console.

  * **Configure CA Service.** Set up the CA service and CA pools that you intend to use for issuing client certificates. You must create root and subordinate certificates inside the CA pools.

    1. Create a [CA pool](https://docs.cloud.google.com/certificate-authority-service/docs/ca-pool). Note the CA pool ID.

For more information about how to create a CA pool, see [Create a CA pool](https://docs.cloud.google.com/certificate-authority-service/docs/creating-ca-pool#create-ca-pool).

    2. Create and enable a root CA for the pool.

For more information about how to enable a root CA for the pool, see [Create a root CA](https://docs.cloud.google.com/certificate-authority-service/docs/creating-certificate-authorities).

    3. Create and enable one or more subordinate CAs. We recommend using a subordinate CA for issuing client certificates rather than using a root CA directly.

For more information about how to create a subordinate CA, see [Create a subordinate certificate authority](https://docs.cloud.google.com/certificate-authority-service/docs/create-subordinate-ca).




### Required roles and permissions

To configure mTLS, you need to ensure both you (the user) and the Managed Service for Apache Kafka service agent have the necessary IAM permissions. This applies whether you are creating a new cluster or updating an existing one for configuring mTLS.

**User permissions**

To create or configure a Managed Service for Apache Kafka cluster for mTLS, you need permissions to create or update the cluster resource. To do so, ask your administrator to grant you the **Managed Kafka Cluster Editor** (`roles/managedkafka.clusterEditor`) role on the project containing your cluster.

This predefined role contains the `managedkafka.clusters.create` and `managedkafka.clusters.update` permissions. These permissions let you create a new cluster or modify an existing one to add the CA Service (CA) pool configuration required for mTLS.

You don't need separate permissions on the CA Service resources to configure mTLS on the Kafka cluster, as long as you have the full resource path of the CA pool. However, to view, create, or manage CA pools in the Google Cloud console, you would need additional roles specific to CA Service, such as **CA Service Admin** (`roles/privateca.admin`) or **CA Service Operator** (`roles/privateca.operator`).

**Service agent permissions**

For the mTLS integration to function, the Managed Service for Apache Kafka service agent requires permission to access the specified CA pool. The service agent is a Google-managed service account for your project.

  * If your Managed Service for Apache Kafka cluster and the CA pool are in the same project, the service agent has the necessary permissions by default. The `managedkafka.serviceAgent` role, automatically granted to the service agent on your project, includes the required `privateca.caPools.get` permission.

  * If your CA pool is in a different project than your Managed Service for Apache Kafka cluster, you must manually grant the service agent permission to access it. [Grant the **Private CA Pool Reader** (`roles/privateca.poolReader`) role to the service agent](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/authentication-kafka-mtls#grant-permissions) on the project that contains the CA pool.




**Summary of required permissions**

To see the exact permissions required, expand the following section.

#### Required permissions

  * **Permissions for the user:**
    * `managedkafka.clusters.create`: Required to create a new Kafka cluster configured for mTLS.
    * `managedkafka.clusters.update`: Required to update an existing Kafka cluster to configure mTLS.
  * **Permissions for the Managed Service for Apache Kafka service agent:**
    * `privateca.caPools.get`: Required for the service agent to access the CA pool. This is included in the `roles/privateca.poolReader` role.



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined).

### Grant the service agent access to CA pools

If your CA Service CA pool and your Managed Service for Apache Kafka cluster are in different Google Cloud projects, you must grant the cluster's service agent permission to access the CA pool. The Managed Service for Apache Kafka service agent is named `service-CLUSTER_PROJECT_NUMBER@gcp-sa-managedkafka.iam.gserviceaccount.com`.

Grant the **CA Pool Reader** (`roles/privateca.poolReader`) role to the Managed Service for Apache Kafka service agent at the individual pool level (recommended) that contains your CAs or across all pools in the project. This role provides the necessary `privateca.caPools.get` permission.

#### Individual CA pool

Granting permissions to a single CA pool is the recommended approach as it follows the principle of least privilege.

Run the [ `gcloud privateca pools add-iam-policy-binding`](https://docs.cloud.google.com/sdk/gcloud/reference/privateca/pools/add-iam-policy-binding) command:
    
    
    gcloud privateca pools add-iam-policy-binding CA_POOL_ID \
        --location=CA_POOL_LOCATION \
        --member='serviceAccount:service-CLUSTER_PROJECT_NUMBER@gcp-sa-managedkafka.iam.gserviceaccount.com' \
        --role='roles/privateca.poolReader'

Replace the following:

  * CA_POOL_ID: The ID of the CA pool to which you are granting access. For example, `test-mtls-pool1`.

  * CA_POOL_LOCATION: The Google Cloud region where the CA pool is located. For example, `us-central1`.

  * CLUSTER_PROJECT_NUMBER: The project number of the project containing your Managed Service for Apache Kafka cluster. For example, `12341234123`.




#### All CA pools

Alternatively, you can grant the service agent permission to access all CA pools within a project by setting the policy at the project level.

Run the [ `gcloud projects add-iam-policy-binding`](https://docs.cloud.google.com/sdk/gcloud/reference/projects/add-iam-policy-binding) command:
    
    
    gcloud projects add-iam-policy-binding CA_PROJECT_ID \
        --member='serviceAccount:service-CLUSTER_PROJECT_NUMBER@gcp-sa-managedkafka.iam.gserviceaccount.com' \
        --role='roles/privateca.poolReader'

Replace the following:

  * CA_PROJECT_ID: The ID of the project containing the CA pools to which you are granting access. For example, `test-cas-project`.

  * CLUSTER_PROJECT_NUMBER: The project number of the project containing your Managed Service for Apache Kafka cluster. For example, `12341234123`.




## Enable mTLS on a cluster

To enable mTLS, provide your cluster with the resource names of one or more CA Service CA pools to use for client authentication. You can do this when creating a new cluster or by updating an existing one that was created after June 24, 2025.

After you provide the CA pool identifiers, the service automatically downloads the CA certificates from the specified pools and installs them into the truststore of each broker in the cluster.

### Console

You can enable mTLS on a new cluster during creation or on an existing cluster by editing it.

### On a new cluster

  1. In the Google Cloud console, go to the **Clusters** page.

[Go to Clusters](https://console.cloud.google.com/managedkafka/clusters)

  2. Select **Create**. 

The **Create Kafka cluster** page opens.

  3. Follow the steps in [ Create a cluster](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/create-cluster).
  4. Before the final step, locate the section **Optional mTLS configuration**.
  5. Enter the full resource name of a CA pool in the format `projects/PROJECT_ID/LOCATION/LOCATION/caPools/POOL_ID`.
  6. To add more, click **Add CA Pool**. You can add up to 10 CA pools.
  7. (Optional) Enter any principal mapping rules.
  8. Click **Create** to create the cluster with mTLS enabled.



### On an existing cluster

  1. In the Google Cloud console, go to the **Clusters** page. 

[Go to Clusters](https://console.cloud.google.com/managedkafka/clusters)

  2. Click the name of the cluster you want to update.
  3. Click **Edit**.
  4. In the **mTLS configuration** section, add or modify the list of CA pools. You can add up to 10 CA pools.
  5. (Optional) Enter or edit any principal mapping rules.
  6. Click **Save**.



### gcloud

### On a new cluster

  1. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

  2. Run the [ `gcloud managed-kafka clusters create`](https://docs.cloud.google.com/sdk/gcloud/reference/managed-kafka/clusters/create) command with the `--mtls-ca-pools` flag. In this example, two CA pools are configured.
         
         gcloud managed-kafka clusters create CLUSTER_ID \
             --location=LOCATION \
             --cpu=3 \
             --memory=3GiB \
             --subnets=projects/PROJECT_ID/locations/LOCATION/subnetworks/SUBNET_ID \
             --mtls-ca-pools=projects/PROJECT_ID/locations/LOCATION/caPools/POOL_ID_1,projects/PROJECT_ID/locations/LOCATION/caPools/POOL_ID_2




Replace the following:

  * CLUSTER_ID: The ID or name of the cluster.

For more information about how to name a cluster, see [ Guidelines to name a Managed Service for Apache Kafka resource](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/guidelines-resource). For example—`test-mtls-cluster`.

  * LOCATION: The location of the cluster.

For more information about supported locations, see [ Supported Managed Service for Apache Kafka locations](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/locations). For example—`us-central1`.

  * SUBNETS: The list of subnets to connect. Use commas to separate multiple subnet values. 

The format of the subnet is `projects/PROJECT_ID/locations/LOCATION/subnetworks/SUBNET_ID`.

POOL_ID_1: the ID of the first CA pool. For example—`test-mtls-pool1`.

  * POOL_ID_2: the ID of the second CA pool. For example—`test-mtls-pool2`.




### On an existing cluster

  1. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

  2. Use the [ `gcloud managed-kafka clusters update`](https://docs.cloud.google.com/sdk/gcloud/reference/managed-kafka/clusters/update) command. This command overwrites the entire set of pools currently configured. Provide the full list of the required CA pools. In this example, two CA pools are configured.
         
         gcloud managed-kafka clusters update CLUSTER_ID \
             --location=LOCATION \
             --mtls-ca-pools=projects/PROJECT_ID/locations/LOCATION/caPools/POOL_ID_1,projects/PROJECT_ID/locations/LOCATION/caPools/POOL_ID_2




Replace the following:

  * CLUSTER_ID: The ID or name of the cluster.

For more information about how to name a cluster, see [ Guidelines to name a Managed Service for Apache Kafka resource](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/guidelines-resource). For example—`test-mtls-cluster`.

  * LOCATION: The location of the cluster.

For more information about supported locations, see [ Supported Managed Service for Apache Kafka locations](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/locations). For example—`us-central1`.

POOL_ID_1: the ID of the first CA pool. For example—`test-mtls-pool1`.

  * POOL_ID_2: the ID of the second CA pool. For example—`test-mtls-pool2`.




## Configure principal name mapping

When a client authenticates with mTLS, by default the Kafka principal is derived from the certificate's Subject Distinguished Name (DN) and is of the form `User:CN=...,OU=...,O=...,L=...,ST=...,C=...`. Create mapping rules to transform the certificate's Subject DN into a convenient alias that is easier to use in Kafka ACLs. For more information about the form for the Subject DN, see [Customizing SSL User Name](https://kafka.apache.org/37/security/authorization-and-acls/#customizing-ssl-user-name) in the Apache Kafka documentation.

These transformations are defined by the `ssl.principal.mapping.rules` Kafka broker property, which uses regular expressions to extract and reformat parts of the certificate subject.

For example, you can apply a rule to transform a full Subject DN into an alias as follows:

  * **Certificate Subject DN:** `CN=order-processing-app,OU=marketing,O=company,C=US`

  * **Mapping rule:** `RULE:^.*[Cc][Nn]=([a-zA-Z0-9.-]*).*$/$1/L,DEFAULT`

  * **Resulting Kafka principal:** `order-processing-app`




This example rule extracts the Common Name (CN) from the certificate subject and uses it as the principal name in Kafka.

To set a mapping rule on your cluster using Google Cloud CLI, follow these steps. When using the console, you can set the mapping rules while creating or updating a cluster.

  * To update your cluster, use the [`gcloud managed-kafka clusters update`](https://docs.cloud.google.com/sdk/gcloud/reference/managed-kafka/clusters/update) command with the `--ssl-principal-mapping-rules` flag.
        
        gcloud managed-kafka clusters update CLUSTER_ID \
            --location=REGION \
            --ssl-principal-mapping-rules='MAPPING_RULE'
        

Replace the following:

    * `CLUSTER_ID`: the ID of the Managed Service for Apache Kafka cluster that you are creating. For example—`test-kafka-cluster`.

    * `REGION`: the Google Cloud region to create the cluster in. For example—`us-central1`.

    * `MAPPING_RULE*`: the mapping rule you want to apply. For example— `RULE:^.*[Cc][Nn]=([a-zA-Z0-9.-]*).*$/$1/L,DEFAULT`.




For more information about how to write mapping rules, see [Authorization and ACLs](https://kafka.apache.org/37/security/authorization-and-acls/) in the Apache Kafka documentation.

## Configure Kafka ACLs for mTLS principals

By default, any client that successfully authenticates with a valid mTLS certificate is granted full access to the cluster. To enforce the principle of least privilege, you must create Kafka ACLs to define specific permissions for your mTLS principals. The principal for an mTLS client is its certificate's Subject DN (or a mapped alias), prefixed with `User:`.

To create Kafka ACLs, you need the **Managed Kafka ACL Editor** (`roles/managedkafka.aclEditor`) IAM role.

Assume you have an application identified by its certificate that produces messages to `orders-topic` and consumes messages from `analytics-topic`. The application's principal, after being simplified with a mapping rule, is `order-processing-app`. When you create Kafka ACLs, you must prefix the principal with `User:`.

  1. Apply the `WRITE` ACL to the cluster. Run the [`gcloud managed-kafka acls add-acl-entry`](https://docs.cloud.google.com/sdk/gcloud/reference/managed-kafka/acls/add-acl-entry) command to grant `WRITE` permission on the `orders-topic`.
         
         gcloud managed-kafka acls add-acl-entry topic/orders-topic \
             --cluster=CLUSTER_ID \
             --location=REGION \
             --principal=User:order-processing-app \
             --operation=WRITE \
             --permission-type=ALLOW \
             --host="*"
         

Replace the following:

     * `CLUSTER_ID`: the ID of the Managed Service for Apache Kafka cluster that you are creating. For example—`test-kafka-cluster`.

     * `REGION`: the Google Cloud region to create the cluster in. For example—`us-central1`.

  2. Apply the `READ` ACL to the cluster. Run the [`gcloud managed-kafka acls add-acl-entry`](https://docs.cloud.google.com/sdk/gcloud/reference/managed-kafka/acls/add-acl-entry) command to grant `READ` permission on the `analytics-topic`.
         
         gcloud managed-kafka acls add-alc-entry topic/analytics-topic \
             --cluster=CLUSTER_ID \
             --location=REGION \
             --principal=User:order-processing-app \
             --operation=READ \
             --permission-type=ALLOW \
             --host="*"
         




After applying these ACLs, the `order-processing-app` client has only the specific permissions you granted. For more information about how to create ACLs, see [Create Kafka ACLs](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/kafka-acls/create-kafka-acls).

## Configure Kafka clients

After you configure mTLS on your cluster, you must configure your client applications to authenticate using this method. The process involves creating a client certificate and configuring your client's properties to use it.

  1. Create and download a client certificate on your client machine. Run the [`gcloud privateca certificates create`](https://docs.cloud.google.com/sdk/gcloud/reference/privateca/certificates/create) command to issue a new certificate from one of the CA pools that you configured for your cluster.

This command downloads the certificate `client-cert.pem` and its private key `client-key.pem` to your local environment.
         
         gcloud privateca certificates create CERTIFICATE_ID \
             --project=PROJECT_ID \
             --issuer-location=REGION \
             --issuer-pool=POOL_ID \
             --ca=CA_NAME \
             --generate-key \
             --dns-san="client.example.com" \
             --subject="CN=test-client-app" \
             --key-output-file=client-key.pem \
             --cert-output-file=client-cert.pem
         

Replace the following:

     * `CERTIFICATE_ID`: a unique name for the certificate object. For example—`order-app-cert`.

     * `PROJECT_ID`: the ID of the project containing the CA pool. For example—`test-project-12345`.

     * `REGION`: the region where the CA pool is located. For example—`us-central1`.

     * `POOL_ID`: the ID of the CA pool from which to issue the certificate. For example—`test-mtls-pool1`.

     * `CA_NAME`: the name of the Certificate Authority within the pool. For example—`test-sub-ca`.

     * `--dns-san="client.example.com"`: the DNS Subject Alternative Name. You can use any value that is relevant for your client.

     * `--subject="CN=test-client-app"`: the Subject DN. This name is used as the mTLS principal unless you have configured a principal name mapping rule.

  2. View the client certificate, view the certificate subject, and verify `ssl.principal.mapping.rules`. Run the [`gcloud privateca certificates describe`](https://docs.cloud.google.com/sdk/gcloud/reference/privateca/certificates/describe) command:
         
         gcloud privateca certificates describe CERTIFICATE_ID \
            --issuer-pool=POOL_ID \
            --issuer-location=REGION
         

Replace the following:

     * `CERTIFICATE_ID`: the unique name for the certificate object. For example— `order-app-cert`.

     * `POOL_ID`: the ID of the CA pool from which you issued the certificate. For example— `test-mtls-pool1`.

     * `REGION`: the region where the CA pool is located. For example— `us-central1`.

The output is similar to the following:
    
    certificateDescription:
      aiaIssuingCertificateUrls:
      - http://privateca-content-68e092f4-0000-288c-95cf-30fd3814648c.storage.googleapis.com/a6553d092bbedd752e34/ca.crt
      authorityKeyId:
        keyId: 9568aa9d2baa11a097addc2e24adeaebea0d6a2a
      certFingerprint:
        sha256Hash: 230e52b8411fd094048fca194fc6cf80e41b3e8561298aec3519e13cb1fd05eb
      ...
      subjectDescription:
        hexSerialNumber: 2107b74cf5a814043a38a87eeb6cd7c7891a5f
        lifetime: P30D
        notAfterTime: '2025-07-13T15:34:43Z'
        notBeforeTime: '2025-06-13T15:34:44Z'
        subject:
          commonName: test-client-app
        subjectAltName:
          dnsNames:
          - client.example.com
      ...
    

  3. Create a Java KeyStore. Combine the certificate and private key into a `PKCS#12` file, and then import it into a Java KeyStore (`.jks`) file.
         
         # Create a password for the keystore
         export KEYSTORE_PASSWORD="KEYSTORE_PASSWORD"
         
         # Combine the key and cert into a PKCS#12 file
         openssl pkcs12 -export -inkey client-key.pem -in client-cert.pem \
           -name client -out client-keystore.p12 -password "pass:$KEYSTORE_PASSWORD"
         
         # Import the PKCS#12 file into a Java KeyStore
         keytool -importkeystore -srckeystore client-keystore.p12 -srcstoretype pkcs12 \
           -destkeystore client-keystore.jks -srcstorepass "$KEYSTORE_PASSWORD" -deststorepass "$KEYSTORE_PASSWORD"
         

You can verify that the key was stored successfully by running the following command:
         
         keytool -v -list -keystore client-keystore.jks -storepass "$KEYSTORE_PASSWORD"
         

The output is similar to the following:
         
         Keystore type: JKS
         Keystore provider: SUN
         
         Your keystore contains 1 entry
         
         Alias name: client
         Creation date: Jun 13, 2024
         Entry type: Private key entry
         Certificate chain length: 1
         Certificate[1]:
         Owner: CN=test-client-app
         Issuer: CN=test-sub-ca
         ...
         

Note that the `Owner` line shows the certificate Subject DN. By default, Kafka sets the Kafka principal to this exact format: `CN=...,OU=...,O=...,L=...,ST=...,C=...`. For more information, see [Authorization and ACLs](https://kafka.apache.org/37/security/authorization-and-acls/) in the Apache Kafka documentation.

  4. Configure the Kafka client properties and bootstrap address. In your Kafka client application, set the following properties to use the keystore for an SSL connection. Also, make sure to use the correct bootstrap address with port `9192`. For more information about how to set up a client, see [Quickstart: Create a Managed Service for Apache Kafka cluster and connect a client](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/quickstart).
         
         security.protocol=SSL
         ssl.keystore.location=KEYSTORE_LOCATION
         ssl.keystore.password=KEYSTORE_PASSWORD
         bootstrap.servers=CLUSTER_BOOTSTRAP_ADDRESS
         

Replace the following:

     * `KEYSTORE_LOCATION`: the path to the `.jks` file.

     * `KEYSTORE_PASSWORD`: the password for the keystore.

     * `CLUSTER_BOOTSTRAP_ADDRESS`: the bootstrap address of your cluster. To find the bootstrap address, see [View cluster details](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/view-cluster). Make sure to add the port number as `9192`.




### Secure your client configuration

The preceding example involves storing private keys and passwords locally, so we don't recommend it for production environments. For production, handle your client secrets securely. Options include the following:

  * Store the keystore and its password as secrets in [Google Cloud Secret Manager](https://docs.cloud.google.com/secret-manager/docs/overview) and retrieve them at runtime in your application code.

  * If you deploy your application on GKE, use the [Secret Manager add-on](https://docs.cloud.google.com/secret-manager/docs/secret-manager-managed-csi-component) to mount the secrets into your application's file system at runtime.




## Monitor mTLS

You can monitor the health of mTLS certificate updates using metrics and logs in Cloud Monitoring and Cloud Logging.

To proactively monitor the health of mTLS certificate updates, use the `managedkafka.googleapis.com/mtls_truststore_update_count` metric in Monitoring. This metric counts the truststore update attempts and includes a `STATUS` label, which can be `SUCCESS` or a failure reason such as `CA_POOL_FETCH_ERROR`.

The Managed Service for Apache Kafka service attempts to refresh the truststore once per hour for each cluster. We recommend that you create an alert that fires when this metric reports a persistent count of errors for more than three hours, as this might indicate a misconfiguration that requires manual intervention.

Truststore updates consume the quota of the Certificate Authority Service API. It's important to understand the following:

  * The update process calls the `FetchCaCerts` method, which is subject to the **`API requests per minute per region`** quota.

  * This quota usage is attributed to your project that contains the referenced CA pool, and not the Managed Service for Apache Kafka project.

  * The default limit is 400 queries per second (QPS) per region. Given the low frequency of one request per cluster per hour, it's unlikely that these truststore updates causes you to exceed this quota.




You can also track truststore updates by viewing logs in Logging. Look for the following log entries to confirm successful updates:

  * `Managed Service for Apache Kafka updated the mTLS trust store`

  * `Added root CA certificate to trust store`




## Troubleshoot

For information about how to troubleshoot mTLS authentication issues, see [Troubleshoot mTLS issues](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/troubleshooting/troubleshoot-mTLS).

## What's next

  * Learn how to [create a cluster](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/create-cluster).

  * Learn how to [view cluster details](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/view-cluster).




_Apache Kafka® is a registered trademark of The Apache Software Foundation or its affiliates in the United States and/or other countries._

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
