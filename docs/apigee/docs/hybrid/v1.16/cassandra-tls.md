---
url: https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/cassandra-tls/
title: Configuring authentication for Cassandra \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T03:45:43.349064+00:00
---

# Configuring authentication for Cassandra  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/cassandra-tls/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Configuring authentication for Cassandra Stay organized with collections  Save and categorize content based on your preferences. 

You are currently viewing version 1.16 of the Apigee hybrid documentation. For more information, see [Supported versions](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions).

Version 1.16 keyboard_arrow_down

Supported versions:

  * [ v1.17 (latest) ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/cassandra-tls.html)
  * [ v1.16 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/cassandra-tls.html)
  * [ v1.15 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.15/cassandra-tls.html)
  * [ v1.14 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/cassandra-tls.html)
  * [ List of supported versions ](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions)

Unsupported versions:

  * [ v1.13 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/cassandra-tls.html)
  * [ v1.12 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/cassandra-tls.html)
  * [ v1.11 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/cassandra-tls.html)
  * [ v1.10 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/cassandra-tls.html)
  * [ v1.9 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/cassandra-tls.html)
  * [ v1.8 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.8/cassandra-tls.html)
  * [ v1.7 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.7/cassandra-tls.html)
  * [ v1.6 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.6/cassandra-tls.html)
  * [ v1.5 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.5/cassandra-tls.html)
  * [ v1.4 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.4/cassandra-tls.html)
  * [ v1.3 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.3/cassandra-tls.html)
  * [ v1.2 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.2/cassandra-tls.html)
  * [ v1.1 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.1/cassandra-tls.html)



This topic explains how to configure authentication for communication between Cassandra nodes and between clients and Cassandra nodes. 

##  How to configure authentication for Cassandra in the runtime plane 

Cassandra provides secure communication between a client machine and a database cluster and between nodes within a cluster. Enabling encryption ensures that data in flight is not compromised and is transferred securely. In Apigee hybrid, TLS is enabled by default for any communication between Cassandra nodes and between clients and Cassandra nodes. 

You can configure the authentication using username/password combinations either placed directly in the overrides file or added to a Kubernetes Secret, as explained in this topic. 

##  About Cassandra user authentication 

The hybrid platform uses Cassandra as the backend datastore for runtime plane data. By default, any of the client communications to Cassandra require authentication. There are multiple client users that communicate with Cassandra. Default passwords are provided for these users. See Changing the default passwords in the overrides file for the steps required to change the default passwords.

These users, including a default user, are described below: 

  1. **DML User** : Used by the client to read and write data to Cassandra (KMS, KVM, Cache and Quota).
  2. **DDL User:** Used by MART for any of the data definition tasks like keyspace creation, update, and deletion.
  3. **Admin User:** Used for any administrative activities performed on cassandra cluster.
  4. **Default Cassandra user:** Cassandra creates a default user when Authentication is enabled and the username is `cassandra`
  5. **JMX User:** Used to authenticate and communicate with the Cassandra JMX interface.
  6. **Jolokia User:** Used to authenticate and communicate with the Cassandra JMX API.



##  About the default Cassandra user 

When Apigee hybrid cluster is created and Cassandra authentication is enabled, the initial user account is the default Cassandra user, identified by the username `cassandra`. The default `cassandra` user functions as a superuser, responsible for tasks such as adding user roles and modifying the database schema. 

The Apigee hybrid `apigee-cassandra-user-setup` job utilizes the default `cassandra` user to establish new roles and update the password associated with this default user. The execution of the `apigee-cassandra-user-setup` job occurs during the initial installation of an Apigee hybrid instance, subsequent instance upgrades, and the provisioning of a new instance as part of region expansion. 

When the Apigee hybrid `apigee-cassandra-user-setup` job is executed, the job needs the ability to update and modify database level configurations either as part of a fresh install or an upgrade. The default `cassandra` user is the only user guaranteed to be present when the `apigee-cassandra-user-setup` job is setting up the new Cassandra pods. Without a known user with superuser access, the Apigee hybrid upgrades and region expansions would not function properly. 

The default `cassandra` user password is changed after initial use as part of additional security measures. This means even if the default `cassandra` user is still enabled, the new password must be known to use the default `cassandra` user. The default `cassandra` user is not used by any other components except `apigee-cassandra-user-setup` job as part of the new install and region expansion. 

##  Changing the default passwords in the overrides file 

As a security best practice, we recommend changing the default passwords for Cassandra. You can do so in the `overrides.yaml` file. Add the following configuration, change the default passwords as you wish, and apply the change to your cluster. See [`cassandra`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#cassandra). You can view the default passwords in your `values.yaml` file. 

**Note:** You can only change these defaults at the time of initial setup. Password rotation or change after hybrid setup is not possible. All the usernames must be in lowercase and no special characters are allowed. 
    
    
    cassandra:
       auth:
         default:  ## the password for the new default user (static username: cassandra)
           password: "NEW_PASSWORD"
         admin: ## the password for the admin user (static username: admin_user)
           password: "NEW_PASSWORD"
         ddl: ## the password for the DDL User (static username: ddl_user)
           password: "NEW_PASSWORD"
         dml: ## the password for the DML User (static username: dml_user)
           password: "NEW_PASSWORD"
         jmx:
           username: "jmxuser" ## the username for the JMX User
           password: "NEW_PASSWORD" ## the password for the JMX User
         jolokia:
           username: "jolokiauser" ## the username to access jolokia interface
           password: "NEW_PASSWORD" ## the password for jolokia user

Note the following: 

  * Certificate Authority (CA) rotation is not supported.
  * A server certificate which is generated with passphrase is not supported.



##  Setting usernames and passwords in a Kubernetes Secret 

This section explains how to configure Cassandra to use Kubernetes Secrets for authentication. 

###  Create the Secret 

Use the following template to configure the Kubernetes Secret. Save the template to a YAML file and edit the required attributes, for example `my-secret.yaml`. Note that if you use this option, you must provide the usernames with each password. 
    
    
    apiVersion: v1
    kind: Secret
    metadata:
      name: SECRET_NAME
      namespace: APIGEE_NAMESPACE
    type: Opaque
    data:
      default.password: DEFAULT_PASSWORD   #base64-encoded string
      admin.user: ADMIN_USERNAME   #base64-encoded string
      admin.password: ADMIN_PASSWORD   #base64-encoded string
      dml.user: DML_USERNAME   #base64-encoded string
      dml.password: DML_PASSWORD   #base64-encoded string
      ddl.user: DDL_USERNAME   #base64-encoded string
      ddl.password: DDL_PASSWORD   #base64-encoded string
      jmx.user: JMX_USERNAME   #base64-encoded string
      jmx.password: JMX_PASSWORD   #base64-encoded string
      jolokia.user: JOLOKIA_USERNAME   #base64-encoded string
      jolokia.password: JOLOKIA_PASSWORD   #base64-encoded string
      

Where SECRET_NAME is the name you choose for the Secret, APIGEE_NAMESPACE is the namespace where the Apigee pods are deployed (default is `apigee`), and each _USERNAME and _PASSWORD are the usernames and passwords for each user. Note that the username and password must be Base64-encoded. 

Apply the Secret to the cluster. For example: 
    
    
    kubectl apply -f SECRET_FILE

Add the Secret to your overrides file: 
    
    
    cassandra:
      auth:
        secret: SECRET_NAME

**Note:** See [`cassandra.auth.secret`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#cassandra-auth-secret) in the Configuration property reference.**Note:** If you are [rotating Cassandra credentials](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/rotating-cassandra-credentials-non-ess), you do not need to apply the updated Cassandra override file to the cluster at this step. Skip applying the datastore chart and continue with the rotation process.

Apply the updated Cassandra override to the cluster: 
    
    
    helm upgrade datastore apigee-datastore/ \
    --namespace APIGEE_NAMESPACE \
    --atomic \
    -f OVERRIDES_FILE.yaml
    

**Note:** If you see an error saying `Error: UPGRADE FAILED: "datastore" has no deployed releases`, replace `upgrade` with `install` and try the command again.

## Check the Cassandra logs

Check the logs as soon as Cassandra starts up. The log below shows you that the Cassandra client connections are encrypted. 
    
    
    kubectl logs apigee-cassandra-2 -n APIGEE_NAMESPACE -f
    
    
    
    INFO  00:44:36 Starting listening for CQL clients on /10.0.2.12:9042 (encrypted)...
    INFO  00:44:36 Binding thrift service to /10.0.2.12:9160
    INFO  00:44:36 enabling encrypted thrift connections between client and server
    INFO  00:44:36 Listening for thrift clients...
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
