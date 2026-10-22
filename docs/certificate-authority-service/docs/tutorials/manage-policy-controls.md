---
url: https://docs.cloud.google.com/certificate-authority-service/docs/tutorials/manage-policy-controls/
title: Manage policy controls \u00a0|\u00a0 Certificate Authority Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:38:16.780164+00:00
---

# Manage policy controls  |  Certificate Authority Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/certificate-authority-service/docs/tutorials/manage-policy-controls/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Certificate Authority Service ](https://docs.cloud.google.com/certificate-authority-service/docs)
  * [ Guides ](https://docs.cloud.google.com/certificate-authority-service/docs/ca-service-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Manage policy controls

This tutorial shows you how to implement policy controls on Certificate Authority Service resources.

## Objectives

This tutorial provides information on configuring a shared certificate authority (CA) pool for DNS certificate issuance with the following policy controls:

  * User `prod-dns-requester` can request end-entity server TLS certificates for the `*.prod.example.com` domain.
  * User `test-dns-requester` can request end-entity server TLS certificates for the `*.test.example.com` domain. 
  * User `blank-check-requester` can request any kind of certificate from the CA pool.



This tutorial uses the certificate issuance policy of a CA pool, certificate templates, and conditional IAM bindings to achieve this scenario.

## Before you begin

  * Read about the various [policy controls](https://docs.cloud.google.com/certificate-authority-service/docs/policy-controls) offered by CA Service.
  * Read how you can [create certificate templates](https://docs.cloud.google.com/certificate-authority-service/docs/creating-certificate-template).
  * Read about the [certificate profiles](https://docs.cloud.google.com/certificate-authority-service/docs/certificate-profile) that you can use for various certificate issuance scenarios.
  * Read how you can use [Common Expression Language (CEL)](https://docs.cloud.google.com/certificate-authority-service/docs/using-cel) to enforce various policy controls for certificate issuance.
  * Read how you can [use a certificate issuance policy](https://docs.cloud.google.com/certificate-authority-service/docs/use-issuance-policy).
  * Read how you can [configure, modify, and remove IAM policies](https://docs.cloud.google.com/certificate-authority-service/docs/configuring-iam) for creating and managing CA Service resources.



## Creating a CA pool

To create a CA pool, use the following instructions:

  1. To create a CA pool that uses the `issuance-policy.yaml` file, use the following `gcloud` command:

### gcloud
         
         gcloud privateca pools create POOL_NAME --location=LOCATION --tier=ENTERPRISE
         

Where:

     * LOCATION is the location where you want to create the CA pool. For the complete list of locations, see [Locations](https://docs.cloud.google.com/certificate-authority-service/docs/tutorials/locations).
     * `--tier` flag is used to specify the tier of the CA pool. For more information about tiers, see [Select the operation tiers](https://docs.cloud.google.com/certificate-authority-service/docs/tiers).

  2. To create a CA with Google-managed resources in the newly created CA pool, use the following `gcloud` command:

### gcloud
         
         gcloud privateca roots create CA_NAME \
             --pool=POOL_NAME \
             --location=LOCATION \
             --subject="CN=Example DNS Root, O=Example LLC, C=US" \
             --validity="10Y" \
             --max-chain-length=1 \
             --auto-enable
         

Where:

     * POOL_NAME is the unique identifier of the CA pool.
     * LOCATION is the location where you want to create the CA pool. For the complete list of locations, see [Locations](https://docs.cloud.google.com/certificate-authority-service/docs/tutorials/locations).
     * `--subject` flag is used to pass the name of the certificate subject.
     * `--validity` flag determines the validity period of the CA. The default validity period is 10 years.
     * `--max-chain-length` flag determines the maximum depth of subordinate CAs allowed under a CA.
     * `--auto-enable` flag creates the CA in `ENABLED` state, rather than in the `STAGED` state. For more information about CA states, see [CA states](https://docs.cloud.google.com/certificate-authority-service/docs/certificate-authority-states).

**Note:** The user who creates the CA pool has permissions associated with the CA Service Operations Manager (`roles/privateca.caManager`) role by default. Project-level permissions associated with the roles supersede any custom bindings set at the resource level. When you are creating fine-grained policy controls, ensure the accounts don't have project or organization-level permissions that might conflict with the issuance policy.



## Configuring policy controls for test certificates

The issuance policy changes are effective immediately. We recommend that you configure test policy controls before using them for production. This section describes how you can configure test policy controls.

For both the test and production DNS templates, you must use the same predefined values for server TLS certificates. Create a YAML file `leaf_server_tls_predefined_values.yaml`, and copy the following end-entity server TLS configuration into the file.
    
    
        keyUsage:
          baseKeyUsage:
            digitalSignature: true
            keyEncipherment: true
          extendedKeyUsage:
            serverAuth: true
        caOptions:
          isCa: false
    

### Configure policy controls for test DNS certificates

This section describes how you can set policy controls to allow the user `test-dns-requester` to request [end-entity server TLS](https://docs.cloud.google.com/certificate-authority-service/docs/certificate-profile#end-server-tls) certificates for DNS in the `*.test.example.com` domain.

#### Create DNS certificate template for test certificates

This section describes how you can create a certificate template that contains the [end-entity server TLS](https://docs.cloud.google.com/certificate-authority-service/docs/certificate-profile#end-server-tls) configuration. This certificate template restricts certificates to using only DNS SANs on the `*.test.example.com` domain. These restrictions are implemented using a Common Expression Language (CEL) expression. The certificate template also drops any subject specified in the certificate request.

  1. Use the following `gcloud` command to create the certificate template that contains the end-entity server TLS extensions, drops any `subject` specified in the certificate request, and limits allowed SANs.

### gcloud
         
         gcloud privateca templates create test-server-tls-template \
         --predefined-values-file  ./leaf_server_tls_predefined_values.yaml \
         --no-copy-subject \
         --copy-sans \
         --identity-cel-expression "subject_alt_names.all(san, san.type == DNS && san.value.endsWith('.test.example.com'))"
         

Where:

     * `--predefined-values-file` flag is used to pass a YAML file that describes any predefined X.509 values set by the certificate template.
     * `--no-copy-subject` flag drops all caller-specified subjects from the certificate request.
     * `--copy sans` flag ensures that the SAN extension from the certificate request is copied into the signed certificate.
     * `--identity-cel-expression` flag is used to pass a CEL expression that is evaluated against the identity in the certificate before it is issued. For more information about using CEL expressions to implement various policy controls, see [Using CEL](https://docs.cloud.google.com/certificate-authority-service/docs/using-cel).

For more information about creating certificate templates, see [Create a certificate template](https://docs.cloud.google.com/certificate-authority-service/docs/creating-certificate-template).




#### Create IAM bindings for DNS test certificates

To allow user `test-dns-requester@` in the DNS CA pool to request test server TLS certificates, create a conditional IAM binding on the CA pool. Grant the `privateca.certificateRequester` role to user `test-dns-requester@` only if the certificate request contains a reference to the `test-server-tls-template` template. For more information about IAM roles and permissions for CA Service, see [Access control with IAM](https://docs.cloud.google.com/certificate-authority-service/docs/access-control).

  1. Create a policy YAML file `test_dns_condition.yaml`, and copy the following TLS configuration into the file.
         
         title: test DNS binding
           description: allows user to only create DNS test certificates
           expression: api.getAttribute("privateca.googleapis.com/template", "") == "PROJECT_ID/-/test-server-tls-template"
         

The template syntax uses `PROJECT_ID/-/TEMPLATE_ID` instead of the standard full resource name `projects/PROJECT_ID/locations/LOCATION/certificateTemplates/TEMPLATE_ID` because certificate templates must reside in the same location as the CA pool. The hyphen (`-`) acts as a location wildcard, which keeps CEL conditions concise, readable, and location-agnostic.

The template name provided in the IAM condition must match the template name in the certificate request. So, if you're providing a project ID in the `privateca.googleapis.com/template` attribute of the CEL expression, you must also provide a project ID when requesting the certificate. If you provide a project number in the CEL expression, you must provide a project number in the certificate request as well.

  2. Use the following `gcloud` command to add policy controls that allow `test-dns-requester@` to only request production test TLS certificates from the CA pool.

### gcloud
         
         gcloud privateca pools add-iam-policy-binding POOL_NAME \
             --location=LOCATION \
             --role='roles/privateca.certificateRequester' \
             --member='user:test-dns-requester@' \
             --condition-from-file=./test_dns_condition.yaml
         

Where:

     * `--role` flag is used to pass the role name that is to be assigned to a member. For more information about IAM roles and permissions for CA Service, see [Access control with IAM](https://docs.cloud.google.com/certificate-authority-service/docs/access-control).
     * `--member` flag is used to pass the member to add the binding for.
     * `condition-from-file` flag is used to pass the name of the file with the CEL condition.

  3. Use the following `gcloud` to add policy controls that allow `test-dns-requester@` to use the 'test-server-tls-template' certificate template.

### gcloud
         
         gcloud privateca templates add-iam-policy-binding test-server-tls-template \
             --role='roles/privateca.templateUser' \
             --member='user:test-dns-requester@'
         

Where:

     * `--role` flag is used to pass the role name that is to be assigned to a member. For more information about IAM roles and permissions for CA Service, see [Access control with IAM](https://docs.cloud.google.com/certificate-authority-service/docs/access-control).
     * `--member` flag is used to pass the member to add the binding for.

For more information about configuring IAM policies, see [Configure IAM policies](https://docs.cloud.google.com/certificate-authority-service/docs/configuring-iam).




## Configuring policy controls for production certificates

Once you have tested your policy controls, you can use those policy controls in your production environment.

### Configure policy controls for production DNS certificates

This section describes how you can set policy controls to allow the user `prod-dns-requester` to request end-entity TLS certificates for the DNS `.prod.example.com` domain.

#### Create certificate template for production DNS certificates

Use the following instructions to create a certificate template that contains [end-entity server TLS](https://docs.cloud.google.com/certificate-authority-service/docs/certificate-profile#end-server-tls) configuration. This certificate template restricts certificates to using only DNS SANs on the `*.prod.example.com` domain. These restrictions are implemented using a Common Expression Language (CEL) expression. The certificate template also drops any subject specified in the certificate request.

Create a certificate template `prod-server-tls-template` using the following `gcloud` command.

### gcloud
    
    
    gcloud privateca templates create prod-server-tls-template \
      --predefined-values-file ./leaf_server_tls_predefined_values.yaml \
      --no-copy-subject \
      --copy-sans \
      --identity-cel-expression "subject_alt_names.all(san, san.type == DNS && san.value.endsWith('.prod.example.com'))"
    

Where:

  * `--predefined-values-file` flag is used to pass a YAML file that describes any predefined X.509 values set by the certificate template.
  * `--no-copy-subject` flag drops all caller-specified subjects from the certificate request.
  * `--copy sans` flag ensures that the SAN extension from the certificate request is copied into the signed certificate.
  * `--identity-cel-expression` flag is used to pass a CEL expression that is evaluated against the identity in the certificate before it is issued. For more information about CEL expressions, see [Using CEL expressions](https://docs.cloud.google.com/certificate-authority-service/docs/using-cel).



For more information about creating certificate templates, see [Create a certificate template](https://docs.cloud.google.com/certificate-authority-service/docs/creating-certificate-template).

For more information about the `gcloud privateca templates create` command, see [gcloud privateca templates create](https://docs.cloud.google.com/sdk/gcloud/reference/privateca/templates/create).

#### Create production DNS IAM binding

To allow user `prod-dns-requester@` in the DNS CA pool to request production server TLS certificates, create a conditional IAM binding on the CA pool. Give the user `prod-dns-requester@` the `privateca.certificateRequester` role only if the certificate request contains a reference to the `prod-server-tls-template` template. For more information about IAM roles and permissions, see: [Access control with IAM](https://docs.cloud.google.com/certificate-authority-service/docs/access-control).

  1. Create a policy YAML file `prod_dns_condition.yaml` and copy the following TLS configuration into the file.
         
         title: Production DNS binding
         description: allows user to only create DNS production certificates
         expression: api.getAttribute("privateca.googleapis.com/template", "") == "PROJECT_ID/-/prod-server-tls-template"
         

  2. Use the following `gcloud` command to add policy controls that allow `prod-dns-requester@` to only request production server TLS certificates from the CA pool.

### gcloud
         
         gcloud privateca pools add-iam-policy-binding POOL_NAME \
             --location=LOCATION \
             --role='roles/privateca.certificateRequester' \
             --member='user:prod-dns-requester@' \
             --condition-from-file=./prod_dns_condition.yaml
         

Where:

     * `--role` flag is used to pass the role name that is to be assigned to a member. For more information about IAM roles and permissions for CA Service, see [Access control with IAM](https://docs.cloud.google.com/certificate-authority-service/docs/access-control).
     * `--member` flag is used to pass the member to add the binding for.
     * `condition-from-file` flag is used to pass the name of the file with the CEL condition.

For more information about the `gcloud privateca pools add-iam-policy-binding` command, see [gcloud privateca pools add-iam-policy-binding](https://docs.cloud.google.com/sdk/gcloud/reference/privateca/pools/add-iam-policy-binding).

  3. To add policy controls that allow `prod-dns-requester@` to use the 'prod-server-tls-template' certificate template, use the following `gcloud` command:

### gcloud
         
         gcloud privateca templates add-iam-policy-binding prod-server-tls-template \
             --role='roles/privateca.templateUser' \
             --member='user:prod-dns-requester@'
         

Where:

     * `--role` flag is used to pass the role name that is to be assigned to a member. For more information about IAM roles and permissions for CA Service, see [Access control with IAM](https://docs.cloud.google.com/certificate-authority-service/docs/access-control).
     * `--member` flag is used to pass the member to add the binding for.




### Unrestricted user policy controls

To allow the user `blank-check-requester@` to request any certificate without any limitations, create an IAM binding without any conditionals giving the user the role `privateca.certificateRequester`.

### gcloud
    
    
    gcloud privateca pools add-iam-policy-binding POOL_NAME \
        --location=LOCATION \
        --role='roles/privateca.certificateRequester' \
        --member='user:blank-check-requester@example.com'
    

Where:

  * The value of the `--role` flag determines the role that is assigned to the user. For more information about IAM roles and permissions for CA Service, see [Access control with IAM](https://docs.cloud.google.com/certificate-authority-service/docs/access-control).
  * The value of the `--member` flag determines the user who is assigned the role.



Replace the following:

  * POOL_NAME: the unique identifier of the CA pool
  * LOCATION: the location of the CA pool. For the complete list of locations, see [Locations](https://docs.cloud.google.com/certificate-authority-service/docs/tutorials/locations).



## Testing the policy controls

Once you have implemented your certificate issuance and IAM policies, it is important to review and test these policies to ensure that they work as expected.

### Retrieve all policy bindings

Fetch all the IAM policies that are implemented on your CA pool. To retrieve all the IAM policies for the CA pool, use the `gcloud privateca pools get-iam-policy` command:

### gcloud
    
    
    gcloud privateca pools get-iam-policy POOL_NAME --location=LOCATION
    

Replace the following:

  * POOL_NAME: the unique identifier of the CA pool
  * LOCATION: the location of the CA pool. For the complete list of locations, see [Locations](https://docs.cloud.google.com/certificate-authority-service/docs/tutorials/locations).



For more information about the `gcloud privateca pools get-iam-policy` command, see [gcloud privateca pools get-iam-policy](https://docs.cloud.google.com/sdk/gcloud/reference/privateca/pools/get-iam-policy).

## Generating certificates

This section provides information on generating general-purpose certificates, and test and production DNS certificates.

### Generate test DNS certificates

To allow user `test-dns-requester@` to request test DNS certificates from the CA pool, use the following `gcloud` command:

### gcloud
    
    
    gcloud privateca certificates create test-dns-1 \
        --project=PROJECT_ID \
        --issuer-location=LOCATION \
        --issuer-pool=POOL_NAME \
        --dns-san=foo.bar.test.example.com \
        --generate-key \
        --key-output-file=KEY_FILE_NAME \
        --cert-output-file=test_dns_cert.pem \
        --template=projects/PROJECT_ID/locations/LOCATION/certificateTemplates/test-server-tls-template
    

Where:

  * `--dns-san` flag is used to set one or more comma-separated DNS SANs.
  * `--generate-key` flag triggers the generation of a new RSA-2048 private key on your machine.
  * `--key-output-file` flag is used to set the path where the generated private key is written (in PEM format).
  * `--cert-output-file` flag is used to set the path where the resulting PEM-encoded certificate chain file is written (ordered from end-entity to root).
  * `--template` flag is used to set the name of the certificate template that you want to use for issuing this certificate. The specified template must be in the same location as the issuing CA pool. For more information about certificate templates, see [Overview of certificate templates and issuance policies](https://docs.cloud.google.com/certificate-authority-service/docs/certificate-template).



Replace the following:

  * PROJECT_ID: the unique identifier of the project
  * LOCATION: the location of the CA pool from which the certificate is requested. For the complete list of locations, see [Locations](https://docs.cloud.google.com/certificate-authority-service/docs/tutorials/locations).
  * POOL_NAME: the unique identifier of the CA pool



### Generate production certificates

The user `prod-dns-requester` can now request production DNS certificates from the CA pool. The `--dns-san=foo.bar.prod.example.com` adds a SAN of DNS type with the specified value to the certificate request.

### gcloud
    
    
    gcloud privateca certificates create prod-dns-1 \
        --project=PROJECT_ID \
        --issuer-location=LOCATION \
        --issuer-pool=POOL_NAME \
        --dns-san=foo.bar.prod.example.com \
        --generate-key \
        --key-output-file=KEY_FILE_NAME \
        --cert-output-file=prod_dns_cert.pem \
        --template=projects/PROJECT_ID/locations/LOCATION/certificateTemplates/prod-server-tls-template
    

Where:

  * `--issuer-location` flag is used to set the location of the certificate. For the complete list of locations, see [Locations](https://docs.cloud.google.com/certificate-authority-service/docs/locations).
  * `--issuer-pool` flag sets the CA pool from which the certificate is requested.
  * `--dns-san` flag is used to set one or more comma-separated DNS SANs.
  * `--generate-key` flag triggers the generation of a new RSA-2048 private key on your machine.
  * `--key-output-file` flag is used to set the path where the generated private key is written (in PEM format).
  * `--cert-output-file` flag is used to set the path where the resulting PEM-encoded certificate chain file is written (ordered from end-entity to root).
  * `--template` flag is used to set the name of the certificate template to use for issuing this certificate. The specified template must be in the same location as the issuing CA pool. For more information about certificate templates, see [Overview of certificate templates and issuance policies](https://docs.cloud.google.com/certificate-authority-service/docs/certificate-template).



### Generate general-purpose certificates

The user `blank-check-requester@` can request any certificate from the CA pool using the `gcloud privateca certificates create` command.

To request a certificate from a CA pool, you can use a public/private key created by CA Service. For more information about requesting certificates, see [Request a certificate and view issued certificate](https://docs.cloud.google.com/certificate-authority-service/docs/requesting-certificates).

## Clean up

This section explains how you can remove IAM policies over a CA pool.

### Remove a specific IAM binding

To remove the IAM conditional bindings over the CA pool for `blank-check-requester` user, use the following `gcloud` command:

### gcloud
    
    
    gcloud privateca pools remove-iam-policy-binding POOL_NAME \
        --location=LOCATION \
        --role='roles/privateca.certificateRequester' \
        --member='user:blank-check-requester@'
    

Where:

  * The value of the `--role` flag determines the role that is assigned to the user. For more information about IAM roles and permissions for CA Service, see [Access control with IAM](https://docs.cloud.google.com/certificate-authority-service/docs/access-control).
  * The value of the `--member` flag determines the user who is assigned the role.



When removing a specific IAM binding, you must provide all the information related to the IAM binding in the `gcloud privateca pools remove-iam-policy-binding` command. A role and member might have multiple IAM bindings with different conditions. It is important that you provide all the details related to the IAM binding to avoid accidentally deleting a different binding.

For more information about the `gcloud privateca pools remove-iam-policy-binding` command, see [gcloud privateca pools remove-iam-policy-binding](https://docs.cloud.google.com/sdk/gcloud/reference/privateca/pools/remove-iam-policy-binding).

### Remove all IAM conditional bindings

To remove an IAM binding, you can use the `gcloud privateca pools remove-iam-policy-binding` command. When removing an IAM conditional binding, you must provide all the information about the binding. A user and a role can have more than one conditional binding. To remove all conditional bindings, use the `--all` flag in your `gcloud` command.

Use the following `gcloud` command to remove all bindings for the `prod-code-signing-requester` user.

### gcloud
    
    
    gcloud privateca pools remove-iam-policy-binding POOL_NAME \
        --location=LOCATION \
        --role='roles/privateca.certificateRequester' \
        --member='user:prod-code-signing-requester@' \
        --all
    

Where:

  * The value of the `--role` flag determines the role that is assigned to the user. For more information about IAM roles and permissions for CA Service, see [Access control with IAM](https://docs.cloud.google.com/certificate-authority-service/docs/access-control).
  * The value of the `--member` flag determines the user who is assigned the role.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
