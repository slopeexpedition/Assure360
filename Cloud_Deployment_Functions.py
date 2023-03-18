import json
import requests


def InsuredSupplyChain(db_params):
    query_type = db_params['queryType']
    url = "https://apacuat.chubbdigital.com/enterprise.operations.authorization"
    data=[]
    payload = ""
    headers = {
    'App_ID': '39730703-2c37-457c-bfed-2ea4cd6654da',
    'App_Key': '7eNLlZNx.r59P~4U44k1-nT4ObWJ_TM._C',
    'Resource': '95f3f01c-a430-467f-ac05-f8dd75c7affb',
    'apiVersion': '1',
    'Cookie': 'crux.api.sessionId=s%3ADRaZrjFxmarTjNvsB10oMOOucpccpNbp.pOW0WgLDIUypt6oUXTwoYPFf2%2FRh9En%2FudkNCDW2Whg'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    res=json.loads(response.text)
    access_token=res["access_token"]
    print(access_token)
    if query_type == "campaign_summary":
        campaign_id = db_params['campaign_id']
        print("enter")
        url = "https://apacuat.chubbdigital.com/sales.chubbstudio-sales/campaigns/summary"

        payload={}
        headers = {
        'Ocp-Apim-Subscription-Key': '445a83b5ee1b44d49443379fcb7259ae',
        'apiVersion': '1',
        'country': 'sg',
        'partner': 'partner-company',
        'product': 'demo',
        'campaign': campaign_id,
        'campaign_id': campaign_id,
        'Authorization': 'Bearer '+ access_token,
        'Cookie': 'crux.api.sessionId=s%3ADRaZrjFxmarTjNvsB10oMOOucpccpNbp.pOW0WgLDIUypt6oUXTwoYPFf2%2FRh9En%2FudkNCDW2Whg'
        }

        response = requests.request("POST", url, headers=headers, data=payload)
        json_res=json.loads(response.text)
        insurance_type=db_params['insuranceType']
        print(insurance_type)
        offer_type=json_res["offers"]
        for one in offer_type:
            if(one['name']==insurance_type):
                for coverage in one['coverages']:
                    for amount in coverage['coverage_amounts']:
                        amount['name']=json_res["name"]
                        amount['coverage_id']=coverage['coverage_id']
                        amount['coverage_type']=coverage['name']
                        amount['campaign_id']=json_res["campaign_id"]
                        amount['offer_id']=one["offer_id"]
                        amount['type']=one["name"]
                        data.append(amount)

    if query_type=="Register_policy":
        url = "https://apacuat.chubbdigital.com/sales.chubbstudio-sales/sales"
        campaign_id = db_params['campaign_id']
        upd={}
        if campaign_id=='web-sg-acc':
            upd={
                    "request_date": "2022/10/01",
                    "channel": "internet",
                    "effective_date": "2022/10/01",
                    "contract_holders": [
                        {
                        "first_name": "John",
                        "last_name": "Doe",
                        "relationship": "self",
                        "gender": "male",
                        "date_of_birth": "1980/01/01",
                        "identification": {
                            "type_of_id": "Others",
                            "id_value": "1234567890"
                        },
                        "home_address": {
                            "address_lines": [
                            "123 Street",
                            "Building"
                            ],
                            "city": "Singapore",
                            "postal_code": "012345",
                            "country": "sg"
                        },
                        "mailing_address_same_as_home": True,
                        "phone": [
                            {
                            "phone_number": "+65 12 345 67 89",
                            "type": "personal"
                            }
                        ],
                        "email": "john.doe@chubb.com"
                        }
                    ],
                    "insureds": [
                        {
                        "insured": {
                            "first_name": "John",
                            "last_name": "Doe",
                            "relationship": "self",
                            "gender": "male",
                            "date_of_birth": "1980/01/01",
                            "identification": {
                            "type_of_id": "Others",
                            "id_value": "1234567890"
                            },
                            "home_address": {
                            "address_lines": [
                                "123 Street",
                                "Building"
                            ],
                            "city": "Singapore",
                            "postal_code": "012345",
                            "country": "sg"
                            },
                            "mailing_address_same_as_home": True,
                            "phone": [
                            {
                                "phone_number": "+65 12 345 67 89",
                                "type": "personal"
                            }
                            ],
                            "email": "john.doe@chubb.com",
                            "beneficiaries": [
                            {
                                "first_name": "Jane",
                                "last_name": "Doe",
                                "relationship": "spouse",
                                "gender": "female",
                                "date_of_birth": "1990/01/01",
                                "identification": {
                                "type_of_id": "Others",
                                "id_value": "1234567890"
                                },
                                "home_address": {
                                "address_lines": [
                                    "123 Street",
                                    "Building"
                                ],
                                "city": "Singapore",
                                "postal_code": "012345",
                                "country": "sg"
                                },
                                "mailing_address_same_as_home": True,
                                "phone": [
                                {
                                    "phone_number": "+65 12 345 67 89",
                                    "type": "personal"
                                }
                                ],
                                "email": "jane.doe@chubb.com"
                            }
                            ]
                        }
                        }
                    ],
                    "insurance_selections": {
                        "campaign_id": "web-sg-acc",
                        "offer_id": "1",
                        "offer_questions": [
                        {
                            "question_id": "coverage_type",
                            "answer": "couple"
                        },
                        {
                            "question_id": "payment_frequency",
                            "answer": 12
                        }
                        ],
                        "additional_coverages": [],
                        "payment_type": "credit_card",
                        "payment_details": {
                        "payment_frequency": 12,
                        "card_type": "visa",
                        "cardholder_name": "John Doe",
                        "payment_token": "fake-three-d-secure-visa-full-authentication-nonce",
                        "exp_month": "07",
                        "exp_year": "30"
                        }
                    },
                    "disclosure_consents": [
                        {
                        "disclosure_id": "123a456b7d89ef0a1b2345c0",
                        "disclosure_consent": True
                        },
                        {
                        "disclosure_id": "123a456b7d89ef0a1b2345c1",
                        "disclosure_consent": True
                        },
                        {
                        "disclosure_id": "123a456b7d89ef0a1b2345c2",
                        "disclosure_consent": True
                        }
                    ]
                    }
        elif campaign_id=='web-sg-val':
            upd={
                    "request_date": "2022/10/01",
                    "channel": "internet",
                    "effective_date": "2022/10/01",
                    "contract_holders": [
                        {
                        "first_name": "John",
                        "last_name": "Doe",
                        "relationship": "self",
                        "gender": "male",
                        "date_of_birth": "1980/01/01",
                        "identification": {
                            "type_of_id": "Others",
                            "id_value": "1234567890"
                        },
                        "home_address": {
                            "address_lines": [
                            "123 Street",
                            "Building"
                            ],
                            "city": "Singapore",
                            "postal_code": "012345",
                            "country": "sg"
                        },
                        "mailing_address_same_as_home": True,
                        "phone": [
                            {
                            "phone_number": "+65 12 345 67 89",
                            "type": "personal"
                            }
                        ],
                        "email": "john.doe@chubb.com"
                        }
                    ],
                    "insureds": [
                        {
                        "insured": {
                            "first_name": "John",
                            "last_name": "Doe",
                            "relationship": "self",
                            "gender": "male",
                            "date_of_birth": "1980/01/01",
                            "identification": {
                            "type_of_id": "Others",
                            "id_value": "1234567890"
                            },
                            "home_address": {
                            "address_lines": [
                                "123 Street",
                                "Building"
                            ],
                            "city": "Singapore",
                            "postal_code": "012345",
                            "country": "sg"
                            },
                            "mailing_address_same_as_home": True,
                            "phone": [
                            {
                                "phone_number": "+65 12 345 67 89",
                                "type": "personal"
                            }
                            ],
                            "email": "john.doe@chubb.com"
                        }
                        }
                    ],
                    "insured_items": {
                        "valuables_info": {
                        "valuables": [
                            {
                            "type": "watch",
                            "make": "Oris",
                            "model": "Artelier",
                            "purchase_date": "2019/12/31",
                            "cost": "2999",
                            "storage_location": "home",
                            "serial_number": "01234567890"
                            }
                        ]
                        }
                    },
                    "insurance_selections": {
                        "campaign_id": "web-sg-val",
                        "offer_id": "1",
                        "offer_questions": [
                        {
                            "question_id": "coverage_type",
                            "answer": "individual"
                        },
                        {
                            "question_id": "payment_frequency",
                            "answer": 12
                        }
                        ],
                        "additional_coverages": [],
                        "payment_type": "credit_card",
                        "payment_details": {
                        "payment_frequency": 12,
                        "card_type": "visa",
                        "cardholder_name": "John Doe",
                        "payment_token": "fake-three-d-secure-visa-full-authentication-nonce",
                        "exp_month": "07",
                        "exp_year": "30"
                        }
                    },
                    "disclosure_consents": [
                        {
                        "disclosure_id": "123a456b7d89ef0a1b2345c0",
                        "disclosure_consent": True
                        },
                        {
                        "disclosure_id": "123a456b7d89ef0a1b2345c1",
                        "disclosure_consent": True
                        },
                        {
                        "disclosure_id": "123a456b7d89ef0a1b2345c2",
                        "disclosure_consent": True
                        }
                    ]
                    }
        else:
            upd={
                    "request_date": "2022/10/01",
                    "channel": "internet",
                    "effective_date": "2022/10/01",
                    "contract_holders": [
                        {
                        "first_name": "John",
                        "last_name": "Doe",
                        "relationship": "self",
                        "gender": "male",
                        "date_of_birth": "1980/01/01",
                        "identification": {
                            "type_of_id": "Others",
                            "id_value": "1234567890"
                        },
                        "home_address": {
                            "address_lines": [
                            "123 Street",
                            "Building"
                            ],
                            "city": "Singapore",
                            "postal_code": "012345",
                            "country": "sg"
                        },
                        "mailing_address_same_as_home": True,
                        "phone": [
                            {
                            "phone_number": "+65 12 345 67 89",
                            "type": "personal"
                            }
                        ],
                        "email": "john.doe@chubb.com"
                        }
                    ],
                    "insureds": [
                        {
                        "insured": {
                            "first_name": "John",
                            "last_name": "Doe",
                            "relationship": "self",
                            "gender": "male",
                            "date_of_birth": "1980/01/01",
                            "identification": {
                            "type_of_id": "Others",
                            "id_value": "1234567890"
                            },
                            "home_address": {
                            "address_lines": [
                                "123 Street",
                                "Building"
                            ],
                            "city": "Singapore",
                            "postal_code": "012345",
                            "country": "sg"
                            },
                            "mailing_address_same_as_home": True,
                            "phone": [
                            {
                                "phone_number": "+65 12 345 67 89",
                                "type": "personal"
                            }
                            ],
                            "email": "john.doe@chubb.com"
                        }
                        }
                    ],
                    "insured_items": {
                        "gadget_info": {
                        "gadgets": [
                            {
                            "type": "phone",
                            "make": "iPhone",
                            "model": "12 Pro Max",
                            "storage": "256GB",
                            "purchase_date": "2020/12/31",
                            "imei": "123456789012345"
                            }
                        ]
                        }
                    },
                    "insurance_selections": {
                        "campaign_id": "web-sg-gad",
                        "offer_id": "1",
                        "offer_questions": [
                        {
                            "question_id": "coverage_type",
                            "answer": "individual"
                        },
                        {
                            "question_id": "payment_frequency",
                            "answer": 12
                        }
                        ],
                        "additional_coverages": [],
                        "payment_type": "credit_card",
                        "payment_details": {
                        "payment_frequency": 12,
                        "card_type": "visa",
                        "cardholder_name": "John Doe",
                        "payment_token": "fake-three-d-secure-visa-full-authentication-nonce",
                        "exp_month": "07",
                        "exp_year": "30"
                        }
                    },
                    "disclosure_consents": [
                        {
                        "disclosure_id": "123a456b7d89ef0a1b2345c0",
                        "disclosure_consent": True
                        },
                        {
                        "disclosure_id": "123a456b7d89ef0a1b2345c1",
                        "disclosure_consent": True
                        },
                        {
                        "disclosure_id": "123a456b7d89ef0a1b2345c2",
                        "disclosure_consent": True
                        }
                    ]
                    }
        payload = json.dumps(upd)
        headers = {
        'Ocp-Apim-Subscription-Key': '445a83b5ee1b44d49443379fcb7259ae',
        'apiVersion': '1',
        'country': 'sg',
        'partner': 'partner-company',
        'product': 'demo',
        'campaign': campaign_id,
        'Authorization': 'Bearer '+ access_token,
        'Content-Type': 'application/json',
        'Cookie': 'crux.api.sessionId=s%3ADRaZrjFxmarTjNvsB10oMOOucpccpNbp.pOW0WgLDIUypt6oUXTwoYPFf2%2FRh9En%2FudkNCDW2Whg'
        }

        response = requests.request("POST", url, headers=headers, data=payload)
        data=json.loads(response.text)

    return data