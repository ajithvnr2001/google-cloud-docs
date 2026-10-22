---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/iam/service-identity/
title: Authenticate with service accounts \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:16:16.645801+00:00
---

# Authenticate with service accounts  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/iam/service-identity/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)



Send feedback 

#  Authenticate with service accounts Stay organized with collections  Save and categorize content based on your preferences. 

Service accounts are the accounts that workloads or services use to programmatically consume resources and access microservices securely. They are a special kind of identity used by an application or workload rather than by a person. Similar to a user account, service accounts can be granted permissions and roles but they can't sign in like a human user.

Service accounts are useful for managing Google Distributed Cloud (GDC) air-gapped appliance infrastructure, such as:

  * Internal GDC air-gapped appliance services and workloads to securely access GDC air-gapped appliance control plane application programming interface (API).
  * Customer workloads in GDC air-gapped appliance to access GDC air-gapped appliance services and make authorized application programming interface (API) calls.
  * External workloads to federate with GDC air-gapped appliance.
  * GDC air-gapped appliance services or system controllers to securely access customer resources. For example, service accounts can manage authentication and authorization workflows where the service controllers running in the bare metal Kubernetes cluster must run workloads managed by customers.



Managing service identities involves both the service identity (represented by a `ProjectServiceAccount` resource) and its associated credentials (public and private key pairs). You can manage accounts by using the GDC console, the gdcloud CLI, or the API. With the gdcloud CLI, the service identity feature is built upon the `ProjectServiceAccount` API.

## Before you begin

To complete the tasks in this document, you must have a project. To learn how to create a project, see [Create a project](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/create-a-project).

You must also have the necessary permissions and prepare your environment.

### Request IAM roles

To create, update, and delete service identities within a project, contact your Organization IAM Admin or Project IAM Admin to request the **Project IAM Admin** (`project-iam-admin`) role.

The Organization IAM Admin can grant this role for any project within the organization. The Project IAM Admin can grant this role within the scope of their specific project.

### Prepare your environment

To use the command-line tools to manage service identities, complete the following setup:

  * [Download](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/resources/gdcloud-download) and [install](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/resources/gdcloud-install) the gdcloud CLI, if you haven't already done so.

  * To use the API with `kubectl`, additional setup is required:

    * Install the `kubectl` CLI, as described in [Install components](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/resources/gdcloud-install#install-components).
    * [Generate the kubeconfig file for the management API server](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/iam/sign-in#management-api-kubeconfig) to configure `kubectl` access.



## Create a service identity

Users with access to service accounts can access all service accounts within a project.

To create service identities in a project, use the GDC console, the gdcloud CLI, or the API.

### Console

  1. Sign in to the GDC console.
  2. In the navigation menu, select **Identity & Access > Service identities**.
  3. Click **add Create Service Identity**. The **Service Identity details** page opens.
  4. In the **Service identity name** field, enter a name for your service identity. For example: `Test service identity`.
  5. Click **Create**.



### gdcloud

Create a service identity:
    
    
    gdcloud iam service-accounts create NAME \
            --project=PROJECT
    

Replace the following values:

  * NAME: the name of the `ProjectServiceAccount`. The name must be unique within the project namespace.
  * PROJECT: the project to create the service identity in. If `gdcloud init` is already set, omit the `--project` flag.



This command creates a `ProjectServiceAccount` in the project namespace.

###  API 

  1. Create a `ProjectServiceAccount` custom resource YAML file, such as `my-project-sa.yaml`:
         
         apiVersion: resourcemanager.gdc.goog/v1
         kind: ProjectServiceAccount
         metadata:
           name: NAME
           namespace: PROJECT
         spec:
           keys:
           - algorithm: ALGORITHM
             id: KEY_ID
             key: BASE64_ENCODED_KEY
             validAfter: "START_TIME"
             validBefore: "EXPIRATION_TIME"
         

Replace the following variables:

     * `NAME`: the name of the `ProjectServiceAccount` resource. The name must be unique within the project namespace.
     * `PROJECT`: the project to create the service identity in.
     * `ALGORITHM`: the algorithm of the key. Only ES256 keys are supported.
     * `KEY_ID`: the unique identifier of the key. The ID is used to determine which key to verify against.
     * `BASE64_ENCODED_KEY`: the base64-encoded public key in PEM format to verify against. The private key used to generate this public key is expected in ECDSA P256 PEM format.
     * `START_TIME`: the start time when the key becomes valid, such as `2025-02-07T00:59:34Z`.
     * `EXPIRATION_TIME`: the expiration time for the key, such as `2026-02-07T00:59:34Z`.
  2. Apply the `ProjectServiceAccount` custom resource to the management API server:
         
         kubectl --kubeconfig MANAGEMENT_API_SERVER_KUBECONFIG apply -f my-project-sa.yaml
         

Replace the `MANAGEMENT_API_SERVER_KUBECONFIG` variable with the path to the kubeconfig file for the management API server.




### View service identities

To view a list of service accounts in a project, use the GDC console or the gdcloud CLI.

### Console

  1. Sign in to the GDC console.
  2. Select a project.
  3. In the navigation menu, click **Identity & Access > Service Identities** to view the list of service accounts for the project.



### gdcloud

List the service accounts in a project:
    
    
    gdcloud iam service-accounts list \
        --project=PROJECT
    

### Assign a role binding to the service identity

Use either the GDC console or the gdcloud CLI to assign a role binding.

### Console

  1. Sign in to the GDC console.
  2. Select a project.
  3. In the navigation menu, select **Identity & Access > Access**.
  4. In the **Member** list, click **add Add member**. You see the **Users and roles** page.
  5. Select **Service identity** in the **Member type** list.
  6. In the **Service identity** list, select the service identity you want to assign a role binding.
  7. In the **Role** list, select the role that you want to assign to the service identity, such as **Backup Creator**.
  8. Optional: To add another role, click **add Add another role**. Select the additional role.
  9. Click **Add**.



### gdcloud

This command creates and names the project role binding to bind the specified role with the `ProjectServiceAccount`:
    
    
    gdcloud iam service-accounts add-iam-policy-binding \
        --project=PROJECT \
        --role=ROLE \
        --iam-account=NAME
    

Replace the following values:

  * PROJECT: the project to create the role binding in. If `gdcloud init` is already set, then you can omit the `--project` flag.
  * ROLE: the predefined role to assign to the `ProjectServiceAccount`. Specify roles in the format `Role/name` where _Role_ is the Kubernetes type, such as `Role`or `ProjectRole`, and _name_ is the name of the predefined role. For example, to assign the Project Viewer role, set the role to `Role/project-viewer`.
  * NAME: the name of the service identity to use.



### Delete a service identity

**Important:** When you delete a service account, its associated role bindings are not automatically removed. If you create a new service account with the same name, it automatically inherits the permissions from the previously deleted service account. To avoid orphaned permissions that can linger from a deleted service account, [remove any existing role bindings](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/iam/set-up-role-bindings#remove-role-bindings) associated with the service account before deleting the service account itself.

To delete service accounts in a project, use theGDC console or the gdcloud CLI.

After you delete a service identity, applications don't have access to project resources through that service identity.

### Console

  1. Sign in to the GDC console.
  2. In the navigation menu, select **Identity & Access > Service Identities**.
  3. Select the checkbox of the service identity that you want to delete.
  4. Click **Delete**.
  5. The confirmation dialog appears. In the **Confirm by typing the following below** field, enter `remove`.
  6. Click **Delete**.



### gdcloud

Run the following command to delete a service identity:
    
    
    gdcloud iam service-accounts delete NAME \
        --project=PROJECT
    

## Create and add key pairs

To create and add key pairs in a project, use the GDC console, the gdcloud CLI, or the API.

### Console

  1. Sign in to the GDC console.
  2. In the navigation menu, select **Identity & Access > Service Identities**.
  3. Click the name of the service identity you want to add in the key.
  4. Click **add Create New Key**.
  5. The new key appears in the **Keys** list, and a dialog confirms you've created the key successfully.



### gdcloud

The `gdcloud` command creates the application default credentials JSON file and the public and private key pairs:
    
    
    gdcloud iam service-accounts keys create APPLICATION_DEFAULT_CREDENTIALS_FILENAME \
        --project=PROJECT \
        --iam-account=NAME \
        --ca-cert-path=CA_CERTIFICATE_PATH
    

Replace the following values:

  * APPLICATION_DEFAULT_CREDENTIALS_FILENAME: the name of the JSON file.
  * PROJECT : selects the project to create the key for. If `gdcloud init` is already set, then you can omit the `--project` flag.
  * NAME: the name of the service identity to add the key for.
  * CA_CERTIFICATE_PATH: Optional: the certificate authority (CA) certificate path to verify the authentication endpoint. If you do not specify this path, the system CA certificates are used. You must install the CA in the system CA certificates.



GDC air-gapped appliance adds the public key to the `ProjectServiceAccount` keys you use to verify the JSON web tokens (JWT) the private key signs. The private key writes to the application default credentials JSON file.

The following example shows the application default credentials JSON file:
    
    
    {
    "type": "gdch_service_account",
    "format_version": "1",
    "project": "project_name",
    "private_key_id": "abcdef1234567890",
    "private_key": "-----BEGIN PRIVATE KEY-----\nETC\n-----END PRIVATE KEY-----\n",
    "name": "service_identity_name",
    "ca_cert_path": "service_identity_name",
    "token_uri": "https://service-identity.<Domain>/authenticate"
    }
    

This example uses the following values:

  * `project`: the project namespace in the organization.
  * `private_key_id`: the ID assigned to the key.
  * `private_key`: the ECDSA P256 private key in PEM format that the CLI generates.
  * `name`: the name of the service identity.
  * `token_uri`: the address of the authentication endpoint.



###  API 

  1. Generate the public and private key pair. The following commands use `openssl` as an example, which is a common tool for this purpose.
         
         openssl ecparam -name prime256v1 -genkey -noout -out "key.pem"
         openssl ec -in "key.pem" -pubout > "pub.pem"
         

  2. Base64 encode the public key and retrieve its key ID:
         
         KEY_ID=$(openssl pkey -in key.pem -pubout -outform der | openssl dgst -sha256 | sed 's/^.* //')
         BASE64_ENCODED_KEY=$(cat pub.pem | base64)
         

  3. Create or update the `ProjectServiceAccount` custom resource YAML file, including the generated key information from the previous step:
         
         apiVersion: resourcemanager.gdc.goog/v1
         kind: ProjectServiceAccount
         metadata:
           name: NAME
           namespace: PROJECT
         spec:
           keys:
           - algorithm: ALGORITHM
             id: KEY_ID
             key: BASE64_ENCODED_KEY
             validAfter: "START_TIME"
             validBefore: "EXPIRATION_TIME"
         

Replace the following variables:

     * `NAME`: the name of the `ProjectServiceAccount` resource. The name must be unique within the project namespace.
     * `PROJECT`: the project in which you're creating the key.
     * `ALGORITHM`: the algorithm of the key. Only ES256 keys are supported.
     * `KEY_ID`: the unique identifier of the key. The ID is used to determine which key to verify against.
     * `BASE64_ENCODED_KEY`: the base64-encoded public key in PEM format to verify against. The private key used to generate this public key is expected in ECDSA P256 PEM format.
     * `START_TIME`: the start time when the key becomes valid, such as `2025-02-07T00:59:34Z`.
     * `EXPIRATION_TIME`: the expiration time for the key, such as `2026-02-07T00:59:34Z`.
  4. Apply the `ProjectServiceAccount` custom resource to the management API server:
         
         kubectl --kubeconfig MANAGEMENT_API_SERVER_KUBECONFIG apply -f my-project-sa.yaml
         

Replace the `MANAGEMENT_API_SERVER_KUBECONFIG` variable with the path to the kubeconfig file for the management API server.

  5. Create the application default credentials JSON file containing the private key. Make sure that the `KEY_ID` variable in the JSON file is set to the same value as the `KEY_ID` variable you used in the `ProjectServiceAccount` spec.
         
         cat <<EOF > "key_file.json"
         {
           "format_version": "1",
           "name": "NAME",
           "private_key": "$(tr '\n' '\t' < "key.pem" | sed 's/\t/\\n/g')",
           "private_key_id": "KEY_ID",
           "project": "PROJECT",
           "token_uri": "AUTH_URL",
           "type": "gdch_service_account"
         }
         EOF
         

Replace the following variables:

     * `NAME`: the name of the service identity.
     * `KEY_ID`: the unique identifier of the key. The ID is used to determine which key to verify against, and it must match the `KEY_ID` value used in the `ProjectServiceAccount` spec.
     * `PROJECT`: the project namespace in the organization.
     * `AUTH_URL`: the address of the authentication endpoint.
  6. Add the key pair to your project by activating the service account:
         
         gdcloud auth activate-service-account –-key-file=key_file.json
         




### List credentials for service accounts

List the public keys from a specific `ProjectServiceAccount` in the project:
    
    
    gdcloud iam service-accounts keys list \
        --project=PROJECT \
        --iam-account=NAME
    

### Delete credentials

To delete the public key, use the GDC console or the gdcloud CLI.

**Note:** Deleting the key does not revoke the short-lived credentials that are issued by using the key.

### Console

  1. Sign in to the GDC console.
  2. In the navigation menu, select **Identity & Access > Service Identities**.
  3. Click the name of the service identity that has the key you want to delete.
  4. Click **delete Delete**.
  5. In the confirmation dialog, click **Delete**.



### gdcloud

Remove the public key with the key ID from the specific `ProjectServiceAccount` in the project:
    
    
    gdcloud iam service-accounts keys delete KEY_ID \
        --project=PROJECT \
        --iam-account=NAME
    

## Authorize a service account using a service account key

**Note:** Service account keys are a security risk if not managed carefully. See [Secure service account keys](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/iam/secure-service-account-keys) for information about best practices for managing, using, and securing service account keys.

You can use the `gdcloud` command to activate a service account using a service account key:

  1. [Create a service account key file](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/iam/service-identity#gdcloud_4), if you don't already have one.

  2. Activate the service account by running the following command:
         
         gdcloud auth activate-service-account --key-file=KEY_FILE
         

Replace KEY_FILE with the path to the service account key file.

After activating the service account, `gdcloud` uses the service account's credentials for subsequent commands, instead of your user credentials.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
