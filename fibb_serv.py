from aiohttp import web


async def help(request):
    return web.Response(text="""
       Go to Hell
       ... or use:   /fib/{fib_index} \n
       """)


async def fib(request):
    n = int(request.match_info.get('n', -1))
    if n == -1:
        return web.Response(text=f"Hot to hell or provide fib_index")
    a, b = 0, 1
    for i in range(0, n):
        a, b = b, a + b
    # return web.Response(text=f"{a}")
    data = {'desc': 'fibonacci number',
            'index': n,
            'value': a
            }
    return web.json_response(data)

app = web.Application()
app.add_routes([web.get(r'/', help),
                web.get(r'/fib/{n:\d+}', fib)])

if __name__ == '__main__':
    web.run_app(app)
