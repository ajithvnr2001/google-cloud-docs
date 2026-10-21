---
url: https://docs.cloud.google.com/run/docs/tutorials/system-packages/
title: Using system packages tutorial \u00a0|\u00a0 Cloud Run \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T02:49:27.753179+00:00
---

# Using system packages tutorial  |  Cloud Run  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/run/docs/tutorials/system-packages/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run)



Send feedback 

#  Using system packages tutorial Stay organized with collections  Save and categorize content based on your preferences. 

This tutorial shows how to build a custom [Cloud Run](https://cloud.google.com/run) service that transforms a graph description input parameter into a diagram in the `PNG` image format. It uses [Graphviz](http://www.graphviz.org/) and is installed as a system package in the service's container environment. Graphviz is used via command-line utilities to serve requests.

## Objectives

  * Write and build a [custom container](https://www.docker.com/resources/what-container) with a [Dockerfile](https://docs.docker.com/engine/reference/builder/)
  * Write, build, and deploy a Cloud Run service
  * Use [Graphviz dot](http://www.graphviz.org/documentation/) utility to generate diagrams
  * Test the service by posting a DOT syntax diagram from the collection or your own creation



## Costs

In this document, you use the following billable components of Google Cloud: 

  * [Cloud Build](https://cloud.google.com/build)
  * [Artifact Registry](https://docs.cloud.google.com/artifact-registry)
  * [Cloud Run](https://cloud.google.com/run)



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

  6. [Enable the Cloud Run Admin API](https://console.cloud.google.com/apis/library/run.googleapis.com)
  7. [Install and initialize](https://docs.cloud.google.com/sdk/docs) the gcloud CLI.
  8. Update components: 
         
         gcloud components update




### Required roles

To get the permissions that you need to complete the tutorial, ask your administrator to grant you the following IAM roles on your project: 

  * [Cloud Build Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.builds.editor) (`roles/cloudbuild.builds.editor`)
  * [Cloud Run Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.admin) (`roles/run.admin`)
  * [Create Service Accounts ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountCreator) (`roles/iam.serviceAccountCreator`)
  * [Service Account User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`)
  * [Service Usage Consumer ](https://docs.cloud.google.com/iam/docs/roles-permissions/serviceusage#serviceusage.serviceUsageConsumer) (`roles/serviceusage.serviceUsageConsumer`)
  * [Storage Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.admin) (`roles/storage.admin`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

**Note:** [IAM basic roles](https://docs.cloud.google.com/iam/docs/roles-overview#basic) might also contain permissions to complete the tutorial. You shouldn't grant basic roles in a production environment, but you can grant them in a development or test environment. 

## Setting up gcloud defaults

To configure gcloud with defaults for your Cloud Run service:

  1. Set your default project:
         
         gcloud config set project PROJECT_ID

Replace PROJECT_ID with the name of the project you created for this tutorial.

  2. Configure gcloud for your chosen region:
         
         gcloud config set run/region REGION

Replace REGION with the supported Cloud Run region of your choice.




### Cloud Run locations

Cloud Run is regional, which means the infrastructure that runs your Cloud Run services is located in a specific region and is managed by Google to be redundantly available across [all the zones within that region](https://docs.cloud.google.com/docs/geography-and-regions).   
  


Meeting your latency, availability, or durability requirements are primary factors for selecting the region where your Cloud Run services are run. You can generally select the region nearest to your users but you should consider the location of the [other Google Cloud products](https://cloud.google.com/about/locations/#locations) that are used by your Cloud Run service. Using Google Cloud products together across multiple locations can affect your service's latency as well as cost.  
  


Cloud Run is available in the following regions:

#### Subject to [Tier 1 pricing](https://cloud.google.com/run/pricing#tables)

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



#### Subject to [Tier 2 pricing](https://cloud.google.com/run/pricing#tables)

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

## Retrieving the code sample

To retrieve the code sample for use:

  1. Clone the sample app repository to your local machine:

###  Node.js 
         
         git clone https://github.com/GoogleCloudPlatform/nodejs-docs-samples.git

Alternatively, you can [ download the sample ](https://github.com/GoogleCloudPlatform/nodejs-docs-samples/archive/master.zip) as a zip file and extract it. 

###  Python 
         
         git clone https://github.com/GoogleCloudPlatform/python-docs-samples.git

Alternatively, you can [ download the sample ](https://github.com/GoogleCloudPlatform/python-docs-samples/archive/master.zip) as a zip file and extract it. 

###  Go 
         
         git clone https://github.com/GoogleCloudPlatform/golang-samples.git

Alternatively, you can [ download the sample ](https://github.com/GoogleCloudPlatform/golang-samples/archive/master.zip) as a zip file and extract it. 

###  Java 
         
         git clone https://github.com/GoogleCloudPlatform/java-docs-samples.git

Alternatively, you can [ download the sample ](https://github.com/GoogleCloudPlatform/java-docs-samples/archive/master.zip) as a zip file and extract it. 

  2. Change to the directory that contains the Cloud Run sample code:

###  Node.js 
         
         cd nodejs-docs-samples/run/system-package/

###  Python 
         
         cd python-docs-samples/run/system-package/

###  Go 
         
         cd golang-samples/run/system_package/

###  Java 
         
         cd java-docs-samples/run/system-package/




## Visualizing the architecture

The basic architecture looks like this:

![Diagram showing request flow from user to web service to graphviz dot
    utility.](https://docs.cloud.google.com/static/run/docs/tutorials/images/diagram-as-a-service.png) For the diagram source, see the [ DOT Description](https://docs.cloud.google.com/static/run/docs/tutorials/resources/diagram-as-a-service.dot.txt)

The user makes an HTTP request to the Cloud Run service which executes a Graphviz utility to transform the request into an image. That image is delivered to the user as the HTTP response.

## Understanding the code

### Defining your environment configuration with the `Dockerfile`

**Key Point:** Use your `Dockerfile` to customize your environment with libraries, utilities, environment variables, configuration files, and startup processes. This is the container-based approach for "server configuration".

Your `Dockerfile` is specific to the language and base operating environment, such as Ubuntu, that your service will use.

This service requires one or more additional system packages not available by default.

  1. Open the `Dockerfile` in an editor.

  2. Look for a `Dockerfile` [`RUN`](https://docs.docker.com/engine/reference/builder/#run) statement. This statement allows running arbitrary shell commands to modify the environment. If the `Dockerfile` has multiple stages, identified by finding multiple `FROM` statements, it will be found in the last stage.

The specific packages required and the mechanism to install them varies by the operating system declared inside the container.

To get instructions for your operating system or base image, click the appropriate tab.

Debian/Ubuntu
         
         RUN apt-get update -y && apt-get install -y \
           graphviz \
           && apt-get clean

Alpine Alpine requires a second package for font support. 
         
         RUN apk --no-cache add graphviz

To determine the operating system of your container image, check the name in the `FROM` statement or a README associated with your base image. For example, if you extend from `node`, you can find documentation and the parent `Dockerfile` on [Docker Hub](http://hub.docker.com/_/node).

  3. Test your customization by building the image, using [`docker build` locally](https://docs.cloud.google.com/run/docs/building/containers#building_locally_and_pushing_using_docker) or Cloud Build.




### Handling incoming requests

The sample service uses parameters from the incoming HTTP request to invoke a system call that executes the appropriate `dot` utility command.

In the HTTP handler below, a graph description input parameter is extracted from the `dot` querystring variable.

Graph descriptions can include characters which must be [URL encoded](https://wikipedia.org/wiki/Query_string#URL_encoding) for use in a querystring.

###  Node.js 
    
    
    app.get('/diagram.png', (req, res) => {
      try {
        const image = createDiagram(req.query.dot);
        res.setHeader('Content-Type', 'image/png');
        res.setHeader('Content-Length', image.length);
        res.setHeader('Cache-Control', 'public, max-age=86400');
        res.send(image);
      } catch (err) {
        console.error(`error: ${err.message}`);
        const errDetails = (err.stderr || err.message).toString();
        if (errDetails.includes('syntax')) {
          res.status(400).send(`Bad Request: ${err.message}`);
        } else {
          res.status(500).send('Internal Server Error');
        }
      }
    });

###  Python 
    
    
    @app.route("/diagram.png", methods=["GET"])
    def index():
        """Takes an HTTP GET request with query param dot and
        returns a png with the rendered DOT diagram in a HTTP response.
        """
        try:
            image = create_diagram(request.args.get("dot"))
            response = make_response(image)
            response.headers.set("Content-Type", "image/png")
            return response
    
        except Exception as e:
            print(f"error: {e}")
    
            # If no graphviz definition or bad graphviz def, return 400
            if "syntax" in str(e):
                return f"Bad Request: {e}", 400
    
            return "Internal Server Error", 500
    
    

###  Go 
    
    
    // diagramHandler renders a diagram using HTTP request parameters and the dot command.
    func diagramHandler(w http.ResponseWriter, r *http.Request) {
    	if r.Method != http.MethodGet {
    		log.Printf("method not allowed: %s", r.Method)
    		http.Error(w, fmt.Sprintf("HTTP Method %s Not Allowed", r.Method), http.StatusMethodNotAllowed)
    		return
    	}
    
    	q := r.URL.Query()
    	dot := q.Get("dot")
    	if dot == "" {
    		log.Print("no graphviz definition provided")
    		http.Error(w, "Bad Request", http.StatusBadRequest)
    		return
    	}
    
    	// Cache header must be set before writing a response.
    	w.Header().Set("Cache-Control", "public, max-age=86400")
    
    	input := strings.NewReader(dot)
    	if err := createDiagram(w, input); err != nil {
    		log.Printf("createDiagram: %v", err)
    		// Do not cache error responses.
    		w.Header().Del("Cache-Control")
    		if strings.Contains(err.Error(), "syntax") {
    			http.Error(w, "Bad Request: DOT syntax error", http.StatusBadRequest)
    		} else {
    			http.Error(w, "Internal Server Error", http.StatusInternalServerError)
    		}
    	}
    }
    

###  Java 
    
    
    get(
        "/diagram.png",
        (req, res) -> {
          InputStream image = null;
          try {
            String dot = req.queryParams("dot");
            image = createDiagram(dot);
            res.header("Content-Type", "image/png");
            res.header("Content-Length", Integer.toString(image.available()));
            res.header("Cache-Control", "public, max-age=86400");
          } catch (Exception e) {
            if (e.getMessage().contains("syntax")) {
              res.status(400);
              return String.format("Bad Request: %s", e.getMessage());
            } else {
              res.status(500);
              return "Internal Server Error";
            }
          }
          return image;
        });

You'll need to differentiate between internal server errors and invalid user input. This sample service returns an Internal Server Error for all dot command-line errors unless the error message contains the string `syntax`, which indicates a user input problem.

### Generating a diagram

The core logic of diagram generation uses the dot command-line tool to process the graph description input parameter into a diagram in the PNG image format.

###  Node.js 
    
    
    // Generate a diagram based on a graphviz DOT diagram description.
    const createDiagram = dot => {
      if (!dot) {
        throw new Error('syntax: no graphviz definition provided');
      }
    
      // Adds a watermark to the dot graphic.
      const dotFlags = [
        '-Glabel="Made on Cloud Run"',
        '-Gfontsize=10',
        '-Glabeljust=right',
        '-Glabelloc=bottom',
        '-Gfontcolor=gray',
      ].join(' ');
    
      const image = execSync(`/usr/bin/dot ${dotFlags} -Tpng`, {
        input: dot,
      });
      return image;
    };

###  Python 
    
    
    def create_diagram(dot):
        """Generates a diagram based on a graphviz DOT diagram description.
    
        Args:
            dot: diagram description in graphviz DOT syntax
    
        Returns:
            A diagram in the PNG image format.
        """
        if not dot:
            raise Exception("syntax: no graphviz definition provided")
    
        dot_args = [  # These args add a watermark to the dot graphic.
            "-Glabel=Made on Cloud Run",
            "-Gfontsize=10",
            "-Glabeljust=right",
            "-Glabelloc=bottom",
            "-Gfontcolor=gray",
            "-Tpng",
        ]
    
        # Uses local `dot` binary from Graphviz:
        # https://graphviz.gitlab.io
        image = subprocess.run(
            ["dot"] + dot_args, input=dot.encode("utf-8"), stdout=subprocess.PIPE
        ).stdout
    
        if not image:
            raise Exception("syntax: bad graphviz definition provided")
        return image
    
    

###  Go 
    
    
    // createDiagram generates a diagram image from the provided io.Reader written to the io.Writer.
    func createDiagram(w io.Writer, r io.Reader) error {
    	stderr := new(bytes.Buffer)
    	args := []string{
    		"-Glabel=Made on Cloud Run",
    		"-Gfontsize=10",
    		"-Glabeljust=right",
    		"-Glabelloc=bottom",
    		"-Gfontcolor=gray",
    		"-Tpng",
    	}
    	cmd := exec.Command("/usr/bin/dot", args...)
    	cmd.Stdin = r
    	cmd.Stdout = w
    	cmd.Stderr = stderr
    
    	if err := cmd.Run(); err != nil {
    		return fmt.Errorf("exec(%s) failed (%w): %s", cmd.Path, err, stderr.String())
    	}
    
    	return nil
    }
    

###  Java 
    
    
    // Generate a diagram based on a graphviz DOT diagram description.
    public static InputStream createDiagram(String dot) {
      if (dot == null || dot.isEmpty()) {
        throw new NullPointerException("syntax: no graphviz definition provided");
      }
      // Adds a watermark to the dot graphic.
      List<String> args = new ArrayList<>();
      args.add("/usr/bin/dot");
      args.add("-Glabel=\"Made on Cloud Run\"");
      args.add("-Gfontsize=10");
      args.add("-Glabeljust=right");
      args.add("-Glabelloc=bottom");
      args.add("-Gfontcolor=gray");
      args.add("-Tpng");
    
      StringBuilder output = new StringBuilder();
      InputStream stdout = null;
      try {
        ProcessBuilder pb = new ProcessBuilder(args);
        Process process = pb.start();
        OutputStream stdin = process.getOutputStream();
        stdout = process.getInputStream();
        // The Graphviz dot program reads from stdin.
        Writer writer = new OutputStreamWriter(stdin, "UTF-8");
        writer.write(dot);
        writer.close();
        process.waitFor();
      } catch (Exception e) {
        System.out.println(e);
      }
      return stdout;
    }

### Designing a secure service

Any vulnerabilities in the `dot` tool are potential vulnerabilities of the web service. You can mitigate this by using up-to-date versions of the `graphviz` package through re-building the container image on a regular basis.

If you extend the current sample to accept user input as command-line parameters, you should protect against [command-injection attacks](https://wikipedia.org/wiki/Code_injection#Shell_injection). Some of the ways to prevent injection attacks include:

  * Mapping inputs to a dictionary of supported parameters
  * Validating inputs match a range of known-safe values, perhaps using regular expressions
  * Escaping inputs to ensure shell syntax is not evaluated



You can further mitigate potential vulnerabilities by deploying the service with a service account that has not been granted any permissions to use Google Cloud services, rather than using the default account, which has commonly used permissions. For that reason, the steps in this tutorial create and use a new service account.

## Shipping the code

To ship your code, you build with Cloud Build, and upload to Artifact Registry, and deploy to Cloud Run:

  1. Create an Artifact Registry:
         
         gcloud artifacts repositories create REPOSITORY \
             --repository-format docker \
             --location REGION

Replace:

     * REPOSITORY: a unique name for the repository. For each repository location in a project, repository names must be unique.
     * REGION: the Google Cloud region to be used for the Artifact Registry repository.
  2. Run the following command to build your container and publish on Artifact Registry.

###  Node.js 
         
         gcloud builds submit --tag REGION-docker.pkg.dev/PROJECT_ID/REPOSITORY/graphviz

Where PROJECT_ID is your Google Cloud project ID, and `graphviz` is the name you want to give your service.

Upon success, you will see a SUCCESS message containing the ID, creation time, and image name. The image is stored in Artifact Registry and can be re-used if desired. 

###  Python 
         
         gcloud builds submit --tag REGION-docker.pkg.dev/PROJECT_ID/REPOSITORY/graphviz

Where PROJECT_ID is your Google Cloud project ID, and `graphviz` is the name you want to give your service.

Upon success, you will see a SUCCESS message containing the ID, creation time, and image name. The image is stored in Artifact Registry and can be reused if desired. 

###  Go 
         
         gcloud builds submit --tag REGION-docker.pkg.dev/PROJECT_ID/REPOSITORY/graphviz

Where PROJECT_ID is your Google Cloud project ID, and `graphviz` is the name you want to give your service.

Upon success, you will see a SUCCESS message containing the ID, creation time, and image name. The image is stored in Artifact Registry and can be reused if desired. 

###  Java 

This sample uses [Jib](https://github.com/GoogleContainerTools/jib) to build Docker images using common Java tools. Jib optimizes container builds without the need for a Dockerfile or having [Docker](https://www.docker.com/) installed. Learn more about [building Java containers with Jib](https://docs.cloud.google.com/run/docs/tutorials/jib). 
     1. Using the Dockerfile, configure and build a base image with the system packages installed to override Jib's default base image:
            
            # Use the Official eclipse-temurin image for a lean production stage of our multi-stage build.
            # https://hub.docker.com/_/eclipse-temurin/
            FROM eclipse-temurin:17.0.18_8-jre
            
            RUN apt-get update -y && apt-get install -y \
              graphviz \
              && apt-get clean
            
            gcloud builds submit --tag REGION-docker.pkg.dev/PROJECT_ID/REPOSITORY/graphviz-base

Where PROJECT_ID is your Google Cloud project ID.

     2. Use the [gcloud credential helper](https://docs.cloud.google.com/run/docs/tutorials/system-packages#gcloud-helper) to authorize Docker to push to your Artifact Registry. 
            
            gcloud auth configure-docker

     3. Build your final container with Jib and publish on Artifact Registry:
            
            <plugin>
              <groupId>com.google.cloud.tools</groupId>
              <artifactId>jib-maven-plugin</artifactId>
              <version>3.4.0</version>
              <configuration>
                <from>
                  <image>gcr.io/PROJECT_ID/graphviz-base</image>
                </from>
                <to>
                  <image>gcr.io/PROJECT_ID/graphviz</image>
                </to>
              </configuration>
            </plugin>
            
            mvn compile jib:build \
             -Dimage=REGION-docker.pkg.dev/PROJECT_ID/REPOSITORY/graphviz \
             -Djib.from.image=REGION-docker.pkg.dev/PROJECT_ID/REPOSITORY/graphviz-base

Where PROJECT_ID is your Google Cloud project ID.

  3. Deploy using the following:

###  gcloud 

     1. Create a new service account. Your code, including any system packages it uses, can use only those Google Cloud services that have been granted to this service account. 
            
            gcloud iam service-accounts create SA_NAME

Where SA_NAME is a name you give this service account. If there is an error or a vulnerability in your code, your code will not be able to access any of your other Google Cloud project resources.
     2. Deploy the code, specifying the service account. 
            
            gcloud run deploy graphviz-web --service-account SA_NAME@PROJECT_ID.iam.gserviceaccount.com  --image REGION-docker.pkg.dev/PROJECT_ID/REPOSITORY/graphviz

Where PROJECT_ID is your Google Cloud project ID, SA_NAME is the name of the service account you created, and `graphviz` is the name of the container from above and `graphviz-web` is the name of the service. Respond `Y` to the "allow unauthenticated" prompt. See [Managing access](https://docs.cloud.google.com/run/docs/securing/managing-access) for more details on IAM-based authentication.
     3. Wait for the deployment to finish. This can take about half a minute. On success, the command line displays the service URL.

### Terraform

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

The following Terraform code creates a Cloud Run service.
    
    resource "google_service_account" "graphviz" {
      account_id   = "graphviz"
      display_name = "GraphViz Tutorial Service Account"
    }
    
    resource "google_cloud_run_v2_service" "default" {
      name     = "graphviz-example"
      location = "us-central1"
    
      deletion_protection = false # set to "true" in production
    
      template {
        containers {
          # Replace with the URL of your graphviz image
          #   gcr.io/<YOUR_GCP_PROJECT_ID>/graphviz
          image = "us-docker.pkg.dev/cloudrun/container/hello"
        }
    
        service_account = google_service_account.graphviz.email
      }
    }

Replace `IMAGE_URL` with a reference to the container image, for example, `us-docker.pkg.dev/cloudrun/container/hello:latest`. If you use Artifact Registry, the [repository](https://docs.cloud.google.com/artifact-registry/docs/repositories/create-repos#docker) REPO_NAME must already be created. The URL follows the format of `LOCATION-docker.pkg.dev/PROJECT_ID/REPO_NAME/PATH:TAG` .

The following Terraform code makes your Cloud Run service public.
    
    # Make Cloud Run service publicly accessible
    resource "google_cloud_run_service_iam_member" "allow_unauthenticated" {
      service  = google_cloud_run_v2_service.default.name
      location = google_cloud_run_v2_service.default.location
      role     = "roles/run.invoker"
      member   = "allUsers"
    }

  4. If you want to deploy a code update to the service, repeat the previous steps. Each deployment to a service creates a new revision and automatically starts serving traffic when ready.




## Try it out

Try out your service by sending HTTP `POST` requests with DOT syntax descriptions in the request payload.

  1. Send an HTTP request to your service.

Copy the URL into your browser URL bar and update `[SERVICE_DOMAIN]`:
         
         https://SERVICE_DOMAIN/diagram.png?dot=digraph Run { rankdir=LR Code -> Build -> Deploy -> Run }

You can embed the diagram in a web page:
         
         <img src="https://SERVICE_DOMAIN/diagram.png?dot=digraph Run { rankdir=LR Code -> Build -> Deploy -> Run }" />

  2. Open the resulting `diagram.png` file in any application that supports `PNG` files, such as Chrome.

It should look like this:

![Diagram showing the stage flow
  of Code to Build to Deploy to 'Run'.](https://docs.cloud.google.com/static/run/docs/tutorials/images/hello-cloud-run.png) Source: [ DOT Description](https://github.com/GoogleCloudPlatform/golang-samples/blob/master/run/system_package/library/hello-cloud-run.dot)



You can explore a small collection of [ready-made diagram descriptions](https://github.com/GoogleCloudPlatform/golang-samples/tree/master/run/system_package/library).

  1. Copy the contents of the selected `.dot` file
  2. Send an HTTP request to your service.

Copy the URL into your browser URL bar
         
         https://SERVICE_DOMAIN/diagram.png?dot=SELECTED DOTFILE CONTENTS

**Success:** You deployed a custom Cloud Run service that transforms a graph description input parameter into a diagram in the `PNG` image format.



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

     * [Delete the container image](https://docs.cloud.google.com/artifact-registry/docs/docker/manage-images#deleting_images) named `REGION-docker.pkg.dev/PROJECT_ID/REPOSITORY/graphviz` from Artifact Registry.

     * Delete the service account SA_NAME.
           
           gcloud iam service-accounts delete SA_NAME@PROJECT_ID.iam.gserviceaccount.com




## What's next

  * Experiment with your graphviz app: 
    * Add support for other graphviz utilities which apply different algorithms to diagram generation.
    * Save diagrams to [Cloud Storage](https://cloud.google.com/storage). Do you want to save the image or the DOT syntax?
    * Implement content abuse protection with [Cloud Natural Language API](https://docs.cloud.google.com/natural-language).
    * See another example of a system package in the [Image Processing with Cloud Run tutorial](https://docs.cloud.google.com/run/docs/tutorials/image-processing).
  * Explore reference architectures, diagrams, and best practices about Google Cloud. Take a look at our [Cloud Architecture Center](https://docs.cloud.google.com/architecture). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
