---
url: https://docs.cloud.google.com/rust/docs/mocking/
title: Write tests using a mock client \u00a0|\u00a0 Rust \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T00:15:19.674720+00:00
---

# Write tests using a mock client  |  Rust  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/rust/docs/mocking/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Rust ](https://docs.cloud.google.com/rust/docs)
  * [ Guides ](https://docs.cloud.google.com/rust/docs/overview)



Send feedback 

#  Write tests using a mock client Stay organized with collections  Save and categorize content based on your preferences. 

Learn how to stub real client implementations to inject a mock for unit testing. Using a mock client with the Google Cloud Client Libraries for Rust lets you write controlled, reliable unit tests that don't make network calls or incur billing charges.

## Dependencies

There are several mocking frameworks available for Rust. This guide uses [`mockall`](https://docs.rs/mockall/latest/mockall/). Add it as a development dependency:
    
    
    cargo add --dev mockall
    

Additionally, this guide uses the [`Speech`](https://docs.rs/google-cloud-speech-v2/latest/google_cloud_speech_v2/client/struct.Speech.html) client to make examples easier to follow (but these concepts apply to all clients).

Add the required dependencies to your `Cargo.toml` file:
    
    
    cargo add google-cloud-speech-v2 google-cloud-lro
    

## Mock a client

To test your code with a mock client, you define a mock struct, configure its expected behavior for your test scenario, and then inject that mock into your application logic. The following example demonstrates this workflow.

First, add `use` statements to simplify the code:
    
    
    use google_cloud_gax as gax;
    use google_cloud_speech_v2 as speech;

Assume the application has a function that uses the `Speech` client to call `GetRecognizer`, setting the `name` field of the request, and process the server response.
    
    
    // An example application function.
    //
    // It makes an RPC, setting some field. In this case, it is the `GetRecognizer`
    // RPC, setting the name field.
    //
    // It processes the response from the server. In this case, it extracts the
    // display name of the recognizer.
    async fn my_application_function(client: &speech::client::Speech) -> gax::Result<String> {
        client
            .get_recognizer()
            .set_name("invalid-test-recognizer")
            .send()
            .await
            .map(|r| r.display_name)
    }

You can test how the application handles different responses from the service.

Next, define the mock struct. This struct implements the [`speech::stub::Speech`](https://docs.rs/google-cloud-speech-v2/latest/google_cloud_speech_v2/stub/trait.Speech.html) trait.
    
    
    mockall::mock! {
        #[derive(Debug)]
        Speech {}
        impl speech::stub::Speech for Speech {
            async fn get_recognizer(&self, req: speech::model::GetRecognizerRequest, _options: gax::options::RequestOptions) -> gax::Result<gax::response::Response<speech::model::Recognizer>>;
        }
    }

Create an instance of the mock. Note that the [`mockall::mock!`](https://docs.rs/mockall/latest/mockall/macro.mock.html) macro prepends a `Mock` prefix to the name of the previously defined struct.
    
    
    let mut mock = MockSpeech::new();

Set expectations on the mock. For example, expect the code to call `GetRecognizer` with a particular name and simulate a successful response from the service.
    
    
    mock.expect_get_recognizer()
        .withf(move |r, _|
            // Optionally, verify fields in the request.
            r.name == "invalid-test-recognizer")
        .return_once(|_, _| {
            Ok(gax::response::Response::from(
                speech::model::Recognizer::new().set_display_name("test-display-name"),
            ))
        });

Create a `Speech` client using the mock:
    
    
    let client = speech::client::Speech::from_stub(mock);

Call the function:
    
    
    let display_name = my_application_function(&client).await?;

Verify the results:
    
    
    assert_eq!(display_name, "test-display-name");

### Simulate errors

Simulating errors is similar to simulating successes. To simulate an error, modify the result returned by the mock.
    
    
    mock.expect_get_recognizer().return_once(|_, _| {
        // This time, return an error.
        use gax::error::Error;
        use gax::error::rpc::{Code, Status};
        let status = Status::default()
            .set_code(Code::NotFound)
            .set_message("Resource not found");
        Err(Error::service(status))
    });

A client built with `from_stub()` does not have an internal retry loop; it returns all errors from the stub directly to the application.

## Next steps

To view the complete code from this guide, see the [source file](https://github.com/googleapis/google-cloud-rust/blob/main/guide/samples/tests/mocking.rs) in the `google-cloud-rust` repository on GitHub.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
