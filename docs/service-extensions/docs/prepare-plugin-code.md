---
url: https://docs.cloud.google.com/service-extensions/docs/prepare-plugin-code/
title: Prepare the plugin code \u00a0|\u00a0 Service Extensions \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T06:49:15.214718+00:00
---

# Prepare the plugin code  |  Service Extensions  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-extensions/docs/prepare-plugin-code/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Service Extensions ](https://docs.cloud.google.com/service-extensions/docs)
  * [ Guides ](https://docs.cloud.google.com/service-extensions/docs/overview)



Send feedback 

#  Prepare the plugin code Stay organized with collections  Save and categorize content based on your preferences. 

The custom code that you create for Service Extensions plugins must be packaged and uploaded to Artifact Registry before other services can access it. This page describes how to create plugin code, package the code, and upload it to an Artifact Registry repository.

This feature is in [Preview](https://cloud.google.com/products#product-launch-stages) for Media CDN.

For information about Service Extensions, see [Service Extensions overview](https://docs.cloud.google.com/service-extensions/docs/overview).

Before you start, review the [best practices](https://docs.cloud.google.com/service-extensions/docs/plugin-best-practices) for writing plugin code.

For more examples, see [Code samples for plugins](https://docs.cloud.google.com/service-extensions/docs/plugin-code-samples).

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. Enable the Network Services, Network Actions, Artifact Registry, Cloud Build, Cloud Logging, and Cloud Monitoring APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=networkservices.googleapis.com,networkactions.googleapis.com,artifactregistry.googleapis.com,cloudbuild.googleapis.com,logging.googleapis.com,monitoring.googleapis.com)

  5. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
  6. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  7. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  8. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  9. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  10. Enable the Network Services, Network Actions, Artifact Registry, Cloud Build, Cloud Logging, and Cloud Monitoring APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=networkservices.googleapis.com,networkactions.googleapis.com,artifactregistry.googleapis.com,cloudbuild.googleapis.com,logging.googleapis.com,monitoring.googleapis.com)

  11. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
  12. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  13. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init




## Set up the toolchain

### C++

The [Proxy-Wasm C++ SDK](https://github.com/proxy-wasm/proxy-wasm-cpp-sdk) let developers use C++ to implement WebAssembly (Wasm) plugins for Service Extensions. The SDK uses the C++ WebAssembly toolchain [Emscripten](https://emscripten.org), as well as other libraries, such as protobuf and, optionally, Abseil.

Because building plugins written in C++ depends on specific versions of these tools and libraries, we recommend using the Docker image provided by the Proxy-Wasm C++ SDK. The instructions for C++ on this page use the Docker method. To build C++ plugins without using Docker, see the [Proxy-Wasm C++ SDK documentation](https://github.com/proxy-wasm/proxy-wasm-cpp-sdk/blob/main/docs/building.md#dependencies-for-building-wasm-modules).

  1. [Install Docker](https://docs.docker.com/install/linux/docker-ce/ubuntu/) if it's not already installed. Docker is included in [Cloud Shell](https://docs.cloud.google.com/shell/docs), the Google Cloud interactive shell environment.

  2. Download a copy of the Proxy-Wasm C++ SDK. The simplest way to do this is to clone the Git repository:
         
         git clone https://github.com/proxy-wasm/proxy-wasm-cpp-sdk.git
         

  3. Build the Proxy-Wasm C++ SDK Docker image from the Dockerfile provided by the SDK:
         
         cd proxy-wasm-cpp-sdk
         docker build -t wasmsdk:v3 -f Dockerfile-sdk .
         

When the command completes building SDK libraries and dependencies, the resulting Docker image is associated with the specified tag, which is `wasmsdk:v3` in this example.




### Go

The [Proxy-Wasm Go SDK](https://github.com/proxy-wasm/proxy-wasm-go-sdk) provides a full-feature Go SDK. Go provides good performance and rich support for third-party libraries written in pure Go.

**Note:** Compiling libraries by using CGo to Wasm is not supported.

[Install the Go toolchain v1.24.0](https://go.dev/doc/install).

### Rust

The customization capability of Service Extensions is provided through the use of WebAssembly and Proxy-Wasm. WebAssembly supports a number of programming languages. Google recommends [Rust](https://www.rust-lang.org/) because it provides excellent WebAssembly support and Proxy-Wasm provides a full-featured Rust SDK. Rust also provides good performance and strong type safety.

  1. [Install the Rust toolchain](https://www.rust-lang.org/tools/install).

At the end of the installation process, follow any instructions printed to the console to finish the configuration process.

  2. Add Wasm support to the Rust toolchain:
         
         rustup target add wasm32-wasip1
         




## Create the plugin package

### C++

  1. Create a new directory, separate from `proxy-wasm-cpp-sdk`:
         
         mkdir myproject
         

  2. In the directory, create a Makefile with the following contents:
         
         # Express any dependencies
         PROTOBUF=     # full / lite / none
         WASM_DEPS=    # absl_base re2 ...
         
         # Include the SDK Makefile
         PROXY_WASM_CPP_SDK=/sdk
         include ${PROXY_WASM_CPP_SDK}/Makefile
         

  3. Add a C++ source file for the plugin in the same directory. The names of C++ source files must match the Wasm files that the Makefile targets, with the `.wasm` suffix replaced by `.cc`. In this example, the source file must be named `myproject.cc`.

  4. Add your plugin code to the source file.

The following sample source code is a plugin that rewrites the request host, and emits a response header:
         
         #include "proxy_wasm_intrinsics.h"
         
         class MyHttpContext : public Context {
          public:
           explicit MyHttpContext(uint32_t id, RootContext* root) : Context(id, root) {}
         
           FilterHeadersStatus onRequestHeaders(uint32_t headers,
                                                bool end_of_stream) override {
             LOG_INFO("onRequestHeaders: hello from wasm");
         
             // Route Extension example: host rewrite
             if (replaceRequestHeader(":authority", "service-extensions.com") != WasmResult::Ok) {
               LOG_ERROR("Failed to replace :authority header");
             }
             if (replaceRequestHeader(":path", "/") != WasmResult::Ok) {
               LOG_ERROR("Failed to replace :path header");
             }
             return FilterHeadersStatus::Continue;
           }
         
           FilterHeadersStatus onResponseHeaders(uint32_t headers,
                                                 bool end_of_stream) override {
             LOG_INFO("onResponseHeaders: hello from wasm");
         
             // Traffic Extension example: add response header
             if (addResponseHeader("hello", "service-extensions") != WasmResult::Ok) {
               LOG_ERROR("Failed to add response header");
             }
             return FilterHeadersStatus::Continue;
           }
         };
         
         static RegisterContextFactory register_StaticContext(
             CONTEXT_FACTORY(MyHttpContext), ROOT_FACTORY(RootContext));

The `onRequestHeaders` method is a [callback](https://docs.cloud.google.com/service-extensions/docs/prepare-plugin-code#callbacks) that Service Extensions invokes.




### Go

  1. Create a new directory for the plugin:
         
         mkdir go-plugin
         

  2. In the directory, create a `go.mod` file by using the Go tool:
         
         go mod init go-plugin
         

  3. In the same directory, create a source file named `main.go`, and add your plugin code to the file.

The following sample source code is a plugin that rewrites the request host, and emits a response header:
         
         package main
         
         import (
         	"fmt"
         
         	"github.com/proxy-wasm/proxy-wasm-go-sdk/proxywasm"
         	"github.com/proxy-wasm/proxy-wasm-go-sdk/proxywasm/types"
         )
         
         func main() {}
         func init() {
         	proxywasm.SetVMContext(&vmContext{})
         }
         
         type vmContext struct {
         	types.DefaultVMContext
         }
         
         type pluginContext struct {
         	types.DefaultPluginContext
         }
         
         type httpContext struct {
         	types.DefaultHttpContext
         }
         
         func (*vmContext) NewPluginContext(contextID uint32) types.PluginContext {
         	return &pluginContext{}
         }
         
         func (*pluginContext) NewHttpContext(uint32) types.HttpContext {
         	return &httpContext{}
         }
         
         func (ctx *httpContext) OnHttpRequestHeaders(numHeaders int, endOfStream bool) types.Action {
         	defer func() {
         		err := recover()
         		if err != nil {
         			proxywasm.SendHttpResponse(500, [][2]string{}, []byte(fmt.Sprintf("%v", err)), 0)
         		}
         	}()
         	proxywasm.LogInfof("onRequestHeaders: hello from wasm")
         
         	// Route Extension example: host rewrite
         	err := proxywasm.ReplaceHttpRequestHeader(":authority", "service-extensions.com")
         	if err != nil {
         		panic(err)
         	}
         	err = proxywasm.ReplaceHttpRequestHeader(":path", "/")
         	if err != nil {
         		panic(err)
         	}
         	return types.ActionContinue
         }
         
         func (ctx *httpContext) OnHttpResponseHeaders(numHeaders int, endOfStream bool) types.Action {
         	defer func() {
         		err := recover()
         		if err != nil {
         			proxywasm.SendHttpResponse(500, [][2]string{}, []byte(fmt.Sprintf("%v", err)), 0)
         		}
         	}()
         	proxywasm.LogInfof("onResponseHeaders: hello from wasm")
         
         	// Traffic Extension example: add response header
         	err := proxywasm.AddHttpResponseHeader("hello", "service-extensions")
         	if err != nil {
         		panic(err)
         	}
         	return types.ActionContinue
         }
         

The `OnHttpRequestHeaders` method is a [callback](https://docs.cloud.google.com/service-extensions/docs/prepare-plugin-code#callbacks) that Service Extensions invokes.

  4. To download and pin library dependencies, run `go mod tidy`:
         
         go mod tidy
         




### Rust

  1. Create a Rust package directory by using the `cargo new` command from Rust's package manager, [Cargo](https://doc.rust-lang.org/cargo/):
         
         cargo new --lib my-wasm-plugin
         

The command creates a directory that contains a `cargo.toml` file that you can update to describe how to build the Rust package and an `src` directory in which you store the plugin code.

  2. Update the `cargo.toml` file to specify the parameters required to build the package:
         
         [package]
         name = "my-wasm-plugin"
         version = "0.1.0"
         edition = "2021"
         

  3. To register the Proxy-Wasm Rust SDK and logging support as dependencies, add the `dependencies` section. For example:
         
         [dependencies]
         proxy-wasm = "0.2"
         log = "0.4"
         

  4. To build a dynamic library as required for plugins, add the `lib` section. For example:
         
         [lib]
         crate-type = ["cdylib"]
         

  5. To reduce the size of the compiled plugin, add the `profile.release` section. For example:
         
         [profile.release]
         lto = true
         opt-level = 3
         codegen-units = 1
         panic = "abort"
         strip = "debuginfo"
         

  6. Add your plugin code to the `lib.rs` file in the `src` directory.

The following sample source code is a plugin that rewrites the request host, and emits a response header:
         
         use log::info;
         use proxy_wasm::traits::*;
         use proxy_wasm::types::*;
         
         proxy_wasm::main! { {
             proxy_wasm::set_log_level(LogLevel::Trace);
             proxy_wasm::set_http_context(|_, _| -> Box<dyn HttpContext> { Box::new(MyHttpContext) });
         } }
         
         struct MyHttpContext;
         
         impl Context for MyHttpContext {}
         
         impl HttpContext for MyHttpContext {
             fn on_http_request_headers(&mut self, _: usize, _: bool) -> Action {
                 info!("onRequestHeaders: hello from wasm");
         
                 // Route extension example: host rewrite
                 self.set_http_request_header(":authority", Some("service-extensions.com"));
                 self.set_http_request_header(":path", Some("/"));
                 return Action::Continue;
             }
         
             fn on_http_response_headers(&mut self, _: usize, _: bool) -> Action {
                 info!("onResponseHeaders: hello from wasm");
         
                 // Traffic extension example: add response header
                 self.add_http_response_header("hello", "service-extensions");
                 return Action::Continue;
             }
         }

The `on_http_request_headers` method is a [callback](https://docs.cloud.google.com/service-extensions/docs/prepare-plugin-code#callbacks) that Service Extensions invokes.




## Compile the plugin

### C++

To compile the plugin, run the following command from within the directory in which the Makefile and C++ plugin source files are located:
    
    
    docker run -v $PWD:/work -w /work wasmsdk:v3 /build_wasm.sh myproject.wasm
    

This command maps the current directory to the `work` directory within the Docker image, and then runs the `build_wasm.sh` script provided by the Docker image to build the plugin code. When the compile operation completes successfully, a `myproject.wasm` file, which contains the compiled Wasm bytecode, is created in the current directory.

The first time that plugin code is compiled using the Docker image, Emscripten generates the standard libraries. To cache these in the Docker image so that they don't need to be regenerated each time, commit the image with the standard libraries after the first successful compilation:
    
    
    docker commit `docker ps -l | grep wasmsdk:v3 | awk '{print $1}'` wasmsdk:v3
    

For more information about building C++ plugins, see the [Proxy-Wasm C++ SDK documentation](https://github.com/proxy-wasm/proxy-wasm-cpp-sdk/blob/main/docs/building.md).

### Go

To compile the plugin code, run the `go build` command:
    
    
    env GOOS=wasip1 GOARCH=wasm go build -buildmode=c-shared -o main.wasm main.go
    

A successful compilation creates a `main.wasm` file in the current directory.

### Rust

To compile the plugin code, run the `cargo build` command:
    
    
    cargo build --release --target wasm32-wasip1
    

When the build completes successfully, a `Finished release [optimized] target(s)` message appears. If you're familiar with [Envoy](https://www.envoyproxy.io/), you might want to load the plugin in Envoy and verify its behavior.

**Note:** If the build fails with a `linker cc not found` error, install a compiler toolchain. On Debian systems, this can be accomplished by installing the `build-essential` package.

## Upload the compiled plugin code to Artifact Registry

Upload the compiled plugin code to an [Artifact Registry repository](https://docs.cloud.google.com/artifact-registry/docs/overview) so that Google Cloud services can access it.

If you are using Service Extensions with a global load balancer, use a repository in a multi-regional `us` [location](https://docs.cloud.google.com/artifact-registry/docs/repositories/repo-locations). If you are using a regional load balancer, use a repository in the same region or in a multi-regional location on the same continent.

When you attach a plugin to a global load-balancer, Service Extensions copies the Wasm module from the Artifact Registry repository to its own storage in locations across the world. So, the location for the repository doesn't affect the latency of the requests sent to the load balancer. For regional load-balancers, the plugin gets copied to locations in the same region where the load balancer is located.

Service Extensions plugins can be uploaded to Artifact Registry generic or Docker repositories.

For a more direct approach to managing standalone binaries, we recommend that you use a generic repository to store your Wasm files. This option is in [Preview](https://cloud.google.com/products#product-launch-stages).

###  Generic repository 

  1. Create a local `package/` directory and copy your publishable plugin module into it. The plugin artifact must be named `plugin.wasm` The following sample command copies the plugin artifact built by Rust:
         
         mkdir -p package && cp -f target/wasm32-wasip1/release/my_wasm_plugin.wasm package/plugin.wasm
         

  2. [Create an Artifact Registry repository](https://docs.cloud.google.com/artifact-registry/docs/repositories/create-repos) with `--repository-format` set to `generic`.

  3. Verify that you have the required [permissions](https://docs.cloud.google.com/artifact-registry/docs/access-control) for the repository.

  4. To upload your Wasm module as a generic artifact to your repository, use the [`gcloud artifacts generic upload` command](https://docs.cloud.google.com/sdk/gcloud/reference/artifacts/generic/upload).
         
         gcloud artifacts generic upload \
             --project=PROJECT_ID \
             --location=LOCATION \
             --repository=REPOSITORY \
             --source=package/plugin.wasm \
             --package=PACKAGE \
             --version=VERSION
         

Replace the following:

     * `PROJECT_ID`: your Google Cloud [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects)
     * `LOCATION`: the regional or multi-regional [location of the repository](https://docs.cloud.google.com/artifact-registry/docs/repo-locations)
     * `REPOSITORY`: the name of the repository to which you want to upload the Wasm module
     * `PACKAGE`: the package name of the file
     * `VERSION`: the version of the Wasm module

When the upload completes, note the name of the generic artifact as mentioned with the `name` label, for example `add_header_plugin:v4` in the following sample. Specify this name when you [create a plugin](https://docs.cloud.google.com/service-extensions/docs/create-plugin) or plugin version.
    
    Uploading file: plugin.wasm...done.
    '@type': type.googleapis.com/google.devtools.artifactregistry.v1.GenericArtifact
    createTime: '2025-06-16T11:02:25.080248Z'
    name: projects/my-project/locations/us/repositories/my-generic-repo/genericArtifacts/add_header_plugin:v4
    updateTime: '2025-06-16T11:02:25.080248Z'
    version: v4
    

  5. To confirm that the artifact was successfully uploaded to Artifact Registry, run the [`gcloud artifacts files list` command](https://docs.cloud.google.com/sdk/gcloud/reference/artifacts/files/list) and verify that the list has a file named `PACKAGE:VERSION:plugin.wasm`.
         
         gcloud artifacts files list \
              --project=PROJECT_ID \
              --location=LOCATION \
              --repository=REPOSITORY
         




###  Docker repository 

  1. [Create an Artifact Registry repository](https://docs.cloud.google.com/artifact-registry/docs/repositories/create-repos) with `--repository-format` set to `docker`.

  2. Verify that you have the required [permissions](https://docs.cloud.google.com/artifact-registry/docs/access-control) for the repository.

  3. Create a local `package/` directory and copy your publishable plugin artifact into it. The following sample copies the plugin artifact built by Rust:
         
         mkdir -p package && cp -f target/wasm32-wasip1/release/my_wasm_plugin.wasm package/plugin.wasm
         

  4. Create a `package/Dockerfile` file with the following contents:
         
         FROM scratch
         COPY plugin.wasm plugin.wasm
         

  5. Package the plugin code by using either Cloud Build or Docker.

###  Cloud Build 

     1. Create a `package/cloudbuild.yaml` [build config](https://docs.cloud.google.com/build/docs/building/build-containers#use-buildconfig) file with the following contents:
            
            steps:
              - name: 'gcr.io/cloud-builders/docker'
                args: [ 'build', '--no-cache', '--platform', 'wasm',
                      '-t', 'LOCATION-docker.pkg.dev/PROJECT_ID/REPOSITORY/IMAGE:IMAGE_TAG', '.' ]
            images: [ 'LOCATION-docker.pkg.dev/PROJECT_ID/REPOSITORY/IMAGE:IMAGE_TAG' ]
            

The path at which you store the plugin must be in the following format:
            
            LOCATION-docker.pkg.dev/PROJECT_ID/REPOSITORY/IMAGE:IMAGE_TAG
            

Replace the following:

        * `LOCATION`: the regional or multi-regional [location](https://docs.cloud.google.com/artifact-registry/docs/repo-locations) of the repository
        * `PROJECT_ID`: your Google Cloud console [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects)
        * `REPOSITORY`: the name of the repository where you intend to store the image
        * `IMAGE`: the name of the container image in the repository—for example, `us-docker.pkg.dev/my-project/my-repo/my-wasm-plugin`
        * `IMAGE_TAG`: the [image tag](https://docs.cloud.google.com/artifact-registry/docs/container-concepts#tags) to assign to the container—for example, `production`
     2. Trigger the operation to build the plugin container and upload it to Artifact Registry:
            
            gcloud builds submit --config package/cloudbuild.yaml package/
            

### Docker

     1. [Install Docker](https://docs.docker.com/install/linux/docker-ce/ubuntu/) if it's not already installed. Docker is included in [Cloud Shell](https://docs.cloud.google.com/shell/docs), the Google Cloud interactive shell environment.

     2. [Configure Docker to authenticate to Artifact Registry](https://docs.cloud.google.com/artifact-registry/docs/docker/authentication). For example:
            
            gcloud auth login
            gcloud auth configure-docker LOCATION-docker.pkg.dev
            gcloud auth print-access-token | docker login -u oauth2accesstoken --password-stdin https://LOCATION-docker.pkg.dev
            

     3. Build the container image:
            
            docker build --no-cache --platform wasm -t my-wasm-plugin package/
            

     4. To tag the local image with the repository image name, use [image tags](https://docs.cloud.google.com/artifact-registry/docs/docker/names#versions):
            
            docker tag my-wasm-plugin LOCATION-docker.pkg.dev/PROJECT_ID/REPOSITORY/IMAGE:IMAGE_TAG
            

Replace the following:

        * `LOCATION`: the regional or multi-regional [location](https://docs.cloud.google.com/artifact-registry/docs/repo-locations) of the repository
        * `PROJECT_ID`: your Google Cloud console [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects)
        * `REPOSITORY`: the name of the repository where you intend to store the image
        * `IMAGE`: the name of the container image in the repository—for example, `us-docker.pkg.dev/my-project/my-repo/my-wasm-plugin`.
        * `IMAGE_TAG`: the image tag to assign to the container—for example, `production`
     5. Upload your tagged container image to Artifact Registry.
            
            docker push LOCATION-docker.pkg.dev/PROJECT_ID/REPOSITORY/IMAGE:IMAGE_TAG
            

  6. To confirm that the image was successfully uploaded to Artifact Registry, run the [`gcloud artifacts docker images list` command](https://docs.cloud.google.com/sdk/gcloud/reference/artifacts/docker/images/list).
         
         gcloud artifacts docker images list LOCATION-docker.pkg.dev/PROJECT_ID/REPOSITORY/IMAGE \
             --include-tags
         




## Prepare and upload the configuration file

Plugins might optionally receive configuration data, which can affect plugin behavior at runtime. Configuration data can be text or binary and in any format accepted by the plugin. If the size of the configuration data is large, you might need to upload the configuration file to Artifact Registry.

### Write plugin code to read configuration data

### C++

Configuration data is passed to the `onConfigure` method of the root context object, which is instantiated once at plugin startup, and remains active for the lifetime of the Wasm runtime that hosts the plugin. The root context object is an instance of the `RootContext` class or of a subclass of `RootContext`.

Plugin code can control what class is used for the root context through the `RegisterContextFactory` value. For example, the following plugin code registers `MyRootContext` and `MyHttpContext` as the classes to use for root and stream context instances. It then reads a secret value from plugin configuration data, which stream context instances can access through the root context object.
    
    
    #include <string>
    #include <string_view>
    
    #include "proxy_wasm_intrinsics.h"
    
    class MyRootContext : public RootContext {
     public:
      explicit MyRootContext(uint32_t id, std::string_view root_id)
          : RootContext(id, root_id) {}
    
      bool onConfigure(size_t config_len) override {
        auto buffer = getBufferBytes(WasmBufferType::PluginConfiguration, 0, config_len);
        if (!buffer) {
          LOG_ERROR("Failed to retrieve plugin configuration");
          return false;
        }
        secret_ = buffer->toString();
        return true;
      }
    
      const std::string& secret() const { return secret_; }
    
     private:
      std::string secret_;
    };
    
    class MyHttpContext : public Context {
     public:
      explicit MyHttpContext(uint32_t id, RootContext* root)
          : Context(id, root),
            secret_(static_cast<MyRootContext*>(root)->secret()) {}
    
      FilterHeadersStatus onRequestHeaders(uint32_t headers,
                                           bool end_of_stream) override {
        // Use secret here...
        LOG_INFO("secret: " + secret_);
        return FilterHeadersStatus::Continue;
      }
    
     private:
      const std::string& secret_;
    };
    
    static RegisterContextFactory register_MyHttpContext(
        CONTEXT_FACTORY(MyHttpContext), ROOT_FACTORY(MyRootContext));

### Go

Configuration data is read while running `OnPluginStart`, a method receiver that the runtime executes on the `PluginContext` struct once at plugin startup. The configuration data doesn't change during the lifetime of the Wasm runtime that hosts the plugin. `PluginContext` is useful for performing initialization logic and maintaining state across many requests.

Plugin code can control what context is used for `PluginContext` by implementing the `NewPluginContext` method on `VMContext`, which instantiates `PluginContext`. `PluginContext` then instantiates `HttpContext` contexts.

For example, the following plugin code registers `VMContext`, which instantiates `PluginContext`, the context that's responsible for reading configuration data and instantiating `HttpContext` contexts as required. `PluginContext` reads a secret value from plugin configuration data, stores it inside the `PluginContext` context, and passes it to `HttpContext` in `NewHttpContext`.
    
    
    package main
    
    import (
    	"fmt"
    
    	"github.com/proxy-wasm/proxy-wasm-go-sdk/proxywasm"
    	"github.com/proxy-wasm/proxy-wasm-go-sdk/proxywasm/types"
    )
    
    func main() {}
    func init() {
    	proxywasm.SetVMContext(&vmContext{})
    }
    
    type vmContext struct {
    	types.DefaultVMContext
    }
    
    type pluginContext struct {
    	types.DefaultPluginContext
    	secret string
    }
    
    type httpContext struct {
    	types.DefaultHttpContext
    	pluginContext *pluginContext
    }
    
    func (*vmContext) NewPluginContext(contextID uint32) types.PluginContext {
    	return &pluginContext{}
    }
    
    func (ctx *pluginContext) OnPluginStart(int) types.OnPluginStartStatus {
    	config, err := proxywasm.GetPluginConfiguration()
    	if err != nil {
    		proxywasm.LogErrorf("Error reading the configuration: %v", err)
    		return types.OnPluginStartStatusFailed
    	}
    	if config == nil {
    		proxywasm.LogError("Configuration is nil")
    		return types.OnPluginStartStatusFailed
    	}
    	ctx.secret = string(config)
    	return types.OnPluginStartStatusOK
    }
    
    func (ctx *pluginContext) NewHttpContext(uint32) types.HttpContext {
    	return &httpContext{pluginContext: ctx}
    }
    
    func (ctx *pluginContext) Secret() string {
    	return ctx.secret
    }
    
    func (ctx *httpContext) OnHttpRequestHeaders(numHeaders int, endOfStream bool) types.Action {
    	defer func() {
    		err := recover()
    		if err != nil {
    			proxywasm.SendHttpResponse(500, [][2]string{}, []byte(fmt.Sprintf("%v", err)), 0)
    		}
    	}()
    	// Use secret here...
    	proxywasm.LogInfof("secret: %v", ctx.pluginContext.Secret())
    	return types.ActionContinue
    }
    

### Rust

Configuration data is read in from a `RootContext` trait, which is instantiated once at plugin startup, and remains active for the lifetime of the Wasm runtime that hosts the plugin. `RootContext` traits are useful for performing operations or maintaining state across many requests.

Plugin code can control what class is used for the root context through the `set_root_context` method, and the root context instantiates stream contexts. For example, the following plugin code registers `MyRootContext`, which instantiates `MyHttpContext` as required. The root context reads a secret value from plugin configuration data, and passes it to stream contexts.
    
    
    use log::info;
    use proxy_wasm::traits::*;
    use proxy_wasm::types::*;
    use std::rc::Rc;
    
    proxy_wasm::main! { {
        proxy_wasm::set_log_level(LogLevel::Trace);
        proxy_wasm::set_root_context(|_| -> Box<dyn RootContext> {
            Box::new(MyRootContext { secret: Rc::new("missing".to_string()) })
        });
    } }
    
    struct MyRootContext {
        secret: Rc<String>,
    }
    
    impl Context for MyRootContext {}
    
    impl RootContext for MyRootContext {
        fn on_configure(&mut self, _: usize) -> bool {
            if let Some(config_bytes) = self.get_plugin_configuration() {
                self.secret = Rc::new(String::from_utf8(config_bytes).unwrap())
            }
            true
        }
    
        fn create_http_context(&self, _: u32) -> Option<Box<dyn HttpContext>> {
            Some(Box::new(MyHttpContext {
                secret: self.secret.clone(), // shallow copy, ref count only
            }))
        }
    
        fn get_type(&self) -> Option<ContextType> {
            Some(ContextType::HttpContext)
        }
    }
    
    struct MyHttpContext {
        secret: Rc<String>,
    }
    
    impl Context for MyHttpContext {}
    
    impl HttpContext for MyHttpContext {
        fn on_http_request_headers(&mut self, _: usize, _: bool) -> Action {
            // Use secret here...
            info!("secret: {}", self.secret);
            Action::Continue
        }
    }

### Upload the configuration file

If the size of the data to be delivered to your plugin in `on_configure` exceeds 900 KiB, upload it to Artifact Registry by following the method described in Upload the compiled plugin code to Artifact Registry. In this case, save the configuration file by the name `plugin.config` (and not `plugin.wasm`).

The next step is to [create a plugin](https://docs.cloud.google.com/service-extensions/docs/create-plugin).

While creating the plugin, you need to provide the URI to the uploaded Wasm module or image.

**Note:** If the size of the configuration data is less than 900 KiB, while creating the plugin, you can upload this data from a file in a local folder. Alternatively, if you're using the [`gcloud service-extensions wasm-plugins create` command](https://docs.cloud.google.com/service-extensions/docs/create-plugin#gcloud), you can use the `plugin-config` flag to embed the data as text in the command.

## Create a new version of plugin code

To create a new version of the plugin code, edit the plugin file. Then, as described in the preceding sections, compile the plugin code, repackage it, and upload it to Artifact Registry.

## Callbacks

The code that you compile into Wasm can define arbitrary methods or functions, but some of them have a special significance. These are the methods that are defined in the Proxy-Wasm SDK for the language of your choice and map to the Proxy-Wasm Application Binary Interface (ABI) specifications. Service Extensions invokes these callbacks in response to user requests or in response to plugin lifecycle events.

These callbacks are listed in the following table in the order in which they're typically invoked:

**Callback name and description** | **C++ method name** | **Go method name** | **Rust method name**  
---|---|---|---  
`START_PLUGIN`: Invoked when a plugin is started. | `RootContext::onStart` | `VMContext.OnVmStart` | `RootContext::on_vm_start`  
`CONFIGURE_PLUGIN`: Invoked after a plugin is started, to provide configuration data to the plugin. | `RootContext::onConfigure` | `PluginContext.OnPluginStart` | `RootContext::on_configure`  
`CREATE_CONTEXT`: Invoked when a new stream context is created. Each stream corresponds to a client HTTP request. | `Context::onCreate` | `PluginContext.NewHttpContext` | `RootContext::``create_http_context`  
`HTTP_REQUEST_HEADERS`: Invoked to process HTTP request headers. | `Context::onRequestHeaders` | `HttpContext.OnHttpRequestHeaders` | `HttpContext::``on_http_request_headers`  
`HTTP_REQUEST_BODY`: Invoked repeatedly to process HTTP request body chunks. | `Context::onRequestBody` | `HttpContext.OnHttpRequestBody` | `HttpContext::``on_http_request_body`  
`HTTP_RESPONSE_HEADERS`: Invoked to process HTTP response headers. | `Context::onResponseHeaders` | `HttpContext.OnHttpResponseHeaders` | `HttpContext::``on_http_response_headers`  
`HTTP_RESPONSE_BODY`: Invoked repeatedly to process HTTP response body chunks. | `Context::onResponseBody` | `HttpContext.OnHttpResponseBody` | `HttpContext::``on_http_response_body`  
`DONE`: Invoked when the processing of a plugin has completed. | `Context::onDone` | `HttpContext.OnHttpStreamDone` | `Context::on_done`  
`DELETE`: Invoked when the stream context object corresponding to a client HTTP request is deleted. | `Context::onDelete` | (no callback) | (no callback)  
  
## What's next

  * [Create a plugin](https://docs.cloud.google.com/service-extensions/docs/create-plugin)
  * See the [Service Extensions overview](https://docs.cloud.google.com/service-extensions/docs/overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
