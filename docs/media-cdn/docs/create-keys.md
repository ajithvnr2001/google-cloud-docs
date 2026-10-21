---
url: https://docs.cloud.google.com/media-cdn/docs/create-keys/
title: Create asymmetric key pairs \u00a0|\u00a0 Media CDN \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:18:21.301150+00:00
---

# Create asymmetric key pairs  |  Media CDN  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/media-cdn/docs/create-keys/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Media CDN ](https://docs.cloud.google.com/media-cdn/docs)
  * [ Guides ](https://docs.cloud.google.com/media-cdn/docs/overview)



Send feedback 

#  Create asymmetric key pairs Stay organized with collections  Save and categorize content based on your preferences. 

This guide demonstrates how to create asymmetric key pairs for Media CDN.

## Generate keys

###  Command line 

You can generate both a private and public key by using Python 3 and OpenSSL 1.1.1 or later (earlier versions of OpenSSL don't support Ed25519).

  1. Generate the private key.
         
         openssl genpkey -algorithm ed25519 -outform PEM -out test.private.key
         

This outputs a PEM-encoded private key. Keep this key secure, ideally by using a key management system or [Secret Manager](https://docs.cloud.google.com/secret-manager).

  2. Generate the public key from the private key in URL-safe base64 format.
         
         openssl pkey -outform DER -pubout -in test.private.key | tail -c +13 | python3 -c "import base64, sys; print(('%s' % base64.urlsafe_b64encode(sys.stdin.buffer.read()))[2:-1])"
         

This command generates the public key from the private key, stripping ASN.1 header information from the raw public key.




###  Python 
    
    
    import base64
    
    from cryptography.hazmat.primitives import serialization
    from cryptography.hazmat.primitives.asymmetric import ed25519
    
    
    def generate_ed25519_keypair(
        private_key_filename: str = "private.key", public_key_filename: str = "public.pub"
    ) -> None:
        """Generate Ed25519 Keys Pairs.
    
        Args:
            private_key_filename(default private.key): private key filename as a string.
            public_key_filename(default public.pub): public key filename as a string
    
        Returns:
    
        """
        private_key = ed25519.Ed25519PrivateKey.generate()
        public_key = private_key.public_key()
    
        private_key_str = private_key.private_bytes(
            encoding=serialization.Encoding.Raw,
            format=serialization.PrivateFormat.Raw,
            encryption_algorithm=serialization.NoEncryption(),
        )
        print("Private Key:\t", base64.urlsafe_b64encode(private_key_str))
    
        public_key_str = public_key.public_bytes(
            encoding=serialization.Encoding.Raw, format=serialization.PublicFormat.Raw
        )
        print("Public Key:\t", base64.urlsafe_b64encode(public_key_str))
    
        with open(private_key_filename, "wb") as fp:
            fp.write(base64.urlsafe_b64encode(private_key_str))
            print(f"Private Key is written to:\t{private_key_filename}")
    
        with open(public_key_filename, "wb") as fp:
            fp.write(base64.urlsafe_b64encode(public_key_str))
            print(f"Public Key is written to:\t{public_key_filename}")
    
    

With the key in this format, you can now [add it to a keyset](https://docs.cloud.google.com/media-cdn/docs/create-keyset). When the keyset is associated with a route as a `cdnPolicy.signedRequestKeyset`, Media CDN validates that the requests were signed before serving any content.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
