from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import Client
from ...models.check_account_transaction_response_model import (
    CheckAccountTransactionResponseModel,
)
from ...models.check_account_transaction_update_model import (
    CheckAccountTransactionUpdateModel,
)
from ...types import Response


def _get_kwargs(
    check_account_transaction_id: int,
    *,
    client: Client,
    json_body: CheckAccountTransactionUpdateModel,
) -> Dict[str, Any]:
    url = "{}/CheckAccountTransaction/{checkAccountTransactionId}".format(
        client.base_url, checkAccountTransactionId=check_account_transaction_id
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "method": "put",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "follow_redirects": client.follow_redirects,
        "json": json_json_body,
    }


def _parse_response(
    *, client: Client, response: httpx.Response
) -> Optional[Union[Any, CheckAccountTransactionResponseModel]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = CheckAccountTransactionResponseModel.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = cast(Any, None)
        return response_400
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = cast(Any, None)
        return response_401
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = cast(Any, None)
        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[Union[Any, CheckAccountTransactionResponseModel]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    check_account_transaction_id: int,
    *,
    client: Client,
    json_body: CheckAccountTransactionUpdateModel,
) -> Response[Union[Any, CheckAccountTransactionResponseModel]]:
    """Update an existing check account transaction

     Update a check account transaction

    Args:
        check_account_transaction_id (int):
        json_body (CheckAccountTransactionUpdateModel): CheckAccountTransaction model. Responsible
            for the transactions on payment accounts.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, CheckAccountTransactionResponseModel]]
    """

    kwargs = _get_kwargs(
        check_account_transaction_id=check_account_transaction_id,
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    check_account_transaction_id: int,
    *,
    client: Client,
    json_body: CheckAccountTransactionUpdateModel,
) -> Optional[Union[Any, CheckAccountTransactionResponseModel]]:
    """Update an existing check account transaction

     Update a check account transaction

    Args:
        check_account_transaction_id (int):
        json_body (CheckAccountTransactionUpdateModel): CheckAccountTransaction model. Responsible
            for the transactions on payment accounts.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, CheckAccountTransactionResponseModel]
    """

    return sync_detailed(
        check_account_transaction_id=check_account_transaction_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    check_account_transaction_id: int,
    *,
    client: Client,
    json_body: CheckAccountTransactionUpdateModel,
) -> Response[Union[Any, CheckAccountTransactionResponseModel]]:
    """Update an existing check account transaction

     Update a check account transaction

    Args:
        check_account_transaction_id (int):
        json_body (CheckAccountTransactionUpdateModel): CheckAccountTransaction model. Responsible
            for the transactions on payment accounts.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, CheckAccountTransactionResponseModel]]
    """

    kwargs = _get_kwargs(
        check_account_transaction_id=check_account_transaction_id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    check_account_transaction_id: int,
    *,
    client: Client,
    json_body: CheckAccountTransactionUpdateModel,
) -> Optional[Union[Any, CheckAccountTransactionResponseModel]]:
    """Update an existing check account transaction

     Update a check account transaction

    Args:
        check_account_transaction_id (int):
        json_body (CheckAccountTransactionUpdateModel): CheckAccountTransaction model. Responsible
            for the transactions on payment accounts.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, CheckAccountTransactionResponseModel]
    """

    return (
        await asyncio_detailed(
            check_account_transaction_id=check_account_transaction_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
