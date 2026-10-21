---
url: https://docs.cloud.google.com/identity-platform/docs/migrating-users/
title: Migrating users from an existing app \u00a0|\u00a0 Identity Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T01:49:20.846064+00:00
---

# Migrating users from an existing app  |  Identity Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/identity-platform/docs/migrating-users/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Identity Platform ](https://docs.cloud.google.com/identity-platform/docs)
  * [ Guides ](https://docs.cloud.google.com/identity-platform/docs/how-to)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Migrating users from an existing app

This document shows you how to migrate users from an existing app to Identity Platform.

## Before you begin

  * [Enable and configure Identity Platform](https://docs.cloud.google.com/identity-platform/docs/quickstart-cicp).

  * [Install the Admin SDK](https://docs.cloud.google.com/identity-platform/docs/install-admin-sdk).

  * [Install the Firebase command-line interface](https://firebase.google.com/docs/cli/index#install_the_firebase_cli).




## Using the Admin SDK

The Admin SDK lets you import users without exporting user data to CSV or JSON. You can import users to all of the providers Identity Platform supports, including OAuth, SAML, and OIDC.

Up to 1000 users can be imported in a single API call. The import operation is optimized for speed and does not check for duplicate fields. Importing a user that collides with an existing `uid` will replace the existing user. Importing a user with any other field duplicated (such as `email`) will result in an additional user with the same value.

The Admin SDK attempts to upload the entire list of provided users, even when a user-specific error occurs. The operation returns a result with the summary of successful and failed imports. Error details are returned per failed user import.

### Importing users with HMAC hashed passwords

HMAC hashing algorithms include `HMAC_MD5`, `HMAC_SHA1`, `HMAC_SHA256` and `HMAC_SHA512`. You'll need to provide the hash signer key.

### Node.js
    
    
    getAuth()
      .importUsers(
        [
          {
            uid: 'some-uid',
            email: 'user@example.com',
            // Must be provided in a byte buffer.
            passwordHash: Buffer.from('password-hash'),
            // Must be provided in a byte buffer.
            passwordSalt: Buffer.from('salt'),
          },
        ],
        {
          hash: {
            algorithm: 'HMAC_SHA256',
            // Must be provided in a byte buffer.
            key: Buffer.from('secret'),
          },
        }
      )
      .then((results) => {
        results.errors.forEach((indexedError) => {
          console.log(`Error importing user ${indexedError.index}`);
        });
      })
      .catch((error) => {
        console.log('Error importing users :', error);
      });
    
    [import_users.js](https://github.com/firebase/snippets-node/blob/7cb8d0ffc824d22d8d586425659d5860f26cbb28/auth/import_users.js#L52-L79)

### Java
    
    
    try {
      List<ImportUserRecord> users = Collections.singletonList(ImportUserRecord.builder()
          .setUid("some-uid")
          .setEmail("user@example.com")
          .setPasswordHash("password-hash".getBytes())
          .setPasswordSalt("salt".getBytes())
          .build());
      UserImportOptions options = UserImportOptions.withHash(
          HmacSha256.builder()
              .setKey("secret".getBytes())
              .build());
      UserImportResult result = FirebaseAuth.getInstance().importUsers(users, options);
      for (ErrorInfo indexedError : result.getErrors()) {
        System.out.println("Failed to import user: " + indexedError.getReason());
      }
    } catch (FirebaseAuthException e) {
      System.out.println("Error importing users: " + e.getMessage());
    }
    
    [FirebaseAuthSnippets.java](https://github.com/firebase/firebase-admin-java/blob/2225373d97869e72b164a4081968027c130c782b/src/test/java/com/google/firebase/snippets/FirebaseAuthSnippets.java#L476-L493)

### Python
    
    
    users = [
        auth.ImportUserRecord(
            uid='some-uid',
            email='user@example.com',
            password_hash=b'password_hash',
            password_salt=b'salt'
        ),
    ]
    
    hash_alg = auth.UserImportHash.hmac_sha256(key=b'secret')
    try:
        result = auth.import_users(users, hash_alg=hash_alg)
        for err in result.errors:
            print('Failed to import user:', err.reason)
    except exceptions.FirebaseError as error:
        print('Error importing users:', error)
    
    [index.py](https://github.com/firebase/firebase-admin-python/blob/de456071dc7450a6d7715667debf6049f38fd85d/snippets/auth/index.py#L490-L505)

### Go
    
    
    users := []*auth.UserToImport{
    	(&auth.UserToImport{}).
    		UID("some-uid").
    		Email("user@example.com").
    		PasswordHash([]byte("password-hash")).
    		PasswordSalt([]byte("salt")),
    }
    h := hash.HMACSHA256{
    	Key: []byte("secret"),
    }
    result, err := client.ImportUsers(ctx, users, auth.WithHash(h))
    if err != nil {
    	log.Fatalln("Error importing users", err)
    }
    for _, e := range result.Errors {
    	log.Println("Failed to import user", e.Reason)
    }
    
    [auth.go](https://github.com/firebase/firebase-admin-go/blob/66a72c371b4dbc592317ab7e7f99ce00d76c62ae/snippets/auth.go#L467-L483)

### Importing users with MD5, SHA and PBKDF hashed passwords

MD5, SHA and PBKDF hashing algorithms include `MD5`, `SHA1`, `SHA256`, `SHA512`, `PBKDF_SHA1` and `PBKDF2_SHA256`. You'll need to provide the rounds used to hash the password (between 0 and 8192 for `MD5`, between 1 and 8192 for `SHA1`, `SHA256` and `SHA512`, and between 0 and 120000 for `PBKDF_SHA1` and `PBKDF2_SHA256`).

### Node.js
    
    
    getAuth()
      .importUsers(
        [
          {
            uid: 'some-uid',
            email: 'user@example.com',
            // Must be provided in a byte buffer.
            passwordHash: Buffer.from('password-hash'),
            // Must be provided in a byte buffer.
            passwordSalt: Buffer.from('salt'),
          },
        ],
        {
          hash: {
            algorithm: 'PBKDF2_SHA256',
            rounds: 100000,
          },
        }
      )
      .then((results) => {
        results.errors.forEach((indexedError) => {
          console.log(`Error importing user ${indexedError.index}`);
        });
      })
      .catch((error) => {
        console.log('Error importing users :', error);
      });
    
    [import_users.js](https://github.com/firebase/snippets-node/blob/7cb8d0ffc824d22d8d586425659d5860f26cbb28/auth/import_users.js#L83-L109)

### Java
    
    
    try {
      List<ImportUserRecord> users = Collections.singletonList(ImportUserRecord.builder()
          .setUid("some-uid")
          .setEmail("user@example.com")
          .setPasswordHash("password-hash".getBytes())
          .setPasswordSalt("salt".getBytes())
          .build());
      UserImportOptions options = UserImportOptions.withHash(
          Pbkdf2Sha256.builder()
              .setRounds(100000)
              .build());
      UserImportResult result = FirebaseAuth.getInstance().importUsers(users, options);
      for (ErrorInfo indexedError : result.getErrors()) {
        System.out.println("Failed to import user: " + indexedError.getReason());
      }
    } catch (FirebaseAuthException e) {
      System.out.println("Error importing users: " + e.getMessage());
    }
    
    [FirebaseAuthSnippets.java](https://github.com/firebase/firebase-admin-java/blob/2225373d97869e72b164a4081968027c130c782b/src/test/java/com/google/firebase/snippets/FirebaseAuthSnippets.java#L499-L516)

### Python
    
    
    users = [
        auth.ImportUserRecord(
            uid='some-uid',
            email='user@example.com',
            password_hash=b'password_hash',
            password_salt=b'salt'
        ),
    ]
    
    hash_alg = auth.UserImportHash.pbkdf2_sha256(rounds=100000)
    try:
        result = auth.import_users(users, hash_alg=hash_alg)
        for err in result.errors:
            print('Failed to import user:', err.reason)
    except exceptions.FirebaseError as error:
        print('Error importing users:', error)
    
    [index.py](https://github.com/firebase/firebase-admin-python/blob/de456071dc7450a6d7715667debf6049f38fd85d/snippets/auth/index.py#L510-L525)

### Go
    
    
    users := []*auth.UserToImport{
    	(&auth.UserToImport{}).
    		UID("some-uid").
    		Email("user@example.com").
    		PasswordHash([]byte("password-hash")).
    		PasswordSalt([]byte("salt")),
    }
    h := hash.PBKDF2SHA256{
    	Rounds: 100000,
    }
    result, err := client.ImportUsers(ctx, users, auth.WithHash(h))
    if err != nil {
    	log.Fatalln("Error importing users", err)
    }
    for _, e := range result.Errors {
    	log.Println("Failed to import user", e.Reason)
    }
    
    [auth.go](https://github.com/firebase/firebase-admin-go/blob/66a72c371b4dbc592317ab7e7f99ce00d76c62ae/snippets/auth.go#L489-L505)

### Importing users with standard SCRYPT hashed passwords

The Admin SDK supports the standard `SCRYPT` algorithm as well as an [internal modified version](https://github.com/firebase/scrypt). The following parameters are required:

  * `memoryCost`: The CPU/memory cost of the hashing algorithm.
  * `parallelization`: The parallelization of the hashing algorithm.
  * `blockSize`: The block size (normally 8) of the hashing algorithm.
  * `derivedKeyLength`: The derived key length of the hashing algorithm.




### Node.js
    
    
    getAuth()
      .importUsers(
        [
          {
            uid: 'some-uid',
            email: 'user@example.com',
            // Must be provided in a byte buffer.
            passwordHash: Buffer.from('password-hash'),
            // Must be provided in a byte buffer.
            passwordSalt: Buffer.from('salt'),
          },
        ],
        {
          hash: {
            algorithm: 'STANDARD_SCRYPT',
            memoryCost: 1024,
            parallelization: 16,
            blockSize: 8,
            derivedKeyLength: 64,
          },
        }
      )
      .then((results) => {
        results.errors.forEach((indexedError) => {
          console.log(`Error importing user ${indexedError.index}`);
        });
      })
      .catch((error) => {
        console.log('Error importing users :', error);
      });
    
    [import_users.js](https://github.com/firebase/snippets-node/blob/7cb8d0ffc824d22d8d586425659d5860f26cbb28/auth/import_users.js#L113-L142)

### Java
    
    
    try {
      List<ImportUserRecord> users = Collections.singletonList(ImportUserRecord.builder()
          .setUid("some-uid")
          .setEmail("user@example.com")
          .setPasswordHash("password-hash".getBytes())
          .setPasswordSalt("salt".getBytes())
          .build());
      UserImportOptions options = UserImportOptions.withHash(
          StandardScrypt.builder()
              .setMemoryCost(1024)
              .setParallelization(16)
              .setBlockSize(8)
              .setDerivedKeyLength(64)
              .build());
      UserImportResult result = FirebaseAuth.getInstance().importUsers(users, options);
      for (ErrorInfo indexedError : result.getErrors()) {
        System.out.println("Failed to import user: " + indexedError.getReason());
      }
    } catch (FirebaseAuthException e) {
      System.out.println("Error importing users: " + e.getMessage());
    }
    
    [FirebaseAuthSnippets.java](https://github.com/firebase/firebase-admin-java/blob/2225373d97869e72b164a4081968027c130c782b/src/test/java/com/google/firebase/snippets/FirebaseAuthSnippets.java#L522-L542)

### Python
    
    
    users = [
        auth.ImportUserRecord(
            uid='some-uid',
            email='user@example.com',
            password_hash=b'password_hash',
            password_salt=b'salt'
        ),
    ]
    
    hash_alg = auth.UserImportHash.standard_scrypt(
        memory_cost=1024, parallelization=16, block_size=8, derived_key_length=64)
    try:
        result = auth.import_users(users, hash_alg=hash_alg)
        for err in result.errors:
            print('Failed to import user:', err.reason)
    except exceptions.FirebaseError as error:
        print('Error importing users:', error)
    
    [index.py](https://github.com/firebase/firebase-admin-python/blob/de456071dc7450a6d7715667debf6049f38fd85d/snippets/auth/index.py#L530-L546)

### Go
    
    
    users := []*auth.UserToImport{
    	(&auth.UserToImport{}).
    		UID("some-uid").
    		Email("user@example.com").
    		PasswordHash([]byte("password-hash")).
    		PasswordSalt([]byte("salt")),
    }
    h := hash.StandardScrypt{
    	MemoryCost:       1024,
    	Parallelization:  16,
    	BlockSize:        8,
    	DerivedKeyLength: 64,
    }
    result, err := client.ImportUsers(ctx, users, auth.WithHash(h))
    if err != nil {
    	log.Fatalln("Error importing users", err)
    }
    for _, e := range result.Errors {
    	log.Println("Failed to import user", e.Reason)
    }
    
    [auth.go](https://github.com/firebase/firebase-admin-go/blob/66a72c371b4dbc592317ab7e7f99ce00d76c62ae/snippets/auth.go#L511-L530)

### Importing users with Identity Platform SCRYPT hashed passwords

Identity Platform and Firebase use a [modified version](https://github.com/firebase/scrypt) of the `SCRYPT` algorithm. If you need to migrate users from Firebase to Identity Platform, or from one Identity Platform project to another, you'll need the internal hash parameters.

To access the parameters in Identity Platform:

  1. Open the [**Users**](https://console.cloud.google.com/customer-identity/users) page in the Google Cloud console.
  2. Click **Import Users**. The password hash parameters appear.



To access the parameters in Firebase:

  1. Open the [**Users**](https://console.firebase.google.com/project/_/authentication/users) tab in the Firebase Console.

  2. Select **Password Hash Parameters** from drop down in the upper-right hand corner of the list of users. The password hash parameters appear.




In your code, you'll need to supply the following:

  * `key`: The signer key normally provided in `base64` encoding.
  * `saltSeparator`: (Optional) The salt separator normally provided in `base64` encoding.
  * `rounds`: The number of rounds used to hash the passwords.
  * `memoryCost`: The memory cost required for this algorithm.




### Node.js
    
    
    getAuth()
      .importUsers(
        [
          {
            uid: 'some-uid',
            email: 'user@example.com',
            // Must be provided in a byte buffer.
            passwordHash: Buffer.from('base64-password-hash', 'base64'),
            // Must be provided in a byte buffer.
            passwordSalt: Buffer.from('base64-salt', 'base64'),
          },
        ],
        {
          hash: {
            algorithm: 'SCRYPT',
            // All the parameters below can be obtained from the Firebase Console's users section.
            // Must be provided in a byte buffer.
            key: Buffer.from('base64-secret', 'base64'),
            saltSeparator: Buffer.from('base64SaltSeparator', 'base64'),
            rounds: 8,
            memoryCost: 14,
          },
        }
      )
      .then((results) => {
        results.errors.forEach((indexedError) => {
          console.log(`Error importing user ${indexedError.index}`);
        });
      })
      .catch((error) => {
        console.log('Error importing users :', error);
      });
    
    [import_users.js](https://github.com/firebase/snippets-node/blob/7cb8d0ffc824d22d8d586425659d5860f26cbb28/auth/import_users.js#L173-L204)

### Java
    
    
    try {
      List<ImportUserRecord> users = Collections.singletonList(ImportUserRecord.builder()
          .setUid("some-uid")
          .setEmail("user@example.com")
          .setPasswordHash(BaseEncoding.base64().decode("password-hash"))
          .setPasswordSalt(BaseEncoding.base64().decode("salt"))
          .build());
      UserImportOptions options = UserImportOptions.withHash(
          Scrypt.builder()
              // All the parameters below can be obtained from the Firebase Console's "Users"
              // section. Base64 encoded parameters must be decoded into raw bytes.
              .setKey(BaseEncoding.base64().decode("base64-secret"))
              .setSaltSeparator(BaseEncoding.base64().decode("base64-salt-separator"))
              .setRounds(8)
              .setMemoryCost(14)
              .build());
      UserImportResult result = FirebaseAuth.getInstance().importUsers(users, options);
      for (ErrorInfo indexedError : result.getErrors()) {
        System.out.println("Failed to import user: " + indexedError.getReason());
      }
    } catch (FirebaseAuthException e) {
      System.out.println("Error importing users: " + e.getMessage());
    }
    
    [FirebaseAuthSnippets.java](https://github.com/firebase/firebase-admin-java/blob/2225373d97869e72b164a4081968027c130c782b/src/test/java/com/google/firebase/snippets/FirebaseAuthSnippets.java#L568-L590)

### Python
    
    
    users = [
        auth.ImportUserRecord(
            uid='some-uid',
            email='user@example.com',
            password_hash=base64.urlsafe_b64decode('password_hash'),
            password_salt=base64.urlsafe_b64decode('salt')
        ),
    ]
    
    # All the parameters below can be obtained from the Firebase Console's "Users"
    # section. Base64 encoded parameters must be decoded into raw bytes.
    hash_alg = auth.UserImportHash.scrypt(
        key=base64.b64decode('base64_secret'),
        salt_separator=base64.b64decode('base64_salt_separator'),
        rounds=8,
        memory_cost=14
    )
    try:
        result = auth.import_users(users, hash_alg=hash_alg)
        for err in result.errors:
            print('Failed to import user:', err.reason)
    except exceptions.FirebaseError as error:
        print('Error importing users:', error)
    
    [index.py](https://github.com/firebase/firebase-admin-python/blob/de456071dc7450a6d7715667debf6049f38fd85d/snippets/auth/index.py#L571-L593)

### Go
    
    
    b64URLdecode := func(s string) []byte {
    	b, err := base64.URLEncoding.DecodeString(s)
    	if err != nil {
    		log.Fatalln("Failed to decode string", err)
    	}
    
    	return b
    }
    b64Stddecode := func(s string) []byte {
    	b, err := base64.StdEncoding.DecodeString(s)
    	if err != nil {
    		log.Fatalln("Failed to decode string", err)
    	}
    	return b
    }
    // Users retrieved from Firebase Auth's backend need to be base64URL decoded
    users := []*auth.UserToImport{
    	(&auth.UserToImport{}).
    		UID("some-uid").
    		Email("user@example.com").
    		PasswordHash(b64URLdecode("password-hash")).
    		PasswordSalt(b64URLdecode("salt")),
    }
    
    // All the parameters below can be obtained from the Firebase Console's "Users"
    // section. Base64 encoded parameters must be decoded into raw bytes.
    h := hash.Scrypt{
    	Key:           b64Stddecode("base64-secret"),
    	SaltSeparator: b64Stddecode("base64-salt-separator"),
    	Rounds:        8,
    	MemoryCost:    14,
    }
    result, err := client.ImportUsers(ctx, users, auth.WithHash(h))
    if err != nil {
    	log.Fatalln("Error importing users", err)
    }
    for _, e := range result.Errors {
    	log.Println("Failed to import user", e.Reason)
    }
    
    [auth.go](https://github.com/firebase/firebase-admin-go/blob/66a72c371b4dbc592317ab7e7f99ce00d76c62ae/snippets/auth.go#L556-L594)

### Importing users with BCRYPT hashed passwords

No additional parameters or password salts are required for `BCRYPT` hashed passwords.

### Node.js
    
    
    getAuth()
      .importUsers(
        [
          {
            uid: 'some-uid',
            email: 'user@example.com',
            // Must be provided in a byte buffer.
            passwordHash: Buffer.from('password-hash'),
          },
        ],
        {
          hash: {
            algorithm: 'BCRYPT',
          },
        }
      )
      .then((results) => {
        results.errors.forEach((indexedError) => {
          console.log(`Error importing user ${indexedError.index}`);
        });
      })
      .catch((error) => {
        console.log('Error importing users :', error);
      });
    
    [import_users.js](https://github.com/firebase/snippets-node/blob/7cb8d0ffc824d22d8d586425659d5860f26cbb28/auth/import_users.js#L146-L169)

### Java
    
    
    try {
      List<ImportUserRecord> users = Collections.singletonList(ImportUserRecord.builder()
          .setUid("some-uid")
          .setEmail("user@example.com")
          .setPasswordHash("password-hash".getBytes())
          .setPasswordSalt("salt".getBytes())
          .build());
      UserImportOptions options = UserImportOptions.withHash(Bcrypt.getInstance());
      UserImportResult result = FirebaseAuth.getInstance().importUsers(users, options);
      for (ErrorInfo indexedError : result.getErrors()) {
        System.out.println("Failed to import user: " + indexedError.getReason());
      }
    } catch (FirebaseAuthException e) {
      System.out.println("Error importing users: " + e.getMessage());
    }
    
    [FirebaseAuthSnippets.java](https://github.com/firebase/firebase-admin-java/blob/2225373d97869e72b164a4081968027c130c782b/src/test/java/com/google/firebase/snippets/FirebaseAuthSnippets.java#L548-L562)

### Python
    
    
    users = [
        auth.ImportUserRecord(
            uid='some-uid',
            email='user@example.com',
            password_hash=b'password_hash',
            password_salt=b'salt'
        ),
    ]
    
    hash_alg = auth.UserImportHash.bcrypt()
    try:
        result = auth.import_users(users, hash_alg=hash_alg)
        for err in result.errors:
            print('Failed to import user:', err.reason)
    except exceptions.FirebaseError as error:
        print('Error importing users:', error)
    
    [index.py](https://github.com/firebase/firebase-admin-python/blob/de456071dc7450a6d7715667debf6049f38fd85d/snippets/auth/index.py#L551-L566)

### Go
    
    
    users := []*auth.UserToImport{
    	(&auth.UserToImport{}).
    		UID("some-uid").
    		Email("user@example.com").
    		PasswordHash([]byte("password-hash")).
    		PasswordSalt([]byte("salt")),
    }
    h := hash.Bcrypt{}
    result, err := client.ImportUsers(ctx, users, auth.WithHash(h))
    if err != nil {
    	log.Fatalln("Error importing users", err)
    }
    for _, e := range result.Errors {
    	log.Println("Failed to import user", e.Reason)
    }
    
    [auth.go](https://github.com/firebase/firebase-admin-go/blob/66a72c371b4dbc592317ab7e7f99ce00d76c62ae/snippets/auth.go#L536-L550)

### Importing users without passwords

If your users authenticate with an external identity provider using OAuth, SAML, or OIDC, you won't have direct access to their password.

### Node.js
    
    
    getAuth()
      .importUsers([
        {
          uid: 'some-uid',
          displayName: 'John Doe',
          email: 'johndoe@gmail.com',
          photoURL: 'http://www.example.com/12345678/photo.png',
          emailVerified: true,
          phoneNumber: '+11234567890',
          // Set this user as admin.
          customClaims: { admin: true },
          // User with Google provider.
          providerData: [
            {
              uid: 'google-uid',
              email: 'johndoe@gmail.com',
              displayName: 'John Doe',
              photoURL: 'http://www.example.com/12345678/photo.png',
              providerId: 'google.com',
            },
          ],
        },
      ])
      .then((results) => {
        results.errors.forEach((indexedError) => {
          console.log(`Error importing user ${indexedError.index}`);
        });
      })
      .catch((error) => {
        console.log('Error importing users :', error);
      });
    
    [import_users.js](https://github.com/firebase/snippets-node/blob/7cb8d0ffc824d22d8d586425659d5860f26cbb28/auth/import_users.js#L208-L238)

### Java
    
    
    try {
      List<ImportUserRecord> users = Collections.singletonList(ImportUserRecord.builder()
          .setUid("some-uid")
          .setDisplayName("John Doe")
          .setEmail("johndoe@gmail.com")
          .setPhotoUrl("http://www.example.com/12345678/photo.png")
          .setEmailVerified(true)
          .setPhoneNumber("+11234567890")
          .putCustomClaim("admin", true) // set this user as admin
          .addUserProvider(UserProvider.builder() // user with Google provider
              .setUid("google-uid")
              .setEmail("johndoe@gmail.com")
              .setDisplayName("John Doe")
              .setPhotoUrl("http://www.example.com/12345678/photo.png")
              .setProviderId("google.com")
              .build())
          .build());
      UserImportResult result = FirebaseAuth.getInstance().importUsers(users);
      for (ErrorInfo indexedError : result.getErrors()) {
        System.out.println("Failed to import user: " + indexedError.getReason());
      }
    } catch (FirebaseAuthException e) {
      System.out.println("Error importing users: " + e.getMessage());
    }
    
    [FirebaseAuthSnippets.java](https://github.com/firebase/firebase-admin-java/blob/2225373d97869e72b164a4081968027c130c782b/src/test/java/com/google/firebase/snippets/FirebaseAuthSnippets.java#L625-L648)

### Python
    
    
    users = [
        auth.ImportUserRecord(
            uid='some-uid',
            display_name='John Doe',
            email='johndoe@gmail.com',
            photo_url='http://www.example.com/12345678/photo.png',
            email_verified=True,
            phone_number='+11234567890',
            custom_claims={'admin': True}, # set this user as admin
            provider_data=[ # user with Google provider
                auth.UserProvider(
                    uid='google-uid',
                    email='johndoe@gmail.com',
                    display_name='John Doe',
                    photo_url='http://www.example.com/12345678/photo.png',
                    provider_id='google.com'
                )
            ],
        ),
    ]
    try:
        result = auth.import_users(users)
        for err in result.errors:
            print('Failed to import user:', err.reason)
    except exceptions.FirebaseError as error:
        print('Error importing users:', error)
    
    [index.py](https://github.com/firebase/firebase-admin-python/blob/de456071dc7450a6d7715667debf6049f38fd85d/snippets/auth/index.py#L598-L623)

### Go
    
    
    users := []*auth.UserToImport{
    	(&auth.UserToImport{}).
    		UID("some-uid").
    		DisplayName("John Doe").
    		Email("johndoe@gmail.com").
    		PhotoURL("http://www.example.com/12345678/photo.png").
    		EmailVerified(true).
    		PhoneNumber("+11234567890").
    		CustomClaims(map[string]interface{}{"admin": true}). // set this user as admin
    		ProviderData([]*auth.UserProvider{                   // user with Google provider
    			{
    				UID:         "google-uid",
    				Email:       "johndoe@gmail.com",
    				DisplayName: "John Doe",
    				PhotoURL:    "http://www.example.com/12345678/photo.png",
    				ProviderID:  "google.com",
    			},
    		}),
    }
    result, err := client.ImportUsers(ctx, users)
    if err != nil {
    	log.Fatalln("Error importing users", err)
    }
    for _, e := range result.Errors {
    	log.Println("Failed to import user", e.Reason)
    }
    
    [auth.go](https://github.com/firebase/firebase-admin-go/blob/66a72c371b4dbc592317ab7e7f99ce00d76c62ae/snippets/auth.go#L600-L625)

Note that `providerId` is used throughout Identity Platform to describe a specific provider. For OIDC and SAML providers, this is defined during creation. For other providers, this has a predefined value (such as `google.com` or `facebook.com`). You can retrieve the `providerId` from the claims of the signed-in user.

### Importing users with multiple authentication factors

If your existing users have phone numbers enrolled for use with [multi-factor authentication](https://docs.cloud.google.com/identity-platform/docs/web/mfa), you can import them to Identity Platform.

Multi-factor users must have a verified email and a [supported first factor](https://docs.cloud.google.com/identity-platform/docs/web/mfa#before_you_begin). Up to 5 secondary factors are allowed per user.

You can import the following multi-factor properties:

Property | Type | Description  
---|---|---  
`uid` | string |  An optional unique ID of the enrolled second factor. If not provided, a random `uid` is automatically generated.   
`phoneNumber` | string |  The enrolled second factor phone number. This phone number must be [E.164](https://wikipedia.org/wiki/E.164) compliant.   
`displayName` | string |  An optional display name. This is useful if a user has multiple enrolled second factors.   
`enrollmentTime` | string |  The date the second factor was enrolled, formatted as a UTC string. If not provided, the current date will be used.   
`factorId` | string |  The second factor type identifier. This is always set to `phone`.   
  
The following example shows how to import multi-factor users:

###  Node.js 
    
    
    // Up to 1000 users can be imported at once.
    const userImportRecords = [
      {
        uid: 'uid1',
        email: 'user1@example.com',
        emailVerified: true,
        passwordHash: Buffer.from('passwordHash1'),
        passwordSalt: Buffer.from('salt1'),
        multiFactor: {
          enrolledFactors: [
            {
              // Enrolled second factor uid is optional.
              uid: 'uid1-unique-mfa-identifier1',
              displayName: 'Personal phone',
              phoneNumber: '+16505551234',
              factorId: 'phone',
              // Enrollment time is also optional.
              enrollmentTime: 'Fri, 22 Sep 2017 01:49:58 GMT',
            },
          ],
        },
      },
      {
        // User with multiple second factors.
        uid: 'uid2',
        email: 'user2@example.com',
        emailVerified: true,
        passwordHash: Buffer.from('passwordHash2'),
        passwordSalt: Buffer.from('salt2'),
        multiFactor: {
          enrolledFactors: [
            {
              displayName: 'Work phone',
              phoneNumber: '+16505550007',
              factorId: 'phone',
            },
            {
              displayName: 'Backup phone',
              phoneNumber:  '+16505550008',
              factorId: 'phone',
            },
          ],
        },
      },
      {
        // User with no second factor.
        uid: 'uid3',
        email: 'user3@example.com',
        passwordHash: Buffer.from('passwordHash3'),
        passwordSalt: Buffer.from('salt3'),
      },
      ...
    ];
    
    const userImportOptions = {
      hash: {
        algorithm: 'HMAC_SHA256',
        key: Buffer.from('secretKey'),
      },
    };
    
    admin.auth().importUsers(userImportRecords, userImportOptions)
      .then((userImportResult) => {
        // The number of successful imports is determined via: userImportResult.successCount.
        // The number of failed imports is determined via: userImportResult.failureCount.
        // To get the error details.
        userImportResult.forEach(function(indexedError) {
          // The corresponding user that failed to upload.
          console.log(userImportRecords[indexedError.index].uid +' failed to import',
              indexedError.error);
        });
      })
      .catch((error) => {
        // Some unrecoverable error occurred that prevented the operation from running.
      });
    

## Using the command-line interface

If your user data is stored as JSON or CSV, you can import it using the Firebase command-line tool:
    
    
      firebase auth:import account_file       \
        --hash-algo=[HASH-ALGORITHM]          \
        --hash-key=[KEY]                      \
        --salt-separator=[SALT-SEPARATOR]     \
        --rounds=[ROUNDS]                     \
        --mem-cost=[MEM-COST]                 \
        --parallelization=[PARALLELIZATION]   \
        --block-size=[BLOCK-SIZE]             \
        --dk-len=[DK-LEN]                     \
        --hash-input-order=[HASH-INPUT-ORDER] \
    

See the command-line interface [reference documentation](https://firebase.google.com/docs/cli/auth#auth-import) for a complete description of each parameter.

## What's next

  * See common [error codes](https://docs.cloud.google.com/identity-platform/docs/error-codes) that occur when importing users.
  * Learn how to [Authenticate users on App Engine using Identity Platform](https://docs.cloud.google.com/identity-platform/docs/how-to-auth-users-app-engine).
  * Learn how to [Configure custom claims with Identity Platform](https://docs.cloud.google.com/identity-platform/docs/how-to-configure-custom-claims).
  * Read about the [Admin Auth API](https://docs.cloud.google.com/identity-platform/docs/concepts-admin-auth-api).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
