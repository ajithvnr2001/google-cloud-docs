---
url: https://docs.cloud.google.com/storage/docs/access-control/signing-urls-manually/
title: V4 signing process with your own program \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:01:32.122682+00:00
---

# V4 signing process with your own program  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/access-control/signing-urls-manually/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Guides ](https://docs.cloud.google.com/storage/docs/discover-object-storage-console)



Send feedback 

#  V4 signing process with your own program Stay organized with collections  Save and categorize content based on your preferences. 

This page describes an algorithm for implementing the V4 signing process so that you can create Cloud Storage RSA key [signed URLs](https://docs.cloud.google.com/storage/docs/access-control/signed-urls) in your own workflow, using a programming language of your choice.

**Note:** In most cases, it's faster and easier to create signed URLs by using the [V4 signing process with Cloud Storage tools](https://docs.cloud.google.com/storage/docs/access-control/signing-urls-with-helpers).

## Before you begin

Before creating a program that implements the V4 signing process, you must complete the following steps:

  1. [Create a service account](https://docs.cloud.google.com/iam/docs/creating-managing-service-accounts#creating_a_service_account). If you already have a service account, you can skip this step. For more information about service accounts, see [Service accounts overview](https://docs.cloud.google.com/iam/docs/service-account-overview).

  2. [Give the service account sufficient permission](https://docs.cloud.google.com/storage/docs/access-control/using-iam-permissions) such that it could perform the request that the signed URL will make.

For example, if your signed URL will allow a user to read object data, the service account must itself have permission to read the object data.

  3. If the [signing algorithm](https://docs.cloud.google.com/storage/docs/authentication/signatures#signing-process) you intend to use is not built into Google Cloud, [generate a new private key](https://docs.cloud.google.com/iam/docs/creating-managing-service-account-keys#creating_service_account_keys), or have an existing private key for the service account. The key can be in either JSON or PKCS12 format.




## Algorithm for signing URLs

Your program should include the following steps:

  1. Construct the _canonical request_ as a string. The canonical request defines elements that users must include in their request when they use your signed URL.

See [Canonical Requests](https://docs.cloud.google.com/storage/docs/authentication/canonical-requests) for details about the parts and format required.

  2. Construct the _string-to-sign_. The string-to-sign is the basis for creating a signature and includes within it the hex-encoded hash value of the canonical request.

See [Signatures](https://docs.cloud.google.com/storage/docs/authentication/signatures) for details about the format of the string-to-sign.

  3. Sign the string-to-sign using an RSA signature with SHA-256. The result of this signing is your _request signature_. There are several options for signing:

     * You can [use the IAM `signBlob` method](https://docs.cloud.google.com/storage/docs/authentication/creating-signatures) provided by Google Cloud.

     * You can use a programming language that has a library for performing RSA signatures.

**Note:** You can also [sign the string-to-sign using HMAC](https://docs.cloud.google.com/storage/docs/authentication/signatures#signing-process) if you are using the XML API for interoperable access.
  4. Construct the _signed URL_ by using the following concatenation:
         
         HOSTNAME + PATH_TO_RESOURCE + "?" + CANONICAL_QUERY_STRING + "&X-Goog-Signature=" + REQUEST_SIGNATURE

The signed URL has the following components:

     * HOSTNAME: This should be `https://storage.googleapis.com`.

     * PATH_TO_RESOURCE: This should match the value you used in constructing the canonical request.

     * CANONICAL_QUERY_STRING: This should match the values you used in constructing the canonical request.

     * REQUEST_SIGNATURE: This is the output from using an RSA signature in the previous step, hex-encoded.

Here is a sample completed URL:
    
    https://storage.googleapis.com/example-bucket/cat.jpeg?X-Goog-Algorithm=GOOG4-
    RSA-SHA256&X-Goog-Credential=example%40example-project.iam.gserviceaccount.com
    %2F20181026%2Fus%2Fstorage%2Fgoog4_request&X-Goog-Date=20181026T211942Z&X-Goog
    -expires=3600&X-Goog-Signedheaders=host&X-Goog-Signature=2d2a6f5055eb004b8690b
    9479883292ae7450cdc15f17d7f99bc49b916f9e7429106ed7e5858ae6b4ab0bbbdb1a8ccc364d
    ad3a0da2caebd30887a70c5b2569d089ceb8afbde3eed4dff5086f0db5483998c175980991fe89
    9fbd2cd8cb813b00165e8d56e0a8aa7b3d7a12ee1baa8400611040f05b50a1a8eab5ba223fe137
    5747748de950ec7a4dc50f8382a6ffd4994ac42498d7daa703d9a414d4475154d0e7edaa92d4f2
    507d92c1f7e8efa7cab64df68b5df48575b9259d8d0bdb5dc752bdf07bd162d98ff2924f2e4a26
    fa6b3cede73ad5333c47d146a21c2ab2d97115986a12c68ff37346d6c2ca83e56b8ec8ad956327
    10b489b75c35697d781c38e




## Python sample program

You can use the Cloud Storage client libraries to create signed URLs for many common programming languages. See [V4 signing process with Cloud Storage tools](https://docs.cloud.google.com/storage/docs/access-control/signing-urls-with-helpers) for examples.

The following sample shows an implementation of the algorithm for signing URLs that does not use the Cloud Storage client libraries. The sample uses the Python programming language but can be adapted to the language of your choice.
    
    
    import binascii
    import collections
    import datetime
    import hashlib
    import sys
    from urllib.parse import quote
    
    # pip install google-auth
    from google.oauth2 import service_account
    
    # pip install six
    import six
    
    
    def generate_signed_url(
        service_account_file,
        bucket_name,
        object_name,
        subresource=None,
        expiration=604800,
        http_method="GET",
        query_parameters=None,
        headers=None,
    ):
        if expiration > 604800:
            print("Expiration Time can't be longer than 604800 seconds (7 days).")
            sys.exit(1)
    
        escaped_object_name = quote(six.ensure_binary(object_name), safe=b"/~")
        canonical_uri = f"/{escaped_object_name}"
    
        datetime_now = datetime.datetime.now(tz=datetime.timezone.utc)
        request_timestamp = datetime_now.strftime("%Y%m%dT%H%M%SZ")
        datestamp = datetime_now.strftime("%Y%m%d")
    
        google_credentials = service_account.Credentials.from_service_account_file(
            service_account_file
        )
        client_email = google_credentials.service_account_email
        credential_scope = f"{datestamp}/auto/storage/goog4_request"
        credential = f"{client_email}/{credential_scope}"
    
        if headers is None:
            headers = dict()
        host = f"{bucket_name}.storage.googleapis.com"
        headers["host"] = host
    
        canonical_headers = ""
        ordered_headers = collections.OrderedDict(sorted(headers.items()))
        for k, v in ordered_headers.items():
            lower_k = str(k).lower()
            strip_v = str(v).lower()
            canonical_headers += f"{lower_k}:{strip_v}\n"
    
        signed_headers = ""
        for k, _ in ordered_headers.items():
            lower_k = str(k).lower()
            signed_headers += f"{lower_k};"
        signed_headers = signed_headers[:-1]  # remove trailing ';'
    
        if query_parameters is None:
            query_parameters = dict()
        query_parameters["X-Goog-Algorithm"] = "GOOG4-RSA-SHA256"
        query_parameters["X-Goog-Credential"] = credential
        query_parameters["X-Goog-Date"] = request_timestamp
        query_parameters["X-Goog-Expires"] = expiration
        query_parameters["X-Goog-SignedHeaders"] = signed_headers
        if subresource:
            query_parameters[subresource] = ""
    
        canonical_query_string = ""
        ordered_query_parameters = collections.OrderedDict(sorted(query_parameters.items()))
        for k, v in ordered_query_parameters.items():
            encoded_k = quote(str(k), safe="")
            encoded_v = quote(str(v), safe="")
            canonical_query_string += f"{encoded_k}={encoded_v}&"
        canonical_query_string = canonical_query_string[:-1]  # remove trailing '&'
    
        canonical_request = "\n".join(
            [
                http_method,
                canonical_uri,
                canonical_query_string,
                canonical_headers,
                signed_headers,
                "UNSIGNED-PAYLOAD",
            ]
        )
    
        canonical_request_hash = hashlib.sha256(canonical_request.encode()).hexdigest()
    
        string_to_sign = "\n".join(
            [
                "GOOG4-RSA-SHA256",
                request_timestamp,
                credential_scope,
                canonical_request_hash,
            ]
        )
    
        # signer.sign() signs using RSA-SHA256 with PKCS1v15 padding
        signature = binascii.hexlify(
            google_credentials.signer.sign(string_to_sign)
        ).decode()
    
        scheme_and_host = "{}://{}".format("https", host)
        signed_url = "{}{}?{}&x-goog-signature={}".format(
            scheme_and_host, canonical_uri, canonical_query_string, signature
        )
    
        return signed_url
    
    

## What's next

  * [Learn how to sign URLs with Cloud Storage tools](https://docs.cloud.google.com/storage/docs/access-control/signing-urls-with-helpers) such as client libraries or the Google Cloud CLI.
  * [Learn more about signed URLs](https://docs.cloud.google.com/storage/docs/access-control/signed-urls).
  * [Learn about canonical requests](https://docs.cloud.google.com/storage/docs/authentication/canonical-requests), which underpin signed URLs.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
