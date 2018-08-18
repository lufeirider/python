import aiohttp
import asyncio
import logging
import requests
from lxml import etree

cookes_dict = ""

def get_cookie():
    global cookes_dict
    with requests.session() as session:
        html_login = session.get('https://github.com/login').text

        try:
            html = etree.HTML(html_login)
            authenticity_token_list = html.xpath('//*[@id="login"]/form/input[2]/@value')

            if len(authenticity_token_list)>0: authenticity_token = authenticity_token_list[0]

            post_form = {
                'commit': 'Sign in',
                'utf8': '✓',
                'authenticity_token':authenticity_token,
                'login':'lufeirider',
                'password':'xxxxxxxxxxxx'
            }

            session.post('https://github.com/session', data=post_form)

            cookies = {
                'user_session': session.cookies.get('user_session'),
                'dotcom_user': session.cookies.get('dotcom_user'),
                '_octo' : session.cookies.get('_octo')
            }

            cookes_dict = cookies
            logging.warning(cookies)
        except Exception as error:
            logging.error("not math authenticity_token:{}".format(error))

async def fetch_content(page):
    async with aiohttp.ClientSession(cookies = cookes_dict,connector = aiohttp.TCPConnector(verify_ssl = False)) as session:
        async with session.get('https://github.com/search?p={}&q=%22360%40.net%22&type=Code'.format(page)) as resp:
            html = await resp.text()
            print(html)
            logging.warning(resp.status)


if __name__ == '__main__':
    get_cookie()

    event_loop = asyncio.get_event_loop()
    tasks = [fetch_content(page) for page in range(1,101)]
    results = event_loop.run_until_complete(asyncio.gather(*tasks))
