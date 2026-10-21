---
url: https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/storing-cassandra-secrets-in-vault/
title: Storing Cassandra secrets in Hashicorp Vault \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T15:51:03.558212+00:00
---

# Storing Cassandra secrets in Hashicorp Vault  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/storing-cassandra-secrets-in-vault/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Storing Cassandra secrets in Hashicorp Vault Stay organized with collections  Save and categorize content based on your preferences. 

You are currently viewing version 1.13 of the Apigee hybrid documentation. **This version is end of life.** You should upgrade to a newer version. For more information, see [Supported versions](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions).

Version 1.13 keyboard_arrow_down

Supported versions:

  * [ v1.17 (latest) ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/storing-cassandra-secrets-in-vault.html)
  * [ v1.16 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/storing-cassandra-secrets-in-vault.html)
  * [ v1.15 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.15/storing-cassandra-secrets-in-vault.html)
  * [ v1.14 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/storing-cassandra-secrets-in-vault.html)
  * [ List of supported versions ](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions)

Unsupported versions:

  * [ v1.13 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/storing-cassandra-secrets-in-vault.html)
  * [ v1.12 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/storing-cassandra-secrets-in-vault.html)
  * [ v1.11 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/storing-cassandra-secrets-in-vault.html)
  * [ v1.10 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/storing-cassandra-secrets-in-vault.html)
  * [ v1.9 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/storing-cassandra-secrets-in-vault.html)
  * [ v1.8 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.8/storing-cassandra-secrets-in-vault.html)
  * [ v1.7 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.7/storing-cassandra-secrets-in-vault.html)
  * [ v1.6 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.6/storing-cassandra-secrets-in-vault.html)
  * [ v1.5 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.5/storing-cassandra-secrets-in-vault.html)
  * [ v1.4 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.4/storing-cassandra-secrets-in-vault.html)
  * [ v1.3 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.3/storing-cassandra-secrets-in-vault.html)
  * [ v1.2 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.2/storing-cassandra-secrets-in-vault.html)
  * [ v1.1 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.1/storing-cassandra-secrets-in-vault.html)



##  Storing Cassandra secrets in Hashicorp Vault 

This feature allows you to store Cassandra DB credentials for Apigee Hybrid in [Hashicorp Vault](https://www.vaultproject.io/), an external secret manager. External secret managers allow you to manage how secrets are stored in Kubernetes, including managing data residency and fine grained access controls.

Before Apigee hybrid version 1.10, the only way to supply passwords for Cassandra users was to specify the password in overrides.yaml. These passwords are stored in Kubernetes secrets. For example:
    
    
    cassandra:
      auth:
        default:
          password: "_********_ "
        admin:
          password: "_********_ "
        ddl:
          password: "_********_ "
        dml:
          password: "_********_ "
        jmx:
          username: "jmxuser"
          password: "_********_ "
        jolokia:
          username: "apigee"
          password: "_********_ "
    

Using Hashicorp Vault, you can supply these passwords via the Kubernetes Secrets Store CSI Driver API ([`SecretProviderClass`](https://secrets-store-csi-driver.sigs.k8s.io/concepts.html#secretproviderclass)). This allows Kubernetes to mount multiple secrets, keys, and certs stored in an external Vault.

### Cassandra users and passwords

You will need to create secrets for the following Cassandra users. Change the default values to meet your organization's security policies.

**Note:** You set the Cassandra usernames when you first install Apigee hybrid. You cannot change them afterwards. The `Default` username must always be `"cassandra"`.**Cassandra User** | **Default username** | **Default password**  
---|---|---  
Admin | `admin_user` | `"********"`  
DDL | `ddl_user` | `"********"`  
Default | **`cassandra`** **Note:** The Default username must always be "cassandra" | `"********"`  
DML | `dml_user` | `"********"`  
JMX | `"jmxuser"` | `"********"`  
Jolokia | `"apigee"` | `"********"`  
  
See [cassandra configuration property](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/config-prop-ref#cassandra) for more information.

## Configure external secret integration

Setting up Vault integration for Apigee hybrid consists of the following procedures. 

  * In the first two procedures, you interact directly with Vault.
  * In the third and fourth procedures, you apply the configurations to your Kubernetes cluster.



Use the following procedures to create the secrets in Vault and enable your hybrid installation to have access to them.

### Create Vault secrets, policies, and roles

  1. Verify that the current Kubernetes context is set to your cluster: 
         
         kubectl config current-context

  2. Use the Vault API, CLI, or UI to create the cassandra secrets. The secret values you create must match the Cassandra usernames and passwords currently used in your cluster. 
     * **Secret key** : Any secret key (or combination of multiple keys) can be used, for example: 
           
           secret/data/apigee/cassandra

     * **Secret data** : Apigee Hybrid expects username and password pairs for the following Cassandra users: Cassandra users  
---  
Admin  
DDL  
Default  
DML  
JMX  
Jolokia  
These username and password values can be spread across any number of secret keys. 
     * **Vault CLI** : The following command shows how to create a single secret containing all the required usernames and passwords: 
           
           vault kv put secret/apigee/cassandra \
               adminUsername="ADMIN_USERNAME" \
               adminPassword="ADMIN_PASSWORD" \
               ddlUsername="DDL_USERNAME" \
               ddlPassword="DDL_PASSWORD" \
               defaultUsername="cassandra" \
               defaultPassword="DEFAULT_PASSWORD" \
               dmlUsername="DML_USERNAME" \
               dmlPassword="DML_PASSWORD" \
               jmxUsername="JMX_USERNAME" \
               jmxPassword="JMX_PASSWORD" \
               jolokiaUsername="JOLOKIA_USERNAME" \
               jolokiaPassword="JOLOKIA_PASSWORD"

**Note** : `data/` should not be included in the secret key when running this command. Vault automatically inserts it.  The default usernames for each user are as follows: Cassandra user | Default value  
---|---  
Admin | `admin_user`  
DDL | `ddl_user`  
Default | `cassandra`  
DML | `dml_user`  
JMX | `jmxuser`  
Jolokia | `apigee`  
**Tip:** You can see the default passwords in the `values.yaml` file in the `apigee-datastore/` chart directory. 
  3. Within Vault, create a policy to grant access to the secret you just created. 
     1. Create a policy file (suggested name: `apigee-cassandra-auth.txt`) with the following contents: 
            
            path "secret/data/apigee/cassandra" {
              capabilities = ["read"]
            }

If you created multiple secrets, each secret must be added to the policy file: 
            
            path "secret/data/apigee/cassandra/admin" {
              capabilities = ["read"]
            }
            
            path "secret/data/apigee/cassandra/ddl" {
              capabilities = ["read"]
            }

**Note** : Do not forget `data/` in the paths (e.g. secret/**data/** apigee/cassandra). 
     2. Apply the policy to Vault: 
            
            vault policy write apigee-cassandra-auth apigee-cassandra-auth.txt

It is possible to create the policy using standard input instead of reading from a file:
            
            echo 'path "secret/data/apigee/cassandra" { capabilities = ["read"] }' | vault policy write apigee-cassandra-auth -

**Note:** `apigee-cassandra-auth` is the policy name. Any value can be used, but this exact value must be specified when binding the policy to Kubernetes service accounts in the next step. 
  4. Bind the policy to the Apigee Cassandra Kubernetes service accounts. 
     1. Define the following environmental variables: 
            
            export ORG_NAME=APIGEE_ORG_NAME
            export ENVS_LIST=LIST_OF_APIGEE-ENVS
            export APIGEE_NAMESPACE=YOUR_APIGEE_NAMESPACE

Where:

        * ORG_NAME is the name of your Apigee organization.
        * ENVS_LIST Is a comma separated list of your Apigee environments, for example `dev,prod`.
        * APIGEE_NAMESPACE is your Apigee namespace. The default is `apigee`.
     2. Create a script with the following contents. The script can have any name. In the following example, the name of the script is `create-vault-cassandra-role.sh`: 
            
            # create-vault-cassandra-role.sh
            
            ORG=ORG_NAME  # ORG name
            ENVS=ENVS_LIST # comma separated env names, for example: dev,prod
            
            org_short_name=$(echo $ORG | head -c 15)
            encode=$(echo -n $ORG | shasum -a 256 | head -c 7)
            org_encode=$(echo "$org_short_name-$encode")
            names=apigee-manager,apigee-cassandra-default,apigee-cassandra-backup-sa,apigee-cassandra-restore-sa,apigee-cassandra-schema-setup-${org_encode},apigee-cassandra-schema-val-${org_encode},apigee-cassandra-user-setup-${org_encode},apigee-mart-${org_encode},apigee-mint-task-scheduler-${org_encode}
            
            for env in ${ENVS//,/ }
            do
              env_short_name=$(echo $env | head -c 15)
              encode=$(echo -n $ORG:$env | shasum -a 256 | head -c 7)
              env_encode=$(echo "$org_short_name-$env_short_name-$encode")
              names+=,apigee-synchronizer-${env_encode},apigee-runtime-${env_encode}
            done
            
            echo $names
            

     3. Run the script and assign the output to the SERVICE_ACCOUNT_NAMES variable. This will create a comma-separated list of Kubernetes service account names. 
            
            export SERVICE_ACCOUNT_NAMES=$(./create-vault-cassandra-role)

**Note:** You may need to `chmod` your script before running it.

Check that the variable was populated with the list:
            
            echo $SERVICE_ACCOUNT_NAMES

     4. Use the Vault CLI to create a role which binds the policy to Kubernetes service accounts: 
            
            vault write auth/kubernetes/role/cassandra \
                bound_service_account_names=${SERVICE_ACCOUNT_NAMES} \
                bound_service_account_namespaces=${APIGEE_NAMESPACE} \
                policies=apigee-cassandra-auth \
                ttl=1m

**Note** : The policy name must match the one created in the previous step (e.g. `apigee-cassandra-auth`). 



### Install CSI driver and Vault provider

Apigee hybrid v1.13.4 supports the following Helm chart versions: 

**Software** | **Version**  
---|---  
Secrets Store CSI Driver | v1.4.4  
Vault | 1.17.2  
  
  1. Follow the [Secrets Store CSI Driver installation instructions](https://secrets-store-csi-driver.sigs.k8s.io/getting-started/installation.html) to Install the CSI driver on your cluster. The CSI driver has a Helm chart for installation. **Note:** On OpenShift installations, grant privileged access to the `secrets-store-csi-driver` service account with the following command: 
         
         oc adm policy add-scc-to-user privileged system:serviceaccount:"${NAMESPACE}":secrets-store-csi-driver

Where NAMESPACE is the namespace where you installed the CSI driver.

  2. Follow the instructions in [Installing the Vault CSI provider](https://developer.hashicorp.com/vault/docs/platform/k8s/csi/installation) to install the Vault CSI provider if you have not installed it already. **Note:** For installations on OpenShift, follow the procedures in [Installation on OpenShift](https://developer.hashicorp.com/vault/docs/platform/k8s/csi/installation#installation-on-openshift). 
     * For KUBERNETES_APPLICATION_NAMESPACE provide the namespace where you installed Vault.
     * For APPLICATION_SERVICE_ACCOUNT provide the name of the Kubernetes service account for Vault. This is usually `vault-csi-provider`. You can check the name of the service account with the following command: 
           
           kubectl -n KUBERNETES_APPLICATION_NAMESPACE get ds vault-csi-provider -oyaml | grep 'serviceAccountName'
           
           serviceAccountName: vault-csi-provider




### Create SecretProviderClass object

The `SecretProviderClass` resource tells the CSI driver what provider to communicate with when requesting secrets. The Cassandra users' credentials must be configured via this object. The following table shows the file names (`objectName`s) expected by Apigee Cassandra:

**Cassandra User** | **Expected secret file names**  
---|---  
Admin | `adminUsername`, `adminPassword`  
DDL | `ddlUsername`, `ddlPassword`  
Default | `cassandra`, `defaultPassword`  
DML | `dmlUsername`, `dmlPassword`  
JMX | `jmxUsername`, `jmxPassword`  
Jolokia | `jolokiaUsername`, `jolokiaPassword`  
  
  1. Create a YAML file for your `SecretProviderClass`. The file name can be anything, for example: `spc.yaml`. Use the following `SecretProviderClass` template to configure this resource: 
         
         apiVersion: secrets-store.csi.x-k8s.io/v1
         kind: SecretProviderClass
         metadata:
           name: apigee-cassandra-auth-spc
         spec:
           provider: vault
           parameters:
             roleName: apigee-cassandra-auth  # the roleName should match the vault role you created earlier in this procedure
         
             # vaultAddress is the endpoint your Vault server is running at.
             # If Vault is running in the same cluster as Apigee, the format will generally be:
             # http://vault.<namespace>.svc.cluster.local:<vaultServicePort>
             vaultAddress: VAULT_ADDRESS
         
             # "objectName" is an alias used within the SecretProviderClass to reference
             # that specific secret. This will also be the filename containing the secret.
             # Apigee Cassandra expects these exact values so they must not be changed.
             # "secretPath" is the path in Vault where the secret should be retrieved.
             # "secretKey" is the key within the Vault secret response to extract a value from.
             # For example, if the Vault secret is located at `secret/data/apigee/cassandra`
             # and you want to specify the admin password, you would use the following:
             # - objectName: "adminPassword"
             #   secretPath: "secret/data/apigee/cassandra"
             #   secretKey: "_key within Vault secret specifying the admin password_ "
             objects: |
               - objectName: "adminUsername"
                 secretPath: ""
                 secretKey: ""
               - objectName: "adminPassword"
                 secretPath: ""
                 secretKey: ""
               - objectName: "defaultUsername"
                 secretPath: ""
                 secretKey: ""
               - objectName: "defaultPassword"
                 secretPath: ""
                 secretKey: ""
               - objectName: "ddlUsername"
                 secretPath: ""
                 secretKey: ""
               - objectName: "ddlPassword"
                 secretPath: ""
                 secretKey: ""
               - objectName: "dmlUsername"
                 secretPath: ""
                 secretKey: ""
               - objectName: "dmlPassword"
                 secretPath: ""
                 secretKey: ""
               - objectName: "jolokiaUsername"
                 secretPath: ""
                 secretKey: ""
               - objectName: "jolokiaPassword"
                 secretPath: ""
                 secretKey: ""
               - objectName: "jmxUsername"
                 secretPath: ""
                 secretKey: ""
               - objectName: "jmxPassword"
                 secretPath: ""
                 secretKey: ""

  2. Apply the `SecretProviderClass` to your `apigee` namespace: 
         
         kubectl -n $APIGEE_NAMESPACE apply -f spc.yaml




### Enable external secret for Cassandra

  1. Within your `overrides.yaml`, add the following configuration to enable external secret usage for Cassandra: 
         
         cassandra:
           auth:
             secretProviderClass: apigee-cassandra-auth-spc  # The name of the SecretProviderClass created in spc.yaml.

**Note:** The name you provide for `cassandra.auth.secretProviderClass` must match the name of the SecretProviderClass you created in the `spc.yaml` file in the previous steps.

See [`cassandra.auth.secretProviderClass`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/config-prop-ref#cassandra-auth-secretproviderclass).

  2. Use `helm upgrade` to apply the change to the `apigee-operator` and `apigee-datastore` components: 
     * The datastore controller in `apigee-operator` takes part in Cassandra decommissioning and data replication during region expansion. These tasks require the JMX and Jolokia credentials. 
           
           helm upgrade operator apigee-operator/ \
             --namespace $APIGEE_NAMESPACE \
             --atomic \
             -f overrides.yaml

     * `apigee-datastore` provides credentials that downstream components like `apigee-runtime`, Synchronizer & MART use when connecting to Cassandra. 
           
           helm upgrade datastore apigee-datastore/ \
             --namespace $APIGEE_NAMESPACE \
             --atomic \
             -f overrides.yaml

  3. Verify external secrets are being used. When external secrets are enabled, new `Volume`s, `Volume Mount`s , and `Environment Variable`s, are added referencing the secrets. 
     * Verify the `apigee-controller-manager` deployment. 

Check that a `Volume` named `apigee-external-secrets` exists and references the `SecretProviderClass` created above:
           
           kubectl -n $APIGEE_NAMESPACE get deployment apigee-controller-manager -o jsonpath='{.spec.template.spec.volumes[?(@.name=="apigee-external-secrets")]}'

Example output:
           
           {
             "csi": {
               "driver": "secrets-store.csi.k8s.io",
               "readOnly": true,
               "volumeAttributes": {
                 "secretProviderClass": "**apigee-cassandra-auth-spc** "
               }
             },
             "name": "**apigee-external-secrets** "
           }

Check that a `VolumeMount` named `apigee-external-secrets` exists:
           
           kubectl -n $APIGEE_NAMESPACE get deployment apigee-controller-manager -o jsonpath='{.spec.template.spec.containers[?(@.name=="manager")].volumeMounts[?(@.name=="apigee-external-secrets")]}'

Example output:
           
           {
             "mountPath": "/opt/apigee/externalsecrets",
             "name": "**apigee-external-secrets** ",
             "readOnly": true
           }

Check that `Environment Variable`s exist that reference external secrets:
           
           kubectl -n $APIGEE_NAMESPACE get deployment apigee-controller-manager -o jsonpath='{.spec.template.spec.containers[?(@.name=="manager")].env}'

Example output:
           
           [
             ...
             {
               "name": "CASSANDRA_JOLOKIA_USERNAME_PATH",
               "value": "/opt/apigee/**externalsecrets** /jolokiaUsername"
             },
             {
               "name": "CASSANDRA_JOLOKIA_PASSWORD_PATH",
               "value": "/opt/apigee/**externalsecrets** /jolokiaPassword"
             }
           ]




## Rollback to K8s Secret

  1. To revert back to non-external secrets, remove the `secretProviderClass` configuration in `overrides.yaml` and use the previous configuration: 
         
         cassandra:
               auth:
                 secretProviderClass: apigee-cassandra-auth-spc # remove this line

  2. Use `helm upgrade` to apply the change to the `apigee-operator` and `apigee-datastore` components: 
         
         helm upgrade operator apigee-operator/ \
           --namespace $APIGEE_NAMESPACE \
           --atomic \
           -f overrides.yaml
         
         helm upgrade datastore apigee-datastore/ \
           --namespace $APIGEE_NAMESPACE \
           --atomic \
           -f overrides.yaml




##  Troubleshooting: Create a client container for debugging 

If you are using Vault, this section replaces instructions in the troubleshooting section, [Create a client container for debugging](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/cassandra/ts-cassandra#create-a-client-container-for-debugging). 

This section explains how to create a client container from which you can access [Cassandra debugging utilities](https://cassandra.apache.org/doc/latest/tools/cqlsh.html) such as `cqlsh`. These utilities allow you to query Cassandra tables and can be useful for debugging purposes.

###  Create the client container 

To create the client container, follow these steps: 

  1. The container uses the TLS certificate from the `apigee-cassandra-user-setup` pod. The first step is to fetch this certificate name: 
         
         kubectl get secrets -n APIGEE_NAMESPACE --field-selector type=kubernetes.io/tls | grep apigee-cassandra-user-setup | awk '{print $1}'

This command returns the certificate name. For example: `apigee-cassandra-user-setup-rg-hybrid-b7d3b9c-tls`. 

  2. Open a new file and paste the following pod spec into it: 
         
         apiVersion: v1
           kind: Pod
           metadata:
             labels:
             name: CASSANDRA_CLIENT_NAME   # For example: my-cassandra-client
             namespace: $APIGEE_NAMESPACE
           spec:
             containers:
             - name: CASSANDRA_CLIENT_NAME
               image: "gcr.io/apigee-release/hybrid/apigee-hybrid-cassandra-client:1.13.4"
               imagePullPolicy: Always
               command:
               - sleep
               - "3600"
               env:
               - name: CASSANDRA_SEEDS
                 value: apigee-cassandra-default.apigee.svc.cluster.local
               - name: APIGEE_DML_USERNAME_PATH
                 value: /opt/apigee/externalsecrets/dmlUsername
               - name: APIGEE_DML_PASSWORD_PATH
                 value: /opt/apigee/externalsecrets/dmlPassword
               volumeMounts:
               - mountPath: /opt/apigee/ssl
                 name: tls-volume
                 readOnly: true
               - name: apigee-external-secrets
                 mountPath: /opt/apigee/externalsecrets
                 readOnly: true
             volumes:
             - name: tls-volume
               secret:
                 defaultMode: 420
                 secretName: apigee-cassandra-user-setup-vaibhavhybridor-8b3e61d-tls
             - name: apigee-external-secrets
               csi:
                 driver: secrets-store.csi.k8s.io
                 readOnly: true
                 volumeAttributes:
                   secretProviderClass: apigee-cass-password
             serviceAccount: apigee-cassandra-default
             serviceAccountName: apigee-cassandra-default
             restartPolicy: Never

  3. Save the file with a `.yaml` extension. For example: `my-spec.yaml`.
  4. Apply the spec to your cluster: 
         
         kubectl apply -f my-spec.yaml -n $APIGEE_NAMESPACE

  5. Log in to the container: 
         
         kubectl exec -n CASSANDRA_CLIENT_NAME -it -- bash

  6. Connect to the Cassandra `cqlsh` interface with the following commands. Enter the commands exactly as shown: 
         
         APIGEE_DML_USER=$(cat "$APIGEE_DML_USERNAME_PATH")
         export APIGEE_DML_USER
         APIGEE_DML_PASSWORD=$(cat "$APIGEE_DML_PASSNAME_PATH")
         export APIGEE_DML_PASSWORD
         cqlsh ${CASSANDRA_SEEDS} -u ${APIGEE_DML_USER} -p ${APIGEE_DML_PASSWORD} --ssl




###  Deleting the client pod 

Use this command to delete the Cassandra client pod: 
    
    
    kubectl delete pods -n $APIGEE_NAMESPACE cassandra-client

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
