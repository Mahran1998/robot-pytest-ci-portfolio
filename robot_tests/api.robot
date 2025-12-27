*** Settings ***
Library           RequestsLibrary
Library           Collections

Suite Setup       Create Session    api    %{BASE_URL}    verify=${True}

*** Variables ***
${BASE_URL}       http://127.0.0.1:8000

*** Test Cases ***
Health Endpoint Returns OK
    ${resp}=    GET On Session    api    /health
    Should Be Equal As Integers   ${resp.status_code}    200
    ${json}=    Set Variable      ${resp.json()}
    Dictionary Should Contain Key    ${json}    status
    Should Be Equal    ${json}[status]    ok

Add Endpoint Returns Correct Sum
    ${resp}=    GET On Session    api    /calc/add    params=a=5&b=7
    Should Be Equal As Integers   ${resp.status_code}    200
    ${json}=    Set Variable      ${resp.json()}
    Should Be Equal As Integers   ${json}[sum]    12

Create Item Returns 201 And Fields
    ${body}=    Create Dictionary    name=robot-item    price=20.5
    ${resp}=    POST On Session    api    /items    json=${body}
    Should Be Equal As Integers   ${resp.status_code}    201
    ${json}=    Set Variable      ${resp.json()}
    Dictionary Should Contain Key    ${json}    id
    Should Be Equal    ${json}[name]    robot-item
    Should Be Equal As Numbers    ${json}[price]    20.5
    Dictionary Should Contain Key    ${json}    tax

Negative Price Returns 400
    ${body}=    Create Dictionary    name=bad    price=-1
    ${resp}=    POST On Session    api    /items    json=${body}
    Should Be Equal As Integers   ${resp.status_code}    400
