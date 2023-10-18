$.ajax({
    url: "https://api-staging.namipay.com.sa/client/get_token",
    method: "POST", // Use "method" instead of "type"
    headers: {
        "Accept": "application/json",
    },
    data: {
        "grant_type": "client_credentials",
        "client_id": "merchantapp",
        "client_secret": "r4vKbc17kVdKtC8R5jCvQZkgXyICRnW0",
        "scope": "SCOPE_MERCHANTAPP"
    },
    dataType: "json",
    success: function (response) {
        var token = response.access_token;
        var expiresIn = response.expires_in;

        console.log("Token:", token);
        console.log("Expires in:", expiresIn);
    },
    error: function (xhr, status, error) {
        console.log("Error:", xhr.responseText);
    }
});
