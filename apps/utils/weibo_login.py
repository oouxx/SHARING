def get_auth_url():
    weibo_auth_url = "https://api.weibo.com/oauth2/authorize"
    # 回调地址
    redirect_url = ""
    auth_url = weibo_auth_url+"?client_id={client_id}&redirect_url={re_url}".format(client_id="", re_url=redirect_url)


def get_access_token(code=""):
    # code是新浪微博生成的
    access_token_url = "https://api.weibo.com/oauth2/access_token"
    import requests
    re_dict = requests.post(access_token_url, data={
        "client_id": "",
        "client_secret": "",
        "code": code,
        "redirect_url": ""
    })