---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/iam/service-identities/
title: Manage service accounts \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T01:17:55.265121+00:00
---

# Manage service accounts  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/iam/service-identities/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Manage service accounts Stay organized with collections  Save and categorize content based on your preferences. 

A service identity in Google Distributed Cloud (GDC) air-gapped provides a dedicated identity for workloads or services to programmatically access resources and microservices securely. These are special identities used by applications or workloads, rather than by a person, and cannot be used for human sign in. Similar to user accounts, you grant permissions and roles to a service identity to define what it is authorized to access.

You might notice two terms used for this concept. The GDC console primarily uses the term service identity, while `gdcloud` commands and API interactions often use service account. The latter reflects the name of the underlying Kubernetes custom resource, `ProjectServiceAccount`. Both terms refer to the same thing: the non-human identity for your workloads. This document uses service identity as the primary term.

Service identities are useful for managing GDC infrastructure, such as:

  * Internal Distributed Cloud services and workloads to securely access Distributed Cloud control plane application programming interface (API). For example, Database Services interacting with the Kubernetes APIs to create and delete databases.
  * Customer workloads in Distributed Cloud to access Distributed Cloud services and make authorized application programming interface (API) calls. For example, service identities can manage a customer using a Vertex AI Workbench notebook to transcribe audio files using the Speech-to-Text API.
  * External workloads to federate with Distributed Cloud. For example, service identities can manage an application external to Distributed Cloud that digitizes documents but wants to use the Optical Character Recognition (OCR) API to replace their current OCR engine.
  * Distributed Cloud services or system controllers to securely access customer resources or user clusters. For example, service identities can manage authentication and authorization workflows where the service controllers running in admin clusters need to run workloads within the user clusters that are managed by customers.



Managing service identities involves both the service identity (represented by a `ProjectServiceAccount` resource) and its associated credentials (public and private key pairs). You can manage accounts for service identities by using the GDC console, the gdcloud CLI, or the API. With the gdcloud CLI, the service identity feature is built upon the global `ProjectServiceAccount` API. Because `ProjectServiceAccount` resources are configured globally, they operate across all zones in your gdcloud universe.

## Before you begin

To complete the tasks in this document, you must have a project. To learn how to create a project, see [Create a project](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/create-a-project).

You must also have the necessary permissions and prepare your environment.

### Request IAM roles

To create, update, and delete service identities within a project, contact your Organization IAM Admin or Project IAM Admin to request the **Project IAM Admin** (`project-iam-admin`) role.

The Organization IAM Admin can grant this role for any project within the organization. The Project IAM Admin can grant this role within the scope of their specific project.

### Prepare your environment

To use the command-line tools to manage service identities, complete the following setup:

  * [Download](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-download) and [install](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-install) the gdcloud CLI, if you haven't already done so.

  * To use the API with `kubectl`, additional setup is required:

    * [Install the kubectl CLI](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/get-started/kubectl).
    * [Generate the kubeconfig file for the global API server](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/iam/sign-in#global-resources-kubeconfig) to configure `kubectl` access.



## Create a service identity

Creating a service identity includes creating an account and its associated credentials.

### Create an account

To create an account for a service identity, use the GDC console, the gdcloud CLI, or the API to create a `ProjectServiceAccount` resource in a project.

### Console

  1. Sign in to the GDC console.
  2. In the navigation menu, select **Identity & Access > Service identities**.
  3. Click **add Create Service Identity**. The **Service Identity details** page opens.
  4. In the **Service identity name** field, enter a name for your service identity. For example: `testserviceidentity`.
  5. Click **Create**.



###  gdcloud 

Create an account:
    
    
    gdcloud iam service-accounts create NAME \
        --project=PROJECT
    

Replace the following values:

  * NAME: the name of the `ProjectServiceAccount`. The name must be unique within the project namespace.
  * PROJECT: the project to create the service identity in. If `gdcloud init` is already set, omit the `--project` flag.



This command creates a `ProjectServiceAccount` in the project namespace on the Management API server.

###  API 

  1. Create a `ProjectServiceAccount` custom resource YAML file, such as `my-project-sa.yaml`:
         
         apiVersion: resourcemanager.global.gdc.goog/v1
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
  2. Apply the `ProjectServiceAccount` custom resource to the global API server:
         
         kubectl --kubeconfig GLOBAL_API_SERVER_KUBECONFIG apply -f my-project-sa.yaml
         

Replace the `GLOBAL_API_SERVER_KUBECONFIG` variable with the path to the kubeconfig file for the global API server.




### Create credentials

To enable a workload or application to authenticate as the service identity (represented by the account you created), you need to generate credentials. Creating credentials involves generating a cryptographic private and public key pair, and associating the public key with the service identity.

To create credentials for a service identity, use the GDC console, the gdcloud CLI, or the API.

### Console

  1. Sign in to the GDC console.
  2. In the navigation menu, select **Identity & Access > Service Identities**.
  3. Click the name of the service identity you want to add in the key.
  4. Click **add Create New Key**.
  5. The new key appears in the **Keys** list, and a dialog confirms you've created the key successfully.



###  gdcloud 

The `gdcloud` command creates an application default credentials JSON file and a public and private key pair:
    
    
    gdcloud iam service-accounts keys create APPLICATION_DEFAULT_CREDENTIALS_FILENAME \
        --project=PROJECT \
        --iam-account=NAME \
        --ca-cert-path=CA_CERTIFICATE_PATH
    

Replace the following values:

  * APPLICATION_DEFAULT_CREDENTIALS_FILENAME: the name of the JSON file.
  * PROJECT : selects the project to create the key for. If `gdcloud init` is already set, then you can omit the `--project` flag.
  * NAME: the name of the service identity to add the key for.
  * CA_CERTIFICATE_PATH: Optional: the certificate authority (CA) certificate path to verify the authentication endpoint. If you do not specify this path, the system CA certificates are used. You must install the CA in the system CA certificates.



Distributed Cloud adds the public key to the `ProjectServiceAccount` keys you use to verify the JSON web tokens (JWT) the private key signs. The private key is written to the application default credentials JSON file.

The following example shows the application default credentials JSON file:
    
    
    {
    "type": "gdch_service_account",
    "format_version": "1",
    "project": "project_name",
    "private_key_id": "abcdef1234567890",
    "private_key": "-----BEGIN PRIVATE KEY-----\nETC\n-----END PRIVATE KEY-----\n",
    "name": "service_identity_name",
    "ca_cert_path": "/path/to/ca.crt",
    "token_uri": "https://service-identity.<Domain>/authenticate"
    }
    

This example uses the following values:

  * `project`: the project namespace in the organization.
  * `private_key_id`: the ID assigned to the key.
  * `private_key`: the ECDSA P256 private key in PEM format that the CLI generates.
  * `name`: the name of the service identity.
  * `ca_cert_path`: the path to the certificate authority (CA) certificate that is used to verify the authentication endpoint.
  * `token_uri`: the address of the authentication endpoint.



###  API 

  1. Generate the public and private key pair. The following commands use `openssl` as an example, which is a common tool for this purpose.
         
         openssl ecparam -name prime256v1 -genkey -noout -out "key.pem"
         openssl ec -in "key.pem" -pubout > "pub.pem"
         

  2. Base64 encode the public key and retrieve its key ID:
         
         KEY_ID=$(openssl pkey -in key.pem -pubout -outform der | openssl dgst -sha256 | sed 's/^.* //')
         BASE64_ENCODED_KEY=$(cat pub.pem | base64)
         

  3. Create or update the `ProjectServiceAccount` custom resource YAML file, including the generated key information from the previous step:
         
         apiVersion: resourcemanager.global.gdc.goog/v1
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
  4. Apply the `ProjectServiceAccount` custom resource to the global API server:
         
         kubectl --kubeconfig GLOBAL_API_SERVER_KUBECONFIG apply -f my-project-sa.yaml
         

Replace the `GLOBAL_API_SERVER_KUBECONFIG` variable with the path to the kubeconfig file for the global API server.

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



For details on how to use the generated key file to authenticate as this service identity, see Authenticate and use a service identity. This section covers using the key with the gdcloud CLI and programmatically with client libraries.

## View service identities

This section describes how to view your service identities and their associated public keys.

### View a list of service identities

To view a list of service identities within a project, use the GDC console or the gdcloud CLI.

### Console

  1. Sign in to the GDC console.
  2. Select a project.
  3. In the navigation menu, click **Identity & Access > Service Identities** to view the list of service identities for the project.



###  gdcloud 

List the service identity accounts in a project:
    
    
    gdcloud iam service-accounts list \
        --project=PROJECT
    

Replace `PROJECT` with the project ID.

### View a list of public keys for a service identity

List the public keys registered with a service identity account in the project:
    
    
    gdcloud iam service-accounts keys list \
        --project=PROJECT \
        --iam-account=NAME
    

Replace the following:

  * PROJECT: the project ID.
  * NAME: the name of the service identity account to use.



## Grant permissions for service identities

To grant permissions to a service identity, assign it one or more roles by creating role bindings using the GDC console or the gdcloud CLI.

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



###  gdcloud 

You can bind the service identity account to roles within the project namespace or to roles in a different namespace.

**Note:** the `--project` and `--role-namespace` flags are mutually exclusive, meaning you can only use one or the other in a single command, not both.

  * Bind the account to a role within the project namespace:
        
        gdcloud iam service-accounts add-iam-policy-binding \
            --project=PROJECT \
            --role=ROLE \
            --iam-account=NAME
        

Replace the following:

    * PROJECT: the project to create the role binding in. If `gdcloud init` is already set, then you can omit the `--project` flag.
    * ROLE: the predefined role to assign to the account. Specify roles in the format `Role/name` where _Role_ is the Kubernetes type `IAMRole`, and _name_ is the name of the predefined role. For example, to assign the Project Viewer role, set the role to `IAMRole/project-viewer`.
    * NAME: the name of the service identity account to use.
  * Bind the account to a role within a different namespace:
        
        gdcloud iam service-accounts add-iam-policy-binding \
            --role=ROLE \
            --role-namespace=ROLE_NAMESPACE \
            --iam-account=NAME
        

Replace the following:

    * ROLE: the predefined role to assign to the account. Specify roles in the format `Role/name` where _Role_ is the Kubernetes type `IAMRole`, and _name_ is the name of the predefined role. For example, to assign the Project Viewer role, set the role to `IAMRole/project-viewer`.
    * ROLE_NAMESPACE: the namespace of the role to bind with the account other than the project namespace.
    * NAME: the name of the service identity account to use.



## Authenticate and use a service identity

After you create a service identity and generate its key file, you can use the key file to authenticate to GDC services and clusters. Authentication lets you obtain short-lived access tokens for API calls or configure cluster access.

There are two ways to authenticate with a service identity:

  * Authenticate with the gdcloud CLI
  * Authenticate programmatically with client libraries



### Authenticate with the gdcloud CLI

To perform actions with the service identity, you must first activate its key file. After activation, you can use the gdcloud CLI to obtain tokens or generate kubeconfig files.

#### Authorize a service identity using a key

**Note:** Service identity keys are a security risk if not managed carefully. See [Secure service account keys](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/iam/secure-service-account-keys) for information about best practices for managing, using, and securing service identity keys.

The `gdcloud auth activate-service-account` command authenticates the gdcloud CLI with a service identity. This lets you perform actions on Distributed Cloud resources using the service identity account permissions instead of a user account.

Authorize a service identity using a key:

  1. Create a credential key file, if you don't already have one.

  2. Activate the service identity by running the following command:
         
         gdcloud auth activate-service-account --key-file=KEY_FILE
         

Replace KEY_FILE with the path to the credential key file, typically in JSON format.

After successful activation, `gdcloud` uses the service identity's credentials instead of your user credentials.




#### Obtain an access token using the gdcloud CLI

After authorizing a service identity, you can use `gdcloud` to print an access token. You can use this token as a bearer token to authenticate HTTP requests. The token grants access to services as defined in the `AUDIENCES` parameter.

Print an identity token for the specified service identity account:
    
    
    gdcloud auth print-identity-token --audiences=AUDIENCES
    

Replace `AUDIENCES` with the intended recipient or service the token is for. Only one audience can be specified.

#### Generate the kubeconfig file

After authorizing a service identity, you can generate a kubeconfig file to authenticate to Kubernetes clusters.

  1. [Set](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-reference/gdcloud-config-set) the gdcloud `core/organization_console_url` property:
         
         gdcloud config set core/organization_console_url
         https://GDC_URL
         

Replace `GDC_URL` with your organization's URL.

  2. Generate the kubeconfig file to access a cluster using the active service identity:

     * **For a zonal cluster:**
           
           export KUBECONFIG=KUBECONFIG_PATH
           gdcloud clusters get-credentials CLUSTER_NAME --zone ZONE
           

Replace the following:

       * KUBECONFIG_PATH: the path where you want to save the generated kubeconfig file.
       * CLUSTER_NAME: the name of the zonal cluster.

**Note:** The list of cluster names is available in the login config URL:   
`https://GDC_URL/.well-known/login-config`.
       * ZONE: the name of the zone where the cluster is located.

     * **For the global API server:**
           
           export KUBECONFIG=KUBECONFIG_PATH
           gdcloud clusters get-credentials global-api
           

Replace `KUBECONFIG_PATH` with the path where you want to save the generated kubeconfig file.




A kubeconfig file is generated, configured to authenticate as the service identity. The following shows an example YAML file:
    
    
    apiVersion: v1
    clusters:
    - cluster:
        certificate-authority-data: <REDACTED>
        server: <REDACTED>
      name: cluster-name
    contexts:
    - context:
        cluster: cluster-name
        user: gdch_console-<REDACTED>_cluster-name
      name: cluster-name-gdch_console-<REDACTED>_cluster-name
    current-context: cluster-name-gdch_console-gdc1-staging-gpcdemolabs-com_cluster-name
    kind: Config
    preferences: {}
    users:
    - name: gdch_console-<REDACTED>_cluster-name
      user:
        exec:
          apiVersion: client.authentication.k8s.io/v1
          args:
          - --audience=<REDACTED>
          command: gdcloud-k8s-auth-plugin
          env: null
          installHint: Run 'gdcloud components install gdcloud-k8s-auth-plugin' to use
            plugin
          interactiveMode: Never
          provideClusterInfo: false
    

### Authenticate programmatically with client libraries

The following examples show how to programmatically authenticate to GDC APIs using the standard [Google Cloud Client Libraries](https://docs.cloud.google.com/apis/docs/cloud-client-libraries). These libraries use the generated service account key file to either generate a Security Token Service (STS) access token or configure a service client with the service identity's credentials. This method doesn't require any prior `gdcloud` authorization.

###  Python 
    
    
    import google.auth
    from google.auth.transport import requests
    import requests as reqs
    
    api_endpoint = "https://console.org-1.zone1.google.gdch.test"
    
    # Load the GDC credentials (via GOOGLE_APPLICATION_CREDENTIALS or default path)
    creds, project_id = google.auth.default()
    
    # Apply the required audience for the GDC Management API
    creds = creds.with_gdch_audience(api_endpoint)
    
    def fetch_gdch_token():
        sesh = reqs.Session()
        # Note: Set verify to False only if bypassing self-signed cert verification.
        # Otherwise, rely on the "ca_cert_path" present in your gdch_credentials.json
        sesh.verify = False
        req = requests.Request(session=sesh)
    
        # Refresh the credentials to fetch the STS access token
        creds.refresh(req)
    
        print("Access Token:", creds.token)
    
    fetch_gdch_token()
    

###  Java 
    
    
    import com.google.auth.oauth2.[GdchCredentials](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.GdchCredentials.html);
    import com.google.auth.oauth2.[GoogleCredentials](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.GoogleCredentials.html);
    
    import java.io.FileInputStream;
    import java.io.InputStream;
    
    public class GdchAuthExample {
        public static void main(String[] args) throws Exception {
            // Path to your service account JSON file
            String credentialsPath = "/path/to/gdch/credentials.json";
            String apiAudience = "https://console.org-1.zone1.google.gdch.test";
    
            try (InputStream credentialsStream = new FileInputStream(credentialsPath)) {
                // Load the generic Google credentials from the stream
                [GoogleCredentials](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.GoogleCredentials.html) credentials = [GoogleCredentials](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.GoogleCredentials.html).fromStream(credentialsStream);
    
                // Verify it loaded as GdchCredentials
                if (credentials instanceof [GdchCredentials](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.GdchCredentials.html)) {
                    // Cast and attach the targeted GDC audience
                    [GdchCredentials](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.GdchCredentials.html) gdch = (([GdchCredentials](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.GdchCredentials.html)) credentials).[createWithGdchAudience](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.GdchCredentials.html#com_google_auth_oauth2_GdchCredentials_createWithGdchAudience_java_lang_String_)(apiAudience);
    
                    // Force negotiation with the GDC Auth Server to fetch the token
                    gdch.[refreshIfExpired](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.OAuth2Credentials.html#com_google_auth_oauth2_OAuth2Credentials_refreshIfExpired__)();
    
                    System.out.println("Access Token: " + gdch.getAccessToken().getTokenValue());
                } else {
                    System.err.println("The provided file is not a valid GdchCredentials format.");
                }
            }
        }
    }
    

###  Go 
    
    
    package main
    
    import (
      "context"
      "fmt"
      "log"
    
      "cloud.google.com/go/auth/credentials"
    )
    
    func main() {
      ctx := context.Background()
      apiEndpoint := "https://console.org-1.zone1.google.gdch.test"
    
      // Load default credentials. The STSAudience parameter is specifically
      // required for the GDC auth flow to correctly negotiate the token.
      creds, err := credentials.[DetectDefault](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/auth/latest/credentials.html#cloud_google_com_go_auth_credentials_DetectDefault)(&credentials.[DetectOptions](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/auth/latest/credentials.html#cloud_google_com_go_auth_credentials_DetectOptions){
        STSAudience: apiEndpoint,
      })
      if err != nil {
        log.Fatalf("Failed to detect credentials: %v", err)
      }
    
      // Fetch an access token
      token, err := creds.Token(ctx)
      if err != nil {
        log.Fatalf("Failed to retrieve token: %v", err)
      }
    
      fmt.Printf("Access Token: %s\n", token.Value)
    }
    

###  C++ 
    
    
    [](std::string const& keyfile, std::string const& audience) {
      auto is = std::ifstream(keyfile);
      is.exceptions(std::ios::badbit);  // Minimal error handling in examples
      auto contents = std::string(std::istreambuf_iterator<char>(is.rdbuf()), {});
      auto options =
          google::cloud::Options{}.set<google::cloud::UnifiedCredentialsOption>(
              google::cloud::MakeGDCHServiceAccountCredentials(contents, audience));
      return google::cloud::speech_v1::AdaptationClient(
          google::cloud::speech_v1::MakeAdaptationConnection(options));
    }
    

## Delete a service identity

**Important:** When you delete a service identity, its associated role bindings are not automatically removed. If you create a new service identity with the same name, it automatically inherits the permissions from the previously deleted service identity. To avoid orphaned permissions that can linger from a deleted service identity, first [remove any existing role bindings](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/iam/set-up-role-bindings#remove-role-bindings) associated with the service identity before deleting the service identity itself.

After you delete a service identity, the `ProjectServiceAccount` and its associated public keys are deleted, existing private keys become invalid, and applications no longer have access to project resources through that service identity.

To delete a service identity, use the GDC console or the gdcloud CLI.

### Console

  1. Sign in to the GDC console.
  2. In the navigation menu, select **Identity & Access > Service Identities**.
  3. Select the checkbox of the service identity you want to delete.
  4. Click **Delete**.
  5. The confirmation dialog appears. In the **Confirm by typing the following below** field, enter `remove`.
  6. Click **Delete**.



###  gdcloud 

Run the following command to delete a service identity account:
    
    
    gdcloud iam service-accounts delete NAME \
        --project=PROJECT
    

Replace the following:

  * NAME: the name of the service identity account to delete.
  * PROJECT: the project ID.



## Delete credentials

If you want to disable a specific key pair without deleting the entire service identity account, you can delete its public key from the service identity's account. This action makes the corresponding private key invalid.

**Note:** Deleting the public key does not revoke the short-lived credentials that are issued by using the corresponding private key.

To delete the public key, use the GDC console or the gdcloud CLI.

### Console

  1. Sign in to the GDC console.
  2. In the navigation menu, select **Identity & Access > Service Identities**.
  3. Click the name of the service identity that has the key you want to delete.
  4. Click **delete Delete**.
  5. In the confirmation dialog, click **Delete**.



###  gdcloud 

Remove the public key with the key ID from a service identity account in the project:
    
    
    gdcloud iam service-accounts keys delete KEY_ID \
        --project=PROJECT \
        --iam-account=NAME
    

Replace the following:

  * KEY_ID: the unique identifier of the key.
  * PROJECT: the project ID.
  * NAME: the name of the service identity account.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
