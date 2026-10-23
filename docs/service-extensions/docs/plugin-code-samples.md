---
url: https://docs.cloud.google.com/service-extensions/docs/plugin-code-samples/
title: Code samples for plugins \u00a0|\u00a0 Service Extensions \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:34:24.389109+00:00
---

# Code samples for plugins  |  Service Extensions  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-extensions/docs/plugin-code-samples/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Service Extensions ](https://docs.cloud.google.com/service-extensions/docs)
  * [ Guides ](https://docs.cloud.google.com/service-extensions/docs/overview)



Send feedback 

#  Code samples for plugins Stay organized with collections  Save and categorize content based on your preferences. 

This page provides code samples that address some common use cases for plugins.

For more Rust, Go, and C++ plugin samples, see the [Service Extensions GitHub repository for plugins](https://github.com/GoogleCloudPlatform/service-extensions/tree/main/plugins#docs).

The plugins feature is in [Preview](https://cloud.google.com/products#product-launch-stages) for Media CDN.

## Add HTTP request and response headers

The following code samples show how to add HTTP request headers.

### C++
    
    
    #include "proxy_wasm_intrinsics.h"
    
    class MyHttpContext : public Context {
     public:
      explicit MyHttpContext(uint32_t id, RootContext* root) : Context(id, root) {}
    
      FilterHeadersStatus onRequestHeaders(uint32_t headers,
                                           bool end_of_stream) override {
        // Always be a friendly proxy.
        addRequestHeader("Message", "hello");
        replaceRequestHeader("Welcome", "warm");
        return FilterHeadersStatus::Continue;
      }
    };
    
    static RegisterContextFactory register_StaticContext(
        CONTEXT_FACTORY(MyHttpContext), ROOT_FACTORY(RootContext));

### Go
    
    
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
    
    func (vc *vmContext) NewPluginContext(contextID uint32) types.PluginContext {
    	return &pluginContext{}
    }
    
    func (pc *pluginContext) NewHttpContext(contextID uint32) types.HttpContext {
    	return &httpContext{}
    }
    
    func (ctx *httpContext) OnHttpRequestHeaders(numHeaders int, endOfStream bool) types.Action {
    	defer func() {
    		if err := recover(); err != nil {
    			proxywasm.SendHttpResponse(500, [][2]string{}, []byte(fmt.Sprintf("%v", err)), 0)
    		}
    	}()
    
    	// Add and replace headers.
    	if err := proxywasm.AddHttpRequestHeader("Message", "hello"); err != nil {
    		panic(err)
    	}
    	if err := proxywasm.ReplaceHttpRequestHeader("Welcome", "warm"); err != nil {
    		panic(err)
    	}
    
    	return types.ActionContinue
    }
    

### Rust
    
    
    use proxy_wasm::traits::*;
    use proxy_wasm::types::*;
    
    proxy_wasm::main! {{
        proxy_wasm::set_log_level(LogLevel::Trace);
        proxy_wasm::set_http_context(|_, _| -> Box<dyn HttpContext> { Box::new(MyHttpContext) });
    }}
    
    struct MyHttpContext;
    
    impl Context for MyHttpContext {}
    
    impl HttpContext for MyHttpContext {
        fn on_http_request_headers(&mut self, _: usize, _: bool) -> Action {
            // Always be a friendly proxy.
            self.add_http_request_header("Message", "hello");
            self.set_http_request_header("Welcome", Some("warm"));
            return Action::Continue;
        }
    }

The following code samples show how to add HTTP response headers.

### C++
    
    
    #include "proxy_wasm_intrinsics.h"
    
    class MyHttpContext : public Context {
     public:
      explicit MyHttpContext(uint32_t id, RootContext* root) : Context(id, root) {}
    
      FilterHeadersStatus onResponseHeaders(uint32_t headers,
                                            bool end_of_stream) override {
        // Conditionally add to a header value.
        auto msg = getResponseHeader("Message");
        if (msg && msg->view() == "foo") {
          addResponseHeader("Message", "bar");
        }
        // Unconditionally remove a header.
        removeResponseHeader("Welcome");
        return FilterHeadersStatus::Continue;
      }
    };
    
    static RegisterContextFactory register_StaticContext(
        CONTEXT_FACTORY(MyHttpContext), ROOT_FACTORY(RootContext));

### Go
    
    
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
    
    func (vc *vmContext) NewPluginContext(contextID uint32) types.PluginContext {
    	return &pluginContext{}
    }
    
    func (pc *pluginContext) NewHttpContext(contextID uint32) types.HttpContext {
    	return &httpContext{}
    }
    
    func (ctx *httpContext) OnHttpResponseHeaders(numHeaders int, endOfStream bool) types.Action {
    	defer func() {
    		if err := recover(); err != nil {
    			proxywasm.SendHttpResponse(500, [][2]string{}, []byte(fmt.Sprintf("%v", err)), 0)
    		}
    	}()
    
    	// Conditionally add to a header value.
    	msgValue, err := proxywasm.GetHttpResponseHeader("Message")
    	if err != nil {
    		proxywasm.LogCriticalf("failed to get 'Message' header: %v", err)
    	} else if msgValue == "foo" {
    		if err := proxywasm.AddHttpResponseHeader("Message", "bar"); err != nil {
    			panic(err)
    		}
    	}
    
    	// Unconditionally remove the "Welcome" header.
    	if err := proxywasm.RemoveHttpResponseHeader("Welcome"); err != nil {
    		panic(err)
    	}
    
    	return types.ActionContinue
    }
    

### Rust
    
    
    use proxy_wasm::traits::*;
    use proxy_wasm::types::*;
    
    proxy_wasm::main! {{
        proxy_wasm::set_log_level(LogLevel::Trace);
        proxy_wasm::set_http_context(|_, _| -> Box<dyn HttpContext> { Box::new(MyHttpContext) });
    }}
    
    struct MyHttpContext;
    
    impl Context for MyHttpContext {}
    
    impl HttpContext for MyHttpContext {
    
        fn on_http_response_headers(&mut self, _: usize, _: bool) -> Action {
            // Conditionally add to a header value.
            let msg = self.get_http_response_header("Message");
            if msg.unwrap_or_default() == "foo" {
                self.add_http_response_header("Message", "bar");
            }
            // Unconditionally remove a header.
            self.set_http_response_header("Welcome", None);
            return Action::Continue;
        }
    }

## Rewrite the request URL

The following code samples show how to rewrite the request URL by using regular expressions. The following code samples remove part of the path, but any URI mutation, such as path, query, or fragment, is feasible.

These samples also show best practices around regular expressions, namely using linear-time regular expression libraries and compiling the expressions at plugin initialization time.

### C++
    
    
    #include "proxy_wasm_intrinsics.h"
    #include "re2/re2.h"
    
    class MyRootContext : public RootContext {
     public:
      explicit MyRootContext(uint32_t id, std::string_view root_id)
          : RootContext(id, root_id) {}
    
      bool onConfigure(size_t) override {
        // Compile the regex expression at plugin setup time.
        path_match.emplace("/foo-([^/]+)/");
        return path_match->ok();
      }
    
      std::optional<re2::RE2> path_match;
    };
    
    class MyHttpContext : public Context {
     public:
      explicit MyHttpContext(uint32_t id, RootContext* root)
          : Context(id, root), root_(static_cast<MyRootContext*>(root)) {}
    
      FilterHeadersStatus onRequestHeaders(uint32_t headers,
                                           bool end_of_stream) override {
        const auto path = getRequestHeader(":path");
        if (!path) {
          LOG_ERROR("Failed to get :path header");
          return FilterHeadersStatus::Continue;
        }
    
        std::string edit = path->toString();  // mutable copy
        if (re2::RE2::Replace(&edit, *root_->path_match, "/\\1/")) {
          if (replaceRequestHeader(":path", edit) != WasmResult::Ok) {
            LOG_ERROR("Failed to replace :path header");
          }
        }
    
        return FilterHeadersStatus::Continue;
      }
    
     private:
      const MyRootContext* root_;
    };
    
    static RegisterContextFactory register_StaticContext(
        CONTEXT_FACTORY(MyHttpContext), ROOT_FACTORY(MyRootContext));

### Go
    
    
    package main
    
    import (
    	"fmt"
    	"regexp"
    
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
    	pathMatch *regexp.Regexp
    }
    
    type httpContext struct {
    	types.DefaultHttpContext
    	pluginContext *pluginContext
    }
    
    func (*vmContext) NewPluginContext(contextID uint32) types.PluginContext {
    	return &pluginContext{}
    }
    
    func (ctx *pluginContext) OnPluginStart(int) types.OnPluginStartStatus {
    	var err error
    	// Compile the regex expression at plugin setup time.
    	ctx.pathMatch, err = regexp.Compile("/foo-([^/]+)/")
    	if err != nil {
    		proxywasm.LogErrorf("Error compiling the path regular expression: %v", err)
    		return types.OnPluginStartStatusFailed
    	}
    	return types.OnPluginStartStatusOK
    }
    
    func (ctx *pluginContext) NewHttpContext(uint32) types.HttpContext {
    	return &httpContext{pluginContext: ctx}
    }
    
    func (ctx *httpContext) OnHttpRequestHeaders(numHeaders int, endOfStream bool) types.Action {
    	defer func() {
    		err := recover()
    		if err != nil {
    			proxywasm.SendHttpResponse(500, [][2]string{}, []byte(fmt.Sprintf("%v", err)), 0)
    		}
    	}()
    	path, err := proxywasm.GetHttpRequestHeader(":path")
    	if err != types.ErrorStatusNotFound {
    		if err != nil {
    			panic(err)
    		}
    		edit := ctx.pluginContext.pathMatch.ReplaceAllString(path, "/$1/")
    		if len(edit) != len(path) {
    			err = proxywasm.ReplaceHttpRequestHeader(":path", edit)
    			if err != nil {
    				panic(err)
    			}
    		}
    	}
    	return types.ActionContinue
    }
    

### Rust
    
    
    use proxy_wasm::traits::*;
    use proxy_wasm::types::*;
    use regex::Regex;
    use std::rc::Rc;
    
    proxy_wasm::main! {{
        proxy_wasm::set_log_level(LogLevel::Trace);
        proxy_wasm::set_root_context(|_| -> Box<dyn RootContext> {
            Box::new(MyRootContext { path_match: None })
        });
    }}
    
    struct MyRootContext {
        path_match: Option<Rc<Regex>>,
    }
    
    impl Context for MyRootContext {}
    
    impl RootContext for MyRootContext {
        fn on_configure(&mut self, _: usize) -> bool {
            self.path_match = Some(Rc::new(Regex::new(r"/foo-([^/]+)/").unwrap()));
            return true;
        }
    
        fn create_http_context(&self, _: u32) -> Option<Box<dyn HttpContext>> {
            Some(Box::new(MyHttpContext {
                path_match: self.path_match.as_ref().unwrap().clone(), // shallow copy, ref count only
            }))
        }
        fn get_type(&self) -> Option<ContextType> {
            Some(ContextType::HttpContext)
        }
    }
    
    struct MyHttpContext {
        path_match: Rc<Regex>,
    }
    
    impl Context for MyHttpContext {}
    
    impl HttpContext for MyHttpContext {
        fn on_http_request_headers(&mut self, _: usize, _: bool) -> Action {
            if let Some(path) = self.get_http_request_header(":path") {
                let edit = self.path_match.replace(&path, "/$1/");
                if path.len() != edit.len() {
                    self.set_http_request_header(":path", Some(&edit));
                }
            }
            return Action::Continue;
        }
    }

## Enable logging for custom variables

The following code samples show how to perform a basic check on the request query string parameters and emit parsed information to Cloud Logging. These samples also show how to parse URLs.

### C++
    
    
    #include <boost/url/parse.hpp>
    #include <boost/url/url.hpp>
    
    #include "proxy_wasm_intrinsics.h"
    
    class MyHttpContext : public Context {
     public:
      explicit MyHttpContext(uint32_t id, RootContext* root) : Context(id, root) {}
    
      FilterHeadersStatus onRequestHeaders(uint32_t headers,
                                           bool end_of_stream) override {
        WasmDataPtr path = getRequestHeader(":path");
        if (path) {
          std::string token = "<missing>";
          boost::system::result<boost::urls::url_view> url =
              boost::urls::parse_uri_reference(path->view());
          if (url) {
            auto it = url->params().find("token");
            if (it != url->params().end()) {
              token = (*it).value;
            }
          }
          LOG_INFO("token: " + token);
        }
        return FilterHeadersStatus::Continue;
      }
    };
    
    static RegisterContextFactory register_StaticContext(
        CONTEXT_FACTORY(MyHttpContext), ROOT_FACTORY(RootContext));

### Go
    
    
    package main
    
    import (
    	"fmt"
    	"net/url"
    
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
    	path, err := proxywasm.GetHttpRequestHeader(":path")
    	if err != types.ErrorStatusNotFound {
    		if err != nil {
    			panic(err)
    		}
    		u, err := url.Parse(path)
    		if err != nil {
    			panic(err)
    		}
    		token := u.Query().Get("token")
    		if token == "" {
    			token = "<missing>"
    		}
    		proxywasm.LogInfof("token: %s", token)
    	}
    
    	return types.ActionContinue
    }
    

### Rust
    
    
    use log::info;
    use proxy_wasm::traits::*;
    use proxy_wasm::types::*;
    use url::Url;
    
    proxy_wasm::main! {{
        proxy_wasm::set_log_level(LogLevel::Trace);  // log everything, subject to plugin LogConfig
        proxy_wasm::set_http_context(|_, _| -> Box<dyn HttpContext> { Box::new(MyHttpContext) });
    }}
    
    struct MyHttpContext;
    
    impl Context for MyHttpContext {}
    
    impl HttpContext for MyHttpContext {
        fn on_http_request_headers(&mut self, _: usize, _: bool) -> Action {
            if let Some(path) = self.get_http_request_header(":path") {
                // Create dummy base/host to allow parsing relative paths.
                let base = Url::parse("http://example.com").ok();
                let options = Url::options().base_url(base.as_ref());
                let token: Option<String> = match options.parse(&path) {
                    Err(_) => None,
                    Ok(url) => url.query_pairs().find_map(|(k, v)| {
                        if k == "token" {
                            Some(v.to_string())
                        } else {
                            None
                        }
                    }),
                };
                info!("token: {}", token.unwrap_or("<missing>".to_string()));
            }
            return Action::Continue;
        }
    }

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
