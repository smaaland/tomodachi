import asyncio
from tomodachi.discovery.registry import Registry
from tomodachi.transport.http import http, http_error


class ExampleHttpService(object):
    name = 'example_http_service'
    log_level = 'INFO'
    discovery = [Registry]
    options = {
        'http': {
            'port': 4711,
            'content_type': 'text/plain; charset=utf-8',
            'access_log': True
        }
    }

    @http('GET', r'/example/?')
    async def example(self, request):
        await asyncio.sleep(1)
        return '友達'  # tomodachi

    @http('GET', r'/example/(?P<id>[^/]+?)/?')
    async def example_with_id(self, request, id):
        return '友達 (id: {})'.format(id)

    @http_error(status_code=404)
    async def error_404(self, request):
        return 'error 404'
