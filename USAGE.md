# API usage

## :heavy_exclamation_mark: Request failure
> ## Note
> When a request has failed the response will be formatted as below, 
> with the `statusCode` key value being `FAILURE` and the `statusMessage` 
> key showing the reason for the failure. `FAILURE` does not mean the 
> request was not received, but the request received could not be
> completed. These failure messages can be shown in the front-end or
> be interpreted by the developer as to how to handle the failure and
> an alternative user-friendly message can be displayed.
>  
>> Examples of failure could be:
>> * Incorrectly formatted request JSON
>> * Unauthenticated credentials
>> * Attempted access to unauthorized routes
>> * Incorrectly formatted data (email address, password length, etc.)

### Request failure response
```json
{
    "status": {
        "statusCode": "FAILURE",
        "statusMessage" : "<The reason for the failure>"
    }
}
```

- - - -

## _[POST]_ `/sign-up` 
### Request
```json
{
    "emailAddress": <email address>,
    "password": <plain text password>,
    "name": <name>
} 
```
### Response
```json
{
    "status": {
        "statusCode": "SUCCESS",
        "statusMessage": "Successfully registered"
    },
    "name": <name>,
    "emailAddress": <email address>
}
```

- - - - -

## _[POST]_ `/sign-in`
### Request
```json
{
    "emailddress": <email address>,
    "password": <plain text password>
} 
```
### Reponse
```json
{
    "status": {
        "statusCode": "SUCCESS",
        "statusMessage": "Successfully signed in"
    },
    "name": <customer name>,
    "emailAddress": <email address>,
    "currentSignInDatetime": <current sign in time>,
    "previousSignInDatetime": <last sign in time>,
}
```

- - - - -

## _[POST]_ `/sign-out`
> The request uses the token present in the authorization header 
> to end the session. No request JSON is required.

- - - - - 

## _[GET]_ `/list/all`
### Response
```json
{
    "status": {
        "statusCode": "SUCCESS",
        "statusMessage": "List of all available cryptocurrencies and bundles"
    },
    "availableCryptocurrencies": [
        {
            "cryptocurrencyCode": <code>,
            "cryptocurrencyName": <name>
        }
    ],
    "availableBundles": [
        {
            "bundleName": <bundle name>,
            "minimumHoldingPeriod": <in monthes>,
            "bundleCryptocurrencies": [
                {
                    "cryptocurrencyCode": <code>,
                    "cryptocurrencyName": <name>,
                    "percentage": <% of the bundle>
                }
            ]
        }
    ]
} 
```
> Where
> * `availableCryptocurrencies` is a list of cryptocurrencies
> * `availableBundles` is a list of bundles

- - - - -

## _[GET]_ `/list/all/cryptocurrencies`
### Response
```json
{
    "status": {
        "statusCode": "SUCCESS",
        "statusMessage": "List of all available cryptocurrencies"
    },
    "availableCryptocurrencies": [
        {
            "cryptocurrencyCode": <code>,
            "cryptocurrencyName": <name>
        }
    ]
}
```
> Where
> * `availableCryptocurrencies` is a list of cryptocurrencies

- - - - -

## _[GET]_ `list/all/bundles`
### Response
```json
{
    "status": {
        "statusCode": "SUCCESS/FAILURE",
        "statusMessage": "show he message to the user in case of FAILURE"
    },
    "availableBundles": [
        {
            "bundleName": "Low Risk",
            "bundleCryptocurrencies": [
                {
                    "cryptocurrencyCode": "code",
                    "cryptocurrencyName": "name",
                    "percentage": 30
                }
            ],
            "minimumHoldingPeriod": 5
        }
    ]
}
```
> Where
> * `availableBundles` is a list of bundles
 
- - - - -



