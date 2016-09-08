// Instantiate the Choreo, using a previously instantiated TembooSession object, eg:
TembooSession session = new TembooSession("ACCOUNT_NAME", "APP_KEY_NAME", "APP_KEY_VALUE");

HelloWorld helloWorldChoreo = new HelloWorld(session);

// Get an InputSet object for the choreo
HelloWorldInputSet helloWorldInputs = helloWorldChoreo.newInputSet();

// Set inputs
helloWorldInputs.set_Value("2374418588");

// Execute Choreo
HelloWorldResultSet helloWorldResults = helloWorldChoreo.execute(helloWorldInputs);
