---
url: https://docs.cloud.google.com/identity-platform/docs/admin/manage-users/
title: Managing users programmatically \u00a0|\u00a0 Identity Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:53:46.304350+00:00
---

# Managing users programmatically  |  Identity Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/identity-platform/docs/admin/manage-users/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Identity Platform ](https://docs.cloud.google.com/identity-platform/docs)
  * [ Guides ](https://docs.cloud.google.com/identity-platform/docs/how-to)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

#  Managing users programmatically 

This document shows you how to use the Identity Platform Admin SDK to manage your users programmatically. The Admin SDK allows you to perform a wide range of common administrative tasks, such as creating, looking up, and modifying users.

## Before you begin

[Install the Admin SDK](https://docs.cloud.google.com/identity-platform/docs/install-admin-sdk).

## Getting a user

### Getting a user by ID

The primary way to identify a user is by their `uid`:

### Node.js
    
    
    getAuth()
      .getUser(uid)
      .then((userRecord) => {
        // See the UserRecord reference doc for the contents of userRecord.
        console.log(`Successfully fetched user data: ${userRecord.toJSON()}`);
      })
      .catch((error) => {
        console.log('Error fetching user data:', error);
      });
    
    [manage_users.js](https://github.com/firebase/snippets-node/blob/7cb8d0ffc824d22d8d586425659d5860f26cbb28/auth/manage_users.js#L14-L22)

### Java
    
    
    UserRecord userRecord = FirebaseAuth.getInstance().getUser(uid);
    // See the UserRecord reference doc for the contents of userRecord.
    System.out.println("Successfully fetched user data: " + userRecord.getUid());
    
    [FirebaseAuthSnippets.java](https://github.com/firebase/firebase-admin-java/blob/2225373d97869e72b164a4081968027c130c782b/src/test/java/com/google/firebase/snippets/FirebaseAuthSnippets.java#L77-L79)

### Python
    
    
    from firebase_admin import auth
    
    user = auth.get_user(uid)
    print(f'Successfully fetched user data: {user.uid}')
    
    [index.py](https://github.com/firebase/firebase-admin-python/blob/de456071dc7450a6d7715667debf6049f38fd85d/snippets/auth/index.py#L183-L186)

### Go
    
    
    // Get an auth client from the firebase.App
    client, err := app.Auth(ctx)
    if err != nil {
    	log.Fatalf("error getting Auth client: %v\n", err)
    }
    
    u, err := client.GetUser(ctx, uid)
    if err != nil {
    	log.Fatalf("error getting user %s: %v\n", uid, err)
    }
    log.Printf("Successfully fetched user data: %v\n", u)
    
    [auth.go](https://github.com/firebase/firebase-admin-go/blob/66a72c371b4dbc592317ab7e7f99ce00d76c62ae/snippets/auth.go#L149-L159)

### C#
    
    
    UserRecord userRecord = await FirebaseAuth.DefaultInstance.GetUserAsync(uid);
    // See the UserRecord reference doc for the contents of userRecord.
    Console.WriteLine($"Successfully fetched user data: {userRecord.Uid}");
    
    [FirebaseAuthSnippets.cs](https://github.com/firebase/firebase-admin-dotnet/blob/19ae6920ee9560cfbc6b8cbce9ecff0e6521b0a0/FirebaseAdmin/FirebaseAdmin.Snippets/FirebaseAuthSnippets.cs#L70-L72)

### Getting a user by email

You can also get a user using their email:

### Node.js
    
    
    getAuth()
      .getUserByEmail(email)
      .then((userRecord) => {
        // See the UserRecord reference doc for the contents of userRecord.
        console.log(`Successfully fetched user data: ${userRecord.toJSON()}`);
      })
      .catch((error) => {
        console.log('Error fetching user data:', error);
      });
    
    [manage_users.js](https://github.com/firebase/snippets-node/blob/7cb8d0ffc824d22d8d586425659d5860f26cbb28/auth/manage_users.js#L26-L34)

### Java
    
    
    UserRecord userRecord = FirebaseAuth.getInstance().getUserByEmail(email);
    // See the UserRecord reference doc for the contents of userRecord.
    System.out.println("Successfully fetched user data: " + userRecord.getEmail());
    
    [FirebaseAuthSnippets.java](https://github.com/firebase/firebase-admin-java/blob/2225373d97869e72b164a4081968027c130c782b/src/test/java/com/google/firebase/snippets/FirebaseAuthSnippets.java#L85-L87)

### Python
    
    
    from firebase_admin import auth
    
    user = auth.get_user_by_email(email)
    print(f'Successfully fetched user data: {user.uid}')
    
    [index.py](https://github.com/firebase/firebase-admin-python/blob/de456071dc7450a6d7715667debf6049f38fd85d/snippets/auth/index.py#L192-L195)

### Go
    
    
    u, err := client.GetUserByEmail(ctx, email)
    if err != nil {
    	log.Fatalf("error getting user by email %s: %v\n", email, err)
    }
    log.Printf("Successfully fetched user data: %v\n", u)
    
    [auth.go](https://github.com/firebase/firebase-admin-go/blob/66a72c371b4dbc592317ab7e7f99ce00d76c62ae/snippets/auth.go#L167-L171)

### C#
    
    
    UserRecord userRecord = await FirebaseAuth.DefaultInstance.GetUserByEmailAsync(email);
    // See the UserRecord reference doc for the contents of userRecord.
    Console.WriteLine($"Successfully fetched user data: {userRecord.Uid}");
    
    [FirebaseAuthSnippets.cs](https://github.com/firebase/firebase-admin-dotnet/blob/19ae6920ee9560cfbc6b8cbce9ecff0e6521b0a0/FirebaseAdmin/FirebaseAdmin.Snippets/FirebaseAuthSnippets.cs#L79-L81)

Note that you can only search using primary emails, not provider-specific emails. For example, if a Facebook account with the email `facebookUser@example.com` is linked to an existing user with the email `user@example.com`, calling `getUserByEmail("facebookUser@example.com")` will yield no results. Calling `getUserByEmail("user@example.com")` will return the expected user.

The primary email depends on your account linking settings:

  * _Link accounts that use the same email_ : The primary email is the first email used to sign in, unless manually updated.
  * _Create multiple accounts for each identity provider_ : The primary email is only set when a password user is created, unless manually updated.



### Getting a user by phone number

If a user has a phone number, you can look them up using it:

### Node.js
    
    
    getAuth()
      .getUserByPhoneNumber(phoneNumber)
      .then((userRecord) => {
        // See the UserRecord reference doc for the contents of userRecord.
        console.log(`Successfully fetched user data:  ${userRecord.toJSON()}`);
      })
      .catch((error) => {
        console.log('Error fetching user data:', error);
      });
    
    [manage_users.js](https://github.com/firebase/snippets-node/blob/7cb8d0ffc824d22d8d586425659d5860f26cbb28/auth/manage_users.js#L38-L46)

### Java
    
    
    UserRecord userRecord = FirebaseAuth.getInstance().getUserByPhoneNumber(phoneNumber);
    // See the UserRecord reference doc for the contents of userRecord.
    System.out.println("Successfully fetched user data: " + userRecord.getPhoneNumber());
    
    [FirebaseAuthSnippets.java](https://github.com/firebase/firebase-admin-java/blob/2225373d97869e72b164a4081968027c130c782b/src/test/java/com/google/firebase/snippets/FirebaseAuthSnippets.java#L94-L96)

### Python
    
    
    from firebase_admin import auth
    
    user = auth.get_user_by_phone_number(phone)
    print(f'Successfully fetched user data: {user.uid}')
    
    [index.py](https://github.com/firebase/firebase-admin-python/blob/de456071dc7450a6d7715667debf6049f38fd85d/snippets/auth/index.py#L221-L224)

### Go
    
    
    u, err := client.GetUserByPhoneNumber(ctx, phone)
    if err != nil {
    	log.Fatalf("error getting user by phone %s: %v\n", phone, err)
    }
    log.Printf("Successfully fetched user data: %v\n", u)
    
    [auth.go](https://github.com/firebase/firebase-admin-go/blob/66a72c371b4dbc592317ab7e7f99ce00d76c62ae/snippets/auth.go#L179-L183)

### C#
    
    
    UserRecord userRecord = await FirebaseAuth.DefaultInstance.GetUserByPhoneNumberAsync(phoneNumber);
    // See the UserRecord reference doc for the contents of userRecord.
    Console.WriteLine($"Successfully fetched user data: {userRecord.Uid}");
    
    [FirebaseAuthSnippets.cs](https://github.com/firebase/firebase-admin-dotnet/blob/19ae6920ee9560cfbc6b8cbce9ecff0e6521b0a0/FirebaseAdmin/FirebaseAdmin.Snippets/FirebaseAuthSnippets.cs#L88-L90)

### Bulk retrieve user data

You can also retrieve a list of users based on identifiers that you provide. You may identify users by their uid, email, or phone number. A maximum of 100 identifiers may be supplied in a single call. Identifiers can contain a mix of types:

### Node.js
    
    
    getAuth()
      .getUsers([
        { uid: 'uid1' },
        { email: 'user2@example.com' },
        { phoneNumber: '+15555550003' },
        { providerId: 'google.com', providerUid: 'google_uid4' },
      ])
      .then((getUsersResult) => {
        console.log('Successfully fetched user data:');
        getUsersResult.users.forEach((userRecord) => {
          console.log(userRecord);
        });
    
        console.log('Unable to find users corresponding to these identifiers:');
        getUsersResult.notFound.forEach((userIdentifier) => {
          console.log(userIdentifier);
        });
      })
      .catch((error) => {
        console.log('Error fetching user data:', error);
      });
    
    [manage_users.js](https://github.com/firebase/snippets-node/blob/7cb8d0ffc824d22d8d586425659d5860f26cbb28/auth/manage_users.js#L50-L70)

### Java
    
    
    GetUsersResult result = FirebaseAuth.getInstance().getUsersAsync(Arrays.asList(
        new UidIdentifier("uid1"),
        new EmailIdentifier("user2@example.com"),
        new PhoneIdentifier("+15555550003"),
        new ProviderIdentifier("google.com", "google_uid4"))).get();
    
    System.out.println("Successfully fetched user data:");
    for (UserRecord user : result.getUsers()) {
      System.out.println(user.getUid());
    }
    
    System.out.println("Unable to find users corresponding to these identifiers:");
    for (UserIdentifier uid : result.getNotFound()) {
      System.out.println(uid);
    }
    
    [FirebaseAuthSnippets.java](https://github.com/firebase/snippets-java/blob/7051da2745f8f95b176c9c6347e0bb0db3de1112/admin/src/main/java/com/google/firebase/example/FirebaseAuthSnippets.java#L36-L50)

### Python
    
    
    from firebase_admin import auth
    
    result = auth.get_users([
        auth.UidIdentifier('uid1'),
        auth.EmailIdentifier('user2@example.com'),
        auth.PhoneIdentifier(+15555550003),
        auth.ProviderIdentifier('google.com', 'google_uid4')
    ])
    
    print('Successfully fetched user data:')
    for user in result.users:
        print(user.uid)
    
    print('Unable to find users corresponding to these identifiers:')
    for uid in result.not_found:
        print(uid)
    
    [index.py](https://github.com/firebase/firebase-admin-python/blob/de456071dc7450a6d7715667debf6049f38fd85d/snippets/auth/index.py#L200-L215)

### Go
    
    
    getUsersResult, err := client.GetUsers(ctx, []auth.UserIdentifier{
    	auth.UIDIdentifier{UID: "uid1"},
    	auth.EmailIdentifier{Email: "user@example.com"},
    	auth.PhoneIdentifier{PhoneNumber: "+15555551234"},
    	auth.ProviderIdentifier{ProviderID: "google.com", ProviderUID: "google_uid1"},
    })
    if err != nil {
    	log.Fatalf("error retriving multiple users: %v\n", err)
    }
    
    log.Printf("Successfully fetched user data:")
    for _, u := range getUsersResult.Users {
    	log.Printf("%v", u)
    }
    
    log.Printf("Unable to find users corresponding to these identifiers:")
    for _, id := range getUsersResult.NotFound {
    	log.Printf("%v", id)
    }
    
    [auth.go](https://github.com/firebase/firebase-admin-go/blob/0be9fa841fdf0e485f4c702bd6de941ad9454f10/snippets/auth.go#L190-L208)

### C#
    
    
    GetUsersResult result = await FirebaseAuth.DefaultInstance.GetUsersAsync(
        new List<UserIdentifier>
        {
            new UidIdentifier("uid1"),
            new EmailIdentifier("user2@example.com"),
            new PhoneIdentifier("+15555550003"),
            new ProviderIdentifier("google.com", "google_uid4"),
        });
    
    Console.WriteLine("Successfully fetched user data:");
    foreach (UserRecord user in result.Users)
    {
        Console.WriteLine($"User: {user.Uid}");
    }
    
    Console.WriteLine("Unable to find users corresponding to these identifiers:");
    foreach (UserIdentifier uid in result.NotFound)
    {
        Console.WriteLine($"{uid}");
    }
    
    
    [FirebaseAuthSnippets.cs](https://github.com/firebase/firebase-admin-dotnet/blob/19ae6920ee9560cfbc6b8cbce9ecff0e6521b0a0/FirebaseAdmin/FirebaseAdmin.Snippets/FirebaseAuthSnippets.cs#L97-L117)

This method returns a list the same size as the input list, with each entry containing either the corresponding `UserRecord` or an error, indicating why that identifier was not able to be looked up.

## Listing users

The code below shows how to list all users:

### Node.js
    
    
    const listAllUsers = (nextPageToken) => {
      // List batch of users, 1000 at a time.
      getAuth()
        .listUsers(1000, nextPageToken)
        .then((listUsersResult) => {
          listUsersResult.users.forEach((userRecord) => {
            console.log('user', userRecord.toJSON());
          });
          if (listUsersResult.pageToken) {
            // List next batch of users.
            listAllUsers(listUsersResult.pageToken);
          }
        })
        .catch((error) => {
          console.log('Error listing users:', error);
        });
    };
    // Start listing users from the beginning, 1000 at a time.
    listAllUsers();
    
    [manage_users.js](https://github.com/firebase/snippets-node/blob/7cb8d0ffc824d22d8d586425659d5860f26cbb28/auth/manage_users.js#L156-L174)

### Java
    
    
    // Start listing users from the beginning, 1000 at a time.
    ListUsersPage page = FirebaseAuth.getInstance().listUsers(null);
    while (page != null) {
      for (ExportedUserRecord user : page.getValues()) {
        System.out.println("User: " + user.getUid());
      }
      page = page.getNextPage();
    }
    
    // Iterate through all users. This will still retrieve users in batches,
    // buffering no more than 1000 users in memory at a time.
    page = FirebaseAuth.getInstance().listUsers(null);
    for (ExportedUserRecord user : page.iterateAll()) {
      System.out.println("User: " + user.getUid());
    }
    
    [FirebaseAuthSnippets.java](https://github.com/firebase/firebase-admin-java/blob/2225373d97869e72b164a4081968027c130c782b/src/test/java/com/google/firebase/snippets/FirebaseAuthSnippets.java#L211-L225)

### Python
    
    
    # Start listing users from the beginning, 1000 at a time.
    page = auth.list_users()
    while page:
        for user in page.users:
            print('User: ' + user.uid)
        # Get next batch of users.
        page = page.get_next_page()
    
    # Iterate through all users. This will still retrieve users in batches,
    # buffering no more than 1000 users in memory at a time.
    for user in auth.list_users().iterate_all():
        print('User: ' + user.uid)
    
    [index.py](https://github.com/firebase/firebase-admin-python/blob/de456071dc7450a6d7715667debf6049f38fd85d/snippets/auth/index.py#L330-L341)

### Go
    
    
    // Note, behind the scenes, the Users() iterator will retrive 1000 Users at a time through the API
    iter := client.Users(ctx, "")
    for {
    	user, err := iter.Next()
    	if err == iterator.Done {
    		break
    	}
    	if err != nil {
    		log.Fatalf("error listing users: %s\n", err)
    	}
    	log.Printf("read user user: %v\n", user)
    }
    
    // Iterating by pages 100 users at a time.
    // Note that using both the Next() function on an iterator and the NextPage()
    // on a Pager wrapping that same iterator will result in an error.
    pager := iterator.NewPager(client.Users(ctx, ""), 100, "")
    for {
    	var users []*auth.ExportedUserRecord
    	nextPageToken, err := pager.NextPage(&users)
    	if err != nil {
    		log.Fatalf("paging error %v\n", err)
    	}
    	for _, u := range users {
    		log.Printf("read user user: %v\n", u)
    	}
    	if nextPageToken == "" {
    		break
    	}
    }
    
    [auth.go](https://github.com/firebase/firebase-admin-go/blob/66a72c371b4dbc592317ab7e7f99ce00d76c62ae/snippets/auth.go#L394-L423)

### C#
    
    
    // Start listing users from the beginning, 1000 at a time.
    var pagedEnumerable = FirebaseAuth.DefaultInstance.ListUsersAsync(null);
    var responses = pagedEnumerable.AsRawResponses().GetAsyncEnumerator();
    while (await responses.MoveNextAsync())
    {
        ExportedUserRecords response = responses.Current;
        foreach (ExportedUserRecord user in response.Users)
        {
            Console.WriteLine($"User: {user.Uid}");
        }
    }
    
    // Iterate through all users. This will still retrieve users in batches,
    // buffering no more than 1000 users in memory at a time.
    var enumerator = FirebaseAuth.DefaultInstance.ListUsersAsync(null).GetAsyncEnumerator();
    while (await enumerator.MoveNextAsync())
    {
        ExportedUserRecord user = enumerator.Current;
        Console.WriteLine($"User: {user.Uid}");
    }
    
    
    [FirebaseAuthSnippets.cs](https://github.com/firebase/firebase-admin-dotnet/blob/19ae6920ee9560cfbc6b8cbce9ecff0e6521b0a0/FirebaseAdmin/FirebaseAdmin.Snippets/FirebaseAuthSnippets.cs#L500-L520)

Users are returned in batches, ordered by their `uid`. Each batch of results contains a list of users, and a next page token used to fetch the next batch. When all users have been listed, no `pageToken` is returned.

The `maxResult` field specifies the maximum batch size. The default and maximum value is 1000.

### Listing user password hashes

Because password hashes are sensitive, the Admin SDK does not return them unless the user has the `firebaseauth.configs.getHashConfig` permission. This permission isn't granted by any predefined roles. To grant it:

  1. [Create a custom role](https://docs.cloud.google.com/iam/docs/creating-custom-roles#creating_a_custom_role) that grants the `firebaseauth.configs.getHashConfig` permission.

  2. [Grant the custom role](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access#granting-console) to the user or service account.




Subsequent calls to `listUsers()` by users with this custom role will include the `passwordHash` and `passwordSalt` fields.

**Warning:** Do not use the Editor role (`roles/editor`) to grant the `firebaseauth.configs.getHashConfig` permission. It includes a wide range of additional permissions that are not required.

## Creating a user

Creating new users programmatically avoids some restrictions placed on end users. You aren't subject to throttling or rate limiting, and can bypass the normal verification process for emails and phone numbers.

To create a new user:

### Node.js
    
    
    getAuth()
      .createUser({
        email: 'user@example.com',
        emailVerified: false,
        phoneNumber: '+11234567890',
        password: 'secretPassword',
        displayName: 'John Doe',
        photoURL: 'http://www.example.com/12345678/photo.png',
        disabled: false,
      })
      .then((userRecord) => {
        // See the UserRecord reference doc for the contents of userRecord.
        console.log('Successfully created new user:', userRecord.uid);
      })
      .catch((error) => {
        console.log('Error creating new user:', error);
      });
    
    [manage_users.js](https://github.com/firebase/snippets-node/blob/7cb8d0ffc824d22d8d586425659d5860f26cbb28/auth/manage_users.js#L74-L90)

### Java
    
    
    CreateRequest request = new CreateRequest()
        .setEmail("user@example.com")
        .setEmailVerified(false)
        .setPassword("secretPassword")
        .setPhoneNumber("+11234567890")
        .setDisplayName("John Doe")
        .setPhotoUrl("http://www.example.com/12345678/photo.png")
        .setDisabled(false);
    
    UserRecord userRecord = FirebaseAuth.getInstance().createUser(request);
    System.out.println("Successfully created new user: " + userRecord.getUid());
    
    [FirebaseAuthSnippets.java](https://github.com/firebase/firebase-admin-java/blob/2225373d97869e72b164a4081968027c130c782b/src/test/java/com/google/firebase/snippets/FirebaseAuthSnippets.java#L112-L122)

### Python
    
    
    user = auth.create_user(
        email='user@example.com',
        email_verified=False,
        phone_number='+15555550100',
        password='secretPassword',
        display_name='John Doe',
        photo_url='http://www.example.com/12345678/photo.png',
        disabled=False)
    print(f'Sucessfully created new user: {user.uid}')
    
    [index.py](https://github.com/firebase/firebase-admin-python/blob/de456071dc7450a6d7715667debf6049f38fd85d/snippets/auth/index.py#L229-L237)

### Go
    
    
    params := (&auth.UserToCreate{}).
    	Email("user@example.com").
    	EmailVerified(false).
    	PhoneNumber("+15555550100").
    	Password("secretPassword").
    	DisplayName("John Doe").
    	PhotoURL("http://www.example.com/12345678/photo.png").
    	Disabled(false)
    u, err := client.CreateUser(ctx, params)
    if err != nil {
    	log.Fatalf("error creating user: %v\n", err)
    }
    log.Printf("Successfully created user: %v\n", u)
    
    [auth.go](https://github.com/firebase/firebase-admin-go/blob/66a72c371b4dbc592317ab7e7f99ce00d76c62ae/snippets/auth.go#L214-L226)

### C#
    
    
    UserRecordArgs args = new UserRecordArgs()
    {
        Email = "user@example.com",
        EmailVerified = false,
        PhoneNumber = "+11234567890",
        Password = "secretPassword",
        DisplayName = "John Doe",
        PhotoUrl = "http://www.example.com/12345678/photo.png",
        Disabled = false,
    };
    UserRecord userRecord = await FirebaseAuth.DefaultInstance.CreateUserAsync(args);
    // See the UserRecord reference doc for the contents of userRecord.
    Console.WriteLine($"Successfully created new user: {userRecord.Uid}");
    
    [FirebaseAuthSnippets.cs](https://github.com/firebase/firebase-admin-dotnet/blob/19ae6920ee9560cfbc6b8cbce9ecff0e6521b0a0/FirebaseAdmin/FirebaseAdmin.Snippets/FirebaseAuthSnippets.cs#L124-L136)

You can set any of the properties below on a new user. All properties are optional.

Property | Type | Description  
---|---|---  
`uid` | string |  The `uid` to assign to the newly created user. Must be a string between 1 and 128 characters long, inclusive. If not provided, a random `uid` will be automatically generated.   
`email` | string |  The user's primary email. Must be a valid email address.   
`emailVerified` | boolean |  Whether or not the user's primary email is verified. If not provided, the default is `false`.   
`phoneNumber` | string |  The user's primary phone number. Must be a valid E.164 spec compliant phone number.   
`password` | string |  The user's raw, unhashed password. Must be at least six characters long.   
`displayName` | string |  The users' display name.   
`photoURL` | string |  The user's photo URL.   
`disabled` | boolean |  Whether or not the user is disabled. `true` for disabled; `false` for enabled. If not provided, the default is `false`.   
  
## Updating a user

### Node.js
    
    
    getAuth()
      .updateUser(uid, {
        email: 'modifiedUser@example.com',
        phoneNumber: '+11234567890',
        emailVerified: true,
        password: 'newPassword',
        displayName: 'Jane Doe',
        photoURL: 'http://www.example.com/12345678/photo.png',
        disabled: true,
      })
      .then((userRecord) => {
        // See the UserRecord reference doc for the contents of userRecord.
        console.log('Successfully updated user', userRecord.toJSON());
      })
      .catch((error) => {
        console.log('Error updating user:', error);
      });
    
    [manage_users.js](https://github.com/firebase/snippets-node/blob/7cb8d0ffc824d22d8d586425659d5860f26cbb28/auth/manage_users.js#L110-L126)

### Java
    
    
    UpdateRequest request = new UpdateRequest(uid)
        .setEmail("user@example.com")
        .setPhoneNumber("+11234567890")
        .setEmailVerified(true)
        .setPassword("newPassword")
        .setDisplayName("Jane Doe")
        .setPhotoUrl("http://www.example.com/12345678/photo.png")
        .setDisabled(true);
    
    UserRecord userRecord = FirebaseAuth.getInstance().updateUser(request);
    System.out.println("Successfully updated user: " + userRecord.getUid());
    
    [FirebaseAuthSnippets.java](https://github.com/firebase/firebase-admin-java/blob/2225373d97869e72b164a4081968027c130c782b/src/test/java/com/google/firebase/snippets/FirebaseAuthSnippets.java#L140-L150)

### Python
    
    
    user = auth.update_user(
        uid,
        email='user@example.com',
        phone_number='+15555550100',
        email_verified=True,
        password='newPassword',
        display_name='John Doe',
        photo_url='http://www.example.com/12345678/photo.png',
        disabled=True)
    print(f'Sucessfully updated user: {user.uid}')
    
    [index.py](https://github.com/firebase/firebase-admin-python/blob/de456071dc7450a6d7715667debf6049f38fd85d/snippets/auth/index.py#L250-L259)

### Go
    
    
    params := (&auth.UserToUpdate{}).
    	Email("user@example.com").
    	EmailVerified(true).
    	PhoneNumber("+15555550100").
    	Password("newPassword").
    	DisplayName("John Doe").
    	PhotoURL("http://www.example.com/12345678/photo.png").
    	Disabled(true)
    u, err := client.UpdateUser(ctx, uid, params)
    if err != nil {
    	log.Fatalf("error updating user: %v\n", err)
    }
    log.Printf("Successfully updated user: %v\n", u)
    
    [auth.go](https://github.com/firebase/firebase-admin-go/blob/66a72c371b4dbc592317ab7e7f99ce00d76c62ae/snippets/auth.go#L250-L262)

### C#
    
    
    UserRecordArgs args = new UserRecordArgs()
    {
        Uid = uid,
        Email = "modifiedUser@example.com",
        PhoneNumber = "+11234567890",
        EmailVerified = true,
        Password = "newPassword",
        DisplayName = "Jane Doe",
        PhotoUrl = "http://www.example.com/12345678/photo.png",
        Disabled = true,
    };
    UserRecord userRecord = await FirebaseAuth.DefaultInstance.UpdateUserAsync(args);
    // See the UserRecord reference doc for the contents of userRecord.
    Console.WriteLine($"Successfully updated user: {userRecord.Uid}");
    
    [FirebaseAuthSnippets.cs](https://github.com/firebase/firebase-admin-dotnet/blob/19ae6920ee9560cfbc6b8cbce9ecff0e6521b0a0/FirebaseAdmin/FirebaseAdmin.Snippets/FirebaseAuthSnippets.cs#L451-L464)

You can update any of the user properties below. All properties are optional. If a property is not specified, its value will remain unchanged.

Property | Type | Description  
---|---|---  
`email` | string |  The user's new primary email. Must be a valid email address.   
`emailVerified` | boolean |  Whether or not the user's primary email is verified. If not provided, the default is `false`.   
`phoneNumber` | string |  The user's new primary phone number. Must be a valid E.164 spec compliant phone number. Set to `null` to clear the user's existing phone number.   
`password` | string |  The user's new raw, unhashed password. Must be at least six characters long.   
`displayName` | string | `null` |  The users' new display name. Set to `null` to clear the user's existing display name.   
`photoURL` | string | `null` |  The users' new photo URL. Set to `null` to clear the user's existing photo URL. If non-`null`, must be a valid URL.   
`disabled` | boolean |  Whether or not the user is disabled. `true` for disabled; `false` for enabled.   
  
## Deleting a user

You can delete a user with their `uid`:

### Node.js
    
    
    getAuth()
      .deleteUser(uid)
      .then(() => {
        console.log('Successfully deleted user');
      })
      .catch((error) => {
        console.log('Error deleting user:', error);
      });
    
    [manage_users.js](https://github.com/firebase/snippets-node/blob/7cb8d0ffc824d22d8d586425659d5860f26cbb28/auth/manage_users.js#L130-L137)

### Java
    
    
    FirebaseAuth.getInstance().deleteUser(uid);
    System.out.println("Successfully deleted user.");
    
    [FirebaseAuthSnippets.java](https://github.com/firebase/firebase-admin-java/blob/2225373d97869e72b164a4081968027c130c782b/src/test/java/com/google/firebase/snippets/FirebaseAuthSnippets.java#L231-L232)

### Python
    
    
    auth.delete_user(uid)
    print('Successfully deleted user')
    
    [index.py](https://github.com/firebase/firebase-admin-python/blob/de456071dc7450a6d7715667debf6049f38fd85d/snippets/auth/index.py#L264-L265)

### Go
    
    
    err := client.DeleteUser(ctx, uid)
    if err != nil {
    	log.Fatalf("error deleting user: %v\n", err)
    }
    log.Printf("Successfully deleted user: %s\n", uid)
    
    [auth.go](https://github.com/firebase/firebase-admin-go/blob/66a72c371b4dbc592317ab7e7f99ce00d76c62ae/snippets/auth.go#L269-L273)

### C#
    
    
    await FirebaseAuth.DefaultInstance.DeleteUserAsync(uid);
    Console.WriteLine("Successfully deleted user.");
    
    [FirebaseAuthSnippets.cs](https://github.com/firebase/firebase-admin-dotnet/blob/19ae6920ee9560cfbc6b8cbce9ecff0e6521b0a0/FirebaseAdmin/FirebaseAdmin.Snippets/FirebaseAuthSnippets.cs#L471-L472)

### Delete Multiple Users

You can also delete multiple users at once:

### Node.js
    
    
    getAuth()
      .deleteUsers([uid1, uid2, uid3])
      .then((deleteUsersResult) => {
        console.log(`Successfully deleted ${deleteUsersResult.successCount} users`);
        console.log(`Failed to delete ${deleteUsersResult.failureCount} users`);
        deleteUsersResult.errors.forEach((err) => {
          console.log(err.error.toJSON());
        });
      })
      .catch((error) => {
        console.log('Error deleting users:', error);
      });
    
    [manage_users.js](https://github.com/firebase/snippets-node/blob/7cb8d0ffc824d22d8d586425659d5860f26cbb28/auth/manage_users.js#L141-L152)

### Java
    
    
    DeleteUsersResult result = FirebaseAuth.getInstance().deleteUsersAsync(
        Arrays.asList("uid1", "uid2", "uid3")).get();
    
    System.out.println("Successfully deleted " + result.getSuccessCount() + " users");
    System.out.println("Failed to delete " + result.getFailureCount() + " users");
    for (ErrorInfo error : result.getErrors()) {
      System.out.println("error #" + error.getIndex() + ", reason: " + error.getReason());
    }
    
    [FirebaseAuthSnippets.java](https://github.com/firebase/snippets-java/blob/7051da2745f8f95b176c9c6347e0bb0db3de1112/admin/src/main/java/com/google/firebase/example/FirebaseAuthSnippets.java#L56-L63)

### Python
    
    
    from firebase_admin import auth
    
    result = auth.delete_users(["uid1", "uid2", "uid3"])
    
    print(f'Successfully deleted {result.success_count} users')
    print(f'Failed to delete {result.failure_count} users')
    for err in result.errors:
        print(f'error #{result.index}, reason: {result.reason}')
    
    [index.py](https://github.com/firebase/firebase-admin-python/blob/de456071dc7450a6d7715667debf6049f38fd85d/snippets/auth/index.py#L270-L277)

### Go
    
    
    deleteUsersResult, err := client.DeleteUsers(ctx, []string{"uid1", "uid2", "uid3"})
    if err != nil {
    	log.Fatalf("error deleting users: %v\n", err)
    }
    
    log.Printf("Successfully deleted %d users", deleteUsersResult.SuccessCount)
    log.Printf("Failed to delete %d users", deleteUsersResult.FailureCount)
    for _, err := range deleteUsersResult.Errors {
    	log.Printf("%v", err)
    }
    
    [auth.go](https://github.com/firebase/firebase-admin-go/blob/0be9fa841fdf0e485f4c702bd6de941ad9454f10/snippets/auth.go#L279-L288)

### C#
    
    
    DeleteUsersResult result = await FirebaseAuth.DefaultInstance.DeleteUsersAsync(new List<string>
        {
            "uid1",
            "uid2",
            "uid3",
        });
    
    Console.WriteLine($"Successfully deleted {result.SuccessCount} users.");
    Console.WriteLine($"Failed to delete {result.FailureCount} users.");
    
    foreach (ErrorInfo err in result.Errors)
    {
        Console.WriteLine($"Error #{err.Index}, reason: {err.Reason}");
    }
    
    
    [FirebaseAuthSnippets.cs](https://github.com/firebase/firebase-admin-dotnet/blob/19ae6920ee9560cfbc6b8cbce9ecff0e6521b0a0/FirebaseAdmin/FirebaseAdmin.Snippets/FirebaseAuthSnippets.cs#L479-L493)

The delete users method returns a list of failures for the users that were unable to be deleted.

## What's next

  * [Migrate users from an existing app to Identity Platform](https://docs.cloud.google.com/identity-platform/docs/migrating-users)
  * [Manage SAML and OIDC providers programmatically](https://docs.cloud.google.com/identity-platform/docs/managing-providers-programmatically).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
