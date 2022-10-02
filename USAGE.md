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
    "currentSignInDatetime": <current sign in datetime>,
    "previousSignInDatetime": <last sign in datetime>,
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
> * `bundleCryptocurrencies` is a list of the cryptocurrencies in that bundle

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
        "statusCode": "SUCCESS",
        "statusMessage": "List of all available bundles"
    },
    "availableBundles": [
        {
            "bundleName": <name of the bundle>,
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
> * `availableBundles` is a list of bundles
> * `bundleCryptocurrencies` is a list of the cryptocurrencies in that bundle
 
- - - - -

## _[GET]_ `/account/customer-details`
### Request
```json
{
    "customerID": <customer ID>
}
```
> The token present in the authorization header is the preferred
> method to confirm access to this route and has priority 
### Response
```json
{
    "status": {
        "statusCode": "SUCCESS",
        "statusMessage": "The customers details"
    },
    "customerID": <Customers ID>,
    "registerDatetime": <datetime of account creation>,
    "emailAddress": <email address>,
    "previousSignInDatetime": <last sign in datetime>,
    "currentSignInDatetime": <current sign in datetime>,
    "name": "name"
}
```

- - - - -

## _[GET]_ `/account/wallets`
### Request
```json
{
    "customerID": "customerID"
}
```
> The token present in the authorization header is the preferred
> method to confirm access to this route and has priority 
### Response
```json
{
    "status": {
        "statusCode": "SUCCESS",
        "statusMessage": "All of the customers wallets"
    },
    "wallets": [
        {
            "walletAddress": <wallet address>,
            "customerID": <customer ID>,
            "initialBalance": <the balance at time of purchase>,
            "currentBalance": <the current balance>,
            "cryptocurrencyCode": <the wallets cryptocurrency>,
            "holdingPeriod": <investment time period>
        }
    ]
}
```
> Where
> * `wallets` is a list of all the customers wallets
 
- - - - -

## _[GET]_ `/account/bundles`
### Request
```json
{
    "customerID": "customerID"
}
```
> The token present in the authorization header is the preferred
> method to confirm access to this route and has priority
### Response
```json
{
    "status": {
        "statusCode": "SUCCESS",
        "statusMessage": "All of the customers bundles"
    },
    "bundles": [
        {
            "bundleAddress": <bundle address>,
            "bundleID": <bundle ID>,
            "customerID": <customer ID>,
            "amount": <amount invested>,
            "holdingPeriod": <investment time period>,
            "purchaseDatetime": <datetime of purchase>,
            "status": <ACTIVE or INACTIVE>
        }
    ]
}
```
> Where
> * `bundles` is a list of all the customers bundles

- - - - -

## _[POST]_ `/account/wallets/<wallet_adddress>`
### Request
```json
{
    "customerID": <customer ID>,
    "walletAddress": <the wallet address for which details are requested>
}
```
### Response
```json
{
    "status": {
        "statusCode": "SUCCESS",
        "statusMessage": "Details for wallet requested"
    },
    "wallet": {
            "walletAddress": <wallet address>,
            "customerID": <customer ID>,
            "initialBalance": <the balance at time of purchase>,
            "currentBalance": <the current balance>,
            "cryptocurrencyCode": <the wallets cryptocurrency>,
            "holdingPeriod": <investment time period>
    },
    "walletTransactions": [
        {
            "transactionID": <transaction ID>,
            "transactionDateTime": <datetime of transaction>,
            "chargeApplied": <charges applied for selling before holding period expires>,
            "amount": <amount invested>,
            "action": <BUY or SELL>,
            "cardNumber": <card number masked>,
            "expiry": <expiry date masked>,
            "unitsSold": <sold cryptocurrency>,
            "initialRate": <rate at which the cryptocurrency was bought>
        }
    ]
}
```
> Where
> * `walletTransactions` is a list of all transactions carried out on that wallet

- - - - -

##




