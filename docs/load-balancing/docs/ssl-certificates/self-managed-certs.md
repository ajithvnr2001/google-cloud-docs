---
url: https://docs.cloud.google.com/load-balancing/docs/ssl-certificates/self-managed-certs/
title: Use self-managed SSL certificates \u00a0|\u00a0 Cloud Load Balancing \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:18:38.748633+00:00
---

# Use self-managed SSL certificates  |  Cloud Load Balancing  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/load-balancing/docs/ssl-certificates/self-managed-certs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Load Balancing ](https://docs.cloud.google.com/load-balancing/docs)
  * [ Guides ](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview)



Send feedback 

#  Use self-managed SSL certificates Stay organized with collections  Save and categorize content based on your preferences. 

Self-managed SSL certificates are certificates that you obtain, provision, and renew yourself. You can use this resource to secure communication between clients and your load balancer.

Self-managed certificates can be any combination of the following certificate types:

  * Domain Validation (DV)
  * Organization Validation (OV)
  * Extended Validation (EV)



Self-managed certificates are supported with the following load balancers:

  * **Global certificates**
    * Global external Application Load Balancer
    * Classic Application Load Balancer
    * External proxy Network Load Balancer (with a target SSL proxy)


  * **Regional certificates**
    * Regional external Application Load Balancer
    * Regional internal Application Load Balancer



This page describes the process of obtaining a valid Compute Engine certificate and then uploading your certificate to create a Google Cloud SSL certificate resource.

To create Google-managed certificates using Certificate Manager, see [Deployment overview](https://docs.cloud.google.com/certificate-manager/docs/deploy).

**Note:**

For self-managed certificates for GKE Ingress, see [ Setting up HTTPS (TLS) between client and load balancer](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/ingress-xlb#setting_up_https_tls_between_client_and_load_balancer) in the Ingress for external Application Load Balancers document.

## Before you begin

  * Make sure that you are familiar with the [SSL certificates overview](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates).
  * Make sure that you have the domain names that you want to use for your self-managed SSL certificate. If you're using Cloud Domains, see [Step 1: Register a domain name using Cloud Domains](https://docs.cloud.google.com/dns/docs/tutorials/create-domain-tutorial#register-domain).



### Permissions

To perform the tasks in this guide, you must be able to create and modify SSL certificates in your project. You can do this if one of the following is true:

  * You are a project [Owner or Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner` or `roles/editor`).
  * You have both the [Compute Security Admin role](https://docs.cloud.google.com/compute/docs/access/iam#compute.securityAdmin) (`compute.securityAdmin`) and the [Compute Network Admin role](https://docs.cloud.google.com/compute/docs/access/iam#compute.networkAdmin) (`compute.networkAdmin`) in the project.
  * You have a custom role for the project that includes the `compute.sslCertificates.*` permissions and one or both of `compute.targetHttpsProxies.*` and `compute.targetSslProxies.*`, depending on the type of load balancer that you are using.



## Step 1: Create a private key and certificate

If you already have a private key and a certificate from a certificate authority (CA), skip this section and go to Creating an SSL certificate resource.

### Select or create a private key

A Google Cloud SSL certificate includes both a private key and the certificate itself, both in PEM format. Your private key must meet the following criteria:

  * It must be in [PEM format](http://ospkibook.sourceforge.net/docs/OSPKI-2.4.7/OSPKI-html/sample-ca-cert.htm).
  * It cannot be protected by a passphrase. Google Cloud stores your private key in its own encrypted format.
  * Its encryption algorithm must be either RSA or ECDSA. To know which key types that you can use, see [Supported key types](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates#key-types).



To create a new _private key_ , use one of the following [OpenSSL](https://www.openssl.org/docs/) commands.

  * Create an RSA-2048 private key:
        
        openssl genrsa -out PRIVATE_KEY_FILE 2048
        

  * Create an ECDSA P-256 private key:
        
        openssl ecparam -name prime256v1 -genkey -noout -out PRIVATE_KEY_FILE
        




Replace PRIVATE_KEY_FILE with the path and filename for the new private key file.

### Create a certificate signing request (CSR)

After you have a private key, you can generate a certificate signing request (CSR) in the PEM format using [OpenSSL](https://www.openssl.org/source/). Your CSR must meet the following criteria:

  * It must be in PEM format.
  * It must have a common name (`CN`) or a subject alternative name (`SAN`) attribute. Practically speaking, your certificate should contain _both_ `CN` and `SAN` attributes, even if it is for a single domain—modern clients, like the [current versions of macOS and iOS](https://support.apple.com/en-us/HT210176) don't rely on just the `CN` attribute.



To create a CSR, follow these steps:

  1. Create an [OpenSSL configuration file](https://github.com/openssl/openssl/blob/master/apps/openssl.cnf). In the following example, subject alternative names are defined in the `[sans_list]`.
         
         cat <<'EOF' >CONFIG_FILE
         [req]
         default_bits              = 2048
         req_extensions            = extension_requirements
         distinguished_name        = dn_requirements
         prompt                    = no
         
         [extension_requirements]
         basicConstraints          = CA:FALSE
         keyUsage                  = nonRepudiation, digitalSignature, keyEncipherment
         subjectAltName            = @sans_list
         
         [dn_requirements]
         countryName               = Country Name (2 letter code)
         stateOrProvinceName       = State or Province Name (full name)
         localityName              = Locality Name (eg, city)
         0.organizationName        = Organization Name (eg, company)
         organizationalUnitName    = Organizational Unit Name (eg, section)
         commonName                = Common Name (e.g. server FQDN or YOUR name)
         emailAddress              = Email Address
         
         [sans_list]
         DNS.1                     = SUBJECT_ALTERNATIVE_NAME_1
         DNS.2                     = SUBJECT_ALTERNATIVE_NAME_2
         
         EOF
         

  2. Run the following OpenSSL command to create a certificate signing request (CSR) file. The command is interactive; you are prompted for attributes _except_ for the subject alternative names, which you defined in the `[sans_list]` of the CONFIG_FILE in the previous step.
         
         openssl req -new -key PRIVATE_KEY_FILE \
             -out CSR_FILE \
             -config CONFIG_FILE
         




For both steps, replace the following:

  * CONFIG_FILE: the path, including the filename, for the OpenSSL configuration file (you can delete the file after you complete this procedure)
  * SUBJECT_ALTERNATIVE_NAME_1 and SUBJECT_ALTERNATIVE_NAME_2: Subject Alternative Names for your certificate

If your certificate is only for one hostname, you should only define a single subject alternative name that matches the Common Name. If you need more than two subject alternative names, add them to the configuration file, incrementing the number after `DNS` (`DNS.3`, `DNS.4`, etc.).

  * PRIVATE_KEY_FILE: the path to the private key file

  * CSR_FILE: the path, including the filename, for the CSR




### Sign the CSR

When a Certificate Authority (CA) signs your CSR, it uses its _own_ private key to create a certificate. Use one of the following methods to sign the CSR:

#### Use a publicly trusted CA

If you request a publicly trusted CA to sign your CSR, the resulting certificate is trusted by all clients that trust that public CA. To produce a signed certificate, the public CA only needs your CSR.

#### Use your own internal CA

If you manage your own CA, you can use it to sign your CSR. Using your CA to sign your CSR creates an _internally trusted_ certificate when your clients have also been configured to trust your own CA.

#### Use a self-signed certificate

If you use the same private key that you used to create the CSR to sign the CSR, then you've created a _self-signed certificate_. You should only use self-signed certificates for testing.

Google Cloud doesn't support client-side verification for self-signed server certificates. Therefore, you must configure the client to skip certificate validation. For example, you can create a web browser client that displays a message asking you if you want to trust a self-signed certificate.

If you manage your own CA, or if you want to create a self-signed certificate for testing, you can use the following OpenSSL command:
    
    
    openssl x509 -req \
        -signkey PRIVATE_KEY_FILE \
        -in CSR_FILE \
        -out CERTIFICATE_FILE \
        -extfile CONFIG_FILE \
        -extensions extension_requirements \
        -days TERM
    

Replace the following:

  * PRIVATE_KEY_FILE: the path to the private key for your CA; if creating a self-signed certificate for testing, this private key is the same as the one used to create the CSR
  * CSR_FILE: the path to the CSR
  * CERTIFICATE_FILE: the path to the certificate file to create
  * TERM: the number of days, from now, during which the certificate should be considered valid by clients that verify it



### Wildcards in common names

Your self-managed SSL certificates can use a wildcard in the common name. For example, a certificate with the common name `*.example.com.` matches the hostnames `www.example.com` and `foo.example.com`, but not `a.b.example.com` or `example.com`. When the load balancer selects a certificate, it always prefers to match a hostname to certificates without wildcards over certificates with wildcards.

Certificates with wildcard fragments, such as `f*.example.com`, aren't supported.

## Step 2: Create a self-managed SSL certificate resource

Before you can create a Google Cloud SSL certificate resource, you must have a private key and certificate. Refer to Creating a private key and certificate if you have not already created or obtained them.

After creating a certificate, you can't change its scope from global to regional, or from regional to global.

###  Console 

You can create global SSL certificates from the **Classic Certificates** tab in the Google Cloud console.

Regional SSL certificates _cannot_ be created from the **Classic Certificates** tab in the Google Cloud console. Use either `gcloud` or the REST API. Regional SSL certificates can also be created as a part of the regional Application Load Balancer creation workflow using the Google Cloud console.

**Note:** The following procedure takes you directly to the **Classic Certificates** tab. You can find the **Classic Certificates** tab in the **Certificate Manager** page linked from the top-level [**Security**](https://console.cloud.google.com/security/) page.

  1. Go to the **Classic Certificate** tab in the Google Cloud console.   
[Go to Classic Certificates](https://console.cloud.google.com/security/ccm/list/lbCertificates)
  2. Click **Create SSL certificate**.
  3. Enter a name and an optional description for the certificate.
  4. Select **Upload my certificate**.
  5. Paste in your certificate or click **Upload** to navigate to your certificate file.   
You can choose to include the CA certificate chain in the same file as the certificate. Google Cloud does not validate the certificate chain for you – validation is your responsibility.
  6. Paste in your private key or click **Upload** to navigate to your private key file.
  7. Click **Create**.



###  gcloud 

To create a global SSL certificate, use the [`gcloud compute ssl-certificates create`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/ssl-certificates/create) command with the `--global` flag:
    
    
    gcloud compute ssl-certificates create CERTIFICATE_NAME \
        --certificate=CERTIFICATE_FILE \
        --private-key=PRIVATE_KEY_FILE \
        --global
    

To create a regional SSL certificate, use the [`gcloud compute ssl-certificates create`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/ssl-certificates/create) command with the `--region` flag:
    
    
    gcloud compute ssl-certificates create CERTIFICATE_NAME \
        --certificate=CERTIFICATE_FILE \
        --private-key=PRIVATE_KEY_FILE \
        --region=REGION
    

Replace the following:

  * CERTIFICATE_NAME: the name of the certificate resource to create
  * CERTIFICATE_FILE: the path to a PEM-formatted certificate file

You can choose to include the CA certificate chain in the same file as the certificate. Google Cloud does not validate the certificate chain for you—validation is your responsibility.

  * PRIVATE_KEY_FILE: the path to a PEM-formatted private key; the private key cannot be protected by a passphrase

  * REGION: if applicable, the region for the regional SSL certificate

If this certificate resource is for either an internal Application Load Balancer or a regional external Application Load Balancer, the region must be the same as the region of the load balancer.




###  Java 

To use the API methods, you must first read the certificate and private key files, and then create the SSL certificate. This is because the API request must include the contents of the files.

The following example shows you how to do this with Java.

For global SSL certificates, use the [sslCertificates.insert](https://docs.cloud.google.com/compute/docs/reference/rest/v1/sslCertificates/insert) API method:
    
    
    import com.google.cloud.compute.v1.[InsertSslCertificateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertSslCertificateRequest.html);
    import com.google.cloud.compute.v1.[SslCertificate](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SslCertificate.html);
    import com.google.cloud.compute.v1.[SslCertificatesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SslCertificatesClient.html);
    import java.io.IOException;
    import java.util.concurrent.ExecutionException;
    import java.util.concurrent.TimeUnit;
    import java.util.concurrent.TimeoutException;
    
    public class CreateCertificate {
    
      public static void main(String[] args)
              throws IOException, InterruptedException, ExecutionException, TimeoutException {
        // TODO(developer): Replace these variables before running the sample.
        // Project ID or project number of the Google Cloud project you want to use.
        String project = "your-project-id";
        // The certificate you want to create in your project.
        String certificate = "your-certificate";
        // The private key you used to sign the certificate with.
        String privateKey = "your-private-key";
        // Name for the certificate once it's created in your project.
        String certificateName = "your-certificate-name";
    
        createCertificate(project, certificate, privateKey, certificateName);
      }
    
      // Create a global SSL self-signed certificate within your Google Cloud project.
      public static [SslCertificate](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SslCertificate.html) createCertificate(String project, String certificate,
                                                     String privateKey, String certificateName)
              throws IOException, ExecutionException, InterruptedException, TimeoutException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests.
        try ([SslCertificatesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SslCertificatesClient.html) client = [SslCertificatesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SslCertificatesClient.html).create()) {
          [SslCertificate](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SslCertificate.html) certificateResource = [SslCertificate](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SslCertificate.html).newBuilder()
                  .setCertificate(certificate)
                  .setPrivateKey(privateKey)
                  .setName(certificateName)
                  .build();
    
          [InsertSslCertificateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertSslCertificateRequest.html) request = [InsertSslCertificateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertSslCertificateRequest.html).newBuilder()
                  .setProject(project)
                  .setSslCertificateResource(certificateResource)
                  .build();
    
          client.insertCallable().futureCall(request).get(60, TimeUnit.SECONDS);
    
          // Wait for server update
          TimeUnit.SECONDS.sleep(1);
    
          [SslCertificate](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SslCertificate.html) sslCert = client.get(project, certificateName);
    
          System.out.printf("Certificate '%s' has been created successfully", sslCert.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SslCertificate.html#com_google_cloud_compute_v1_SslCertificate_getName__)());
    
          return sslCert;
        }
      }
    }

For regional SSL certificates, use the [regionSslCertificates.insert](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionSslCertificates/insert) API method:
    
    
    import com.google.cloud.compute.v1.[InsertRegionSslCertificateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertRegionSslCertificateRequest.html);
    import com.google.cloud.compute.v1.[RegionSslCertificatesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionSslCertificatesClient.html);
    import com.google.cloud.compute.v1.[SslCertificate](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SslCertificate.html);
    import java.io.IOException;
    import java.util.concurrent.ExecutionException;
    import java.util.concurrent.TimeUnit;
    import java.util.concurrent.TimeoutException;
    
    public class CreateRegionalCertificate {
      public static void main(String[] args)
              throws IOException, InterruptedException, ExecutionException, TimeoutException {
        // TODO(developer): Replace these variables before running the sample.
        // Project ID or project number of the Google Cloud project you want to use.
        String project = "your-project-id";
        // The certificate you want to create in your project.
        String certificate = "your-certificate";
        // The private key you used to sign the certificate with.
        String privateKey = "your-private-key";
        // Name for the certificate once it's created in your project.
        String certificateName = "your-certificate-name";
        // Name of the region you want to use.
        String region = "your-region";
    
        createRegionCertificate(project, certificate, region, privateKey, certificateName);
      }
    
      // Create a regional SSL self-signed certificate within your Google Cloud project.
      public static [SslCertificate](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SslCertificate.html) createRegionCertificate(String project, String certificate,
                                                           String region, String privateKey,
                                                           String certificateName)
              throws IOException, ExecutionException, InterruptedException, TimeoutException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests.
        try ([RegionSslCertificatesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionSslCertificatesClient.html) client = [RegionSslCertificatesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionSslCertificatesClient.html).create()) {
          [SslCertificate](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SslCertificate.html) certificateResource = [SslCertificate](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SslCertificate.html).newBuilder()
                  .setCertificate(certificate)
                  .setPrivateKey(privateKey)
                  .setName(certificateName)
                  .build();
    
          [InsertRegionSslCertificateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertRegionSslCertificateRequest.html) request = [InsertRegionSslCertificateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertRegionSslCertificateRequest.html).newBuilder()
                  .setProject(project)
                  .setRegion(region)
                  .setSslCertificateResource(certificateResource)
                  .build();
    
          client.insertCallable().futureCall(request).get(60, TimeUnit.SECONDS);
    
          // Wait for server update
          TimeUnit.SECONDS.sleep(1);
    
          [SslCertificate](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SslCertificate.html) sslCert = client.get(project, region, certificateName);
    
          System.out.printf("Regional cert '%s' has been created successfully", sslCert.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SslCertificate.html#com_google_cloud_compute_v1_SslCertificate_getName__)());
    
          return sslCert;
        }
      }
    }

For additional code samples, see the [API reference page](https://docs.cloud.google.com/compute/docs/reference/rest/v1/sslCertificates/insert#examples).

###  Python 

To use the API methods, you must first read the certificate and private key files, and then create the SSL certificate. This is because the API request must include the contents of the files.

The following examples show how to do this with Python.

For global SSL certificates, use the [sslCertificates.insert](https://docs.cloud.google.com/compute/docs/reference/rest/v1/sslCertificates/insert) API method:
    
    
    from pathlib import Path
    from pprint import pprint
    from typing import Union
    
    from googleapiclient import discovery
    
    
    def create_certificate(
        project_id: str,
        certificate_file: Union[str, Path],
        private_key_file: Union[str, Path],
        certificate_name: str,
        description: str = "Certificate created from a code sample.",
    ) -> dict:
        """
        Create a global SSL self-signed certificate within your Google Cloud project.
    
        Args:
            project_id: project ID or project number of the Cloud project you want to use.
            certificate_file: path to the file with the certificate you want to create in your project.
            private_key_file: path to the private key you used to sign the certificate with.
            certificate_name: name for the certificate once it's created in your project.
            description: description of the certificate.
    
        Returns:
            Dictionary with information about the new global SSL self-signed certificate.
        """
        service = discovery.build("compute", "v1")
    
        # Read the cert into memory
        with open(certificate_file) as f:
            _temp_cert = f.read()
    
        # Read the private_key into memory
        with open(private_key_file) as f:
            _temp_key = f.read()
    
        # Now that the certificate and private key are in memory, you can create the
        # certificate resource
        ssl_certificate_body = {
            "name": certificate_name,
            "description": description,
            "certificate": _temp_cert,
            "privateKey": _temp_key,
        }
        request = service.sslCertificates().insert(
            project=project_id, body=ssl_certificate_body
        )
        response = request.execute()
        pprint(response)
        return response
    
    

For regional SSL certificates, use the [regionSslCertificates.insert](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionSslCertificates/insert) API method:
    
    
    from pathlib import Path
    from pprint import pprint
    from typing import Union
    
    from googleapiclient import discovery
    
    
    def create_regional_certificate(
        project_id: str,
        region: str,
        certificate_file: Union[str, Path],
        private_key_file: Union[str, Path],
        certificate_name: str,
        description: str = "Certificate created from a code sample.",
    ) -> dict:
        """
        Create a regional SSL self-signed certificate within your Google Cloud project.
    
        Args:
            project_id: project ID or project number of the Cloud project you want to use.
            region: name of the region you want to use.
            certificate_file: path to the file with the certificate you want to create in your project.
            private_key_file: path to the private key you used to sign the certificate with.
            certificate_name: name for the certificate once it's created in your project.
            description: description of the certificate.
    
            Returns:
            Dictionary with information about the new regional SSL self-signed certificate.
        """
        service = discovery.build("compute", "v1")
    
        # Read the cert into memory
        with open(certificate_file) as f:
            _temp_cert = f.read()
    
        # Read the private_key into memory
        with open(private_key_file) as f:
            _temp_key = f.read()
    
        # Now that the certificate and private key are in memory, you can create the
        # certificate resource
        ssl_certificate_body = {
            "name": certificate_name,
            "description": description,
            "certificate": _temp_cert,
            "privateKey": _temp_key,
        }
        request = service.regionSslCertificates().insert(
            project=project_id, region=region, body=ssl_certificate_body
        )
        response = request.execute()
        pprint(response)
    
        return response
    
    

For additional code samples, see the [API reference page](https://docs.cloud.google.com/compute/docs/reference/rest/v1/sslCertificates/insert#examples).

## Step 3: Associate an SSL certificate with a target proxy

You must associate at least one SSL certificate with each target HTTPS or SSL proxy. You can configure the target proxy with up to [the maximum number of SSL certificates per target HTTPS or target SSL proxy](https://docs.cloud.google.com/load-balancing/docs/quotas#target_pools_and_target_proxies). You can reference multiple self-managed certificates on the same target proxy.

**Note:** When replacing an existing SSL certificate, first create the replacement SSL certificate and associate it with the load balancer's target proxy before you delete the old SSL certificate.

###  Console 

When you use the Google Cloud console to edit an existing load balancer, you automatically associate the SSL certificate with the appropriate target proxy.

###  gcloud 

To associate a global SSL certificate with a target HTTPS proxy, use the [`gcloud compute target-https-proxies update`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/target-https-proxies/update) command with the `--global` and `--global-ssl-certificates` flags:
    
    
    gcloud compute target-https-proxies update TARGET_PROXY_NAME \
        --global \
        --ssl-certificates=SSL_CERTIFICATE_LIST \
        --global-ssl-certificates
    

To associate a global SSL certificate with a target SSL proxy, use the [`gcloud compute target-ssl-proxies update`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/target-ssl-proxies/update) command:
    
    
    gcloud compute target-ssl-proxies update TARGET_PROXY_NAME \
        --ssl-certificates=SSL_CERTIFICATE_LIST
    

To associate a regional SSL certificate with a target HTTPS proxy, use the [`gcloud compute target-https-proxies update`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/target-https-proxies/update) command with the `--region` and `--ssl-certificates-region` flags:
    
    
    gcloud compute target-https-proxies update TARGET_PROXY_NAME \
        --region=REGION \
        --ssl-certificates=SSL_CERTIFICATE_LIST \
        --ssl-certificates-region=REGION
    

Replace the following:

  * `TARGET_PROXY_NAME`: the name of the load balancer's target proxy
  * `REGION` (if applicable): the region for the regional target proxy and regional SSL certificate; the regions must match
  * `SSL_CERTIFICATE_LIST`: a comma-delimited list of Google Cloud SSL certificate names

Make sure that the list of referenced certificates includes all older valid SSL certificates as well as the new SSL certificate. The `gcloud compute target-ssl-proxies update` command overrides the original values for `--ssl-certificates` with the new value.




###  API 

To associate a global SSL certificate with a target HTTPS proxy, make a `POST` request to the [`targetHttpsProxies.insert`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/targetHttpsProxies/insert) method, replacing `PROJECT_ID` with your project ID.
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/targetHttpsProxy
    
    {
    "name": "l7-xlb-proxy",
    "urlMap": "projects/PROJECT_ID/global/urlMaps/l7-xlb-map",
    "sslCertificates": /projectsPROJECT_IDglobal/sslCertificates/SSL_CERT_NAME
    }
    

To associate a global SSL certificate with a target HTTPS proxy, make a `POST` request to the [`targetSslProxies.insert`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/targetSslProxies/insert) method, replacing `PROJECT_ID` with your project ID.
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/targetSslProxy
    
    {
    "name": "l7-ssl-proxy",
    "sslCertificates": /projectsPROJECT_IDglobal/sslCertificates/SSL_CERT_NAME
    }
    

To associate a regional SSL certificate with a target HTTPS proxy, make a `POST` request to the [`targetHttpsProxies.insert`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/targetHttpsProxies/insert) method, replacing `PROJECT_ID` with your project ID.
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/targetHttpsProxy
    
    {
    "name": "l7-xlb-proxy",
    "urlMap": "projects/PROJECT_ID/global/urlMaps/l7-ilb-map",
    "region": "us-west1"
    "sslCertificates": /projectsPROJECT_IDregions/us-west1/sslCertificates/SSL_CERT_NAME
    }
    

## Step 4: Update the DNS A and AAAA records to point to the load balancer's IP address

At your registrar's site, DNS host, or ISP (wherever your DNS records are managed), add or update the DNS A records (for IPv4) and DNS AAAA records (for IPv6) for your domains and any subdomains so that they point to the IP address associated with the load balancer's forwarding rule or rules.

If you're using [Cloud DNS](https://docs.cloud.google.com/dns/docs) and [Cloud Domains](https://docs.cloud.google.com/domains/docs), [set up your domains](https://docs.cloud.google.com/dns/docs/tutorials/create-domain-tutorial#set-up-domain) and [update your name servers](https://docs.cloud.google.com/dns/docs/tutorials/create-domain-tutorial#update-nameservers).

If you're using multiple domains for a single certificate, you must add or update DNS records for all of the domains and any subdomains so that they all point to your load balancer's IP address.

**Important:** Make sure that your domain name resolves directly to the IP address of your external Application Load Balancer. It cannot resolve to any other IP address, even if that other IP address passes, proxies, or caches responses for your load balancer. For example, you cannot use self-managed certificates if your domain name resolves to the external IP address of a third-party CDN provider.

After waiting for [DNS propagation to complete](https://docs.cloud.google.com/dns/docs/overview#performance_and_timing), you can verify your setup by running the `dig` command. For example, suppose your domain is `www.example.com`. Run the following `dig` command:
    
    
    dig www.example.com
    
    
    
    ; <<>> DiG 9.10.6 <<>> www.example.com
    ;; global options: +cmd
    ;; Got answer:
    ;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 31748
    ;; flags: qr rd ra; QUERY: 1, ANSWER: 4, AUTHORITY: 0, ADDITIONAL: 1
    
    ;; OPT PSEUDOSECTION:
    ; EDNS: version: 0, flags:; udp: 512
    ;; QUESTION SECTION:
    ;www.example.com.           IN  A
    
    ;; ANSWER SECTION:
    www.example.com.        1742    IN  CNAME   www.example.com.edgekey.net.
    www.example.com.edgekey.net. 21330 IN   CNAME   www.example.com.edgekey.net.globalredir.akadns.net.
    www.example.com.edgekey.net.globalredir.akadns.net. 3356 IN CNAME   e6858.dsce9.akamaiedge.net.
    e6858.dsce9.akamaiedge.net. 19  IN  A   203.0.113.5
    
    ;; Query time: 43 msec
    ;; SERVER: 8.8.8.8#53(8.8.8.8)
    ;; WHEN: Wed Jun 03 16:54:44 PDT 2020
    ;; MSG SIZE  rcvd: 193
    
    

In this example, `203.0.113.5` is your load balancer's IP address.

## Step 5: Test with OpenSSL

It can take up to 30 minutes for your load balancer to begin using your self-managed SSL certificate.

To test, run the following OpenSSL command, replacing DOMAIN with your DNS name and IP_ADDRESS with the IP address of your load balancer.
    
    
    echo | openssl s_client -showcerts -servername DOMAIN -connect IP_ADDRESS:443 -verify 99 -verify_return_error
    

This command outputs the certificates that the load balancer presents to the client. Along with other detailed information, the output should include the certificate chain and `Verify return code: 0 (ok)`.

## Work with self-managed SSL certificates

The following sections describe how to list, view, delete, and replace SSL certificate resources.

### List SSL certificates

###  Console 

You can check the status of your global SSL certificates on the **Classic Certificates** tab on the **Certificate Manager** page. Regional SSL certificates cannot be maintained in the Google Cloud console. Use either `gcloud` or the REST API.

  1. Go to the Classic Certificates tab in the Google Cloud console.   
[Go to Classic Certificates](https://console.cloud.google.com/security/ccm/list/lbCertificates)
  2. (Optional) Filter the list of SSL certificates.



###  gcloud 

To list global SSL certificates, use the [`gcloud compute ssl-certificates list`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/ssl-certificates/list) command with the `--global` flag:
    
    
    gcloud compute ssl-certificates list \
       --global
    

To list regional SSL certificates, use the [`gcloud compute ssl-certificates list`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/ssl-certificates/list) command with the `region` filter:
    
    
    gcloud compute ssl-certificates list \
       --filter="region:(REGION ...)"
    

Replace the following:

  * REGION: a Google Cloud region; include multiple regions as a space-separated list



### Describe SSL certificates

###  Console 

You can view additional details about your global SSL certificates on the **Classic Certificates** tab on the **Certificate Manager** page.

  1. Go to the Classic Certificates page in the Google Cloud console.   
[Go to Classic Certificates](https://console.cloud.google.com/security/ccm/list/lbCertificates)
  2. (Optional) Filter the list of SSL certificates.
  3. To view more details, click the certificate name.



###  gcloud 

To describe a global SSL certificate, use the [`gcloud compute ssl-certificates describe`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/ssl-certificates/describe) command with the `--global` flag:
    
    
    gcloud  compute ssl-certificates describe CERTIFICATE_NAME \
       --global
    

To describe a regional SSL certificate, use the [`gcloud compute ssl-certificates describe`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/ssl-certificates/describe) command with the `--region` flag:
    
    
    gcloud compute ssl-certificates describe CERTIFICATE_NAME \
       --region=REGION
    

Replace the following:

  * CERTIFICATE_NAME: the name of the SSL certificate
  * REGION: a Google Cloud region



**Note:** Google Cloud never returns the contents of a private key when describing an existing certificate. The private key is stored securely and cannot be retrieved using the Google Cloud console, `gcloud`, or the API.

### Delete SSL certificates

Before you can delete an SSL certificate, you must first update each target proxy that references the certificate. For each target proxy, run the appropriate `gcloud update` command to update the target proxy's SSL_CERTIFICATE_LIST such that it no longer includes the SSL certificate that you need to delete. Each target SSL proxy or target HTTPS proxy must reference at least one SSL certificate.

**Note:** To understand the sequence of events that you must follow if you plan to replace an SSL certificate, see Replace or renew an SSL certificate before it expires.

After you update the target proxy, you can delete the SSL certificate.

###  Console 

You can delete global SSL certificates on the **Classic Certificates** tab on the **Certificate Manager** page.

  1. Go to the Classic Certificates tab in the Google Cloud console.   
[Go to Classic Certificates](https://console.cloud.google.com/security/ccm/list/lbCertificates)
  2. Select the SSL certificate that you want to delete.
  3. Click delete**Delete**.
  4. To confirm, click delete**Delete** again.



###  gcloud 

To delete a global SSL certificate, use the [`gcloud compute ssl-certificates delete`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/ssl-certificates/delete) command with the `--global` command:
    
    
    gcloud compute ssl-certificates delete CERTIFICATE_NAME \
        --global
    

To delete a regional SSL certificate, use the [`gcloud compute ssl-certificates delete`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/ssl-certificates/delete) command with the `--region` command:
    
    
    gcloud compute ssl-certificates delete CERTIFICATE_NAME \
        --region=REGION
    

Replace the following:

  * CERTIFICATE_NAME: the name of the SSL certificate
  * REGION: a Google Cloud region



### Replace or renew an SSL certificate before it expires

Follow these steps if you need to replace, renew, or rotate an SSL certificate without service downtime:

  1. Run the [`gcloud compute ssl-certificates describe`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/ssl-certificates/describe) command for the current certificate, to check if it's about to expire.

  2. Create a new SSL certificate resource. The new SSL certificate must have a unique name within the project.

  3. Update the target proxy to detach the old SSL certificate and add the new one. Make sure to include any other existing SSL certificates that you want to retain.

To help avoid downtime, run a single `gcloud` command with the `--ssl-certificates` flag. For example:

**For global external Application Load Balancers:**

Use the [`gcloud compute target-https-proxies update`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/target-https-proxies/update#--ssl-certificates) command with the `--global` flag.
         
         gcloud compute target-https-proxies update TARGET_PROXY_NAME \
            --global \
            --ssl-certificates=new-ssl-cert,other-certificates \
            --global-ssl-certificates
         

**For regional external Application Load Balancers and regional internal Application Load Balancers:**

Use the [`gcloud compute target-https-proxies update`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/target-https-proxies/update#--ssl-certificates) command with the `--region` flag.
         
         gcloud compute target-https-proxies update TARGET_PROXY_NAME \
            --region=REGION \
            --ssl-certificates=new-ssl-cert,other-certificates \
            --ssl-certificates-region=REGION
         

**For external proxy Network Load Balancers:**

Use the [`gcloud compute target-ssl-proxies update`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/target-ssl-proxies/update#--ssl-certificates) command with the `--backend-service` flag.
         
         gcloud compute target-ssl-proxies update TARGET_PROXY_NAME \
            --ssl-certificates=new-ssl-cert,other-certificates
         

  4. Verify that the load balancer is serving the replacement certificate by running the following OpenSSL command:
         
         echo | openssl s_client -showcerts -connect IP_ADDRESS:443 -verify 99 -verify_return_error
         

**Note:** If multiple certificates match the SNI hostname that is specified by the client, the load balancer might select a certificate other than the primary certificate (the first certificate in the list). For details, see [Multiple SSL certificates](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates#multiplessl).
  5. Wait 15 minutes to ensure that the replacement operation has propagated to all Google Front Ends (GFEs).

  6. (Optional) Delete the old SSL certificate.




### Rotate SSL certificates periodically

This [sample solution](https://github.com/GoogleCloudPlatform/cas-gclb-rotation) periodically checks the status of certificates used with Google Cloud load balancers and rotates certificates when they reach a given percentage of their lifetime. The tool uses CAs configured by using the [Certificate Authority Service](https://docs.cloud.google.com/certificate-authority-service/docs).

This solution works with the following load balancers:

  * Global external Application Load Balancer
  * Classic Application Load Balancer
  * Regional external Application Load Balancer
  * Internal Application Load Balancer
  * External proxy Network Load Balancer with an SSL proxy

**Important:** This solution is not an official product and is not supported by Google, but is a sample provided for your reference.

## What's next

  * To troubleshoot SSL certificates, see [Troubleshooting SSL certificates](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates/troubleshooting).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
