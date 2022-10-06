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
        "statusMessage" : The reason for the failure
    }
}
```
- - - - -
# User registration, signing in and signing out
- - - - -

## _[POST]_ `/sign-up` 
### Request
```json
{
    "emailAddress": email address,
    "password": plain text password,
    "name": name
} 
```
### Response
```json
{
    "status": {
        "statusCode": "SUCCESS",
        "statusMessage": "Successfully registered"
    },
    "name": name,
    "emailAddress": email address
}
```

- - - - -

## _[POST]_ `/sign-in`
### Request
```json
{
    "emailddress": email address,
    "password": plain text password
} 
```
### Reponse
```json
{
    "status": {
        "statusCode": "SUCCESS",
        "statusMessage": "Successfully signed in"
    },
    "name": customer name,
    "emailAddress": email address,
    "currentSignInDatetime": current sign in datetime,
    "previousSignInDatetime": last sign in datetime
}
```

- - - - -

## _[POST]_ `/sign-out`
> The request uses the token present in the authorization header 
> to end the session. No request JSON is required.

- - - - -
# Customer profile
- - - - -

## _[GET]_ `/profile/customer-details`
### Request
> The token present in the authorization header is the 
> method to confirm access to this route  
### Response
```json
{
    "status": {
        "statusCode": "SUCCESS",
        "statusMessage": "The customers details"
    },
    "customerID": Customers ID,
    "registerDatetime": datetime of account creation,
    "emailAddress": email address,
    "previousSignInDatetime": last sign in datetime,
    "currentSignInDatetime": current sign in datetime,
    "name": name
}
```

- - - - -

## _[POST]_ `/profile/change-password`
### Request
```json
{
    "currentPassword": current password,
    "newPassword": new password
}
```
> The token present in the authorization header is the method 
> to confirm access to this route  
### Response
```json
{
    "status": {
        "statusCode": "SUCCESS",
        "statusMessage": "Successfully changed password for customer. You will be signed out. Sign in with new password"
    },
    "customerID": customer ID
}
```

- - - - -

## _[POST]_ `/profile/change-emailaddress`
### Request
```json
{
    "currentPassword": current password,
    "newEmailAddress": new email address
}
```
> The token present in the authorization header is the method 
> to confirm access to this route  
### Response
```json
{
    "status": {
        "statusCode": "SUCCESS",
        "statusMessage": "Successfully changed email address for customer"
    },
    "customerID": customer ID
}
```

- - - - -
# Items available to purchase
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
            "cryptocurrencyCode": code,
            "cryptocurrencyName": name
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
            "bundleName": name of the bundle,
            "minimumHoldingPeriod": in monthes,
            "bundleCryptocurrencies": [
                {
                    "cryptocurrencyCode": code,
                    "cryptocurrencyName": name,
                    "percentage": % of the bundle
                }
            ]
        }
    ]
}
```
> Where
> * `availableBundles` is a list of bundles
> * `bundleCryptocurrencies` is a list of the cryptocurrencies in that bundle
### Bundles 

| ID  | code | percent | minimum holding |
|:----|:-----|--------:|----------------:|
| 1   | btc  |      50 |               6 |
| 1   | eth  |      50 |               6 |
| 2   | bch  |      25 |              12 |
| 2   | eth  |      15 |              12 |
| 2   | xrp  |      15 |              12 |
| 2   | ltc  |      25 |              12 |
| 2   | xmr  |      20 |              12 |
| 3   | doge |      20 |              12 |
| 3   | shib |      20 |              12 |
| 3   | etc  |      30 |              12 |
| 3   | ape  |      30 |              12 |
| 4   | link |      20 |              12 |
| 4   | mana |      20 |              12 |
| 4   | qnt  |      20 |              12 |
| 4   | wbtc |      20 |              12 |
| 4   | usdc |      20 |              12 |
| 5   | dai  |      20 |              12 |
| 5   | bnb  |      20 |              12 |
| 5   | sol  |      20 |              12 |
| 6   | algo |      20 |              18 |     
| 6   | busd |      20 |              18 |
| 6   | flow |      20 |              18 |
| 6   | fil  |      20 |              18 |
| 6   | dot  |      20 |              18 |

- - - - -
# Customer account
- - - - -

## _[GET]_ `/account/wallets`
### Request
```json
{
    "customerID": customerID
}
```
> The token present in the authorization header is the 
> method to confirm access to this route  
### Response
```json
{
    "status": {
        "statusCode": "SUCCESS",
        "statusMessage": "All of the customers wallets"
    },
    "wallets": [
        {
            "walletAddress": wallet address,
            "customerID": customer ID,
            "initialBalance": the balance at time of purchase,
            "currentBalance": the current balance,
            "cryptocurrencyCode": the wallets cryptocurrency,
            "holdingPeriod": investment time period
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
    "customerID": customerID
}
```
> The token present in the authorization header is the 
> method to confirm access to this route 
### Response
```json
{
    "status": {
        "statusCode": "SUCCESS",
        "statusMessage": "All of the customers bundles"
    },
    "bundles": [
        {
            "bundleAddress": bundle address,
            "bundleID": bundle ID,
            "customerID": customer ID,
            "amount": amount invested,
            "holdingPeriod": investment time period,
            "purchaseDatetime": datetime of purchase,
            "status": ACTIVE or INACTIVE
        }
    ]
}
```
> Where
> * `bundles` is a list of all the customers bundles

- - - - -

## _[POST]_ `/account/wallets/wallet-address`
### Request
```json
{
    "customerID": customer ID,
    "walletAddress": the wallet address for which details are requested
}
```
> The token present in the authorization header is the 
> method to confirm access to this route 
### Response
```json
{
    "status": {
        "statusCode": "SUCCESS",
        "statusMessage": "Details for wallet requested"
    },
    "wallet": {
            "walletAddress": wallet address,
            "customerID": customer ID,
            "initialBalance": the balance at time of purchase,
            "currentBalance": the current balance,
            "cryptocurrencyCode": the wallets cryptocurrency,
            "holdingPeriod": investment time period
    },
    "walletTransactions": [
        {
            "transactionID": transaction ID,
            "transactionDateTime": datetime of transaction,
            "chargeApplied": charges applied for selling before holding period expires,
            "amount": amount invested,
            "action": BUY or SELL,
            "cardNumber": card number masked,
            "expiry": expiry date masked,
            "unitsSold": sold cryptocurrency,
            "initialRate": rate at which the cryptocurrency was bought
        }
    ]
}
```
> Where
> * `walletTransactions` is a list of all transactions carried out on 
> that wallet

- - - - -

## _[POST]_ `/account/bundles/bundle-address`
### Request
```json
{
    "customerID": customer ID,
    "bundleAddress": bundle address
}
```
> The token present in the authorization header is the 
> method to confirm access to this route 
### Response
```json

{
    "status": {
        "statusCode": "SUCCESS",
        "statusMessage": "Details for the bundle requested"
    },
    "bundle": {
        "bundleAddress": bundle address,
        "bundleID": bundle ID,
        "customerID": customer ID,
        "amount": amount invested,
        "holdingPeriod": investment time period,
        "purchaseDatetime": datetime of purchase,
        "status": ACTIVE or INACTIVE
    },
    "bundleTransactions": [ 
        {
            "transactionID": transaction ID,
            "transactionDateTime": datetime of transaction,
            "chargeApplied": charges applied for selling before holding period expires,
            "amount": amount invested,
            "action": BUY or SELL,
            "cardNumber": card number masked,
            "expiry": expiry date masked,
            "initialRate": rate at which the cryptocurrency was bought
        }
    ]
}
```
> Where
> * `bundleTransactions` is a list of all transactions carried out on 
> that wallet

- - - - -
#  Purchasing
- - - - -

## _[POST]_ `/account/purchase/wallet`
### Request
```json
{
    "customerID": customerID,
    "initialBalance": initial balance,
    "cryptocurrencyCode": cryptocurrency code,
    "holdingPeriod": holding period,
    "initialRate": initial rate,
    "amount": amount,
    "cardNumber": card number,
    "expiry": expiry
}
```
### Response
```json
{
    "status": {
        "statusCode": "SUCCESS",
        "statusMessage": "Wallet purchased"
    },
    "wallet": {
        "walletAddress": wallet address,
        "customerID": customer ID,
        "initialBalance": the balance at time of purchase,
        "currentBalance": the current balance,
        "cryptocurrencyCode": the wallets cryptocurrency,
        "holdingPeriod": investment time period
    },
    "walletTransaction": {
        "transactionID": transaction ID,
        "transactionDateTime": datetime of transaction,
        "chargeApplied": charges applied for selling before holding period expires,
        "amount": amount invested,
        "action": BUY or SELL,
        "cardNumber": card number masked,
        "expiry": expiry date masked,
        "unitsSold": sold cryptocurrency,
        "initialRate": rate at which the cryptocurrency was bought
    }
}
```
> Where
> * `walletTransaction` is the details of that particular transaction carried out 

- - - - -

## _[POST]_ `/account/sell/wallet`
### Request
```json
{
    "walletAddress": wallet address,
    "customerID": customerID,
    "initialRate": initial rate,
    "amount": amount,
    "cardNumber": card number,
    "expiry": expiry,
    "unitsSold": units sold
}
```
### Response
```json
{
    "status": {
        "statusCode": "SUCCESS",
        "statusMessage": "Successfully sold wallet"
    },
    "wallet": {
        "walletAddress": wallet address,
        "customerID": customer ID,
        "initialBalance": initial balance,
        "currentBalance": current balance,
        "cryptocurrencyCode": cryptocurrency code,
        "holdingPeriod": holdingPeriod
    },
    "walletTransaction": {
        "transactionID": transaction ID,
        "transactionDateTime": transaction datetime,
        "chargeApplied": charge applied,
        "amount": amount,
        "action": action,
        "cardNumber": card number,
        "expiry": expiry,
        "unitsSold": unitsSold,
        "initialRate": initial rate
    }
}
```

- - - - -

## _[POST]_ `/account/purchase/bundle`
### Request
```json
{
    "customerID": customerID,
    "bundleID": bundle ID,
    "holdingPeriod": holding period,
    "initialRate": initial rate,
    "amount": amount,
    "cardNumber": card number,
    "expiry": expiry
}
```
### Response
```json
{
    "status": {
        "statusCode": "SUCCESS",
        "statusMessage": "Bundle purchased"
    },
    "bundle": {
        "bundleAddress": bundle address,
        "customerID": customer ID,
        "bundleID": bundle ID,
        "purchaseDatetime": purchase datetime,
        "status": status,
        "holdingPeriod": investment time period
    },
    "bundleTransaction": {
        "transactionID": transaction ID,
        "transactionDateTime": datetime of transaction,
        "chargeApplied": charges applied for selling before holding period expires,
        "amount": amount invested,
        "action": BUY or SELL,
        "cardNumber": card number masked,
        "expiry": expiry date masked,
        "initialRate": rate at which the cryptocurrency was bought
    }
}
```
> Where
> * `bundleTransaction` is the details of that particular transaction carried out 

- - - - -

## _[POST]_ `/account/sell/bundle`
### Request
```json
{
    "bundleAddress": bundle address,
    "customerID": customer ID,
    "bundleID": bundle ID,
    "initialRate": initial rate,
    "amount": amount,
    "cardNumber": card number,
    "expiry": expiry
}
```
### Response
```json
{
    "status": {
        "statusCode": "SUCCESS",
        "statusMessage": "Successfully sold bundle"
    },
    "bundle": {
        "bundleAddress": bundle address,
        "customerID": customer ID,
        "bundleID": bundle ID,
        "purchaseDatetime": purchase datetime,
        "status": status,
        "holdingPeriod": holdingPeriod
    },
    "bundleTransaction": {
        "transactionID": transaction ID,
        "transactionDateTime": transaction datetime,
        "chargeApplied": charge applied,
        "amount": amount,
        "action": action,
        "cardNumber": card number,
        "expiry": expiry,
        "initialRate": initial rate
    }
}
```

