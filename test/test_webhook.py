import responses
from myiokalib.resources.webhook import Webhook, BASE_URL

@responses.activate
def test_get_webhooks():
    responses.add(
        responses.GET,
        f'{BASE_URL}/webhooks',
        json=[{'url': 'http://example.com', 'id': 'webhook_id'}],
        status=200
    )
    webhook = Webhook()
    result = webhook.get_webhooks(api_key='test_api_key')
    assert result == [{'url': 'http://example.com', 'id': 'webhook_id'}]


@responses.activate
def test_create_webhook():
    responses.add(
        responses.POST,
        f'{BASE_URL}/webhooks',
        json={'url': 'http://example.com', 'id': 'webhook_id'},
        status=201
    )
    webhook = Webhook()
    result = webhook.create_webhook(api_key='test_api_key', url='http://example.com', events=['ORDER_EXPIRED'])
    assert result == {'url': 'http://example.com', 'id': 'webhook_id'}


@responses.activate
def test_get_webhook_by_id():
    responses.add(
        responses.GET,
        f'{BASE_URL}/webhooks/webhook_id',
        json={'url': 'http://example.com', 'id': 'webhook_id'},
        status=200
    )
    webhook = Webhook()
    result = webhook.get_webhook_by_id(api_key='test_api_key', webhook_id='webhook_id')
    assert result == {'url': 'http://example.com', 'id': 'webhook_id'}


@responses.activate
def test_delete_webhook_by_id():
    responses.add(
        responses.DELETE,
        f'{BASE_URL}/webhooks/webhook_id',
        status=204
    )
    webhook = Webhook()
    result = webhook.delete_webhook_by_id(api_key='test_api_key', webhook_id='webhook_id')
    assert result == "Successfully deleted"


@responses.activate
def test_update_webhook_by_id():
    responses.add(
        responses.PATCH,
        f'{BASE_URL}/webhooks/webhook_id',
        json={'url': 'http://example.com', 'id': 'webhook_id'},
        status=200
    )
    webhook = Webhook()
    result = webhook.update_webhook_by_id(api_key='test_api_key', webhook_id='webhook_id', url='http://example.com', events=['ORDER_EXPIRED'])
    assert result == {'url': 'http://example.com', 'id': 'webhook_id'}
