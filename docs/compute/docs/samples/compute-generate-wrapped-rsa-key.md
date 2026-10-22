---
url: https://docs.cloud.google.com/compute/docs/samples/compute-generate-wrapped-rsa-key/
title: Encrypt customer private key with Google public key \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:50:29.516062+00:00
---

# Encrypt customer private key with Google public key  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/samples/compute-generate-wrapped-rsa-key/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Samples ](https://docs.cloud.google.com/compute/docs/samples)



#  Encrypt customer private key with Google public key Stay organized with collections  Save and categorize content based on your preferences. 

This sample demonstrates how to encrypt a customer private key with the Google public key, ensuring that only Google can decrypt it.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Encrypt disks with customer-supplied encryption keys](https://docs.cloud.google.com/compute/docs/disks/customer-supplied-encryption)



## Code sample

### Python

Before trying this sample, follow the Python setup instructions in the [Compute Engine quickstart using client libraries](https://docs.cloud.google.com/compute/docs/api/using-libraries). For more information, see the [Compute Engine Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/compute/latest). 

To authenticate to Compute Engine, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=computeengine). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
