---
url: https://docs.cloud.google.com/certificate-authority-service/docs/tutorials/using-3pi-with-reflection/
title: Issue certificates that attest to third-party identity \u00a0|\u00a0 Certificate Authority Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T14:59:36.999904+00:00
---

# Issue certificates that attest to third-party identity  |  Certificate Authority Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/certificate-authority-service/docs/tutorials/using-3pi-with-reflection/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Certificate Authority Service ](https://docs.cloud.google.com/certificate-authority-service/docs)
  * [ Guides ](https://docs.cloud.google.com/certificate-authority-service/docs/ca-service-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Issue certificates that attest to third-party identity

This tutorial demonstrates how you can issue certificates that attest to a third-party identity using [identity reflection](https://docs.cloud.google.com/certificate-authority-service/docs/using-identity-reflection) and [workload identity pools](https://docs.cloud.google.com/iam/docs/workload-identity-federation#pools).

You can use identity reflection to create certificates that match the verified identity of a certificate requester. Using identity reflection, you can limit an unprivileged certificate requester to requesting only certificates with a subject alternative name (SAN) corresponding to the identity in their credential.

## Objectives

This tutorial provides information about how you can use CA Service with workload identity pools to federate a third-party identity and obtain a certificate that attests to this identity.

## Before you begin

Before you begin, make sure that you understand the following concepts:

  * **Workload identity pools** : Workload identity pools let you manage third-party identity providers. For more information, see [Manage workload identity pools and providers](https://docs.cloud.google.com/iam/docs/manage-workload-identity-pools-providers).
  * **Workload identity federation** : Workload identity federation leverages workload identity pools to give third-party identities access to Google Cloud services. For more information, see [Workload identity federation](https://docs.cloud.google.com/iam/docs/workload-identity-federation).
  * **Security Token Service (STS)** : The Security Token Service lets you exchange third-party credentials for first-party (Google Cloud) tokens. For more information, see [Security Token Service](https://docs.cloud.google.com/iam/docs/reference/sts/rest).
  * **Identity reflection** : The identity reflection feature lets the verified identity of a certificate requester go on to the requested certificate. For more information, see [Identity reflection](https://docs.cloud.google.com/certificate-authority-service/docs/using-identity-reflection).



Make sure that you have the following [IAM roles](https://docs.cloud.google.com/iam/docs/overview#roles):

**Note:** Grant the following IAM roles with caution. The permissions associated with the following roles grant access to security critical Google Cloud controls. If you plan to use the same project later for production, we recommend reviewing these permissions again and reducing access wherever possible.

  * To manage certificate authorities (CAs) and [CA pools](https://docs.cloud.google.com/certificate-authority-service/docs/ca-pool), and request certificates, you must have the CA Service Operation Manager (`privateca.caManager`) role. For more information about IAM roles for CA Service, see [Access control with IAM](https://docs.cloud.google.com/certificate-authority-service/docs/access-control).
  * To manage workload identity pools and providers, you must have the Workload Identity Pool Admin (`iam.workloadIdentityPoolAdmin`) role.
  * To create a service account, you must have the Service Account Admin (`iam.serviceAccountAdmin`) role.



For information about granting IAM roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). You can grant the required IAM roles to a Google Account, a service account, a Google group, a Google Workspace account, or a Cloud Identity domain.

## Set up a workload identity pool and provider

This tutorial explains how you can use a [Google OpenID Connect (OIDC)](https://developers.google.com/identity/protocols/oauth2/openid-connect) provider combined with a service account to act as a third-party identity. The Google Accounts OIDC provider acts as a third-party identity provider (IDP) and the Google Cloud service account is a sample third-party identity asserted by this IDP.

Workload identity pools support a variety of identity providers, including Microsoft Azure/On-premises Active Directory, AWS, and SAML-based identity providers.

To set up a workload identity pool and provider, do the following:

  1. To represent a trusted set of federated identities, create a workload identity pool:
         
         gcloud iam workload-identity-pools create IDENTITY_POOL_ID --location global --display-name "tutorial-wip"
         

Replace the following:

     * IDENTITY_POOL_ID: The unique identifier of the new workload identity pool
  2. Create a workload identity pool provider for your third-party identity provider:
         
         gcloud iam workload-identity-pools providers create-oidc PROVIDER_ID --location global --workload-identity-pool IDENTITY_POOL_ID --display-name "tutorial-oidc" --attribute-mapping "google.subject=assertion.sub" --issuer-uri="https://accounts.google.com"
         

Replace the following:

     * PROVIDER_ID: The unique identifier of the identity provider that you want to create in the workload identity pool

You can customize the following flags to your use case:

     * `attribute-mapping`: This flag sets the mapping between the third-party claims to the Google principal claim, `google.subject`. `google.subject` is a required mapping that you can set to any claims or combination of claims using a [CEL](https://opensource.google/projects/cel) expression. For more information, see [Define an attribute mapping and condition](https://docs.cloud.google.com/iam/docs/configuring-workload-identity-federation#mappings-and-conditions).
     * `issuer-uri`: For OIDC providers, this flag is a publicly accessible endpoint that Google reaches out to for verification of third-party tokens. For more information, see [Preparing an external identity provider](https://docs.cloud.google.com/iam/docs/configuring-workload-identity-federation#prepare).

For more information about setting up a workload identity provider, see [Configuring workload identity federation](https://docs.cloud.google.com/iam/docs/workload-identity-federation-with-other-providers#configure).




## Create a CA pool and an issuing CA

This section explains how you can create a CA pool and add a root CA to it. You can use this CA pool to issue identity-reflected certificates. If you want to use an existing CA pool and CA, you can skip this section.

Instead of a root CA, you can also choose to create a subordinate CA. Creating a root CA helps shorten the procedure.

  1. Create a CA pool in the [DevOps tier](https://docs.cloud.google.com/certificate-authority-service/docs/tiers):
         
         gcloud privateca pools create CA_POOL_ID --location LOCATION --tier devops
         

Replace the following:

     * CA_POOL_ID \- The ID of the CA Service CA pool that issues certificates
     * LOCATION \- The location of the CA pool

For more information about creating CA pools, see [Create a CA pool](https://docs.cloud.google.com/certificate-authority-service/docs/creating-ca-pool).

  2. Create a root CA:
         
         gcloud privateca roots create CA_ID --pool CA_POOL_ID  --location LOCATION --subject "CN=test,O=test-org"
         

Replace the following:

     * CA_ID \- The ID of certificate authority that issues certificates
     * CA_POOL_ID \- The ID of the CA Service CA pool that issues certificates
     * LOCATION \- The location of the CA pool

For more information about creating a root CA, see [Create a root CA](https://docs.cloud.google.com/certificate-authority-service/docs/creating-root-ca).

  3. Enable identities federated from the workload identity pool to issue certificates from the CA Pool. Identity reflection requires the CA Service Workload Certificate Requester (`roles/privateca.workloadCertificateRequester`) IAM role for the requesters of [`CreateCertificate`](https://docs.cloud.google.com/certificate-authority-service/docs/reference/rpc/google.cloud.security.privateca.v1#createcertificaterequest).

You can represent workload identity pool principals in various granularities, ranging from a single subject to all identities in the pool across providers. For more information, see the [principals or principal sets that are available (use the Google Cloud CLI tab)](https://docs.cloud.google.com/iam/docs/using-workload-identity-federation#impersonate) to best suit your use case.

**Note:** You don't need to impersonate a service account to reach out to CA Service.
         
         gcloud privateca pools add-iam-policy-binding CA_POOL_ID --location LOCATION --role roles/privateca.workloadCertificateRequester --member "principalSet://iam.googleapis.com/projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/IDENTITY_POOL_ID/*"
         

Replace the following:

     * CA_POOL_ID: The ID of the CA Service CA pool that issues certificates
     * LOCATION: The location of the CA pool
     * PROJECT_NUMBER: The project number of the project where you created the workload identity pool
     * IDENTITY_POOL_ID: The unique identifier of the new workload identity pool



## Create a service account that represents a third-party identity

The following procedure assumes that a service account represents a third-party. This section shows how you can use the [`GenerateIdToken`](https://docs.cloud.google.com/iam/docs/creating-short-lived-service-account-credentials#sa-credentials-oidc) IAM endpoint to retrieve a third-party identity in the form of an OIDC token. Depending on your use case, you might need different steps to obtain the third-party identity token of your choosing.
    
    
    gcloud iam service-accounts create SERVICE_ACCOUNT
    

Replace the following:

  * SERVICE_ACCOUNT \- The ID of the service account that represents the third-party identity



## Issue a certificate attesting to a third-party identity

Before you begin, make sure that you have the Service Account OpenID Connect Identity Token Creator (`roles/iam.serviceAccountOpenIdTokenCreator`) IAM role. You need this IAM role to call the `GenerateIdToken` API.

To obtain a certificate that attests to a third-party identity, do the following:

  1. Obtain a third-party identity token from your third-party identity provider.

### curl

**Note:** To perform this command, you need the [`python3`](https://www.python.org/download/releases/3.0/) CLI.
         
         export ID_TOKEN=`curl -d '{"audience":"//iam.googleapis.com/projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/IDENTITY_POOL_ID/providers/PROVIDER_ID"}' -H 'Content-Type: application/json' -H "Authorization: Bearer $(gcloud auth print-access-token)" https://iamcredentials.googleapis.com/v1/projects/-/serviceAccounts/SERVICE_ACCOUNT@PROJECT_ID.iam.gserviceaccount.com:generateIdToken | python3 -c "import sys;import json;print(json.load(sys.stdin)['token'])"`
         

Replace the following:

     * PROJECT_ID \- The Google Cloud project ID for the project you want to create resources in

### Client libraries

**Note:** This flow requires the Python-based client libraries for CA Service. For information about installing the Python-based client libraries, see [Python client for CA Service](https://docs.cloud.google.com/python/docs/reference/privateca/latest)

To access the third-party token programmatically, you can obtain a token from a file-sourced credential or a url-sourced credential. For more information, see [Authenticating by using client libraries, the gcloud CLI, or Terraform](https://docs.cloud.google.com/iam/docs/using-workload-identity-federation#generate-automatic). In this tutorial, we follow a file-source credential workflow.

Load your credential into a path readable by your certificate requester:
    
    curl -d '{"audience":"//iam.googleapis.com/projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/IDENTITY_POOL_ID/providers/PROVIDER_ID"}' -H 'Content-Type: application/json' -H "Authorization: Bearer $(gcloud auth print-access-token)" https://iamcredentials.googleapis.com/v1/projects/-/serviceAccounts/SERVICE_ACCOUNT@PROJECT_ID.iam.gserviceaccount.com:generateIdToken | python3 -c "import sys;import json;       print(json.load(sys.stdin)['token']) > /tmp/oidc_token.txt
    

Replace the following:

     * PROJECT_ID: The project ID of the project you want to create resources in

  2. Exchange your third-party token for a federated OAuth token using the STS `token` endpoint:

### curl
         
         export STS_TOKEN=`curl -L -X POST 'https://sts.googleapis.com/v1/token' -H 'Content-Type: application/json' \
         -d '{
             "grant_type": "urn:ietf:params:oauth:grant-type:token-exchange",
             "audience": "//iam.googleapis.com/projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/IDENTITY_POOL_ID/providers/PROVIDER_ID",
             "requested_token_type": "urn:ietf:params:oauth:token-type:access_token",
             "scope": "https://www.googleapis.com/auth/cloud-platform",
             "subject_token": "'$ID_TOKEN'",
             "subject_token_type": "urn:ietf:params:oauth:token-type:jwt"
         }' | python3 -c "import sys;import json; print(json.load(sys.stdin)['access_token'])"`
         

### Client libraries

     1. Create a credential configuration file named `oidc_token.txt` that the certificate requesting code can read to perform a token exchange.
    
    gcloud iam workload-identity-pools create-cred-config projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/IDENTITY_POOL_ID --output-file=/tmp/cred_config.json --credential-source-file=/tmp/oidc_token.txt
    

     1. Read the `oidc_token.txt` file to set the authorization mechanism in the client library:

### python
    
    import json
    
    from google.auth import identity_pool
    
    with open('/tmp/cred_config.json', 'r') as f:
      json_config_info = json.loads(f.read())
    credentials = identity_pool.Credentials.from_info(json_config_info)
    scoped_credentials = credentials.with_scopes(
        ['https://www.googleapis.com/auth/cloud-platform'])
    

  3. Make a request to CA Service with the [`REFLECTED_SPIFFE`](https://docs.cloud.google.com/certificate-authority-service/docs/reference/rest/v1/projects.locations.caPools.certificates#subjectrequestmode) subject request mode:

### curl

     1. Optional: If you don't have a CSR, create a CSR by executing the following command.

**Note:** The following command creates a CSR with no subject. CA Service will add a subject that reflects the certificate requester's identity.
            
            export TUTORIAL_CSR=$(openssl req -newkey rsa:2048 -nodes -subj / -keyout tutorial_do_not_use.key)
            

     2. Request a certificate with the CSR, a lifetime, and a reflected subject request mode:
            
            curl -H "Authorization: Bearer $(echo $STS_TOKEN)" https://privateca.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION/caPools/CA_POOL_ID/certificates\?alt\=json  -X POST -H "Content-Type: application/json" -H 'Accept: application/json' --data '{"lifetime": "100s", "pemCsr": "'$TUTORIAL_CSR'", "subjectMode": "REFLECTED_SPIFFE"}'
            

### Client libraries

To forward the first-party token to CA Service, you must create a credentialed client. You can then use this credentialed client to make certificate requests:

     1. Initiate a credentialed CA Service client:

### python
            
            caServiceClient = privateca_v1.CertificateAuthorityServiceClient(credentials=scoped_credentials)
            

     2. Request a certificate.

**Note:** Make sure to update the `caServiceClient` variable in the following example to use the credentialed version described in the previous step.

### Python

To authenticate to CA Service, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
            
            import google.cloud.security.privateca_v1 as privateca_v1
            from google.protobuf import duration_pb2
            
            
            def create_certificate(
                project_id: str,
                location: str,
                ca_pool_name: str,
                ca_name: str,
                certificate_name: str,
                common_name: str,
                domain_name: str,
                certificate_lifetime: int,
                public_key_bytes: bytes,
            ) -> None:
                """
                Create a Certificate which is issued by the Certificate Authority present in the CA Pool.
                The key used to sign the certificate is created by the Cloud KMS.
            
                Args:
                    project_id: project ID or project number of the Cloud project you want to use.
                    location: location you want to use. For a list of locations, see: https://cloud.google.com/certificate-authority-service/docs/locations.
                    ca_pool_name: set a unique name for the CA pool.
                    ca_name: the name of the certificate authority which issues the certificate.
                    certificate_name: set a unique name for the certificate.
                    common_name: a title for your certificate.
                    domain_name: fully qualified domain name for your certificate.
                    certificate_lifetime: the validity of the certificate in seconds.
                    public_key_bytes: public key used in signing the certificates.
                """
            
                caServiceClient = privateca_v1.CertificateAuthorityServiceClient()
            
                # The public key used to sign the certificate can be generated using any crypto library/framework.
                # Also you can use Cloud KMS to retrieve an already created public key.
                # For more info, see: https://cloud.google.com/kms/docs/retrieve-public-key.
            
                # Set the Public Key and its format.
                public_key = privateca_v1.PublicKey(
                    key=public_key_bytes,
                    format_=privateca_v1.PublicKey.KeyFormat.PEM,
                )
            
                subject_config = privateca_v1.CertificateConfig.SubjectConfig(
                    subject=privateca_v1.Subject(common_name=common_name),
                    subject_alt_name=privateca_v1.SubjectAltNames(dns_names=[domain_name]),
                )
            
                # Set the X.509 fields required for the certificate.
                x509_parameters = privateca_v1.X509Parameters(
                    key_usage=privateca_v1.KeyUsage(
                        base_key_usage=privateca_v1.KeyUsage.KeyUsageOptions(
                            digital_signature=True,
                            key_encipherment=True,
                        ),
                        extended_key_usage=privateca_v1.KeyUsage.ExtendedKeyUsageOptions(
                            server_auth=True,
                            client_auth=True,
                        ),
                    ),
                )
            
                # Create certificate.
                certificate = privateca_v1.Certificate(
                    config=privateca_v1.CertificateConfig(
                        public_key=public_key,
                        subject_config=subject_config,
                        x509_config=x509_parameters,
                    ),
                    lifetime=duration_pb2.Duration(seconds=certificate_lifetime),
                )
            
                # Create the Certificate Request.
                request = privateca_v1.CreateCertificateRequest(
                    parent=caServiceClient.ca_pool_path(project_id, location, ca_pool_name),
                    certificate_id=certificate_name,
                    certificate=certificate,
                    issuing_certificate_authority_id=ca_name,
                )
                result = caServiceClient.create_certificate(request=request)
            
                print("Certificate creation result:", result)
            
            

     3. Verify the certificate. Your certificate should have a subject containing a single URI SAN. The SAN that attests to an identity is in the following format:
            
            spiffe://IDENTITY_POOL_ID.PROJECT_NUMBER.global.workload.id.goog/subject/<oidc_subject_number>
            

Replace:

        * IDENTITY_POOL_ID: The unique identifier of the workload identity pool
        * PROJECT_NUMBER \- The project number of the project where you created the workload identity pool




## Clean up

To avoid incurring charges to your Google Cloud account for the CA Service resources you created following this document, perform the following operations using the Google Cloud CLI:

  1. Delete the CA you created.

     1. Disable the CA:
            
            gcloud privateca roots disable CA_ID --pool CA_POOL_ID  --location LOCATION
            

Replace:

        * CA_ID: The unique identifier of the CA
        * CA_POOL_ID: The unique identifier of the CA pool
        * LOCATION: The location of the CA pool
     2. Delete the CA:
            
            gcloud privateca roots delete CA_ID --pool CA_POOL_ID  --location LOCATION --ignore-active-certificates
            

Replace:

        * CA_ID: The unique identifier of the CA
        * CA_POOL_ID: The unique identifier of the CA pool
        * LOCATION: The location of the CA pool
  2. Delete the CA pool you created.

**Note:** You can't delete a CA pool until you have permanently deleted all the CAs within it. The default expiration time of a CA is 30 days.
         
         gcloud privateca pools delete CA_POOL_ID --location LOCATION
         

Replace:

     * CA_POOL_ID: The unique identifier of the CA pool
     * LOCATION: The location of the CA pool

For more information about the `gcloud privateca pools delete` command, see [gcloud privateca pools delete](https://docs.cloud.google.com/sdk/gcloud/reference/privateca/pools/delete).

  3. Delete the workload identity pool you created:
         
         gcloud iam workload-identity-pools delete IDENTITY_POOL_ID --location global
         

Replace:

     * IDENTITY_POOL_ID: The unique identifier of the workload identity pool
  4. Delete the service account that you created:
         
         gcloud iam service-accounts delete SERVICE_ACCOUNT@PROJECT_ID.iam.gserviceaccount.com
         

Replace:

     * SERVICE_ACCOUNT: The unique identifier of the workload identity pool
     * PROJECT_ID: The project that owns the service account



The CA Service Workload Certificate Requester (`privateca.workloadCertificateRequester`) IAM role restricts the subject of the issued certificate to only the identity of the requester. Ensure that users or workloads using the identity reflection feature are only granted the CA Service Workload Certificate Requester (`privateca.workloadCertificateRequester`) IAM role. To abide by the principle of least privilege, you can avoid granting the CA Service Certificate Requester (`privateca.certificateRequester`) IAM role.

## What's next

  * Read about the various [policy controls](https://docs.cloud.google.com/certificate-authority-service/docs/policy-controls) that let you control the properties of the requested certificate beyond a reflected identity.
  * Read how you can [configure and manage various policy controls](https://docs.cloud.google.com/certificate-authority-service/docs/tutorials/manage-policy-controls).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
