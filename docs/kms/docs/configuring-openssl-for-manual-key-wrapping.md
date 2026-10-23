---
url: https://docs.cloud.google.com/kms/docs/configuring-openssl-for-manual-key-wrapping/
title: Configuring OpenSSL for manual key wrapping \u00a0|\u00a0 Cloud Key Management Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:36:27.544802+00:00
---

# Configuring OpenSSL for manual key wrapping  |  Cloud Key Management Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kms/docs/configuring-openssl-for-manual-key-wrapping/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Cloud KMS ](https://docs.cloud.google.com/kms/docs)
  * [ Guides ](https://docs.cloud.google.com/kms/docs/key-management-service)



Send feedback 

#  Configuring OpenSSL for manual key wrapping Stay organized with collections  Save and categorize content based on your preferences. 

Before you can import a key into Cloud KMS, it must be wrapped using the [PKCS#11](https://docs.oasis-open.org/pkcs11/pkcs11-curr/v2.40/cos01/pkcs11-curr-v2.40-cos01.html#_Toc408226908) `CKM_RSA_AES_KEY_WRAP` scheme, which includes both `RSA-OAEP` (which is included in OpenSSL 1.1 by default) and AES Key Wrap with Padding (which is not). That mechanism is not included in OpenSSL.

We recommend using the Google Cloud CLI to [wrap each key automatically](https://docs.cloud.google.com/kms/docs/importing-a-key#request_import) during the import. If you must wrap your keys manually due to compliance or regulatory requirements, you must first recompile OpenSSL to add support for AES Key Wrap with Padding. After recompiling OpenSSL, you can [wrap the key manually](https://docs.cloud.google.com/kms/docs/wrapping-a-key).

**Important:** If you use automatic wrapping, do not follow these steps. Instead, you need to [install the Pyca cryptographic library](https://docs.cloud.google.com/kms/docs/crypto), which works with the OpenSSL binaries already installed on your local system. The Google Cloud CLI can use that library to automatically wrap your key during the import request.

## Before you begin

**Caution:** These steps require advanced knowledge of Linux. Most users should allow the Google Cloud CLI command to [automatically wrap and import](https://docs.cloud.google.com/kms/docs/importing-a-key#automatically_wrap_and_import) keys instead of following the instructions in this topic.

Do not overwrite your system's built-in OpenSSL binaries with the patched binaries produced by following the procedures in this topic. For example, do not install the patched OpenSSL directly into `/usr`. If you follow this procedure exactly, the patched OpenSSL is built in `$HOME/build` and installed into `$HOME/local/bin`.

If `${HOME}/local/bin` already exists, back up its contents or move those files elsewhere before following the steps in this topic.

## Patch and install OpenSSL v1.1.0

If you choose to use OpenSSL to manually wrap your keys before importing them into Cloud KMS, OpenSSL v1.1.0 is required, with the following patch applied. You will need to compile OpenSSL and install it into a location separate from your system's default OpenSSL installation.

  1. Download the source for OpenSSL 1.1.0l release from [https://www.openssl.org/source](https://www.openssl.org/source/old/1.1.0/openssl-1.1.0l.tar.gz). This is the latest release in the 1.1.0 code line. Do not use a newer version of OpenSSL, such as v1.1.1, in this procedure. The patch will fail to apply.

  2. Extract the archive to `${HOME}/build/openssl/` using the following command. This command overrides the default directory, which includes the version of OpenSSL and changes often. Replace /path/to/downloaded-openssl.tar.gz with the path to the downloaded `.tar.gz` archive.
         
         # Create the directory for the eventual OpenSSL binaries
         mkdir -p ${HOME}/local/ssl
         
         # Create the build directory
         mkdir -p ${HOME}/build/openssl
         
         # Extract the archive to ${HOME}/build/openssl
         tar xzvf /path/to/downloaded-openssl.tar.gz \
           -C ${HOME}/build/openssl/ \
           --strip-components 1
         

  3. Apply a custom patch to the extracted OpenSSL source, using the following commands.The patch enables the `EVP_CIPHER_CTX_FLAG_WRAP_ALLOW` flag.

**Warning:** This patch fails to apply to versions of OpenSSL other than v1.1.0l.
         
         cd ${HOME}/build
         cat <<-EOF | patch -d . -p0
         --- orig/openssl/apps/enc.c 2020-01-17 14:39:54.991708785 -0500
         +++ openssl/apps/enc.c  2020-01-17 14:41:33.215704269 -0500
         @@ -482,6 +482,7 @@
                   */
         
                  BIO_get_cipher_ctx(benc, &ctx);
         +   EVP_CIPHER_CTX_set_flags(ctx, EVP_CIPHER_CTX_FLAG_WRAP_ALLOW);
         
                  if (!EVP_CipherInit_ex(ctx, cipher, NULL, NULL, NULL, enc)) {
                      BIO_printf(bio_err, "Error setting cipher %s\n",
         EOF
         

  4. Run the following commands to build the OpenSSL binaries and libraries from the patched source, test the build for validity, and install the binaries and libraries into the `${HOME}/local` directory.
         
         CPUS=$(getconf _NPROCESSORS_ONLN)
         cd ${HOME}/build/openssl
         ./config --prefix=${HOME}/local --openssldir=${HOME}/local/ssl
         make -j${CPUS}
         make test
         make install
         

Do not omit or modify the `--prefix` or `--openssldir` flags, to ensure that you do not overwrite the system's OpenSSL installation.

  5. Run the following command to check that the new OpenSSL binary installed successfully:
         
         test -x ${HOME}/local/bin/openssl || echo FAIL
         

You should see no output if the binaries are installed correctly. If you see `FAIL`, check the output of the `make`, `make test`, and `make install` commands you ran earlier.

  6. The patched OpenSSL binaries are dynamically linked against the OpenSSL libraries in `${HOME}/local/ssl/lib/`, but the `ld` command does not index these libraries by default. Run the following commands to create a wrapper script that adds the patched libraries to the `${LD_LIBRARY_PATH}` before invoking the CLI for the patched OpenSSL.
         
         cat > ${HOME}/local/bin/openssl.sh <<-EOF
         #!/bin/bash
         env LD_LIBRARY_PATH=${HOME}/local/lib/ ${HOME}/local/bin/openssl "\$@"
         EOF
         chmod u+x ${HOME}/local/bin/openssl.sh
         

  7. Check that the version of OpenSSL that the script starts is the version you just built and installed, using the following command:
         
         ${HOME}/local/bin/openssl.sh version
         




You can now invoke the `${HOME}/local/bin/openssl.sh` wrapper script to [manually wrap keys for import](https://docs.cloud.google.com/kms/docs/wrapping-a-key).

[ Previous arrow_back  Format a key for import  ](https://docs.cloud.google.com/kms/docs/formatting-keys-for-import)

[ Next Wrap a key using OpenSSL  arrow_forward  ](https://docs.cloud.google.com/kms/docs/wrapping-a-key)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
