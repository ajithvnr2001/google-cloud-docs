---
url: https://docs.cloud.google.com/compute/docs/disks/customer-supplied-encryption/
title: Encrypt disks with customer-supplied encryption keys \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:18:32.735957+00:00
---

# Encrypt disks with customer-supplied encryption keys  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/disks/customer-supplied-encryption/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Encrypt disks with customer-supplied encryption keys Stay organized with collections  Save and categorize content based on your preferences. 

Linux  Windows 

**Caution:** Customer-supplied encryption keys (CSEK) for Compute Engine are [deprecated](https://docs.cloud.google.com/compute/docs/deprecations). For more information and instructions on alternatives, see [CSEK deprecation in Compute Engine](https://docs.cloud.google.com/compute/docs/deprecations/csek-deprecation-in-compute-engine). 

This document discusses how to encrypt [disks](https://docs.cloud.google.com/compute/docs/disks) with [customer-supplied encryption keys](https://docs.cloud.google.com/docs/security/encryption/customer-supplied-encryption-keys).

For information about disk encryption, see [About disk encryption](https://docs.cloud.google.com/compute/docs/disks/disk-encryption).

For information about encrypting disks with customer-managed encryption keys (CMEK) see [Protect resources by using Cloud KMS keys](https://docs.cloud.google.com/compute/docs/disks/customer-managed-encryption).

Using CSEKs means you provide your own encryption keys and Compute Engine uses your keys to protect the Google-owned and Google-managed encryption keys used to encrypt and decrypt your data. Only users who can provide the correct key can use resources protected by a customer-supplied encryption key (CSEK).

Google does not store your keys on its servers and cannot access your protected data unless you provide the key. This also means that if you forget or lose your key, **there is no way for Google to recover the key or to recover any data encrypted with the lost key.**

When you delete a Persistent Disk volume, Google discards the cipher keys, rendering the data irretrievable. This process is irreversible.

## Before you begin

  * Read about [disks](https://docs.cloud.google.com/compute/docs/disks), [images](https://docs.cloud.google.com/compute/docs/images), and [disk snapshots](https://docs.cloud.google.com/compute/docs/disks/create-snapshots).
  * If you haven't already, set up [authentication](https://docs.cloud.google.com/compute/docs/authentication). Authentication verifies your identity for access to Google Cloud services and APIs. To run code or samples from a local development environment, you can authenticate to Compute Engine by selecting one of the following options: 

Select the tab for how you plan to use the samples on this page:

### Console

When you use the Google Cloud console to access Google Cloud services and APIs, you don't need to set up authentication. 

### gcloud

    1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. After installation, [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the Google Cloud CLI by running the following command: 
           
           gcloud init

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
    2. [ Set a default region and zone](https://docs.cloud.google.com/compute/docs/gcloud-compute#set_default_zone_and_region_in_your_local_client).

### Python

To use the Python samples on this page in a local development environment, install and initialize the gcloud CLI, and then set up Application Default Credentials with your user credentials. 

    1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

    2. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

    3. If you're using a local shell, then create local authentication credentials for your user account: 
           
           gcloud auth application-default login

You don't need to do this if you're using Cloud Shell.

If an authentication error is returned, and you are using an external identity provider (IdP), confirm that you have [ signed in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

For more information, see [ Set up authentication for a local development environment](https://docs.cloud.google.com/compute/docs/authentication#local-development). 

### REST

To use the REST API samples on this page in a local development environment, you use the credentials you provide to the gcloud CLI. 

[Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

For more information, see [Authenticate for using REST](https://docs.cloud.google.com/docs/authentication/rest) in the Google Cloud authentication documentation. 




### Required roles and permissions

To get the permissions that you need to create CSEK-encrypted snapshots, images, and disks, ask your administrator to grant you the following IAM roles on the project: 

  * [Compute Instance Admin (v1) ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin.v1) (`roles/compute.instanceAdmin.v1`)
  * To connect to a VM that has an attached service account: [Service Account User (v1) ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to create CSEK-encrypted snapshots, images, and disks. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to create CSEK-encrypted snapshots, images, and disks:

  * To create a snapshot of a disk: 
    * `compute.snapshots.create` on the project
    * `compute.disks.createSnapshot` on the disk
  * To create an image: 
    * `compute.images.create` on the project
    * `compute.disks.useReadOnly` on the disk
  * To create a disk from a standard snapshot: 
    * `compute.disks.create` on the destination project for the new disk
    * `compute.snapshots.useReadOnly` on the snapshot
  * To create a disk from an image: 
    * `compute.disks.create` on the destination project for the new disk
    * `compute.images.useReadOnly` on the image
  * To create a disk from an instant snapshot: 
    * `compute.disks.create` on the destination project for the new disk
    * `compute.instantSnapshots.useReadOnly` on the source instant snapshot



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Restrictions

For CSEK, the following restrictions apply:

### General restrictions

Availability of customer-supplied encryption keys depends on the location of your billing account, not the location of the resource.

Customer-supplied encryption keys are not available for billing accounts that are in the following countries:

  * Brazil
  * India



### Technical restrictions

  * You can only encrypt new persistent disks with your own key. You can't encrypt existing persistent disks with your own key.

  * You can't use your own keys with [Local SSD disks](https://docs.cloud.google.com/compute/docs/disks#localssds) because Local SSD disks use Google-owned and Google-managed encryption keys. The keys are deleted when the VM is terminated.

  * Compute Engine does not store encryption keys with [instance templates](https://docs.cloud.google.com/compute/docs/instance-templates), so you need to store your own keys in [KMS](https://docs.cloud.google.com/kms/docs) to encrypt disks in a [managed instance group](https://docs.cloud.google.com/compute/docs/instance-groups).

  * You can't suspend instances that have CSEK-protected disks attached.




## Specifications

This section describes the encryption specification and the format of CSEK.

### Encryption

Compute Engine uses your encryption key to protect Google's encryption keys with AES-256 encryption.

### Required key format

It is up to you to generate and manage your key. You must provide a key that is a 256-bit string encoded in [RFC 4648 standard base64](https://tools.ietf.org/html/rfc4648#section-4) to Compute Engine.

The following is an example of a base64 encoded key, generated with the string "Hello from Google Cloud Platform"
    
    
    SGVsbG8gZnJvbSBHb29nbGUgQ2xvdWQgUGxhdGZvcm0=
    

It can be generated using the following script:
    
    
    read -sp "String:" ; \
        [[ ${#REPLY} == 32 ]] && \
            echo "$(echo -n "$REPLY" | base64)" || \
            (>&2 echo -e "\nERROR:Wrong Size"; false)
    

### RSA key wrapping

**Beta**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

In addition to encoding your key in base64, you can optionally wrap your key using an RSA public key certificate provided by Google, encode the key in base64, and then use that key in your requests.

RSA wrapping is a process in which you use a public key to encrypt your data. After that data has been encrypted with the public key, it can only be decrypted by the respective private key. In this case, the private key is known only to Google Cloud services. By wrapping your key using the RSA certificate, you ensure that only Google Cloud services can unwrap your key and use it to protect your data.

For more information, see [RSA encryption](https://wikipedia.org/wiki/RSA_\(cryptosystem\)).

To create an RSA-wrapped key for Compute Engine, do the following:

  1. Wrap your key using the public key provided in a certificate that Compute Engine manages. **Make sure to wrap your key using OAEP padding, not PKCS #1 v1.5 padding.**
  2. Encode your RSA-wrapped key using standard base64 encoding.



Download the public certificate maintained by Compute Engine from:
    
    
    https://cloud-certs.storage.googleapis.com/google-cloud-csek-ingress.pem
    

There are many ways of generate and RSA-wrap your key; use a method that is familiar to you. The following are two examples of RSA-wrapping your key that you could use.

**Example 1**

The following instructions use the [openssl](https://www.openssl.org/) command-line utility to RSA-wrap and encode a key.

**Note:** This example creates and saves a random key in a file. Because your key is sensitive information, make sure to follow best practices for securing your key file.

  1. Optional: Generate a 256-bit (32-byte) random key. If you already have a key you want to use, you can skip this step. There are many ways you can generate a key. For example:
         
         $ head -c 32 /dev/urandom | LC_CTYPE=C tr '\n' = > mykey.txt
         

  2. Download the [public key certificate](https://cloud-certs.storage.googleapis.com/google-cloud-csek-ingress.pem):
         
         $  curl -s -O -L https://cloud-certs.storage.googleapis.com/google-cloud-csek-ingress.pem

  3. Extract the public key from the certificate:
         
         $ openssl x509 -pubkey -noout -in google-cloud-csek-ingress.pem > pubkey.pem
         

  4. RSA-wrap your key, making sure to replace `mykey.txt` with your own key file.
         
         $ openssl rsautl -oaep -encrypt -pubin -inkey pubkey.pem -in mykey.txt -out rsawrappedkey.txt
         

  5. Encode your RSA-wrapped key in base64.
         
         $ openssl enc -base64 -in rsawrappedkey.txt | tr -d '\n' | sed -e '$a\' > rsawrapencodedkey.txt
         




**Example 2**

The following is sample Python script that generates a 256-bit (32-byte) random string and creates a base64 encoded RSA-wrapped key using the [cryptography](https://pypi.python.org/pypi/cryptography) library:
    
    
    import argparse
    import base64
    import os
    from typing import Optional
    
    from cryptography import x509
    from cryptography.hazmat.backends import default_backend
    from cryptography.hazmat.primitives import hashes
    from cryptography.hazmat.primitives.asymmetric import padding
    from cryptography.hazmat.primitives.asymmetric.rsa import RSAPublicKey
    import requests
    
    
    GOOGLE_PUBLIC_CERT_URL = (
        "https://cloud-certs.storage.googleapis.com/google-cloud-csek-ingress.pem"
    )
    
    
    def get_google_public_cert_key() -> RSAPublicKey:
        """
        Downloads the Google public certificate.
    
        Returns:
            RSAPublicKey object with the Google public certificate.
        """
        r = requests.get(GOOGLE_PUBLIC_CERT_URL)
        r.raise_for_status()
    
        # Load the certificate.
        certificate = x509.load_pem_x509_certificate(r.content, default_backend())
    
        # Get the certicate's public key.
        public_key = certificate.public_key()
    
        return public_key
    
    
    def wrap_rsa_key(public_key: RSAPublicKey, private_key_bytes: bytes) -> bytes:
        """
        Use the Google public key to encrypt the customer private key.
    
        This means that only the Google private key is capable of decrypting
        the customer private key.
    
        Args:
            public_key: The public key to use for encrypting.
            private_key_bytes: The private key to be encrypted.
    
        Returns:
            private_key_bytes encrypted using the public_key. Encoded using
            base64.
        """
        wrapped_key = public_key.encrypt(
            private_key_bytes,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA1()),
                algorithm=hashes.SHA1(),
                label=None,
            ),
        )
        encoded_wrapped_key = base64.b64encode(wrapped_key)
        return encoded_wrapped_key
    
    
    def main(key_file: Optional[str]) -> None:
        """
        This script will encrypt a private key with Google public key.
    
        Args:
            key_file: path to a file containing your private key. If not
                provided, a new key will be generated (256 bit).
        """
        # Generate a new 256-bit private key if no key is specified.
        if not key_file:
            customer_key_bytes = os.urandom(32)
        else:
            with open(key_file, "rb") as f:
                customer_key_bytes = f.read()
    
        google_public_key = get_google_public_cert_key()
        wrapped_rsa_key = wrap_rsa_key(google_public_key, customer_key_bytes)
    
        b64_key = base64.b64encode(customer_key_bytes).decode("utf-8")
    
        print(f"Base-64 encoded private key: {b64_key}")
        print(f"Wrapped RSA key: {wrapped_rsa_key.decode('utf-8')}")
    
    
    if __name__ == "__main__":
        parser = argparse.ArgumentParser(
            description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
        )
        parser.add_argument("--key_file", help="File containing your binary private key.")
    
        args = parser.parse_args()
    
        main(args.key_file)

Your key is now ready to use!

#### Use a RSA-wrapped key

Using the Google Cloud CLI, you can provide a regular key and a RSA-wrapped key in the same way.

In the [API](https://docs.cloud.google.com/compute/docs/reference/latest/disks#diskEncryptionKey), use the `sha256` property instead of `rawKey` if you want to use a RSA-wrapped key instead.

## Encrypting resources with CSEK using the command-line tool

Encryption keys can be used through the Google Cloud CLI.

[Download and install `gcloud`](https://docs.cloud.google.com/sdk/gcloud).

### Key file

When you use the `gcloud compute` command-line tool to set your keys, you provide encoded keys using a key file that contains your encoded keys as a JSON list. A key file can contain multiple keys, letting you manage many keys in a single place. Alternatively, you can create single key files to handle each key separately. A key file is only usable with the gcloud CLI. When using REST, you must supply the key directly in your request.

Each entry in your key file must provide:

  * The fully qualified URI to the resource the key protects
  * The corresponding key
  * The type of key, either `raw` or `rsa-encrypted`



When you use the key file in your requests, the tool looks for matching resources and uses the respective keys. If no matching resources are found, the request fails.

### Key file format

The following is an example key file:
    
    
    [
      {
      "uri": "https://www.googleapis.com/compute/v1/projects/myproject/zones/us-central1-a/disks/example-disk",
      "key": "acXTX3rxrKAFTF0tYVLvydU1riRZTvUNC4g5I11NY+c=",
      "key-type": "raw"
      },
      {
      "uri": "https://www.googleapis.com/compute/v1/projects/myproject/global/snapshots/my-private-snapshot",
      "key": "ieCx/NcW06PcT7Ep1X6LUTc/hLvUDYyzSZPPVCVPTVEohpeHASqC8uw5TzyO9U+Fka9JFHz0mBibXUInrC/jEk014kCK/NPjYgEMOyssZ4ZINPKxlUh2zn1bV+MCaTICrdmuSBTWlUUiFoDD6PYznLwh8ZNdaheCeZ8ewEXgFQ8V+sDroLaN3Xs3MDTXQEMMoNUXMCZEIpg9Vtp9x2oeQ5lAbtt7bYAAHf5l+gJWw3sUfs0/Glw5fpdjT8Uggrr+RMZezGrltJEF293rvTIjWOEB3z5OHyHwQkvdrPDFcTqsLfh+8Hr8g+mf+7zVPEC8nEbqpdl3GPv3A7AwpFp7MA==",
      "key-type": "rsa-encrypted"
      }
    ]
    

### Best practices for managing your key file

If you use a key file, restrict access to your file to only those who need it. Make sure to set appropriate permissions on these files and consider encrypting these files using additional tools:

  * On Windows, consider using [BitLocker](https://docs.microsoft.com/en-us/windows/security/information-protection/bitlocker/bitlocker-overview) or [Encrypting File System (EFS)](http://windows.microsoft.com/en-us/windows/what-is-encrypting-file-system#1TC=windows-7).
  * On macOS, consider using [FileVault 2](https://support.apple.com/en-us/HT204837).
  * On Linux, consider [Linux Unified Key Setup (LUKS)](https://guardianproject.info/code/luks/) or [eCryptfs](http://ecryptfs.org/).

**Note:** You must maintain secure and robust storage for your CSEKs. If you don't want to locally manage encryption keys, use [Cloud Key Management Service](https://docs.cloud.google.com/kms/docs) to create and manage [customer-managed encryption keys (CMEKs)](https://docs.cloud.google.com/compute/docs/disks/customer-managed-encryption).

## Create a blank CSEK-encrypted Persistent Disk volume

You can encrypt a new persistent disk by supplying a key during VM or disk creation.

###  Console 

  1. Go to the **Disks** page.

[Go to Disks](https://console.cloud.google.com/compute/disks)

  2. Click **Create disk** and enter the properties for the new disk.

  3. Under **Encryption** , select **Customer-supplied key**.

  4. Provide the encryption key for the disk in the **Source disk encryption key** field and select **Wrapped key** if the key has been wrapped with the public RSA key.




###  gcloud 

In the `gcloud compute` tool, encrypt a disk using the `--csek-key-file` flag during VM creation. If you are using an RSA-wrapped key, use the `gcloud beta` component:
    
    
    gcloud (beta) compute instances create example-instance --csek-key-file example-file.json
    

To encrypt a standalone persistent disk:
    
    
    gcloud (beta) compute disks create example-disk --csek-key-file example-file.json
    

###  REST 

You can encrypt a disk by using the `diskEncryptionKey` property and making a request to the v1 API for a raw (non-RSA wrapped) key, or to the Beta API for a RSA-wrapped key. Provide one of the following properties in your request:

  * `rawKey`: if your key is base64 encoded
  * `rsaEncryptedKey`: if your key is RSA-wrapped and base64 encoded



For example, to encrypt a new disk during VM creation with an RSA-wrapped key:
    
    
    POST https://compute.googleapis.com/compute/beta/projects/myproject/zones/us-central1-a/instances
    
    {
    "machineType": "zones/us-central1-a/machineTypes/e2-standard-2",
    "disks": [
     {
      "type": "PERSISTENT",
      "diskEncryptionKey": {
        "rsaEncryptedKey": "ieCx/NcW06PcT7Ep1X6LUTc/hLvUDYyzSZPPVCVPTVEohpeHASqC8uw5TzyO9U+Fka9JFHz0mBibXUInrC/jEk014kCK/NPjYgEMOyssZ4ZINPKxlUh2zn1bV+MCaTICrdmuSBTWlUUiFoDD6PYznLwh8ZNdaheCeZ8ewEXgFQ8V+sDroLaN3Xs3MDTXQEMMoNUXMCZEIpg9Vtp9x2oeQ5lAbtt7bYAAHf5l+gJWw3sUfs0/Glw5fpdjT8Uggrr+RMZezGrltJEF293rvTIjWOEB3z5OHyHwQkvdrPDFcTqsLfh+8Hr8g+mf+7zVPEC8nEbqpdl3GPv3A7AwpFp7MA=="
      },
      "initializeParams": {
       "sourceImage": "projects/debian-cloud/global/images/debian-9-stretch-v20170619"
      },
      "boot": true
     }
    ],
    ...
    }
    

Similarly, you can also use REST to create a new standalone persistent disk and encrypt it with your own key:
    
    
    POST https://compute.googleapis.com/compute/beta/projects/myproject/zones/
    us-central1-a/disks?sourceImage=https%3A%2F%2Fwww.googleapis.com%2Fcompute%2F
    alpha%2Fprojects%2Fdebian-cloud%2Fglobal%2Fimages%2Fdebian-9-stretch-v20170619
    
    {
     "name": "new-encrypted-disk-key",
     "diskEncryptionKey": {
       "rsaEncryptedKey": "ieCx/NcW06PcT7Ep1X6LUTc/hLvUDYyzSZPPVCVPTVEohpeHASqC8uw5TzyO9U+Fka9JFHz0mBibXUInrC/jEk014kCK/NPjYgEMOyssZ4ZINPKxlUh2zn1bV+MCaTICrdmuSBTWlUUiFoDD6PYznLwh8ZNdaheCeZ8ewEXgFQ8V+sDroLaN3Xs3MDTXQEMMoNUXMCZEIpg9Vtp9x2oeQ5lAbtt7bYAAHf5l+gJWw3sUfs0/Glw5fpdjT8Uggrr+RMZezGrltJEF293rvTIjWOEB3z5OHyHwQkvdrPDFcTqsLfh+8Hr8g+mf+7zVPEC8nEbqpdl3GPv3A7AwpFp7MA=="
      },
     "type": "zones/us-central1-a/diskTypes/pd-standard"
    }
    

## Create a snapshot from a CSEK-encrypted disk

If you create a snapshot from a CSEK-encrypted disk, you must provide the encryption key that you used to encrypt the disk and a key to encrypt the new snapshot. You must also encrypt the snapshot with a CSEK.

To convert CSEK-encrypted disks or snapshots to use Google-owned and Google-managed encryption keys, you must create a new disk or snapshot.

Snapshots of disks encrypted with CSEK are always full snapshots. This differs from snapshots of disks encrypted with [customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/compute/docs/disks/customer-managed-encryption), which are [incremental](https://docs.cloud.google.com/compute/docs/disks/create-snapshots). Snapshots are priced based on the total size of the snapshot, so a full snapshot might cost more than an incremental snapshot.

Review the [Best practices for disk snapshots](https://docs.cloud.google.com/compute/docs/disks/snapshot-best-practices) before creating your snapshot.

**Note:** You can only create a snapshot from an encrypted disk in the Google Cloud console or REST.

###  Console 

  1. Go to the **Snapshots** page.

[Go to Snapshots](https://console.cloud.google.com/compute/snapshots)

  2. Click **Create snapshot**.

  3. Under **Source disk** , choose the encrypted disk you want to create a snapshot of.

  4. Provide the encryption key for the disk in the **Source disk encryption key** field and select **Wrapped key** if the key has been wrapped with the public RSA key.

  5. To encrypt the new snapshot, select an encryption method by supplying an additional encryption key under the **Encryption** section.




###  REST 

To make the request, provide the `sourceDiskEncryptionKey` property to access the source persistent disk. You must encrypt the new snapshot using the `snapshotEncryptionKey` property.

Make a request to the v1 API for a raw (non-RSA wrapped) key, or to the Beta API for a RSA-wrapped key.
    
    
    POST https://compute.googleapis.com/compute/beta/projects/myproject/zones/us-central1-a/disks/example-disk/createSnapshot
    
    {
     "snapshotEncryptionKey":  {
       "rsaEncryptedKey": "ieCx/NcW06PcT7Ep1X6LUTc/hLvUDYyzSZPPVCVPTVEohpeHASqC8uw5TzyO9U+Fka9JFHz0mBibXUInrC/jEk014kCK/NPjYgEMOyssZ4ZINPKxlUh2zn1bV+MCaTICrdmuSBTWlUUiFoDD6PYznLwh8ZNdaheCeZ8ewEXgFQ8V+sDroLaN3Xs3MDTXQEMMoNUXMCZEIpg9Vtp9x2oeQ5lAbtt7bYAAHf5l+gJWw3sUfs0/Glw5fpdjT8Uggrr+RMZezGrltJEF293rvTIjWOEB3z5OHyHwQkvdrPDFcTqsLfh+8Hr8g+mf+7zVPEC8nEbqpdl3GPv3A7AwpFp7MA=="
     },
      "sourceDiskEncryptionKey": {
       "rsaEncryptedKey": "ieCx/NcW06PcT7Ep1X6LUTc/hLvUDYyzSZPPVCVPTVEohpeHASqC8uw5TzyO9U+Fka9JFHz0mBibXUInrC/jEk014kCK/NPjYgEMOyssZ4ZINPKxlUh2zn1bV+MCaTICrdmuSBTWlUUiFoDD6PYznLwh8ZNdaheCeZ8ewEXgFQ8V+sDroLaN3Xs3MDTXQEMMoNUXMCZEIpg9Vtp9x2oeQ5lAbtt7bYAAHf5l+gJWw3sUfs0/Glw5fpdjT8Uggrr+RMZezGrltJEF293rvTIjWOEB3z5OHyHwQkvdrPDFcTqsLfh+8Hr8g+mf+7zVPEC8nEbqpdl3GPv3A7AwpFp7MA=="
      },
     "name": "snapshot-encrypted-disk"
    }
    

The `sourceDiskEncryptionKey` property must match the key used to encrypt the persistent disk. Otherwise, the request fails.

The `snapshotEncryptionKey` lets you supply a key to encrypt the snapshot so that if the snapshot is used to create new persistent disks, a matching key must be provided. This key must follow the preceding key format. You can also choose to leave this property undefined and the snapshot can be used to create new persistent disks without requiring a key.

## Create a new image from a disk or custom image encrypted with CSEK

You can create custom images from encrypted persistent disks or copy encrypted images. You cannot use the console to copy images. Use the Google Cloud CLI or REST to copy images.

###  Console 

  1. Go to the **Images** page.

[Go to Images](https://console.cloud.google.com/compute/images)

  2. Click **Create image**.

  3. Under **Source disk** , choose the encrypted disk you want to create an image of.

  4. Under **Encryption** , select an encryption key management solution.

  5. If the key has been wrapped with the public RSA key, select **Wrapped key**.




###  gcloud 

Follow the instructions to [create an image](https://docs.cloud.google.com/compute/docs/images/create-delete-deprecate-private-images), and add the `--csek-key-file` flag with a path to the encryption key file for the encrypted source object. Use the `gcloud beta` component if you are using an RSA-wrapped key:
    
    
    gcloud (beta) compute images create .... --csek-key-file example-file.json
    

If you want to encrypt the new image with your key, add the key to the key file:
    
    
    [
      {
      "uri": "https://www.googleapis.com/compute/v1/projects/myproject/zones/us-central1-a/disks/source-disk",
      "key": "acX3RqzxrKAFTF0tYVLvydU1riRZTvUNC4g5I11NY-c=",
      "key-type": "raw"
      },
      {
      "uri": "https://www.googleapis.com/compute/v1/projects/myproject/global/snapshots/the-new-image",
      "key": "TF0t-cSfl7CT7xRF1LTbAgi7U6XXUNC4zU_dNgx0nQc=",
      "key-type": "raw"
      }
    ]
    

###  REST 

Your API creation request must contain the encryption key property for your source object. For example, include one of the following properties depending on the source object type:

  * Persistent disk: `sourceDiskEncryptionKey`
  * Image: `sourceImageEncryptionKey`



Also include the `rawKey` or `rsaEncryptedKey` properties depending on key type. Make a request to the v1 API for a raw (non-RSA wrapped) key, or to the Beta API for a RSA-wrapped key. The following example converts an encrypted and RSA-wrapped persistent disk to an image that uses the same encryption key.
    
    
    POST https://compute.googleapis.com/compute/beta/projects/myproject/global/images
    
    {
     "name": "image-encrypted-disk",
     "sourceDiskEncryptionKey": {
        "rsaEncryptedKey": "ieCx/NcW06PcT7Ep1X6LUTc/hLvUDYyzSZPPVCVPTVEohpeHASqC8uw5TzyO9U+Fka9JFHz0mBibXUInrC/jEk014kCK/NPjYgEMOyssZ4ZINPKxlUh2zn1bV+MCaTICrdmuSBTWlUUiFoDD6PYznLwh8ZNdaheCeZ8ewEXgFQ8V+sDroLaN3Xs3MDTXQEMMoNUXMCZEIpg9Vtp9x2oeQ5lAbtt7bYAAHf5l+gJWw3sUfs0/Glw5fpdjT8Uggrr+RMZezGrltJEF293rvTIjWOEB3z5OHyHwQkvdrPDFcTqsLfh+8Hr8g+mf+7zVPEC8nEbqpdl3GPv3A7AwpFp7MA=="
      }
     "imageEncryptionKey": {
        "rsaEncryptedKey":  "ieCx/NcW06PcT7Ep1X6LUTc/hLvUDYyzSZPPVCVPTVEohpeHASqC8uw5TzyO9U+Fka9JFHz0mBibXUInrC/jEk014kCK/NPjYgEMOyssZ4ZINPKxlUh2zn1bV+MCaTICrdmuSBTWlUUiFoDD6PYznLwh8ZNdaheCeZ8ewEXgFQ8V+sDroLaN3Xs3MDTXQEMMoNUXMCZEIpg9Vtp9x2oeQ5lAbtt7bYAAHf5l+gJWw3sUfs0/Glw5fpdjT8Uggrr+RMZezGrltJEF293rvTIjWOEB3z5OHyHwQkvdrPDFcTqsLfh+8Hr8g+mf+7zVPEC8nEbqpdl3GPv3A7AwpFp7MA=="
        },
     "sourceDisk": "projects/myproject/zones/us-central1-a/disks/source-disks"
    }
    

The optional `imageEncryptionKey` property lets you supply a key to encrypt the image so when the image is used to create new persistent disks, a matching key must be provided. This key must follow the same key format described earlier. You can also choose to leave this property undefined and the image can be used to create new persistent disks without requiring a key.

## Encrypt an imported image with CSEK

You can encrypt a new image when you [manually import a custom image](https://docs.cloud.google.com/compute/docs/import/import-existing-image) to Compute Engine. Before you can import an image, you must [create and compress a disk image file](https://docs.cloud.google.com/compute/docs/images/import-existing-image#create_image_file) and [upload that compressed file to Cloud Storage](https://docs.cloud.google.com/storage/docs/cloud-console#_uploadingdata).

Import the custom Compute Engine image that you want to encrypt. Specify the URI to the compressed file and also specify a path to your encryption key file.

###  Console 

  1. Go to the **Images** page.

[Go to Images](https://console.cloud.google.com/compute/images)

  2. Click **Create image**.

  3. Under **Source** , choose **Cloud Storage file**.

  4. Under **Cloud Storage file** , enter the Cloud Storage URI.

  5. Under **Encryption** , choose **Customer-supplied key** and provide the encryption key to encrypt the image in the **Source disk encryption key** field.




###  gcloud 

Use the `compute images create` command to create a new image, and specify the `--csek-key-file` flag with an encryption key file. If you are using an RSA-wrapped key, use the `gcloud beta` component:
    
    
    gcloud (beta) compute images create [IMAGE_NAME] \
        --source-uri gs://[BUCKET_NAME]/[COMPRESSED_FILE] \
        --csek-key-file [KEY_FILE]
    

Replace the following:

  * `[IMAGE_NAME]`: the name for the new custom image.
  * `[BUCKET_NAME]`: the name of the Cloud Storage bucket that holds your compressed image file.
  * `[COMPRESSED_FILE]`: the name of the compressed image file.
  * `[KEY_FILE]`: the path to an encryption key file on your local workstation.



###  REST 

To encrypt a new image created from a RAW file, add the new `imageEncryptionKey` property to the image creation request, followed by either `rawKey` or `rsaEncryptedKey`. Make a request to the v1 API for a raw (non-RSA wrapped) key, or to the Beta API for a RSA-wrapped key.
    
    
    POST https://compute.googleapis.com/compute/beta/projects/myproject/global/images
    
    {
    "rawDisk": {
     "source": "http://storage.googleapis.com/example-image/example-image.tar.gz"
    },
    "name": "new-encrypted-image",
    "sourceType": "RAW",
    "imageEncryptionKey": {
      "rsaEncryptedKey": "ieCx/NcW06PcT7Ep1X6LUTc/hLvUDYyzSZPPVCVPTVEohpeHASqC8uw5TzyO9U+Fka9JFHz0mBibXUInrC/jEk014kCK/NPjYgEMOyssZ4ZINPKxlUh2zn1bV+MCaTICrdmuSBTWlUUiFoDD6PYznLwh8ZNdaheCeZ8ewEXgFQ8V+sDroLaN3Xs3MDTXQEMMoNUXMCZEIpg9Vtp9x2oeQ5lAbtt7bYAAHf5l+gJWw3sUfs0/Glw5fpdjT8Uggrr+RMZezGrltJEF293rvTIjWOEB3z5OHyHwQkvdrPDFcTqsLfh+8Hr8g+mf+7zVPEC8nEbqpdl3GPv3A7AwpFp7MA=="
      }
    }
    

## Create a Persistent Disk from a CSEK-encrypted resource

You can create a Persistent Disk from the following CSEK-encrypted resources:

  * instant snapshots
  * standard snapshots
  * images



### Create a disk from a CSEK-encrypted snapshot

###  Console 

  1. Go to the **Disks** page.

[Go to Disks](https://console.cloud.google.com/compute/disks)

  2. Click **Create disk**.

  3. Under **Source type** , select the type of snapshot:

     * For a standard snapshot, select **Snapshot**.
     * For an instant snapshot, select **Instant snapshot**.
     * For a standard snapshot, select **Archive snapshot**.
  4. Provide the source snapshot's encryption key. In the **Source snapshot encryption key** field, enter the CSEK used to encrypt the source snapshot.

  5. If the key has been wrapped with the public RSA key, select **Wrapped key**.

  6. Optional: if the source snapshot is a standard or archive snapshot, you can choose to configure the encryption for the new disk.

     1. Expand the expand_more **Advanced configurations** section.
     2. Under **Encryption** , select an encryption key management solution. 
        * To use a Google-owned and Google-managed encryption key, select **Google-managed encryption key**.
        * To use a key managed by the Cloud Key Management Service, select **Cloud KMS key**.
  7. Optional: configure backups for the disk in the **Data protection** section.

  8. To create the disk, click **Create**.




###  gcloud 

Use the [`gcloud compute disks create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/disks/create). Provide the encryption key for the snapshot using the `--csek-key-file` flag.

If you are using an RSA-wrapped key, use the `gcloud beta` version of the command.

  * Create a disk from a CSEK-encrypted standard or archive snapshot.


    
    
    gcloud compute disks create ... --source-snapshot example-snapshot \
     --csek-key-file example-file.json
    

  * Create a disk from a CSEK-encrypted instant snapshot:


    
    
    gcloud compute disks create ... --source-instant-snapshot example-instant-snapshot \
      --csek-key-file example-file.json
    

###  REST 

Create a `POST` request to the [`disks.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/disks/insert). To use an encrypted snapshot, supply the `sourceSnapshotEncryptionKey` in your request, followed by `rawKey` or `rsaEncryptedKey`.

If you use RSA-wrapped keys, use the beta version of the [`disks.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/beta/disks/insert).

  * To create a new disk from a standard or archive snapshot that uses an RSA-wrapped key:
        
        POST https://compute.googleapis.com/compute/beta/projects/myproject/zones/us-central1-a/disks
        
        {
        "name": "disk-from-encrypted-snapshot",
        "sourceSnapshot": "global/snapshots/encrypted-snapshot",
        "sourceSnapshotEncryptionKey": {
        "rsaEncryptedKey": "ieCx/NcW06PcT7Ep1X6LUTc/hLvUDYyzSZPPVCVPTVEohpeHASqC8uw5TzyO9U+Fka9JFHz0mBibXUInrC/jEk014kCK/NPjYgEMOyssZ4ZINPKxlUh2zn1bV+MCaTICrdmuSBTWlUUiFoDD6PYznLwh8ZNdaheCeZ8ewEXgFQ8V+sDroLaN3Xs3MDTXQEMMoNUXMCZEIpg9Vtp9x2oeQ5lAbtt7bYAAHf5l+gJWw3sUfs0/Glw5fpdjT8Uggrr+RMZezGrltJEF293rvTIjWOEB3z5OHyHwQkvdrPDFcTqsLfh+8Hr8g+mf+7zVPEC8nEbqpdl3GPv3A7AwpFp7MA=="
        }
        }
        

  * To create a disk from an instant snapshot that uses an RSA-wrapped key:
        
        POST https://compute.googleapis.com/compute/beta/projects/PROJECT/zones/SOURCE_ZONE/disks/insert
        {
          "name": "NEW_DISK_NAME",
          "sourceInstantSnapshot": "projects/PROJECT/zones/SOURCE_ZONE/instantSnapshots/INSTANT_SNAPSHOT_NAME",
          "diskEncryptionKey": {
             "rsaEncryptedKey": "RSA_ENCRYPTED_KEY"
          }
        }
        




### Create a disk from an image encrypted with CSEK

###  Console 

  1. Go to the **Disks** page.

[Go to Disks](https://console.cloud.google.com/compute/disks)

  2. Click **Create disk**.

  3. Under **Source type** , select **Image**.

  4. Under **Encryption** , select an encryption key management solution.

  5. If the key has been wrapped with the public RSA key, select **Wrapped key**.




###  gcloud 

In the `gcloud compute` tool, provide the encryption key for the image using the `--csek-key-file` flag when you create the disk. If you are using an RSA-wrapped key, use the `gcloud beta` component:
    
    
    gcloud (beta) compute disks create ... --image example-image --csek-key-file example-file.json
    

###  REST 

To use an encrypted image, provide the `sourceImageEncryptionKey`, followed by either `rawKey` or `rsaEncryptedKey`. Make a request to the v1 API for a raw (non-RSA wrapped) key, or to the Beta API for a RSA-wrapped key.
    
    
    POST https://compute.googleapis.com/compute/v1/projects/myproject/zones/us-central1-a/disks
    
    {
    "name": "disk-from-encrypted-image",
    "sourceImageEncryptionKey": {
      "rsaEncryptedKey": "ieCx/NcW06PcT7Ep1X6LUTc/hLvUDYyzSZPPVCVPTVEohpeHASqC8uw5TzyO9U+Fka9JFHz0mBibXUInrC/jEk014kCK/NPjYgEMOyssZ4ZINPKxlUh2zn1bV+MCaTICrdmuSBTWlUUiFoDD6PYznLwh8ZNdaheCeZ8ewEXgFQ8V+sDroLaN3Xs3MDTXQEMMoNUXMCZEIpg9Vtp9x2oeQ5lAbtt7bYAAHf5l+gJWw3sUfs0/Glw5fpdjT8Uggrr+RMZezGrltJEF293rvTIjWOEB3z5OHyHwQkvdrPDFcTqsLfh+8Hr8g+mf+7zVPEC8nEbqpdl3GPv3A7AwpFp7MA=="
      },
    "sourceImage": "global/images/encrypted-image"
    }
    

## Attaching a disk encrypted with CSEK to a new VM

###  Console 

  1. Go to the **Create an instance** page.

[Go to Create an instance](https://console.cloud.google.com/compute/instancesAdd)

  2. In the **Boot disk** section, click **Change** , and do the following:

     1. On the **Boot disk** page, click the **Existing disks** tab.
     2. From the **Disk** list, choose an existing encrypted disk to attach to the VM.
     3. Enter the encryption key in the **Source disk decryption key** field. If the key has been wrapped with the public RSA key, select **Wrapped key**.

**Note:** These options appear only when an encrypted disk is selected in the **Disk** list.
     4. Click **Select**.

  3. Continue with the VM creation process.




###  gcloud 

To create a VM and attach an encrypted disk, create a key file and provide the key using the `--csek-key-file` flag when you create the VM. If you are using an RSA-wrapped key, use the `gcloud beta` component:
    
    
    gcloud (beta) compute instances create example-instance \
        --disk name=example-disk,boot=yes \
        --csek-key-file example-file.json
    

###  REST 

[Create a VM](https://docs.cloud.google.com/compute/docs/instances/create-start-instance) using the Compute Engine API and provide either the `rawKey` or `rsaEncryptedKey` with the disk specification. Make a request to the v1 API for a raw (non-RSA wrapped) key, or to the Beta API for a RSA-wrapped key.

Here is a snippet of an example disk specification:
    
    
    "disks": [
    {
      "deviceName": "encrypted-disk",
      "source": "projects/myproject/zones/us-central1-f/disks/encrypted-disk",
      "diskEncryptionKey": {
        "rawKey": "SGVsbG8gZnJvbSBHb29nbGUgQ2xvdWQgUGxhdGZvcm0="
      }
     }
    ]
    

## Starting or restarting VMs that have disks encrypted with CSEK

For details on stopping or starting a VM that has encrypted disks, read [Restarting a VM with an encrypted disk](https://docs.cloud.google.com/compute/docs/instances/stop-start-instance#restarting_an_instance_that_has_encrypted_disks).

## Create resources that have different encryption types

You can create instances and other resources that use a mix of CSEK-, CMEK-, and Google-owned and managed key-encrypted resources. For example, you can create an instance that has a CSEK-encrypted boot disk and a CMEK-encrypted data disk.

To create such resources in a single request with the Google Cloud CLI, you must include the `--no-require-csek-key-create` flag in your request.

You must still specify the CSEK key for any CSEK-encrypted resources with the `--csek-key-file` flag. When you provide both flags, Compute Engine creates any customer-encrypted resources that are explicitly defined in your key file and also creates any standard resources you specify.

For example, assume a key file contains the following:
    
    
    [
      {
      "uri": "https://www.googleapis.com/compute/beta/projects/myproject/zones/us-central1-a/disks/example-disk",
      "key": "ieCx/NcW06PcT7Ep1X6LUTc/hLvUDYyzSZPPVCVPTVEohpeHASqC8uw5TzyO9U+Fka9JFHz0mBibXUInrC/jEk014kCK/NPjYgEMOyssZ4ZINPKxlUh2zn1bV+MCaTICrdmuSBTWlUUiFoDD6PYznLwh8ZNdaheCeZ8ewEXgFQ8V+sDroLaN3Xs3MDTXQEMMoNUXMCZEIpg9Vtp9x2oeQ5lAbtt7bYAAHf5l+gJWw3sUfs0/Glw5fpdjT8Uggrr+RMZezGrltJEF293rvTIjWOEB3z5OHyHwQkvdrPDFcTqsLfh+8Hr8g+mf+7zVPEC8nEbqpdl3GPv3A7AwpFp7MA==",
      "key-type": "rsa-encrypted"
      }
    ]
    

You can simultaneously create two instances, one with a boot disk that's encrypted with a CSEK and the other with a boot disk encrypted with a Google-owned and managed key with the following command:

**Note:** If you are using an RSA-wrapped key, use the `gcloud beta` component.
    
    
    gcloud beta compute instances create example-disk example-disk-2 \
        --csek-key-file mykeyfile.json --no-require-csek-key-create
    

Normally, it wouldn't be possible to create `example-disk-2` if you specified the `--csek-key-file` flag because the disk is not explicitly defined in the key file. By adding the `--no-require-csek-key-create`, both disks are created, one encrypted using the key file, and the other encrypted using Google-owned and managed keys.

## Remove your CSEK from a Persistent Disk

You can decrypt the contents of a customer-encrypted disk and create a new disk that uses Google-owned and managed keys instead.

  1. Create an image of the encrypted disk and specify **automatic** encryption for the new image.
  2. Use the new image to [create a new persistent disk](https://docs.cloud.google.com/compute/docs/disks/add-persistent-disk#create_disk).



After you create the new persistent disk, Compute Engine uses Google-owned and managed keys to protect the disk contents. Any snapshots that you create from that disk must also use Google-owned and managed keys

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
