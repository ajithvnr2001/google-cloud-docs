---
url: https://docs.cloud.google.com/storage/docs/samples/storage-generate-encryption-key/
title: Generate an encryption key \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:31:48.246789+00:00
---

# Generate an encryption key  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/samples/storage-generate-encryption-key/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Samples ](https://docs.cloud.google.com/storage/docs/samples)



#  Generate an encryption key Stay organized with collections  Save and categorize content based on your preferences. 

Generate an encryption key.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Use customer-supplied encryption keys](https://docs.cloud.google.com/storage/docs/encryption/using-customer-supplied-keys)



## Code sample

### C++

For more information, see the [Cloud Storage C++ API reference documentation](https://docs.cloud.google.com/cpp/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    // Create a pseudo-random number generator (PRNG), this is included for
    // demonstration purposes only. You should consult your security team about
    // best practices to initialize PRNG. In particular, you should verify that
    // the C++ library and operating system provide enough entropy to meet the
    // security policies in your organization.
    
    // Use the Mersenne-Twister Engine in this example:
    //   https://en.cppreference.com/w/cpp/numeric/random/mersenne_twister_engine
    // Any C++ PRNG can be used below, the choice is arbitrary.
    using GeneratorType = std::mt19937_64;
    
    // Create the default random device to fetch entropy.
    std::random_device rd;
    
    // Compute how much entropy we need to initialize the GeneratorType:
    constexpr auto kRequiredEntropyWords =
        GeneratorType::state_size *
        (GeneratorType::word_size / std::numeric_limits<unsigned int>::digits);
    
    // Capture the entropy bits into a vector.
    std::vector<std::uint64_t> entropy(kRequiredEntropyWords);
    std::generate(entropy.begin(), entropy.end(), [&rd] { return rd(); });
    
    // Create the PRNG with the fetched entropy.
    std::seed_seq seed(entropy.begin(), entropy.end());
    
    // initialized with enough entropy such that the encryption keys are not
    // predictable. Note that the default constructor for all the generators in
    // the C++ standard library produce predictable keys.
    std::mt19937_64 gen(seed);
    
    namespace gcs = ::google::cloud::storage;
    gcs::EncryptionKeyData data = gcs::CreateKeyFromGenerator(gen);
    
    std::cout << "Base64 encoded key = " << data.key << "\n"
              << "Base64 encoded SHA256 of key = " << data.sha256 << "\n";

### C#

For more information, see the [Cloud Storage C# API reference documentation](https://cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    using [Google.Cloud.Storage.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.html);
    using System;
    
    public class GenerateEncryptionKeySample
    {
        public string GenerateEncryptionKey()
        {
            var encryptionKey = [EncryptionKey](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.EncryptionKey.html).[Generate](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.EncryptionKey.html#Google_Cloud_Storage_V1_EncryptionKey_Generate)().[Base64Key](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.EncryptionKey.html#Google_Cloud_Storage_V1_EncryptionKey_Base64Key);
            Console.WriteLine($"Generated Base64-encoded AES-256 encryption key: {encryptionKey}");
            return encryptionKey;
        }
    }

### Go

For more information, see the [Cloud Storage Go API reference documentation](https://pkg.go.dev/cloud.google.com/go/storage). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    import (
    	"crypto/rand"
    	"encoding/base64"
    	"fmt"
    	"io"
    )
    
    // generateEncryptionKey generates a 256 bit (32 byte) AES encryption key and
    // prints the base64 representation.
    func generateEncryptionKey(w io.Writer) error {
    	// This is included for demonstration purposes. You should generate your own
    	// key. Please remember that encryption keys should be handled with a
    	// comprehensive security policy.
    	key := make([]byte, 32)
    	if _, err := rand.Read(key); err != nil {
    		return fmt.Errorf("rand.Read: %w", err)
    	}
    	encryptionKey := base64.StdEncoding.EncodeToString(key)
    	fmt.Fprintf(w, "Generated base64-encoded encryption key: %v\n", encryptionKey)
    	return nil
    }
    

### Java

For more information, see the [Cloud Storage Java API reference documentation](https://cloud.google.com/java/docs/reference/google-cloud-storage/latest/overview). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    import com.google.common.io.BaseEncoding;
    import java.security.SecureRandom;
    
    public class GenerateEncryptionKey {
      /**
       * Generates a 256 bit (32 byte) AES encryption key and prints the base64 representation. This is
       * included for demonstration purposes only. You should generate your own key, and consult your
       * security team about best practices. Please remember that encryption keys should be handled with
       * a comprehensive security policy.
       */
      public static void generateEncryptionKey() {
        byte[] key = new byte[32];
        new SecureRandom().nextBytes(key);
        String encryptionKey = BaseEncoding.base64().encode(key);
    
        System.out.println("Generated Base64-encoded AES-256 encryption key: " + encryptionKey);
      }
    }

### Node.js

For more information, see the [Cloud Storage Node.js API reference documentation](https://cloud.google.com/nodejs/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    const crypto = require('crypto');
    
    function generateEncryptionKey() {
      /**
       * Generates a 256 bit (32 byte) AES encryption key and prints the base64
       * representation.
       *
       * This is included for demonstration purposes. You should generate your own
       * key. Please remember that encryption keys should be handled with a
       * comprehensive security policy.
       */
      const buffer = crypto.randomBytes(32);
      const encodedKey = buffer.toString('base64');
      console.log(`Base 64 encoded encryption key: ${encodedKey}`);
    }
    generateEncryptionKey();

### PHP

For more information, see the [Cloud Storage PHP API reference documentation](https://googleapis.github.io/google-cloud-php/#/docs/google-cloud/latest/storage/storageclient). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    /**
     * Generate a base64 encoded encryption key for Google Cloud Storage.
     */
    function generate_encryption_key(): void
    {
        $key = random_bytes(32);
        $encodedKey = base64_encode($key);
        printf('Your encryption key: %s' . PHP_EOL, $encodedKey);
    }

### Python

For more information, see the [Cloud Storage Python API reference documentation](https://cloud.google.com/python/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    import base64
    import os
    
    
    def generate_encryption_key():
        """Generates a 256 bit (32 byte) AES encryption key and prints the
        base64 representation.
    
        This is included for demonstration purposes. You should generate your own
        key. Please remember that encryption keys should be handled with a
        comprehensive security policy.
        """
        key = os.urandom(32)
        encoded_key = base64.b64encode(key).decode("utf-8")
    
        print(f"Base 64 encoded encryption key: {encoded_key}")
    
    

### Ruby

For more information, see the [Cloud Storage Ruby API reference documentation](https://googleapis.dev/ruby/google-cloud-storage/latest/Google/Cloud/Storage.html). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    def generate_encryption_key
      # Generates a 256 bit (32 byte) AES encryption key and prints the base64 representation.
      #
      # This is included for demonstration purposes. You should generate your own key.
      # Please remember that encryption keys should be handled with a comprehensive security policy.
      require "base64"
      require "openssl"
    
      encryption_key  = OpenSSL::Cipher.new("aes-256-cfb").encrypt.random_key
      encoded_enc_key = Base64.encode64 encryption_key
    
      puts "Sample encryption key: #{encoded_enc_key}"
    end

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=storage). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
