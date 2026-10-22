---
url: https://docs.cloud.google.com/alloydb/docs/auth-proxy/connect/
title: Connect using the AlloyDB Auth Proxy \u00a0|\u00a0 AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:27:10.479849+00:00
---

# Connect using the AlloyDB Auth Proxy  |  AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/docs/auth-proxy/connect/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)
  * [ Guides ](https://docs.cloud.google.com/alloydb/docs/overview)



Send feedback 

#  Connect using the AlloyDB Auth Proxy Stay organized with collections  Save and categorize content based on your preferences. 

To make authorized, encrypted connections to AlloyDB for PostgreSQL instances, you can use the AlloyDB Auth Proxy. For more information, see [About the AlloyDB Auth Proxy](https://docs.cloud.google.com/alloydb/docs/auth-proxy/overview).

To use the AlloyDB Auth Proxy, you perform several one-time setup steps, then you start the Auth Proxy client and use it to connect to a database.

## Before you begin

The client host must meet these requirements:

  * The client must have a network path to the AlloyDB instance based on your connection method:

    * **Private services access (default)** : The client must have network visibility to the Virtual Private Cloud (VPC) network where the instances reside. Client hosts (such as Compute Engine instances) in this VPC network inherently have this network visibility. Client hosts in external networks (on-premises networks or different VPC networks) have this visibility if the AlloyDB instance's VPC network is connected to the external network by using a [Cloud VPN tunnel](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/overview) or a VLAN attachment for [Dedicated Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/dedicated/provisioning-overview) or [Partner Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/partner/provisioning-overview).
    * **Private Service Connect** : The client's VPC network must have a [Private Service Connect endpoint and a matching private DNS record](https://docs.cloud.google.com/alloydb/docs/configure-private-service-connect#configure-dns), and you must start the Auth Proxy client with the `--psc` flag.
    * **Public IP** : The instance must have [Public IP enabled](https://docs.cloud.google.com/alloydb/docs/connect-public-ip), and you must start the Auth Proxy client with the `--public-ip` flag. When you connect by using the Auth Proxy, you don't need to add the client host's IP address to Authorized external networks.
  * If the client host has an outbound firewall policy, it must allow outgoing connections to port `5433` on your AlloyDB instances' IP addresses and allow outgoing connections to port `443` (the standard HTTPS port) to all IP addresses.

  * If you're using a Compute Engine instance as the client host, it must have the `https://www.googleapis.com/auth/cloud-platform` access scope so that it can use the AlloyDB API. If necessary, [change its access scope](https://docs.cloud.google.com/compute/docs/access/create-enable-service-accounts-for-instances#changeserviceaccountandscopes) to include this scope.




## Download the Auth Proxy client

The machine that you download the Auth Proxy client to depends on whether you want to connect to your AlloyDB instances from within its VPC network, or from outside of it.

If you want to connect to your cluster using [private services access](https://docs.cloud.google.com/alloydb/docs/about-private-services-access), then you can download the Auth Proxy client onto a Compute Engine virtual machine (VM) instance running within the VPC network that has private services access to your cluster.

If you intend to connect to your cluster from outside the VPC, then the machine you install it on depends on which external connection strategy you use. For example, you can install the Auth Proxy client onto a macOS or Windows machine that's local to your application, and then use a SOCKS server running within your AlloyDB VPC network as a connection intermediary. For more information, see [Connect to a cluster from outside its VPC](https://docs.cloud.google.com/alloydb/docs/connect-external#socks).

**Note:** Ensure that you are using the latest Auth Proxy client version. Google releases new versions of the Auth Proxy client monthly. You can find the current version by checking the [Auth Proxy client GitHub releases](https://github.com/GoogleCloudPlatform/alloydb-auth-proxy/releases) page.

### Linux

### 64-bit (AMD)

  1. Download the Auth Proxy client:
         
         wget https://storage.googleapis.com/alloydb-auth-proxy/v1.14.2/alloydb-auth-proxy.linux.amd64 -O alloydb-auth-proxy

  2. Make the Auth Proxy client executable:
         
         chmod +x alloydb-auth-proxy

  3. Add the Auth Proxy client to your PATH:
         
         mkdir -p ~/.local/bin
         mv alloydb-auth-proxy ~/.local/bin/
         export PATH="$HOME/.local/bin:$PATH"

To persist these changes across sessions, add `export PATH="$HOME/.local/bin:$PATH"` to your `~/.bashrc` or `~/.zshrc` file.




### 32-bit (AMD)

  1. Download the Auth Proxy client:
         
         wget https://storage.googleapis.com/alloydb-auth-proxy/v1.14.2/alloydb-auth-proxy.linux.386 -O alloydb-auth-proxy

  2. Make the Auth Proxy client executable:
         
         chmod +x alloydb-auth-proxy

  3. Add the Auth Proxy client to your PATH:
         
         mkdir -p ~/.local/bin
         mv alloydb-auth-proxy ~/.local/bin/
         export PATH="$HOME/.local/bin:$PATH"

To persist these changes across sessions, add `export PATH="$HOME/.local/bin:$PATH"` to your `~/.bashrc` or `~/.zshrc` file.




### 64-bit (ARM)

  1. Download the Auth Proxy client:
         
         wget https://storage.googleapis.com/alloydb-auth-proxy/v1.14.2/alloydb-auth-proxy.linux.arm64 -O alloydb-auth-proxy

  2. Make the Auth Proxy client executable:
         
         chmod +x alloydb-auth-proxy

  3. Add the Auth Proxy client to your PATH:
         
         mkdir -p ~/.local/bin
         mv alloydb-auth-proxy ~/.local/bin/
         export PATH="$HOME/.local/bin:$PATH"

To persist these changes across sessions, add `export PATH="$HOME/.local/bin:$PATH"` to your `~/.bashrc` or `~/.zshrc` file.




### 32-bit (ARM)

  1. Download the Auth Proxy client:
         
         wget https://storage.googleapis.com/alloydb-auth-proxy/v1.14.2/alloydb-auth-proxy.linux.arm -O alloydb-auth-proxy

  2. Make the Auth Proxy client executable:
         
         chmod +x alloydb-auth-proxy

  3. Add the Auth Proxy client to your PATH:
         
         mkdir -p ~/.local/bin
         mv alloydb-auth-proxy ~/.local/bin/
         export PATH="$HOME/.local/bin:$PATH"

To persist these changes across sessions, add `export PATH="$HOME/.local/bin:$PATH"` to your `~/.bashrc` or `~/.zshrc` file.




### macOS

### ARM64

  1. Download the Auth Proxy client:
         
         curl -o alloydb-auth-proxy https://storage.googleapis.com/alloydb-auth-proxy/v1.14.2/alloydb-auth-proxy.darwin.arm64

  2. Make the Auth Proxy client executable:
         
         chmod +x alloydb-auth-proxy

  3. Add the Auth Proxy client to your PATH:
         
         mkdir -p ~/.local/bin
         mv alloydb-auth-proxy ~/.local/bin/
         export PATH="$HOME/.local/bin:$PATH"

To persist these changes across sessions, add `export PATH="$HOME/.local/bin:$PATH"` to your `~/.bashrc` or `~/.zshrc` file.




### AMD64

  1. Download the Auth Proxy client:
         
         curl -o alloydb-auth-proxy https://storage.googleapis.com/alloydb-auth-proxy/v1.14.2/alloydb-auth-proxy.darwin.amd64

  2. Make the Auth Proxy client executable:
         
         chmod +x alloydb-auth-proxy

  3. Add the Auth Proxy client to your PATH:
         
         mkdir -p ~/.local/bin
         mv alloydb-auth-proxy ~/.local/bin/
         export PATH="$HOME/.local/bin:$PATH"

To persist these changes across sessions, add `export PATH="$HOME/.local/bin:$PATH"` to your `~/.bashrc` or `~/.zshrc` file.




### Windows

### 64-bit

  1. Right-click <https://storage.googleapis.com/alloydb-auth-proxy/v1.14.2/alloydb-auth-proxy-x64.exe> and select **Save Link As** to download the Auth Proxy client. Rename the file to `alloydb-auth-proxy.exe`.

  2. Add the Auth Proxy client to your PATH:
         
         New-Item -ItemType Directory -Force -Path "$HOME\bin"
         Move-Item -Path .\alloydb-auth-proxy.exe -Destination "$HOME\bin"
         $userPath = [Environment]::GetEnvironmentVariable("Path", "User")
         [Environment]::SetEnvironmentVariable("Path", "$userPath;$HOME\bin", "User")
         




### 32-bit

  1. Right-click <https://storage.googleapis.com/alloydb-auth-proxy/v1.14.2/alloydb-auth-proxy-x86.exe> and select **Save Link As** to download the Auth Proxy client. Rename the file to `alloydb-auth-proxy.exe`.

  2. Add the Auth Proxy client to your PATH:
         
         New-Item -ItemType Directory -Force -Path "$HOME\bin"
         Move-Item -Path .\alloydb-auth-proxy.exe -Destination "$HOME\bin"
         $userPath = [Environment]::GetEnvironmentVariable("Path", "User")
         [Environment]::SetEnvironmentVariable("Path", "$userPath;$HOME\bin", "User")
         




### Docker image

For convenience, several container images that contain the Auth Proxy client are available in the [Artifact Registry](https://console.cloud.google.com/artifacts).

You can pull the latest image to your local machine using Docker with the following command:
    
    
    docker pull gcr.io/alloydb-connectors/alloydb-auth-proxy:latest

### Other OS

For other operating systems not included here, you can [compile the Auth Proxy client from source](https://github.com/GoogleCloudPlatform/alloydb-auth-proxy).

## Choose the Identity and Access Management (IAM) principal and prepare it for authorization

The AlloyDB Auth Proxy supports the use of these types of IAM principals to authorize connections between your client and an AlloyDB instance:

  * **An attached service account**. If your client host runs on Google Cloud—for example, on a Compute Engine instance—you can authorize connections using the service account attached to that resource.

We recommend that you use a service account for authorization in production environments. An attached service account is the most secure option because it doesn't require a downloaded key.

  * **Your user account**. You can use your own IAM user account to authorize connections.

Using your own user account is convenient in development environments where you are managing AlloyDB resources using the gcloud CLI, developing the database using a tool like `psql`, and developing application code all on the same host.

  * **A user-managed service account**. You can [create an IAM service account](https://docs.cloud.google.com/alloydb/docs/auth-proxy/best-practices#using-a-service-account) for your application and then authorize connections using the service account.

Use a user-managed service account when your client host runs outside of Google Cloud and can't use an attached service account.




After you choose which IAM principal to use, verify that it has the required IAM permissions and that its credentials are available on your client host.

### Required IAM permissions

The IAM principal you use to authorize connections must have the permissions provided by the `roles/alloydb.client` (AlloyDB Client) and `roles/serviceusage.serviceUsageConsumer` (Service Usage Consumer) predefined roles.

**Note:** The `roles/alloydb.admin` (AlloyDB Admin) role also provides the required permissions.

To assign the AlloyDB Client role to an IAM principal:

  * The Cloud Resource Manager API must be enabled in the Google Cloud project.

  * You must have the `roles/owner` (Owner) basic IAM role in the Google Cloud project, or a role that grants these permissions:

    * `resourcemanager.projects.get`
    * `resourcemanager.projects.getIamPolicy`
    * `resourcemanager.projects.setIamPolicy`

To gain these permissions while following the principle of least privilege, ask your administrator to grant you the `roles/resourcemanager.projectIamAdmin` (Project IAM Admin) role.




### Make IAM credentials available on the client host

The Auth Proxy client uses [Application Default Credentials](https://docs.cloud.google.com/docs/authentication/application-default-credentials) (ADC) to locate IAM credentials on the client host. In most environments these credentials are already present, so you don't need to configure anything. The Auth Proxy client looks for the following credential sources, in order:

  * **Your user account**. When you develop locally, authenticate with your own user account by running the following gcloud CLI command:
        
        gcloud auth application-default login
        

The Auth Proxy client detects and uses these credentials. You don't need to download a service account key.

  * **An attached service account**. When your client host runs on Google Cloud—for example, on a Compute Engine instance—the environment's metadata server supplies credentials from the attached service account. The Auth Proxy client discovers and uses these credentials without extra configuration.




#### Other credential sources

Use the following methods only when Application Default Credentials aren't available—for example, when you run the Auth Proxy client outside of Google Cloud, or when you need to override the credentials in the environment.

  * **A service account key**. Use a service account key when your client host runs outside of Google Cloud—for example, in an on-premises data center or on another cloud provider—and you can't use workload identity federation.

[Create a JSON-format service account key](https://docs.cloud.google.com/iam/docs/creating-managing-service-account-keys#creating) and download it to your client host. Then, either set the `GOOGLE_APPLICATION_CREDENTIALS` environment variable to the path of the key file:
        
        export GOOGLE_APPLICATION_CREDENTIALS="/path/to/service-account-key.json"
        

Optionally, you can specify the path with the `--credentials-file` flag when you start the Auth Proxy client:
        
        alloydb-auth-proxy --credentials-file /path/to/service-account-key.json INSTANCE_URI
        

**Caution:** Service account keys are a security risk if they aren't managed correctly. Before you create a key, consider a [more secure alternative](https://docs.cloud.google.com/iam/docs/migrate-from-service-account-keys).
  * **An OAuth 2.0 access token**. Use an access token when another system already issues short-lived tokens for you—for example, a continuous integration pipeline that obtains a token before it starts the Auth Proxy client.

If you already have a valid OAuth 2.0 access token, pass it directly when you start the Auth Proxy client:
        
        alloydb-auth-proxy --token "ACCESS_TOKEN" INSTANCE_URI
        

  * **gcloud CLI credentials**. Use the `--gcloud-auth` flag only when you must reuse an existing `gcloud auth login` session and you can't run `gcloud auth application-default login`.

The `--gcloud-auth` flag makes the Auth Proxy client use the account that you authenticated with `gcloud auth login` instead of using Application Default Credentials. We don't recommend this flag. Run `gcloud auth application-default login` instead.




## Gather connection URIs for the AlloyDB instances

When you start the Auth Proxy client, you identify the AlloyDB instance or instances you want to connect to using this _connection URI_ format:

`projects/PROJECT_ID/locations/REGION_ID/clusters/CLUSTER_ID/instances/INSTANCE_ID`

To see a list of all of your instances' connection URIs, use the gcloud CLI [`alloydb instances list`](https://docs.cloud.google.com/sdk/gcloud/reference/alloydb/instances/list) command:
    
    
    gcloud alloydb instances list \
        --region=REGION_ID \
        --cluster=CLUSTER_ID \
        --project=PROJECT_ID

Replace the following:

  * `REGION_ID`: the region where the instances are placed
  * `CLUSTER_ID`: the ID of the cluster where the instances are placed
  * `PROJECT_ID`: the ID of the project where the cluster is placed



Gather the instance connection URI for each instance you want to connect to.

## Start the Auth Proxy client

When you start the Auth Proxy client, you provide it information about what AlloyDB instances to connect to and, if necessary, credential information to use when authorizing these connections.

When it starts, the Auth Proxy client:

  * Authorizes connections to AlloyDB instances using the credentials and IAM permissions of the IAM principal you have configured. It looks for credentials by following [a specific sequence of steps](https://docs.cloud.google.com/alloydb/docs/auth-proxy/overview#how-authorized).
  * Authorizes public IP connections to source network automatically, if the instance has Public IP enabled.
  * Configures a private, mTLS 1.3 connection to each instance's Auth Proxy server.
  * Begins listening for local client connection requests.



By default, the Auth Proxy client listens for TCP connections on IP address 127.0.0.1, starting at port 5432 and incrementing by one port number for each AlloyDB instance beyond the first. You can specify a different listener address and different ports when you start the Auth Proxy client.

**Warning:** Be careful when binding the Auth Proxy client to an external interface. Anyone with access to that interface or port is authorized to connect to your instance.**Note:** Google recommends that you [run the Auth Proxy client as a persistent service](https://docs.cloud.google.com/alloydb/docs/auth-proxy/best-practices#persistent-service) in production environments.

### Command line
    
    
    alloydb-auth-proxy INSTANCE_URI... \
        [ --credentials-file PATH_TO_KEY_FILE \ ]
        [ --token OAUTH_ACCESS_TOKEN \ ]
        [ --port INITIAL_PORT_NUMBER \ ]
        [ --address LOCAL_LISTENER_ADDRESS \ ]
        [ --auto-iam-authn \ ]
        [ --psc \ ]
        [ --public-ip \ ]
        [ --disable-built-in-telemetry ]

Replace the following:

  * `INSTANCE_URI`: the instance connection URI of an AlloyDB instance to connect to, specified using this format:

`projects/PROJECT_ID/locations/REGION_ID/clusters/CLUSTER_ID/instances/INSTANCE_ID`

You can override the default local listener port that the Auth Proxy client will use for the instance by adding the `port` query parameter to the URI:

`"projects/PROJECT_ID/locations/REGION_ID/clusters/CLUSTER_ID/instances/INSTANCE_ID?port=PORT"`

  * Optional: `PATH_TO_KEY_FILE`: The path to the JSON key file of the user-managed service account to use for connection authorization.

  * Optional: `OAUTH_ACCESS_TOKEN`: An OAuth2 token value to use for connection authorization.

  * Optional: `INITIAL_PORT_NUMBER`: The starting port number to use instead of the default port `5432` when listening for local TCP connections.

  * Optional: `LOCAL_LISTENER_ADDRESS`: The listener address to use instead of the default `127.0.0.1` when listening for local TCP connections.




The optional `--auto-iam-authn` flag lets you authenticate automatically to the instance. This works only for the database user associated with the IAM account that is running the Auth Proxy client. For more information, see [Authenticate automatically using the Auth Proxy](https://docs.cloud.google.com/alloydb/docs/connect-iam#automatic).

The optional `--psc` flag lets the Auth Proxy connect to an instance with Private Service Connect enabled. For more information about setting up DNS with Private Service Connect, see [Configure a DNS managed zone and a DNS record](https://docs.cloud.google.com/alloydb/docs/configure-private-service-connect#configure-dns).

The optional `--public-ip` flag lets the Auth Proxy connect to an instance with Public IP enabled by using the instance's Public IP address. For more information about Public IP, see [Connect using Public IP](https://docs.cloud.google.com/alloydb/docs/connect-public-ip).

The optional `--disable-built-in-telemetry` flag disables the internal metric reporter the Auth Proxy uses to report on connection and network health. By default, the Auth Proxy reports on its internal operations to the `alloydb.googleapis.com` system metric prefix. These metrics help AlloyDB improve performance and identify client connectivity problems. This option is useful for applications that operate in environments where outbound metric exporting is restricted. To opt out of this telemetry, use this flag.

### Docker container

Start the Auth Proxy client using the `docker run` command.

If you're using the credentials provided by your Compute Engine instance, then you can use a command similar to the following:
    
    
    docker run \
      --publish 127.0.0.1:PORT:PORT \
      gcr.io/alloydb-connectors/alloydb-auth-proxy:latest \
      --address 0.0.0.0 \
      --port PORT \
      INSTANCE_URI

Replace the following:

  * `PORT`: The port to use for local connections to the Auth Proxy client. The default is `5432`.

  * `INSTANCE_URI`: The instance connection URI of an AlloyDB instance to connect to, specified using the following format:

`projects/PROJECT_ID/locations/REGION_ID/clusters/CLUSTER_ID/instances/INSTANCE_ID`

You can override the default local listener port that the Auth Proxy client uses for the instance by adding the `port` query parameter to the URI:

`"projects/PROJECT_ID/locations/REGION_ID/clusters/CLUSTER_ID/instances/INSTANCE_ID?port=PORT"`




Always specify `127.0.0.1` prefix in the `--publish` flag so that the Auth Proxy client is not exposed outside the local host.

The `0.0.0.0` value in the `--address` flag is required to make the listener accessible from outside of the Docker container.

To provide credentials that you have stored in a local JSON file, include `--volume` and `--credentials-file` flags when running the `docker run` command:
    
    
    docker run \
      --volume PATH_TO_KEY_FILE:/key.json \
      --publish 127.0.0.1:PORT:PORT \
      gcr.io/alloydb-connectors/alloydb-auth-proxy:latest \
      --address 0.0.0.0 \
      --port PORT \
      --credentials-file=/key.json \
      INSTANCE_URI

Replace `PATH_TO_KEY_FILE` with the path to the JSON key file of the user-managed service account to use for connection authorization.

### Startup Examples

The following examples show various ways to start the Auth Proxy client. They use these example instance connection URIs:
    
    
    projects/myproject/locations/us-central1/clusters/mycluster/instances/myprimary
    
    
    
    projects/myproject/locations/us-central1/clusters/mycluster/instances/myreadpool
    

#### Basic startup
    
    
    alloydb-auth-proxy \
      "projects/myproject/locations/us-central1/clusters/mycluster/instances/myprimary"

In this example, the Auth Proxy client authorizes the connection by following its normal [sequence of authorization steps](https://docs.cloud.google.com/alloydb/docs/auth-proxy/overview#how-authorized) and then starts listening for local connections to the `myprimary` instance on `127.0.0.1:5432`.

#### Startup using a user-managed service account
    
    
    alloydb-auth-proxy \
      "projects/myproject/locations/us-central1/clusters/mycluster/instances/myprimary" \
      --credentials-file "myappaccount/key.json"

In this example, the Auth Proxy client authorizes the connection using the user-managed service account's JSON key stored at `myappaccount/key.json` and then starts listening for local connections to the `myprimary` instance on `127.0.0.1:5432`.

#### Startup connecting to multiple instances
    
    
    alloydb-auth-proxy \
      "projects/myproject/locations/us-central1/clusters/mycluster/instances/myprimary" \
      "projects/myproject/locations/us-central1/clusters/mycluster/instances/myreadpool"

In this example, the Auth Proxy client authorizes the connection by following its normal [sequence of authorization steps](https://docs.cloud.google.com/alloydb/docs/auth-proxy/overview#how-authorized) and then starts listening for local connections to the `myprimary` instance on `127.0.0.1:5432` and to the `myreadpool` instance on `127.0.0.1:5433`.

#### Startup listening on custom ports

Using custom ports for the Auth Proxy client can be useful when you need to reserve port `5432` for other PostgreSQL connections.
    
    
    alloydb-auth-proxy \
      "projects/myproject/locations/us-central1/clusters/mycluster/instances/myprimary?port=5000" \
      "projects/myproject/locations/us-central1/clusters/mycluster/instances/myreadpool?port=5001"

In this example, the Auth Proxy client authorizes the connection by following its normal [sequence of authorization steps](https://docs.cloud.google.com/alloydb/docs/auth-proxy/overview#how-authorized) and then starts listening for local connections to the `myprimary` instance on `127.0.0.1:5000` and to the `myreadpool` instance on `127.0.0.1:5001`.

Because these custom ports are sequential, the same effect can be achieved using this startup command:
    
    
    alloydb-auth-proxy \
      "projects/myproject/locations/us-central1/clusters/mycluster/instances/myprimary" \
      "projects/myproject/locations/us-central1/clusters/mycluster/instances/myreadpool" \
      --port 5000

#### Startup listening on a custom IP address
    
    
    alloydb-auth-proxy \
      "projects/myproject/locations/us-central1/clusters/mycluster/instances/myprimary" \
      --address "0.0.0.0"

In this example, the Auth Proxy client authorizes the connection by following its normal [sequence of authorization steps](https://docs.cloud.google.com/alloydb/docs/auth-proxy/overview#how-authorized) and then starts listening for local connections to the `myprimary` instance on `0.0.0.0:5432`.

## Connect an application to a database using the AlloyDB Auth Proxy

The following examples show how you can connect an application to a database using the AlloyDB Auth Proxy.

The `psql` example provides an example of connecting a command-line tool.

Connecting to an AlloyDB instance using the Auth Proxy is, for several programming languages, identical to connecting to a Cloud SQL for PostgreSQL instance using the Cloud SQL Auth Proxy, so the language examples are the same as those for Cloud SQL for PostgreSQL.

These examples are based on a default startup of the Auth Proxy client so that it is listening for local TCP connections on `127.0.0.1:5432`.

**Note:** With a new cluster, you can connect as the `postgres` user, using the password that you specified when creating the cluster.

### psql
    
    
    psql -h 127.0.0.1 -p 5432 -U DB_USER

Replace `DB_USER` with the database user that you want to connect as—for example, `postgres`.

This prompts you to enter the password of the `DB_USER` user.

### Python
    
    
    import os
    
    import sqlalchemy
    
    
    # connect_tcp_socket initializes a TCP connection pool
    # for an AlloyDB instance.
    def connect_tcp_socket() -> sqlalchemy.engine.base.Engine:
        # Note: Saving credentials in environment variables is convenient, but not
        # secure - consider a more secure solution such as
        # Cloud Secret Manager (https://cloud.google.com/secret-manager) to help
        # keep secrets safe.
        INSTANCE_HOST = os.environ[
            "INSTANCE_HOST"
        ]  # e.g. '127.0.0.1' ('172.17.0.1' if deployed to GAE Flex)
        db_user = os.environ["DB_USER"]  # e.g. 'my-db-user'
        db_pass = os.environ["DB_PASS"]  # e.g. 'my-db-password'
        db_name = os.environ["DB_NAME"]  # e.g. 'my-database'
        db_port = os.environ["DB_PORT"]  # e.g. 5432
    
        pool = sqlalchemy.create_engine(
            # Equivalent URL:
            # postgresql+pg8000://<db_user>:<db_pass>@<INSTANCE_HOST>:<db_port>/<db_name>
            sqlalchemy.engine.url.URL.create(
                drivername="postgresql+pg8000",
                username=db_user,
                password=db_pass,
                host=INSTANCE_HOST,
                port=db_port,
                database=db_name,
            ),
            # ...
        )
        return pool
    
    

### Java
    
    
    import com.zaxxer.hikari.HikariConfig;
    import com.zaxxer.hikari.HikariDataSource;
    import javax.sql.DataSource;
    
    public class TcpConnectionPoolFactory extends ConnectionPoolFactory {
    
      // Note: Saving credentials in environment variables is convenient, but not
      // secure - consider a more secure solution such as
      // Cloud Secret Manager (https://cloud.google.com/secret-manager) to help
      // keep secrets safe.
      private static final String DB_USER = System.getenv("DB_USER");
      private static final String DB_PASS = System.getenv("DB_PASS");
      private static final String DB_NAME = System.getenv("DB_NAME");
    
      private static final String INSTANCE_HOST = System.getenv("INSTANCE_HOST");
      private static final String DB_PORT = System.getenv("DB_PORT");
    
    
      public static DataSource createConnectionPool() {
        // The configuration object specifies behaviors for the connection pool.
        HikariConfig config = new HikariConfig();
    
        // The following URL is equivalent to setting the config options below:
        // jdbc:postgresql://<INSTANCE_HOST>:<DB_PORT>/<DB_NAME>?user=<DB_USER>&password=<DB_PASS>l
    
        // Configure which instance and what database user to connect with.
        config.setJdbcUrl(String.format("jdbc:postgresql://%s:%s/%s", INSTANCE_HOST, DB_PORT, DB_NAME));
        config.setUsername(DB_USER); // e.g. "root", "postgres"
        config.setPassword(DB_PASS); // e.g. "my-password"
    
    
    
        // ... Specify additional connection properties here.
        // ...
    
        // Initialize the connection pool using the configuration object.
        return new HikariDataSource(config);
      }
    }

### Node.js
    
    
    const Knex = require('knex');
    const fs = require('fs');
    
    // createTcpPool initializes a TCP connection pool for an AlloyDB cluster.
    const createTcpPool = async config => {
      // Note: Saving credentials in environment variables is convenient, but not
      // secure - consider a more secure solution such as
      // Cloud Secret Manager (https://cloud.google.com/secret-manager) to help
      // keep secrets safe.
      const dbConfig = {
        client: 'pg',
        connection: {
          host: process.env.INSTANCE_HOST, // e.g. '127.0.0.1'
          port: process.env.DB_PORT, // e.g. '5432'
          user: process.env.DB_USER, // e.g. 'my-user'
          password: process.env.DB_PASS, // e.g. 'my-user-password'
          database: process.env.DB_NAME, // e.g. 'my-database'
        },
        // ... Specify additional properties here.
        ...config,
      };
      // Establish a connection to the database.
      return Knex(dbConfig);
    };

### Go

To see this snippet in the context of a web application, view [the Go examples on GitHub](https://github.com/GoogleCloudPlatform/alloydb-auth-proxy/tree/main/examples/go).
    
    
    package alloydb
    
    import (
    	"database/sql"
    	"fmt"
    	"log"
    	"os"
    
    	// Note: If connecting using the App Engine Flex Go runtime, use
    	// "github.com/jackc/pgx/stdlib" instead, since v4 requires
    	// Go modules which are not supported by App Engine Flex.
    	_ "github.com/jackc/pgx/v5/stdlib"
    )
    
    // connectTCPSocket initializes a TCP connection pool for an AlloyDB cluster.
    func connectTCPSocket() (*sql.DB, error) {
    	mustGetenv := func(k string) string {
    		v := os.Getenv(k)
    		if v == "" {
    			log.Fatalf("Warning: %s environment variable not set.", k)
    		}
    		return v
    	}
    	// Note: Saving credentials in environment variables is convenient, but not
    	// secure - consider a more secure solution such as
    	// Cloud Secret Manager (https://cloud.google.com/secret-manager) to help
    	// keep secrets safe.
    	var (
    		dbUser    = mustGetenv("DB_USER")       // e.g. 'my-db-user'
    		dbPwd     = mustGetenv("DB_PASS")       // e.g. 'my-db-password'
    		dbTCPHost = mustGetenv("INSTANCE_HOST") // e.g. '127.0.0.1' or IP Address of Cluster
    		dbPort    = mustGetenv("DB_PORT")       // e.g. '5432'
    		dbName    = mustGetenv("DB_NAME")       // e.g. 'my-database'
    	)
    
    	dbURI := fmt.Sprintf("host=%s user=%s password=%s port=%s database=%s",
    		dbTCPHost, dbUser, dbPwd, dbPort, dbName)
    
    	// dbPool is the pool of database connections.
    	dbPool, err := sql.Open("pgx", dbURI)
    	if err != nil {
    		return nil, fmt.Errorf("sql.Open: %v", err)
    	}
    
    	// ...
    
    	return dbPool, nil
    }
    

### C#

To see this snippet in the context of a web application, view [the README on GitHub](https://github.com/GoogleCloudPlatform/dotnet-docs-samples/blob/main/cloud-sql/postgres/README.md).
    
    
    using Npgsql;
    using System;
    
    namespace CloudSql
    {
        public class PostgreSqlTcp
        {
            public static NpgsqlConnectionStringBuilder NewPostgreSqlTCPConnectionString()
            {
                // Equivalent connection string:
                // "Uid=<DB_USER>;Pwd=<DB_PASS>;Host=<INSTANCE_HOST>;Database=<DB_NAME>;"
                var connectionString = new NpgsqlConnectionStringBuilder()
                {
                    // Note: Saving credentials in environment variables is convenient, but not
                    // secure - consider a more secure solution such as
                    // Cloud Secret Manager (https://cloud.google.com/secret-manager) to help
                    // keep secrets safe.
                    Host = Environment.GetEnvironmentVariable("INSTANCE_HOST"),     // e.g. '127.0.0.1'
                    // Set Host to 'cloudsql' when deploying to App Engine Flexible environment
                    Username = Environment.GetEnvironmentVariable("DB_USER"), // e.g. 'my-db-user'
                    Password = Environment.GetEnvironmentVariable("DB_PASS"), // e.g. 'my-db-password'
                    Database = Environment.GetEnvironmentVariable("DB_NAME"), // e.g. 'my-database'
    
                    // The Cloud SQL proxy provides encryption between the proxy and instance.
                    SslMode = SslMode.Disable,
                };
                connectionString.Pooling = true;
                // Specify additional properties here.
                return connectionString;
            }
        }
    }

### Ruby

To see this snippet in the context of a web application, view [the README on GitHub](https://github.com/GoogleCloudPlatform/ruby-docs-samples/blob/main/cloud-sql/postgres/activerecord/README.md).
    
    
    development:
      adapter: postgresql
      # Configure additional properties here.
      username: <%= ENV["DB_USER"] %>  # e.g. "my-database-user"
      password: <%= ENV["DB_PASS"] %> # e.g. "my-database-password"
      database: <%= ENV.fetch("DB_NAME") { "vote_development" } %>
      host: <%= ENV.fetch("DB_HOST") { "127.0.0.1" }%> # '172.17.0.1' if deployed to GAE Flex
      port: <%= ENV.fetch("DB_PORT")  { 5432 }%>

### PHP

To see this snippet in the context of a web application, view [the README on GitHub](https://github.com/GoogleCloudPlatform/php-docs-samples/blob/main/cloud_sql/postgres/pdo/README.md).
    
    
    // $username = 'your_db_user';
    // $password = 'yoursupersecretpassword';
    // $dbName = 'your_db_name';
    // $dbHost = "127.0.0.1";
    
    // Connect using TCP
    $dsn = sprintf('pgsql:dbname=%s;host=%s', $dbName, $dbHost);
    
    // Connect to the database
    $conn = new PDO($dsn, $username, $password, $connConfig);

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
