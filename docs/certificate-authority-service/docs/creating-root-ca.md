---
url: https://docs.cloud.google.com/certificate-authority-service/docs/creating-root-ca/
title: Create a root CA \u00a0|\u00a0 Certificate Authority Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:23:58.652885+00:00
---

# Create a root CA  |  Certificate Authority Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/certificate-authority-service/docs/creating-root-ca/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Certificate Authority Service ](https://docs.cloud.google.com/certificate-authority-service/docs)
  * [ Guides ](https://docs.cloud.google.com/certificate-authority-service/docs/ca-service-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Create a root CA

This page describes how to create a root certificate authority (CA) in a CA pool.

A root CA is at the top of a public key infrastructure (PKI) hierarchy and is responsible for forming the _trust anchor_ of the PKI. To properly participate and use certificates in a PKI, a device, software, or component needs to trust the PKI. This is accomplished by configuring the device, software, or component to trust the root CA. As a result, all the certificates issued by the root CA are trusted.

## Before you begin

  * Make sure you have the CA Service Operation Manager (`roles/privateca.caManager`) or the CA Service Admin (`roles/privateca.admin`) IAM role. For information, see [Configure IAM policies](https://docs.cloud.google.com/certificate-authority-service/docs/configuring-iam).
  * If you use an existing Cloud Key Management Service key to sign certificates that the CA issues, you must grant the necessary IAM roles to the [CA Service Agent](https://docs.cloud.google.com/iam/docs/service-agents#private-ca-service-account) on that Cloud Key Management Service key. For more information about the specific roles required and instructions, see [Using the CA Service Agent](https://docs.cloud.google.com/certificate-authority-service/docs/access-control#service-agent).

  * [Create a CA pool](https://docs.cloud.google.com/certificate-authority-service/docs/creating-ca-pool).

  * [Determine your CA settings](https://docs.cloud.google.com/certificate-authority-service/docs/certificate-authority-settings).




## Create a root CA

A root CA has a self-signed certificate that you must distribute to the trust stores of your clients. The root CA's certificate is at the top of the _certificate chain_. No other CA can revoke the CA certificate. The CRL of the root CA applies only to the other certificates the root CA issued, but not to itself.

You can create a root CA either in an existing CA pool or a new CA pool. The following instructions use an existing pool.

### Console

To create a root CA in an existing CA pool, do the following:

  1. Go to the **Certificate Authority Service** page in the Google Cloud console.

[Go to Certificate Authority Service](https://console.cloud.google.com/security/cas)

  2. Click the **CA manager** tab.

**Note:** You can't create more than one CA inside a CA pool using the **CA manager** tab.
  3. Click the **Create CA** arrow_drop_down expander arrow, and then select **Create CA in an existing CA pool**.




**Select CA pool**

Select an existing CA pool from the list and click **Continue**.

**Select CA type**

  1. Under **Type** , select **Root CA**.
  2. In the **Valid for** field, enter the duration that you want the certificates issued by the root CA to be valid for.
  3. Under **Initialized state** , select the operational state to create the CA in.
  4. Click **Continue**.

**Configure CA subject name**

  1. Optional: In the **Organization (O)** field, enter the name of your company. 
  2. Optional: In the **Organization unit (OU)** field, enter the company subdivision or business unit. 
  3. Optional: In the **Country name (C)** field, enter a two letter country code. 
  4. Optional: In the **State or province name** field, enter the name of your state. 
  5. Optional: In the **Locality name** field, enter the name of your city. 
  6. In the **CA common name (CN)** field, enter the CA name. 
  7. Click **Continue**. 

**Configure CA key size and algorithm**

  1. Choose the key algorithm that best meets your needs. For more details on signing key options, see [Configure CA signing keys](https://docs.cloud.google.com/certificate-authority-service/docs/choosing-key-algorithm). 
  2. To use a customer-managed signing key, select **Customer-managed key** and provide the Cloud Key Management Service crypto key version. 
  3. Click **Continue**. 

**Configure CA artifacts**

  1. Choose whether you want to use a Google-managed or a customer-managed Cloud Storage bucket. 
     1. For a Google-managed Cloud Storage bucket, CA Service creates a Google-managed bucket in the same location as the CA. 
     2. For a customer-managed Cloud Storage bucket, click Browse and select one of the existing Cloud Storage buckets. 
  2. Click **Continue**. 

**Add labels**

The following steps are optional. 

If you want to add labels to the CA, do the following: 

  1. Click add**Add item**. 
  2. In the **Key 1** field, enter the label key. 
  3. In the **Value 1** field, enter the label value. 
  4. If you want to add another label, click add**Add item**. Then, add the label key and value as mentioned in steps 2 and 3. 
  5. Click **Continue**. 

**Review the settings**

Carefully review all the settings, then click **Done** to create the CA. 

### gcloud

  1. To create a new root CA in an existing CA pool, run the following command:
         
         gcloud privateca roots create ROOT_CA_ID \
             --location=LOCATION \
             --pool=POOL_ID \
             --key-algorithm=KEY_ALGORITHM \
             --subject="CN=my-ca, O=Test LLC"
         

Replace the following:

     * ROOT_CA_ID: the name of the CA
     * LOCATION: the location of the CA pool
     * POOL_ID: the name of the CA pool
     * KEY_ALGORITHM: the algorithm to use for creating a Cloud KMS key. This flag is optional. If you don't include this flag, the key algorithm defaults to `rsa-pkcs1-4096-sha256`. For more information, see [\--key-algorithm flag](https://docs.cloud.google.com/sdk/gcloud/reference/privateca/roots/create#--key-algorithm).

By default, the CA is created in the `STAGED` state. To enable a CA by default, include the `--auto-enable` flag.

If you want to use a customer-managed Cloud Storage bucket for publishing CA certificates and CRLs, add `--bucket bucket-name` to the command. Replace bucket-name with the name of the Cloud Storage bucket.

To specify custom Authority Information Access (AIA) and CRL Distribution Point (CDP) access URLs, use the `--custom-aia-urls` and `--custom-cdp-urls` flags. If specified, these URLs are included in all certificates issued by the CA and supersede the default Cloud Storage bucket access URLs.

To create a root CA using a customer-managed signing key, run the following command:
    
    gcloud privateca roots create ROOT_CA_ID \
        --location=LOCATION \
        --pool=POOL_ID \
        --kms-key-version=KMS_KEY_VERSION \
        --subject="CN=my-ca, O=Test LLC"
    

Replace the following:

     * ROOT_CA_ID: the unique identifier of the root CA
     * LOCATION: the location of the CA pool
     * POOL_ID: the name of the CA pool
     * KMS_KEY_VERSION: the full resource ID of a customer-managed Cloud KMS crypto key version to use as the signing key

For more details on signing key options and preparing a customer-managed signing key, see [Configure CA signing keys](https://docs.cloud.google.com/certificate-authority-service/docs/choosing-key-algorithm).

To see the exhaustive list of settings, run the following command:
    
    gcloud privateca roots create --help
    




### Terraform

To create a root CA using a Google-owned and Google-managed encryption key, use the following sample configuration:
    
    
    resource "google_privateca_certificate_authority" "root_ca" {
      // This example assumes this pool already exists.
      // Pools cannot be deleted in normal test circumstances, so we depend on static pools
      pool                                   = "my-pool"
      certificate_authority_id               = "my-certificate-authority-root"
      location                               = "us-central1"
      deletion_protection                    = false # set to true to prevent destruction of the resource
      ignore_active_certificates_on_deletion = true
      config {
        subject_config {
          subject {
            organization = "ACME"
            common_name  = "my-certificate-authority"
          }
        }
        x509_config {
          ca_options {
            # is_ca *MUST* be true for certificate authorities
            is_ca = true
          }
          key_usage {
            base_key_usage {
              # cert_sign and crl_sign *MUST* be true for certificate authorities
              cert_sign = true
              crl_sign  = true
            }
            extended_key_usage {
            }
          }
        }
      }
      key_spec {
        algorithm = "RSA_PKCS1_4096_SHA256"
      }
      // valid for 10 years
      lifetime = "${10 * 365 * 24 * 3600}s"
    }

To create a root CA using a self-managed key, use the following sample configuration:
    
    
    resource "google_project_service_identity" "privateca_sa" {
      provider = google-beta
      service  = "privateca.googleapis.com"
    }
    
    resource "google_kms_crypto_key_iam_binding" "privateca_sa_keyuser_signerverifier" {
      crypto_key_id = "projects/keys-project/locations/us-central1/keyRings/key-ring/cryptoKeys/crypto-key"
      role          = "roles/cloudkms.signerVerifier"
    
      members = [
        "serviceAccount:${google_project_service_identity.privateca_sa.email}",
      ]
    }
    
    resource "google_kms_crypto_key_iam_binding" "privateca_sa_keyuser_viewer" {
      crypto_key_id = "projects/keys-project/locations/us-central1/keyRings/key-ring/cryptoKeys/crypto-key"
      role          = "roles/viewer"
      members = [
        "serviceAccount:${google_project_service_identity.privateca_sa.email}",
      ]
    }
    
    resource "google_privateca_certificate_authority" "default" {
      // This example assumes this pool already exists.
      // Pools cannot be deleted in normal test circumstances, so we depend on static pools
      pool                     = "ca-pool"
      certificate_authority_id = "my-certificate-authority"
      location                 = "us-central1"
      deletion_protection      = false # set to true to prevent destruction of the resource
      key_spec {
        cloud_kms_key_version = "projects/keys-project/locations/us-central1/keyRings/key-ring/cryptoKeys/crypto-key/cryptoKeyVersions/1"
      }
    
      config {
        subject_config {
          subject {
            organization = "Example, Org."
            common_name  = "Example Authority"
          }
        }
        x509_config {
          ca_options {
            # is_ca *MUST* be true for certificate authorities
            is_ca                  = true
            max_issuer_path_length = 10
          }
          key_usage {
            base_key_usage {
              # cert_sign and crl_sign *MUST* be true for certificate authorities
              cert_sign = true
              crl_sign  = true
            }
            extended_key_usage {
              server_auth = false
            }
          }
        }
      }
    
      depends_on = [
        google_kms_crypto_key_iam_binding.privateca_sa_keyuser_signerverifier,
        google_kms_crypto_key_iam_binding.privateca_sa_keyuser_viewer,
      ]
    }

###  Go 

To authenticate to CA Service, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	privateca "cloud.google.com/go/security/privateca/apiv1"
    	"cloud.google.com/go/security/privateca/apiv1/privatecapb"
    	"google.golang.org/protobuf/types/known/durationpb"
    )
    
    // Create Certificate Authority which is the root CA in the given CA Pool. This CA will be
    // responsible for signing certificates within this pool.
    func createCa(
    	w io.Writer,
    	projectId string,
    	location string,
    	caPoolId string,
    	caId string,
    	caCommonName string,
    	org string,
    	caDuration int64) error {
    	// projectId := "your_project_id"
    	// location := "us-central1"		// For a list of locations, see: https://cloud.google.com/certificate-authority-service/docs/locations.
    	// caPoolId := "ca-pool-id"			// The CA Pool id under which the CA should be created.
    	// caId := "ca-id"					// A unique id/name for the ca.
    	// caCommonName := "ca-name"		// A common name for your certificate authority.
    	// org := "ca-org"					// The name of your company for your certificate authority.
    	// ca_duration := int64(31536000)	// The validity of the certificate authority in seconds.
    
    	ctx := context.Background()
    	caClient, err := privateca.[NewCertificateAuthorityClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/security/latest/privateca/apiv1.html#cloud_google_com_go_security_privateca_apiv1_CertificateAuthorityClient_NewCertificateAuthorityClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("NewCertificateAuthorityClient creation failed: %w", err)
    	}
    	defer caClient.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/security/latest/privateca/apiv1.html#cloud_google_com_go_security_privateca_apiv1_CertificateAuthorityClient_Close)()
    
    	// Set the types of Algorithm used to create a cloud KMS key.
    	keySpec := &privatecapb.CertificateAuthority_KeyVersionSpec{
    		KeyVersion: &privatecapb.CertificateAuthority_KeyVersionSpec_Algorithm{
    			Algorithm: privatecapb.[CertificateAuthority_RSA_PKCS1_2048_SHA256](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/security/latest/privateca/apiv1/privatecapb.html#cloud_google_com_go_security_privateca_apiv1_privatecapb_CertificateAuthority_SIGN_HASH_ALGORITHM_UNSPECIFIED_CertificateAuthority_RSA_PSS_2048_SHA256_CertificateAuthority_RSA_PSS_3072_SHA256_CertificateAuthority_RSA_PSS_4096_SHA256_CertificateAuthority_RSA_PKCS1_2048_SHA256_CertificateAuthority_RSA_PKCS1_3072_SHA256_CertificateAuthority_RSA_PKCS1_4096_SHA256_CertificateAuthority_EC_P256_SHA256_CertificateAuthority_EC_P384_SHA384),
    		},
    	}
    
    	// Set CA subject config.
    	subjectConfig := &privatecapb.CertificateConfig_SubjectConfig{
    		Subject: &privatecapb.Subject{
    			CommonName:   caCommonName,
    			Organization: org,
    		},
    	}
    
    	// Set the key usage options for X.509 fields.
    	isCa := true
    	x509Parameters := &privatecapb.X509Parameters{
    		KeyUsage: &privatecapb.KeyUsage{
    			BaseKeyUsage: &privatecapb.KeyUsage_KeyUsageOptions{
    				CrlSign:  true,
    				CertSign: true,
    			},
    		},
    		CaOptions: &privatecapb.X509Parameters_CaOptions{
    			IsCa: &isCa,
    		},
    	}
    
    	// Set certificate authority settings.
    	// Type: SELF_SIGNED denotes that this CA is a root CA.
    	ca := &privatecapb.CertificateAuthority{
    		Type:    privatecapb.[CertificateAuthority_SELF_SIGNED](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/security/latest/privateca/apiv1/privatecapb.html#cloud_google_com_go_security_privateca_apiv1_privatecapb_CertificateAuthority_TYPE_UNSPECIFIED_CertificateAuthority_SELF_SIGNED_CertificateAuthority_SUBORDINATE),
    		KeySpec: keySpec,
    		Config: &privatecapb.CertificateConfig{
    			SubjectConfig: subjectConfig,
    			X509Config:    x509Parameters,
    		},
    		Lifetime: &durationpb.Duration{
    			Seconds: caDuration,
    		},
    	}
    
    	fullCaPoolName := fmt.Sprintf("projects/%s/locations/%s/caPools/%s", projectId, location, caPoolId)
    
    	// Create the CreateCertificateAuthorityRequest.
    	// See https://pkg.go.dev/cloud.google.com/go/security/privateca/apiv1/privatecapb#CreateCertificateAuthorityRequest.
    	req := &privatecapb.CreateCertificateAuthorityRequest{
    		Parent:                 fullCaPoolName,
    		CertificateAuthorityId: caId,
    		CertificateAuthority:   ca,
    	}
    
    	op, err := caClient.CreateCertificateAuthority(ctx, req)
    	if err != nil {
    		return fmt.Errorf("CreateCertificateAuthority failed: %w", err)
    	}
    
    	if _, err = op.Wait(ctx); err != nil {
    		return fmt.Errorf("CreateCertificateAuthority failed during wait: %w", err)
    	}
    
    	fmt.Fprintf(w, "CA %s created", caId)
    
    	return nil
    }
    

###  Java 

To authenticate to CA Service, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.api.core.[ApiFuture](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.ApiFuture.html);
    import com.google.cloud.security.privateca.v1.[CaPoolName](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CaPoolName.html);
    import com.google.cloud.security.privateca.v1.[CertificateAuthority](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateAuthority.html);
    import com.google.cloud.security.privateca.v1.[CertificateAuthority](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateAuthority.html).[KeyVersionSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateAuthority.KeyVersionSpec.html);
    import com.google.cloud.security.privateca.v1.[CertificateAuthority](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateAuthority.html).[SignHashAlgorithm](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateAuthority.SignHashAlgorithm.html);
    import com.google.cloud.security.privateca.v1.[CertificateAuthorityServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateAuthorityServiceClient.html);
    import com.google.cloud.security.privateca.v1.[CertificateConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateConfig.html);
    import com.google.cloud.security.privateca.v1.[CertificateConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateConfig.html).[SubjectConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateConfig.SubjectConfig.html);
    import com.google.cloud.security.privateca.v1.[CreateCertificateAuthorityRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CreateCertificateAuthorityRequest.html);
    import com.google.cloud.security.privateca.v1.[KeyUsage](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.KeyUsage.html);
    import com.google.cloud.security.privateca.v1.[KeyUsage](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.KeyUsage.html).[KeyUsageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.KeyUsage.KeyUsageOptions.html);
    import com.google.cloud.security.privateca.v1.[Subject](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.Subject.html);
    import com.google.cloud.security.privateca.v1.[X509Parameters](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.X509Parameters.html);
    import com.google.cloud.security.privateca.v1.[X509Parameters](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.X509Parameters.html).[CaOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.X509Parameters.CaOptions.html);
    import com.google.longrunning.[Operation](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.longrunning.Operation.html);
    import com.google.protobuf.[Duration](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html);
    import java.io.IOException;
    import java.util.concurrent.ExecutionException;
    
    public class CreateCertificateAuthority {
    
      public static void main(String[] args)
          throws InterruptedException, ExecutionException, IOException {
        // TODO(developer): Replace these variables before running the sample.
        // location: For a list of locations, see:
        // https://cloud.google.com/certificate-authority-service/docs/locations
        // poolId: Set it to the CA Pool under which the CA should be created.
        // certificateAuthorityName: Unique name for the CA.
        String project = "your-project-id";
        String location = "ca-location";
        String poolId = "ca-pool-id";
        String certificateAuthorityName = "certificate-authority-name";
        createCertificateAuthority(project, location, poolId, certificateAuthorityName);
      }
    
      // Create Certificate Authority which is the root CA in the given CA Pool.
      public static void createCertificateAuthority(
          String project, String location, String poolId, String certificateAuthorityName)
          throws InterruptedException, ExecutionException, IOException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the `certificateAuthorityServiceClient.close()` method on the client to safely
        // clean up any remaining background resources.
        try ([CertificateAuthorityServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateAuthorityServiceClient.html) certificateAuthorityServiceClient =
            [CertificateAuthorityServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateAuthorityServiceClient.html).create()) {
    
          String commonName = "common-name";
          String orgName = "org-name";
          int caDuration = 100000; // Validity of this CA in seconds.
    
          // Set the type of Algorithm.
          [KeyVersionSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateAuthority.KeyVersionSpec.html) keyVersionSpec =
              [KeyVersionSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateAuthority.KeyVersionSpec.html).newBuilder().[setAlgorithm](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateAuthority.KeyVersionSpec.Builder.html#com_google_cloud_security_privateca_v1_CertificateAuthority_KeyVersionSpec_Builder_setAlgorithm_com_google_cloud_security_privateca_v1_CertificateAuthority_SignHashAlgorithm_)([SignHashAlgorithm](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateAuthority.SignHashAlgorithm.html).RSA_PKCS1_4096_SHA256).build();
    
          // Set CA subject config.
          [SubjectConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateConfig.SubjectConfig.html) subjectConfig =
              [SubjectConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateConfig.SubjectConfig.html).newBuilder()
                  .setSubject(
                      [Subject](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.Subject.html).newBuilder().[setCommonName](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.Subject.Builder.html#com_google_cloud_security_privateca_v1_Subject_Builder_setCommonName_java_lang_String_)(commonName).[setOrganization](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.Subject.Builder.html#com_google_cloud_security_privateca_v1_Subject_Builder_setOrganization_java_lang_String_)(orgName).build())
                  .build();
    
          //  Set the key usage options for X.509 fields.
          [X509Parameters](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.X509Parameters.html) x509Parameters =
              [X509Parameters](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.X509Parameters.html).newBuilder()
                  .[setKeyUsage](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.X509Parameters.Builder.html#com_google_cloud_security_privateca_v1_X509Parameters_Builder_setKeyUsage_com_google_cloud_security_privateca_v1_KeyUsage_)(
                      [KeyUsage](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.KeyUsage.html).newBuilder()
                          .[setBaseKeyUsage](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.KeyUsage.Builder.html#com_google_cloud_security_privateca_v1_KeyUsage_Builder_setBaseKeyUsage_com_google_cloud_security_privateca_v1_KeyUsage_KeyUsageOptions_)(
                              [KeyUsageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.KeyUsage.KeyUsageOptions.html).newBuilder().[setCrlSign](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.KeyUsage.KeyUsageOptions.Builder.html#com_google_cloud_security_privateca_v1_KeyUsage_KeyUsageOptions_Builder_setCrlSign_boolean_)(true).[setCertSign](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.KeyUsage.KeyUsageOptions.Builder.html#com_google_cloud_security_privateca_v1_KeyUsage_KeyUsageOptions_Builder_setCertSign_boolean_)(true).build())
                          .build())
                  .[setCaOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.X509Parameters.Builder.html#com_google_cloud_security_privateca_v1_X509Parameters_Builder_setCaOptions_com_google_cloud_security_privateca_v1_X509Parameters_CaOptions_)([CaOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.X509Parameters.CaOptions.html).newBuilder().[setIsCa](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.X509Parameters.CaOptions.Builder.html#com_google_cloud_security_privateca_v1_X509Parameters_CaOptions_Builder_setIsCa_boolean_)(true).build())
                  .build();
    
          // Set certificate authority settings.
          [CertificateAuthority](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateAuthority.html) certificateAuthority =
              [CertificateAuthority](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateAuthority.html).newBuilder()
                  // CertificateAuthority.Type.SELF_SIGNED denotes that this CA is a root CA.
                  .setType([CertificateAuthority](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateAuthority.html).Type.SELF_SIGNED)
                  .[setKeySpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateAuthority.Builder.html#com_google_cloud_security_privateca_v1_CertificateAuthority_Builder_setKeySpec_com_google_cloud_security_privateca_v1_CertificateAuthority_KeyVersionSpec_)(keyVersionSpec)
                  .setConfig(
                      [CertificateConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateConfig.html).newBuilder()
                          .[setSubjectConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateConfig.Builder.html#com_google_cloud_security_privateca_v1_CertificateConfig_Builder_setSubjectConfig_com_google_cloud_security_privateca_v1_CertificateConfig_SubjectConfig_)(subjectConfig)
                          .[setX509Config](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateConfig.Builder.html#com_google_cloud_security_privateca_v1_CertificateConfig_Builder_setX509Config_com_google_cloud_security_privateca_v1_X509Parameters_)(x509Parameters)
                          .build())
                  // Set the CA validity duration.
                  .setLifetime([Duration](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html).newBuilder().setSeconds(caDuration).build())
                  .build();
    
          // Create the CertificateAuthorityRequest.
          [CreateCertificateAuthorityRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CreateCertificateAuthorityRequest.html) certificateAuthorityRequest =
              [CreateCertificateAuthorityRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CreateCertificateAuthorityRequest.html).newBuilder()
                  .setParent([CaPoolName](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CaPoolName.html).of(project, location, poolId).toString())
                  .[setCertificateAuthorityId](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CreateCertificateAuthorityRequest.Builder.html#com_google_cloud_security_privateca_v1_CreateCertificateAuthorityRequest_Builder_setCertificateAuthorityId_java_lang_String_)(certificateAuthorityName)
                  .setCertificateAuthority(certificateAuthority)
                  .build();
    
          // Create Certificate Authority.
          ApiFuture<Operation> futureCall =
              certificateAuthorityServiceClient
                  .[createCertificateAuthorityCallable](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateAuthorityServiceClient.html#com_google_cloud_security_privateca_v1_CertificateAuthorityServiceClient_createCertificateAuthorityCallable__)()
                  .futureCall(certificateAuthorityRequest);
          [Operation](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.longrunning.Operation.html) response = futureCall.get();
    
          if (response.[hasError](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.longrunning.Operation.html#com_google_longrunning_Operation_hasError__)()) {
            System.out.println("Error while creating CA !" + response.[getError](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.longrunning.Operation.html#com_google_longrunning_Operation_getError__)());
            return;
          }
    
          System.out.println(
              "Certificate Authority created successfully : " + certificateAuthorityName);
        }
      }
    }

###  Python 

To authenticate to CA Service, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import google.cloud.security.privateca_v1 as privateca_v1
    from google.protobuf import duration_pb2
    
    
    def create_certificate_authority(
        project_id: str,
        location: str,
        ca_pool_name: str,
        ca_name: str,
        common_name: str,
        organization: str,
        ca_duration: int,
    ) -> None:
        """
        Create Certificate Authority which is the root CA in the given CA Pool. This CA will be
        responsible for signing certificates within this pool.
    
        Args:
            project_id: project ID or project number of the Cloud project you want to use.
            location: location you want to use. For a list of locations, see: https://cloud.google.com/certificate-authority-service/docs/locations.
            ca_pool_name: set it to the CA Pool under which the CA should be created.
            ca_name: unique name for the CA.
            common_name: a title for your certificate authority.
            organization: the name of your company for your certificate authority.
            ca_duration: the validity of the certificate authority in seconds.
        """
    
        caServiceClient = privateca_v1.CertificateAuthorityServiceClient()
    
        # Set the types of Algorithm used to create a cloud KMS key.
        key_version_spec = privateca_v1.CertificateAuthority.KeyVersionSpec(
            algorithm=privateca_v1.CertificateAuthority.SignHashAlgorithm.RSA_PKCS1_4096_SHA256
        )
    
        # Set CA subject config.
        subject_config = privateca_v1.CertificateConfig.SubjectConfig(
            subject=privateca_v1.Subject(common_name=common_name, organization=organization)
        )
    
        # Set the key usage options for X.509 fields.
        x509_parameters = privateca_v1.X509Parameters(
            key_usage=privateca_v1.KeyUsage(
                base_key_usage=privateca_v1.KeyUsage.KeyUsageOptions(
                    crl_sign=True,
                    cert_sign=True,
                )
            ),
            ca_options=privateca_v1.X509Parameters.CaOptions(
                is_ca=True,
            ),
        )
    
        # Set certificate authority settings.
        certificate_authority = privateca_v1.CertificateAuthority(
            # CertificateAuthority.Type.SELF_SIGNED denotes that this CA is a root CA.
            type_=privateca_v1.CertificateAuthority.Type.SELF_SIGNED,
            key_spec=key_version_spec,
            config=privateca_v1.CertificateConfig(
                subject_config=subject_config,
                x509_config=x509_parameters,
            ),
            lifetime=duration_pb2.Duration(seconds=ca_duration),
        )
    
        ca_pool_path = caServiceClient.ca_pool_path(project_id, location, ca_pool_name)
    
        # Create the CertificateAuthorityRequest.
        request = privateca_v1.CreateCertificateAuthorityRequest(
            parent=ca_pool_path,
            certificate_authority_id=ca_name,
            certificate_authority=certificate_authority,
        )
    
        operation = caServiceClient.create_certificate_authority(request=request)
        result = operation.result()
    
        print("Operation result:", result)
    
    

### REST API

  1. Create a root CA.

To use a customer-managed signing key, specify the `cloud_kms_key_version` in the `key_spec` field instead of `algorithm`.

For more details on signing key options and preparing a customer-managed signing key, see [Configure CA signing keys](https://docs.cloud.google.com/certificate-authority-service/docs/choosing-key-algorithm). 

HTTP method and URL: 
         
         POST https://privateca.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/caPools/POOL_ID/certificateAuthorities?certificate_authority_id=ROOT_CA_ID

Request JSON body: 
         
         {
         "type": "SELF_SIGNED",
         "lifetime": {
           "seconds": 315576000,
           "nanos": 0
         },
         "config": {
           "subject_config": {
             "subject": {
               "organization": "ORGANIZATION_NAME",
               "common_name": "COMMON_NAME"
             }
           },
           "x509_config":{
             "ca_options":{
               "is_ca":true
             },
             "key_usage":{
               "base_key_usage":{
                 "cert_sign":true,
                 "crl_sign":true
               }
             }
           }
         },
         "key_spec":{
           "algorithm":"RSA_PKCS1_4096_SHA256"
         }
         }
         

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
         
         curl -X POST \  
              -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
              -H "Content-Type: application/json; charset=utf-8" \  
              -d @request.json \  
              "https://privateca.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/caPools/POOL_ID/certificateAuthorities?certificate_authority_id=ROOT_CA_ID"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
         
         $cred = gcloud auth print-access-token  
         $headers = @{ "Authorization" = "Bearer $cred" }  
           
         Invoke-WebRequest `  
             -Method POST `  
             -Headers $headers `  
             -ContentType: "application/json; charset=utf-8" `  
             -InFile request.json `  
             -Uri "https://privateca.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/caPools/POOL_ID/certificateAuthorities?certificate_authority_id=ROOT_CA_ID" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
         
         {
           "name": "projects/PROJECT_ID/locations/LOCATION/operations/operation-UUID",
           "metadata": {...},
           "done": false
         }
         

  2. Poll the operation until it has completed.

HTTP method and URL: 
         
         GET https://privateca.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/operations/operation-UUID

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
         
         curl -X GET \  
              -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
              "https://privateca.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/operations/operation-UUID"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
         
         $cred = gcloud auth print-access-token  
         $headers = @{ "Authorization" = "Bearer $cred" }  
           
         Invoke-WebRequest `  
             -Method GET `  
             -Headers $headers `  
             -Uri "https://privateca.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/operations/operation-UUID" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
         
         {
          "name": "projects/PROJECT_ID/locations/LOCATION/operations/operation-UUID",
          "metadata": {...},
          "done": true,
          "response": {
            "@type": "type.googleapis.com/google.cloud.security.privateca.v1.CertificateAuthority",
            "name": "...",
          }
         }
         




**Note:** Root CAs are created in the `STAGED` state by default. We recommend that you test your CA while it is still in the `STAGED` state. You must directly request certificates from the CA `STAGED` state because these CAs cannot issue certificates through CA pool load-balancing. For more information, see Testing a CA.  
  
For more information about CA states, see [CA states](https://docs.cloud.google.com/certificate-authority-service/docs/certificate-authority-states).

After you have verified that the CA works as expected, you can enable it to start issuing load-balanced certificates for the CA pool.

**Note:** If you delete resources such as CA pools, certificate authorities, and certificate templates, you will not be able to create a new resource of that type with the same name in the same project and location.

## Enable a root CA

### gcloud

To enable a root CA, run the following `gcloud` command:
    
    
    gcloud privateca roots enable ROOT_CA_ID --location=LOCATION --pool=POOL_ID
    

Replace the following:

  * ROOT_CA_ID: the name of the CA
  * LOCATION: the location of the CA pool. For the complete list of locations, see [Locations](https://docs.cloud.google.com/certificate-authority-service/docs/locations).
  * POOL_ID: the name of the CA pool



### Terraform

If you use Terraform to create a root CA, the root CA is enabled on creation. To create a root CA in the `STAGED` state, set the `desired_state` field to `STAGED` when creating the CA.

You can set the `desired_state` field to `ENABLED` or `DISABLED` after CA creation.

###  Go 

To authenticate to CA Service, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	privateca "cloud.google.com/go/security/privateca/apiv1"
    	"cloud.google.com/go/security/privateca/apiv1/privatecapb"
    )
    
    // Enable the Certificate Authority present in the given ca pool.
    // CA cannot be enabled if it has been already deleted.
    func enableCa(w io.Writer, projectId string, location string, caPoolId string, caId string) error {
    	// projectId := "your_project_id"
    	// location := "us-central1"	// For a list of locations, see: https://cloud.google.com/certificate-authority-service/docs/locations.
    	// caPoolId := "ca-pool-id"		// The id of the CA pool under which the CA is present.
    	// caId := "ca-id"				// The id of the CA to be enabled.
    
    	ctx := context.Background()
    	caClient, err := privateca.[NewCertificateAuthorityClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/security/latest/privateca/apiv1.html#cloud_google_com_go_security_privateca_apiv1_CertificateAuthorityClient_NewCertificateAuthorityClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("NewCertificateAuthorityClient creation failed: %w", err)
    	}
    	defer caClient.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/security/latest/privateca/apiv1.html#cloud_google_com_go_security_privateca_apiv1_CertificateAuthorityClient_Close)()
    
    	fullCaName := fmt.Sprintf("projects/%s/locations/%s/caPools/%s/certificateAuthorities/%s",
    		projectId, location, caPoolId, caId)
    
    	// Create the EnableCertificateAuthorityRequest.
    	// See https://pkg.go.dev/cloud.google.com/go/security/privateca/apiv1/privatecapb#EnableCertificateAuthorityRequest.
    	req := &privatecapb.EnableCertificateAuthorityRequest{Name: fullCaName}
    
    	op, err := caClient.EnableCertificateAuthority(ctx, req)
    	if err != nil {
    		return fmt.Errorf("EnableCertificateAuthority failed: %w", err)
    	}
    
    	var caResp *privatecapb.CertificateAuthority
    	if caResp, err = op.Wait(ctx); err != nil {
    		return fmt.Errorf("EnableCertificateAuthority failed during wait: %w", err)
    	}
    
    	if caResp.State != privatecapb.[CertificateAuthority_ENABLED](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/security/latest/privateca/apiv1/privatecapb.html#cloud_google_com_go_security_privateca_apiv1_privatecapb_CertificateAuthority_STATE_UNSPECIFIED_CertificateAuthority_ENABLED_CertificateAuthority_DISABLED_CertificateAuthority_STAGED_CertificateAuthority_AWAITING_USER_ACTIVATION_CertificateAuthority_DELETED) {
    		return fmt.Errorf("unable to enable Certificate Authority. Current state: %s", caResp.State.String())
    	}
    
    	fmt.Fprintf(w, "Successfully enabled Certificate Authority: %s.", caId)
    	return nil
    }
    

###  Java 

To authenticate to CA Service, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.api.core.[ApiFuture](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.ApiFuture.html);
    import com.google.cloud.security.privateca.v1.[CertificateAuthority](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateAuthority.html).State;
    import com.google.cloud.security.privateca.v1.[CertificateAuthorityName](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateAuthorityName.html);
    import com.google.cloud.security.privateca.v1.[CertificateAuthorityServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateAuthorityServiceClient.html);
    import com.google.cloud.security.privateca.v1.[EnableCertificateAuthorityRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.EnableCertificateAuthorityRequest.html);
    import com.google.longrunning.[Operation](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.longrunning.Operation.html);
    import java.io.IOException;
    import java.util.concurrent.ExecutionException;
    
    public class EnableCertificateAuthority {
    
      public static void main(String[] args)
          throws InterruptedException, ExecutionException, IOException {
        // TODO(developer): Replace these variables before running the sample.
        // location: For a list of locations, see:
        // https://cloud.google.com/certificate-authority-service/docs/locations
        // poolId: The id of the CA pool under which the CA is present.
        // certificateAuthorityName: The name of the CA to be enabled.
        String project = "your-project-id";
        String location = "ca-location";
        String poolId = "ca-pool-id";
        String certificateAuthorityName = "certificate-authority-name";
        enableCertificateAuthority(project, location, poolId, certificateAuthorityName);
      }
    
      // Enable the Certificate Authority present in the given ca pool.
      // CA cannot be enabled if it has been already deleted.
      public static void enableCertificateAuthority(
          String project, String location, String poolId, String certificateAuthorityName)
          throws IOException, ExecutionException, InterruptedException {
        try ([CertificateAuthorityServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateAuthorityServiceClient.html) certificateAuthorityServiceClient =
            [CertificateAuthorityServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateAuthorityServiceClient.html).create()) {
          // Create the Certificate Authority Name.
          [CertificateAuthorityName](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateAuthorityName.html) certificateAuthorityParent =
              [CertificateAuthorityName](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateAuthorityName.html).newBuilder()
                  .setProject(project)
                  .setLocation(location)
                  .setCaPool(poolId)
                  .setCertificateAuthority(certificateAuthorityName)
                  .build();
    
          // Create the Enable Certificate Authority Request.
          [EnableCertificateAuthorityRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.EnableCertificateAuthorityRequest.html) enableCertificateAuthorityRequest =
              [EnableCertificateAuthorityRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.EnableCertificateAuthorityRequest.html).newBuilder()
                  .setName(certificateAuthorityParent.[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateAuthorityName.html#com_google_cloud_security_privateca_v1_CertificateAuthorityName_toString__)())
                  .build();
    
          // Enable the Certificate Authority.
          ApiFuture<Operation> futureCall =
              certificateAuthorityServiceClient
                  .[enableCertificateAuthorityCallable](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateAuthorityServiceClient.html#com_google_cloud_security_privateca_v1_CertificateAuthorityServiceClient_enableCertificateAuthorityCallable__)()
                  .futureCall(enableCertificateAuthorityRequest);
          [Operation](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.longrunning.Operation.html) response = futureCall.get();
    
          if (response.[hasError](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.longrunning.Operation.html#com_google_longrunning_Operation_hasError__)()) {
            System.out.println("Error while enabling Certificate Authority !" + response.[getError](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.longrunning.Operation.html#com_google_longrunning_Operation_getError__)());
            return;
          }
    
          // Get the current CA state.
          State caState =
              certificateAuthorityServiceClient
                  .getCertificateAuthority(certificateAuthorityParent)
                  .getState();
    
          // Check if the CA is enabled.
          if (caState == State.ENABLED) {
            System.out.println("Enabled Certificate Authority : " + certificateAuthorityName);
          } else {
            System.out.println(
                "Cannot enable the Certificate Authority ! Current CA State: " + caState);
          }
        }
      }
    }

###  Python 

To authenticate to CA Service, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import google.cloud.security.privateca_v1 as privateca_v1
    
    
    def enable_certificate_authority(
        project_id: str, location: str, ca_pool_name: str, ca_name: str
    ) -> None:
        """
        Enable the Certificate Authority present in the given ca pool.
        CA cannot be enabled if it has been already deleted.
    
        Args:
            project_id: project ID or project number of the Cloud project you want to use.
            location: location you want to use. For a list of locations, see: https://cloud.google.com/certificate-authority-service/docs/locations.
            ca_pool_name: the name of the CA pool under which the CA is present.
            ca_name: the name of the CA to be enabled.
        """
    
        caServiceClient = privateca_v1.CertificateAuthorityServiceClient()
        ca_path = caServiceClient.certificate_authority_path(
            project_id, location, ca_pool_name, ca_name
        )
    
        # Create the Enable Certificate Authority Request.
        request = privateca_v1.EnableCertificateAuthorityRequest(
            name=ca_path,
        )
    
        # Enable the Certificate Authority.
        operation = caServiceClient.enable_certificate_authority(request=request)
        operation.result()
    
        # Get the current CA state.
        ca_state = caServiceClient.get_certificate_authority(name=ca_path).state
    
        # Check if the CA is enabled.
        if ca_state == privateca_v1.CertificateAuthority.State.ENABLED:
            print("Enabled Certificate Authority:", ca_name)
        else:
            print("Cannot enable the Certificate Authority ! Current CA State:", ca_state)
    
    

### REST API

  1. Enable the CA to issue certificates from the CA pool.

HTTP method and URL: 
         
         POST https://privateca.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/caPools/POOL_ID/certificateAuthorities/ROOT_CA_ID:enable

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
         
         curl -X POST \  
              -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
              -H "Content-Type: application/json; charset=utf-8" \  
              -d "" \  
              "https://privateca.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/caPools/POOL_ID/certificateAuthorities/ROOT_CA_ID:enable"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
         
         $cred = gcloud auth print-access-token  
         $headers = @{ "Authorization" = "Bearer $cred" }  
           
         Invoke-WebRequest `  
             -Method POST `  
             -Headers $headers `  
             -Uri "https://privateca.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/caPools/POOL_ID/certificateAuthorities/ROOT_CA_ID:enable" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
         
         {
             "name": "projects/PROJECT_ID/locations/LOCATION/operations/operation-UUID",
             "metadata": {...},
             "done": false
         }
         

  2. Poll the operation until it has completed.

HTTP method and URL: 
         
         GET https://privateca.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/operations/operation-UUID

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
         
         curl -X GET \  
              -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
              "https://privateca.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/operations/operation-UUID"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
         
         $cred = gcloud auth print-access-token  
         $headers = @{ "Authorization" = "Bearer $cred" }  
           
         Invoke-WebRequest `  
             -Method GET `  
             -Headers $headers `  
             -Uri "https://privateca.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/operations/operation-UUID" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
         
         {
             "name": "projects/PROJECT_ID/locations/LOCATION/operations/operation-UUID",
             "metadata": {...},
             "done": true,
             "response": {
               "@type": "type.googleapis.com/google.cloud.security.privateca.v1.CertificateAuthority",
               "name": "...",
             }
         }
         




**Caution:** Any certificate signed by the private key of the root CA is widely trusted by browsers. We recommend that you don't issue end-entity certificates from a root CA. Create subordinate CAs to issue end-entity certificates.

## Test a CA

To verify that a CA is able to issue certificates, request a certificate from the associated CA pool and explicitly mention the name of the CA you want to test using the `--ca` flag.

You can use the following methods to request a certificate from a CA pool:

  1. Have CA Service create a private or public key for you.
  2. Generate your own private or public key and submit a Certificate Signing Request (CSR).



It is easier to use an auto-generated private key or public key to request a certificate from a CA in a CA pool. This section provides information on testing a CA using that method.

To use an auto-generated private key or public key to request a certificate from a CA in a CA pool, run the following `gcloud` command:
    
    
    gcloud privateca certificates create \
        --issuer-pool=POOL_ID \
        --issuer-location=ISSUER_LOCATION \
        --ca=ROOT_CA_ID \
        --generate-key \
        --key-output-file=KEY_FILENAME \
        --cert-output-file=CERT_FILENAME \
        --dns-san=DNS_NAME
    

Replace the following:

  * POOL_ID: the name of the CA pool
  * ISSUER_LOCATION: the location of the Certificate Authority (CA) that issued the digital certificate
  * ROOT_CA_ID: the unique identifier of the CA that you want to test
  * KEY_FILENAME: the file where the generated key is written in PEM format
  * CERT_FILENAME: the file where the resulting PEM-encoded certificate chain file is written. The order of the certificate chain is from leaf to root.
  * DNS_NAME: one or more comma-separated DNS Subject Alternative Names (SANs)

The `--generate-key` flag generates a new RSA-2048 private key on your machine.




To use a Certificate Signing Request (CSR) to request a certificate from a CA in a CA pool, or for more information about requesting certificates, see [Request a certificate and view issued certificates](https://docs.cloud.google.com/certificate-authority-service/docs/requesting-certificates).

## Clone certificate authorities

To clone an existing CA to renew that CA, or to create a new CA with the same configuration, run the following command:
    
    
    gcloud privateca roots create NEW_CA_ID \
        --location=LOCATION \
        --pool=POOL_ID \
        --from-ca=EXISTING_CA_ID \
        --key-algorithm "ec-p384-sha384"
    

Replace the following:

  * NEW_CA_ID: the unique identifier of the new CA
  * LOCATION: the location of the CA pool
  * POOL_ID: the name of the CA pool where you want to create the new CA
  * EXISTING_CA_ID: the ID of the source CA or fully qualified identifier for the source CA



The `--from-ca` flag is supported for root and subordinate CA creation. The existing CA must be in the same CA pool as the new CA.

The `--key-algorithm` flag copies all CA configuration from the existing CA (except for the Cloud KMS key version and Cloud Storage bucket). However, you can still override any of the configuration values in the new CA by explicitly providing the appropriate flag. For example, you can still specify `--subject SUBJECT to use a new subject.

If you omit the `--key-algorithm` flag, the algorithm defaults to:

  * `rsa-pkcs1-4096-sha256` for root CAs.
  * `rsa-pkcs1-2048-sha256` for subordinate CAs.



For more information about this `gcloud` command, see [gcloud privateca roots create](https://docs.cloud.google.com/sdk/gcloud/reference/privateca/roots/create).

## What's next

  * Learn how to [create a subordinate CA](https://docs.cloud.google.com/certificate-authority-service/docs/create-subordinate-ca).
  * Learn how to [create a subordinate CA from an external CA](https://docs.cloud.google.com/certificate-authority-service/docs/create-sub-ca-from-external-ca).
  * Learn about [CA states](https://docs.cloud.google.com/certificate-authority-service/docs/certificate-authority-states).
  * Learn how to [request certificates](https://docs.cloud.google.com/certificate-authority-service/docs/requesting-certificates).
  * Learn about [templates and issuance policies](https://docs.cloud.google.com/certificate-authority-service/docs/certificate-template).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
