---
url: https://docs.cloud.google.com/run/docs/tutorials/identity-platform/
title: End user authentication for Cloud Run tutorial \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T21:06:27.462792+00:00
---

# End user authentication for Cloud Run tutorial  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/run/docs/tutorials/identity-platform/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run)



Send feedback 

#  End user authentication for Cloud Run tutorial Stay organized with collections  Save and categorize content based on your preferences. 

This tutorial shows how to create a voting service, consisting of the following components:

  * A browser-based client that does the following:

    1. Uses [Identity Platform](https://docs.cloud.google.com/identity-platform/docs) to fetch an ID token.
    2. Allows users to vote for their favorite domestic animal.
    3. Adds that ID token to a request to the Cloud Run server that processes the vote.
  * A Cloud Run server that does the following:

    1. Checks to make sure that the end user has properly authenticated by providing a valid ID token.
    2. Processes the end user's vote.
    3. Using its own credentials, sends the vote on to Cloud SQL for storage.
  * A PostgreSQL database that stores the votes.




For simplicity, this tutorial uses Google as a [provider](https://docs.cloud.google.com/identity-platform/docs/web/google). To acquire their ID token, users must authenticate using their user account. However, you can use other providers or authentication methods to [sign in users](https://docs.cloud.google.com/identity-platform/docs/how-to#signing-in-users).

When this document uses the term _user account_ , it refers to a Google Account, or a user account managed by your identity provider and federated with [Workforce Identity Federation](https://docs.cloud.google.com/iam/docs/workforce-identity-federation). 

You use the credentials provided by your user account to sign in to the tool.

This service minimizes security risks by using [Secret Manager](https://docs.cloud.google.com/secret-manager/docs) to protect sensitive data used to connect to the Cloud SQL instance. It also uses a [least-privilege service identity](https://docs.cloud.google.com/run/docs/securing/service-identity) to secure access to the database.

## Objectives

Write, build, and deploy a service to Cloud Run that shows how to:

  * Use Identity Platform to authenticate an end user to the Cloud Run service backend.

  * Create a least-privilege identity for the service to grant minimal access to Google Cloud resources.

  * Use Secret Manager to handle sensitive data when connecting the Cloud Run service to a postgreSQL database. 




## Costs

In this document, you use the following billable components of Google Cloud: 

  * [Cloud Build](https://docs.cloud.google.com/build/docs)
  * [Artifact Registry](https://docs.cloud.google.com/artifact-registry)
  * [Secret Manager](https://docs.cloud.google.com/secret-manager)
  * [Cloud SQL](https://docs.cloud.google.com/sql)
  * [Identity Platform](https://docs.cloud.google.com/identity-platform)
  * [Cloud Run](https://docs.cloud.google.com/run)



To generate a cost estimate based on your projected usage, use the [pricing calculator](https://docs.cloud.google.com/products/calculator). 

New Google Cloud users might be eligible for a [free trial](https://docs.cloud.google.com/free). 

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  5. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  6. Enable the Cloud Run, Secret Manager, Cloud SQL, Artifact Registry, and Cloud Build APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=run.googleapis.com,secretmanager.googleapis.com,sqladmin.googleapis.com,sql-component.googleapis.com,cloudbuild.googleapis.com,artifactregistry.googleapis.com)




### Required roles

To get the permissions that you need to complete the tutorial, ask your administrator to grant you the following IAM roles on your project: 

  * [Artifact Registry Repository Administrator ](https://docs.cloud.google.com/iam/docs/roles-permissions/artifactregistry#artifactregistry.repoAdmin) (`roles/artifactregistry.repoAdmin`)
  * [Cloud Build Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.builds.editor) (`roles/cloudbuild.builds.editor`)
  * [Cloud Run Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.admin) (`roles/run.admin`)
  * [Cloud SQL Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudsql#cloudsql.admin) (`roles/cloudsql.admin`)
  * [Create Service Accounts ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountCreator) (`roles/iam.serviceAccountCreator`)
  * [Identity Platform Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/identityplatform#identityplatform.admin) (`roles/identityplatform.admin`)
  * [OAuth Config Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/oauthconfig#oauthconfig.editor) (`roles/oauthconfig.editor`)
  * [Project IAM Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.projectIamAdmin) (`roles/resourcemanager.projectIamAdmin`)
  * [Secret Manager Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/secretmanager#secretmanager.admin) (`roles/secretmanager.admin`)
  * [Service Account User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`)
  * [Service Usage Consumer ](https://docs.cloud.google.com/iam/docs/roles-permissions/serviceusage#serviceusage.serviceUsageConsumer) (`roles/serviceusage.serviceUsageConsumer`)
  * [Storage Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.admin) (`roles/storage.admin`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

**Note:** [IAM basic roles](https://docs.cloud.google.com/iam/docs/roles-overview#basic) might also contain permissions to complete the tutorial. You shouldn't grant basic roles in a production environment, but you can grant them in a development or test environment. 

## Set up gcloud CLI defaults

To configure Google Cloud CLI with defaults for your Cloud Run service:

  1. Set your default project:
         
         gcloud config set project PROJECT_ID

Replace PROJECT_ID with the name of the project you created for this tutorial.

  2. Configure Google Cloud CLI for your chosen region:
         
         gcloud config set run/region REGION

Replace REGION with the supported Cloud Run region of your choice.




### Cloud Run locations

Cloud Run is regional, which means the infrastructure that runs your Cloud Run services is located in a specific region and is managed by Google to be redundantly available across [all the zones within that region](https://docs.cloud.google.com/docs/geography-and-regions).   
  


Meeting your latency, availability, or durability requirements are primary factors for selecting the region where your Cloud Run services are run. You can generally select the region nearest to your users but you should consider the location of the [other Google Cloud products](https://cloud.google.com/about/locations/#locations) that are used by your Cloud Run service. Using Google Cloud products together across multiple locations can affect your service's latency as well as cost.  
  


Cloud Run is available in the following regions:

#### Subject to [Tier 1 pricing](https://docs.cloud.google.com/run/pricing#tables)

  * `asia-east1` (Taiwan) 
  * `asia-northeast1` (Tokyo) 
  * `asia-northeast2` (Osaka) 
  * `asia-south1` (Mumbai, India) 
  * `asia-southeast3 ` (Bangkok) 
  * `europe-north1` (Finland) ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)
  * `europe-north2` (Stockholm) ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)
  * `europe-southwest1` (Madrid) ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)
  * `europe-west1` (Belgium) ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)
  * `europe-west4` (Netherlands) ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)
  * `europe-west8` (Milan) ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)
  * `europe-west9` (Paris) ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)
  * `me-west1` (Tel Aviv) 
  * `northamerica-south1` (Mexico) 
  * `us-central1` (Iowa) ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)
  * `us-east1` (South Carolina) 
  * `us-east4` (Northern Virginia) 
  * `us-east5` (Columbus) 
  * `us-south1` (Dallas) ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)
  * `us-west1` (Oregon) ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)



#### Subject to [Tier 2 pricing](https://docs.cloud.google.com/run/pricing#tables)

  * `africa-south1` (Johannesburg) 
  * `asia-east2` (Hong Kong) 
  * `asia-northeast3` (Seoul, South Korea) 
  * `asia-southeast1` (Singapore) 
  * `asia-southeast2 ` (Jakarta) 
  * `asia-south2` (Delhi, India) 
  * `australia-southeast1` (Sydney) 
  * `australia-southeast2` (Melbourne) 
  * `europe-central2` (Warsaw, Poland) ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)
  * `europe-west10` (Berlin) 
  * `europe-west12` (Turin) ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)
  * `europe-west2` (London, UK) ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)
  * `europe-west3` (Frankfurt, Germany) 
  * `europe-west6` (Zurich, Switzerland) ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)
  * `me-central1` (Doha) 
  * `me-central2` (Dammam) 
  * `northamerica-northeast1` (Montreal) ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)
  * `northamerica-northeast2` (Toronto) ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)
  * `southamerica-east1` (Sao Paulo, Brazil) ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)
  * `southamerica-west1` (Santiago, Chile) ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)
  * `us-west2` (Los Angeles) 
  * `us-west3` (Salt Lake City) 
  * `us-west4` (Las Vegas) 



If you already created a Cloud Run service, you can view the region in the Cloud Run dashboard in the [Google Cloud console](https://console.cloud.google.com/run).

OK

## Retrieve the code sample

To retrieve the code sample for use:

  1. Clone the sample app repository to your local machine:

###  Node.js 
         
         git clone https://github.com/GoogleCloudPlatform/nodejs-docs-samples.git

Alternatively, you can [ download the sample ](https://github.com/GoogleCloudPlatform/nodejs-docs-samples/archive/master.zip) as a zip file and extract it. 

###  Python 
         
         git clone https://github.com/GoogleCloudPlatform/python-docs-samples.git

Alternatively, you can [ download the sample ](https://github.com/GoogleCloudPlatform/python-docs-samples/archive/master.zip) as a zip file and extract it. 

###  Java 
         
         git clone https://github.com/GoogleCloudPlatform/java-docs-samples.git

Alternatively, you can [ download the sample ](https://github.com/GoogleCloudPlatform/java-docs-samples/archive/master.zip) as a zip file and extract it. 

  2. Change to the directory that contains the Cloud Run sample code:

###  Node.js 
         
         cd nodejs-docs-samples/run/idp-sql/

###  Python 
         
         cd python-docs-samples/run/idp-sql/

###  Java 
         
         cd java-docs-samples/run/idp-sql/




## Visualize the architecture

![End user signin flow.](https://docs.cloud.google.com/static/run/docs/tutorials/images/idp-sql-architecture.png) Diagram shows an end user logging in through a Google sign-in dialog provided by Identity Platform, and then being redirected back to Cloud Run with the user's identity. 

  1. An end user makes the first request to the Cloud Run server.

  2. The client loads in the browser.

  3. The user provides login credentials through the Google sign-in dialog from Identity Platform. An alert welcomes the signed-in user.

  4. Control is redirected back to the server. The end user votes using the client, which fetches an ID token from Identity Platform and adds it to the vote request header.

  5. When the server receives the request, it verifies the Identity Platform ID token, confirming that the end user is appropriately authenticated. Then server sends the vote to Cloud SQL, using its own credentials.




## Understand the core code

The sample is implemented as client and server, as described next.

### Integrate with Identity Platform: client-side code

This sample uses [Firebase SDKs](https://firebase.google.com/docs/auth/web/start) to integrate with Identity Platform in order to sign-in and manage users. To connect to Identity Platform, the client-side JavaScript holds the reference to the project's credentials as a config object and imports the necessary [Firebase JavaScript SDKs](https://firebase.google.com/docs/web/setup):
    
    
    const config = {
      apiKey: 'API_KEY',
      authDomain: 'PROJECT_ID.firebaseapp.com',
    };
    
    
    <!-- Firebase App (the core Firebase SDK) is always required and must be listed first-->
    <script src="https://www.gstatic.com/firebasejs/7.18/firebase-app.js"></script>
    <!-- Add Firebase Auth service-->
    <script src="https://www.gstatic.com/firebasejs/7.18/firebase-auth.js"></script>

The Firebase JavaScript SDK handles the sign-in flow by prompting the end user to sign in to their Google Account using a dialog window. It then redirects them back to the service.
    
    
    function signIn() {
      const provider = new firebase.auth.GoogleAuthProvider();
      provider.addScope('https://www.googleapis.com/auth/userinfo.email');
      firebase
        .auth()
        .signInWithPopup(provider)
        .then(result => {
          // Returns the signed in user along with the provider's credential
          console.log(`${result.user.displayName} logged in.`);
          window.alert(`Welcome ${result.user.displayName}!`);
        })
        .catch(err => {
          console.log(`Error during sign in: ${err.message}`);
          window.alert('Sign in failed. Retry or check your browser logs.');
        });
    }

**Note:** To capture browser logging, you might want to route logs to [Cloud Logging](https://docs.cloud.google.com/logging). For an implementation example, refer to [Stackdriver Error Reporting library](https://github.com/GoogleCloudPlatform/stackdriver-errors-js).

When a user successfully signs in, the client uses Firebase methods to mint an ID token. The client adds the ID token to the `Authorization` header of its request to the server.
    
    
    async function vote(team) {
      if (firebase.auth().currentUser) {
        // Retrieve JWT to identify the user to the Identity Platform service.
        // Returns the current token if it has not expired. Otherwise, this will
        // refresh the token and return a new one.
        try {
          const token = await firebase.auth().currentUser.getIdToken();
          const response = await fetch('/', {
            method: 'POST',
            headers: {
              'Content-Type': 'application/x-www-form-urlencoded',
              Authorization: `Bearer ${token}`,
            },
            body: 'team=' + team, // send application data (vote)
          });
          if (response.ok) {
            const text = await response.text();
            window.alert(text);
            window.location.reload();
          }
        } catch (err) {
          console.log(`Error when submitting vote: ${err}`);
          window.alert('Something went wrong... Please try again!');
        }
      } else {
        window.alert('User not signed in.');
      }
    }

### Integrate with Identity Platform: server-side code

The server uses the [Firebase Admin SDK](https://firebase.google.com/docs/auth/admin) to verify the user ID token sent from the client. If the provided ID token has the correct format, is not expired, and is properly signed, the method returns the decoded ID token. The server extracts the Identity Platform `uid` for that user.

###  Node.js 
    
    
    const firebase = require('firebase-admin');
    // Initialize Firebase Admin SDK
    firebase.initializeApp();
    
    // Extract and verify Id Token from header
    const authenticateJWT = (req, res, next) => {
      const authHeader = req.headers.authorization;
      if (authHeader) {
        const token = authHeader.split(' ')[1];
        // If the provided ID token has the correct format, is not expired, and is
        // properly signed, the method returns the decoded ID token
        firebase
          .auth()
          .verifyIdToken(token)
          .then(decodedToken => {
            const uid = decodedToken.uid;
            req.uid = uid;
            next();
          })
          .catch(err => {
            req.logger.error(`Error with authentication: ${err}`);
            return res.sendStatus(403);
          });
      } else {
        return res.sendStatus(401);
      }
    };

###  Python 
    
    
    def jwt_authenticated(func: Callable[..., int]) -> Callable[..., int]:
        """Use the Firebase Admin SDK to parse Authorization header to verify the
        user ID token.
    
        The server extracts the Identity Platform uid for that user.
        """
    
        @wraps(func)
        def decorated_function(*args: a, **kwargs: a) -> a:
            header = request.headers.get("Authorization", None)
            if header:
                token = header.split(" ")[1]
                try:
                    decoded_token = firebase_admin.auth.verify_id_token(token)
                except Exception as e:
                    logger.exception(e)
                    return Response(status=403, response=f"Error with authentication: {e}")
            else:
                return Response(status=401)
    
            request.uid = decoded_token["uid"]
            return func(*args, **kwargs)
    
        return decorated_function
    
    

###  Java 
    
    
    /** Extract and verify Id Token from header */
    private String authenticateJwt(Map<String, String> headers) {
      String authHeader =
          (headers.get("authorization") != null)
              ? headers.get("authorization")
              : headers.get("Authorization");
      if (authHeader != null) {
        String idToken = authHeader.split(" ")[1];
        // If the provided ID token has the correct format, is not expired, and is
        // properly signed, the method returns the decoded ID token
        try {
          FirebaseToken decodedToken = FirebaseAuth.getInstance().verifyIdToken(idToken);
          String uid = decodedToken.getUid();
          return uid;
        } catch (FirebaseAuthException e) {
          logger.error("Error with authentication: " + e.toString());
          throw new ResponseStatusException(HttpStatus.FORBIDDEN, "", e);
        }
      } else {
        logger.error("Error no authorization header");
        throw new ResponseStatusException(HttpStatus.UNAUTHORIZED);
      }
    }

### Connect the server to Cloud SQL

The server connects to the Cloud SQL instance Unix domain socket using the format: `/cloudsql/CLOUD_SQL_CONNECTION_NAME`.

###  Node.js 
    
    
    /**
     * Connect to the Cloud SQL instance through UNIX Sockets
     *
     * @param {object} credConfig The Cloud SQL connection configuration from Secret Manager
     * @returns {object} Knex's PostgreSQL client
     */
    const connectWithUnixSockets = async credConfig => {
      const dbSocketPath = process.env.DB_SOCKET_PATH || '/cloudsql';
      // Establish a connection to the database
      return Knex({
        client: 'pg',
        connection: {
          user: credConfig.DB_USER, // e.g. 'my-user'
          password: credConfig.DB_PASSWORD, // e.g. 'my-user-password'
          database: credConfig.DB_NAME, // e.g. 'my-database'
          host: `${dbSocketPath}/${credConfig.CLOUD_SQL_CONNECTION_NAME}`,
        },
        ...config,
      });
    };

###  Python 
    
    
    def init_unix_connection_engine(
        db_config: dict[str, int]
    ) -> sqlalchemy.engine.base.Engine:
        """Initializes a Unix socket connection pool for a Cloud SQL instance of PostgreSQL.
    
        Args:
            db_config: a dictionary with connection pool config
    
        Returns:
            A SQLAlchemy Engine instance.
        """
        creds = credentials.get_cred_config()
        db_user = creds["DB_USER"]
        db_pass = creds["DB_PASSWORD"]
        db_name = creds["DB_NAME"]
        db_socket_dir = creds.get("DB_SOCKET_DIR", "/cloudsql")
        cloud_sql_connection_name = creds["CLOUD_SQL_CONNECTION_NAME"]
    
        pool = sqlalchemy.create_engine(
            # Equivalent URL:
            # postgres+pg8000://<db_user>:<db_pass>@/<db_name>
            #                         ?unix_sock=<socket_path>/<cloud_sql_instance_name>/.s.PGSQL.5432
            sqlalchemy.engine.url.URL.create(
                drivername="postgresql+pg8000",
                username=db_user,  # e.g. "my-database-user"
                password=db_pass,  # e.g. "my-database-password"
                database=db_name,  # e.g. "my-database-name"
                query={
                    "unix_sock": f"{db_socket_dir}/{cloud_sql_connection_name}/.s.PGSQL.5432"
                    # e.g. "/cloudsql", "<PROJECT-NAME>:<INSTANCE-REGION>:<INSTANCE-NAME>"
                },
            ),
            **db_config,
        )
        pool.dialect.description_encoding = None
        logger.info("Database engine initialized from unix connection")
    
        return pool
    
    

###  Java 

Use the [Spring Cloud Google Cloud PostgreSQL starter](https://spring.io/projects/spring-cloud-gcp) integration to interact with your PostgreSQL databases in Cloud SQL using Spring JDBC libraries. Set your Cloud SQL for MySQL config to auto-configure a [`DataSource`](https://docs.spring.io/spring-boot/docs/current/reference/html/spring-boot-features.html#boot-features-sql) bean, which, coupled with Spring JDBC, provides a [`JdbcTemplate`](https://docs.spring.io/spring/docs/current/spring-framework-reference/html/jdbc.html#jdbc-JdbcTemplate) object bean that allows for operations such as querying and modifying a database. 
    
    
    # Uncomment and add env vars for local development
    # spring.datasource.username=${DB_USER}
    # spring.datasource.password=${DB_PASSWORD}
    # spring.cloud.gcp.sql.database-name=${DB_NAME}
    # spring.cloud.gcp.sql.instance-connection-name=${CLOUD_SQL_CONNECTION_NAME}  
    
    
    private final JdbcTemplate jdbcTemplate;
    
    public VoteController(JdbcTemplate jdbcTemplate) {
      this.jdbcTemplate = jdbcTemplate;
    }

### Handle sensitive configuration with Secret Manager

Secret Manager provides centralized and secure storage of sensitive data such as Cloud SQL configuration. The server injects the Cloud SQL credentials from Secret Manager at runtime using an environment variable. Learn more about [Using secrets](https://docs.cloud.google.com/run/docs/configuring/services/secrets) with Cloud Run.

###  Node.js 
    
    
    // CLOUD_SQL_CREDENTIALS_SECRET is the resource ID of the secret, passed in by environment variable.
    // Format: projects/PROJECT_ID/secrets/SECRET_ID/versions/VERSION
    const {CLOUD_SQL_CREDENTIALS_SECRET} = process.env;
    if (CLOUD_SQL_CREDENTIALS_SECRET) {
      try {
        // Parse the secret that has been added as a JSON string
        // to retrieve database credentials
        return JSON.parse(CLOUD_SQL_CREDENTIALS_SECRET.toString('utf8'));
      } catch (err) {
        throw Error(
          `Unable to parse secret from Secret Manager. Make sure that the secret is JSON formatted: ${err}`
        );
      }
    }

###  Python 
    
    
    def get_cred_config() -> dict[str, str]:
        """Retrieve Cloud SQL credentials stored in Secret Manager
        or default to environment variables.
    
        Returns:
            A dictionary with Cloud SQL credential values
        """
        secret = os.environ.get("CLOUD_SQL_CREDENTIALS_SECRET")
        if secret:
            return json.loads(secret)

###  Java 
    
    
    /** Retrieve config from Secret Manager */
    public static HashMap<String, Object> getConfig() {
      String secret = System.getenv("CLOUD_SQL_CREDENTIALS_SECRET");
      if (secret == null) {
        throw new IllegalStateException("\"CLOUD_SQL_CREDENTIALS_SECRET\" is required.");
      }
      try {
        HashMap<String, Object> config = new Gson().fromJson(secret, HashMap.class);
        return config;
      } catch (JsonSyntaxException e) {
        logger.error(
            "Unable to parse secret from Secret Manager. Make sure that it is JSON formatted: "
                + e);
        throw new RuntimeException(
            "Unable to parse secret from Secret Manager. Make sure that it is JSON formatted.");
      }
    }

## Set up Identity Platform

Identity Platform requires manual setup in the Google Cloud console.

  1. In the Google Cloud console, enable the Identity Platform API:

[Enable the API](https://console.cloud.google.com/marketplace/details/google-cloud-platform/customer-identity?project=_)

  2. Configure your project:

     1. In a new window, go to the Google Auth Platform > Overview page.

[Go to Overview](https://console.cloud.google.com/auth/overview?project=_)

     2. Click **Get Started** and follow the project configuration setup.

     3. In the **App information** dialog:

        1. Supply the application name.
        2. Select one of the displayed user support emails.
     4. In the **Audience** dialog, select **External**.

     5. In the **Contact information** dialog, enter a contact email.

     6. Agree to the user data policy, then click **Create**.

  3. Create and obtain your OAuth Client ID and Secret:

     1. In the Google Cloud console, go to the APIs & Services > Credentials page.

[Go to Credentials](https://console.cloud.google.com/apis/credentials?project=_)

     2. At the top of the page, click **Create Credentials** and select `OAuth client ID`.

     3. From **Application Type** , select **Web Application** and supply the name.

     4. Click **Create**

     5. The `client_id` and `client_secret` values will be used in the next step.

  4. Configure Google as a provider:

     1. In the Google Cloud console, go to the Identity Providers page.

[Go to Identity Providers](https://console.cloud.google.com/customer-identity/providers?project=_)

     2. Click **Add A Provider**.

     3. Select **Google** from the list.

     4. In the Web SDK Configuration settings, enter the `client_id` and `client_secret` values from the previous step.

     5. Under **Configure your application** , click **Setup Details**.

  5. Copy the configuration to your application:

     * Copy the `apiKey` and `authDomain` values into the sample's `static/config.js` to initialize the Identity Platform Client SDK.

**Note:** This configuration is not yet complete. After you deploy your Cloud Run server, you still need to authorize your service domain, as described in Finishing touches.

## Deploy the service

Follow the steps to complete infrastructure provisioning and deployment:

  1. Create a Cloud SQL instance with postgreSQL database using the [console](https://docs.cloud.google.com/sql/docs/postgres/create-instance) or CLI:
         
         gcloud sql instances create CLOUD_SQL_INSTANCE_NAME \
             --database-version=POSTGRES_16 \
             --region=CLOUD_SQL_REGION \
             --cpu=2 \
             --memory=7680MB \
             --root-password=DB_PASSWORD

  2. Add your Cloud SQL credential values to `postgres-secrets.json`:

###  Node.js 
         
         {
           "CLOUD_SQL_CONNECTION_NAME": "PROJECT_ID:REGION:INSTANCE",
           "DB_NAME": "postgres",
           "DB_USER": "postgres",
           "DB_PASSWORD": "PASSWORD_SECRET"
         }
         

###  Python 
         
         {
           "CLOUD_SQL_CONNECTION_NAME": "PROJECT_ID:REGION:INSTANCE",
           "DB_NAME": "postgres",
           "DB_USER": "postgres",
           "DB_PASSWORD": "PASSWORD_SECRET"
         }
         

###  Java 
         
         {
           "spring.cloud.gcp.sql.instance-connection-name": "PROJECT_ID:REGION:INSTANCE",
           "spring.cloud.gcp.sql.database-name": "postgres",
           "spring.datasource.username": "postgres",
           "spring.datasource.password": "PASSWORD_SECRET"
         }

  3. Create a versioned secret using the [console](https://docs.cloud.google.com/secret-manager/docs/creating-and-accessing-secrets) or CLI:
         
         gcloud secrets create idp-sql-secrets \
             --replication-policy="automatic" \
             --data-file=postgres-secrets.json

  4. Create a service account for the server using the [console](https://docs.cloud.google.com/iam/docs/creating-managing-service-accounts) or CLI:
         
         gcloud iam service-accounts create idp-sql-identity

  5. Grant roles for Secret Manager and Cloud SQL access using the [console](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access#granting-console) or CLI:

     1. Allow the service account associated with the server to access the created secret:
            
            gcloud secrets add-iam-policy-binding idp-sql-secrets \
              --member serviceAccount:idp-sql-identity@PROJECT_ID.iam.gserviceaccount.com \
              --role roles/secretmanager.secretAccessor

     2. Allow the service account associated with the server to access Cloud SQL:
            
            gcloud projects add-iam-policy-binding PROJECT_ID \
              --member serviceAccount:idp-sql-identity@PROJECT_ID.iam.gserviceaccount.com \
              --role roles/cloudsql.client

  6. Create an Artifact Registry:
         
         gcloud artifacts repositories create REPOSITORY \
             --repository-format docker \
             --location REGION

     * `REPOSITORY` is the name of the repository. For each repository location in a project, repository names must be unique.
  7. Build the container image using Cloud Build: 

###  Node.js 
         
         gcloud builds submit --tag REGION-docker.pkg.dev/PROJECT_ID/REPOSITORY/idp-sql

###  Python 
         
         gcloud builds submit --tag REGION-docker.pkg.dev/PROJECT_ID/REPOSITORY/idp-sql

###  Java 

This sample uses [Jib](https://github.com/GoogleContainerTools/jib) to build Docker images using common Java tools. Jib optimizes container builds without the need for a Dockerfile or having [Docker](https://www.docker.com/) installed. Learn more about [building Java containers with Jib](https://docs.cloud.google.com/run/docs/tutorials/jib).

     1. Use the [gcloud credential helper](https://docs.cloud.google.com/artifact-registry/docs/docker/authentication#gcloud-helper) to authorize Docker to push to your Artifact Registry. 
            
            gcloud auth configure-docker

     2. Use the Jib Maven Plugin to build and push the container to Artifact Registry. 
            
            mvn compile jib:build -Dimage=REGION-docker.pkg.dev/PROJECT_ID/REPOSITORY/idp-sql

  8. Deploy the container image to Cloud Run using the [console](https://docs.cloud.google.com/run/docs/deploying#console) or CLI. Note that the server is deployed to allow unauthenticated access. This is so that the user can load the client and begin the process. The server verifies the ID token added to the vote request manually, authenticating the end user.
         
         gcloud run deploy idp-sql \
             --image REGION-docker.pkg.dev/PROJECT_ID/REPOSITORY/idp-sql \
             --allow-unauthenticated \
             --service-account idp-sql-identity@PROJECT_ID.iam.gserviceaccount.com \
             --add-cloudsql-instances PROJECT_ID:REGION:CLOUD_SQL_INSTANCE_NAME \
             --update-secrets CLOUD_SQL_CREDENTIALS_SECRET=idp-sql-secrets:latest

Also note the flags `--service-account`, `--add-cloudsql-instances`, and `--update-secrets`, which specify the service identity, the Cloud SQL instance connection, and the secret name with version as an environment variable, respectively.

**Note:** Environment variables are resolved at instance startup time, so if you use this method, Google recommends that you pin the secret to a particular version rather than using _latest_.



## Finishing touches

Identity Platform requires that you authorize the Cloud Run service URL as an allowed redirect after it has signed in the user:

  1. Edit the Google provider by clicking the pen icon in the [**Identity Providers**](http://console.cloud.google.com/customer-identity/providers) page.

  2. Click **Add Domain** under Authorized Domains on the right panel, and enter the Cloud Run service URL.

You can locate the service URL in the logs after the build or deployment or you can find it anytime using:
         
         gcloud run services describe idp-sql --format 'value(status.url)'

  3. [Go to the APIs & Services > Credentials page](https://console.cloud.google.com/apis/credentials?project=_)

     1. Click the pencil icon beside your OAuth Client ID to edit it and under the `Authorized redirect URIs click the` **Add URI** button.

     2. In the field copy and paste the following URL and click the **Save** button at the bottom of the page.
    
    https://PROJECT_ID.firebaseapp.com/__/auth/handler




## Try it out

To try out the complete service:

  1. Navigate your browser to the URL provided by the previous deployment step.

  2. Click the **Sign in with Google** button and go through the authentication flow.

  3. Add your vote!

It should look like this: ![User Interface shows vote count for each team and a list of votes.](https://docs.cloud.google.com/static/run/docs/tutorials/images/idp-sql-frontend.png)

**Success:** You deployed a Cloud Run service that authenticates end users with Identity Platform and securely manages sensitive data using Secret Manager.



If you choose to continue developing these services, remember that they have restricted Identity and Access Management (IAM) access to the rest of Google Cloud and will need to be given additional IAM roles to access many other services.

## Clean up

To avoid additional charges to your Google Cloud account, delete all the resources you deployed with this tutorial.

### Delete the project

If you created a new project for this tutorial, delete the project. If you used an existing project and need to keep it without the changes you added in this tutorial, delete resources that you created for the tutorial.

The easiest way to eliminate billing is to delete the project that you created for the tutorial. 

To delete the project: 

**Caution** : Deleting a project has the following effects: 
     * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
     * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 

If you plan to explore multiple architectures, tutorials, or quickstarts, reusing projects can help you avoid exceeding project quota limits. 

  1. In the Google Cloud console, go to the **Manage resources** page. 

[Go to Manage resources](https://console.cloud.google.com/iam-admin/projects)

  2. In the project list, select the project that you want to delete, and then click **Delete**. 
  3. In the dialog, type the project ID, and then click **Shut down** to delete the project. 



### Delete tutorial resources

  1. Delete the Cloud Run service you deployed in this tutorial. Cloud Run services don't incur costs until they receive requests.

To delete your Cloud Run service, run the following command:
         
         gcloud run services delete SERVICE-NAME

Replace SERVICE-NAME with the name of your service.

You can also delete Cloud Run services from the [Google Cloud console](https://console.cloud.google.com/run).

  2. Remove the `gcloud` default region configuration you added during tutorial setup:
         
         gcloud config unset run/region
         

  3. Remove the project configuration:
         
         gcloud config unset project
         

  4. Delete other Google Cloud resources created in this tutorial:

     * [Delete the service container image](https://docs.cloud.google.com/artifact-registry/docs/docker/manage-images#deleting_images) from Artifact Registry
     * [Delete the service account `vote-identity@PROJECT_ID.iam.gserviceaccount.com`](https://docs.cloud.google.com/iam/docs/creating-managing-service-accounts#iam-service-accounts-delete-gcloud)
     * [Delete the Cloud SQL instance](https://docs.cloud.google.com/)
     * [Delete the secret in Secret Manager](https://docs.cloud.google.com/)



## What's next

  * Dive deeper into [Connecting from Cloud Run to Cloud SQL](https://docs.cloud.google.com/sql/docs/postgres/connect-run)
  * Learn more about [sign in methods and managing users with Identity Platform](https://docs.cloud.google.com/identity-platform/docs/how-to)
  * Review [other ways to authenticate developers, services, and users](https://docs.cloud.google.com/run/docs/securing/authenticating) of services deployed to Cloud Run
  * Explore other [Cloud Run demos, tutorials, and samples](https://docs.cloud.google.com/run/docs)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
